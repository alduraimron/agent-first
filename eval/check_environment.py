#!/usr/bin/env python3
"""Read-only native context checks and isolated launcher guard scenarios. No model calls."""
import argparse
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
PROMPT_RULES = ('git *reset*--hard*', 'git *clean*', 'git *stash* clear*',
                'git *commit*--amend*', 'git *checkout*', 'git *restore*',
                'rm *-r*', 'rm *-R*', 'rm *--recursive*', 'find *-delete*',
                'sudo *', 'doas *', 'systemctl *', 'scp *', 'ssh *',
                'aws *', 'terraform *', 'kubectl *', 'docker *prune*',
                'docker *volume rm*', 'ovnfs *apply*')
AUTO_COMMANDS = (
    'npm test', 'npm run check', 'npm run build', 'git status --short',
    'git add sum.js', 'git commit --help', 'git push --help', 'git fetch --help',
    'git pull --help', 'git clone --help', 'git merge --help', 'git cherry-pick --help',
    'git revert --help', 'git branch new-branch', 'git stash save --help',
    'git stash apply --help', 'git stash pop --help', 'git switch new-branch',
    'npm install --help', 'npm ci --help', 'npm update --help', 'npm uninstall --help',
    'npm exec --help', 'npx --help', 'pnpm add --help', 'pnpm dlx --help',
    'yarn add --help', 'bun add --help', 'bunx --help', 'uv add --help',
    'uv sync --help', 'uv run --help', 'cargo update --help', 'go get --help',
    'curl --help', 'wget --help', 'rm -- obsolete.txt', 'rmdir -- empty',
    'docker run --help', 'docker build --help', 'docker start --help',
    'docker stop --help', 'docker logs --help', 'docker exec --help',
    'docker compose up --help', 'docker compose down --help')
ASK_COMMANDS = (
    'rm -r --help', 'rm -R --help', 'rm -fr --help', 'rm --recursive --help',
    'git reset --hard --help', 'git reset --merge --help', 'git clean --help',
    'git stash clear --help', 'git stash drop --help', 'git branch -D --help',
    'git worktree remove --help', 'git commit --amend --help', 'git rebase --help',
    'git checkout --help', 'git restore --help', 'git switch --force --help',
    'npm install --global --help', 'npm --global install --help',
    'npm install -g --help', 'pnpm add --global --help', 'bun add -g --help',
    'pip install --user --help', 'python -m pip install --prefix=/tmp/probe --help',
    'uv pip install --system --help', 'cargo install --help', 'go install --help',
    'sudo --help', 'doas --help', 'systemctl --help', 'ssh -V', 'scp --help',
    'terraform --help', 'aws --help', 'kubectl --help', 'npm publish --help',
    'docker push --help', 'docker volume rm --help', 'docker system prune --help',
    'docker compose down --volumes --help', 'docker compose down -v --help',
    'docker --context remote run --help', 'docker --host tcp://example run --help',
    'ovnfs apply --help', 'ovnfs apply --dry-run --help', 'ovnfs rm --help',
    'dropdb --help', 'redis-cli FLUSHALL --help')
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


def catalog_skill_names(system_prompt):
    """Read native catalog metadata, excluding explicit leaf pointers elsewhere."""
    text = '\n'.join(system_prompt) if isinstance(system_prompt, list) else system_prompt
    sections = re.findall(r'<skills>\s*(.*?)\s*</skills>', text, re.S)
    if len(sections) != 1:
        raise ValueError('Expected exactly one native skills catalog')
    return set(re.findall(r'^- ([a-z][a-z0-9-]*):', sections[0], re.M))


