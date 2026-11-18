# Native project plugin migration validation

## Disposition

Agent-First 2.0.0 is implemented as a native project-scoped OMP marketplace plugin. The catalog, plugin assets and documentation are local and uncommitted. No GitHub release, commit or push was performed. Native packaging/lifecycle works; behavioral results are not an all-green or all-model reliability claim. Later targeted outcomes and native integration corrections are recorded below, without rewriting earlier failures.

Observed environment: OMP `18.22.1`; Tern `0.9.26 (6a1aeb9)`; OVNFS `0.7.0`. Existing Python, Git and Node were used without dependency/runtime/browser installation or updates. Commands ran from `/home/alduraimron/code/omp/agent-first` unless a retained command record names its synthetic workspace.

## Implemented cutover

- `.omp-plugin/marketplace.json` publishes `agent-first@agent-first`, version `2.0.0`, from `./plugins/agent-first`.
- `plugins/agent-first/.omp-plugin/plugin.json` is native OMP metadata. Conventional `skills/`, `agents/` and `rules/` load through the existing marketplace provider; there is no executable extension, plugin manager, launcher, MCP server or separate runtime.
- `rules/agent-first-orchestrator.md`: always-apply, `agents: [main]`, preserving adaptive engineering/interaction routing, main implementation ownership, selective reading, context and evidence handoff.
- `rules/agent-first-shared.md`: always-apply for main, six advisors and bundled reviewer. It contains behavioral authorization, no-bypass, advisory, browser and evidence boundaries, not native permission settings.
- All 57 skills retained: 11 original engineering/support skills, 24 principle leaves, 20 interaction leaves and two selectors. All eight workflow procedures, context templates, provenance and pstack MIT attribution/license remain. Native `hide: true` on the 44 leaves replaces the removed profile's catalog filtering without disabling URI reads.
- All six read-only domain advisors retained with `tools: [read, grep, glob]`, `spawns: []`, domain/selector autoloads, `structured: true` and an explicit native output schema with required string `report`. Both flag and schema are needed for native yield. Bundled `reviewer` is not copied/replaced; its native output mode is respected, with yields only when provided and inspected final findings/verdict otherwise.
- Removed `bin/af`, profile config/APPEND_SYSTEM/RULES, enrollment/symlink setup and obsolete launcher/custom-permission probes/tests. Active evaluation entry points use ordinary `omp`, actual project plugin installation and no named profile or append-system flag.

### Effective authority

The plugin supplies no `tools.approvalMode`, `tools.approval`, command patterns, restricted folders, model roles, config overlays, provider disables or browser settings. Operator/project native permissions remain effective, including explicitly configured YOLO. Native prompts/denies/guards and user-authorized scope remain binding; a refused effect cannot be rerouted through eval, scripts, children or alternate tools. Consequential decisions and commit/push still need their specific task authority, not a new Agent-First command matrix.

Two concurrent consultations and one delegation level are behavioral instructions, not installed scheduler settings. Stricter operator limits win. Native headless execution cannot answer an interactive gate; actual main/child runtime tiers can differ and must not be represented as a plugin security guarantee.

Project scope is explicitly selected by `--scope project`; native scope defaults to user and no supported manifest field enforces project-only installation. The nearest `.omp/`, otherwise Git root, anchors the install and descendants inherit it. Marketplace registration and shared caches use native user storage, but approval/model settings are not modified. This is not an OS/filesystem/process/network sandbox.

Existing actual `~/.local/bin/af` and named-profile symlinks were not deleted or rewritten. Their old targets are retired; use `omp` and operator-reviewed cleanup of verified old links only. The preexisting source config, including local `hideThinkingBlock` preference, was preserved privately before retiring that obsolete file at `/tmp/agent-first-plugin-baseline.mukhQw/preexisting-config.yml`. No default-profile or team configuration was edited.

## Native model-free evidence

