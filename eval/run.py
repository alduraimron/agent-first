#!/usr/bin/env python3
"""Sequential native OMP evaluations. Python standard library only."""
import argparse
import contextlib
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
READ_ONLY = {"read", "grep", "glob", "yield"}
MUTATING = {"edit", "write", "ast_edit", "delete", "move"}
AGENTS = {"af-architect", "af-database", "af-security", "af-frontend",
          "af-performance", "af-devops", "reviewer"}
ROUTES = {"quick-change", "feature-development", "architecture-impacting",
          "project-initialization", "bug-investigation", "refactoring",
          "code-review", "performance-optimization"}


def save_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=True) + "\n")


def run_command(argv, cwd, output, label, timeout, env):
    """Never use a shell; retain output even on timeout or launch failure."""
    record = {"argv": [str(arg) for arg in argv], "cwd": str(cwd),
              "timeout_seconds": timeout, "status": "not-run"}
    start = time.monotonic()
    with (output / f"{label}.stdout").open("wb") as stdout, (output / f"{label}.stderr").open("wb") as stderr:
        try:
            process = subprocess.Popen(record["argv"], cwd=cwd, env=env,
                                       stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                       start_new_session=True)
            try:
                record["returncode"] = process.wait(timeout=timeout)
                record["status"] = "pass" if process.returncode == 0 else "fail"
            except subprocess.TimeoutExpired:
                record["status"] = "timeout"
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                record["returncode"] = process.returncode
        except OSError as error:
            record["status"] = "launch-error"
            record["error"] = str(error)
    record["duration_seconds"] = round(time.monotonic() - start, 3)
    record["stdout"] = f"{label}.stdout"
    record["stderr"] = f"{label}.stderr"
    save_json(output / f"{label}.command.json", record)
    return record


def load_jsonl(path, failures):
    records = []
    try:
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
                if not isinstance(item, dict) or not isinstance(item.get("type"), str):
                    raise ValueError("event must be an object with a string type")
                records.append(item)
            except (ValueError, TypeError) as error:
                failures.append(f"Malformed event {path.name}:{number}: {error}")
    except (OSError, UnicodeError) as error:
        failures.append(f"Cannot read evidence {path.name}: {error}")
    if not records:
        failures.append(f"Missing events in {path.name}")
    return records


def is_session_journal(path):
    """Audit JSONL files are artifacts, not conversation journals."""
    try:
        with path.open(encoding="utf-8") as stream:
            entry = json.loads(stream.readline())
            if isinstance(entry, dict) and entry.get("type") == "title":
                entry = json.loads(stream.readline())
            return isinstance(entry, dict) and entry.get("type") == "session"
    except (OSError, ValueError, UnicodeError):
        return False


def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)


def text_content(message):
    content = message.get("content", [])
    if isinstance(content, str):
        return content
    return "\n".join(block.get("text", "") for block in content
                     if isinstance(block, dict) and block.get("type") == "text")


def timestamp(entry):
    value = entry.get("timestamp")
    if isinstance(value, (int, float)):
        return value / 1000
    if isinstance(value, str):
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()
    raise ValueError("Missing timestamp in session evidence")


def journal_evidence(path, records):
    header = next((entry for entry in records if entry["type"] == "session"), None)
    if not header or not header.get("id"):
        raise ValueError(f"Missing session header in {path.name}")
    calls, results, assistant = [], {}, []
    agent = None
    for entry in records:
        if entry["type"] == "session_init":
            agent = entry.get("agent", agent)
        if entry["type"] != "message":
            continue
        message = entry.get("message", {})
        if message.get("role") == "assistant":
            assistant.append({"time": timestamp(entry), "text": text_content(message),
                              "stopReason": message.get("stopReason"),
                              "provider": message.get("provider"), "model": message.get("model"),
                              "usage": message.get("usage")})
            for block in message.get("content", []):
                if isinstance(block, dict) and block.get("type") == "toolCall":
                    if not isinstance(block.get("id"), str) or not isinstance(block.get("arguments"), dict):
                        raise ValueError(f"Malformed toolCall in {path.name}")
                    calls.append({"id": block["id"], "name": block.get("name"),
                                  "arguments": block["arguments"], "time": timestamp(entry)})
        elif message.get("role") == "toolResult":
            results[message.get("toolCallId")] = {"time": timestamp(entry),
                "isError": bool(message.get("isError")), "details": message.get("details"),
                "text": text_content(message)}
    for call in calls:
        call["result"] = results.get(call["id"])
    return {"path": str(path), "id": header["id"], "agent": agent,
            "calls": calls, "assistant": assistant}


