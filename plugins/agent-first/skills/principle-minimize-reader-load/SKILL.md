---
name: principle-minimize-reader-load
description: Reduce forwarding layers and hidden mutable state when code is difficult to trace or explain.
hide: true
---

# Minimize Reader Load

## Purpose

Reduce two independent costs of understanding code: the layers between a question and its answer, and the changing state a reader must remember. Short code is not enough if ownership and causality remain hidden.

## Triggers

- Finding a value's origin requires tracing several forwarding methods.
- A reader must track fields or globals across unrelated calls.
- Derived values are stored and synchronized with their source.
- An invariant is re-explained or rediscovered by each consumer.

## Decision procedure

1. Choose a concrete reader question: where a result comes from, what can change it, or why a branch is safe. Trace the current answer and note both indirections and mutable dependencies.
2. Identify layers that only forward and have no independent contract. Inline or collapse them when permitted, while retaining boundaries that own policy, resource lifetime, security, or supported substitution.
3. Shrink mutable scope: prefer a returned value over mutation and a local over shared state when behavior permits. Derive inexpensive values from their source rather than maintaining synchronized copies; retain justified caching with explicit invalidation ownership.
4. Express the invariant once at its owning boundary using the project's types, names, or checks. Keep legitimate validation at separate trust boundaries.
5. Finish when a reader can trace the chosen value and its possible changes directly, and each remaining layer or shared value has a stated responsibility.

## Trade-offs

Inlining everything creates large, tangled functions. Keep abstractions that compress a real concept or isolate volatility even with one caller. Avoid recomputing expensive derived data merely to remove a field. Readability improvements must preserve public contracts, concurrency behavior, and unrelated user changes.

## Examples

**Good:** Return the normalized configuration from the loader and use a local value, replacing a module-level variable updated by three helper calls.

**Problematic:** Hide that same mutable variable behind several one-line accessors, or inline transaction handling into every caller to reduce apparent layering.

## Observable outcomes

Value origins and mutation owners are locally visible. Fewer synchronization obligations and meaningless forwarding hops remain, without losing meaningful boundaries.

## Verification

Have main trace the same question after the change; use thirty seconds as a readability heuristic, not a correctness threshold. Through `skill://af-verification`, check returned values, error behavior, and any affected state lifetime. A shorter call chain alone does not prove equivalent behavior.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
