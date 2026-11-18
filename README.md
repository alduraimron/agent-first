# Agent-First Coding System

Agent-First **2.0.0** is a native OMP marketplace plugin for trusted personal projects, supported on **OMP 18.22.1**. Main selects a proportional workflow, implements and verifies; specialists advise. No launcher, named profile, extension runtime, MCP server or package dependencies are added.

## Project installation

Use existing OMP and normally configured authorized model access. Agent-First supplies no model, credentials, permissions or configuration overrides.

This migration is currently local, not evidence of a published GitHub release. To test the checkout, start in the intended project:

```sh
cd /path/to/personal-project
omp plugin marketplace add /absolute/path/to/agent-first
omp plugin install --scope project agent-first@agent-first
omp
```

After release 2.0.0 is published to `alduraimron/agent-first`, use:

```sh
cd /path/to/personal-project
omp plugin marketplace add alduraimron/agent-first
omp plugin install --scope project agent-first@agent-first
omp
```

Local and GitHub catalogs share the marketplace name. Choose one deliberately; inspect `omp plugin marketplace list` rather than assuming a new add replaced an existing registration. Inside OMP the equivalent commands are `/marketplace add alduraimron/agent-first` and `/marketplace install --scope project agent-first@agent-first`.

**Always specify project scope.** Native installation defaults to user scope; that is not the supported Agent-First mode, and the manifest cannot enforce scope.

OMP anchors project state at the nearest ancestor containing `.omp/`, otherwise the nearest Git root. With neither, explicit project installation can create `.omp/` in cwd; home is not a project. Installation applies to all descendants of that anchor, not just the invoking directory. A workspace-level `.omp/` can therefore cover multiple repositories. Choose the boundary intentionally; there is no enrollment or automatic personal/team ownership detection.

Project registration lives under `<anchor>/.omp/plugins/`. Native marketplace registry and catalog/plugin caches use user storage, normally `~/.omp/marketplaces.json` and `~/.omp/plugins/cache/`; XDG roots can differ. These writes are not approval/model settings changes. Installation does not overwrite `AGENTS.md` or project/user config.

## Everyday use, update and removal

Use ordinary native OMP:

```sh
omp "Add the requested feature and verify its real behavior"
omp --model PROVIDER/MODEL "Inspect this behavior"
omp --continue
omp --resume SESSION_ID
```

No `af`, setup, named profile, enrollment or manual workflow command is needed. Existing native instructions and operator model routing remain effective.

```sh
omp plugin marketplace update agent-first
omp plugin upgrade --scope project agent-first@agent-first
omp plugin uninstall --scope project agent-first@agent-first
```

Catalog update alone does not reinstall. Named upgrade reinstalls the catalog version even when unchanged. Version-keyed cache content is shared across projects and user/project scopes: same-version reinstall can affect other installs using that cache. Publish a new immutable version for content changes rather than repacking an installed version; project scope controls registration, not private cache copies.

