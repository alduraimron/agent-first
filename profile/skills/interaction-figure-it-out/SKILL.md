---
name: interaction-figure-it-out
description: Find a way forward for an unfamiliar problem when the approach or diagnostic starting point is unknown.
---

# figure-it-out - Requirement Discovery

## Intent and trigger

Structure exploration of unfamiliar problems with explicit uncertainty. Use when the user asks to find a way forward without a known approach or diagnostic starting point.

## Procedure

1. Clarify the outcome from the available request.
2. Inventory known facts, unknowns and existing capabilities.
3. Form competing hypotheses.
4. Select the cheapest permitted information-gathering experiment. Prefer source inspection for a discussion-only request; present experiments requiring writes, execution, sensitive access, or external effects as proposals unless separately authorized.
5. Update direction based on findings. When actual defect investigation is requested, use the existing investigation route through `skill://af-engineering`.

## Output contract

Best-supported path, confidence, failed approaches actually attempted, and next test. Keep proposed experiments distinct from executed ones.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared RULES.md, accepted project decisions, and native permissions. Do not install tools, browse sensitive data or take irreversible actions just to explore. Uncertainty is not permission escalation. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: We have an unfamiliar timeout; figure out the next diagnostic step.
- Success: Recommend a source-grounded next diagnostic step without silently executing a mutating experiment.