| Check | Outcome | Observed evidence |
| --- | --- | --- |
| `python3 -B eval/check_plugin.py --upgrade-marketplace /home/alduraimron/checkouts/af-plugin-upgrade-20261118` | PASS, 35 assertions | `results/plugin-lifecycle-oi386ve0/result.json` and exact CLI/RPC/stdout/stderr records |
| Fresh project installation, no user-scoped install | PASS | Native project registry actually created; uninstalled sibling project had no Agent-First routing |
| Native skill discovery and resolution | PASS | All 57 registered skills actually read through native `skill://`; 44 hidden leaves, 13 visible entries |
| Orchestration and coexistence | PASS | Real RPC `get_state` injected main/shared rules and preserved existing project instructions; unrelated project skill and independently installed plugin survived uninstall |
| Permission inheritance | PASS | Nonempty effective settings snapshots equal before/after install; project `write`, explicit eval deny and bash pattern remained; separate operator-YOLO project remained YOLO |
| Upgrade, uninstall and previews | PASS | Real native `2.0.0 -> 2.0.1` upgrade using a disposable newer OVNFS catalog; runtime routing after upgrade, uninstall removed owned routing/advisors/skills only; dry-runs did not remove registration |
| Fixture boundary | PASS | Child fixture installation under an existing parent `.omp/` created its own registry without modifying the parent's registration |
| Existing configuration/context/global preservation | PASS | Existing project config, AGENTS, skill and context byte-preserved; real global settings/marketplace/plugin registry hashes unchanged; source package unchanged by installer |
| `python3 -B eval/check_principles.py` | PASS, 212 assertions | `results/principles-native-o7uknk8b/result.json`; complete catalog/contracts/attribution, native reads and disable/enable handling, no model call |
| `python3 -B -m unittest discover -s eval -p 'test_*.py' -v` | PASS, 38 tests | Final integrated fixture/parser suite, including read-only SQLite backup, timeout retention, scoped test evidence and cleanup/prediction/fragment false-PASS guards |

The upgrade checkout was created with native `ovnfs new ... --name af-plugin-upgrade-20261118 --json`; only its two version fields were changed. No apply occurred. Its diff was retained at `/tmp/agent-first-plugin-baseline.mukhQw/upgrade-checkout.patch`, then only that owned checkout was removed. Reproducing a different-version upgrade requires an existing disposable newer marketplace via `--upgrade-marketplace`; the check without that option explicitly reports that portion NOT-RUN, not PASS.

The lifecycle proof covers packaging, scopes and settings before later advisory content/schema corrections. Those do not replace discovery or operator settings; final native schema behavior is exercised in the SQLite follow-through below. Older result hashes describe their recorded source state, not identical final bytes.

## Behavioral engineering evaluations

Model: explicit `opencode-go/gpt-5.6-luna`. Existing operator authentication was explicitly selected with `--auth-source /home/alduraimron/.omp/agent/agent.db`. The evaluation-only helper makes a read-only SQLite backup into private isolated HOME, uses `.omp` as a directory name, and deletes the private credential DB on exit. No credential content belongs in published evidence.

The plugin itself has no permission overlay. `--policy native` adds only `eval/native.yml` scheduling/child-budget controls; the two forced-prompt scenarios additionally use independent `eval/prompt-check.yml`. Both are evaluation controls, not installed plugin settings. Each actual argv, prompt, case expectation, result, native journal and independent consumer is retained.

Commands:

```sh
python3 -B eval/run.py --suite principles --policy native \
  --case quick-duration --model opencode-go/gpt-5.6-luna \
  --auth-source /home/alduraimron/.omp/agent/agent.db --max-time 600 --max-cost 1.5
# Subsequent explicit --case batches covered every remaining retained scenario,
# with the same model/auth/bounds and --keep-workspaces.
```

