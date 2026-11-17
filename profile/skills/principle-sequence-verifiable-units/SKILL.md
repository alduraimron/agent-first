---
name: principle-sequence-verifiable-units
description: Order multi-step changes around coherent behavioral checkpoints instead of accumulating an uncheckable migration or sweep.
---

# Sequence Verifiable Units

## Purpose

Make a change sequence explain and validate itself. Each unit should establish a meaningful behavior or invariant, limiting how much uncertain work can accumulate before the next useful observation.

## Triggers

- A migration spans several interfaces or data representations.
- Repetitive edits could propagate one mistaken assumption widely.
- A large change has no intermediate state that a reviewer can understand or check.

## Decision procedure

1. Identify the end behavior, dependencies, and existing evidence. Use reported failures as the baseline rather than rerunning unchanged failures merely to establish one.
2. Partition work by coherent behavior or invariant, not by arbitrary file counts. Define a checkpoint and its falsifying observation for each unit; combine tightly coupled edits into one unit when separation would create a meaningless broken state.
3. Order units so earlier evidence supports later changes: establish the contract, perform the compatible cutover, then remove obsolete structure as permitted. The main agent chooses and runs authorized checks through the existing verification workflow; advisory work stays read-only.
4. Stop expansion when a checkpoint reveals a wrong assumption, resolve it, then proceed. Finish when every requested behavior is covered and the final integrated state has appropriate evidence.

## Trade-offs

Checkpoints are not a demand for tests after every line or file. Coalesce checks when they answer the same question, and respect assignments that defer execution to the main agent. Temporary breakage is acceptable only inside explicitly authorized isolated, reversible migration boundaries, never as an assumption about shared or production state. This principle does not authorize commits, publication, or pull requests.

## Examples

**Good:** Migrate an internal serializer and all of its consumers as one coherent unit, check round-trip behavior, then delete the obsolete representation after the cutover is established.

**Problematic:** Change producers in one shared-state delivery and defer all consumers to another, leaving the team with unreadable data. Running a formatter after every file does not make that sequence verifiable.

## Observable outcomes

Failures point to a bounded behavioral change. Reviewers can identify the purpose and evidence of each checkpoint, and migration boundaries do not leak unsupported intermediate states.

## Verification

Compare checkpoints with actual dependencies and recorded observations. Each must detect a plausible error in its unit; final verification must cover interactions. A checkpoint consisting only of successful editing, or a supposedly independent unit requiring an unavailable later change, falsifies the partition.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
