---
name: principle-separate-before-serializing-shared-state
description: Separate independent writes before adding synchronization when concurrent actors share a file, key, branch, or state object.
hide: true
---

# Separate Before Serializing Shared State

## Purpose

Remove unnecessary shared mutation before managing its races. Independent facts should have independent write ownership; genuinely shared invariants need structural concurrency control rather than instructions to be careful.

## Triggers

- Concurrent activities update different fields in one file or record.
- Lost updates motivate a lock around otherwise independent outputs.
- A shared branch, temporary directory, cache key, or status object creates collisions.

## Decision procedure

1. Identify writers, write targets, readers, and the invariant that supposedly requires sharing. Distinguish independent reports from one ordered state transition.
2. Where facts are independent, assign separate files, keys, or state directories and aggregate at the read boundary. Define identity, lifetime, and cleanup ownership so separation does not create ambiguity.
3. Where one shared target is essential, use existing transactions, compare-and-swap, a single writer, locks, or sequential phases. Include crash recovery and readers in the consistency design.
4. Have the main agent implement the smallest suitable structure within existing concurrency and isolation limits. Finish when each mutable target has explicit ownership or an enforced synchronization rule.

## Trade-offs

Separation can complicate aggregation and retention, and cannot replace an atomic cross-record invariant. A global balance or uniqueness constraint may genuinely require serialization. Conversely, one lock around every operation can erase useful concurrency. This principle does not increase allowed concurrency, authorize implementation workers, or replace native Tern and optional OVNFS isolation procedures.

## Examples

**Good:** Independent analysis tasks publish uniquely named result records; the main agent reads and combines them. A ledger debit still uses the database transaction that preserves its balance invariant.

**Problematic:** Two activities read the same `status.json`, edit their own fields, and overwrite the whole file. Telling them to avoid simultaneous writes leaves the lost-update race intact.

## Observable outcomes

Independent writers stop overwriting one another. Shared mutations have a discoverable enforcement mechanism, and readers see either a defined snapshot or an explicitly partial aggregate.

## Verification

Using the existing verification procedure, exercise overlapping writes with distinct payloads and inspect the resulting state. Both independent facts must survive; a truly shared invariant must hold across contention and interruption. An instruction-only ordering rule or unexplained last-writer-wins loss disproves the design.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
