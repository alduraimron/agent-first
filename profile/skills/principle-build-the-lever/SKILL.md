---
name: principle-build-the-lever
description: Reuse or build proportionate tooling when repetition, error risk, or reproducibility makes manual work inferior.
---

# Build the Lever

## Purpose

Make error-prone work repeatable and inspectable with the smallest adequate tool. The lever may already exist as a native operation, project command, structural edit, or check; creating a new artifact is not the objective.

## Triggers

- Repeated edits must preserve the same nontrivial invariant.
- Manual analysis or checking is difficult to reproduce reliably.
- A migration's error risk or scale justifies deterministic transformation.
- Existing tooling can turn a fragile procedure into a bounded operation.

## Decision procedure

1. Inspect installed native and project tools before proposing code. Identify the work unit, expected result, error modes, and likely repetition. Compare tooling cost with saved effort, reduced mistakes, and reproducibility.
2. Choose direct editing for a few obvious one-off changes. Otherwise select an existing operation; build a small script or codemod only when it closes a concrete capability gap. Do not install dependencies automatically.
3. Understand one representative unit before generalizing. Define selection boundaries, preserved content, and the expected transformation. Prefer syntax-aware tooling when structure matters.
4. Have main validate the lever on that unit before broad application. Make reruns safe through idempotence or explicit preconditions that reject already transformed input without damaging it. Keep writes within the authorized scope and preserve unrelated user changes.
5. Finish when all selected units meet the invariant and excluded units remain untouched. Retain a reusable artifact only when future use justifies its maintenance; remove disposable scripts. No committed artifact, commit, or publication is automatic.

## Trade-offs

A framework can cost more than the task it automates. A text substitution is unsafe when identical spelling has different semantics. Determinism does not establish correctness, and automation must not widen authorization or replace main's responsibility for implementation and checks.

## Examples

**Good:** Reuse an installed structural-edit tool to rename calls of one resolved internal API, checking representative transformed and excluded call sites before applying it across the migration.

**Problematic:** Create a generator framework to rename two obvious fields, or replace every matching token without distinguishing strings, unrelated methods, and supported external contracts.

## Observable outcomes

Repeated work follows one inspectable transformation. Selection boundaries and rerun behavior are explicit, with less manual drift and no unnecessary tooling layer.

## Verification

Main uses `skill://af-verification` to compare expected and actual transformed units, exclusions, and affected consumer behavior. Check rerun safety where promised. Report unavailable execution as NOT-RUN; successful tool exit alone does not establish semantic correctness.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
