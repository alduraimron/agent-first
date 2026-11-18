---
name: principle-make-operations-idempotent
description: Design state-changing operations to converge safely when retries, restarts, or partial prior runs are possible.
hide: true
---

# Make Operations Idempotent

## Purpose

Make repeated execution reach the intended state without duplicating effects or depending on a previous run's intentions. Recovery should derive from observable durable state, including evidence left by interrupted work.

## Triggers

- A command may be rerun after an uncertain result.
- Jobs, lifecycle hooks, migrations, or consumers can restart midway.
- Temporary files, locks, claims, or half-written records survive failure.

## Decision procedure

1. Define the desired end state and the effect that must occur at most once. Identify durable observations that distinguish absent, partial, complete, and stale work.
2. Examine each interruption point, including a crash after an external effect but before local acknowledgment. Choose existing transactions, uniqueness constraints, idempotency keys, reconciliation, or atomic publication appropriate to that boundary.
3. Compare actual state with the goal and apply only the missing transition. Use temporary-file publication with an atomic rename when filesystem semantics support it; establish ownership before removing stale artifacts.
4. Have the main agent implement recovery through the existing workflow. Finish when repeated execution and every relevant partial state have defined, safe outcomes.

## Trade-offs

Idempotency is not permission to retry indefinitely or initiate an unauthorized action. Some external effects cannot be made exactly-once without receiver cooperation; state that limitation and use the supported reconciliation contract. Preserve required event history rather than collapsing meaningful repeated operations into one. Avoid durable orchestration machinery for an operation already covered by an existing transaction.

## Examples

**Good:** A payment consumer stores a unique event key with the ledger mutation in one transaction. A redelivery reads the existing result instead of issuing another debit.

**Problematic:** Debit first and then write `processed=true`; a crash between those writes permits a second debit. An in-memory set does not fix restart recovery.

## Observable outcomes

Reruns produce the same intended state, stale claims have evidence-based recovery, and duplicate delivery does not multiply effects. Logs distinguish completion from reconciliation rather than merely counting attempts.

## Verification

Using isolated fixtures and existing verification tools, repeat the operation and simulate interruption around durable transitions. Compare resulting records and externally visible effects, not just exit codes. A second debit, unrecoverable stale claim, or corrupted published file falsifies the idempotency claim.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
