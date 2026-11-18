---
name: principle-boundary-discipline
description: Concentrate parsing and error translation at trust boundaries when validation or framework concerns spread through business logic.
hide: true
---

# Boundary Discipline

## Purpose

Turn untrusted input into a trustworthy domain representation at an explicit boundary. Keep business rules independent of transport details so callers can reason about valid inputs without repeating defensive checks everywhere.

## Triggers

- CLI, configuration, persistence, or network data enters application logic.
- Internal functions repeatedly check the same shape or nullable field.
- Framework request objects or transport errors leak into reusable business APIs.

## Decision procedure

1. Identify each trust boundary and the guarantees it actually establishes. A type assertion or database read alone does not validate external data.
2. Parse and narrow incoming values there, returning a domain value or an explicit error. Distinguish validation from projection: preserve the consumer's accepted payload contract, including nested data when promised, rather than silently dropping fields to simplify copying. Translate outgoing errors where the caller's protocol requires it.
3. Separate deterministic business decisions from transport, framework, and effectful orchestration where doing so removes coupling. Keep the shell thin without creating layers for trivial pass-through code.
4. Remove repeated internal shape checks only after proving the invariant holds on every entry path. Finish when raw inputs have explicit conversion points and domain functions expose domain contracts.

## Trade-offs

Trust is specific to an invariant, not blanket permission. Authorization, freshness, concurrency, and database constraints may require checks at the moment of use. Preserve security and integrity defenses across genuine boundaries; do not delete them because an earlier parser accepted the shape. Dynamically typed code may need explicit internal contracts where static guarantees are absent.

## Examples

**Good:** Parse an HTTP order body into a validated order command, call a transport-independent pricing function, then map its domain error to an HTTP response. Check authorization against the current resource before mutation.

**Problematic:** Pass the request object into pricing and repeatedly test whether `quantity` is a string. Equally problematic: remove an ownership check because the request already passed JSON validation.

## Observable outcomes

Malformed input fails predictably at entry. Domain tests need no HTTP framework, and internal signatures stop accepting raw payloads or transport responses.

## Verification

The main agent uses existing verification to submit malformed and valid input through each affected entry point, then exercises the domain function independently. Verify unauthorized well-formed input still fails. A bypass path accepting raw data or a removed security check disproves boundary completeness.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
