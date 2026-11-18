---
name: interaction-ketchup
description: Summarize current project progress, completed work, blockers and next actions when asked for a catch-up.
hide: true
---

# ketchup - Context & Communication

## Intent and trigger

Produce a concise project catch-up and current-state brief. Use when the user asks what happened, what is done or what remains.

## Procedure

1. Read the active task, handoff, recent relevant decisions, verification and current working state when available. Use `skill://af-context` for scoped recovery; missing context is a stated gap, not permission to create files.
2. Separate completed, in-progress, blocked and next actions.
3. Identify stale evidence, comparing stored claims with current source and available state rather than treating timestamps as proof.

## Output contract

Short state-of-work brief with the next actionable item and verification status.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. Do not treat old PASS as current; avoid dumping the entire history. A catch-up request remains read-only and does not authorize context refreshes or new verification runs. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Catch me up on this project.
- Success: Summarize actual current progress and evidence gaps without updating project files.
