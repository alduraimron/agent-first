"""Evidence parser regressions: claims must not substitute for observed activation."""
from pathlib import Path
import unittest

from run import finite_check_passed, full_skill_reads, inspect_principles, post_evidence_report

SKILLS = Path(__file__).resolve().parents[1] / 'plugins/agent-first/skills'


def read(name, at=1, path=None, error=False, text=None):
    return {'name': 'read', 'time': at,
            'arguments': {'path': path or 'skill://principle-' + name},
            'result': {'time': at + 0.1, 'isError': error,
                       'text': text if text is not None else
                       (SKILLS / ('principle-' + name) / 'SKILL.md').read_text()}}


def journal(calls, agent=None, path='/sessions/main.jsonl', assistant=None):
    return {'calls': calls, 'agent': agent, 'path': path, 'assistant': assistant or []}


class PrincipleEvidenceTests(unittest.TestCase):
    def case(self, **extra):
        return {'require_native_principle_reads': True, **extra}

    def inspect(self, case, calls, children=None, requested=None):
        failures = []
        evidence = inspect_principles(case, journal(calls), children or [], requested or [], failures)
        return evidence, failures

    def test_mentions_registry_and_failed_or_partial_reads_do_not_count(self):
        full = read('prove-it-works')
        attempts = [
            read('prove-it-works', text='Registered skill: principle-prove-it-works'),
            read('prove-it-works', error=True),
            read('prove-it-works', path='skill://principle-prove-it-works:1-20'),
            read('prove-it-works', text=full['result']['text'].split('## Verification')[0]),
            {'name': 'task', 'arguments': {'context': full['result']['text']},
             'time': 1, 'result': {'time': 2, 'isError': False, 'text': 'Applied prove-it-works'}},
        ]
        self.assertEqual(full_skill_reads(journal(attempts)), {})
        self.assertEqual(set(full_skill_reads(journal([full]))), {'prove-it-works'})

    def test_root_cause_read_must_finish_before_implementation(self):
        edit = {'name': 'edit', 'time': 2, 'arguments': {'input': '[format.js#ABCD]'},
                'result': {'time': 2.1, 'isError': False, 'text': 'changed'}}
        case = self.case(principles_before_mutation=['fix-root-causes'])
        _, failures = self.inspect(case, [edit, read('fix-root-causes', at=3)])
        self.assertTrue(any('before implementation' in failure for failure in failures))
        _, failures = self.inspect(case, [read('fix-root-causes'), edit])
        self.assertEqual(failures, [])

    def test_negative_selection_rejects_excess_and_untriggered_leaf(self):
        case = self.case(principles_all=['prove-it-works'], max_principles=1,
                         forbidden_principles=['build-the-lever'])
        _, failures = self.inspect(case, [read('prove-it-works'), read('build-the-lever')])
        self.assertTrue(any('Untriggered' in failure for failure in failures))
        self.assertTrue(any('Excessive' in failure for failure in failures))

    def test_alternatives_require_a_real_eligible_read(self):
        case = self.case(principles_any=[['laziness-protocol', 'minimize-reader-load']])
        _, failures = self.inspect(case, [read('prove-it-works')])
        self.assertTrue(any('alternatives' in failure for failure in failures))
        _, failures = self.inspect(case, [read('minimize-reader-load')])
        self.assertEqual(failures, [])

    def test_assignment_does_not_imply_child_inheritance(self):
        case = self.case(principle_child_agents={'af-architect': ['boundary-discipline']})
        requests = [{'agent': 'af-architect', 'native_id': 'child', 'result': {'isError': False},
                     'context': 'Read skill://principle-boundary-discipline for this boundary.'}]
        stop = [{'time': 5, 'stopReason': 'stop', 'text': 'Source-backed architectural advice.'}]
        empty = journal([], 'af-architect', '/sessions/child.jsonl', stop)
        _, failures = self.inspect(case, [], [empty], requests)
        self.assertTrue(any('did not read assigned' in failure for failure in failures))
        child = journal([read('boundary-discipline')], 'af-architect', '/sessions/child.jsonl', stop)
        _, failures = self.inspect(case, [], [child], requests)
        self.assertEqual(failures, [])
        late = journal([read('boundary-discipline', at=6)], 'af-architect', '/sessions/child.jsonl', stop)
        _, failures = self.inspect(case, [], [late], requests)
        self.assertTrue(any('before advice' in failure for failure in failures))

    def test_all_assigned_leaves_need_observed_child_reads(self):
        case = self.case(principle_child_agents={'af-architect': ['boundary-discipline']})
        requests = [{'agent': 'af-architect', 'native_id': 'child', 'result': {'isError': False},
                     'context': 'skill://principle-boundary-discipline skill://principle-model-the-domain'}]
        child = journal([read('boundary-discipline')], 'af-architect', '/sessions/child.jsonl',
                        [{'time': 5, 'stopReason': 'stop', 'text': 'Advice'}])
        _, failures = self.inspect(case, [], [child], requests)
        self.assertTrue(any('model-the-domain' in failure for failure in failures))

    def test_independent_work_must_actually_follow_native_denial(self):
        case = self.case(read_after_denied='rollout-notes.md')
        denied = {'name': 'bash', 'time': 2, 'arguments': {'command': 'node --test'},
                  'result': {'time': 3, 'isError': True, 'text': 'Requires approval; no interactive UI'}}
        notes = {'name': 'read', 'time': 1, 'arguments': {'path': 'rollout-notes.md'},
                 'result': {'time': 1.1, 'isError': False, 'text': 'Operator preconditions'}}
        _, failures = self.inspect(case, [notes, denied])
        self.assertTrue(any('did not continue' in failure for failure in failures))
        notes['time'] = 4
        notes['result']['time'] = 4.1
        _, failures = self.inspect(case, [denied, notes])
        self.assertEqual(failures, [])

    def test_failed_preflight_is_not_a_spawned_child(self):
        case = self.case(principle_child_agents={'af-architect': ['boundary-discipline']})
        failed = {'agent': 'af-architect', 'native_id': None,
                  'result': {'isError': True}, 'context': 'No executed assignment'}
        valid = {'agent': 'af-architect', 'native_id': 'child', 'result': {'isError': False},
                 'context': 'Read skill://principle-boundary-discipline'}
        child = journal([read('boundary-discipline')], 'af-architect', '/sessions/child.jsonl',
                        [{'time': 5, 'stopReason': 'stop', 'text': 'Advice'}])
        _, failures = self.inspect(case, [], [child], [failed, valid])
        self.assertEqual(failures, [])
        _, failures = self.inspect(case, [], [], [failed])
        self.assertTrue(any('Missing af-architect assignment' in failure for failure in failures))

    def test_service_readiness_and_failure_are_not_test_passes(self):
        self.assertTrue(finite_check_passed({'isError': False, 'details': {}}))
        for details in ({'service': {'state': 'ready'}}, {'service': {'state': 'failed'}},
                        {'async': True}, {'timedOut': True}):
            self.assertFalse(finite_check_passed({'isError': False, 'details': details}))
        self.assertFalse(finite_check_passed(None))
        self.assertFalse(finite_check_passed({'isError': True, 'details': {}}))
        self.assertFalse(finite_check_passed({'isError': False, 'details': {
            'service': {'state': 'exited'}}, 'text': 'No test completion evidence'}))
        self.assertTrue(finite_check_passed({'isError': False, 'details': {
            'service': {'state': 'exited'}}, 'text': 'ℹ tests 4\nℹ pass 4\nℹ fail 0\n'}))

    def test_cleanup_does_not_erase_completed_post_check_report(self):
        calls = [{"name": "bash", "arguments": {"command": "node --test"},
                  "result": {"time": 3}}]
        report = "PASS: node --test. Browser NOT-RUN."
        messages = [{"time": 4, "stopReason": "stop", "text": report},
                    {"time": 5, "stopReason": "stop", "text": "Owned server stopped."}]
        self.assertEqual(post_evidence_report(messages, calls, ["PASS", "NOT-RUN"]), report)

    def test_predictions_and_aborts_are_not_post_evidence_reports(self):
        calls = [{"name": "task", "arguments": {}, "result": {"time": 3}}]
        messages = [{"time": 2, "stopReason": "stop", "text": "PASS after we finish."},
                    {"time": 4, "stopReason": "aborted", "text": "PASS"}]
        self.assertEqual(post_evidence_report(messages, calls, ["PASS"]), "")
        self.assertEqual(post_evidence_report(
            [{"time": 4, "stopReason": "stop", "text": "PASS"}], calls, ["PASS"], after=5), "")

    def test_report_requirements_cannot_merge_unrelated_messages(self):
        messages = [{"time": 4, "stopReason": "stop", "text": "PASS: node --test."},
                    {"time": 5, "stopReason": "stop", "text": "Browser NOT-RUN."}]
        report = post_evidence_report(messages, [], ["PASS", "NOT-RUN"])
        self.assertFalse("PASS" in report and "NOT-RUN" in report)


if __name__ == '__main__':
    unittest.main()
