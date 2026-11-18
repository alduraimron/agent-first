---
name: af-performance
description: Measure bottlenecks and compare optimization experiments across latency, throughput, allocations, memory, I/O, and contention with correctness guardrails.
---

# Measurement-first optimization

Use shared `rule://agent-first-shared`, af-engineering planning/routing, and af-verification evidence execution. Main runs measurements and implements; advisors analyze available evidence.

Use `af-principles` to explain measured numbers and reason from the actual limiting mechanism. Consider ownership separation only for evidenced contention and leverage only for recurring measurement work. Predictions and source complexity remain distinct from observed performance.

## Procedure
1. Define metric, budget, workload distribution, concurrency, data size, environment, and correctness constraints. Read existing benchmarks, profiling hooks, hot paths, and prior measurements with their revision/conditions.
2. Specify a comparable baseline: warmup/cold-start distinction, sample count/duration, percentiles or distribution, noise sources, and resource measurements. Use existing installed tooling; identify missing measurement prerequisites explicitly.
3. Attribute cost using evidence: CPU work, allocations/copies, GC, I/O round trips, query plans, lock contention, queueing, or external latency. Distinguish wall time from CPU and steady state from startup.
4. Rank candidate changes by measured contribution and expected gain. Prefer removing redundant work or a better algorithm over speculative caching/concurrency. Define one causal experiment and its predicted outcome.
5. Evaluate tradeoffs: peak memory, tail latency, throughput, fairness, cache invalidation, cancellation, and overload behavior. Architectural scaling changes route through af-engineering before implementation.
6. Recommend equivalent before/after measurement plus correctness checks, including raw sample retention and uncertainty. Report the measured gain only when observations support it.

## Invariants
- Compared runs use equivalent workload, environment, settings, and correctness semantics; material differences are disclosed.
- Optimization preserves outputs, ordering, error behavior, and ownership/lifetime requirements.
- Caches have explicit key, capacity, invalidation, and freshness semantics; parallelism has bounded concurrency and backpressure.
- Allocation/copy reductions respect lifetime and aliasing safety; resource cost is not merely shifted off the measured path.

## Verification recommendations
Recommend existing benchmark/profiler commands and focused regression tests with representative small/large and contention/overload cases. Compare distributions and resource use, not a single favorable timing. For unavailable production workloads, state representativeness limits and avoid capacity claims. Escalate measurement access gaps or contradictory samples before recommending a broad redesign.
