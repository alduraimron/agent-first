---
name: principle-laziness-protocol
description: Minimize a refactor's necessary diff and consolidate repeated decisions before adding layers or threaded state.
---

# Laziness Protocol

## Purpose

Reduce the work required to implement, review, and maintain a correct change. Laziness means eliminating unnecessary decisions and machinery, not omitting required behavior or hiding complexity behind a short diff.

## Triggers

- A fix introduces wrappers, configuration plumbing, or a flag through several layers.
- Several consumers independently decide the same policy.
- A small request is expanding into an unrelated cleanup or abstraction project.

## Decision procedure

1. Identify the requested behavior, its consumers, and the invariants the change must preserve. Separate required work from optional tidying before selecting a smaller design.
2. Locate repeated decisions. Consolidate a genuinely shared policy at its existing owner; pass the resulting value only where necessary. Keep distinct policies separate even when their current expressions happen to match.
3. Compare a direct change with the proposed abstraction. Count affected concepts, callers, mutable values, and future edit sites, not just changed lines.
4. Choose the smallest coherent change that handles the complete request. Delete machinery made obsolete by that choice while preserving unrelated user changes and required compatibility.
5. Stop simplifying when each remaining layer or decision has a concrete responsibility and every requested consumer path is accounted for.

## Trade-offs

A tiny patch that duplicates policy or bypasses validation is not simpler. Retain useful boundaries, explicit security checks, and abstractions that own real variation. Broader redesign requires its own justification; minimizing today's diff must not preserve a known structural defect indefinitely.

## Examples

**Good:** An export feature checks the same capability in three internal helpers. The owning service decides once and passes an immutable export mode to the renderer that needs it.

**Problematic:** Add a generic policy registry and five forwarding adapters for that single decision, or remove an authorization check merely to shorten the patch.

## Observable outcomes

Policy changes have one authoritative edit site. Fewer forwarding layers and synchronized values remain, while accepted behavior, failure handling, and compatibility stay intact.

## Verification

Have main trace every affected caller and use `skill://af-verification` for relevant behavior checks. A changed policy should affect all intended consumers; unauthorized and incompatible cases must retain their required outcomes. Report unavailable checks as NOT-RUN rather than treating a smaller diff as proof.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
