---
name: interaction-pause-safely
description: Prepare a recoverable handoff and next safe action when asked to pause a task or prepare continuation.
hide: true
---

# pause-safely - Context & Communication

## Intent and trigger

Create a recoverable handoff when stopping a meaningful task. Use when the user asks to pause or prepare continuation.

## Procedure

1. Capture current goal, state, affected files, pending decisions, last verification and known failures.
2. Identify owned processes/temporary files and any unknown ownership. Report their observed state; identification is not cleanup or cancellation.
3. Document safe resumption steps, including pending execution or cleanup and its permission requirements.
4. Write project context only when authorized. An explicit request to record a handoff or context may authorize those artifacts alone; use `skill://af-context` for their structure and consistent state. Otherwise provide the handoff in chat.

## Output contract

Minimal handoff with the very next safe action and any ongoing process or cleanup uncertainty.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. Pausing does not authorize commits, pushes, deletion, or unrelated process termination. Stop an owned process only when separately authorized and safe; claim cancellation, termination, or cleanup only after observing its result. Do not claim that preparing a handoff stopped a running command. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Pause here and record a handoff for a fresh session.
- Success: Record only the requested handoff/context artifacts and preserve accurate process and verification state.
