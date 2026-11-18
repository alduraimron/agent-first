---
name: principle-model-the-domain
description: Model stateful logic when synchronized flags, repeated shape assumptions, or growing conditionals obscure valid states.
hide: true
---

# Model the Domain

## Purpose

Represent the domain's invariants in data rather than rediscovering them in every branch. A useful model removes invalid combinations and makes transitions, ownership, and access patterns explicit.

## Triggers

- Two booleans must change together or exclude one another.
- Adding a variant requires editing conditionals across several files.
- Callers repeatedly reconstruct the same relationship, ordering, or lookup.

## Decision procedure

1. Name the entities, valid states, transitions, and invariants demonstrated by current requirements. Distinguish known requirements from speculative future variants.
2. Locate the repeated assumptions and identify which representation creates them. Consider a tagged union, state machine, normalized collection, registry, queue, or index only where its semantics fit.
3. Compare the simplest candidate with the current representation. Prefer a model that deletes synchronization work or impossible combinations rather than merely hiding conditionals behind methods.
4. Have the main agent implement the chosen representation through the existing workflow, updating affected callers and preserving required behavior. Finish when every identified invariant has one owner and affected callers no longer recreate the old assumptions.

## Trade-offs

A local two-case branch may be clearer than a framework or registry. Models carry migration and conceptual costs; avoid predicting domain states without evidence. Preserve required compatibility and legitimate boundary validation rather than treating a new representation as permission to remove them.

## Examples

**Good:** Represent a payment as `Pending`, `Settled(receipt)`, or `Failed(reason)`. Only settled payments contain a receipt, and transition logic rejects settlement after cancellation.

**Problematic:** Add `isPaid`, `hasFailed`, and nullable `receipt` fields, then teach each screen which contradictory combinations to ignore. Renaming these fields inside a class does not repair the model.

## Observable outcomes

Invalid combinations become unconstructable or fail at one transition boundary. New variants have a discoverable integration point, and callers read domain facts instead of reconciling flags.

## Verification

Using existing verification procedures, exercise each allowed transition and at least one forbidden transition. Check that receipt-dependent behavior cannot execute for a pending payment. Search affected callers for surviving duplicated state reconstruction; unexplained copies falsify the claimed simplification.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
