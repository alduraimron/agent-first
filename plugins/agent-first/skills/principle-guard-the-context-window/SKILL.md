---
name: principle-guard-the-context-window
description: Bound source reads and preserve reusable evidence when large outputs, repeated exploration, or advisory fan-out threaten useful context.
hide: true
---

# Guard the Context Window

## Purpose

Keep decision-relevant evidence available without flooding the working context. Preserve constraints, provenance, and unresolved questions in compact reusable form instead of repeatedly loading bulk source material.

## Triggers

- Searches return many unrelated files or oversized outputs.
- The same long source is repeatedly reopened to recover one fact.
- Advisory requests are broad enough to produce another context dump.
- A transition between phases risks losing decisions or evidence.

## Decision procedure

1. Name the concrete question and the evidence needed to answer it. Scope searches by subsystem, symbol, or error, then read bounded relevant sections with enough surrounding context to preserve meaning.
2. Summarize established facts once, including source locations, constraints, and uncertainty. Reuse that summary and revisit sources only for an unresolved question or changed evidence; do not substitute a summary for the artifact needed to verify a claim.
3. If existing routing permits advisory help, ask an installed read-only domain a concrete question with a bounded source set and desired evidence. Keep main-agent implementation and check execution ownership; retain configured concurrency and depth limits.
4. Before changing phases, preserve decisions and exact evidence pointers through the existing repository-context or continuity mechanism. Finish when the next decision can be made from a compact, traceable working set.

## Trade-offs

Compression can erase exceptions or make hypotheses look settled. Keep decisive constraints and contradictory evidence explicit. Inline investigation is often cheaper than delegation for a small known file. This principle does not authorize generic implementation delegation, nested workers, parallel CLI workers, new agents, or increased concurrency.

## Examples

**Good:** Search the authentication adapter for token parsing, read the relevant function, then retain the invariant and location. Ask security advice specifically whether that boundary validates issuer and audience.

**Problematic:** Load every authentication file, paste all outputs into several workers, and ask each to implement a fix. A summary saying only "auth looks safe" loses both evidence and uncertainty.

## Observable outcomes

Reads stay tied to questions, findings carry recoverable locations, and advisory responses resolve bounded uncertainties rather than creating duplicate implementation streams.

## Verification

For each active decision, identify its evidence pointer and any unresolved assumption without rereading the entire subsystem. Check that summaries distinguish observations from inference and advisory asks remain read-only. Missing decisive constraints or repeated bulk reads without a new question falsify effective context protection.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