def source_patterns(source=None):
    """Parse this profile's block or inline YAML rules, failing on ambiguous input.

    This deliberately supports only scalar match/approval mappings, not general YAML.
    Native effective settings remain the authoritative parser comparison.
    """
    if source is None:
        source = (ROOT / 'profile/config.yml').read_text()
    lines = source.splitlines()
    bash_headers = [index for index, line in enumerate(lines) if re.fullmatch(r'bash:\s*(?:#.*)?', line)]
    if len(bash_headers) != 1:
        raise ValueError('Expected exactly one top-level bash mapping')
    start = bash_headers[0] + 1
    end = next((index for index in range(start, len(lines))
                if lines[index].strip() and not lines[index].startswith((' ', '#'))), len(lines))
    headers = [index for index in range(start, end)
               if re.fullmatch(r'  patterns:\s*(?:#.*)?', lines[index])]
    if len(headers) != 1:
        raise ValueError('Expected exactly one bash.patterns sequence')
    start = headers[0] + 1
    end = next((index for index in range(start, end)
                if lines[index].strip() and not lines[index].lstrip().startswith('#')
                and len(lines[index]) - len(lines[index].lstrip()) <= 2), end)

    def scalar(value):
        value = value.strip()
        if value.startswith('"'):
            try:
                decoded, consumed = json.JSONDecoder().raw_decode(value)
            except ValueError as error:
                raise ValueError('Malformed quoted YAML scalar') from error
            suffix = value[consumed:].strip()
            if not isinstance(decoded, str) or (suffix and not suffix.startswith('#')):
                raise ValueError('Unexpected quoted YAML scalar suffix')
            return decoded
        if value.startswith("'"):
            match = re.fullmatch(r"'((?:[^']|'')*)'\s*(?:#.*)?", value)
            if not match:
                raise ValueError('Malformed single-quoted YAML scalar')
            return match[1].replace("''", "'")
        value = re.split(r'\s+#', value, maxsplit=1)[0].rstrip()
        if not value or value[0] in '*&!{}[]|>':
            raise ValueError('Expected a nonempty plain or quoted YAML scalar')
        return value

    patterns = []
    current = None
    seen = set()

    def finish():
        if current is None:
            return
        if set(current) != {'match', 'approval'} or not current['match'] \
                or current['approval'] not in ('allow', 'prompt', 'deny'):
            raise ValueError('Incomplete or invalid bash pattern rule')
        if current['match'] in seen:
            raise ValueError('Duplicate bash pattern match: ' + current['match'])
        seen.add(current['match'])
        patterns.append(current)

    quoted = r"""(?:'(?:[^']|'')*'|"(?:[^"\\]|\\.)*"|[^,{}]+)"""
    for line in lines[start:end]:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if line.startswith('    - '):
            finish()
            current = {}
            body = line[6:].strip()
            if body.startswith('{'):
                inline = re.fullmatch(r'\{\s*(.*?)\s*\}\s*(?:#.*)?', body)
                if not inline:
                    raise ValueError('Malformed inline bash pattern')
                fields = re.fullmatch(
                    rf'(match|approval):\s*({quoted})\s*,\s*(match|approval):\s*({quoted})\s*',
                    inline[1])
                if not fields or fields[1] == fields[3]:
                    raise ValueError('Expected unique match and approval fields')
                current = {fields[1]: scalar(fields[2]), fields[3]: scalar(fields[4])}
                continue
        elif line.startswith('      ') and current is not None:
            body = line[6:].strip()
        else:
            raise ValueError('Unexpected bash pattern indentation or item')
        field = re.fullmatch(r'(match|approval):\s*(.*)', body)
        if not field or field[1] in current:
            raise ValueError('Unknown or duplicate bash pattern field')
        current[field[1]] = scalar(field[2])
    finish()
    if not patterns:
        raise ValueError('Empty bash.patterns sequence')
    return patterns


def hashes():
    home = Path.home() / '.omp/agent'
    return {name: hashlib.sha256((home / name).read_bytes()).hexdigest()
            for name in ('config.yml', 'RULES.md', 'mcp.json') if (home / name).is_file()}


