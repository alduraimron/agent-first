---
name: interaction-show-me-your-work
description: Explain what changed, how it was done and the observable implementation or decision evidence when asked to show proof.
hide: true
---

# show-me-your-work - Context & Communication

## Intent and trigger

Explain the observable decision and implementation evidence. Use when the user asks what changed, how it was done or to show proof.

## Procedure

1. Inspect exact relevant diffs, retained outputs, source references and recorded decisions. For Git evidence use `git diff --no-ext-diff --no-textconv` and `git status --short`. Keep both diff flags on every invocation, including `--stat` or `--cached`, so configured external diff/textconv helpers do not execute during read-only inspection.
2. Map each requested outcome to its implementation and check, or identify missing implementation/evidence.
3. Separate absent evidence from failure. Use `skill://af-verification` for evidence meanings and applicability; report NOT-APPLICABLE when justified, not as a substitute for missing evidence.

## Output contract

Change-to-evidence map with PASS/FAIL/NOT-RUN/NOT-APPLICABLE and limitations, with a concise public rationale where useful.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. Provide an understandable evidence-based summary, not hidden private reasoning or a reconstructed internal monologue. Do not invent tool results, imply inspected tests ran, or claim historical evidence verifies current changes without establishing applicability. Showing existing evidence is read-only and does not itself authorize new runs or artifact edits; explicit verification requests retain their engineering route. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional; advisors are optional for material specialist questions.

## Example invocation

- User: Show what changed and which checks passed.
- Success: Cite actual changes and retained results, stating exactly what was not checked.
