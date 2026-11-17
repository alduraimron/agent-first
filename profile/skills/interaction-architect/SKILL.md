---
name: interaction-architect
description: Compare architectural options and trade-offs before implementation, facilitating a decision without executing it.
---

# architect - Requirement Discovery

## Intent and trigger

Facilitate an architecture decision without executing it. Use when the user asks for architectural options or trade-offs before implementation.

## Procedure

1. Inspect contracts and constraints.
2. Identify decisions and source of truth.
3. Compare existing design with viable alternatives.
4. Evaluate consistency, operations, migrations and reversal.
5. Document proposed invariants in the response or explicitly requested artifact, keeping proposals distinct from accepted decisions.

## Output contract

Decision options, recommendation, risks and checks. Refer a substantive domain question to `skill://af-design` or the `af-architect` advisor when needed.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared RULES.md, accepted project decisions, and native permissions. Discussion-only requests do not authorize code edits. This skill does not substitute for mandatory architect advisory in an engineering workflow; interaction-only consultation remains optional. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional to the request.

## Example invocation

- User: Compare monolith versus service boundaries without coding.
- Success: Deliver decision options and a recommendation without implementation or permission escalation.
