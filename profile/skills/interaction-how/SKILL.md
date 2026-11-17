---
name: interaction-how
description: Explain how a feature, API, module or flow works by tracing actual source paths and observable behavior.
---

# how - Understanding & Explanation

## Intent and trigger

Explain implemented behavior and code paths, not merely intended architecture. Use for questions asking how a feature, API, module, or flow works.

## Procedure

1. Locate the entry point.
2. Trace caller -> data transformations -> side effects -> outputs.
3. Identify boundary cases and relevant tests by inspection.
4. Communicate a minimal call/data-flow map.

## Output contract

Explain the observable flow with cited paths/symbols and gaps. Distinguish source-traced behavior from observed runtime execution.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared RULES.md, accepted project decisions, and native permissions. Do not edit code or claim unobserved runtime execution. Inspecting a test does not mean it ran. Explanation remains read-only. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: How does login work in this repository?
- Success: Explain the actual source flow with references and explicit runtime evidence limits.
