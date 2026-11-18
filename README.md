# Agent-First Coding System

A reusable personal engineering environment built from native OMP profiles, skills, agents, approvals, sessions, and the existing Tern browser integration. Main selects the workflow and implements; specialists advise only when a concrete domain question warrants it. No separate orchestration runtime, extension, MCP server, Tern plugin, or memory database is added.

## One-time setup

Prerequisites: existing OMP, Python 3.9+, a configured default model and authorized model access. Git projects need existing Git. Tern is used for browser work; optional isolation needs existing OVNFS. Full SQLite evaluations need Node 24+, while original evaluations need Node 18+. Setup installs or updates no dependencies.

From this checkout at a stable path:

```sh
./bin/af --setup
```

This creates `~/.local/bin/af` pointing to this guarded launcher and registers the five native profile assets under `~/.omp/profiles/agent-first/agent/`. Existing conflicting commands/profile entries are refused, never overwritten. It does not enroll the setup directory or edit shell startup files, team configuration, default OMP configuration, or existing commands.

If `~/.local/bin` is not already on PATH, add it to your shell's PATH once. For bash/zsh:

```sh
export PATH="$HOME/.local/bin:$PATH"
# Keep that export in your own shell startup file if needed.
```

## Everyday use

```sh
cd /path/to/personal-project
af

# Or describe an outcome immediately:
af "Add the requested feature and verify its real behavior"

# Existing options remain available:
af --cwd /another/personal-project
af --model PROVIDER/MODEL "Use this model for this launch"
```

The current working directory is the project unless `--cwd` is supplied. No `--model` is required: fresh launches read native `modelRoles.default` from the `agent-first` profile, falling back to your ordinary OMP default role when the personal profile has none. Only the selector is reused, not other default-profile settings, extensions or credentials. The launcher does not hardcode or silently substitute a model. If neither role is configured, it explains the missing prerequisite instead of choosing another model. Explicit `--model` wins; continuation/resume keeps native saved-model behavior unless you override it.

Keep this checkout in place because command/profile registration uses symlinks. On a new machine, authenticate separately with `omp --profile agent-first login`; credentials are never copied. `af --activate` remains available for profile-link registration without installing the PATH command or starting a session.

## Personal-project enrollment

The first interactive `af` in an unknown or changed project asks whether it is a **personal** project, defaulting to **No**. Declining starts no OMP session. A headless launch refuses unknown projects, even with `--cwd`. Setup never implicitly approves its cwd.

For an operator's explicit non-interactive enrollment or revocation:

```sh
af --cwd /path/to/personal-project --trust-project
af --cwd /path/to/personal-project --untrust-project
```

Approvals are private user-local records under `~/.config/agent-first/projects/`, not team/repository configuration. Git subdirectories reuse their repository's approval; nested repositories do not inherit it. Replaced directories/Git metadata and changed local remote URLs require new confirmation. Symlinks use the real target. Non-Git folders are approved individually, not recursively. Git context-redirection environment variables are cleared so the selected cwd is not silently redirected elsewhere.

This is explicit project designation, **not automatic ownership detection or OS containment**. Never approve a team/production project. The launcher cannot discover every ownership change without changed metadata; human classification remains necessary. Do not have an agent enroll real projects automatically. There are no shell/cwd hooks: entering a directory does not activate Agent-First.

Use installed `af` (the same `bin/af` entry point), not a bare `omp --profile agent-first` alias, to retain these guards and the pinned policy. Profile isolation still does not isolate every external configuration source. Use a fresh launch after changes; hot-reload of running sessions is not established.

Describe the desired result. Normal work does not require `/plan`, `/build`, `/review`, a workflow selector, or an agent name.

## Interaction & Reasoning Skills

For explanations, learning, interviews, idea/design discussion, context recovery, reflection and communication, main reads `af-interaction` and only the relevant `interaction-*` leaf. Ask naturally: "How does this work?", "Why was enrollment introduced?", "Teach me the context system", "Interview me about this feature", or "Catch me up". Ordinary use remains `af`, without manual skill commands or a coding workflow for every question.

The 20 leaves cover `how`, `why`, `teach`, `blast-radius`, `technical-writing`, `bro`, `interview-me`, `in-your-own-words`, `idea-refine`, `sharpen`, `architect`, `figure-it-out`, `recall`, `ketchup`, `show-me-your-work`, `pause-safely`, `reflect`, `correct`, `automate-me` and `unslop`. The [interaction selector](profile/skills/af-interaction/SKILL.md) defines triggers and composition. Its leaves are hidden from the always-visible catalog, not from native URI access.

