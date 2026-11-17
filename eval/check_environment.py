#!/usr/bin/env python3
"""Read-only native context checks and isolated launcher guard scenarios. No model calls."""
import hashlib
import json
import os
from pathlib import Path
import re
import selectors
import shutil
import subprocess
import tempfile
import time

from check_principles import INTERACTIONS, PRINCIPLES

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ['af-engineering', 'af-design', 'af-database', 'af-frontend', 'af-testing',
          'af-security', 'af-performance', 'af-operations', 'af-context',
          'af-verification', 'af-isolation', 'af-principles', 'af-interaction']
LEAVES = ['principle-' + name for name in PRINCIPLES] + ['interaction-' + name for name in INTERACTIONS]

# These are policy observations only. No command below is submitted or executed.
PROMPT_RULES = ('git *commit*', 'git *push*', 'git *fetch*', 'git *pull*',
                'git *clone*', 'git *reset*', 'rm *', 'rmdir *', 'unlink *',
                'chmod *', 'chown *', 'npm install*', 'npm exec*', 'pnpm dlx*',
                'yarn add*', 'bun install*', 'pip* install*', 'cargo install*',
                'go install*', 'uv run*', 'npx*', 'sudo *', 'doas *',
                'curl *', 'wget *', 'scp *', 'ssh *', 'aws *', 'terraform *',
                'kubectl *', 'docker run*', 'docker *system prune*', 'ovnfs *apply*')
DENY_RULES = ('dd *', 'mkfs*', 'shred *', 'truncate *', 'wipefs *', 'fdisk *', 'parted *',
              'pkill *', 'killall *', 'shutdown*', 'reboot*', 'poweroff*', 'halt*',
              'ssh-keygen *', 'ssh-add *', 'nc *', 'socat *',
              'git *config *--global*', 'git *config *--system*', 'git *update-ref*',
              'git *push*--force*', 'git *push -f*',
              'omp *auth*', 'omp *token*', 'omp *login*', 'omp *config*',
              'curl *.ssh/*', 'curl *.aws/credentials*')
DENY_COMMANDS = ('dd --help', 'mkfs --help', 'git push --force --help',
                 'git push --force-with-lease --help', 'git push -f --help',
                 'git push -vf --help', 'git push --delete --help',
                 'git push -d --help', 'git push --mirror --help',
                 'git push origin +HEAD:refs/heads/probe', 'git push origin :probe',
                 'rm -rf /', 'rm -- ../probe', 'rm -- ~/probe',
                 'rm -- $HOME/probe')
READ_ONLY_GIT = {'git branch --show-current', 'git branch --list', 'git branch -a',
                 'git branch -r', 'git branch -v', 'git branch -vv',
                 'git tag --list', 'git tag -l', 'git remote -v'}


def pattern_policy(command, patterns):
    """Native single-command matching: normalized whitespace, anchored '*' only."""
    normalized = ' '.join(command.split())
    for rule in patterns:
        match = ' '.join(str(rule.get('match', '')).split())
        expression = '.*'.join(re.escape(part) for part in match.split('*'))
        if re.fullmatch(expression, normalized):
            return rule.get('approval')
    return None