def baseline_checks(path, values, patterns):
    """Compare actual native values, not YAML formatting or setting descriptions."""
    baseline = json.loads(path.read_text())
    prior_values = {name: item.get('value') for name, item in baseline['effective_settings'].items()}
    prior_patterns = prior_values.pop('bash.patterns')
    current_values = {name: value for name, value in values.items() if name != 'bash.patterns'}
    changed = sorted(name for name in prior_values.keys() | current_values.keys()
                     if name not in prior_values or name not in current_values
                     or prior_values[name] != current_values[name])
    denies = lambda rules: [rule for rule in rules if rule.get('approval') == 'deny']
    allows = lambda rules: [rule for rule in rules if rule.get('approval') == 'allow']
    authorized = {
        'profile/config.yml', 'profile/RULES.md',
        'profile/skills/af-verification/SKILL.md', 'profile/skills/af-verification/approval.md',
        'profile/skills/af-verification/checks.md',
        'profile/skills/af-engineering/workflows/project-initialization.md',
        'profile/skills/af-isolation/SKILL.md',
    }
    changed_assets = [name for name, digest in baseline['source_hashes'].items()
                      if name not in authorized and (
                          not (ROOT / name).is_file()
                          or hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest)]
    default_hashes = {str(Path.home() / '.omp/agent' / name): digest
                      for name, digest in hashes().items()}
    checks = {
        'baseline-all-non-pattern-effective-values-unchanged': not changed,
        'baseline-all-114-deny-rules-and-order-unchanged':
            len(denies(prior_patterns)) == 114 and denies(patterns) == denies(prior_patterns),
        'baseline-all-nine-exact-allows-unchanged':
            len(allows(prior_patterns)) == 9 and allows(patterns) == allows(prior_patterns),
        'baseline-launcher-unchanged': hashlib.sha256((ROOT / 'bin/af').read_bytes()).hexdigest()
            == baseline['launcher_sha256'],
        'baseline-default-user-configuration-unchanged':
            default_hashes == baseline['default_configuration_hashes'],
        'baseline-unrelated-source-assets-unchanged': not changed_assets,
        'baseline-user-hide-thinking-preference-preserved':
            prior_values.get('hideThinkingBlock') == values.get('hideThinkingBlock'),
    }
    return checks, {'path': str(path.resolve()), 'changed_effective_values': changed,
                    'changed_unrelated_assets': changed_assets,
                    'authorized_source_changes': sorted(authorized)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path,
                        help='Compare native effective values and preservation hashes to a captured baseline JSON')
    options = parser.parse_args()
    (ROOT / 'eval/results').mkdir(parents=True, exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix='environment-', dir=ROOT / 'eval/results'))
    output.chmod(0o700)
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
        try:
            catalog_names = catalog_skill_names(state.get('data', {}).get('systemPrompt', []))
        except ValueError as error:
            catalog_names = set()
            result['native_catalog_error'] = str(error)
        native_checks = {
            'native-state-response': bool(state.get('success')),
            'main-orchestrator-loaded': 'Agent-First orchestration' in state_text,
            'shared-rules-loaded': 'Agent-First shared rules' in state_text,
            'project-context-loaded': 'AF_FULL_CONTEXT_PROBE' in state_text,
            'all-skills-discovered': bool(commands.get('success')) and all(
                name in commands_text for name in SKILLS + LEAVES),
            'principle-selector-catalog-visible': 'af-principles' in catalog_names,
            'interaction-selector-catalog-visible': 'af-interaction' in catalog_names,
            'interaction-routing-contract-loaded': 'Interaction-first intent routing' in state_text,
            'on-demand-leaf-catalog-hidden': bool(catalog_names) and not set(LEAVES) & catalog_names,
            'exact-thirteen-visible-catalog-entries': catalog_names == set(SKILLS),
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
        try:
            parsed_patterns = source_patterns()
        except ValueError as error:
            parsed_patterns = None
            result['source_pattern_error'] = str(error)
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
            'routine-development-classified-AUTO': all(
                pattern_policy(command, patterns) in (None, 'allow') for command in AUTO_COMMANDS),
            'high-risk-help-probes-require-native-prompt': all(
                pattern_policy(command, patterns) == 'prompt' for command in ASK_COMMANDS),
            'profile-patterns-match-effective-source': patterns == parsed_patterns,
            'only-nine-exact-readonly-git-allow-grants':
                sum(rule.get('approval') == 'allow' for rule in patterns) == 9
                and {rule.get('match') for rule in patterns if rule.get('approval') == 'allow'}
                == READ_ONLY_GIT,
            'native-git-guard-preserved': values.get('bash.gitGuard') is True,
            'bounded-delegation': values.get('task.maxConcurrency') == 2 and values.get('task.maxRecursionDepth') == 1,
            'automatic-isolation-and-apply-disabled': values.get('task.isolation.enabled') is False and values.get('task.isolation.apply') is False,
            'automatic-provisioning-disabled': values.get('eval.autoProvision') is False,
            'compound-command-policy-preserved': values.get('bash.allowCompoundCommands') is False,
            'project-configuration-unchanged': team_config.read_text() == team_content,
        }
        result['effective_classifications'] = {
            category: [{'command': command, 'pattern_approval': pattern_policy(command, patterns)}
                       for command in commands]
            for category, commands in (('AUTO', AUTO_COMMANDS), ('ASK', ASK_COMMANDS), ('DENY', DENY_COMMANDS))}
        if options.baseline:
            try:
                preservation, result['baseline'] = baseline_checks(options.baseline, values, patterns)
                settings_checks.update(preservation)
            except (OSError, ValueError, KeyError, TypeError) as error:
                settings_checks['baseline-readable-and-valid'] = False
                result['baseline_error'] = str(error)
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