Conversations default to read-only. Explicitly requested documentation or handoff writes authorize only those artifacts, not code changes or external effects. Defect review, diagnosis, verification and implementation retain their engineering routes; a clear change needs no mandatory interview or teaching. Design discussion does not replace the architect consultation required for architecture-changing implementation.

The supplied package adds procedures, not permissions, plugins, agents or runtime dependencies. [Provenance](profile/skills/af-interaction/SOURCES.md) is separate from the existing principle-layer MIT attribution. Start a fresh `af` session after updating.

## Adaptive workflow library

For engineering execution, main inspects intent, complexity, risk, and architectural impact, announces the selected exact route prefix (for example, `Workflow: quick-change`) with a rationale, and reads the relevant procedure. New evidence can change the route; consequential changes follow the approval boundary.

| Intent | Procedure |
| --- | --- |
| New personal project | [Project Initialization](profile/skills/af-engineering/workflows/project-initialization.md) |
| New behavior within existing boundaries | [Feature Development](profile/skills/af-engineering/workflows/feature-development.md) |
| Unexpected behavior or uncertain cause | [Bug Investigation](profile/skills/af-engineering/workflows/bug-investigation.md) |
| Behavior-preserving restructuring | [Refactoring](profile/skills/af-engineering/workflows/refactoring.md) |
| Changed architectural boundary/contract | [Architecture Change](profile/skills/af-engineering/workflows/architecture-impacting.md) |
| Read-only defect assessment | [Code Review](profile/skills/af-engineering/workflows/code-review.md) |
| Measured latency/resource problem | [Performance Optimization](profile/skills/af-engineering/workflows/performance-optimization.md) |
| Local understood low-risk edit | [Quick Change](profile/skills/af-engineering/workflows/quick-change.md) |

Each procedure specifies inputs, steps/decision points, consultation criteria, verification, exit, and failure/escalation behavior. The sequence remains **workflow -> relevant domain procedure -> decision-relevant principles -> main implementation and checks**. Architecture-impacting implementation requires actual architect advice first. Trivial changes do not delegate; read-only requests do not authorize edits.

## Domain consultation and skills

| Native agent | Domain skill | Consultation question |
| --- | --- | --- |
| `af-architect` | `af-design` | Boundaries, public contracts, ownership, compatibility and alternatives |
| `af-database` | `af-database` | Modeling, migrations, transaction integrity, query design |
| `af-security` | `af-security` | Trust, authorization, secrets, input-to-sensitive-sink paths |
| `af-frontend` | `af-frontend` | Interaction state, semantics, accessibility, responsive behavior |
| `af-performance` | `af-performance` | Measured bottlenecks, algorithms, resources and experiment design |
| `af-devops` | `af-operations` | Deployment ordering, health, observability, recovery |

Custom advisors expose only read/grep/glob, cannot spawn, and hand advice to main through native yield. All six autoload their domain skill plus `af-principles`. Main passes only selected leaf URIs, their observed triggers and the decision question; each child reads those leaves directly before advice. Children do not inherit main's append text or leaf-read history. Shared report and handoff rules live in `profile/RULES.md`. Main evaluates advice, owns implementation, and performs checks. The bundled native `reviewer` receives the same explicit principle handoff and actual patch, without a cloned definition. Routine work stays inline; implemented data-exposure/corruption invariants require independent review of the actual patch, not just pre-design consultation.

The eleven original domain/support skills remain: `af-engineering` owns requirements, planning, routing and consultation; domain skills own their engineering procedures; `af-testing` owns diagnosis/test design; `af-verification`, `af-context`, and `af-isolation` own evidence, project records and optional checkout lifecycle. Together with `af-principles`, its 24 leaves, `af-interaction` and its 20 leaves, the profile has **57 native registry entries, with 13 visible catalog entries**. See the [skills catalog](docs/skills-catalog.md) for all names and pointers.

