---
name: interaction-technical-writing
description: Write an accurate README, ADR, API guide, runbook or document-form technical explanation for an explicitly requested audience and task.
hide: true
---

# technical-writing - Understanding & Explanation

## Intent and trigger

Write accurate, usable engineering documentation. Use when the user explicitly requests a README, ADR, API guide, runbook, or technical explanation in document form.

## Procedure

1. Identify audience, task, and requested delivery form: chat document or a specific repository artifact. Use the request and existing project conventions to resolve the target where possible.
2. Inspect actual code/config, commands and supported behavior.
3. Organize prerequisites, steps, examples, failure modes and verification.
4. Review for ambiguous instructions, unsupported assertions, and commands whose effects or prerequisites need explanation.
5. Deliver copy-ready prose in chat unless the user requests creating or editing an artifact. For an authorized file request, write only the requested documentation and preserve unrelated content.

## Output contract

Copy-ready document or requested documentation file using factual code paths, commands and clearly labeled examples. Keep proposed decisions distinct from accepted ADRs.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. An explicit documentation file request may authorize that artifact, not code changes, Git actions, installation, publication, or executing documented commands. Do not claim tested commands without observed runs; avoid secret values and marketing filler. Use `skill://af-context` if the requested artifact is a durable context or handoff record. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Write a practical API integration guide.
- Success: Provide factual copy-ready documentation; edit a repository file only when that delivery was requested.
