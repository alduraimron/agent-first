# Performance optimization

## Entry and inputs
Use for measuring or improving latency, throughput, memory, CPU, I/O, or scalability. Require the target metric/budget, representative workload, environment, correctness constraints, available profiling tools, and measurement-only versus implementation authorization.

## Steps and decision points
1. Load `skill://af-performance`. Establish comparable baseline evidence or identify precisely why measurement is unavailable.
2. Locate the measured bottleneck and distinguish capacity, algorithmic, allocation, I/O, contention, and environmental causes. Rank hypotheses by measured contribution.
3. Define a minimal experiment and expected metric change with correctness guardrails. Measurement-only requests stop at findings and recommendations.
4. For authorized optimization, main changes one causal mechanism at a time without hiding work through reduced correctness. If the proposal changes boundaries or contracts, route architecture-impacting before implementation.
5. Compare before/after under equivalent conditions and account for variance, resource tradeoffs, and regressions outside the target metric.

## Consultation
Use af-performance for a material profiling or optimization question; af-database or af-devops when the measured cause belongs there. Follow router protocol; no blanket advisor fan-out.

## Verification
Use `skill://af-verification` for the existing benchmark/profiler and correctness checks. Record workload, environment, revisions, samples, and limitations. An unmeasured optimization is not a demonstrated speedup.

## Exit
The requested analysis or authorized change is complete, correctness has an evidence status, and improvement is quantified or explicitly unverified.

## Failure and escalation
If tooling/workload access is missing, report the exact measurement gap and proposed existing-tool check. Do not install benchmarks, invent timings, or extrapolate production capacity from an unrepresentative sample.
