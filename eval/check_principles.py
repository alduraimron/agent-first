#!/usr/bin/env python3
"""Check principle packaging and native OMP discovery/URI reads without model calls."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
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
SECTIONS = ('Purpose', 'Triggers', 'Decision procedure', 'Trade-offs', 'Examples',
            'Observable outcomes', 'Verification')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def default_hashes():
    return {str(path): digest(path) for path in
            (Path.home() / '.omp/agent' / name for name in ('config.yml', 'RULES.md', 'mcp.json'))
            if path.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path,
                        help='Optional pre-change settings/default-config/launcher snapshot')
    options = parser.parse_args()
    results = ROOT / 'eval/results'
    results.mkdir(exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix='principles-native-', dir=results))
    before = default_hashes()
    checks = []

    def check(name, passed, detail=None):
        checks.append({'name': name, 'status': 'PASS' if passed else 'FAIL', 'detail': detail})

    expected_leaves = {'principle-' + name for name in PRINCIPLES}
    files = {path.parent.name: path for path in (ROOT / 'profile/skills').glob('*/SKILL.md')}
    check('complete-skill-set', set(files) == ORIGINAL | {'af-principles'} | expected_leaves,
          sorted(files))
    source = (ROOT / 'profile/skills/af-principles/SOURCES.md').read_text()
    license_text = (ROOT / 'profile/skills/af-principles/LICENSE').read_text()
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
    check('no-principle-bodies-in-main-prompt', all(
        '## ' + section not in (ROOT / 'profile/APPEND_SYSTEM.md').read_text()
        for section in SECTIONS))
    for path in (ROOT / 'profile/agents').glob('af-*.md'):
        content = path.read_text()
        check('advisor-index-only-' + path.stem,
              'tools: [read, grep, glob]' in content and 'spawns: []' in content
              and 'autoloadSkills: [' in content and ', af-principles]' in content
              and 'autoloadSkills: [principle-' not in content)

    omp = shutil.which('omp')
    check('existing-omp', bool(omp))
    env = dict(os.environ)
    for key in ('PI_CONFIG_FILES', 'PI_CODING_AGENT_DIR', 'PI_SESSION_ID',
                'PI_SESSION_FILE', 'PI_TOOL_CALL_ID'):
        env.pop(key, None)
    env.update(OMP_PROFILE='agent-first', PI_PROFILE='agent-first')
    base = [omp, '--profile', 'agent-first', '--config', str(ROOT / 'profile/config.yml')] if omp else []

    def native(label, args):
        argv = [*base, *args]
        record = {'argv': argv, 'status': 'NOT-RUN'}
        try:
            run = subprocess.run(argv, env=env, cwd=ROOT, text=True, capture_output=True, timeout=45)
            (output / (label + '.stdout')).write_text(run.stdout)
            (output / (label + '.stderr')).write_text(run.stderr)
            record.update(status='PASS' if run.returncode == 0 else 'FAIL', exit_code=run.returncode)
            return run
        except (OSError, subprocess.TimeoutExpired) as error:
            record.update(status='FAIL', error=str(error))
            return None
        finally:
            (output / (label + '.command.json')).write_text(json.dumps(record, indent=2) + '\n')

    settings = {}
    if omp:
        listing = native('skill-list', ['skill', 'list', '--json'])
        try:
            skills = json.loads(listing.stdout)['skills'] if listing and listing.returncode == 0 else []
            registered = {item['name']: item for item in skills}
            check('native-discovery-exact-36', set(registered) == set(files))
            check('native-hidden-leaves-only',
                  {name for name, item in registered.items() if item.get('hide')} == expected_leaves)
            check('native-visible-catalog-12',
                  {name for name, item in registered.items() if not item.get('hide')} == ORIGINAL | {'af-principles'})
        except (ValueError, KeyError, TypeError) as error:
            check('native-skill-list-readable', False, str(error))
        for name in ['af-principles', *sorted(expected_leaves)]:
            run = native('read-' + name, ['read', 'skill://' + name])
            expected = files.get(name)
            # Native output must contain the actual body, not just a registry entry.
            body = expected.read_text().split('---', 2)[-1].strip() if expected else ''
            check('native-uri-' + name, bool(run and run.returncode == 0 and body and body in run.stdout))
        run = native('effective-settings', ['config', 'list', '--json'])
        try:
            settings = json.loads(run.stdout) if run and run.returncode == 0 else {}
        except ValueError as error:
            check('native-settings-readable', False, str(error))
    values = {key: item.get('value') for key, item in settings.items()}
    check('effective-exact-inclusion', set(values.get('skills.includeSkills') or []) == set(files))
    check('effective-leaf-hiding', values.get('skills.manualSkills') == ['principle-*'])
    check('existing-safety-invariants', values.get('tools.approvalMode') == 'yolo'
          and values.get('task.maxConcurrency') == 2 and values.get('task.maxRecursionDepth') == 1
          and values.get('task.isolation.enabled') is False
          and values.get('task.isolation.apply') is False
          and values.get('eval.autoProvision') is False)
    if options.baseline:
        baseline = json.loads(options.baseline.read_text())
        old_values = {key: item.get('value') for key, item in baseline['effective_settings'].items()}
        ignored = {'skills.includeSkills', 'skills.manualSkills'}
        differences = {key: {'before': old_values.get(key), 'after': values.get(key)}
                       for key in old_values.keys() | values.keys()
                       if key not in ignored and old_values.get(key) != values.get(key)}
        check('only-skill-settings-changed', not differences, differences)
        check('launcher-unchanged', digest(ROOT / 'bin/af') == baseline['launcher_sha256'])
        check('default-config-baseline-unchanged', default_hashes() == baseline['default_configuration_hashes'])
    check('default-config-check-unchanged', default_hashes() == before)
    result = {'status': 'FAIL' if any(item['status'] != 'PASS' for item in checks) else 'PASS',
              'checks': checks, 'artifacts': str(output),
              'scope': 'Native packaging/discovery/URI resolution, not model decision quality'}
    (output / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return result['status'] != 'PASS'


if __name__ == '__main__':
    raise SystemExit(main())
