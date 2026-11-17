---
name: principle-migrate-callers-then-delete-legacy-apis
description: Cut over internal API callers together when obsolete interfaces or compatibility layers would otherwise persist.
---

# Migrate Callers Then Delete Legacy APIs

## Purpose

Finish an internal API change rather than leaving two conventions indefinitely. A coordinated cutover removes obsolete entry points, tests, aliases, and adapters once every affected caller uses the replacement contract.

## Triggers

- A replacement API is being introduced beside an older internal API.
- A refactor retains forwarding wrappers without a required consumer.
- Callers and tests disagree about which contract is authoritative.

## Decision procedure

1. Establish the compatibility boundary before deleting anything. Identify internal callers, generated consumers, plugins, documentation examples, and any external commitments. Explicit compatibility requirements, accepted decisions, staged migrations, and approvals take precedence.
2. For a permitted coordinated cutover, define the replacement behavior and inventory every affected caller, including indirect references and tests.
3. Have the main agent migrate those callers and their contract assertions in coherent units through the existing workflow. Remove tests only when they protect obsolete implementation details, not still-required behavior.
4. Delete the superseded API, aliases, exports, adapters, and stale guidance once no supported caller needs them. Finish when one authoritative internal contract remains, or when a required staged boundary is explicitly accounted for.

## Trade-offs

Published interfaces, independently deployed clients, persisted formats, and accepted rollout plans may need compatibility. In those cases retain only the mechanism required by that contract and its defined retirement conditions. This principle does not authorize a breaking change outside scope or removal of unrelated user work.

## Examples

**Good:** Replace an internal `loadUser(id, true)` API with `loadActiveUser(id)`, update every internal caller and behavioral test, then delete the boolean API and its re-export.

**Problematic:** Add `loadActiveUser` but keep the old API as an undocumented wrapper forever. Also problematic: delete a public endpoint used by independently deployed clients merely because repository search finds no calls.

## Observable outcomes

New code has one obvious entry point. Search no longer reveals supported internal callers of the removed interface, and tests describe the replacement contract rather than preserving dead signatures.

## Verification

The main agent checks the caller inventory against remaining references and uses existing verification for migrated behavior. Exercise any explicitly retained compatibility boundary. A missed supported caller, unresolved old export, or broken required client falsifies completion even if the replacement API itself passes tests.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
