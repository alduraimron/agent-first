---
name: interaction-in-your-own-words
description: Restate a user's requested outcome and boundaries when asked to confirm intent or when an ambiguous consequence changes the decision.
hide: true
---

# in-your-own-words - Requirement Discovery

## Intent and trigger

Restate requested outcome and boundaries to check shared understanding. Use when the user says repeat/confirm my request, summarize my intent, or there is a material ambiguous consequence.

## Procedure

1. Restate goal, target, constraints, non-goals, definition of done and remaining uncertainties.
2. Differentiate explicit statements from assumptions.
3. Ask only the single decision-changing question if needed.

## Output contract

Compact understanding statement with assumptions and any required approval point. If none is needed, proceed within the existing authorization instead of requiring confirmation.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. Do not turn all coding requests into mandatory confirmation or falsely imply agreement. Restatement alone does not expand authorization. Label observations, inferences, unknowns, and unexecuted checks separately when relevant. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Repeat what I want before making any changes.
- Success: Give a compact, faithful restatement and respect the requested pause before edits.