| Scenario | Initial complete result | Evidence/disposition |
| --- | --- | --- |
| quick-duration | PASS | `results/20261118T015716Z-_u392orx`; quick-change, no delegation, actual main tests and independent consumer |
| feature-cli-summary | PASS | `results/20261118T020045Z-_1v0tuyh/feature-cli-summary`; actual CLI behavior and consumers |
| architecture-tenant-notes | FAIL | `results/20261118T020437Z-x84srxwb`; implementation/main tests/independent consumers passed, but main hit its 600-second deadline before final report; reviewer assignment lacked relevant principle URI |
| initialize-health-service | PASS | Real HTTP/service consumers and actual operations advisor |
| investigate-bearer-auth | FAIL | Code, main tests, consumers and bundled review passed; security advisor did not read every assigned principle before advice |
| refactor-invoice-format | PASS | Preserved behavior and no delegation |
| review-retry-errors | FAIL | Actionable findings and no edits/tests, but reviewer answered from supplied context without required own inspection/assigned-leaf reads |
| optimize-catalog-lookups | FAIL | Real fixed benchmark medians `74.535 ms -> 6.347 ms` and consumers passed; main omitted the required proof leaf. Initial harness also failed to recognize legitimate scoped Node tests; corrected parser replay removes only those false negatives |
| sqlite-atomic-migration | PASS | Actual architect/database advice; SQLite forward migration, failure atomicity and rollback consumers |
| recover-csv-task | PASS | Fresh-session durable context/task/decision/handoff recovery and consumer contract |
| approval-denied-verification | PASS | Native tool approval actually refused the check without UI; honest NOT-RUN and no execution sentinel |
| report-executed-test-failure | PASS | Intentional failing test actually ran once and remained honestly FAIL; independent consumer confirmed execution/no repair |
| browser-task-ui | FAIL | Real frontend advice, API tests and consumers passed; assignment invented nonexistent principle URIs. Original model falsely inferred no new Tern hosting from an empty block list. Independent actual Tern follow-through below passed |
| principle-uncertain-rounding | PASS | Root cause read before fix and behavioral consumers |
| principle-minimal-cli | PASS | Minimal existing-file API/CLI implementation and invalid-input consumers |
| principle-approval-independent-work | FAIL | Native refusal, subsequent independent safe inspection and approval/rollback content were correct; first prose omitted the exact workflow prefix |

Initial behavioral score under native permissions: **10/16 PASS**. All 16 independent scenario consumers passed in that initial coverage. A consumer PASS does not discharge missing inspection, leaf handoff, report format, a timeout or other workflow failure. Original results remain unchanged. Later attempts below have their own outcomes; no acceptance was weakened to make failures green.

### Corrections and retained failures

1. Initial lifecycle harness incorrectly parsed the native settings map/catalog and re-added an existing marketplace. `results/plugin-lifecycle-g_cxcvn8` remains FAIL. Corrected parsers reject empty settings/catalogs, with regression tests; later native lifecycle passed.
2. The first retained interaction fixture installed before creating its own Git/`.omp` anchor. It temporarily created managed plugin registration in this Agent-First source repository, not in the intended child. Later fixtures refused the duplicate install. No existing config/instructions were overwritten. The test-only registration was explicitly uninstalled and its empty managed files/directories removed. `PluginFixture` now creates its own `.omp` anchor before native commands; the native nested-install regression proves parent preservation. `results/interactions-unzlfqh6` and interrupted `results/20261118T020045Z-_1v0tuyh` remain retained, not current success claims.
3. Native bundled reviewer does not itself opt into structured tasks. The migrated handoff now respects actual native output mode instead of requiring an unavailable yield tool or restoring a profile setting.
4. Exact catalog-URI handoff format now lives in `af-principles`; domain labels are not invented skill names. Children must inspect assigned source/leaves themselves. This improves instructions, not native enforcement.
5. Existing scoped Node-test evidence parser is shared by both runners. It accepts completed whole-project or literal in-workspace scoped tests with actual passing output; preserves rejection of foreign cwd, escaping/missing/symlink targets, flags/compound commands and failures. `optimize-catalog-lookups/scoped-test-parser-replay.json` still FAILS solely for the actually missing proof-leaf read. No benchmark was rerun for this parser replay.
6. Browser guidance now distinguishes a successful empty Tern block list from unavailable hosting. Native owned-tab opening and backend inspection remain required; no fallback or engine installation is authorized.
7. Runtime session headers proved `structured: true` without an output schema still left custom advisors with only read/grep/glob and no yield. Each of the six definitions now declares an explicit native JTD output schema with required string `report`; no global `task.structured` is installed. Final native architect/database calls actually used successful schema-shaped yields.
8. Native service cleanup can produce a later short acknowledgment after a substantive completed report. The scorer now selects one coherent completed post-test/post-advice report; it rejects predictions, aborts and combining fragments. Original case/report requirements remain unchanged. The UI replay described below passes while retaining all four intermediate tool failures.

