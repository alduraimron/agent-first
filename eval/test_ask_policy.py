#!/usr/bin/env python3
"""Guard the evaluation operator's narrowly scoped native approval responses."""
import io
import json
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace

from check_ask_policy import COMMANDS, Evidence, ProbeError, TARGETS


class ApprovalGuardTests(unittest.TestCase):
    def setUp(self):
        self.fixture = tempfile.TemporaryDirectory(prefix="af-approval-guards-")
        self.addCleanup(self.fixture.cleanup)
        self.workspace = Path(self.fixture.name).resolve()
        for target in TARGETS:
            (self.workspace / target).mkdir()
        self.result = {"failures": [], "checks": []}
        self.evidence = Evidence(self.workspace, self.result)
        self.process = SimpleNamespace(stdin=io.BytesIO())
        self.sent = io.BytesIO()

    def handle(self, event):
        self.evidence.handle(event, self.process, self.sent, "unused")

    def submit(self):
        target = self.workspace / TARGETS[0]
        self.handle({"type": "message_end", "message": {"role": "assistant", "content": [
            {"type": "text", "text": f"Command: {COMMANDS[0]}\nCwd: {self.workspace}\n"
             f"Target: {target}\nRemove only this empty directory. Risk: low, non-recursive. "
             "Rollback: recreate the empty directory."}]}})
        self.handle({"type": "tool_execution_start", "toolCallId": "owned-call", "toolName": "bash",
                     "args": {"command": COMMANDS[0], "cwd": str(self.workspace)}})

    def dialog(self, command=COMMANDS[0]):
        return {"type": "extension_ui_request", "id": "owned-dialog", "method": "select",
                "title": "Allow tool: bash\nReason: Prompt required by bash pattern: rmdir *\nCommand: " + command,
                "options": ["Approve", "Deny"]}

    def assert_denied(self, frame):
        with self.assertRaises(ProbeError):
            self.handle(frame)
        replies = [json.loads(line) for line in self.sent.getvalue().splitlines()]
        self.assertEqual(replies[-1], {"type": "extension_ui_response", "id": frame["id"], "value": "Deny"})
        self.assertTrue(self.result["failures"])

    def test_unbound_native_dialog_cannot_authorize_a_command(self):
        self.assert_denied(self.dialog())
        self.assertTrue(all((self.workspace / target).is_dir() for target in TARGETS))

    def test_different_target_cannot_reuse_a_valid_submission(self):
        self.submit()
        self.assert_denied(self.dialog("rmdir -- another-directory"))
        self.assertTrue(all((self.workspace / target).is_dir() for target in TARGETS))

    def test_symlink_replacement_before_approval_is_denied(self):
        self.submit()
        with tempfile.TemporaryDirectory(prefix="af-unapproved-target-") as outside:
            marker = Path(outside) / "keep.txt"
            marker.write_text("must remain untouched")
            target = self.workspace / TARGETS[0]
            target.rmdir()
            target.symlink_to(outside, target_is_directory=True)
            self.assert_denied(self.dialog())
            self.assertEqual(marker.read_text(), "must remain untouched")
            self.assertTrue(target.is_symlink())

    def test_repeated_approval_frame_never_grants_a_second_action(self):
        self.submit()
        self.handle(self.dialog())
        self.assert_denied(self.dialog())
        replies = [json.loads(line) for line in self.sent.getvalue().splitlines()]
        self.assertEqual([reply["value"] for reply in replies], ["Approve", "Deny"])
        self.assertTrue(all((self.workspace / target).is_dir() for target in TARGETS))


if __name__ == "__main__":
    unittest.main()
