# Native system evaluation

This is a sequential Python standard-library harness around native OMP 18.22.0 print JSON sessions, not an orchestration framework. It uses only synthetic, newly allocated disposable Node projects. No installation, default-profile change, authentication import, or credential copying is performed.

## Prerequisites and run

Activate `bin/af --activate` and authorize model access in the named `agent-first` profile first. Existing OMP, Python 3, Git, and Node must already be available. Original cases need Node 18+; the full SQLite case uses existing Node 24+ and its built-in SQLite module. Do not pass credentials as arguments or put them in this repository. The runner uses existing profile authentication without recording the environment.

From this repository, run:

```sh
python3 -B eval/run.py --suite full --keep-workspaces --model PROVIDER/MODEL --max-time 600 --max-cost 1.5
```

Replace `PROVIDER/MODEL` with an authorized explicit selector. That selector is used for all main sessions; native child model routing is inherited. Actual provider/model and usage evidence remains in the journals. The runner does not import authentication, silently change provider, retry paid failures, or resume a previous session. `--suite phase1` runs the original three cases unchanged; the default full suite adds ten cases.

To isolate an integrated failure, use an explicit case ID:

```sh
python3 eval/run.py --model PROVIDER/MODEL --case architecture-tenant-notes --max-time 600 --max-cost 1.5
```

`--case` is repeatable and filters by exact ID. `--results PATH` selects the artifact parent, defaulting to gitignored `eval/results/`. Every run allocates a private output directory. `--keep-workspaces` retains only newly created synthetic workspaces under each result for live runtime/browser follow-through; without it the temporary workspaces are archived then deleted. There is no dry-run result that can be mistaken for a pass.

## Authorization and bounds

The runner invokes `omp` with fixed `profile/config.yml`, appended main contract, named profile, disabled extensions, native print JSON, external session output, and explicit model/time/cost limits. Synthetic implementation cases add `eval/config.yml`. The approval-denied case deliberately omits that overlay and keeps normal profile prompts; it must submit the actual check, receive native rejection, leave its execution sentinel absent, and report NOT-RUN. No yolo, approval-mode override, arbitrary flags, alternate profile, or permission relaxation is passed.

The evaluation-only overlay authorizes parent task calls. General eval is denied. Bash is prompted at tool level, then ordered command patterns permit only the exact standalone `node --test` and `git diff --no-ext-diff --no-textconv`, denying everything else. A tool-wide `bash: deny` would also deny those commands. Each fixture's AGENTS.md names the authorized checks; initial files are staged in a new local Git repository without making a commit, so the main agent can provide an actual patch to the bundled reviewer. Compound commands, installs, shell escapes, package-manager commands, and arbitrary `node -e` are not authorized. These evaluation grants do not change normal launcher policy. Agent frontmatter and actual child journals assess advisory behavior; neither approvals nor this harness is an OS sandbox. Generated tests retain the user's process permissions. Use only disposable synthetic projects.

The synthetic overlay uses `async.enabled: false` for settled native `details.results` and actual `agentSource`/child IDs. Normal profile scheduling is unchanged, including the unoverlaid approval probe; scheduling is recorded per case. Native `--wait-async` remains present. Planned text is not actual task/yield/tool evidence.

Per-case defaults are 600 native seconds and a USD 1.50 soft cost cap; full suite is thirteen sequential cases (USD 19.50 nominal batch cap), original suite three (USD 4.50). Actual requests in flight can exceed native soft caps. Limits accept 60..1200 seconds and USD 0.01..5 per case, with a subprocess deadline thirty seconds later and thirty-second independent checks. Children retain the synthetic five-minute/sixty-request budget. All selected cases run after earlier failures; no automatic paid retry occurs. Use an explicit subset to investigate a changed scenario.

## Coverage and evidence

Expected routing metadata lives only in the harness case definitions, not the synthetic user prompts:

- `quick-duration`: a localized fractional-seconds bug, expected quick change and no delegation.
- `feature-cli-summary`: a real end-to-end feature through a launched CLI, expected feature development. Consumer checks cover unchanged output, filtering, argument order, totals, credits, empty selections, and invalid options.
- `architecture-tenant-notes`: a breaking synchronous-to-asynchronous storage-boundary cutover protecting private tenant data. Requires an actual `af-architect` consultation before implementation and a bundled `reviewer` execution after implementation. Consumer checks cover adapter injection, migration of the example caller, rejection propagation, input validation before storage, same-ID tenant isolation, delimiter/prototype keys, and mutation ownership.