### Targeted native validation after corrections

```sh
python3 -B eval/run.py --suite principles --policy native \
  --case architecture-tenant-notes --case investigate-bearer-auth \
  --case review-retry-errors --case optimize-catalog-lookups --case browser-task-ui \
  --model opencode-go/gpt-5.6-luna \
  --auth-source /home/alduraimron/.omp/agent/agent.db \
  --max-time 600 --max-cost 1.5 --keep-workspaces
```

Retained output: `results/20261118T025701Z-65n_4p8a`. This run followed the URI-handoff/browser clarifications and preceded the final explicit advisor output schemas.

| Scenario | Actual new outcome |
| --- | --- |
| investigate-bearer-auth | PASS, including assigned security leaves, real tests/consumers and bundled review |
| optimize-catalog-lookups | PASS, including actual comparable measurements, source/leaf evidence and consumers |
| browser-task-ui | Raw FAIL only because the last cleanup acknowledgment displaced the earlier completed report. `completion-report-replay.json`: PASS using unchanged scenario requirements; original run remains FAIL and four intermediate tool failures remain recorded |
| architecture-tenant-notes | FAIL: architect's provider request returned `ECONNRESET` and was aborted; main reached its deadline without implementing the dependent change. Its consumer failed. This is not the earlier implementation's PASS or a reason to skip required architecture consultation |
| review-retry-errors | FAIL: main deadline, missing first-prose/final-report and relevant reviewer URI. No provider/policy/budget bypass or automatic unchanged rerun |

The new UI model run actually selected/opened Tern, submitted literal markup through the real UI/API, reloaded persistent state, checked whitespace errors and focus, and exercised an offline POST failure. It correctly reported narrow-viewport/assistive-technology and initial-load failure coverage NOT-RUN. Two attempts to inject initial GET failure via route did time out and remain failed evidence; later network inspection showed real 200 responses, not a successful failure injection. Its owned tabs/server were closed. This is new automatic-browser evidence, separate from the earlier independent eight-check follow-through.

After adding the six explicit output schemas, executed:

```sh
python3 -B eval/run.py --suite principles --policy native \
  --case sqlite-atomic-migration --model opencode-go/gpt-5.6-luna \
  --auth-source /home/alduraimron/.omp/agent/agent.db \
  --max-time 600 --max-cost 1.5 --keep-workspaces
```

**PASS**: `results/20261118T033949Z-s2vib2a1/sqlite-atomic-migration`. Native `af-architect` and `af-database` sessions each exposed read/grep/glob/yield and each completed one successful yield with string `data.report`. Their source/assigned-leaf inspection, architect-before-implementation chronology, main implementation/tests and independent SQLite/consumer checks passed. A real bundled reviewer also inspected source read-only and returned its native unstructured report, without yield. No permission/profile/output-mode override was added. The other four advisor schemas have the same native shape but were not separately re-delegated after this final schema edit.

Remaining behavioral failures are explicit: the larger tenant case/provider/deadline, retry-review deadline/handoff, and exact first-prose routing in the independent-work and trivial-interaction cases. These are not erased by successful narrower native paths or parser replays. There is no single all-green final sixteen-case run.

## Interaction evaluations

```sh
python3 -B eval/check_interactions.py \
  --case how --case why --case teach --case interview --case ketchup \
  --case show --case write --case negative-no-interview \
  --case negative-review --case negative-read-only \
  --model opencode-go/gpt-5.6-luna \
  --auth-source /home/alduraimron/.omp/agent/agent.db --max-time 300 --max-cost 0.5
```

`results/interactions-aycpvjrp`: initial **8/10 PASS**. Successful natural routing/full leaf reads and scoped behavior covered how, why, teach, interview, catch-up, existing evidence, requested README authoring and read-only explanation. No plugin permission overlays were used and native effective settings stayed equal.