def mutation_paths(call):
    if call["name"] not in MUTATING:
        return []
    args = call["arguments"]
    if args.get("path"):
        return [args["path"]]
    return re.findall(r"\[([^\]\n]+)#[0-9A-F]{4}\]", args.get("input", ""))


def workspace_mutation(call, include_context=False):
    if call["name"] not in MUTATING:
        return False
    targets = mutation_paths(call)
    if targets and all("://" in target for target in targets):
        return False
    if not include_context and targets and all(
            ".agent-first" in Path(target).parts for target in targets):
        return False
    return True


def inspect_evidence(case, output, workspace, failures):
    events = load_jsonl(output / "omp.stdout", failures)
    if not any(event["type"] == "session" for event in events):
        failures.append("Print JSON session header is missing")
    if not any(event["type"] == "agent_end" for event in events):
        failures.append("Print JSON terminal agent_end is missing")
    session_root = output / "sessions"
    roots = sorted(path for path in session_root.glob("*.jsonl") if is_session_journal(path))
    if len(roots) != 1:
        failures.append(f"Expected one main session journal, found {len(roots)}")
        return {"events": len(events), "sessions": []}
    journals, raw = [], []
    for path in sorted(path for path in session_root.rglob("*.jsonl") if is_session_journal(path)):
        records = load_jsonl(path, failures)
        raw.extend(records)
        try:
            journals.append(journal_evidence(path, records))
        except (ValueError, TypeError, KeyError) as error:
            failures.append(str(error))
    main = next((journal for journal in journals if journal["path"] == str(roots[0])), None)
    if not main:
        failures.append("Main journal is unreadable")
        return {"events": len(events), "sessions": journals}
    children = [journal for journal in journals if journal is not main]
    calls = main["calls"]
    assistant = main["assistant"]
    prose = "\n".join(message["text"] for message in assistant)
    expected_route = case["route"]
    opening = next((message["text"] for message in assistant if message["text"].strip()), "")
    match = re.search(r"Workflow:\s*(" + "|".join(sorted(ROUTES)) + r")\b", opening)
    route = match.group(1) if match else None
    if route != expected_route:
        failures.append(f"Opening classification missing or incorrect: expected {expected_route}, observed {route}")
    if not calls:
        failures.append("No actual main tool calls recorded")
    if not any(call["name"] in {"read", "grep", "glob", "ast_grep"} and call["result"] and not call["result"]["isError"] for call in calls):
        failures.append("No successful main inspection tool recorded")
    mutations = [call for call in calls if workspace_mutation(call)]
    if case.get("require_mutation", True) and not any(
            call["result"] and not call["result"]["isError"] for call in mutations):
        failures.append("No successful main implementation write recorded")
    if not case.get("allow_mutation", True) and any(workspace_mutation(call, True) for call in calls):
        failures.append("Read-only request attempted a workspace mutation")
    task_calls = [call for call in calls if call["name"] == "task"]
    requested = []
    for call in task_calls:
        args = call["arguments"]
        native_results = ((call["result"] or {}).get("details") or {}).get("results", [])
        for index, item in enumerate(args.get("tasks", [args])):
            native = next((result for result in native_results
                           if result.get("index") == index and result.get("agent") == item.get("agent")), {})
            requested.append({"agent": item.get("agent"), "name": item.get("name"),
                              "native_id": native.get("id"), "agent_source": native.get("agentSource"),
                              "time": call["time"], "result": call["result"]})
    if case["forbid_delegation"] and (task_calls or children):
        failures.append("Trivial quick change delegated work")
    for call in calls:
        if call["result"] is None:
            failures.append(f"Main tool has no result: {call['name']} ({call['id']})")
        if call["name"] == "eval":
            failures.append("Main attempted forbidden general eval execution")
        if call["name"] == "bash" and call["arguments"].get("command", "").strip() not in {
                "node --test", "git diff --no-ext-diff --no-textconv"}:
            failures.append(f"Main attempted a non-allowlisted shell command: {call['arguments'].get('command')}")
    verified = []
    for call in calls:
        if call["name"] != "bash" or call["arguments"].get("command", "").strip() != "node --test":
            continue
        result = call["result"]
        cwd = Path(call["arguments"].get("cwd") or workspace)
        if not cwd.is_absolute():
            cwd = workspace / cwd
        if cwd.resolve() != workspace.resolve():
            continue
        if result and not result["isError"] and not (result.get("details") or {}).get("async") and not (result.get("details") or {}).get("timedOut"):
            verified.append(call)
    final_mutation = max((call["time"] for call in mutations), default=0)
    if case.get("require_verification", True):
        if not any(call["time"] > final_mutation for call in verified):
            failures.append("No successful actual node --test after the last implementation write")
        if "node --test" not in prose:
            failures.append("Main report does not name the actual verification command")
    final_report = next((message["text"] for message in reversed(assistant) if message["text"].strip()), "")
    for pattern in case.get("report_patterns", []):
        if not re.search(pattern, final_report, re.IGNORECASE):
            failures.append(f"Final evidence report does not satisfy: {pattern}")
    for path in case.get("context_reads", []):
        if not any(call["name"] == "read" and path in call["arguments"].get("path", "")
                   and call["result"] and not call["result"]["isError"] for call in calls):
            failures.append(f"Authoritative context was not read: {path}")
    if case.get("expect_denied_check"):
        attempts = [call for call in calls if call["name"] == "bash"
                    and call["arguments"].get("command", "").strip() == "node --test"]
        if not attempts or not any(call["result"] and call["result"]["isError"] for call in attempts):
            failures.append("Required approval-denied test submission was not observed")
        if verified:
            failures.append("A check ran despite the expected headless approval boundary")
    if case.get("expect_failed_check"):
        attempts = [call for call in calls if call["name"] == "bash"
                    and call["arguments"].get("command", "").strip() == "node --test"]
        if len(attempts) != 1 or not attempts[0]["result"] or not attempts[0]["result"]["isError"]:
            failures.append("Exactly one executed failing check was not observed")
        elif "intentional fixture failure" not in attempts[0]["result"]["text"]:
            failures.append("Check error does not establish the expected executed failure")
    if case.get("require_measurement"):
        measured = [call for call in verified if re.search(r"MEASURE\s+\d", call["result"]["text"])]
        if not mutations or not any(call["time"] < min(item["time"] for item in mutations) for call in measured):
            failures.append("No actual baseline measurement before optimization")
        if not any(call["time"] > final_mutation for call in measured):
            failures.append("No comparable actual measurement after optimization")
    referenced_ids = {request["native_id"] for request in requested if request["native_id"]}
    bootstrap_journals = [child["path"] for child in children
                          if not child["calls"] and Path(child["path"]).stem not in referenced_ids]
    for child in children:
        for call in child["calls"]:
            if call["name"] not in READ_ONLY:
                failures.append(f"Advisory child {Path(child['path']).stem} attempted non-read-only tool {call['name']}")
            if call["result"] is None:
                failures.append(f"Child tool has no result: {Path(child['path']).stem}/{call['id']}")
        if child["path"] not in bootstrap_journals and any(
                message["stopReason"] in {"error", "aborted"} for message in child["assistant"]):
            failures.append(f"Child failed or aborted: {Path(child['path']).stem}")
    for request in requested:
        if request["agent"] not in AGENTS:
            failures.append(f"Unexpected delegation type: {request['agent']}")
    for agent in case["required_agents"]:
        requests = [request for request in requested if request["agent"] == agent and request["result"] and not request["result"]["isError"]]
        matching = [child for child in children if child["agent"] == agent
                    and any(request["native_id"] == Path(child["path"]).stem for request in requests)]
        if not requests or not matching:
            failures.append(f"Missing actual {agent} task execution and child journal")
            continue
        complete = []
        for child in matching:
            inspected = any(call["name"] in READ_ONLY - {"yield"} and call["result"] and not call["result"]["isError"] for call in child["calls"])
            advice = [message["time"] for message in child["assistant"] if len(message["text"].strip()) >= 40 and message["stopReason"] == "stop"]
            advice.extend(call["time"] for call in child["calls"]
                          if call["name"] == "yield" and call["result"] and not call["result"]["isError"]
                          and len(json.dumps(call["arguments"])) >= 40)
            if not inspected or not advice:
                failures.append(f"No completed, inspected substantive advice from {agent}")
            else:
                complete.append(max(advice))
        for item in objects(events + raw):
            if item.get("agent") == agent and isinstance(item.get("exitCode"), int) and item["exitCode"] != 0:
                failures.append(f"Native {agent} result reports failure (code {item['exitCode']})")
        if agent == "af-architect" and case.get("architect_before_mutation"):
            if not complete or not mutations or min(complete) >= min(call["time"] for call in mutations):
                failures.append("Architect consultation did not finish before implementation")
        if agent == "reviewer" and case.get("review_after_mutation"):
            if not complete or not mutations or max(complete) <= min(call["time"] for call in mutations):
                failures.append("Independent review did not follow an implementation write")
            if not re.search(r"review|finding", prose, re.IGNORECASE):
                failures.append("Main did not report evaluating independent review")
            if not any(item.get("agent") == "reviewer" and item.get("agentSource") == "bundled" for item in objects(events + raw)):
                failures.append("Reviewer source not evidenced as bundled in native task result")
    if any(message["stopReason"] in {"error", "aborted"} for message in assistant):
        failures.append("Main assistant failed or aborted")
    return {"events": len(events), "route": route, "expected_route": expected_route, "requested_agents": requested,
            "verification_calls": verified, "sessions": journals,
            "unreferenced_empty_journals": bootstrap_journals,
            "tool_failures": [{"session": journal["path"], **call} for journal in journals
                              for call in journal["calls"] if call["result"] and call["result"]["isError"]]}