Start a new session after CLI lifecycle changes. TUI marketplace mutations change disk/cache state without refreshing the active session: `/reload-plugins` refreshes skills, task agents, commands and MCP servers. Restart for a complete rule/context rebuild, and for newly installed non-MCP tools, hooks or extensions in other plugins. TUI `/plugins enable` and `/plugins disable` refresh supported active capabilities immediately; ACP/RPC refresh behavior differs. See [native marketplace semantics](omp://marketplace.md).

### Coexistence and migration

Operator provider disables, plugin feature selection, skill filters, rule controls and disabled-agent settings remain authoritative. Native skill precedence keeps the higher-priority bare name, namespaces differing copies and collapses identical copies. Agents use exact-name first-wins shadowing: native project/user definitions and earlier extension roots can shadow marketplace advisors or bundled `reviewer`. A name alone does not prove which definition ran. Report inaccessible/shadowed required material rather than overriding operator controls.

The retired launcher/profile and custom permission matrix are no longer distributed. Existing real `~/.local/bin/af` and named-profile symlinks are **not automatically deleted or rewritten**; plugin uninstall does not remove them. Optional operator-reviewed cleanup must inspect each link and resolved target, remove only verified old Agent-First links you own, and preserve real files, unrelated links, credentials and session history. Never use broad recursive removal. Run ordinary `omp`, not a stale launcher.

## Adaptive workflows

Main announces `Workflow: <route>` with its rationale, then follows **workflow -> relevant domain procedure -> relevant principles -> main implementation and checks**.

| Intent | Procedure |
| --- | --- |
| New project | [project-initialization](plugins/agent-first/skills/af-engineering/workflows/project-initialization.md) |
| New behavior within existing boundaries | [feature-development](plugins/agent-first/skills/af-engineering/workflows/feature-development.md) |
| Unexpected behavior or uncertain cause | [bug-investigation](plugins/agent-first/skills/af-engineering/workflows/bug-investigation.md) |
| Behavior-preserving restructuring | [refactoring](plugins/agent-first/skills/af-engineering/workflows/refactoring.md) |
| Changed architectural boundary/contract | [architecture-impacting](plugins/agent-first/skills/af-engineering/workflows/architecture-impacting.md) |
| Read-only defect assessment | [code-review](plugins/agent-first/skills/af-engineering/workflows/code-review.md) |
| Measured resource/latency problem | [performance-optimization](plugins/agent-first/skills/af-engineering/workflows/performance-optimization.md) |
| Local understood low-risk edit | [quick-change](plugins/agent-first/skills/af-engineering/workflows/quick-change.md) |

Architecture-impacting implementation requires actual architect advice first. Trivial work stays inline. Explanation, teaching, interviews, idea/design discussion, recovery, reflection and writing use [af-interaction](plugins/agent-first/skills/af-interaction/SKILL.md) and the smallest relevant `interaction-*` leaf. Conversations default to read-only; explicit artifact requests authorize only those artifacts. Clear changes need no mandatory interview. Design discussion does not replace required architectural consultation for implementation.

## Skills and consultation

| Native advisor | Domain skill |
| --- | --- |
| `af-architect` | `af-design` |
| `af-database` | `af-database` |
| `af-security` | `af-security` |
| `af-frontend` | `af-frontend` |
| `af-performance` | `af-performance` |
| `af-devops` | `af-operations` |

All six read-only advisors expose read/grep/glob, prohibit spawning, declare `structured: true` plus a native `{report: string}` output schema, and autoload their domain skill plus `af-principles`. The schema is necessary for native yield; the flag alone does not create it. Main supplies selected leaf URIs, triggers and the question; children read them themselves. Main owns implementation/checks. Reuse the bundled `reviewer` with actual patch/source and explicit read-only scope, not a copied definition or forced global output mode. Two consultations and one delegation level are behavioral limits, not installed scheduler settings.

The plugin contains **57 skills: 13 visible and 44 hidden-but-readable leaves**. Frontmatter `hide: true` hides 24 principle and 20 interaction leaves without removing enabled `skill://` access. Read only relevant full leaves, usually one to three per decision; trivial work normally needs proof alone. Metadata and name mentions do not establish application. See the [complete catalog](docs/skills-catalog.md).

## Context and recovery

[af-context](plugins/agent-first/skills/af-context/SKILL.md) retains templates for meaningful project records:

```text
.agent-first/
  context.md
  tasks/<task-id>.md
  decisions/<id>.md
  verification.md
  handoff.md
  issues.md
  corrections.md
```

Create only relevant records, not empty paperwork. Accepted decisions are authoritative; native sessions retain execution history. Recovery reads active task, relevant decisions and handoff, reconciles source changes and treats old results as historical until applicable. Read-only work proposes records rather than writing them. Keep secrets/customer data out of tracked context; inspect journals before sharing.

## Authorization, verification and optional tools

Agent-First inherits native operator/project permissions, guards, model routing and tool/provider settings unchanged. It ships no config, approval mode or AUTO/ASK/DENY command-pattern policy. Authorization remains scoped to the requested outcome. Verify exact project/runtime/database/remote and Docker endpoints before effects. Refusal or unavailable approval blocks dependent actions, not independent safe work; never bypass through wrappers, eval or children. Commit/push requires explicit user instruction.

Choose affected static/type/lint/build, regression/consumer, database, security, performance, operational and UI checks from existing tools. Report **PASS**, **FAIL**, **NOT-RUN** and **NOT-APPLICABLE**, exact command/cwd/results and gaps. Missing dependencies or denied checks are NOT-RUN. Do not automatically provision unrelated tools, runtimes, backends or browsers.

Browser checks use existing Tern hosting/native APIs: preflight the host, observe actual backend, interact through the UI, inspect state/errors and capture evidence. Requesting Tern is not a native fail-closed/no-download guarantee; fallback can occur. Reject unexpected backend coverage honestly.

[OVNFS](plugins/agent-first/skills/af-isolation/SKILL.md) is explicit opt-in only. Use installed `ovnfs new`, work in its printed checkout, inspect `ovnfs diff -p`, review source concurrency and preserve a recoverable baseline. Dry-run, real integration and discard/cleanup require separately scoped authorization plus configured native gates. No automatic apply occurs; reverify integrated source. Checkout removal does not undo applied source changes. Neither OVNFS nor tool grants is an OS sandbox: ambient network, credentials, processes and host paths remain.

## Evaluation and evidence

```sh
# No paid model run:
python3 -B eval/check_plugin.py
python3 -B eval/check_principles.py
# Explicitly authorized model evaluations:
python3 -B eval/check_interactions.py --model PROVIDER/MODEL
python3 -B eval/run.py --policy native --suite phase1 --model PROVIDER/MODEL
python3 -B eval/run.py --policy strict --suite principles --keep-workspaces \
  --model PROVIDER/MODEL --max-time 600 --max-cost 1.5
```

Executed results and retained failures are in the [plugin migration validation report](eval/plugin-migration-validation.md). Native lifecycle/loading and actual Tern follow-through passed; some model workflow/hand-off checks failed. The report separates source state, parser replay, consumer correctness and model compliance rather than claiming a blanket pass. [Evaluation guidance](eval/README.md) documents independent test controls. Old launcher/permission reports are historical only.

## Source and references

```text
.omp-plugin/marketplace.json
plugins/agent-first/.omp-plugin/plugin.json
plugins/agent-first/{rules,agents,skills}/
eval/                       # Lifecycle, discovery and behavior checks; historical evidence
docs/                       # Architecture, catalog, cutover plan and backlog
```

Native references: [marketplace](omp://marketplace.md), [task discovery](omp://task-agent-discovery.md), [skills](omp://skills.md), and OMP v18.22.1 `packages/coding-agent/src/discovery/claude-plugins.ts` `loadRules` for marketplace rules (some marketplace summaries omit them). See [architecture](docs/architecture.md) and [backlog](docs/backlog.md).

The principle layer adapts [pstack revision 2f87c854fe3e2fcda44ca86b46ede35aad3c46b7](https://github.com/cursor/plugins/tree/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack), Copyright (c) 2026 Lauren Tan, MIT, with [sources](plugins/agent-first/skills/af-principles/SOURCES.md) and [preserved license](plugins/agent-first/skills/af-principles/LICENSE). Interaction provenance is [separate](plugins/agent-first/skills/af-interaction/SOURCES.md). Evidence is not all-model reliability, production certification, complete accessibility or OS containment.
