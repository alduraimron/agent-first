---
name: principle-type-system-discipline
description: Strengthen language-appropriate types when semantic primitives, invalid states, external data, or unhandled variants can escape existing contracts.
hide: true
---

# Type System Discipline

## Purpose

Move enforceable domain distinctions into the existing type system. Reject impossible states and mismatched values before execution while preserving runtime validation for facts the compiler cannot establish.

## Triggers

- A function accepts interchangeable primitives with different meanings.
- Nullable fields or flags permit contradictory states.
- External payloads are cast directly to trusted models.
- A schema and a handwritten type describe the same contract independently.

## Decision procedure

1. Identify a concrete invalid program or state that currently passes the available checks. Name the guarantee needed rather than pursuing stronger typing in the abstract.
2. Use the project's language and conventions: newtypes, enums, tagged unions, constrained constructors, or equivalent facilities. Validate semantic values at their creation boundary.
3. Derive types from the authoritative schema when supported by existing tooling. Do not create a competing shape definition or install a generator merely for this task.
4. Make variant handling exhaustive where the language supports it, and keep escape hatches narrow and justified. Finish when the targeted invalid case is rejected and valid callers remain expressible without routine casts.

## Trade-offs

Types cannot prove authorization, remote data quality, or time-dependent state. Runtime boundary checks remain necessary. A wrapper around every primitive can impose more ceremony than protection; prioritize distinctions whose confusion has real consequences. Do not migrate the language or toolchain solely to gain branded types, and preserve required external representations.

## Examples

**Good:** Give `CustomerId` and `InvoiceId` distinct types and parse received strings through their respective constructors. A settlement function accepts only the invoice identifier.

**Problematic:** Cast every incoming string to `InvoiceId`, or call both identifiers `string` and rely on parameter order. A nominal wrapper with unrestricted bypasses provides a misleading guarantee.

## Observable outcomes

Incorrect argument swaps and omitted variants fail near their introduction. Domain signatures explain accepted values; schema changes cannot silently leave parallel models behind.

## Verification

Through the existing verification procedure, check that a representative swapped identifier or missing variant is rejected by the available checker. Exercise malformed runtime input through its parser and valid input through normal callers. Record checks not executed as NOT-RUN rather than claiming type safety from declarations alone.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
