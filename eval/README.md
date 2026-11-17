# Phase 1 evaluation

This is a sequential Python standard-library harness around native OMP 18.22.0 print JSON sessions, not an orchestration framework. It uses only synthetic, newly allocated disposable Node projects. No installation, default-profile change, authentication import, or credential copying is performed.

## Prerequisites and run

The integration owner must first activate the parent-owned launcher (`bin/af --activate`) and authorize model access in the named `agent-first` profile. Existing `omp`, Python 3, Git, and a Node release supporting `node --test`, ES modules, and `structuredClone` must already be available. Do not pass credentials as arguments or put them in this repository. The runner uses the profile's existing authentication or the caller's authorized provider environment without recording that environment.

From this repository, run:

```sh
python3 eval/run.py --model PROVIDER/MODEL --max-time 600 --max-cost 1.5
```

Replace `PROVIDER/MODEL` with the integration owner's authorized explicit selector. The same selector is used for all three main sessions. Native child model routing is inherited from the profile; actual provider/model and usage evidence for every main and child session is retained. The runner does not silently choose a model, import authentication, retry a failed model on another provider, or resume a prior session.

To isolate an integrated failure, use an explicit case ID:

```sh
python3 eval/run.py --model PROVIDER/MODEL --case architecture-tenant-notes --max-time 600 --max-cost 1.5
```

Other IDs are `quick-duration` and `feature-cli-summary`. `--case` is repeatable. `--results PATH` selects the artifact parent, defaulting to gitignored `eval/results/`. Every run gets a new private directory. There is no dry-run result that can be mistaken for an actual pass.

## Authorization and bounds

The runner invokes `omp` directly with fixed absolute `profile/config.yml` then `eval/config.yml` overlays, `profile/APPEND_SYSTEM.md`, `--profile agent-first`, `--no-extensions`, `--print --mode json --wait-async`, an external `--session-dir`, and explicit model/time/cost limits. It does not pass yolo, an approval-mode override, arbitrary extra flags, or a different profile. Base write-mode and restricted-operation policy remain intact.

The evaluation-only overlay authorizes parent task calls. General eval is denied. Bash is prompted at tool level, then ordered command patterns permit only the exact standalone `node --test` and `git diff --no-ext-diff --no-textconv`, denying everything else. A tool-wide `bash: deny` would also deny those commands. Each fixture's AGENTS.md names the authorized checks; initial files are staged in a new local Git repository without making a commit, so the main agent can provide an actual patch to the bundled reviewer. Compound commands, installs, shell escapes, package-manager commands, and arbitrary `node -e` are not authorized. These evaluation grants do not change normal launcher policy. Agent frontmatter and actual child journals assess advisory behavior; neither approvals nor this harness is an OS sandbox. Generated tests retain the user's process permissions. Use only disposable synthetic projects.

The evaluation overlay sets `async.enabled: false` so task calls settle synchronously and expose deterministic native `details.results`, including `agentSource`. This scheduling difference is recorded in each case result and the batch summary. Normal profile async behavior is unchanged. `--wait-async` remains present; no text-only routing or source inspection substitutes for actual task, yield, tool, and child-journal evidence.

Per-case defaults are 600 native seconds and a USD 1.50 soft cost cap, for three sequential cases (USD 4.50 nominal batch cap). Accepted limits are 60 to 1200 seconds and USD 0.01 to 5 per case. A native request already in flight may overshoot its soft cost cap. There is also a subprocess deadline 30 seconds beyond the native deadline, and separate 30-second deadlines for each independent check. Child runs have an evaluation-only five-minute runtime and 60-request budget. All cases run even if an earlier one fails. No automatic paid retries occur.

## Coverage and evidence

Expected routing metadata lives only in the harness case definitions, not the synthetic user prompts:

- `quick-duration`: a localized fractional-seconds bug, expected quick change and no delegation.
- `feature-cli-summary`: a real end-to-end feature through a launched CLI, expected feature development. Consumer checks cover unchanged output, filtering, argument order, totals, credits, empty selections, and invalid options.
- `architecture-tenant-notes`: a breaking synchronous-to-asynchronous storage-boundary cutover protecting private tenant data. Requires an actual `af-architect` consultation before implementation and a bundled `reviewer` execution after implementation. Consumer checks cover adapter injection, migration of the example caller, rejection propagation, input validation before storage, same-ID tenant isolation, delimiter/prototype keys, and mutation ownership.

A route sentence alone never passes a case. The harness evaluates the first visible assistant prose, allowing the skill/context reads required before classification. It requires successful main inspection and implementation, a completed `node --test` after the last write, and independent consumer acceptance plus project tests. The architecture case requires actual tasks and retained child journals, inspected substantive advice, consultation/review chronology, native bundled-reviewer evidence, and a main review report. Verification must follow the final implementation change; review without further edits does not require rerunning an unchanged check. Every child is checked for attempted tools outside the advisory set, including denied attempts. Unexpected delegation types fail. Successful native structured yields count as completed advice.

Malformed/missing JSON events, missing main/child journals, missing tool results, missing terminal events, native nonzero exit, model abort/error, timeout, and failed acceptance checks fail visibly with a nonzero runner exit. Failed intermediate tool calls remain in `tool_failures` even if the agent repairs the issue and later passes. Independent acceptance code is stored outside the agent workspace and executed in a separate process with a minimal environment, without provider credentials or inherited `NODE_OPTIONS`. It tests consumer behavior rather than source-code spelling. Workspace tests are also independently rerun so deleting or weakening an agent-visible regression test cannot replace consumer acceptance.

Only JSONL files with a native session header are evaluated as conversations. Native edit-audit files such as `changes.jsonl` remain retained artifacts, not additional sessions.

Child provenance uses the ID in native synchronous `task` results, not a requested display name or every journal sharing an agent type. Empty, unreferenced startup journals remain diagnostic artifacts; referenced cancellations and non-advisory attempts still fail. The native-ID regression replays retained evidence and must preserve the real reviewer timeout while recognizing the completed architect consultation.

## Retained output and human assessment

Before the disposable workspace is deleted, each case retains:

- The natural prompt, independent consumer test, every actual argv/cwd/deadline/status, stdout, and stderr.
- Native print JSON events and the complete session/artifact directory, including child journals.
- `result.json`: explicit failures, observed route, tool calls/results, task dispatches, child activity, actual verification evidence, usage, and failed intermediate tools.
- `workspace.tar.gz` and a SHA-256/symlink manifest for the completed or failed workspace. Archive limits are 2000 entries and 10 MiB per regular file; incomplete retention is a visible failure. Symlinks are retained without following them.

The run-level `summary.json` is updated after each case. Results are private local diagnostic material, not automatically published. Authentication files, environment dumps, and prior profile sessions are never copied. Native journals can contain synthetic source, prompts, provider identifiers, usage, and pseudonymous credential-pin metadata; inspect before sharing.

Read the actual advice and main response in the retained journals when evaluating trade-off quality and reviewer finding disposition. Automated chronology and substantive-output checks prove consultation occurred, not that its reasoning was good. Record any inadequate evaluation of advice as a human-assessed failure rather than treating the route word as proof. Browser/runtime UI evaluation is not applicable to these non-UI fixtures. These cases do not prove filesystem containment or safety for real repositories.

