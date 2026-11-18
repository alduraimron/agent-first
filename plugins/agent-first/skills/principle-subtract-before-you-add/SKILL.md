---
name: principle-subtract-before-you-add
description: Remove proven obsolete code and redundant structure before building an addition or refactor on top of it.
hide: true
---

# Subtract Before You Add

## Purpose

Reduce the surface a change must navigate before introducing new behavior. Remove dead branches, superseded representations, and empty indirection so the addition rests on the real system rather than its accumulated debris.

## Triggers

- A feature would extend code already made obsolete by an accepted change.
- Several validators enforce the same invariant within one trusted boundary.
- A rewrite leaves unused exports, stub references, or duplicate implementations.
- An abstraction exists only to preserve an abandoned path.

## Decision procedure

1. Identify candidate removals inside the assigned scope. Establish why each is obsolete using callers, ownership, tests, configuration, and required external contracts; an absent textual reference alone may miss dynamic entry points.
2. Separate redundant enforcement from legitimate boundary checks. Preserve validation at trust boundaries, authorization, data integrity, and intentionally supported compatibility paths.
3. Remove proven dead structure and its affected references as a coherent change. Preserve unrelated user edits. Required staged migrations and accepted decisions override a preference for immediate deletion.
4. Re-evaluate the addition against the simpler base. Reuse the surviving model instead of recreating the deleted complexity under a new name.
5. Stop when obsolete paths within scope have no remaining consumers and every remaining addition serves a required behavior. Use existing workflows for implementation sequencing rather than widening the cleanup.

## Trade-offs

Deletion is not inherently safer than addition. Runtime discovery, supported integrations, and rollback requirements can make apparently unused code necessary. Where evidence is insufficient, retain the path and state the uncertainty rather than deleting speculatively or leaving a misleading empty stub.

## Examples

**Good:** After an authorized internal parser cutover, remove the old parser, its registration, obsolete fixtures, and references before adding another format to the surviving parser.

**Problematic:** Delete request validation because an internal helper also validates, or remove an externally supported parser merely because no repository caller remains.

## Observable outcomes

There is one live implementation for the migrated responsibility, fewer branches to maintain, and no empty references advertising deleted behavior. Security and supported compatibility remain intact.

## Verification

Main should search known registration and call paths, then use `skill://af-verification` to exercise surviving behavior, required failures, and supported integrations. Confirm the removed path is unreachable under supported configuration. Reduced line count does not establish preserved behavior; unavailable checks remain NOT-RUN.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
