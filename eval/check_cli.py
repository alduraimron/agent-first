#!/usr/bin/env python3
"""Disposable CLI admission/setup checks; --native also exercises real default-model launches."""
import argparse
import json
import os
from pathlib import Path
import pty
import runpy
import select
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

from run import load_jsonl, run_command, save_json, text_content

ROOT = Path(__file__).resolve().parents[1]
AF = runpy.run_path(str(ROOT / "bin/af"), run_name="af_cli")


class LauncherChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="af-cli-check-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.home = self.base / "home"
        self.home.mkdir()
        self.project = self.base / "personal"
        self.project.mkdir()
        self.team = self.base / "team"
        self.team.mkdir()
        self.tools = self.base / "tools"
        self.tools.mkdir()
        self.called = self.base / "native-called"
        # Negative probes must stop before any native startup or model-role lookup.
        omp = self.tools / "omp"
        omp.write_text("#!" + sys.executable + "\nimport os\nfrom pathlib import Path\n"
                       "Path(os.environ['NATIVE_CALLED']).write_text('unexpected execution')\n"
                       "raise SystemExit(97)\n")
        omp.chmod(0o700)
        self.env = {"HOME": str(self.home), "LANG": "C.UTF-8", "TERM": "dumb",
                    "NATIVE_CALLED": str(self.called), "GIT_CONFIG_GLOBAL": os.devnull,
                    "GIT_CONFIG_SYSTEM": os.devnull,
                    "PATH": os.pathsep.join([str(self.home / ".local/bin"), str(self.tools),
                                             str(Path(sys.executable).parent),
                                             str(Path(shutil.which("git")).parent), "/usr/bin", "/bin"])}

    def invoke(self, *args, cwd=None, global_command=False):
        return subprocess.run(["af" if global_command else str(ROOT / "bin/af"), *args],
                              cwd=cwd or self.project, env=self.env, stdin=subprocess.DEVNULL,
                              capture_output=True, text=True, timeout=15)

    def git(self, directory, *args):
        subprocess.run([shutil.which("git"), "-C", str(directory), *args], env=self.env,
                       check=True, capture_output=True, timeout=10)

    def enroll(self, directory):
        result = self.invoke("--trust-project", cwd=directory)
        self.assertEqual(result.returncode, 0, result.stderr)

    def approved(self, directory):
        with patch.dict(os.environ, self.env, clear=True):
            return AF["is_personal"](AF["project_identity"](directory.resolve()))

    def refused(self, directory, *args):
        result = self.invoke(*args, "--json", "--", "Do not change files", cwd=directory)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("not approved as personal", result.stderr)
        self.assertFalse(self.called.exists(), "Native OMP ran for an unapproved project")

    def test_setup_global_command_works_away_from_checkout(self):
        self.assertEqual(self.invoke("--setup").returncode, 0)
        self.assertEqual(self.invoke("--setup").returncode, 0)
        result = self.invoke("--help", cwd=self.team, global_command=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--cwd", result.stdout)
        self.assertEqual((self.home / ".local/bin/af").resolve(), ROOT / "bin/af")
        self.assertFalse(self.approved(self.project), "Setup implicitly enrolled its cwd")
        self.assertFalse(self.called.exists())

    def test_setup_preserves_existing_command(self):
        target = self.home / ".local/bin/af"
        target.parent.mkdir(parents=True)
        target.write_text("existing user command\n")
        result = self.invoke("--setup")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(target.read_text(), "existing user command\n")
        self.assertFalse((self.home / ".omp").exists())

    def test_setup_preserves_foreign_broken_symlink(self):
        target = self.home / ".local/bin/af"
        target.parent.mkdir(parents=True)
        target.symlink_to(self.base / "missing")
        self.assertEqual(self.invoke("--setup").returncode, 2)
        self.assertEqual(os.readlink(target), str(self.base / "missing"))

    def test_setup_refuses_another_path_command(self):
        shadow = self.tools / "af"
        shadow.write_text("#!/bin/sh\nexit 91\n")
        shadow.chmod(0o700)
        self.assertEqual(self.invoke("--setup").returncode, 2)
        self.assertFalse((self.home / ".local/bin/af").exists())
        self.assertFalse((self.home / ".omp").exists())

    def test_unknown_team_project_never_starts_native_omp(self):
        marker = self.team / "README.md"
        marker.write_text("Team-owned fixture, not a personal approval\n")
        self.refused(self.team)
        self.assertEqual(marker.read_text(), "Team-owned fixture, not a personal approval\n")
        self.assertFalse((self.home / ".omp").exists())
        self.assertFalse((self.team / ".agent-first").exists())

    def test_cwd_flag_is_not_project_consent(self):
        self.enroll(self.project)
        self.refused(self.project, "--cwd", str(self.team))

    def test_default_interactive_answer_declines(self):
        master, slave = pty.openpty()
        process = subprocess.Popen([str(ROOT / "bin/af")], cwd=self.team, env=self.env,
                                   stdin=slave, stdout=slave, stderr=slave)
        os.close(slave)
        captured = bytearray()
        try:
            deadline = time.monotonic() + 8
            while b"[y/N]" not in captured and time.monotonic() < deadline:
                if select.select([master], [], [], max(0, deadline - time.monotonic()))[0]:
                    captured.extend(os.read(master, 65536))
            self.assertIn(b"[y/N]", captured)
            os.write(master, b"\n")
            self.assertEqual(process.wait(timeout=5), 2)
            self.assertFalse(self.called.exists())
            self.assertFalse(self.approved(self.team))
            self.assertFalse((self.home / ".omp").exists())
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()
            os.close(master)

    def test_global_command_enrolls_actual_cwd_and_cwd_override(self):
        self.assertEqual(self.invoke("--setup").returncode, 0)
        self.assertEqual(self.invoke("--trust-project", global_command=True).returncode, 0)
        self.assertTrue(self.approved(self.project))
        second = self.base / "another-personal"
        second.mkdir()
        self.assertFalse(self.approved(second))
        result = self.invoke("--cwd", str(second), "--trust-project", global_command=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(self.approved(second))
        self.assertEqual(self.invoke("--cwd", str(second), "--untrust-project",
                                     global_command=True).returncode, 0)
        self.assertTrue(self.approved(self.project))
        self.refused(second)

    def test_registration_does_not_change_project_or_default_profile(self):
        note = self.project / "README.md"
        note.write_text("Personal fixture\n")
        default = self.home / ".omp/agent/config.yml"
        default.parent.mkdir(parents=True)
        default.write_text("# Existing default profile\n")
        self.enroll(self.project)
        self.assertEqual(note.read_text(), "Personal fixture\n")
        self.assertEqual(default.read_text(), "# Existing default profile\n")
        self.assertFalse((self.project / ".agent-first").exists())
        self.assertFalse(self.called.exists())
        record = next((self.home / ".config/agent-first/projects").glob("*.json"))
        self.assertEqual(record.stat().st_mode & 0o777, 0o600)

    def test_non_git_parent_does_not_approve_descendants(self):
        self.enroll(self.project)
        child = self.project / "another-project"
        child.mkdir()
        self.refused(child)

    def test_git_subdirectory_reuses_only_its_repository_approval(self):
        self.git(self.project, "init", "--quiet")
        self.enroll(self.project)
        child = self.project / "src"
        child.mkdir()
        self.assertTrue(self.approved(child))
        nested = child / "team-repository"
        nested.mkdir()
        self.git(nested, "init", "--quiet")
        self.refused(nested)

    def test_symlink_cannot_borrow_personal_parent_approval(self):
        self.enroll(self.project)
        alias = self.project / "team-link"
        alias.symlink_to(self.team, target_is_directory=True)
        self.refused(alias)

    def test_changed_remote_requires_new_personal_consent(self):
        self.git(self.project, "init", "--quiet")
        self.enroll(self.project)
        remote = "https://token-for-test@example.invalid/team/repository.git"
        self.git(self.project, "remote", "add", "origin", remote)
        self.refused(self.project)
        self.enroll(self.project)
        self.assertTrue(self.approved(self.project))
        record = next((self.home / ".config/agent-first/projects").glob("*.json"))
        self.assertNotIn(remote, record.read_text())

    def test_replaced_repository_requires_new_consent(self):
        self.git(self.project, "init", "--quiet")
        self.enroll(self.project)
        (self.project / ".git").rename(self.project / "old-git")
        self.git(self.project, "init", "--quiet")
        self.refused(self.project)

    def test_git_environment_cannot_redirect_project_selection(self):
        self.git(self.project, "init", "--quiet")
        self.git(self.team, "init", "--quiet")
        self.env.update(GIT_DIR=str(self.team / ".git"), GIT_WORK_TREE=str(self.team))
        self.enroll(self.project)
        self.assertTrue(self.approved(self.project))
        self.assertFalse(self.approved(self.team))

    def test_corrupt_approval_fails_closed_without_replacement(self):
        self.enroll(self.project)
        record = next((self.home / ".config/agent-first/projects").glob("*.json"))
        record.write_text("invalid user record\n")
        result = self.invoke("--json", "Inspect this project")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Invalid personal-project approval", result.stderr)
        self.assertEqual(record.read_text(), "invalid user record\n")
        self.assertFalse(self.called.exists())


def native_launches(output):
    """Actual af execution, model identity, and cwd-relative consumer reads."""
    if Path(shutil.which("af") or "").resolve() != ROOT / "bin/af":
        raise RuntimeError("Run bin/af --setup first; af on PATH must resolve to this launcher")
    native_env = os.environ.copy()
    for key in ("PI_CONFIG_FILES", "PI_CODING_AGENT_DIR", "PI_SESSION_ID", "PI_SESSION_FILE", "PI_TOOL_CALL_ID"):
        native_env.pop(key, None)
    native_env.update(OMP_PROFILE="agent-first", PI_PROFILE="agent-first")
    records, failures = [], []
    with tempfile.TemporaryDirectory(prefix="af-cli-native-") as temporary:
        projects = [Path(temporary) / "personal one", Path(temporary) / "personal two"]
        try:
            for index, project in enumerate(projects):
                project.mkdir()
                subprocess.run([shutil.which("git"), "-c", "init.templateDir=", "init", "--quiet", str(project)],
                               check=True, capture_output=True, timeout=10)
                (project / "project.txt").write_text(f"AF_PERSONAL_PROJECT_{index + 1}\n")
                enrollment = run_command(["af", "--trust-project"], project, output,
                                         f"enroll-{index}", 30, native_env)
                if enrollment["status"] != "pass":
                    raise RuntimeError("Disposable personal enrollment failed")
            scenarios = [(projects[0], projects[0], []), (projects[1], projects[1], []),
                         (projects[0], projects[1], ["--cwd", str(projects[1])])]
            for index, (cwd, target, flags) in enumerate(scenarios):
                roles = {}
                for profile in ("agent-first", None):
                    env = dict(native_env)
                    command = [shutil.which("omp"), "--cwd", str(target)]
                    if profile:
                        command.extend(["--profile", profile, "--config", str(ROOT / "profile/config.yml")])
                    else:
                        env.pop("OMP_PROFILE", None)
                        env.pop("PI_PROFILE", None)
                    role_result = subprocess.run(command + ["config", "get", "modelRoles", "--json"],
                                                 env=env, capture_output=True, text=True, timeout=30, check=True)
                    roles = json.loads(role_result.stdout)["value"]
                    if roles.get("default"):
                        break
                selector = roles.get("default")
                if not selector or "/" not in selector:
                    raise RuntimeError("Native identity comparison requires a configured provider/model default role")
                canonical = selector
                if selector.rpartition(":")[2] in {"off", "minimal", "low", "medium", "high", "xhigh", "max", "auto"}:
                    canonical = selector.rpartition(":")[0]
                prompt = ("Read project.txt using the native read tool and report its exact contents. "
                          "Do not edit files, run commands, delegate, or install anything. "
                          "This is a verification-only request in an explicitly approved disposable personal project.")
                command = run_command(["af", *flags, "--json", "--max-time", "120", "--max-cost", "0.5", "--", prompt],
                                      cwd, output, f"native-{index}", 150, native_env)
                events = load_jsonl(output / f"native-{index}.stdout", failures)
                marker = (target / "project.txt").read_text().strip()
                sessions = [event for event in events if event["type"] == "session"]
                reads = [event for event in events if event["type"] == "tool_execution_end"
                         and event.get("toolName") == "read" and not event.get("isError")
                         and marker in text_content(event.get("result", {}))]
                models = {f"{event['message']['provider']}/{event['message']['model']}" for event in events
                          if event["type"] == "message_end" and event.get("message", {}).get("role") == "assistant"}
                passed = (command["status"] == "pass" and any(event["type"] == "agent_end" for event in events)
                          and len(sessions) == 1 and sessions[0]["cwd"] == str(target)
                          and bool(reads) and models == {canonical})
                record = {"status": "PASS" if passed else "FAIL", "cwd": str(cwd), "project": str(target),
                          "configured_selector": selector, "observed_models": sorted(models),
                          "actual_project_read": bool(reads), "command": command}
                records.append(record)
                if not passed:
                    failures.append(f"Native launch {index} did not establish cwd/model/read behavior")
        finally:
            for index, project in enumerate(projects):
                if project.is_dir():
                    cleanup = run_command(["af", "--untrust-project"], project, output,
                                          f"forget-{index}", 30, native_env)
                    if cleanup["status"] != "pass":
                        failures.append(f"Could not revoke disposable project {project}")
    return {"status": "FAIL" if failures else "PASS", "launches": records, "failures": failures}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--native", action="store_true", help="also run three real default-model launches after user-local setup")
    options = parser.parse_args()
    if shutil.which("git") is None:
        parser.error("Existing Git is required; nothing will be installed")
    results = ROOT / "eval/results"
    results.mkdir(exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix="cli-check-", dir=results))
    output.chmod(0o700)
    with (output / "tests.txt").open("w") as stream:
        run = unittest.TextTestRunner(stream=stream, verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(LauncherChecks))
    result = {"status": "PASS" if run.wasSuccessful() else "FAIL", "tests_run": run.testsRun,
              "failures": len(run.failures), "errors": len(run.errors), "artifacts": str(output)}
    if options.native and run.wasSuccessful():
        try:
            result["native"] = native_launches(output)
        except Exception as error:
            result["native"] = {"status": "FAIL", "error": f"{type(error).__name__}: {error}"}
        if result["native"]["status"] != "PASS":
            result["status"] = "FAIL"
    save_json(output / "result.json", result)
    print(json.dumps(result, indent=2))
    return result["status"] != "PASS"


if __name__ == "__main__":
    sys.exit(main())
