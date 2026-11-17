---
name: interaction-bro
description: Explain technical ideas simply or casually, using an analogy while preserving accuracy.
---

# bro - Understanding & Explanation

## Intent and trigger

Translate technical ideas into plain language while preserving accuracy. Use when the user asks for a simple, casual explanation or analogy.

## Procedure

1. State the idea in one sentence.
2. Choose one grounded analogy.
3. Map the analogy back to actual components.
4. Identify where the analogy stops matching reality.

## Output contract

Short accessible explanation and one practical example if useful.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared RULES.md, accepted project decisions, and native permissions. Avoid patronizing tone, analogies that change semantics, or excessive slang. Explanation remains read-only. Label observations, inferences, unknowns, and unexecuted checks separately when relevant. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Explain event loops simply.
- Success: Give an accurate short explanation with a grounded analogy and its limits.
