---
name: af-engineering
description: Engineering workflow selection for ordinary fixes and features, architecture-impacting changes, or design consultations; inspect repository evidence, scale planning and advisory use to risk, and define acceptance criteria before main-agent implementation.
---

# Adaptive engineering

Apply the shared Agent-First RULES.md. The workflow below is for the main session. Advisory sessions use only the inspection, design-evaluation, and consultation guidance relevant to their assignment, then return advice under their agent contract.

## Classify from evidence

Inspect enough task context to identify the requested observable outcome, affected area, and existing conventions. Consider all three dimensions: complexity, risk, and architectural impact. Choose the smallest adequate route; file count alone is not a classifier.

After the required inspection, start the first prose report with one of these exact prefixes and a rationale covering those dimensions. Tool intents can describe inspection before that report:

- `Workflow: quick-change` for a localized, understood, low-risk change with no boundary or contract redesign.
- `Workflow: feature-development` for a behavior addition or multi-step change requiring acceptance criteria and a plan, without architectural impact.
- `Workflow: architecture-impacting` for a change to module/service ownership, public contracts, persistence/schema, security/trust boundaries, major dependency direction, or cross-cutting design.

Do not ask the user to select a workflow. If the initial route is provisional, say so. Reclassify visibly when inspection reveals different complexity, risk, or architectural impact; perform any newly required consultation before implementing the affected design. Do not inflate a trivial task into a design exercise.

A verification-only request uses quick-change with inspection and verification only. Make no modification when none was requested; do not invent another workflow category.

## Quick Change: Inspect -> Modify -> Verify

1. **Inspect**: read the affected code and immediate callers/tests; identify expected behavior and the narrow acceptance check. Exit when the change can be explained without a material unknown.
2. **Modify**: make the smallest complete main-agent change consistent with the local pattern. Skip delegation and formal plans for trivial work.
3. **Verify**: use `skill://af-verification`; finish only with evidence for the changed behavior or an explicit blocked/unverified requirement.

## Feature Development: Understand -> Plan -> Implement -> Verify

1. **Understand**: trace the current user-visible path and integration points. Record acceptance criteria including relevant failure/boundary behavior. Exit when every requested outcome has a concrete observable criterion; ask only about unresolved intent that repository context cannot answer.
2. **Plan**: give a short implementation sequence tied to those criteria and affected paths. Identify the installed verification commands and whether concrete risk warrants independent review. Reclassify if the plan changes architecture.
3. **Implement**: complete the end-to-end path in the main session, including callers and appropriate tests. Match existing conventions rather than adding a second mechanism. Exit when every acceptance criterion has an implementation and a planned check.
4. **Verify**: use `skill://af-verification`, including a consumer-visible/runtime check where applicable.

## Architecture-Impacting Change: Inspect -> Consult -> Evaluate -> Approval when needed -> Implement -> Verify

1. **Inspect**: trace affected boundaries, consumers, compatibility requirements, and existing design choices. Establish the design question and acceptance criteria before consulting.
2. **Consult af-architect**: request a native `task` consultation with `agent: af-architect`. Supply the question, paths, known evidence, alternatives under consideration, and scoped acceptance criteria. Ask for facts, assumptions, recommendations, and enforceable constraints. Complete this step on actual returned advice, not an announced intention to delegate. If consultation is denied or unavailable, report the exact blocker and leave the affected architectural change pending rather than claiming consultation occurred.

   Native task API: omit the per-task `tools` field or leave it empty. It forwards eval-defined functions, not built-in tool permissions; `read`, `grep`, and `glob` belong in agent frontmatter and the advisory assignment, not that field. Do not override the native agent output schema.
3. **Evaluate trade-offs**: compare advice to source evidence and the simpler viable alternative. State the chosen approach, important rejected alternative, compatibility/migration implications, and unresolved risks. Treat recommendations as proposals; retain, adapt, or reject them with a reason.
4. **Approval when needed**: apply the shared escalation boundary. A safe, reversible design inside the authorized request does not require ceremonial approval. Resolve required approval before the affected action.
5. **Implement**: the main agent implements the chosen design and its complete caller/migration path, then checks that the adopted constraints are represented in code and acceptance criteria.
6. **Verify**: use `skill://af-verification`; cover adopted invariants, changed contracts, and failure/rollback behavior relevant to the design.

## Conditional independent review

Use the bundled native `reviewer` only when a concrete unresolved risk benefits from independent inspection, such as authorization/data exposure, data loss/migration, subtle concurrency, or compatibility-sensitive behavior. State that risk in the task assignment. Routine edits do not need a reviewer, and architecture consultation alone does not imply a second review.

Provide the reviewer with the actual patch obtained by the main agent, changed paths, relevant contracts, acceptance criteria, the main agent's evidence, and a focused read-only question. In the assignment itself, explicitly limit inspection to `read`, `grep`, and `glob` and request native `yield` for its report; the supplied patch replaces its Git-command procedure. Its broader listed tools are not authorization to use them. Request evidence-backed findings with severity, location, failure scenario, and recommended checks. Resolve substantive findings yourself or explain, with evidence, why they do not apply. Run any required verification in the main session. No findings is not proof of correctness.

For the native reviewer handoff, each incremental `type: ["findings"]` yield contains one finding object, not an array. After any findings, request one terminal yield without `type`, with `data` containing `overall_correctness`, `explanation`, and `confidence`; do not repeat incremental findings. Successful yields omit `error` (or leave it empty if the provider requires the field). This uses the bundled schema rather than replacing it.
