#!/usr/bin/env python3
"""Exercise native project marketplace lifecycle without a model request or settings overlay."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from plugin_fixture import PluginFixture, ROOT

PLUGIN = 'agent-first@agent-first'
ADVISORS = {'af-architect', 'af-database', 'af-security', 'af-frontend',
            'af-performance', 'af-devops'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def settings_values(text):
    value = json.loads(text)
    if isinstance(value, dict) and 'settings' not in value:
        if not value or not all(isinstance(row, dict) for row in value.values()):
            raise ValueError('Invalid native settings map')
        return {key: row.get('value') for key, row in value.items()}
    rows = value.get('settings', []) if isinstance(value, dict) else value
    if not isinstance(rows, list) or not rows:
        raise ValueError('Missing native settings rows')
    return {row['key']: row.get('value') for row in rows}


def catalog_names(prompt):
    blocks = re.findall(r'<skills>\s*(.*?)</skills>', prompt, re.S)
    body = '\n'.join(blocks)
    names = set(re.findall(r'<name>([^<]+)</name>', body))
    names.update(re.findall(r'^- ([a-z0-9][a-z0-9_./~-]*): ', body, re.M))
    if not names:
        raise ValueError('Missing readable native skill catalog')
    return names


def inspect_session(fixture, output, label, cwd=None):
    """RPC EOF drains state responses; no prompt/model request is sent."""
    argv = [fixture.omp, '--mode', 'rpc', '--no-ui', '--no-session', '--no-title']
    commands = [{'id': 'state', 'type': 'get_state'},
                {'id': 'commands', 'type': 'get_available_commands'}]
    payload = ''.join(json.dumps(command) + '\n' for command in commands)
    (output / (label + '.stdin')).write_text(payload)
    result = subprocess.run(argv, cwd=cwd or fixture.workspace, env=fixture.env,
                            input=payload, text=True, capture_output=True, timeout=60)
    (output / (label + '.stdout')).write_text(result.stdout)
    (output / (label + '.stderr')).write_text(result.stderr)
    record = {'argv': argv, 'cwd': str(cwd or fixture.workspace),
              'returncode': result.returncode, 'model_request': False}
    (output / (label + '.command.json')).write_text(json.dumps(record, indent=2) + '\n')
    responses = {}
    for line in result.stdout.splitlines():
        event = json.loads(line)
        if event.get('type') == 'response':
            responses[event.get('id')] = event
    state = responses.get('state', {})
    if result.returncode or not state.get('success'):
        raise RuntimeError(f'Native RPC state failed: {label}')
    return state['data'], responses.get('commands', {})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, default=ROOT / 'eval/results')
    parser.add_argument('--upgrade-marketplace', type=Path,
                        help='An existing disposable OVNFS marketplace checkout with a newer catalog version')
    options = parser.parse_args()
    omp = shutil.which('omp')
    if not omp:
        parser.error('Existing omp required; nothing is installed')
    options.results.mkdir(parents=True, exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix='plugin-lifecycle-', dir=options.results.resolve()))
    os.chmod(output, 0o700)
    result = {'checks': [], 'commands': [], 'model_requests': 0,
              'artifacts': str(output), 'status': 'FAIL'}
    actual_home = Path.home()
    protected = [actual_home / '.omp/agent' / name for name in
                 ('config.yml', 'config.yaml', 'settings.json', 'RULES.md', 'mcp.json')]
    protected += [actual_home / '.omp/marketplaces.json',
                  actual_home / '.omp/plugins/installed_plugins.json',
                  actual_home / '.omp/plugins/omp-plugins.lock.json']
    baseline = {str(path): digest(path) for path in protected}
    source = ROOT / 'plugins/agent-first'
    source_hashes = {str(path.relative_to(source)): digest(path)
                     for path in source.rglob('*') if path.is_file()}
    expected = {path.parent.name for path in (source / 'skills').glob('*/SKILL.md')}
    hidden = {name for name in expected if name.startswith(('principle-', 'interaction-'))}
    result['source_hashes'] = source_hashes
    result['global_baseline'] = baseline

    def check(name, passed, evidence=None, status=None):
        result['checks'].append({'name': name, 'status': status or ('PASS' if passed else 'FAIL'),
                                 'evidence': evidence})

    with tempfile.TemporaryDirectory(prefix='af-plugin-projects-') as allocation:
        allocation = Path(allocation)
        project, other = allocation / 'personal', allocation / 'unrelated'
        for path in (project, other):
            (path / '.omp').mkdir(parents=True)
        own_skill = project / '.omp/skills/project-convention/SKILL.md'
        own_skill.parent.mkdir(parents=True)
        own_skill.write_text('---\nname: project-convention\ndescription: Project-owned convention probe.\n---\n\nPROJECT_CONVENTION_RETAINED\n')
        project_config = project / '.omp/config.yml'
        project_config.write_text('tools:\n  approvalMode: write\n  approval:\n    eval: deny\nbash:\n  patterns:\n    - {match: "printf af-never-execute", approval: deny}\n')
        instructions = project / 'AGENTS.md'
        instructions.write_text('# Project instructions\n\nPLUGIN_COEXISTENCE_INSTRUCTIONS\nKeep existing project assets.\n')
        context = project / '.agent-first/context.md'
        context.parent.mkdir()
        context.write_text('# Existing durable context\n\nExisting decision: use project-owned scripts.\n')
        preserved = {path: path.read_bytes() for path in (own_skill, project_config, instructions, context)}
        fixture = PluginFixture(omp, project, output)
        try:
            record = fixture.command('version', '--version')
            result['version'] = (output / record['stdout']).read_text().strip()
            record = fixture.command('before-settings', 'config', 'list', '--json')
            before = settings_values((output / record['stdout']).read_text())
            check('before-settings-readable', record['status'] == 'pass')
            check('fresh-native-project-install', fixture.install())
            registry = project / '.omp/plugins/installed_plugins.json'
            check('actual-project-registry', registry.is_file(), str(registry))
            check('no-user-scoped-install', not (fixture.config / 'plugins/installed_plugins.json').exists())
            record = fixture.command('after-settings', 'config', 'list', '--json')
            after = settings_values((output / record['stdout']).read_text())
            check('all-native-settings-inherited', before == after)
            check('project-write-mode-and-denies-inherited', after.get('tools.approvalMode') == 'write'
                  and after.get('tools.approval', {}).get('eval') == 'deny'
                  and after.get('bash.patterns') == before.get('bash.patterns'))
            record = fixture.command('skills', 'skill', 'list', '--json')
            skills = json.loads((output / record['stdout']).read_text()).get('skills', [])
            own = [skill for skill in skills if skill['name'] in expected]
            check('all-fifty-seven-plugin-skills-discovered', len(expected) == 57
                  and {skill['name'] for skill in own} == expected)
            check('forty-four-leaves-hidden-and-thirteen-visible',
                  {skill['name'] for skill in own if skill.get('hide')} == hidden
                  and len(hidden) == 44 and len(own) - len(hidden) == 13)
            check('existing-project-skill-coexists', any(skill['name'] == 'project-convention' for skill in skills))
            # Resolve every skill through the real native URI handler, including hidden leaves.
            resolved = []
            for index, name in enumerate(sorted(expected)):
                record = fixture.command('skill-read-' + str(index), 'read', 'skill://' + name)
                content = (output / record['stdout']).read_text()
                if record['status'] == 'pass' and 'name: ' + name in content:
                    resolved.append(name)
            check('all-skill-uris-actually-resolve', set(resolved) == expected, resolved)
            state, commands = inspect_session(fixture, output, 'main-rpc')
            prompt = state.get('systemPrompt', [])
            prompt = '\n'.join(prompt) if isinstance(prompt, list) else prompt
            check('native-main-orchestrator-and-shared-rule-injected',
                  'Agent-First orchestration' in prompt and 'Agent-First shared contract' in prompt)
            check('native-project-instructions-preserved-in-context', 'PLUGIN_COEXISTENCE_INSTRUCTIONS' in prompt)
            check('visible-selector-index-without-leaf-catalog', catalog_names(prompt) == expected - hidden | {'project-convention'},
                  sorted(catalog_names(prompt)))
            roster = json.dumps(state.get('dumpTools', []))
            check('six-advisors-and-native-reviewer-advertised',
                  all(name in roster for name in ADVISORS | {'reviewer'}))
            other_state, _ = inspect_session(fixture, output, 'unrelated-rpc', other)
            check('uninstalled-project-has-no-agent-first-routing',
                  'Agent-First orchestration' not in str(other_state.get('systemPrompt')))
            # A descendant without its own .omp/ or .git/ inherits the ancestor project install.
            descendant = project / 'packages/sub-service'
            descendant.mkdir(parents=True)
            descendant_state, _ = inspect_session(fixture, output, 'descendant-rpc', descendant)
            check('descendant-inherits-ancestor-project-install',
                  'Agent-First orchestration' in str(descendant_state.get('systemPrompt')))
            # Reproduce retained-fixture nesting: a parent .omp must not capture
            # installation intended for a newly allocated child project.
            parent_registry = registry.read_bytes()
            nested = project / 'nested-disposable'
            nested.mkdir()
            nested_output = output / 'nested-install'
            nested_output.mkdir()
            nested_fixture = PluginFixture(omp, nested, nested_output)
            check('nested-fixture-project-install', nested_fixture.install())
            nested_registry = nested / '.omp/plugins/installed_plugins.json'
            check('nested-fixture-does-not-mutate-ancestor-registration',
                  nested_registry.is_file() and registry.read_bytes() == parent_registry,
                  str(nested_registry))
            result['nested_fixture'] = nested_fixture.evidence()
            # An independent marketplace plugin must survive Agent-First removal.
            extra = allocation / 'extra-marketplace'
            (extra / '.omp-plugin').mkdir(parents=True)
            (extra / 'plugins/extra/skills/unrelated-plugin').mkdir(parents=True)
            (extra / '.omp-plugin/marketplace.json').write_text(json.dumps({
                'name': 'coexistence-probe', 'owner': {'name': 'Disposable fixture'},
                'plugins': [{'name': 'extra', 'source': './plugins/extra', 'version': '1.0.0'}]}))
            (extra / 'plugins/extra/skills/unrelated-plugin/SKILL.md').write_text(
                '---\nname: unrelated-plugin\ndescription: Independent plugin coexistence probe.\n---\n\nUNRELATED_PLUGIN_RETAINED\n')
            check('unrelated-marketplace-added', fixture.command('extra-add', 'plugin', 'marketplace', 'add', extra)['status'] == 'pass')
            check('unrelated-plugin-installed', fixture.command('extra-install', 'plugin', 'install', '--scope', 'project',
                                                               'extra@coexistence-probe')['status'] == 'pass')
            record = fixture.command('upgrade-dry-run', 'plugin', 'upgrade', '--scope', 'project', '--dry-run', PLUGIN)
            check('native-upgrade-preview', record['status'] == 'pass')
            if options.upgrade_marketplace:
                upgraded = options.upgrade_marketplace.expanduser().resolve(strict=True)
                catalog = json.loads((upgraded / '.omp-plugin/marketplace.json').read_text())
                new_version = next(entry['version'] for entry in catalog['plugins'] if entry['name'] == 'agent-first')
                old_catalog = json.loads((ROOT / '.omp-plugin/marketplace.json').read_text())
                old_version = old_catalog['plugins'][0]['version']
                if new_version == old_version:
                    raise ValueError('Upgrade fixture must contain a distinct newer version')
                check('disposable-upgrade-catalog-switch',
                      fixture.command('catalog-remove', 'plugin', 'marketplace', 'remove', 'agent-first')['status'] == 'pass'
                      and fixture.command('catalog-add', 'plugin', 'marketplace', 'add', upgraded)['status'] == 'pass')
                check('native-catalog-refresh', fixture.command('catalog-update', 'plugin', 'marketplace', 'update', 'agent-first')['status'] == 'pass')
            else:
                new_version = None
                check('different-version-upgrade', False, 'Supply --upgrade-marketplace with an existing disposable newer checkout', 'NOT-RUN')
            check('native-project-upgrade', fixture.command('upgrade', 'plugin', 'upgrade', '--scope', 'project', PLUGIN)['status'] == 'pass')
            installed = json.loads(registry.read_text())
            if new_version:
                check('different-version-upgrade', new_version in json.dumps(installed), new_version)
            state, _ = inspect_session(fixture, output, 'upgraded-rpc')
            check('upgraded-orchestrator-loads', 'Agent-First orchestration' in str(state.get('systemPrompt')))
            check('native-uninstall-preview', fixture.command('uninstall-preview', 'plugin', 'uninstall', '--scope', 'project',
                                                              '--dry-run', PLUGIN)['status'] == 'pass')
            check('preview-keeps-registration', PLUGIN in registry.read_text())
            check('native-project-uninstall', fixture.command('uninstall', 'plugin', 'uninstall', '--scope', 'project', PLUGIN)['status'] == 'pass')
            record = fixture.command('uninstalled-skills', 'skill', 'list', '--json')
            remaining = {skill['name'] for skill in json.loads((output / record['stdout']).read_text()).get('skills', [])}
            check('uninstall-removes-only-owned-skills', not expected & remaining
                  and {'project-convention', 'unrelated-plugin'} <= remaining)
            state, _ = inspect_session(fixture, output, 'uninstalled-rpc')
            check('uninstall-removes-orchestration-and-advisors',
                  'Agent-First orchestration' not in str(state.get('systemPrompt'))
                  and not any(name in json.dumps(state.get('dumpTools', [])) for name in ADVISORS))
            check('project-config-instructions-and-context-byte-preserved',
                  all(path.read_bytes() == content for path, content in preserved.items()))
            # The fixture operator explicitly chooses YOLO; the plugin never writes it.
            yolo = allocation / 'operator-yolo'
            (yolo / '.omp').mkdir(parents=True)
            (yolo / '.omp/config.yml').write_text('tools:\n  approvalMode: yolo\n')
            fixture.workspace = yolo
            check('operator-yolo-project-install',
                  fixture.command('operator-yolo-install', 'plugin', 'install', '--scope', 'project', PLUGIN)['status'] == 'pass')
            record = fixture.command('operator-yolo-settings', 'config', 'get', 'tools.approvalMode', '--json')
            check('operator-yolo-inherited', json.loads((output / record['stdout']).read_text()).get('value') == 'yolo')
            # Project-owned skills/agents shadow plugin names and operator disables remain authoritative.
            collision = allocation / 'collision-probe'
            (collision / '.omp/skills/af-engineering').mkdir(parents=True)
            (collision / '.omp/agents').mkdir(parents=True)
            shadow_skill = collision / '.omp/skills/af-engineering/SKILL.md'
            shadow_skill.write_text('---\nname: af-engineering\ndescription: Project-owned engineering override.\n---\n\nPROJECT_OWNED_ENGINEERING_SHADOW\n')
            shadow_agent = collision / '.omp/agents/af-architect.md'
            shadow_agent.write_text('---\nname: af-architect\ndescription: PROJECT_OWNED_ARCHITECT_SHADOW\ntools: [read]\nspawns: []\n---\n\nProject override body.\n')
            collision_config = collision / '.omp/config.yml'
            collision_config.write_text('task:\n  disabledAgents:\n    - af-devops\n')
            collision_preserved = {path: path.read_bytes() for path in (shadow_skill, shadow_agent, collision_config)}
            fixture.workspace = collision
            check('collision-project-install',
                  fixture.command('collision-install', 'plugin', 'install', '--scope', 'project', PLUGIN)['status'] == 'pass')
            record = fixture.command('collision-skill-read', 'read', 'skill://af-engineering')
            check('project-skill-keeps-bare-name-on-collision',
                  record['status'] == 'pass' and 'PROJECT_OWNED_ENGINEERING_SHADOW' in (output / record['stdout']).read_text())
            collision_state, _ = inspect_session(fixture, output, 'collision-rpc', collision)
            collision_roster = json.dumps(collision_state.get('dumpTools', []))
            check('project-agent-shadows-plugin-advisor', 'PROJECT_OWNED_ARCHITECT_SHADOW' in collision_roster)
            check('operator-disabled-agent-honored', 'af-devops' not in collision_roster and 'af-security' in collision_roster)
            check('collision-project-uninstall',
                  fixture.command('collision-uninstall', 'plugin', 'uninstall', '--scope', 'project', PLUGIN)['status'] == 'pass')
            check('collision-project-overrides-byte-preserved',
                  all(path.read_bytes() == content for path, content in collision_preserved.items()))
            result['fixture'] = fixture.evidence()
        except Exception as error:
            check('lifecycle-completed', False, f'{type(error).__name__}: {error}')
        finally:
            check('real-global-config-and-registries-unchanged', baseline == {str(path): digest(path) for path in protected})
            check('source-plugin-unchanged-by-native-installer', source_hashes == {
                str(path.relative_to(source)): digest(path) for path in source.rglob('*') if path.is_file()})
            result['commands'] = fixture.commands
    result['status'] = 'FAIL' if any(row['status'] == 'FAIL' for row in result['checks']) else 'PASS'
    (output / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return 1 if result['status'] == 'FAIL' else 0


if __name__ == '__main__':
    raise SystemExit(main())
