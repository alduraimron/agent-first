#!/usr/bin/env python3
"""Reject silent policy-rule loss across the profile's supported YAML spellings."""
import unittest

from check_environment import catalog_skill_names, pattern_policy, source_patterns


class PatternParserTests(unittest.TestCase):
    def test_block_and_inline_rules_preserve_order_and_scalar_meaning(self):
        expanded = """tools:
  approvalMode: yolo
bash:
  gitGuard: true
  patterns:
    - match: git *push*--force*
      approval: deny
    - approval: prompt
      match: 'rm *-r*'
    - match: "git branch --list"
      approval: allow
hideThinkingBlock: true
"""
        inline = """bash:
  patterns:
    - { match: 'git *push*--force*', approval: deny }
    - { approval: prompt, match: 'rm *-r*' }
    - { match: "git branch --list", approval: allow }
"""
        expected = [
            {'match': 'git *push*--force*', 'approval': 'deny'},
            {'match': 'rm *-r*', 'approval': 'prompt'},
            {'match': 'git branch --list', 'approval': 'allow'},
        ]
        self.assertEqual(source_patterns(expanded), expected)
        self.assertEqual(source_patterns(inline), expected)
        self.assertEqual(pattern_policy('git push --force --help', source_patterns(expanded)), 'deny')
        self.assertEqual(pattern_policy('rm   -r --help', source_patterns(inline)), 'prompt')
        self.assertIsNone(pattern_policy('git branch --list other', source_patterns(inline)))

    def test_quoted_punctuation_and_comments_are_not_rule_boundaries(self):
        rules = source_patterns("""bash:
  patterns:
    # Keep punctuation within the scalar.
    - {match: 'printf ''a,b # c''', approval: prompt} # operator note
    - match: "printf \\\"quoted\\\""
      approval: deny # operator note
""")
        self.assertEqual(rules, [
            {'match': "printf 'a,b # c'", 'approval': 'prompt'},
            {'match': 'printf "quoted"', 'approval': 'deny'},
        ])

    def test_missing_empty_and_duplicate_sections_fail_closed(self):
        for source in (
            'tools:\n  approvalMode: yolo\n',
            'bash:\n  gitGuard: true\n',
            'bash:\n  patterns:\n',
            'bash:\n  patterns:\nbash:\n  patterns:\n',
            'bash:\n  patterns:\n  patterns:\n',
        ):
            with self.subTest(source=source), self.assertRaises(ValueError):
                source_patterns(source)

    def test_malformed_incomplete_and_duplicate_rules_fail_closed(self):
        for body in (
            '    - match: rm *-r*\n',
            '    - match: rm *-r*\n      approval: unknown\n',
            '    - match: rm *-r*\n      approval: prompt\n      approval: allow\n',
            '    - {match: "rm *-r*", match: "dd *"}\n',
            '    - {match: "rm *-r*", approval: prompt\n',
            '    - match: "unterminated\n      approval: prompt\n',
            '    - match: rm *-r*\n      approval: prompt\n'
            '    - match: rm *-r*\n      approval: allow\n',
            '    - match: rm *-r*\n     approval: prompt\n',
        ):
            with self.subTest(body=body), self.assertRaises(ValueError):
                source_patterns('bash:\n  patterns:\n' + body)

    def test_catalog_metadata_excludes_leaf_pointers_elsewhere(self):
        prompt = ['<skills>\n- af-interaction: Route conversations.\n</skills>',
                  'Read skill://interaction-show-me-your-work before reporting evidence.']
        self.assertEqual(catalog_skill_names(prompt), {'af-interaction'})
        leaked = ['<skills>\n- af-interaction: Route conversations.\n'
                  '- interaction-show-me-your-work: Full leaf metadata.\n</skills>']
        self.assertIn('interaction-show-me-your-work', catalog_skill_names(leaked))

    def test_missing_or_duplicate_catalog_is_not_hidden_metadata_proof(self):
        for prompt in (['Read skill://af-interaction'],
                       ['<skills></skills>', '<skills></skills>']):
            with self.subTest(prompt=prompt), self.assertRaises(ValueError):
                catalog_skill_names(prompt)

    def test_only_star_is_a_wildcard_and_matching_remains_anchored(self):
        rules = [{'match': 'probe [x]?.txt*', 'approval': 'deny'}]
        self.assertEqual(pattern_policy('probe [x]?.txt.bak', rules), 'deny')
        self.assertIsNone(pattern_policy('probe x1.txt', rules))
        self.assertIsNone(pattern_policy('prefix probe [x]?.txt.bak', rules))


if __name__ == '__main__':
    unittest.main()
