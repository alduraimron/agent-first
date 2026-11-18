import json
import unittest

from check_plugin import catalog_names, settings_values


class PluginEvidenceTests(unittest.TestCase):
    def test_native_settings_map_preserves_mode_and_restrictions(self):
        baseline = {'tools.approvalMode': {'value': 'write', 'type': 'enum'},
                    'tools.approval': {'value': {'eval': 'deny'}, 'type': 'record'},
                    'bash.patterns': {'value': [{'match': 'printf secret', 'approval': 'deny'}]},
                    'auth.broker.url': {'type': 'string'}}
        values = settings_values(json.dumps(baseline))
        self.assertEqual(values['tools.approvalMode'], 'write')
        self.assertEqual(values['tools.approval'], {'eval': 'deny'})
        changed = dict(baseline, **{'tools.approvalMode': {'value': 'yolo'}})
        self.assertNotEqual(values, settings_values(json.dumps(changed)))
        changed = dict(baseline, **{'bash.patterns': {'value': []}})
        self.assertNotEqual(values, settings_values(json.dumps(changed)))

    def test_empty_or_invalid_settings_cannot_pass_inheritance(self):
        for value in ({}, [], {'settings': []}, {'tools.approvalMode': 'yolo'}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                settings_values(json.dumps(value))

    def test_compact_native_catalog_excludes_instruction_mentions(self):
        prompt = ('Always use skill://principle-prove-it-works.\n<skills>\n'
                  '- af-engineering: Route changes.\n- af-interaction: Route discussion.\n'
                  '- project-convention: Local guidance.\n</skills>\n'
                  '- interaction-how: This is outside the catalog.\n')
        self.assertEqual(catalog_names(prompt), {'af-engineering', 'af-interaction', 'project-convention'})

    def test_xml_catalog_is_also_supported(self):
        self.assertEqual(catalog_names('<skills><skill><name>af-context</name></skill></skills>'), {'af-context'})

    def test_missing_catalog_is_not_successful_empty_discovery(self):
        with self.assertRaises(ValueError):
            catalog_names('Instructions without a native catalog.')


if __name__ == '__main__':
    unittest.main()
