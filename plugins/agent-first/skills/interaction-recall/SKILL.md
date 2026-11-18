---
name: interaction-recall
description: Recover specific past decisions, requests, attempts or recorded facts from scoped project context and accessible history.
hide: true
---

# recall - Context & Communication

## Intent and trigger

Recover specific past decisions and facts from durable project context. Use when the user asks what was decided, requested, tried, or recorded before.

## Procedure

1. Read scoped `.agent-first` context and current project evidence; use `skill://af-context` when its recovery procedures are needed.
2. Search relevant native session history only when accessible and permitted.
3. Distinguish historical state from current state.
4. Identify conflicting records and missing history rather than silently resolving them by date alone.

## Output contract

Source-backed answer with dates or locations where available and explicit missing history.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. Never fabricate memory or claim current code matches old notes without checking. Recall is read-only; it does not authorize creating or rewriting context records. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: What did we decide about authentication?
- Success: Cite the recorded decision or identify unavailable/conflicting history without inventing rationale.
