---
name: principle-explain-the-number
description: Establish decision relevance, measurement validity, and limiting factors before trusting performance or evaluation numbers.
---

# Explain the Number

## Purpose

Prevent a precise-looking measurement from driving a decision it cannot support. Explain what work was measured, how variable the result is, and which observed constraint limits it.

## Triggers

- A speedup, latency, throughput, regression, or evaluation score will influence a decision.
- A surprising result could reflect caching, skipped work, errors, or unequal conditions.
- A reported average omits trials, spread, workload, or environment.

## Decision procedure

1. State the decision and the effect size that would change it before requesting a run. Define the workload, success criteria, comparison conditions, and a proportionate trial plan.
2. Use existing performance or verification procedures and installed tools. The main agent executes authorized measurements; advisory domains can identify hypotheses and evidence needs without launching implementation workers.
3. Rule out alternative explanations with observations: confirm the intended path ran, outputs were correct, work volumes matched, and cache or error behavior did not bias one side.
4. Ask why the result is not twice as good. Use profiles, counters, or equivalent runtime evidence to identify the limiter; label an unmeasured explanation as a hypothesis.
5. Keep trial count, spread, conditions, and limiter beside the conclusion. Finish when evidence supports the decision, or report that noise or missing evidence prevents it.

## Trade-offs

Measurement effort should track decision impact. Stop claiming a meaningful difference when run-to-run variation overwhelms it; redesign the comparison rather than endlessly repeating it. A microbenchmark cannot establish end-to-end benefit by itself. Do not install tools or use production load without authorization, and do not treat one evaluation scenario as universal model quality.

## Examples

**Good:** Compare two parsers on identical validated inputs across repeated trials, report the distribution, and use a profile to show allocation dominates the slower path.

**Problematic:** Claim a tenfold speedup after one run where the new path returned cached results and the old path parsed every file. A low error rate calculated over silently skipped requests is equally misleading.

## Observable outcomes

Numbers remain attached to their conditions and uncertainty. Optimization targets the observed bottleneck, and inconclusive measurements do not become confident rankings.

## Verification

Check whether equal completed work, correct outputs, trial count, spread, and runtime limiter evidence accompany the claim. A missing workload check or an effect inside the observed noise falsifies a decisive comparison. Measurements not executed must be marked NOT-RUN.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
