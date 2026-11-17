---
name: af-engineering
description: Route ordinary engineering requests automatically across initialization, fixes, features, architecture, debugging, refactoring, review, and optimization; derive acceptance criteria and proportional plans before main-session implementation.
---

# Adaptive engineering

Apply shared RULES.md. This router serves the main session; advisors use the relevant domain procedure and their own read-only contract.

## Route from evidence

1. Inspect the request, affected code, immediate callers, and existing commands. Identify observable intent, complexity, risk, and architectural impact. File count is not a classifier.
2. Start the first visible prose with the selected row's exact literal prefix below, followed by a concise rationale covering intent, complexity, risk and architectural impact. Inspection tools may precede it. Verification-only and blocked requests still have a route; if the final report is the first prose, put the prefix there. Choose the smallest adequate procedure automatically, without asking the user to choose.
3. Read the selected procedure before acting. Reclassify visibly when evidence changes the route. Architecture-impacting takes precedence over implementation routes when changing ownership, public contracts, persistence/schema design, trust boundaries, dependency direction, or cross-cutting design. Investigation and review remain read-only unless modification is authorized.
4. After relevant inspection, read `skill://af-principles`, select by the actual decision triggers, and read the selected leaves before applying them. Reassess when evidence changes. Use the selector's proportionality guidance rather than loading a fixed bundle for each route.

| Intent | Route and procedure |
| --- | --- |
| Local understood low-risk edit; verification-only request | `Workflow: quick-change`: [procedure](skill://af-engineering/workflows/quick-change.md) |
| Add behavior within existing boundaries | `Workflow: feature-development`: [procedure](skill://af-engineering/workflows/feature-development.md) |
| Change an architectural boundary or contract | `Workflow: architecture-impacting`: [procedure](skill://af-engineering/workflows/architecture-impacting.md) |
| Initialize a personal project or recover missing project setup | `Workflow: project-initialization`: [procedure](skill://af-engineering/workflows/project-initialization.md) |
| Explain or fix unexpected behavior with an uncertain cause | `Workflow: bug-investigation`: [procedure](skill://af-engineering/workflows/bug-investigation.md) |
| Restructure code while preserving behavior and boundaries | `Workflow: refactoring`: [procedure](skill://af-engineering/workflows/refactoring.md) |
| Assess a patch or code for defects without implementing | `Workflow: code-review`: [procedure](skill://af-engineering/workflows/code-review.md) |
| Measure or improve latency, throughput, resource use, or scalability | `Workflow: performance-optimization`: [procedure](skill://af-engineering/workflows/performance-optimization.md) |

## Requirements and proportional planning

Before implementation, translate each requested outcome into an observable acceptance criterion, including relevant failure cases, compatibility, and non-goals. Separate facts from unresolved intent; inspect repository evidence before asking about the latter. A trivial task needs a narrow check, not a formal plan. Multi-step work needs an ordered path from entry point through dependencies to consumer-visible behavior, with a check for every criterion and explicit blockers.

Use `skill://af-context` when meaningful work needs durable requirements, decisions, recovery, or handoff. Load domain procedures only for touched concerns: `af-design` for boundaries/APIs; `af-database` for data; `af-frontend` for UI; `af-testing` for diagnosis/tests; `af-security` for trust; `af-performance` for measurement; `af-operations` for runtime delivery. Main owns edits and verification through `skill://af-verification`; shared safety and reporting remain in RULES.md.

## Proportional consultation

Trivial quick changes have no delegation. Consult only for a material domain question or uncertainty, or an explicit request for independent domain assessment: `af-architect` for architecture, `af-database` for persistence, `af-security` for trust, `af-frontend` for UI/accessibility, `af-performance` for measured bottlenecks, `af-devops` for deployment/observability. Architecture-impacting requires actual returned architect advice before affected implementation. Other consultations are conditional, not a six-agent checklist. Keep at most two concurrent consultations, recursion one, and no child spawning.

Supply the specific question, scope/non-goals, paths, observed evidence, acceptance criteria, alternatives, constraints, and requested advisory output. Follow RULES.md's principle handoff for relevant selected leaves; children must read them themselves. Use native `task` with the exact `agent` name. Omit per-task `tools` or leave it empty: it forwards eval functions, not built-in permissions. Agent frontmatter controls built-ins. Preserve native output schemas. Evaluate returned advice against source evidence and document adoption or rejection with reasons; an announced delegation is not consultation.

## Bundled reviewer protocol

Use native `reviewer` for a concrete independent-review question such as migration/data loss, authorization, concurrency, or compatibility risk, or when independent review is explicitly requested; routine edits do not require it. For an implemented authorization, private cross-tenant isolation, destructive migration, or shared-state concurrency invariant whose failure exposes or corrupts data, obtain a bundled review of the actual completed patch before declaring completion. Pre-implementation architect/security advice does not inspect the later patch.

Before a patch-review task, main obtains the actual diff with `git diff --no-ext-diff --no-textconv` and reads new-file content that Git omits. Include that verbatim diff and new-file content in the task context, not a prose summary labeled "actual patch". For a source-only review, supply the complete scoped source instead. Do not dispatch with missing review inputs and expect the reviewer to run Git to recover them; collect the inputs first or report the unavailable evidence.

State in the reviewer assignment that its tools are `read`, `grep`, `glob`, and native `yield` only under RULES.md, and that the supplied patch/source replaces its native Git-command procedure. Require inspection of relevant complete source and immediate contracts before yielding; a verdict-only response is incomplete. Main evaluates findings and verifies resulting implementation edits before handoff. This is a procedural scope constraint, not a change to the bundled reviewer's native tool metadata.

Each incremental `type: ["findings"]` yield contains one finding object, not an array. Request a terminal yield without `type`, whose `data` contains `overall_correctness`, `explanation`, and `confidence`, without repeating findings. Successful yields omit `error`, or leave it empty when required by the provider. Never replace the bundled schema. Main resolves substantive findings or records evidence for rejecting them; absence of findings is not verification.
