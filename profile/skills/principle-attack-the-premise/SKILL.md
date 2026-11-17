---
name: principle-attack-the-premise
description: Test the shared assumption before another fix when two attempts fail the same gate.
---

# Attack the Premise

## Purpose

Break a cycle of plausible fixes that all depend on the same incorrect model. Investigate the assumption that predicts success before adding another mechanism that merely compensates for failure.

## Triggers

- Two or more fixes sharing an assumption fail the same acceptance gate.
- Increasing retries, delays, or tolerances changes magnitude but not the failure pattern.
- After failed approaches, failures cluster by actor, input class, timing, or environment in a way their shared explanation does not predict.

Use `fix-root-causes` for an initial uncertain bug. Load this leaf only when existing failed approaches or contradictory observations actually expose a shared premise; a user's tentative explanation alone is not that evidence.

## Decision procedure

1. Collect existing failure evidence and the attempted changes. User reports and failing existing tests count; do not rerun an unchanged failure solely to confirm it.
2. Write the shared premise as one falsifiable sentence, such as "both workers load the same configuration." Distinguish observed facts from the assumptions linking them.
3. Identify an observation with different predicted outcomes if the premise is true or false. Prefer an existing trace, targeted source read, or narrowly authorized diagnostic over another speculative fix.
4. Examine how failures are distributed, not only their total count. Compare the shared losing condition with the premise's prediction. Ask a concrete read-only domain question if specialist knowledge is needed; main retains implementation and check ownership.
5. If contradicted, revise the causal model and change the mechanism creating the condition. If supported, retain it provisionally and investigate a different premise. Proceed with another fix only when the discriminating evidence or an explicit diagnostic limitation is recorded.

## Trade-offs

Do not turn every ordinary failure into a broad epistemic exercise. A direct error with a known cause needs a direct correction. A disproved premise does not establish a replacement explanation, and diagnostic work remains inside authorization and production boundaries.

## Examples

**Good:** Two timeout increases fail only on worker B. Inspect its effective endpoint and discover it targets a different service; correct configuration ownership.

**Problematic:** Add a third retry layer because the aggregate failure rate remains high, without checking why worker B always loses.

## Observable outcomes

The next change follows evidence distinguishing competing explanations. Symptom controls no longer accumulate around an untested premise, and the failure distribution has an explicit causal explanation.

## Verification

Main uses `skill://af-verification` to exercise the corrected condition and a contrasting unaffected condition. Compare the predicted result with the observed distribution. Mark a diagnostic or regression check NOT-RUN if unavailable; absence of a new failure report is not proof.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
