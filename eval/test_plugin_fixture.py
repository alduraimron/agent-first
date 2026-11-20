"""Model-free fixture plumbing tests; native discovery is checked separately."""
from contextlib import closing
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

from plugin_fixture import PluginFixture, backup_database, run_command
from run import case_policy, policy_overlays, save_json


class PluginFixtureTests(unittest.TestCase):
    def fixture(self, root, inherited=None):
        workspace, output = root / 'workspace', root / 'output'
        workspace.mkdir()
        output.mkdir()
        return PluginFixture('omp', workspace, output, inherited=inherited)

    def test_environment_replaces_user_state_and_clears_session_inheritance(self):
        inherited = {'PATH': '/usr/bin', 'HOME': '/operator', 'OMP_PROFILE': 'personal',
                     'PI_PROFILE': 'personal', 'PI_CONFIG_DIR': '/operator/config',
                     'PI_CONFIG_FILES': '/operator/config.yml', 'PI_SESSION_ID': 'parent',
                     'PI_SESSION_DIR': '/operator/sessions', 'OMP_SESSION_FILE': 'parent.jsonl',
                     'PI_CODING_AGENT_DIR': '/operator/agent', 'PI_TOOL_CALL_ID': 'call',
                     'CLAUDE_CONFIG_DIR': '/operator/claude', 'OPENAI_API_KEY': 'synthetic',
                     'XDG_DATA_HOME': '/operator/data'}
        original = dict(inherited)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = self.fixture(root, inherited)
            self.assertEqual(inherited, original)
            self.assertEqual(fixture.env['HOME'], str(fixture.home))
            self.assertEqual(fixture.env['PI_CONFIG_DIR'], '.omp')
            self.assertEqual(Path(fixture.env['HOME']) / fixture.env['PI_CONFIG_DIR'], fixture.config)
            for key in ('OMP_PROFILE', 'PI_PROFILE', 'PI_CONFIG_FILES', 'PI_SESSION_ID',
                        'PI_SESSION_DIR', 'OMP_SESSION_FILE', 'PI_CODING_AGENT_DIR',
                        'PI_TOOL_CALL_ID', 'CLAUDE_CONFIG_DIR'):
                self.assertNotIn(key, fixture.env)
            self.assertEqual(fixture.env['OPENAI_API_KEY'], 'synthetic')
            for kind in ('CONFIG', 'DATA', 'STATE', 'CACHE'):
                path = Path(fixture.env['XDG_' + kind + '_HOME'])
                self.assertTrue(path.is_relative_to(fixture.state))
                self.assertTrue(path.is_dir())
                self.assertFalse((path / 'omp').exists())
            argv = fixture.argv('--print', '--', 'literal; not a shell')
            self.assertEqual(argv, ['omp', '--cwd', str(fixture.workspace),
                                    '--print', '--', 'literal; not a shell'])
            self.assertNotIn('--profile', argv)
            self.assertNotIn('--append-system-prompt', argv)
            self.assertEqual(fixture.evidence()['scope'], 'project')

    def test_run_command_retains_real_argv_output_failure_and_cwd(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            argv = [sys.executable, '-c',
                    'import os,sys; print(os.getcwd()); print(sys.argv[1]); '
                    'print("failure detail", file=sys.stderr); sys.exit(7)', 'literal; argument']
            record = run_command(argv, root, root, 'child', 10, dict(os.environ))
            self.assertEqual(record['status'], 'fail')
            self.assertEqual(record['returncode'], 7)
            self.assertEqual(record['argv'], argv)
            self.assertEqual((root / 'child.stdout').read_text().splitlines(),
                             [str(root), 'literal; argument'])
            self.assertEqual((root / 'child.stderr').read_text(), 'failure detail\n')
            self.assertEqual(json.loads((root / 'child.command.json').read_text()), record)

    def test_launch_failure_and_timeout_are_retained(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            failed = run_command([str(root / 'missing')], root, root, 'missing', 1, {})
            self.assertEqual(failed['status'], 'launch-error')
            timed = run_command([sys.executable, '-u', '-c',
                                 'import time; print("started"); time.sleep(30)'],
                                root, root, 'timeout', 0.2, dict(os.environ))
            self.assertEqual(timed['status'], 'timeout')
            self.assertIn('started', (root / 'timeout.stdout').read_text())
            self.assertIsInstance(timed['returncode'], int)

    def test_authentication_is_opt_in_private_and_removed_even_after_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'operator.db'
            with closing(sqlite3.connect(source)) as database:
                database.execute('CREATE TABLE fixture (value TEXT)')
                database.execute("INSERT INTO fixture VALUES ('synthetic credential')")
                database.commit()
            before = hashlib.sha256(source.read_bytes()).hexdigest()
            fixture = self.fixture(root, {})
            target = fixture.config / 'agent/agent.db'
            with fixture.model_environment():
                self.assertFalse(target.exists())
            # A preceding native command can initialize its own empty database.
            target.parent.mkdir()
            with closing(sqlite3.connect(target)) as database:
                database.execute('CREATE TABLE initial_native_state (value TEXT)')
            with self.assertRaisesRegex(RuntimeError, 'synthetic failure'):
                with fixture.model_environment(source):
                    self.assertTrue(target.is_file())
                    self.assertFalse(target.is_symlink())
                    self.assertEqual(target.stat().st_mode & 0o777, 0o600)
                    with closing(sqlite3.connect(target)) as database:
                        self.assertEqual(database.execute('SELECT value FROM fixture').fetchone(),
                                         ('synthetic credential',))
                    raise RuntimeError('synthetic failure')
            self.assertFalse(target.exists())
            self.assertFalse(target.with_name('evaluation-auth.db').exists())
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), before)
            self.assertNotIn('synthetic credential', json.dumps(fixture.evidence()))

    def test_sqlite_backup_includes_committed_wal_without_writing_source(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, target = root / 'source.db', root / 'copy.db'
            with closing(sqlite3.connect(source)) as database:
                database.execute('PRAGMA journal_mode=WAL')
                database.execute('CREATE TABLE fixture (value INTEGER)')
                database.execute('INSERT INTO fixture VALUES (42)')
                database.commit()
                before = {path.name: path.read_bytes() for path in (source, Path(str(source) + '-wal'))}
                backup_database(source, target)
                self.assertEqual({path.name: path.read_bytes()
                                  for path in (source, Path(str(source) + '-wal'))}, before)
                with closing(sqlite3.connect(target)) as copied:
                    self.assertEqual(copied.execute('SELECT value FROM fixture').fetchone(), (42,))
            self.assertEqual(target.stat().st_mode & 0o777, 0o600)
            with self.assertRaises(FileExistsError):
                backup_database(source, target)

    def test_native_policy_has_no_legacy_alias_and_prompt_stays_stricter(self):
        self.assertEqual(case_policy({}, 'native'), 'native')
        self.assertEqual(case_policy({'approval': 'prompt'}, 'native'), 'prompt')
        self.assertEqual(policy_overlays('native'), ['eval/native.yml'])
        self.assertEqual(policy_overlays('strict'), ['eval/config.yml'])
        self.assertEqual(policy_overlays('prompt'), ['eval/native.yml', 'eval/prompt-check.yml'])
        with self.assertRaises(ValueError):
            policy_overlays('profile')

    def test_save_json_creates_missing_parent_directories(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / 'nested' / 'case-id' / 'result.json'
            save_json(target, {'status': 'fail'})
            self.assertEqual(json.loads(target.read_text()), {'status': 'fail'})


if __name__ == '__main__':
    unittest.main()