def source_patterns():
    """Read this profile's inline YAML rules without adding a YAML dependency."""
    source = (ROOT / 'profile/config.yml').read_text()
    return [{'match': match, 'approval': approval} for _, match, approval in re.findall(
        r"""^\s*-\s*\{\s*match:\s*(['"])(.*?)\1,\s*approval:\s*(allow|prompt|deny)\s*\}\s*$""",
        source, re.M)]


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

        for flag, value in (('--yolo', None), ('--auto-approve', None),
                            ('--approval-mode', 'yolo'), ('--config', 'foreign.yml'),
                            ('--profile', 'default'), ('--extension', 'foreign.js')):
            guard('reject-override-' + flag[2:], [flag, *([value] if value else [])],
                  'unrecognized arguments')
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
        enrollment = subprocess.run([str(ROOT / 'bin/af'), '--cwd', str(project), '--trust-project'],
                                    env=env, text=True, capture_output=True, timeout=15)
        enrolled = enrollment.returncode == 0
        result['checks'].append({'name': 'explicit-personal-enrollment',
                                 'status': 'PASS' if enrolled else 'FAIL'})
        if not enrolled:
            failures.append('explicit-personal-enrollment')
        outside = fixture / 'foreign.jsonl'
        outside.write_text('{}\n')
        guard('reject-external-resume', ['--resume', str(outside), 'Continue'], 'Resume paths')

        # Native RPC is configuration inspection only: no prompt or model request is sent.
        native_project = fixture / 'native-project'
        native_project.mkdir()
        # A project cannot replace the launcher's pinned scalar or deny-pattern array.
        (native_project / '.omp').mkdir()
        team_config = native_project / '.omp/config.yml'
        team_content = ('tools:\n  approvalMode: always-ask\n'
                        'bash:\n  patterns:\n    - { match: "*", approval: allow }\n')
        team_config.write_text(team_content)
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
        system_prompt_text = json.dumps(state.get('data', {}).get('systemPrompt', []))
        native_checks = {
            'native-state-response': bool(state.get('success')),
            'main-orchestrator-loaded': 'Agent-First orchestration' in state_text,
            'shared-rules-loaded': 'Agent-First shared rules' in state_text,
            'project-context-loaded': 'AF_FULL_CONTEXT_PROBE' in state_text,
            'all-skills-discovered': bool(commands.get('success')) and all(
                name in commands_text for name in SKILLS + LEAVES),
            'principle-selector-catalog-visible': 'af-principles' in system_prompt_text,
            'interaction-selector-catalog-visible': 'af-interaction' in system_prompt_text,
            'interaction-routing-contract-loaded': 'Interaction-first intent routing' in state_text,
            'on-demand-leaf-catalog-hidden': all(name not in system_prompt_text for name in LEAVES),
        }
        for name, passed in native_checks.items():
            result['checks'].append({'name': name, 'status': 'PASS' if passed else 'FAIL'})
            if not passed:
                failures.append(name)
        result['native_rpc_argv'] = argv
        settings_argv = [shutil.which('omp'), '--profile', 'agent-first',
                         '--cwd', str(native_project), '--config',
                         str(ROOT / 'profile/config.yml'), 'config', 'list', '--json']
        settings_run = subprocess.run(settings_argv, env=native_env, text=True,
                                      capture_output=True, timeout=30)
        (output / 'settings.stdout').write_text(settings_run.stdout)
        (output / 'settings.stderr').write_text(settings_run.stderr)
        settings = json.loads(settings_run.stdout) if settings_run.returncode == 0 else {}
        values = {name: item.get('value') for name, item in settings.items()}
        policies = values.get('tools.approval') or {}
        patterns = values.get('bash.patterns') or []
        settings_checks = {
            'effective-yolo-despite-project-mode': values.get('tools.approvalMode') == 'yolo',
            'routine-tools-without-overrides': all(name not in policies for name in ('bash', 'eval', 'task')),
            'explicit-tool-denies-preserved': all(policies.get(name) == 'deny' for name in (
                'debug', 'github', 'checkpoint', 'rewind', 'security_scan',
                'manage_skill', 'computer.control')),
            'explicit-prompt-families-preserved': all(
                any(rule.get('match') == match and rule.get('approval') == 'prompt'
                    for rule in patterns) for match in PROMPT_RULES),
            'explicit-hard-deny-rules-preserved': all(
                any(rule.get('match') == match and rule.get('approval') == 'deny'
                    for rule in patterns) for match in DENY_RULES),
            'stronger-hard-denies-precede-prompts': all(
                pattern_policy(command, patterns) == 'deny' for command in DENY_COMMANDS),
            'help-probes-require-native-prompt': all(
                pattern_policy(command, patterns) == 'prompt' for command in (
                    'rm --help', 'git push --help', 'git commit --help',
                    'npm install --help', 'sudo --help', 'curl --help',
                    'terraform --help', 'ovnfs apply --help', 'rmdir -- approved-empty')),
            'profile-patterns-match-effective-source': bool(source_patterns()) and patterns == source_patterns(),
            'only-exact-readonly-git-allow-grants': all(
                '*' not in str(rule.get('match', '')) and rule.get('match') in READ_ONLY_GIT
                for rule in patterns if rule.get('approval') == 'allow'),
            'native-git-guard-preserved': values.get('bash.gitGuard') is True,
            'bounded-delegation': values.get('task.maxConcurrency') == 2 and values.get('task.maxRecursionDepth') == 1,
            'automatic-isolation-and-apply-disabled': values.get('task.isolation.enabled') is False and values.get('task.isolation.apply') is False,
            'automatic-provisioning-disabled': values.get('eval.autoProvision') is False,
            'project-configuration-unchanged': team_config.read_text() == team_content,
        }
        for name, passed in settings_checks.items():
            result['checks'].append({'name': name, 'status': 'PASS' if passed else 'FAIL'})
            if not passed:
                failures.append(name)
        result['settings_argv'] = settings_argv
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
