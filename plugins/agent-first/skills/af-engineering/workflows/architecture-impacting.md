# Architecture-impacting change

## Entry and inputs
Use when authorized work changes ownership, public contracts, persistence/schema design, trust boundaries, dependency direction, or cross-cutting design. Require affected boundaries/consumers, acceptance criteria, compatibility constraints, and the actual design question.

## Steps and decision points
1. Load `skill://af-design`; map current dependencies, data/control flow, and invariants with source locations. Identify the simplest viable option and material alternatives.
2. Consult `af-architect` through the router's native task protocol before affected implementation. Supply the map, evidence, options, constraints, and question. Wait for actual returned advice.
3. Evaluate advice against repository evidence. Record chosen design, rejected alternative, tradeoffs, migration/rollback, and enforceable constraints through `skill://af-context` when durable decisions matter.
4. Resolve required approvals under `rule://agent-first-shared`. Main implements the complete cutover, migrating consumers and removing superseded interfaces rather than adding compatibility shims without a requirement.
5. Trace every adopted invariant to implementation and a verification recommendation.

## Consultation
Architect consultation is mandatory. Consult other domain advisors only for distinct material uncertainties. Use a bundled reviewer for an independently reviewable concrete risk under the router protocol.

## Verification
Use `skill://af-verification`; cover changed contracts, representative consumers, failure behavior, migration and rollback assumptions with existing project tooling.

## Exit
The chosen design, full consumer path, constraints, and evidence statuses are accounted for. Advice alone is not implementation or verification.

## Failure and escalation
If architect consultation is denied/unavailable, report the exact blocker and leave affected architectural implementation pending. Reopen the decision when evidence invalidates an assumption. Do not bypass approval or conceal incomplete migration behind fallback behavior.
