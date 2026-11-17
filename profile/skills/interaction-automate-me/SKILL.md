---
name: interaction-automate-me
description: Find recurring tasks or documented repeated steps suitable for safe automation, proposing a design before authorized implementation.
---

# automate-me - Reflection & Improvement

## Intent and trigger

Find repeatable work suitable for safe automation. Use when the user asks to automate a recurring task or repeated steps are documented.

## Procedure

1. Measure the repeated sequence and variability from available evidence; identify missing measurements rather than inventing frequency or savings.
2. Search for existing native features.
3. Specify input/output, triggers, idempotency, error handling, approval boundaries and rollback.
4. Implement only if authorized, through `skill://af-engineering` and any relevant skill-authoring guidance.

## Output contract

Automation proposal or authorized skill/script with checks and ownership. Separate projected benefits from measured results.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared RULES.md, accepted project decisions, and native permissions. Do not create a new framework or schedule external actions without explicit request. A proposal, documented repetition, or request about feasibility does not authorize implementation, installation, or recurring execution. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: I repeat this release checklist weekly. Can we automate it?
- Success: Propose safe automation and its boundaries without silently scheduling or implementing it.
