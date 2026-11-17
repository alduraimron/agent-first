---
name: principle-encode-lessons-in-structure
description: Convert evidenced recurring corrections into narrow structural enforcement before adding more judgment-only instructions.
---

# Encode Lessons in Structure

## Purpose

Make a demonstrated lesson hard to forget by placing it in the system that owns the invariant. Repeated prose reminders are weaker than code, types, tests, or existing enforcement that rejects the actual mistake.

## Triggers

- The correction ledger records the same failure across independent occurrences.
- An instruction must repeatedly restate an objectively checkable invariant.
- A correction depends on memory even though the responsible boundary can enforce it.

## Decision procedure

1. Read the relevant ledger evidence and identify the recurring failure, affected scope, and causal pattern. Distinguish repeated evidence from several descriptions of one incident.
2. Locate the narrowest authoritative owner. Prefer a code invariant or type constraint, then targeted behavioral tests, installed lint rules, or existing architecture enforcement as appropriate to the failure.
3. Compare prevention strength with false positives and maintenance cost. Reuse current tools; add a script or framework only when recurrence and reproducibility savings justify it within authorized scope.
4. Have the main agent implement the structural correction through the existing workflow and update ledger evidence using its established mechanism. Retain judgment-only guidance only for the remainder that cannot be encoded. Finish when the demonstrated failure is prevented or detected at its owner without broad unrelated policy.

## Trade-offs

A single failure can justify a local bug fix or regression test without justifying a global rule. Structural enforcement must preserve legitimate exceptions and cannot automatically redefine user intent. Do not install tools, publish changes, or edit global instructions merely to make a lesson permanent. When judgment is irreducible, narrowly scoped guidance with a concrete counterexample is more honest than a brittle heuristic.

## Examples

**Good:** Repeated ledger entries show customer and invoice identifiers being swapped. Introduce distinct existing-language types at the API boundary and a focused regression test instead of another reminder to check parameter order.

**Problematic:** After one timeout, mandate retries for every network operation. The blanket policy can duplicate non-idempotent effects and encodes an unsupported generalization rather than the actual cause.

## Observable outcomes

The recurring mistake fails earlier through a named mechanism. Guidance shrinks where enforcement becomes authoritative, and unrelated workflows retain their existing choices.

## Verification

Using existing verification, the main agent demonstrates that the known failing case is rejected or detected and a legitimate neighboring case remains accepted. Check ledger scope against enforcement scope. A rule that misses the recurrence, rejects valid exceptions, or relies only on a stronger warning falsifies the claimed structural correction.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