def archive_workspace(workspace, output, failures):
    manifest = {}
    with tarfile.open(output / "workspace.tar.gz", "w:gz", dereference=False) as archive:
        for index, path in enumerate(sorted(workspace.rglob("*"))):
            if index >= 2000:
                failures.append("Workspace archive exceeded 2000 entries")
                break
            name = str(path.relative_to(workspace))
            if path.is_symlink():
                manifest[name] = {"symlink": os.readlink(path)}
            elif path.is_file():
                if path.stat().st_size > 10 * 1024 * 1024:
                    failures.append(f"Workspace artifact too large to retain: {name}")
                    continue
                manifest[name] = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            elif not path.is_dir():
                failures.append(f"Unsupported workspace artifact: {name}")
                continue
            archive.add(path, arcname=name, recursive=False)
    save_json(output / "workspace-manifest.json", manifest)


def run_case(case, options, run_dir, omp, node, git):
    output = run_dir / case["id"]
    output.mkdir(mode=0o700)
    (output / "sessions").mkdir()
    (output / "acceptance.test.mjs").write_text(case["acceptance"])
    (output / "prompt.txt").write_text(case["prompt"] + "\n")
    failures = []
    result = {"id": case["id"], "failures": failures, "commands": [],
              "evaluation_scheduling": ("synchronous task settlement (async.enabled=false)"
                                       if case.get("approval", "evaluation") == "evaluation"
                                       else "normal profile approvals and native async scheduling"),
              "normal_profile_scheduling": "native async behavior unchanged"}
    if options.keep_workspaces:
        (output / "workspace").mkdir()
        allocation = contextlib.nullcontext(str(output / "workspace"))
    else:
        allocation = tempfile.TemporaryDirectory(prefix=f"af-{case['id']}-")
    with allocation as temporary:
        workspace = Path(temporary)
        result["disposable_workspace"] = str(workspace)
        for name, content in case["files"].items():
            target = workspace / name
            if Path(name).is_absolute() or ".." in Path(name).parts:
                raise ValueError(f"Unsafe fixture filename: {name}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
        (workspace / "AGENTS.md").write_text(
            "# Disposable personal evaluation project\n\n"
            "Use the installed command `node --test` directly for verification. "
            "Headless evaluation authorizes that exact command and "
            "`git diff --no-ext-diff --no-textconv`; other shell commands and eval are denied. "
            "Read skills with the direct read tool, not eval. The initial files are staged, "
            "not committed, so the main agent can obtain "
            "a real patch for advisory review. Supply that patch to the reviewer; "
            "advisory children do not execute shell commands. Do not install dependencies.\n"
        )
        consumer_env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                        "LANG": "C.UTF-8", "AF_WORKSPACE": str(workspace),
                        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull}
        for label, args in (("git-init", [git, "-c", "init.templateDir=", "init", "--quiet"]),
                            ("git-stage", [git, "add", "--", "."])):
            setup = run_command(args, workspace, output, label, 30, consumer_env)
            result["commands"].append(setup)
            if setup["status"] != "pass":
                failures.append(f"Disposable Git baseline {label} failed; native session not launched")
        argv = [omp, "--profile", "agent-first", "--cwd", str(workspace),
                "--config", str(ROOT / "profile/config.yml")]
        if case.get("approval", "evaluation") == "evaluation":
            argv.extend(("--config", str(ROOT / "eval/config.yml")))
        argv.extend([
                "--append-system-prompt", str(ROOT / "profile/APPEND_SYSTEM.md"),
                "--no-extensions", "--no-title", "--print", "--mode", "json", "--wait-async",
                "--session-dir", str(output / "sessions"), "--model", options.model,
                "--max-time", str(options.max_time), "--max-cost", str(options.max_cost),
                "--", case["prompt"]])
        native_env = dict(os.environ)
        for key in ("PI_SESSION_ID", "PI_SESSION_FILE", "PI_TOOL_CALL_ID",
                    "PI_CONFIG_FILES", "PI_CODING_AGENT_DIR"):
            native_env.pop(key, None)
        native_env["OMP_PROFILE"] = "agent-first"
        native_env["PI_PROFILE"] = "agent-first"
        if not failures:
            try:
                command = run_command(argv, workspace, output, "omp", options.max_time + 30, native_env)
                result["commands"].append(command)
                if command["status"] != "pass":
                    failures.append(f"Native OMP ended with {command['status']} (code {command.get('returncode')})")
                result["evidence"] = inspect_evidence(case, output, workspace, failures)
            except (OSError, ValueError, TypeError, KeyError) as error:
                failures.append(f"Native evidence processing failed: {error}")
        protected = case.get("protected_files", [])
        if not case.get("allow_mutation", True):
            protected = list(case["files"])
        for name in protected:
            target = workspace / name
            if not target.is_file() or target.read_text() != case["files"][name]:
                failures.append(f"Protected source changed: {name}")
        # Acceptance is a separate consumer process with no model credentials or NODE_OPTIONS.
        checks = [("consumer", [node, "--test", str(output / "acceptance.test.mjs")])]
        if case.get("run_project_tests", True):
            checks.append(("project-tests", [node, "--test"]))
        for label, args in checks:
            command = run_command(args, workspace, output, label, 30, consumer_env)
            result["commands"].append(command)
            if command["status"] != "pass":
                failures.append(f"Independent {label} check {command['status']} (code {command.get('returncode')})")
        try:
            archive_workspace(workspace, output, failures)
        except OSError as error:
            failures.append(f"Workspace artifact retention failed: {error}")
        result["status"] = "fail" if failures else "pass"
        save_json(output / "result.json", result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="One explicit provider/model selector for every case")
    parser.add_argument("--case", action="append", dest="cases", help="Run only this case ID (repeatable)")
    parser.add_argument("--max-time", type=int, default=600, help="Per-case native seconds, 60..1200 (default 600)")
    parser.add_argument("--max-cost", type=float, default=1.5, help="Per-case native USD soft cap, 0.01..5 (default 1.5)")
    parser.add_argument("--results", type=Path, default=ROOT / "eval/results")
    parser.add_argument("--suite", choices=("phase1", "full"), default="full")
    parser.add_argument("--keep-workspaces", action="store_true",
                        help="Retain synthetic workspaces under private results for live browser checks")
    options = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_./:@+\[\]-]+", options.model):
        parser.error("--model must be one provider/model selector without whitespace or flags")
    if not 60 <= options.max_time <= 1200:
        parser.error("--max-time must be between 60 and 1200 seconds")
    if not math.isfinite(options.max_cost) or not 0.01 <= options.max_cost <= 5:
        parser.error("--max-cost must be finite and between 0.01 and 5 USD")
    cases = json.loads((ROOT / "eval/cases.json").read_text())["cases"]
    if options.suite == "full":
        cases.extend(json.loads((ROOT / "eval/extended-cases.json").read_text())["cases"])
        cases.extend(json.loads((ROOT / "eval/ui-case.json").read_text())["cases"])
    if options.cases:
        unknown = set(options.cases) - {case["id"] for case in cases}
        if unknown:
            parser.error(f"Unknown case IDs: {', '.join(sorted(unknown))}")
        cases = [case for case in cases if case["id"] in options.cases]
    omp, node, git = shutil.which("omp"), shutil.which("node"), shutil.which("git")
    if not omp or not node or not git:
        parser.error("Existing omp, node and git executables are required; nothing will be installed")
    for path in (ROOT / "profile/config.yml", ROOT / "profile/APPEND_SYSTEM.md"):
        if not path.is_file():
            parser.error(f"Integrated profile prerequisite missing: {path}")
    options.results = options.results.expanduser().resolve()
    options.results.mkdir(parents=True, exist_ok=True)
    run_dir = Path(tempfile.mkdtemp(prefix=dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ-"), dir=options.results))
    summary = {"model": options.model, "max_time_seconds_per_case": options.max_time,
               "evaluation_async_enabled": False, "normal_profile_async_unchanged": True,
               "max_cost_usd_per_case": options.max_cost, "max_cost_usd_batch_soft_cap": len(cases) * options.max_cost,
               "artifacts": str(run_dir), "cases": []}
    save_json(run_dir / "summary.json", summary)
    print(f"Artifacts: {run_dir}", flush=True)
    for case in cases:
        try:
            result = run_case(case, options, run_dir, omp, node, git)
        except Exception as error:
            result = {"id": case["id"], "status": "fail", "failures": [f"Harness error: {type(error).__name__}: {error}"]}
            save_json(run_dir / case["id"] / "result.json", result)
        summary["cases"].append(result)
        save_json(run_dir / "summary.json", summary)
        print(f"{result['status'].upper()}: {case['id']}", flush=True)
        for failure in result["failures"]:
            print(f"  {failure}", flush=True)
    summary["status"] = "pass" if all(case["status"] == "pass" for case in summary["cases"]) else "fail"
    save_json(run_dir / "summary.json", summary)
    return 0 if summary["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
