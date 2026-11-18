---
name: principle-redesign-from-first-principles
description: Reconsider affected design assumptions when a new requirement would otherwise become a bolted-on exception.
hide: true
---

# Redesign From First Principles

## Purpose

Integrate a requirement as a coherent part of the design rather than accumulating exceptions around assumptions it invalidates. A fresh conceptual model guides the change; it does not automatically justify rewriting the system.

## Triggers

- A new requirement contradicts an existing type, ownership rule, or boundary.
- Supporting it requires special cases across several callers.
- An existing design works only because the new case was previously impossible.

## Decision procedure

1. Read the affected contracts, implementations, immediate callers, and relevant decision records. Use bounded reads and follow references until the requirement's actual impact is mapped.
2. Separate durable constraints from historical accidents. Include explicit external compatibility, accepted architectural decisions, security boundaries, and approval requirements among the constraints.
3. Ask what the smallest design would be if the new requirement had existed from the start. Compare that target with the current model and identify which assumptions must change.
4. Select the least disruptive permitted path to that target. Propagate the adopted model through affected types, callers, tests, examples, and rationale. Respect required staged migrations rather than silently removing supported contracts.
5. Use the existing architecture workflow for consequential boundary changes. Main implements coherent checkpoints and owns verification; the principle does not authorize a wider rewrite.
6. Finish when all affected references express the adopted model and any intentionally retained compatibility has an explicit owner and purpose.

## Trade-offs

Local adaptation is appropriate when the underlying model remains valid. A redesign must earn its migration cost and risk. Preserve unrelated working code and user changes; a cleaner imaginary system is not sufficient evidence to replace them.

## Examples

**Good:** Adding partial refunds leads to explicit refund records and a derived refunded amount, replacing the assumption that a payment has one boolean refund state across internal consumers.

**Problematic:** Keep that boolean, add separate partial-refund flags to each screen, and let consumers guess which combination is authoritative.

## Observable outcomes

The new requirement uses ordinary model concepts instead of scattered exceptions. Contracts and explanations agree, and existing supported consumers have a deliberate migration path.

## Verification

Main uses `skill://af-verification` to cover both old supported cases and the new case end to end. Search affected references for the invalidated assumption, then verify representative transitions and compatibility behavior. A design diagram without exercised consumer behavior is not completion evidence.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
