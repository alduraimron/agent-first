# Agent-First Coding System

A reusable personal engineering environment built from native OMP profiles, skills, agents, approvals, sessions, and the existing Tern browser integration. Main selects the workflow and implements; specialists advise only when a concrete domain question warrants it. No separate orchestration runtime, extension, MCP server, Tern plugin, or memory database is added.

## Start in a personal project

Prerequisites: an existing OMP installation, Python 3.9+ for the launcher/evaluations, authorized model access, and Tern for browser work. Full SQLite evaluations use an existing Node 24+; the original evaluations need Node 18+ and Git. Optional isolation needs an existing OVNFS. Nothing installs or updates dependencies automatically.

```sh
# From this stable Agent-First checkout:
./bin/af --activate
./bin/af --cwd /absolute/path/to/personal-project --model PROVIDER/MODEL

# Or supply an ordinary outcome immediately:
./bin/af --cwd /absolute/path/to/personal-project --model PROVIDER/MODEL \
  "Add the requested feature and verify its real behavior"
```

The target directory must already exist. Choose a personal project, not a team/production repository. Replace the model selector with an authorized native OMP selector; current-policy probes use `opencode-go/gpt-5.6-luna`, while earlier results record their own models. For a new machine, authenticate separately with `omp --profile agent-first login`. The launcher never copies credentials; the historical Phase 1 credential transfer is documented in its validation record.

Use `bin/af` for the complete boundary, not merely `omp --profile agent-first`. Activation registers the five profile assets as symlinks under `~/.omp/profiles/agent-first/agent/`, refuses conflicting entries, and preserves the default profile. Keep this checkout at a stable path. Native persistent settings writes can update the linked personal config, so review operator changes.

Use a fresh `bin/af` launch for the updated policy. Current-policy evidence covers fresh launches, not hot-reload of an already running session.

Describe the desired result. Normal work does not require `/plan`, `/build`, `/review`, a workflow selector, or an agent name. Existing command definitions are not overwritten.

## Adaptive workflow library

Main inspects intent, complexity, risk, and architectural impact, announces the selected exact route prefix (for example, `Workflow: quick-change`) with a rationale, and reads the relevant procedure. New evidence can change the route; consequential changes follow the approval boundary.

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

Each procedure specifies inputs, steps/decision points, consultation criteria, verification, exit, and failure/escalation behavior. Architecture-impacting implementation requires actual architect advice first. Trivial changes do not delegate; read-only requests do not authorize edits.

## Domain consultation and skills

| Native agent | Domain skill | Consultation question |
| --- | --- | --- |
| `af-architect` | `af-design` | Boundaries, public contracts, ownership, compatibility and alternatives |
| `af-database` | `af-database` | Modeling, migrations, transaction integrity, query design |
| `af-security` | `af-security` | Trust, authorization, secrets, input-to-sensitive-sink paths |
| `af-frontend` | `af-frontend` | Interaction state, semantics, accessibility, responsive behavior |
| `af-performance` | `af-performance` | Measured bottlenecks, algorithms, resources and experiment design |
| `af-devops` | `af-operations` | Deployment ordering, health, observability, recovery |

Custom advisors expose only read/grep/glob, cannot spawn, and hand advice to main through native yield. Shared report fields live in `profile/RULES.md`; domain files define distinct engineering questions and constraints. Main evaluates advice, owns implementation, and performs checks. The bundled native `reviewer` is reused without a replacement definition. Routine work stays inline; implemented data-exposure/corruption invariants require independent review of the actual patch, not just pre-design consultation.

`af-engineering` owns requirements analysis, planning, routing and native consultation protocol. `af-testing` owns debugging/test design. `af-verification`, `af-context`, and `af-isolation` own execution evidence, durable project records, and optional checkout lifecycle. All eleven skills are model-discoverable; no manual skill invocation is required.

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
./bin/af --cwd /absolute/path/to/personal-project --continue
./bin/af --cwd /absolute/path/to/personal-project --resume PERSONAL_SESSION_ID
```

Resume file paths must exist inside the named profile. If a session is unavailable, describe the outcome or ask to continue the active project task; recovery uses repository records. Keep secrets/customer data out of tracked context and inspect raw evidence before sharing.

## Verification and approvals

Main selects installed project checks for relevant static/type/lint/build, regression/integration/consumer, API/database, security, performance, deployment, and browser/accessibility boundaries. Reports use **PASS**, **FAIL**, **NOT-RUN**, and **NOT-APPLICABLE**, with exact command/cwd/result, real runtime evidence, uncovered requirements, and remaining risks. Missing dependencies and denied checks are NOT-RUN, not success or irrelevance.

Browser checks use the existing native eval browser API inside Tern: preflight the existing host, observe, act through the UI, inspect resulting state/errors, exercise keyboard/semantic checks, and capture visual proof. Confirm the actual native backend; unsupported/manual assistive-technology and browser capabilities remain gaps. No fallback engine installation or fallback acceptance is authorized. Native Tern hosting can fall back to an owned engine, so this procedure is not a native fail-closed or no-download guarantee.

`profile/config.yml` is the settings authority and selects native **YOLO** autonomy. Routine scoped reads, edits, shell/eval verification, advisory task calls, and Tern interaction proceed without routine approval, including headless execution. YOLO auto-approves native read/write/exec tiers, not explicit denies or prompts. Restricted-folder gates and stricter explicit overlays still require native approval and refuse without an interactive approver. For bounded ordinary headless work:

```sh
./bin/af --cwd /absolute/path/to/personal-project --model PROVIDER/MODEL \
  --json --max-time 5m --max-cost 1 "Inspect the requested behavior"
