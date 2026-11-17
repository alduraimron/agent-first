---
name: interaction-why
description: Investigate rationale, history or design intent behind an implementation or surprising decision using source and historical evidence.
---

# why - Understanding & Explanation

## Intent and trigger

Investigate why an implementation or decision exists. Use for questions about rationale, history, design intent, or a surprising decision.

## Procedure

1. Inspect relevant source and tests.
2. Search local decision records and scoped Git log/blame if permitted; use accessible session history only when relevant and authorized.
3. Distinguish documented reason, plausible hypothesis, and unknown.
4. Compare rejected alternatives only when evidenced.

## Output contract

Timeline of evidence with explicit confidence; identify who or what can resolve unknown intent. If history is unavailable, say so rather than fabricating a timeline.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared RULES.md, accepted project decisions, and native permissions. Do not invent developer motivation or pretend current code proves historical intent. Separate documented public rationale from hypotheses; do not reconstruct private reasoning. Historical explanation is read-only. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Why was Redis introduced here?
- Success: Cite actual decision/history evidence or state that the original rationale is unknown.