- `negative-no-interview`: consumer implementation/tests/no-delegation passed, but first prose said `Workflow: quick fix` instead of the contracted `Workflow: quick-change`; retained FAIL, no format assertion waiver.
- `negative-review`: correct source-based actual `180` versus expected `160` was rejected only because its labeled equations used Markdown bullets/bold/code spans. The parser now normalizes that formatting while preserving label/result association and rejecting swapped numbers. Fifteen targeted interaction evidence tests passed; `negative-review/numeric-parser-replay.json` is PASS without a new model run. The original raw run/summary stays FAIL. This is parser correction, not fresh model compliance.
- The remaining 13 supplied reference scenarios were NOT-RUN as model tasks. All 20 interaction skill bodies were independently discovered/read in native loading checks.

## Actual Tern runtime follow-through

The original UI fixture's retained implementation was exercised independently using native OMP eval/browser, not a launcher/profile or an alternative browser engine:

1. Main started `node server.js` in `results/20261118T020437Z-x84srxwb/browser-task-ui/workspace`, as owned service `af-plugin-ui-runtime`; actual URL `http://127.0.0.1:42559`.
2. Existing Tern responded successfully to block/target preflight with an empty list. `browser.open({name:'af-plugin-migration-ui', app:'tern', url, allowed_domains:['127.0.0.1']})` actually opened a Tern browser PiP on pane `498216206337`.
3. Only after observing that native backend result, main executed existing `eval/browser-check.mjs` `checkTaskUi` against the real page.
4. **PASS, eight actual checks:** associated label/form; empty Enter validation and focus; keyboard POST persisted through actual API; markup-like content remained literal text without injected elements; success focus/live feedback; Tab order; reload/server state; no recorded page errors.
5. Evidence: `browser-task-ui/native-tern-followthrough.json` and retained `native-tern-followthrough.webp`. The helper closed its owned tab; the owned service was stopped. No borrowed page/navigation, fake app-state mutation or browser provisioning occurred.

This proves the exercised Tern API/UI flow, not the original model's automatic browser decision. Manual screen-reader/full accessibility and cross-browser checks are NOT-RUN. Observed small viewport was `390x225`, with `scrollWidth:440` after long text: horizontal overflow remains an app-fixture layout limitation, not a responsive-layout PASS.

## Remaining boundaries

- GitHub marketplace installation/publication: NOT-RUN, local checkout only; no commit or push authorized.
- Real installation/upgrade/uninstall in personal/team/production repositories: NOT-RUN deliberately; only synthetic projects were used apart from the disclosed, removed test-only source registration.
- All-model routing quality, all collision layouts, live TUI/ACP reload, OS containment, full accessibility and deployment/production/other-database behavior: NOT-RUN, not implied by local results.
- Actual dependency installation, cloud changes, production deployment, OVNFS source apply and destructive host operations: NOT-APPLICABLE to this migration's runtime target and not executed.
- Legacy global launcher/profile cleanup: NOT-RUN by design; inspect owned old links manually if retiring them.

## Native technical sources

- [OMP 18.22.1 marketplace lifecycle/scopes](https://github.com/can1357/oh-my-pi/blob/v18.22.1/docs/marketplace.md).
- [Marketplace provider: actual skills and rule loading/registration](https://github.com/can1357/oh-my-pi/blob/v18.22.1/packages/coding-agent/src/discovery/claude-plugins.ts).
- [Skills: hide, URI reads, collisions and child autoload](https://github.com/can1357/oh-my-pi/blob/v18.22.1/docs/skills.md).
- [Task discovery, tool/spawn restrictions and structured-output semantics](https://github.com/can1357/oh-my-pi/blob/v18.22.1/docs/task-agent-discovery.md).
- [Bundled reviewer definition](https://github.com/can1357/oh-my-pi/blob/v18.22.1/packages/coding-agent/src/prompts/agents/reviewer.md).
- [Rule agent filtering and prompt injection](https://github.com/can1357/oh-my-pi/blob/v18.22.1/docs/rulebook-matching-pipeline.md).
- [Native permission precedence and headless refusal](https://github.com/can1357/oh-my-pi/blob/v18.22.1/docs/approval-mode.md).
- [Actual user-root path joining and scope helpers](https://github.com/can1357/oh-my-pi/blob/v18.22.1/packages/utils/src/dirs.ts). For evaluation isolation use a private HOME and `PI_CONFIG_DIR='.omp'`; an absolute `PI_CONFIG_DIR` is not treated as an absolute root by `path.join`.
