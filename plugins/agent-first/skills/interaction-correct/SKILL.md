---
name: interaction-correct
description: Address a user-identified agent mistake or evidenced repeated failure, distinguishing local correction from broader policy promotion.
hide: true
---

# correct - Reflection & Improvement

## Intent and trigger

Turn a demonstrated agent error into a durable correction. Use when the user identifies an agent mistake or repeated failure pattern.

## Procedure

1. Reconstruct expected versus observed behavior using source and logs. Treat the user's reported failure as evidence; do not rerun a failing check merely to confirm their report.
2. Identify root cause and failure layer, distinguishing confirmed cause from hypothesis.
3. Fix the local artifact only if authorized; route engineering changes through `skill://af-engineering`.
4. Propose a structural guard and regression evaluation.
5. Summarize recurrence evidence; record it durably only when requested or otherwise authorized, using `skill://af-context` for context/correction records.

## Output contract

Correction with cause, scope, test, residual risk, and promotion criteria. Distinguish proposed, implemented-unverified, and validated corrections.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. Do not convert one anomaly into a global rule or bypass approvals to fix configuration. A report of an error alone does not authorize artifact, policy, or runtime changes. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: The agent falsely claimed the test passed; correct the process.
- Success: Identify the unsupported claim, propose an evidence-backed correction, and preserve existing approval boundaries.
