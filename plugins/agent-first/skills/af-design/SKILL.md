---
name: af-design
description: Design architecture and API boundaries, compare alternatives, and derive compatibility, ownership, and migration invariants for new or changed contracts.
---

# Boundary design

Use shared `rule://agent-first-shared` and af-engineering for routing, requirements, and consultation. Advisors provide analysis; main owns changes and evidence execution.

Use `af-principles` for triggered design lenses: domain modeling when concepts or invariants are unclear, boundary discipline when ownership changes, and caller migration when replacing an internal API. Explore alternatives only for an unresolved material fork; apply the shared principle handoff rather than copying leaf bodies into assignments.

## Procedure
1. Read the affected interfaces, implementations, consumers, and existing decisions. Map dependency direction, data/control flow, ownership, and sources of truth with source locations. Finish when every changed boundary has identified producers and consumers.
2. Enumerate contract invariants: valid/invalid input, output/error semantics, identity, ordering, concurrency, resource lifecycle, compatibility, and failure propagation. Mark unknowns that could change the design.
3. Compare the existing design plus smallest viable correction against material alternatives. Evaluate coupling, operational cost, failure isolation, migration complexity, and reversibility. Prefer an existing mechanism unless evidence requires a new one.
4. Specify the chosen interfaces and complete consumer cutover. For network APIs include method/path or operation, request/response shape, status/error behavior, authorization point, pagination/idempotency when relevant, and version compatibility.
5. Specify migration ordering and rollback limits; identify irreversible actions and required operator decisions. Return enforceable constraints, source-backed rationale, rejected alternatives, and checks through the shared advisory contract.

## Invariants
- One authoritative owner per state/decision; dependency direction is explicit and cyclic ownership is resolved.
- Each public contract has defined success and failure behavior, and every consumer is migrated or has an explicit compatibility requirement.
- Retries cannot duplicate non-idempotent side effects; cancellation/error paths release owned resources.
- A design recommendation does not substitute for required architect consultation under af-engineering.

## Verification recommendations
Inspect existing contract/integration tests and build/type-check scripts. Recommend concrete cases for old/new consumers, invalid inputs, partial failure, concurrency/idempotency, and migration/rollback. Use existing API schema validation tools only when present. Main records execution through af-verification; unavailable evidence remains explicit. Escalate unresolved ownership or compatibility requirements before implementation rather than guessing a contract.