Full-suite additions:

| Case | Observable coverage |
| --- | --- |
| `initialize-health-service` | Initialization, operations consultation, real HTTP health/404 and testable lifecycle |
| `investigate-bearer-auth` | Bug investigation, security consultation, exact credential comparison and negative consumer checks |
| `refactor-invoice-format` | Internal refactor, preserved output, no delegation |
| `review-retry-errors` | Review-only scope, bundled reviewer, actionable findings without edits/checks |
| `optimize-catalog-lookups` | Performance advisor, fixed real before/after measurements, semantic equivalence |
| `sqlite-atomic-migration` | Architect/database advice, actual SQLite forward migration, duplicate failure atomicity, rollback |
| `recover-csv-task` | Fresh-session context/task/decision/handoff reads and accepted integer-cents contract |
| `approval-denied-verification` | Normal headless policy, submitted-and-denied check, honest NOT-RUN, absent sentinel |
| `report-executed-test-failure` | Exactly one real failing check, preserved source, honest FAIL rather than denied/not-run attribution |
| `browser-task-ui` | Frontend advice, real API acceptance, browser gap reporting, retained UI for Tern verification |


A route sentence alone never passes. Implementation cases retain successful inspection/write, actual `node --test` after the final implementation edit, and independent consumer/project checks. Context bookkeeping is recorded but does not invalidate unchanged tested implementation. Read-only cases forbid all workspace mutations and do not pretend tests ran; the denied-approval case checks actual rejection rather than executing the sentinel itself. The optimization case requires comparable real baseline and post-edit measurement output from the fixed benchmark. Expected specialist types and actual native child provenance/inspection/advice are checked; advisory non-read-only attempts fail even if denied. Architecture consultation precedes implementation; the original architecture case also requires bundled review after a write. Existing consumer assertions and failed history are preserved.

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

Read actual advice and main disposition for decision quality. Automated chronology cannot grade alternatives, unsupported premises or finding rejection; record human-assessed deficiencies separately. Browser flow is a separate actual Tern check on the retained model-produced UI, not a source-text assertion. These cases do not prove OS containment or safety for real repositories.

## Environment, browser and isolation follow-through

`python3 -B eval/check_environment.py` makes no model requests. It exercises five launcher guards in a temporary HOME, inspects actual native RPC context/skill discovery in a fresh project, and compares default configuration hashes. Raw RPC results are private local evidence.

After the UI case, start its retained `workspace/server.js` on a task-owned localhost port using installed Node. Read `xd://eval/browser` and preflight the existing Tern host without opening fallback engines. In an approved OMP JavaScript eval, open the owned tab first:

```js
const tab = await browser.open({
  name: 'af-ui-check', app: 'tern',
  url: 'http://127.0.0.1:ACTUAL_PORT', allowed_domains: ['127.0.0.1']
});
```

Inspect that native result before continuing. If it is not actually Tern, close this owned tab and record NOT-RUN. Only after observing Tern, use a separate eval call:

```js
const {checkTaskUi} = await import('/absolute/path/to/agent-first/eval/browser-check.mjs');
const result = await checkTaskUi({
  tab, backend: 'tern',
  url: 'http://127.0.0.1:ACTUAL_PORT',
  output: '/absolute/private/results/browser.json',
  write, print
});
```

Inspect the actual native open result. A requested Tern app is not backend proof; if native fallback occurs, close only the owned tab and record NOT-RUN. The helper exercises associated label/form, empty Enter feedback, keyboard submission, actual API persistence, safe markup-like text, focus/live status, reload, page errors and screenshot. It reads DOM/API state but does not manufacture success. It closes its owned tab in finally. Stop the owned runtime after evidence capture. Manual screen-reader/full audit and unsupported viewport/cross-browser checks stay explicit gaps.

Run [the disposable OVNFS procedure](ovnfs-check.md) separately with explicit opt-in and integration approval; normal profile application stays denied and automatic isolation/application stays off. Read [full validation](full-validation.md) for executed commands/results and [Phase 1 history](validation.md) for preserved earlier failures. No repository artifact claiming PASS substitutes for an actual result.
