---
name: interaction-unslop
description: Rewrite prose for precision, concision or clearer communication while preserving evidence, uncertainty and important constraints.
hide: true
---

# unslop - Interaction Quality

## Intent and trigger

Make writing precise and proportionate without erasing important information. Use when the user requests a concise rewrite, less filler, clearer outputs, or a communication quality pass.

## Procedure

1. Identify audience and purpose.
2. Remove repetition, vague claims, cliches and inflated language.
3. Preserve evidence, constraints, uncertainty and actionable next steps.
4. Check for changed meaning.

## Output contract

Clear revised content with faithful technical assertions.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. Do not conceal risk, missing verification or source attribution for brevity. Return rewritten prose in chat unless editing the source artifact was explicitly requested; authorization covers only that artifact. Label observations, inferences, unknowns, and unexecuted checks separately when relevant. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Make this report concise without hiding failures.
- Success: Preserve the failures, limitations and attribution in a clearer, shorter report.
