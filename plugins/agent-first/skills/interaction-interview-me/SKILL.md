---
name: interaction-interview-me
description: Elicit requirements one focused question at a time when explicitly asked to interview or unresolved decisions prevent a useful design.
hide: true
---

# interview-me - Requirement Discovery

## Intent and trigger

Elicit requirements through focused questions with user agency. Use when the user explicitly asks to be interviewed or genuinely unresolved decisions prevent a useful design.

## Procedure

1. State the outcome to discover.
2. Ask exactly one highest-information question per turn, after using available context to avoid already answered questions.
3. Update confirmed assumptions in the conversation, distinguishing answers from unconfirmed assumptions.
4. Distinguish must-haves, constraints, risks and non-goals.
5. End with a reviewable brief when decisions are sufficient to describe the intended outcome, boundaries and acceptance examples; retain any remaining unknowns explicitly.

## Output contract

During the interview, one focused question per turn. At completion, a concise requirement brief with decisions, open questions and acceptance examples.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. Never interrogate before a straightforward task. Interviewing alone does not authorize implementation; if implementation was also requested, route it through `skill://af-engineering` once necessary discovery is complete. Label observations, inferences, unknowns, and unexecuted checks separately when relevant. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Interview me about a booking app idea.
- Success: Ask one material question at a time and finish with a reviewable brief, not an unrequested implementation.
