---
name: interaction-blast-radius
description: Identify concrete consumers, compatibility boundaries and side effects when asked what a proposed change affects or breaks.
---

# blast-radius - Understanding & Explanation

## Intent and trigger

Identify concrete consumers and side effects of a proposed change. Use when the user asks what will break, what is affected, or requests analysis before changing a shared contract.

## Procedure

1. Identify definition and call sites, exports, schemas, tests, deployments and data paths.
2. Classify direct versus transitive impacts.
3. Identify compatibility and rollback boundaries.
4. Recommend focused checks.

## Output contract

Impact map with known/possible/unknown effects and exact locations.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared RULES.md, accepted project decisions, and native permissions. Do not label search matches as verified runtime consumers or make speculative exhaustive claims. Analysis remains read-only; proposed checks are not execution authorization. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: What breaks if we change this interface?
- Success: Map concrete consumers and compatibility risks without changing the interface.
