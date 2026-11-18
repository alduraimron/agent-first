---
name: principle-prove-it-works
description: Establish direct evidence for requested behavior before claiming completion or relying on another actor's success report.
hide: true
---

# Prove It Works

## Purpose

Tie completion claims to the actual artifact and requested behavior. Compilation, timestamps, self-reports, and successful editing are useful observations but do not by themselves establish that the feature works.

## Triggers

- Work is ready for a completion claim.
- A generated artifact or delegated finding is being accepted.
- A check measures a proxy rather than the behavior users requested.

## Decision procedure

1. Translate each requested outcome into an observable condition and choose the smallest check that could falsify it. Reuse existing verification procedures and installed project tools.
2. Accept user reports and already observed failing tests as reproduction evidence. Do not rerun an unchanged failure simply to confirm it; target subsequent checks at the change or an unresolved question.
3. The main agent performs authorized checks against the actual affected artifact, including relevant failure paths. Advisory domains provide read-only analysis and check recommendations, not independent implementation or execution ownership.
4. Connect each result to its claim and environment. Finish when requested outcomes have direct supporting evidence or are explicitly marked NOT-RUN with the reason and remaining uncertainty.

## Trade-offs

Verification must be proportionate to risk and scope. A focused existing check can be better than a new harness or broad suite. Do not install dependencies, mutate production, bypass native denials, or trigger external effects to manufacture evidence. When a check fails, examine both its observation method and the system; do not dismiss the failure as a faulty measurement without evidence.

## Examples

**Good:** After changing CSV export, use the existing test or an authorized isolated run to inspect the produced header, row values, and escaping against a concrete expected result.

**Problematic:** Report that export works because the command exited zero or the output file's timestamp changed. Likewise, repeating an existing failing test before any change adds no reproduction evidence.

## Observable outcomes

Completion statements distinguish executed checks from expectations. Evidence concerns the delivered artifact, and unchecked behavior remains visible instead of being implied by a neighboring success.

## Verification

For every success claim, identify the actual observation and what incorrect result would have failed it. A claimed passing run without captured results, a proxy that cannot detect wrong output, or missing NOT-RUN disclosure falsifies the proof standard.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
