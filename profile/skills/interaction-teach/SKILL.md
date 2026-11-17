---
name: interaction-teach
description: Teach a concept at the requested depth using real project examples, a source reading path and optional practice.
---

# teach - Understanding & Explanation

## Intent and trigger

Teach a developer a concept grounded in the project at an appropriate depth. Use when the user asks to learn, be taught, practice, or understand deeply.

## Procedure

1. Assess current level from the request, not an assumed biography.
2. Explain a small mental model.
3. Use the real source as an example.
4. Introduce one concept at a time.
5. Invite a small exercise and give feedback when answered.

## Output contract

Clear conceptual explanation, actionable source reading path, and optional short practice prompt. Mark any suggested commands or exercises as unexecuted unless observed.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared RULES.md, accepted project decisions, and native permissions. Do not turn a request for a quick answer into a long lesson or alter code to teach. Exercises are invitations, not authorization to execute commands or modify files. Label observations, inferences, unknowns, and unexecuted checks separately when relevant. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Teach me this routing code.
- Success: Build a small mental model from real source and offer optional practice without changing the code.
