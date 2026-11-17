"""Model-free regressions for interaction evidence false-PASS boundaries."""
from pathlib import Path
import tempfile
import unittest

from check_interactions import (BASE_FILES, answer_checks, changed_paths,
                                claims_unrun_tests_passed, full_native_reads,
                                passing_node_test, read_only_tool_violation,
                                snapshot, source_evidence, unauthorized_mutation)

LEAF = '---\nname: interaction-how\n---\n\n# How\n\nRead actual source.\n\n## Last section\nReport unknowns.\n'


def read(path='skill://interaction-how', text=LEAF, error=False):
    return {'name': 'read', 'arguments': {'path': path}, 'time': 1,
            'result': {'isError': error, 'text': text, 'time': 2}}


def journal(*calls):
    return {'calls': list(calls)}


class InteractionEvidenceTests(unittest.TestCase):
    def test_activation_requires_entire_successful_native_leaf(self):
        sources = {'interaction-how': LEAF}
        invalid = [read(error=True), read(text='Read skill://interaction-how'),
                   read(path='skill://interaction-how:1-8'),
                   read(path='skill://interaction-how:raw'),
                   read(path='skill://af-interaction', text=LEAF),
                   read(text=LEAF.rsplit('## Last section', 1)[0]),
                   read(text=LEAF.replace('Read actual source.', '...'))]
        for call in invalid:
            with self.subTest(call=call):
                self.assertEqual(full_native_reads(journal(call), sources), {})
        self.assertEqual(full_native_reads(journal(read()), sources), {'interaction-how': [2]})

    def test_multiple_partial_reads_do_not_accidentally_merge(self):
        midpoint = len(LEAF) // 2
        evidence = journal(read(text=LEAF[:midpoint]), read(text=LEAF[midpoint:]))
        self.assertEqual(full_native_reads(evidence, {'interaction-how': LEAF}), {})

    def test_numbered_full_read_preserves_every_line(self):
        numbered = '\n'.join(f'{number}:{line}' for number, line in enumerate(LEAF.splitlines(), 1))
        self.assertEqual(full_native_reads(journal(read(text=numbered)), {'interaction-how': LEAF}),
                         {'interaction-how': [2]})

    def test_read_only_snapshot_covers_context_deletions_and_new_paths(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / '.agent-first').mkdir()
            context = root / '.agent-first/context.md'
            context.write_text('Do not edit')
            code = root / 'code.mjs'
            code.write_text('original')
            before = snapshot(root)
            context.write_text('silently rewritten')
            code.unlink()
            (root / 'surprise.md').write_text('new')
            (root / 'empty').mkdir()
            self.assertEqual(changed_paths(before, snapshot(root)),
                             ['.agent-first/context.md', 'code.mjs', 'empty', 'surprise.md'])

    def test_generated_source_citations_do_not_count_as_inspection(self):
        root = Path('/owned-fixture')
        calls = [read(path='src/routes.mjs', text=BASE_FILES['src/routes.mjs']),
                 read(path='src/login.mjs', text=BASE_FILES['src/login.mjs'], error=True)]
        checks = source_evidence('how', [journal(*calls)], root)
        self.assertTrue(checks['src/routes.mjs'])
        self.assertFalse(checks['src/login.mjs'])
        calls[1] = read(path='/somewhere-else/src/login.mjs', text=BASE_FILES['src/login.mjs'])
        self.assertFalse(source_evidence('how', [journal(*calls)], root)['src/login.mjs'])

    def test_work_report_needs_real_diff_result(self):
        root = Path('/owned-fixture')
        self.assertFalse(source_evidence('show', [journal(read(text='Continue -> Proceed'))], root)
                         ['actual-local-diff'])
        diff = "diff --git a/src/label.mjs b/src/label.mjs\n-export function buttonLabel() { return 'Continue'; }\n+export function buttonLabel() { return 'Proceed'; }\n"
        call = {'name': 'bash', 'arguments': {'command': 'git diff --no-ext-diff --no-textconv'},
                'result': {'isError': False, 'text': diff}}
        self.assertTrue(source_evidence('show', [journal(call)], root)['actual-local-diff'])

    def test_review_numbers_must_match_actual_and_expected_behavior(self):
        prefix = 'src/billing.mjs: for subtotal 200, discount 20 percent, '
        good = answer_checks('negative-review', prefix + 'actual result 180; expected result 160.')
        self.assertTrue(all(good.values()))
        reversed_values = answer_checks('negative-review', prefix + 'actual result 160; expected result 180.')
        self.assertFalse(reversed_values['actual-wrong-output'])
        self.assertFalse(reversed_values['expected-output'])

    def test_labeled_equations_preserve_actual_and_expected_results(self):
        prefix = 'src/billing.mjs: subtotal 200, discount 20 percent.\n'
        correct = prefix + 'Actual: 200 - 20 = 180\nExpected: 200 * (1 - 20 / 100) = 160\n'
        self.assertTrue(all(answer_checks('negative-review', correct).values()))
        reversed_results = prefix + 'Actual: 200 - 20 = 160\nExpected: 200 * (1 - 20 / 100) = 180\n'
        checks = answer_checks('negative-review', reversed_results)
        self.assertFalse(checks['actual-wrong-output'])
        self.assertFalse(checks['expected-output'])

    def test_catchup_requires_facts_not_a_repeated_filename(self):
        brief = ('Done: hash parsing shipped. In progress: audit export formatting, not complete. '
                 'Blocked: sandbox credentials unavailable. Next: obtain sandbox credentials. '
                 'No tests have run.')
        self.assertTrue(all(answer_checks('ketchup', brief).values()))
        self.assertFalse(answer_checks('ketchup', 'Everything is done; checks passed.')['blocked'])

    def test_scoped_test_evidence_requires_success_and_owned_cwd(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'test').mkdir()
            (root / 'test/label.test.mjs').write_text('// Owned fixture test')
            call = {'name': 'bash', 'arguments': {'command': 'node --test test/label.test.mjs', 'cwd': '.'},
                    'result': {'isError': False, 'text': '# pass 1\n# fail 0\n', 'details': {}}}
            self.assertTrue(passing_node_test(call, root))
            for command in ('node --test ../outside.mjs', 'node --test missing.mjs',
                            'node --test && touch surprise', 'node --test --eval=code'):
                with self.subTest(command=command):
                    self.assertFalse(passing_node_test(
                        {**call, 'arguments': {'command': command}}, root))
            self.assertFalse(passing_node_test({**call, 'arguments': {
                **call['arguments'], 'cwd': root.parent}}, root))
            self.assertFalse(passing_node_test({**call, 'result': {
                'isError': True, 'text': '# pass 1\n# fail 0\n'}}, root))
            self.assertFalse(passing_node_test({**call, 'result': {
                'isError': False, 'text': '# pass 1\n# fail 1\n'}}, root))

    def test_unrun_test_disclaimer_does_not_mask_later_false_pass(self):
        self.assertFalse(claims_unrun_tests_passed('Tests have not run. PASS: source inspection only.'))
        self.assertTrue(claims_unrun_tests_passed('No tests were run. All tests passed.'))
        self.assertTrue(claims_unrun_tests_passed('PASS: node tests'))

    def test_reverted_writes_and_opaque_execution_are_not_read_only(self):
        self.assertTrue(read_only_tool_violation({'name': 'edit', 'arguments': {}}))
        self.assertTrue(read_only_tool_violation({'name': 'eval', 'arguments': {'code': 'write(...)'}}))
        self.assertTrue(read_only_tool_violation({'name': 'bash', 'arguments': {'command': 'touch file; rm file'}}))
        self.assertFalse(read_only_tool_violation({'name': 'bash', 'arguments': {
            'command': 'git diff --no-ext-diff --no-textconv'}}))

    def test_equivalent_git_inspection_forms_are_not_opaque_execution(self):
        for command in ('git status', 'git status --porcelain=v1', 'git status -sb',
                        'git --no-pager diff --no-textconv --no-ext-diff -- src/billing.mjs',
                        'git diff --stat --no-ext-diff --no-textconv',
                        'git diff --no-ext-diff --no-textconv -U10 -- src/label.mjs',
                        'git diff --no-ext-diff --no-textconv && git status --short',
                        "git diff --no-ext-diff --no-textconv && printf '\\n--- STATUS ---\\n' && git status --short",
                        'git diff HEAD --no-ext-diff --no-textconv'):
            with self.subTest(command=command):
                self.assertFalse(read_only_tool_violation(
                    {'name': 'bash', 'arguments': {'command': command}}))
        for command in ('git diff', 'git diff --ext-diff --no-textconv',
                        'git diff --no-ext-diff --no-textconv --output=README.md',
                        'git -c core.fsmonitor=script status',
                        'git status; touch surprise', 'git status && touch surprise',
                        'git status > README.md', 'git status $(touch surprise)',
                        'git status\ntouch surprise', 'git status `touch surprise`',
                        'git diff --no-ext-diff --no-textconv -- ../outside',
                        'git diff --no-ext-diff --no-textconv && touch surprise',
                        'git status & git status', 'git status || git status',
                        'git status && printf -v GLOBAL variable'):
            with self.subTest(command=command):
                self.assertTrue(read_only_tool_violation(
                    {'name': 'bash', 'arguments': {'command': command}}))

    def test_requested_document_does_not_authorize_reverted_context_edits(self):
        root = Path('/owned-fixture')
        allowed = {'README.md'}
        self.assertFalse(unauthorized_mutation(
            {'name': 'write', 'arguments': {'path': 'README.md'}}, root, allowed))
        self.assertTrue(unauthorized_mutation(
            {'name': 'write', 'arguments': {'path': '.agent-first/context.md'}}, root, allowed))
        self.assertTrue(unauthorized_mutation(
            {'name': 'edit', 'arguments': {'input': '[src/login.mjs#ABCD]\nPUT 1.=1:\n+changed\n'}},
            root, allowed))
        self.assertTrue(unauthorized_mutation(
            {'name': 'write', 'arguments': {'path': '../README.md'}}, root, allowed))


if __name__ == '__main__':
    unittest.main()
