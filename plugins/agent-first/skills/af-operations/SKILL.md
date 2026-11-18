---
name: af-operations
description: Engineer deployment, configuration, observability, and recovery with explicit rollout, readiness, failure, and rollback invariants using existing runtime tooling.
---

# Operable delivery

Use shared `rule://agent-first-shared` and af-engineering for scope/approval/routing; main owns implementation and runtime evidence through af-verification. Advisors inspect and recommend, not provision infrastructure.

Use `af-principles` for idempotency when work can replay, verifiable units when rollout stages need independent stop conditions, and safe autonomy when approval blocks only one branch. Consequential integration stays blocked while genuinely independent authorized work continues.

## Procedure
1. Read runtime manifests, service entry points, deployment/configuration files, CI scripts, and runbooks. Map environments, dependencies, process ownership, persistent state, and configuration/secret sources.
2. Trace startup/readiness/liveness and graceful shutdown. Identify dependency timeouts, retry budgets, backpressure, resource limits, and failure signals. Distinguish process-alive from ready-to-serve.
3. Define rollout ordering, compatibility windows, state/migration dependencies, health gates, rollback trigger, and recovery procedure. State irreversible operations and required operator approval before any deployment action.
4. Design observability for relevant outcomes: structured/redacted logs, request correlation, error/latency/saturation metrics, actionable alert condition, and diagnostic path. Tie each signal to a concrete failure mode rather than adding telemetry indiscriminately.
5. Check configuration validation, least-privilege runtime assumptions, secret delivery/rotation, and environment parity. Cross-boundary deployment changes route through af-engineering and af-design.
6. Return actionable configuration/runbook recommendations, operational invariants, environment assumptions, risks, and safe existing-tool checks.

## Invariants
- Readiness reflects required dependencies; shutdown stops accepting work and handles in-flight work with a bounded policy.
- Retries/timeouts are bounded and preserve idempotency; overload does not create unbounded queues or retry storms.
- Rollback considers data compatibility, not only reverting the executable. Recovery ownership and triggers are explicit.
- Diagnostics redact secrets and identify failures without reporting successful service solely from process existence.

## Verification recommendations
Recommend existing configuration validators, CI checks, local service health checks, and authorized disposable-environment startup/shutdown or rollback exercises. Identify command cwd, prerequisites, health expectation, and cleanup ownership; avoid production mutations or assumed provisioning. Recommend failure-path observations for unavailable dependencies and invalid configuration. Report untested deployment assumptions explicitly; main uses af-verification for outcomes.
