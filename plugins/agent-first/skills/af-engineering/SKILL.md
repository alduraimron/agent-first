---
name: af-engineering
description: Route code/configuration changes, defect investigation/review and new check execution across the eight engineering workflows; documentation-only authoring and existing-evidence summaries use af-interaction.
---

# Adaptive engineering

Apply `rule://agent-first-shared`. This router serves main; advisors use their domain skill and read-only contract.

## Interaction boundary

Use `skill://af-interaction` for explanation, learning, interviews, ideation, rationale, catch-up, prose refinement, docs-only edits (e.g., README/ADR -> `skill://interaction-technical-writing`) or existing-evidence reports (e.g., diff/test summaries -> `skill://interaction-show-me-your-work`). Running new checks, defect diagnosis (`bug-investigation`), defect assessment (`code-review`) and code/config changes stay here. Mixed requests complete needed discussion first, then route authorized engineering here. Clear tasks need no interview ceremony.

## Route from evidence

1. Inspect the request, affected code, immediate callers and existing commands. Classify by intent, complexity, risk and architectural impact—never file count alone.
2. Start the **first visible prose** (including final or blocked-work reports) with the exact kebab-case literal prefix from the table below—never paraphrase it (e.g., `Workflow: quick-change`, not `Workflow: quick fix`)—followed by a brief rationale. Inspection tools may precede it.
3. Read the selected workflow procedure before acting. Reclassify visibly if evidence changes. `architecture-impacting` takes precedence whenever ownership, public contracts, persistence/schema, trust boundaries or dependency direction change. Investigation and review remain read-only unless edits are authorized.
4. After inspection, read `skill://af-principles` and only decision-triggered leaves before applying them (reassess if facts change). Keep trivial work lightweight.

| Intent | Exact literal prefix and procedure |
| --- | --- |
| Local understood low-risk edit; verification-only request | `Workflow: quick-change` — [procedure](skill://af-engineering/workflows/quick-change.md) |
| Add behavior within existing boundaries | `Workflow: feature-development` — [procedure](skill://af-engineering/workflows/feature-development.md) |
| Change an architectural boundary or contract | `Workflow: architecture-impacting` — [procedure](skill://af-engineering/workflows/architecture-impacting.md) |
| Initialize a personal project or recover missing project setup | `Workflow: project-initialization` — [procedure](skill://af-engineering/workflows/project-initialization.md) |
| Explain or fix unexpected behavior with an uncertain cause | `Workflow: bug-investigation` — [procedure](skill://af-engineering/workflows/bug-investigation.md) |
| Restructure code while preserving behavior and boundaries | `Workflow: refactoring` — [procedure](skill://af-engineering/workflows/refactoring.md) |
| Assess a patch or code for defects without implementing | `Workflow: code-review` — [procedure](skill://af-engineering/workflows/code-review.md) |
| Measure or improve latency, throughput, resource use or scalability | `Workflow: performance-optimization` — [procedure](skill://af-engineering/workflows/performance-optimization.md) |

## Requirements, domain skills and planning

Translate each requested outcome into observable acceptance criteria (failure paths, compatibility, non-goals) before editing. Inspect repo facts before asking questions. Trivial tasks need a narrow check, not a formal plan; multi-step work needs an ordered path to consumer-visible behavior with a check per criterion.

Before editing, open any project guidance linked from the project instructions whose scope matches the change. Load `skill://af-context` only when durable task/decision/recovery records matter. Load touched domain skills on demand: `af-design`, `af-database`, `af-frontend`, `af-testing`, `af-security`, `af-performance`, `af-operations`. Main owns edits and verification via `skill://af-verification`.

## Proportional consultation

- Trivial quick changes: **no delegation**.
- Consult only for material domain uncertainty or explicit requests for independent assessment: `af-architect`, `af-database`, `af-security`, `af-frontend`, `af-performance`, `af-devops`. `architecture-impacting` **requires** returned `af-architect` advice before affected edits; other consultations are conditional, not a checklist. Max 2 concurrent, depth 1, no child spawning.
- Dispatch via native `task` with exact `agent` name. Omit per-task `tools` (or leave empty): it forwards eval functions, not built-in permissions (frontmatter controls built-ins).
- Provide: concrete question, scope/non-goals, paths, observed facts, acceptance criteria, constraints, and exact `Principles:` handoff from `skill://af-principles` (exact catalog URIs or justified `none`). Children must read assigned leaves and cited source themselves. Main evaluates advice against source evidence before adopting or rejecting it.

## Bundled reviewer protocol

Use native `reviewer` for concrete independent risk (migration/data loss, authorization, concurrency, compatibility) or explicit review requests—not routine edits. **Mandatory** after implementation (before claiming completion) whenever changes affect authorization, private tenant isolation, destructive migration or shared-state concurrency invariants whose failure exposes or corrupts data; pre-design advice does not substitute for patch review.

1. **Supply verbatim inputs:** Collect `git diff --no-ext-diff --no-textconv` plus full content of untracked/new files (or complete scoped source for source-only review) and include them literally in task context—never a prose summary, and never expect `reviewer` to run Git.
2. **State explicit read-only scope & handoff:** Instruct `reviewer` to use only `read`, `grep`, `glob` (plus `yield` only if actually provided) under `rule://agent-first-shared`, include exact `Principles:` URIs, and require reading cited source and assigned leaves before advising (a verdict-only reply without own inspection is incomplete).
3. **Honor native output mode:** In OMP 18.22.1, `reviewer` declares a schema without opting into `structured: true`. If `yield` is available, preserve its schema: one finding object per `type: ["findings"]` yield (never an array), then a terminal yield without `type` containing `{overall_correctness, explanation, confidence}`. Otherwise request inspected findings and a concise verdict in its final response. Never enable `task.structured`, replace its schema or clone `reviewer`. Main resolves or documents disposition of every substantive finding; absence of findings is not verification.
