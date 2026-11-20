#!/usr/bin/env python3
"""Check native principle/interaction discovery and URI reads without model calls."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
from plugin_fixture import PLUGIN, PluginFixture
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRINCIPLES = (
    'laziness-protocol', 'foundational-thinking', 'redesign-from-first-principles',
    'attack-the-premise', 'subtract-before-you-add', 'minimize-reader-load',
    'outcome-oriented-execution', 'experience-first', 'exhaust-the-design-space',
    'build-the-lever', 'model-the-domain', 'boundary-discipline',
    'type-system-discipline', 'make-operations-idempotent',
    'migrate-callers-then-delete-legacy-apis', 'separate-before-serializing-shared-state',
    'prove-it-works', 'fix-root-causes', 'sequence-verifiable-units',
    'test-behavior-not-implementation', 'explain-the-number',
    'guard-the-context-window', 'never-block-on-the-human', 'encode-lessons-in-structure',
)
ORIGINAL = {'af-engineering', 'af-design', 'af-database', 'af-frontend', 'af-testing',
            'af-security', 'af-performance', 'af-operations', 'af-context',
            'af-verification', 'af-isolation'}
INTERACTIONS = (
    'how', 'why', 'teach', 'blast-radius', 'technical-writing', 'bro',
    'interview-me', 'in-your-own-words', 'idea-refine', 'sharpen', 'architect',
    'figure-it-out', 'recall', 'ketchup', 'show-me-your-work', 'pause-safely',
    'reflect', 'correct', 'automate-me', 'unslop',
)
SECTIONS = ('Purpose', 'Triggers', 'Decision procedure', 'Trade-offs', 'Examples',
            'Observable outcomes', 'Verification')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def advisor_contract_valid(content):
    """Require read-only tools, no spawning, index-only autoload and report JTD schema."""
    match = re.match(r'^---\n(.*?)\n---(?:\n|\Z)', content, re.S)
    if not match:
        return False
    frontmatter = match.group(1)
    has_report_schema = bool(re.search(
        r'(?m)^output:\s*\n  properties:\s*\n    report:\s*\n      type:\s*string\s*$',
        frontmatter))
    return (bool(re.search(r'(?m)^tools:\s*\[read, grep, glob\]\s*$', frontmatter))
            and bool(re.search(r'(?m)^spawns:\s*\[\]\s*$', frontmatter))
            and bool(re.search(r'(?m)^structured:\s*true\s*$', frontmatter))
            and has_report_schema
            and bool(re.search(r'(?m)^autoloadSkills:\s*\[af-[a-z-]+,\s*af-principles\]\s*$', frontmatter))
            and 'principle-' not in frontmatter)


def default_hashes():
    return {str(path): digest(path) for path in
            (Path.home() / '.omp/agent' / name for name in ('config.yml', 'RULES.md', 'mcp.json'))
            if path.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path,
                        help='Optional historical default-configuration hash snapshot')
    options = parser.parse_args()
    results = ROOT / 'eval/results'
    results.mkdir(exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix='principles-native-', dir=results))
    before = default_hashes()
    checks = []

    def check(name, passed, detail=None):
        checks.append({'name': name, 'status': 'PASS' if passed else 'FAIL', 'detail': detail})

    expected_leaves = {'principle-' + name for name in PRINCIPLES}
    interaction_leaves = {'interaction-' + name for name in INTERACTIONS}
    hidden_leaves = expected_leaves | interaction_leaves
    visible_skills = ORIGINAL | {'af-principles', 'af-interaction'}
    plugin = ROOT / 'plugins/agent-first'
    files = {path.parent.name: path for path in (plugin / 'skills').glob('*/SKILL.md')}
    check('complete-skill-set', set(files) == visible_skills | hidden_leaves,
          sorted(files))
    source = (plugin / 'skills/af-principles/SOURCES.md').read_text()
    license_text = (plugin / 'skills/af-principles/LICENSE').read_text()
    check('upstream-mit-notice', 'Copyright (c) 2026 Lauren Tan' in license_text
          and 'Permission is hereby granted' in license_text
          and 'THE SOFTWARE IS PROVIDED "AS IS"' in license_text)
    selector = files['af-principles'].read_text()
    for name in sorted(expected_leaves):
        content = files[name].read_text() if name in files else ''
        check('contract-' + name, all('\n## ' + section + '\n' in content for section in SECTIONS)
              and '\nname: ' + name + '\n' in content
              and '**Good:**' in content and '**Problematic:**' in content
              and 'Copyright (c) 2026 Lauren Tan, MIT' in content
              and 'skill://af-principles/SOURCES.md' in content)
        check('indexed-and-attributed-' + name, 'skill://' + name in selector
              and '/skills/' + name + '/SKILL.md' in source)
    interaction_selector = files['af-interaction'].read_text() if 'af-interaction' in files else ''
    for name in sorted(interaction_leaves):
        content = files[name].read_text() if name in files else ''
        check('interaction-contract-' + name, '\nname: ' + name + '\n' in content
              and '\n## Output contract\n' in content)
        check('interaction-indexed-' + name, 'skill://' + name in interaction_selector)
    check('no-principle-bodies-in-main-prompt', all(
        '## ' + section not in (plugin / 'rules/agent-first-orchestrator.md').read_text()
        for section in SECTIONS))
    for path in (plugin / 'agents').glob('af-*.md'):
        content = path.read_text()
        check('advisor-index-only-' + path.stem, advisor_contract_valid(content))

    omp = shutil.which('omp')
    check('existing-omp', bool(omp))
    if omp:
        workspace = output / 'workspace'
        (workspace / '.omp').mkdir(parents=True)
        project_config = workspace / '.omp/config.yml'
        project_config.write_text('task:\n  maxConcurrency: 3\n  structured: false\n'
                                  'tools:\n  approvalMode: always-ask\n')
        instructions = workspace / 'AGENTS.md'
        instructions.write_text('Synthetic discovery fixture. Preserve these project instructions.\n')
        protected = {str(path): digest(path) for path in (project_config, instructions)}
        fixture = PluginFixture(omp, workspace, output)

        def native(label, args):
            record = fixture.command(label, *args)
            check('command-' + label, record['status'] == 'pass', record)
            return (output / record['stdout']).read_text()

        def settings(label):
            text = native(label, ['config', 'list', '--json'])
            try:
                return {key: item.get('value') for key, item in json.loads(text).items()}
            except (ValueError, TypeError, AttributeError) as error:
                check(label + '-readable', False, str(error))
                return {}

        before_settings = settings('settings-before-install')
        check('fixture-operator-policy-effective',
              before_settings.get('tools.approvalMode') == 'always-ask'
              and before_settings.get('task.maxConcurrency') == 3
              and before_settings.get('task.structured') is False)
        installed = fixture.install()
        check('native-project-install', installed, fixture.evidence())
        registry = workspace / '.omp/plugins/installed_plugins.json'
        check('native-project-install-registry', registry.is_file())
        after_settings = settings('settings-after-install')
        check('plugin-inherits-native-settings',
              bool(before_settings) and before_settings == after_settings,
              {key: {'before': before_settings.get(key), 'after': after_settings.get(key)}
               for key in before_settings.keys() | after_settings.keys()
               if before_settings.get(key) != after_settings.get(key)})

        def listing(label):
            try:
                return {item['name']: item for item in
                        json.loads(native(label, ['skill', 'list', '--json']))['skills']}
            except (ValueError, KeyError, TypeError) as error:
                check(label + '-readable', False, str(error))
                return {}

        registered = listing('skill-list')
        check('native-discovery-exact-57', set(registered) == set(files))
        check('native-hidden-leaves-only',
              {name for name, item in registered.items() if item.get('hide')} == hidden_leaves)
        check('native-visible-catalog-13',
              {name for name, item in registered.items() if not item.get('hide')} == visible_skills)
        for name in ['af-principles', 'af-interaction', *sorted(hidden_leaves)]:
            text = native('read-' + name, ['read', 'skill://' + name])
            expected = files.get(name)
            body = expected.read_text().split('---', 2)[-1].strip() if expected else ''
            check('native-uri-' + name, bool(body and body in text))
        # Discovery must track native enablement, not merely count source names.
        native('disable-project-plugin', ['plugin', 'disable', PLUGIN, '--scope', 'project'])
        disabled = listing('skills-disabled')
        check('disabled-plugin-not-discovered', not (set(disabled) & set(files)))
        native('enable-project-plugin', ['plugin', 'enable', PLUGIN, '--scope', 'project'])
        restored = listing('skills-restored')
        check('reenabled-plugin-discovered', set(restored) == set(files))
        text = native('read-restored-selector', ['read', 'skill://af-principles'])
        check('reenabled-plugin-uri-body', selector.split('---', 2)[-1].strip() in text)
        check('native-settings-still-inherited', settings('settings-final') == before_settings)
        check('unrelated-project-context-preserved',
              all(Path(name).is_file() and digest(Path(name)) == value
                  for name, value in protected.items()))
        (output / 'plugin-fixture.json').write_text(json.dumps(fixture.evidence(), indent=2) + '\n')
    if options.baseline:
        baseline = json.loads(options.baseline.read_text())
        check('default-config-baseline-unchanged',
              default_hashes() == baseline['default_configuration_hashes'])
    check('default-config-check-unchanged', default_hashes() == before)
    result = {'status': 'FAIL' if any(item['status'] != 'PASS' for item in checks) else 'PASS',
              'checks': checks, 'artifacts': str(output),
              'scope': 'Native packaging/discovery/URI resolution, not model decision quality'}
    (output / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return result['status'] != 'PASS'


if __name__ == '__main__':
    raise SystemExit(main())
