# Agent-First

Adaptive engineering workflows, selective decision principles, interaction skills, and read-only domain advisors for [OMP](https://github.com/can1357/oh-my-pi), packaged as a zero-runtime, project-scoped marketplace plugin.

## Quick Start

> Tested on **OMP 18.22.1** and **19.0.1**. Always pass `--scope project` so installation stays scoped to the target repository instead of OMP's default user scope.

### Install from GitHub

```sh
cd /path/to/your-project
omp plugin marketplace add alduraimron/agent-first
omp plugin install --scope project agent-first@agent-first
omp
```

Inside OMP, the equivalent commands are `/marketplace add alduraimron/agent-first` and `/marketplace install --scope project agent-first@agent-first`.

### Install from a local checkout

```sh
cd /path/to/your-project
omp plugin marketplace add /absolute/path/to/agent-first
omp plugin install --scope project agent-first@agent-first
omp
```

## Usage

Run ordinary `omp` — no wrapper command, custom profile, or manual workflow syntax is required:

```sh
omp "Add pagination to the tasks endpoint and verify its behavior"
omp --model PROVIDER/MODEL "Review this diff for concurrency bugs"
omp --continue
```

### Project Architecture & Standards

Start with a discussion in a project that has Agent-First installed: “Let's decide this project's architecture and coding conventions before implementing.” No files change during discussion. To record the settled decisions, say “Save the approved standards and architecture decisions.” To add one later, ask to record the specific rule.

Keep short project-wide rules in `AGENTS.md` (or the existing instruction file). Link to area guides and architecture docs with a trigger for when to read each one. Recording decisions does not change code or create `.agent-first/` records.

### Delegated Implementation

Ask “Plan this change for delegated implementation; I'll pick the worker model after seeing the plan.” Agent-First writes one shared task brief and one assignment per verifiable slice under `.agent-first/tasks/`, then pauses without editing code.

When ready, ask it to start and select a worker model with `^` in the OMP composer. Main checks each slice before starting its dependents, then verifies the combined change. The `^` route can inherit native model fallback. For an exact model without main-loop fallback, use an operator-approved native per-call model instead. Without delegation opt-in, main implements as usual.

### Update & Uninstall

```sh
omp plugin marketplace update agent-first
omp plugin upgrade --scope project agent-first@agent-first
omp plugin uninstall --scope project agent-first@agent-first
```

Start a new session after CLI plugin changes (or use `/reload-plugins` in the TUI for skills and agents; restart for a full rule rebuild).

## What's Included

### Engineering Workflows

Main classifies the request, announces `Workflow: <route>`, and adapts the procedure proportionally:

| Workflow | When it triggers |
| --- | --- |
| `quick-change` | Localized low-risk edits or verification-only checks |
| `feature-development` | New behavior within existing boundaries |
| `bug-investigation` | Unexpected behavior with an uncertain root cause |
| `refactoring` | Behavior-preserving restructuring |
| `architecture-impacting` | Boundary, ownership, schema, or public contract changes (requires `af-architect`) |
| `code-review` | Read-only defect assessment |
| `performance-optimization` | Measured latency, throughput, or resource bottlenecks |
| `project-initialization` | Setting up a new project or recovering missing baseline setup |

Questions, explanations, teaching, interviews, catch-up, reflection, and docs-only edits route through [`af-interaction`](plugins/agent-first/skills/af-interaction/SKILL.md) (read-only by default).

### Read-Only Advisors

| Advisor | Domain Skill | Focus |
| --- | --- | --- |
| `af-architect` | `af-design` | Boundaries, contracts, ownership, compatibility |
| `af-database` | `af-database` | Schemas, migrations, transactions, query plans |
| `af-security` | `af-security` | Trust boundaries, authz, sensitive data, abuse paths |
| `af-frontend` | `af-frontend` | UI state, accessibility, keyboard & responsive behavior |
| `af-performance` | `af-performance` | Profiling, benchmarks, bottlenecks |
| `af-devops` | `af-operations` | Deployment, lifecycle, health, observability, recovery |

All six advisors are restricted to `read`, `grep`, `glob`, and structured `yield` (`spawns: []`). Independent patch review reuses OMP's native bundled `reviewer`.

### Verification, Context & Optional Tools

- **Evidence-based verification** ([`af-verification`](plugins/agent-first/skills/af-verification/SKILL.md)): runs existing project checks and reports `PASS`, `FAIL`, `NOT-RUN`, and `NOT-APPLICABLE` with commands and gaps.
- **Durable project memory** ([`af-context`](plugins/agent-first/skills/af-context/SKILL.md)): optional `.agent-first/` templates for active tasks, decisions, handoffs, and verification logs — created only when needed.
- **Optional integrations**: supports interactive browser verification via existing Tern hosting and explicit opt-in isolated checkouts via [`af-isolation`](plugins/agent-first/skills/af-isolation/SKILL.md) (OVNFS). Neither is provisioned or enabled automatically.

See the [skills catalog](docs/skills-catalog.md) for all 57 skills and [architecture](docs/architecture.md) for rule and scope details.

## License & Attribution

Released under the [MIT License](LICENSE).

- The engineering principles layer adapts [pstack](https://github.com/cursor/plugins/tree/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack) (Copyright © 2026 Lauren Tan, MIT) — see [SOURCES.md](plugins/agent-first/skills/af-principles/SOURCES.md) and [LICENSE](plugins/agent-first/skills/af-principles/LICENSE).
- Interaction skill provenance is documented separately in [af-interaction/SOURCES.md](plugins/agent-first/skills/af-interaction/SOURCES.md).
