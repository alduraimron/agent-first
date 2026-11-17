#!/usr/bin/env python3
"""Read-only native context checks and isolated launcher guard scenarios. No model calls."""
import hashlib
import json
import os
from pathlib import Path
import selectors
import shutil
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ['af-engineering', 'af-design', 'af-database', 'af-frontend', 'af-testing',
          'af-security', 'af-performance', 'af-operations', 'af-context',
          'af-verification', 'af-isolation']


def hashes():
    home = Path.home() / '.omp/agent'
    return {name: hashlib.sha256((home / name).read_bytes()).hexdigest()
            for name in ('config.yml', 'RULES.md', 'mcp.json') if (home / name).is_file()}


def main():
    (ROOT / 'eval/results').mkdir(parents=True, exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix='environment-', dir=ROOT / 'eval/results'))
    result = {'status': 'FAIL', 'artifacts': str(output), 'checks': []}
    before = hashes()
    failures = []
    with tempfile.TemporaryDirectory(prefix='af-environment-') as temporary:
        fixture = Path(temporary)
        home = fixture / 'home'
        home.mkdir()
        project = home / 'personal'
        project.mkdir()
        env = dict(os.environ, HOME=str(home))
        for key in ('PI_CONFIG_DIR', 'PI_CODING_AGENT_DIR', 'PI_CONFIG_FILES',
                    'PI_SESSION_ID', 'PI_SESSION_FILE', 'PI_TOOL_CALL_ID'):
            env.pop(key, None)

        def guard(name, args, expected):
            run = subprocess.run([str(ROOT / 'bin/af'), '--cwd', str(project), *args],
                                 env=env, text=True, capture_output=True, timeout=15)
            passed = run.returncode == 2 and expected in run.stderr
            result['checks'].append({'name': name, 'status': 'PASS' if passed else 'FAIL',
                                     'argv': run.args, 'exit_code': run.returncode,
                                     'stdout': run.stdout, 'stderr': run.stderr})
            if not passed:
                failures.append(name)

        guard('reject-yolo', ['--yolo'], 'unrecognized arguments')
        profile = home / '.omp/profiles/agent-first/agent'
        profile.mkdir(parents=True)
        conflict = profile / 'config.yml'
        conflict.write_text('user-owned\n')
        guard('preserve-conflicting-profile', ['--activate'], 'Refusing to overwrite')
        if conflict.read_text() != 'user-owned\n':
            failures.append('conflicting-profile-was-modified')
        conflict.unlink()
        tools = project / '.omp/tools'
        tools.mkdir(parents=True)
        (tools / 'owned.js').write_text('// Native project tool fixture\n')
        guard('reject-project-tools', ['--activate'], 'Native project tools')
        (tools / 'owned.js').unlink()
        tools.rmdir()
        agents = project / '.omp/agents'
        agents.mkdir()
        (agents / 'af-security.md').write_text('name: af-security\n')
        guard('reject-agent-shadow', ['--activate'], 'shadow profile agents')
        (agents / 'af-security.md').unlink()
        agents.rmdir()
        outside = fixture / 'foreign.jsonl'
        outside.write_text('{}\n')
        guard('reject-external-resume', ['--resume', str(outside), 'Continue'], 'Resume paths')

        # Native RPC is configuration inspection only: no prompt or model request is sent.
        native_project = fixture / 'native-project'
        native_project.mkdir()
        (native_project / 'AGENTS.md').write_text('# AF_FULL_CONTEXT_PROBE\nPersonal synthetic fixture.\n')
        native_env = os.environ.copy()
        for key in ('PI_CONFIG_FILES', 'PI_CODING_AGENT_DIR', 'PI_SESSION_ID',
                    'PI_SESSION_FILE', 'PI_TOOL_CALL_ID'):
            native_env.pop(key, None)
        native_env.update(OMP_PROFILE='agent-first', PI_PROFILE='agent-first')
        argv = [shutil.which('omp'), '--profile', 'agent-first', '--cwd', str(native_project),
                '--config', str(ROOT / 'profile/config.yml'), '--append-system-prompt',
                str(ROOT / 'profile/APPEND_SYSTEM.md'), '--no-extensions', '--no-title',
                '--mode', 'rpc', '--no-ui']
        with (output / 'rpc.stderr').open('wb') as errors:
            process = subprocess.Popen(argv, env=native_env, stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE, stderr=errors)
            responses = {}
            raw = bytearray()
            pending = bytearray()
            selector = selectors.DefaultSelector()
            selector.register(process.stdout, selectors.EVENT_READ)
            try:
                for identifier, command in (('af-state', 'get_state'), ('af-commands', 'get_available_commands')):
                    process.stdin.write((json.dumps({'id': identifier, 'type': command}) + '\n').encode())
                process.stdin.flush()
                deadline = time.monotonic() + 45
                while len(responses) < 2 and time.monotonic() < deadline:
                    events = selector.select(max(0, deadline - time.monotonic()))
                    if not events:
                        break
                    chunk = os.read(process.stdout.fileno(), 65536)
                    if not chunk:
                        break
                    raw.extend(chunk)
                    pending.extend(chunk)
                    while b'\n' in pending:
                        line, _, rest = pending.partition(b'\n')
                        pending = bytearray(rest)
                        try:
                            event = json.loads(line)
                        except ValueError:
                            continue
                        if event.get('type') == 'response' and event.get('id') in ('af-state', 'af-commands'):
                            responses[event['id']] = event
            finally:
                selector.close()
                process.stdin.close()
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
                process.stdout.close()
                (output / 'rpc.stdout').write_bytes(raw)
        state = responses.get('af-state', {})
        commands = responses.get('af-commands', {})
        state_text = json.dumps(state)
        commands_text = json.dumps(commands)
        native_checks = {
            'native-state-response': bool(state.get('success')),
            'main-orchestrator-loaded': 'Agent-First orchestration' in state_text,
            'shared-rules-loaded': 'Agent-First shared rules' in state_text,
            'project-context-loaded': 'AF_FULL_CONTEXT_PROBE' in state_text,
            'all-skills-discovered': bool(commands.get('success')) and all(name in commands_text for name in SKILLS),
        }
        for name, passed in native_checks.items():
            result['checks'].append({'name': name, 'status': 'PASS' if passed else 'FAIL'})
            if not passed:
                failures.append(name)
        result['native_rpc_argv'] = argv
        result['native_response_ids'] = list(responses)
    result['default_configuration_hashes_unchanged'] = hashes() == before
    if not result['default_configuration_hashes_unchanged']:
        failures.append('default-configuration-changed')
    result['failures'] = failures
    result['status'] = 'FAIL' if failures else 'PASS'
    (output / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
