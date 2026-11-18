---
name: principle-foundational-thinking
description: Choose core data shapes, access patterns, and ownership before layering logic onto a feature or shared state.
hide: true
---

# Foundational Thinking

## Purpose

Make downstream logic straightforward by choosing representations and ownership that express the actual problem. Share a stable structure where it captures an invariant, rather than deduplicating every similar line.

## Triggers

- A feature needs new core types, indexes, or relationships.
- Callers repeatedly reshape the same data or synchronize parallel collections.
- Concurrent actors may read and modify the same state.
- Implementation phases depend on common scaffolding that does not yet exist.

## Decision procedure

1. Enumerate the important reads, writes, identity rules, ordering requirements, and expected scale. Complete this inventory when every required consumer operation has a representation to use.
2. Choose language-appropriate types and structures that make dominant accesses direct and invalid combinations difficult to construct. Reuse project conventions rather than introducing a toolchain solely for stronger types.
3. Assign each mutable value an owner. Ask what another actor can observe during a modification. Where interference changes correctness, prefer isolated state or an existing ownership boundary before adding shared coordination.
4. Order only the foundations actually needed by later behavior: shared contracts, a missing test seam, or a necessary index. Avoid building a speculative platform. Existing workflows still govern implementation and approval.
5. Finish when the representation supports all required operations, ownership is explicit, and the next behavior can be implemented without compensating data translations.

## Trade-offs

An uncommon access may remain less efficient to keep the dominant path simple. Do not replace established public formats without a permitted migration, or delay a narrow fix to redesign unrelated infrastructure. Foundational work serves delivery, not an independent scaffolding milestone.

## Examples

**Good:** Store jobs by stable identifier with an explicit ordered queue of identifiers; the scheduler owns transitions and consumers receive snapshots.

**Problematic:** Maintain three independently mutated job arrays and repair inconsistencies with callbacks, or build a general event platform for one queue.

## Observable outcomes

Consumer logic needs fewer conversions and repair branches. Identity, ordering, and mutation ownership are visible in the data model, including concurrent access boundaries.

## Verification

Main should check representative reads, updates, deletion, and ordering through `skill://af-verification`. Exercise the relevant concurrent interleaving when state is shared. Verify that every required operation preserves the model's invariants; source inspection alone does not establish race freedom.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