The [principle selector](profile/skills/af-principles/SKILL.md) is the authoritative activation map for engineering judgment, not a fixed checklist. Usually one to three leaves inform a decision; a trivial understood edit normally needs only `prove-it-works`, with at most one other relevant leaf. Main reads selected leaves in full before applying them. No manual skill commands, new planning ceremony, agent or runtime are required. In OMP 18.22.0, `skills.manualSkills: [principle-*, interaction-*]` hides leaf metadata from the visible catalog, not native `skill://` access; exact `includeSkills` entries retain all leaves. Start a fresh session after profile changes.

The principles adapt [pstack at revision `2f87c854fe3e2fcda44ca86b46ede35aad3c46b7`](https://github.com/cursor/plugins/tree/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack), Copyright (c) 2026 Lauren Tan, MIT. [Source attribution](profile/skills/af-principles/SOURCES.md) and the [preserved license](profile/skills/af-principles/LICENSE) cover those adaptations, not unrelated Agent-First files.

## Context, decisions and handoff

For meaningful work main creates only relevant ordinary files in the selected personal project:

```text
.agent-first/
  context.md               # Project facts, commands, active task, session pointer
  tasks/<task-id>.md        # Requirements, acceptance, plan, progress, advice disposition
  decisions/<id>.md         # Options, accepted/pending decision, approval, constraints
  verification.md          # Append-only attributable evidence
  handoff.md               # Current state, blockers, next executable action
  issues.md                # Unresolved defects and uncertainties
  corrections.md           # Observed patterns, cause, action, validation and placement
```

Accepted repository decisions are authoritative; native OMP sessions retain execution history. Fresh/continued work reads the active task, relevant decisions and handoff, reconciles source changes, and treats old results as historical until applicability is established. Quick trivial work needs no empty paperwork tree. Read-only work proposes records rather than writing files. Templates and lifecycle: [af-context](profile/skills/af-context/SKILL.md).

```sh
af --cwd /absolute/path/to/personal-project --continue
af --cwd /absolute/path/to/personal-project --resume PERSONAL_SESSION_ID
```

Resume file paths must exist inside the named profile. If a session is unavailable, describe the outcome or ask to continue the active project task; recovery uses repository records. Keep secrets/customer data out of tracked context and inspect raw evidence before sharing.

## Verification and approvals

Main verifies the exact project, runtime, database, Docker endpoint/volumes or remote target before effects, then selects relevant static/type/lint/build, regression/integration/consumer, API/database, security, performance, deployment and browser/accessibility checks. Reports use **PASS**, **FAIL**, **NOT-RUN**, and **NOT-APPLICABLE**, with exact command/cwd/result, real runtime evidence, uncovered requirements, and remaining risks. Unavailable dependencies or denied checks are NOT-RUN, not success or irrelevance.

Browser checks use the existing native eval browser API inside Tern: preflight the existing host, observe, act through the UI, inspect resulting state/errors, exercise keyboard/semantic checks, and capture visual proof. Confirm the actual native backend; unsupported/manual assistive-technology and browser capabilities remain gaps. No fallback engine installation or fallback acceptance is authorized. Native Tern hosting can fall back to an owned engine, so this procedure is not a native fail-closed or no-download guarantee.

`profile/config.yml` is the sole settings authority and selects native **YOLO + Ask When Needed**. Representative categories, not a second command-pattern specification:

| Decision | Scope |
| --- | --- |
| AUTO | Scoped inspection/content edits and ordinary authorized obsolete/generated-file cleanup; checks/debugging/owned services, readonly advisors and Tern; scoped project dependencies/pinned runners, workspace downloads without script execution, local owned Docker development without persistent-volume deletion, and normal Git operations subject to Git guards |
| ASK | Recursive/mass/data-loss deletion; hard Git reset/clean/discard, branch/stash/worktree deletion or history rewrite; global/system installs or settings, privilege/services, SSH/transfers, cloud/deploy/infrastructure, package/container publication, Docker volume deletion/prune/remote contexts/cluster operations, destructive database utilities and OVNFS integration/discard |
| DENY | Existing system/disk destruction, force/destructive remote history, credential transmission/control/auth bypass, protected configuration and tool denies; semantic equivalents remain forbidden through wrappers, eval or children |

Ordinary requested Git commit/push, project dependency changes, downloads and Docker development do not need repeated native prompts. Main commits or pushes **only on explicit user instruction**, never automatically and never by proactively asking after every ordinary task. Ordinary Git add/fetch/pull/clone/merge/cherry-pick/revert/branch creation/stash save/apply/pop/switch remain subject to independent guards; force/destructive operations do not become AUTO.

Native patterns are coarse spelling checks, not scope or production classifiers. Ambiguous `git checkout`/`restore`, cloud/remote tooling, global installers, privilege and integration families can still prompt harmless variants. Uncertain scope or an unmatched high-risk helper without a reliable native per-operation gate stays operator-only, not executable through another tool. Production/destructive migration effects require precise authorization even when no pattern recognizes them.

YOLO honors explicit native prompts and denies; stronger Git guards and restricted-folder gates remain. ASK refuses without an interactive approval UI, including headless sessions; leave the dependent action pending and continue independent safe work without retrying through another tool. For bounded ordinary headless work:

```sh
af --cwd /absolute/path/to/approved-personal-project \
  --json --max-time 5m --max-cost 1 "Inspect the requested behavior"
```

Before an ASK call, main shows the short exact command, cwd, resolved target, impact/risk and rollback, then submits the native per-call prompt. Native command display is truncated and does not infer semantic risk or show cwd; split and review long consequential commands first. Explicit prompts offer Approve/Deny, not session approval. Chat approval alone cannot override a native deny or guard; operator fallback is for an actual deny/guard or unavailable approval, not the default route for supported prompts. Authorization covers the requested outcome, not permission to widen scope.

Safety defaults:

- Maximum two concurrent consultations, one delegation level; no implementation workers or nested spawning.
- Native command prompts and stronger denies live in `profile/config.yml`; native commit/checkpoint helpers remain off. `bash.gitGuard` stays true: branch/stash operations can still refuse a shared main checkout after approval. Use reviewed operator action or explicitly opted-in private OVNFS, never absolute Git paths, wrappers or environment bypass.
- No automatic OVNFS task isolation/application, extension discovery, project MCP, foreign tool/agent/skill discovery, automatic memory learning, analysis backends or tool provisioning.
- Known native additive project tools and agent-shadowing definitions are refused. Existing project instructions remain loaded; native profile isolation does not isolate every external configuration source.
- Readonly advisors remain headless. Child native tiers also use yolo, but explicit prompts fail closed without an approver and denies/advisory scope still apply. The bundled reviewer has broader native metadata than its advisory scope; actual activity matters.
- Restricted folders gate path-tool targets, including symlink resolution, but gate shell/eval/browser by cwd rather than paths embedded in code. Ordered command patterns are not arbitrary-code inspection.
- Configuration ownership and credential/exfiltration restrictions include behavioral semantic denies, not native per-path policy or a firewall. Resolve literal project targets/ancestors, symlinks, ownership and user changes before cleanup. Ordinary authorized obsolete-file edits/removals or nonrecursive cleanup are AUTO; recursive/mass/valuable-data deletion is ASK. Native edit has no deletion-only gate: never use edit REM/eval/scripts to replace a high-risk gated or refused effect. Existing absolute-path rm/chmod/chown denies remain.
- Shell, eval, browser runtimes, project dependencies and scripts retain ambient filesystem/network/process authority. Dependency install/update/removal is autonomous only within a verified trusted project (including a project venv for pip); inspect lifecycle scripts, bootstrap behavior, target and pinned runners. Downloads do not authorize executing downloaded scripts. Do not automatically install unrelated tools, global runtimes, analysis backends or browsers. Use installed/cached/vendor/offline execution where appropriate; report unavailable verification honestly. Never use wrappers or children to bypass policy. Native tool grants are not a sandbox; neither profiles nor OVNFS provide OS containment.

## Optional OVNFS

Opt in explicitly for an experiment or isolated implementation. Use native `ovnfs new`, work in the printed checkout and inspect `ovnfs diff -p`. After reviewing the diff, request native per-call authorization for `ovnfs apply --dry-run`, then separate authorization for real source integration. Creation implies neither apply nor discard approval.

Integration needs exact patch/source review, source-concurrency checks and a recoverable baseline; reverify integrated source. Cleanup/discard is consequential and ASK, limited to owned checkouts. Automatic application stays disabled. Use operator fallback only for an actual deny/guard or unavailable approval. Full procedure and rollback limits: [af-isolation](profile/skills/af-isolation/SKILL.md).

## Evaluate and improve

```sh
python3 -B eval/check_environment.py
# Optional preservation comparison with a retained pre-change capture:
python3 -B eval/check_environment.py --baseline /absolute/private/baseline.json
(cd eval && python3 -B -m unittest test_policy_patterns test_ask_policy)
python3 -B eval/check_cli.py --native
python3 -B eval/check_controlled_yolo.py --model PROVIDER/MODEL
python3 -B eval/check_ask_policy.py --model PROVIDER/MODEL
# Principle-layer checks; commands are not recorded results:
python3 -B eval/check_principles.py
# Interaction routing/behavior with an explicitly authorized model:
python3 -B eval/check_interactions.py --model PROVIDER/MODEL
python3 -B eval/run.py --suite principles --keep-workspaces \
  --model PROVIDER/MODEL --max-time 600 --max-cost 1.5
python3 -B eval/run.py --suite full --keep-workspaces \
  --model PROVIDER/MODEL --max-time 600 --max-cost 1.5
# Original cases remain available:
python3 -B eval/run.py --suite phase1 --model PROVIDER/MODEL
# Same original cases under normal permissions, without synthetic tool grants:
python3 -B eval/run.py --suite phase1 --policy profile --model PROVIDER/MODEL
```

The sequential native-session harness evaluates natural prompts and actual task/tool journals, then runs independent consumer and project checks. `phase1` retains the original three cases, `full` retains all thirteen, and `principles` adds three cases plus principle metadata to the full suite. Principle evidence requires full native leaf reads before the relevant decision, child URI/read chronology, and bounded manual assessment of actual choices, not name mentions. It preserves failed runs, private journals, workspace archives, and intermediate errors. Read-only, approval-denied, recovered-context and measured-optimization cases have explicit contracts instead of pretending every task must edit files.

Historical verification covers thirteen scenarios across explicit runs and two authorized models, all eight routes, the six advisors plus bundled reviewer, actual Tern interaction, and approved disposable OVNFS apply/restore/cleanup under the earlier policy. It is not a clean single-model full-suite result or evidence for the current YOLO policy; native reviewer timeouts and recovered tool/schema errors remain documented.

Current observations belong in [Minimal-ASK validation](eval/minimal-ask-validation.md). The controlled-YOLO probe distinguishes ordinary native AUTO help probes, headless ASK refusals and hard DENY rejections; the interactive probe checks live native RPC approval and disposable `rm -r -- approved-empty` / `rm -r -- denied-empty` effects, not direct operator RPC bash. Commands listed here are not passing results. [Ask-policy validation](eval/ask-policy-validation.md), [Principles validation](eval/principles-validation.md), [Controlled YOLO validation](eval/controlled-yolo-validation.md), [full validation](eval/full-validation.md) and [Phase 1 history](eval/validation.md) retain their historical scopes and failures, not current minimal-ASK evidence. See also [evaluation instructions](eval/README.md), [architecture](docs/architecture.md), [correction ledger](docs/corrections.md), and [improvement backlog](docs/backlog.md).

Interaction-package checks, adaptations and retained results belong in [Interaction validation](eval/interaction-validation.md). The focused interaction probe checks actual full leaf reads and source-grounded responses, no changes for read-only requests, explicitly scoped artifact writes, and ordinary implementation/review routing. Its 23 supplied scenarios are candidate evaluations, not a claim that every scenario or model was tested.

## Source layout

```text
bin/af
profile/{config.yml,APPEND_SYSTEM.md,RULES.md}
profile/agents/             # Six native domain definitions; no reviewer copy
profile/skills/             # 11 original skills + 2 selectors + 44 leaves; 8 workflows
eval/{run.py,check_environment.py,check_cli.py,check_controlled_yolo.py,check_ask_policy.py,check_principles.py,check_interactions.py,browser-check.mjs}
eval/{cases.json,extended-cases.json,ui-case.json,principle-cases.json,principle-expectations.json,interaction-scenarios.json}
eval/{config.yml,profile.yml,prompt-check.yml}
eval/{README.md,minimal-ask-validation.md,interaction-validation.md,ask-policy-validation.md,principles-validation.md,controlled-yolo-validation.md,validation.md,full-validation.md}
eval/results/              # Private, gitignored execution evidence
docs/{architecture.md,skills-catalog.md,implementation-plan.md,corrections.md,backlog.md}
```

Recorded checks are scoped evidence, not deterministic model guarantees, production certification, cross-database compatibility, full accessibility compliance, or OS containment. Independently managed OMP/Tern/OVNFS upgrades require revalidation of relevant interfaces.