```

Autonomy covers the authorized outcome, not permission to widen scope. Main asks at the point of risk for consequential actions outside that authorization; instructions carry this behavioral boundary, not a native semantic classifier. Explicit denies remain operator-only even after chat approval. The synthetic restrictive evaluation overlay is not an operating policy.

Safety defaults:

- Maximum two concurrent consultations, one delegation level; no implementation workers or nested spawning.
- Preserved explicit denies plus protected command families in `profile/config.yml`; denied operations, including Git publication, installations and OVNFS apply, require reviewed operator-terminal actions. Native commit/checkpoint helpers remain off.
- No automatic OVNFS task isolation/application, extension discovery, project MCP, foreign tool/agent/skill discovery, automatic memory learning, analysis backends or tool provisioning.
- Known native additive project tools and agent-shadowing definitions are refused. Existing project instructions remain loaded; native profile isolation does not isolate every external configuration source.
- Child native tiers also use yolo; explicit prompts/denies and advisory read-only scope still apply. The bundled reviewer has broader native metadata than its advisory scope; actual activity matters.
- Restricted folders gate path-tool targets, including symlink resolution, but gate shell/eval/browser by cwd rather than paths embedded in code. Ordered command patterns are not arbitrary-code inspection.
- Shell, eval, browser runtimes and trusted project scripts retain ambient filesystem/network/process authority. Inspect script definitions and bootstrap behavior before execution; tests/builds can fetch packages themselves. Use installed/cached/vendor/offline execution where appropriate and stop for missing dependencies. Never use code, wrappers or children to bypass policy. Neither profiles nor OVNFS provide OS containment. Use trusted personal projects, not hostile repositories.

## Optional OVNFS

Opt in explicitly for an experiment or isolated implementation. Use native `ovnfs new`, work in the printed checkout, inspect `ovnfs diff -p`, and obtain a dry-run result before integration. Approval of creation is not approval of apply.

The normal profile denies `ovnfs apply`, including dry-run. Main presents reviewed commands for the operator's own terminal rather than bypassing that deny. Integration requires exact patch/source approval and a recoverable baseline; reverify integrated source, and remove only owned checkouts. Full procedure and rollback limits: [af-isolation](profile/skills/af-isolation/SKILL.md). Automatic application stays disabled.

## Evaluate and improve

```sh
python3 -B eval/check_environment.py
python3 -B eval/check_controlled_yolo.py --model PROVIDER/MODEL
python3 -B eval/run.py --suite full --keep-workspaces \
  --model PROVIDER/MODEL --max-time 600 --max-cost 1.5
# Original cases remain available:
python3 -B eval/run.py --suite phase1 --model PROVIDER/MODEL
# Same original cases under normal permissions, without synthetic tool grants:
python3 -B eval/run.py --suite phase1 --policy profile --model PROVIDER/MODEL
```

The sequential native-session harness evaluates natural prompts and actual task/tool journals, then runs independent consumer and project checks. It preserves failed runs, private journals, workspace archives, and intermediate errors. Read-only, approval-denied, recovered-context and measured-optimization cases have explicit contracts instead of pretending every task must edit files.

Historical verification covers thirteen scenarios across explicit runs and two authorized models, all eight routes, the six advisors plus bundled reviewer, actual Tern interaction, and approved disposable OVNFS apply/restore/cleanup under the earlier policy. It is not a clean single-model full-suite result or evidence for the current YOLO policy; native reviewer timeouts and recovered tool/schema errors remain documented.

Current-policy probe results and limitations belong in [Controlled YOLO validation](eval/controlled-yolo-validation.md), separately from [historical full validation](eval/full-validation.md) and [Phase 1 history](eval/validation.md). See also [evaluation instructions](eval/README.md), [architecture](docs/architecture.md), [correction ledger](docs/corrections.md), and [improvement backlog](docs/backlog.md). The ledger records recurrence, root cause, smallest correction placement and actual validation; it does not automatically rewrite global policy after one failure.

## Source layout

```text
bin/af
profile/{config.yml,APPEND_SYSTEM.md,RULES.md}
profile/agents/             # Six native domain definitions; no reviewer copy
profile/skills/             # Eleven skills, eight workflows, context templates
eval/{run.py,check_environment.py,check_controlled_yolo.py,browser-check.mjs}
eval/{cases.json,extended-cases.json,ui-case.json,config.yml,profile.yml,prompt-check.yml}
eval/{README.md,controlled-yolo-validation.md,validation.md,full-validation.md}
eval/results/              # Private, gitignored execution evidence
docs/{architecture.md,implementation-plan.md,corrections.md,backlog.md}
```

Recorded checks are scoped evidence, not deterministic model guarantees, production certification, cross-database compatibility, full accessibility compliance, or OS containment. Independently managed OMP/Tern/OVNFS upgrades require revalidation of relevant interfaces.
