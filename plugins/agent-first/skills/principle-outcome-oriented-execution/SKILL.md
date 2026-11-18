---
name: principle-outcome-oriented-execution
description: Converge planned rewrites and migrations on a verifiable target without unnecessary transitional compatibility machinery.
hide: true
---

# Outcome-Oriented Execution

## Purpose

Optimize migration decisions for the intended supported end state instead of making every private editing step resemble a releasable product. Avoid temporary bridges that survive indefinitely without serving an actual compatibility requirement.

## Triggers

- A planned rewrite has explicit target contracts and phase boundaries.
- Temporary adapters are proposed only to keep unfinished local edits passing.
- Migration effort is preserving intermediate structure rather than completing the consumer cutover.

## Decision procedure

1. State the target behavior, surviving contracts, supported consumers, and completion checks. Include required external compatibility, rollback, and deployment constraints before choosing a migration path.
2. Identify coherent checkpoints where the target can be meaningfully verified. Follow the existing migration workflow; main owns changes and verification.
3. Prefer a coordinated internal cutover when authorized. Use staged adapters only where required consumers, release sequencing, or accepted decisions need them, and give their removal a concrete condition.
4. Permit temporary breakage only inside explicitly authorized, isolated, reversible migration boundaries. Keep shared branches, team environments, and production usable; lack of an explicit boundary means preserving their required stability.
5. At each declared checkpoint, obtain the relevant evidence. Finish when all target consumer paths work, required compatibility remains, and obsolete transitional code is removed. Do not stop at a structurally complete but unverified rewrite.

## Trade-offs

End-state focus is not permission to skip checks, abandon rollback, or ignore existing users. A staged migration may be the simplest safe delivery path. Do not invent a migration for a local change or commit, publish, or create a pull request automatically.

## Examples

**Good:** In an authorized isolated workspace, replace an internal response type and all its callers before checking the coherent result; no adapter is shipped solely for the half-edited state.

**Problematic:** Break a shared service until every client migrates, or delete a promised API version because the final architecture has only one version.

## Observable outcomes

The delivered system has a coherent target model. Any remaining bridge corresponds to a real supported transition with a defined exit condition, not forgotten editing convenience.

## Verification

Main uses `skill://af-verification` for the selected static and runtime checks covering the completed migration, affected callers, and required compatibility. Verify at meaningful behavior checkpoints rather than after every file. Record unavailable checks as NOT-RUN; intermediate success does not prove the final cutover.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
