"""Evaluation-only native marketplace fixture. No distribution/runtime dependency."""
from contextlib import closing, contextmanager
import json
import os
from pathlib import Path
import signal
import sqlite3
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'agent-first@agent-first'
CLEAR_ENV = (
    'HOME', 'OMP_PROFILE', 'PI_PROFILE', 'PI_CONFIG_DIR', 'OMP_CONFIG_DIR', 'PI_CONFIG_FILES',
    'PI_CODING_AGENT_DIR', 'OMP_CODING_AGENT_DIR', 'PI_SESSION_ID', 'PI_SESSION_FILE',
    'PI_TOOL_CALL_ID', 'PI_BLOCKED_AGENT', 'PI_TASK_DEPTH', 'CLAUDE_CONFIG_DIR',
    'XDG_CONFIG_HOME', 'XDG_DATA_HOME', 'XDG_STATE_HOME', 'XDG_CACHE_HOME',
)


def run_command(argv, cwd, output, label, timeout, env):
    """Retain exact argv, stdout/stderr, launch failures and partial timeout output."""
    record = {'argv': [str(arg) for arg in argv], 'cwd': str(cwd),
              'timeout_seconds': timeout, 'status': 'not-run'}
    start = time.monotonic()
    with (output / f'{label}.stdout').open('wb') as stdout, (output / f'{label}.stderr').open('wb') as stderr:
        try:
            process = subprocess.Popen(record['argv'], cwd=cwd, env=env,
                                       stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                       start_new_session=True)
            try:
                record['returncode'] = process.wait(timeout=timeout)
                record['status'] = 'pass' if process.returncode == 0 else 'fail'
            except subprocess.TimeoutExpired:
                record['status'] = 'timeout'
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                record['returncode'] = process.returncode
        except OSError as error:
            record.update(status='launch-error', error=str(error))
    record.update(duration_seconds=round(time.monotonic() - start, 3),
                  stdout=f'{label}.stdout', stderr=f'{label}.stderr')
    (output / f'{label}.command.json').write_text(json.dumps(record, indent=2) + '\n')
    return record


def backup_database(source, target):
    """Opt-in private SQLite backup; never open the operator database for writes."""
    source = Path(source).expanduser().resolve(strict=True)
    target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    descriptor = os.open(target, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    os.close(descriptor)
    try:
        with closing(sqlite3.connect(source.as_uri() + '?mode=ro', uri=True)) as original:
            with closing(sqlite3.connect(target)) as private:
                original.backup(private)
    except Exception:
        target.unlink(missing_ok=True)
        raise


class PluginFixture:
    """One synthetic project plus isolated native user registry/cache/config state."""

    def __init__(self, omp, workspace, output, *, marketplace=ROOT, inherited=None):
        self.omp = str(omp)
        self.workspace = Path(workspace).resolve()
        # Fixtures may live under another Git/.omp root. Anchor before any native
        # install so project scope cannot escape into that ancestor.
        (self.workspace / '.omp').mkdir(mode=0o700, exist_ok=True)
        self.output = Path(output).resolve()
        self.marketplace = Path(marketplace).resolve()
        self.state = self.output / 'native-state'
        self.state.mkdir(mode=0o700)
        self.home = self.state / 'home'
        self.home.mkdir(mode=0o700)
        self.config = self.home / '.omp'
        self.config.mkdir(mode=0o700)
        self.env = dict(os.environ if inherited is None else inherited)
        self.cleared = sorted(key for key in self.env if key in CLEAR_ENV
                              or key.startswith(('PI_SESSION_', 'OMP_SESSION_',
                                                 'PI_CONFIG_', 'OMP_CONFIG_')))
        for key in self.cleared:
            self.env.pop(key, None)
        self.env['HOME'] = str(self.home)
        # Native getBaseConfigRoot joins homedir and PI_CONFIG_DIR as path segments.
        self.env['PI_CONFIG_DIR'] = '.omp'
        # Private empty XDG roots prevent ambient state without rerouting native DBs.
        for kind in ('config', 'data', 'state', 'cache'):
            path = self.state / ('xdg-' + kind)
            path.mkdir(mode=0o700)
            self.env['XDG_' + kind.upper() + '_HOME'] = str(path)
        self.commands = []

    def argv(self, *args):
        return [self.omp, '--cwd', str(self.workspace), *map(str, args)]

    def command(self, label, *args, timeout=45):
        record = run_command(self.argv(*args), self.workspace, self.output,
                             label, timeout, self.env)
        self.commands.append(record)
        return record

    def install(self):
        """Use the actual CLI, never synthesize installation/registry files."""
        for label, args in (
            ('marketplace-add', ('plugin', 'marketplace', 'add', str(self.marketplace))),
            ('plugin-install', ('plugin', 'install', PLUGIN, '--scope', 'project')),
        ):
            if self.command(label, *args)['status'] != 'pass':
                return False
        return True

    @contextmanager
    def model_environment(self, auth_source=None):
        """Credentials are opt-in, private, and removed before retaining artifacts."""
        target = self.config / 'agent' / 'agent.db'
        temporary = target.with_name('evaluation-auth.db')
        copied = False
        try:
            if auth_source is not None:
                backup_database(auth_source, temporary)
                # CLI setup may already have initialized an empty private agent.db.
                for suffix in ('-wal', '-shm', '-journal'):
                    Path(str(target) + suffix).unlink(missing_ok=True)
                temporary.replace(target)
                copied = True
            yield self.env
        finally:
            temporary.unlink(missing_ok=True)
            if copied:
                for suffix in ('', '-wal', '-shm', '-journal'):
                    Path(str(target) + suffix).unlink(missing_ok=True)

    def evidence(self):
        return {'plugin': PLUGIN, 'scope': 'project', 'marketplace': str(self.marketplace),
                'cleared_environment': self.cleared,
                'isolated_native_state': str(self.state), 'commands': self.commands,
                'authentication': 'Optional read-only SQLite backup; private copy removed after model run'}
