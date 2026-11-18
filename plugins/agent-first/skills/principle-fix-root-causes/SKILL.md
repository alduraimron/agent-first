---
name: principle-fix-root-causes
description: Trace failures to the first violated invariant when guards, retries, or discarded state would only hide the symptom.
hide: true
---

# Fix Root Causes

## Purpose

Repair the decision that first made the system wrong, not merely the location where the error became visible. A legitimate exceptional state needs handling; an impossible state needs its producer corrected.

## Triggers

- A proposed fix swallows an error, clamps a value, retries, or adds a null guard.
- The same failure appears through several call paths.
- A downstream crash reveals state that should never have existed.

## Decision procedure

1. Start from the user's observation or existing failure evidence. Identify the expected invariant and earliest known divergence without rerunning unchanged failures just for confirmation.
2. Trace actual values and ownership backward through the relevant path. When evidence is missing, use focused, authorized observation rather than guessing from the final stack frame.
3. Decide whether the triggering state is legitimate. Handle legitimate absence or failure at its responsible boundary; otherwise fix the operation that created invalid state.
4. Search the bounded affected area for the same causal pattern. Have the main agent repair that pattern and add proportionate regression coverage through the existing workflow. Finish when the causal path explains the symptom and the repair covers its affected variants.

## Trade-offs

Do not turn causal investigation into an unrelated subsystem rewrite. Security guards and boundary validation remain valid even when upstream code improves. An urgent, explicitly approved containment may coexist with a root repair, but label its limited effect rather than presenting suppression as resolution. Add persistent diagnostics only when they cheaply expose a demonstrated blind spot.

## Examples

**Good:** A duplicated charge comes from acknowledging a job before recording its idempotency key. Repair the transaction ordering and cover redelivery after interruption.

**Problematic:** Catch the duplicate-charge exception and return success, leaving the second debit intact. Adding retries to the same path can amplify the underlying fault.

## Observable outcomes

The original failure path is eliminated for a stated reason, equivalent callers receive the same repair, and legitimate exceptional states still produce defined outcomes rather than disappearing silently.

## Verification

The main agent uses the existing reproduction evidence to select a post-change regression check and a neighboring legitimate-state case. Confirm the externally visible result, not just absence of the exception. A surviving wrong debit, hidden error, or unexplained causal step falsifies the root-cause claim.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
