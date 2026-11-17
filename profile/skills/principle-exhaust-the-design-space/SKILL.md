---
name: principle-exhaust-the-design-space
description: Compare bounded alternatives when an important novel interaction or architectural fork cannot be settled from existing evidence.
---

# Exhaust the Design Space

## Purpose

Expose meaningful alternatives before an expensive commitment. Exhaust the uncertainty that matters to the decision, not every imaginable design. Exploration is useful only when its evidence can change the choice.

## Triggers

- A consequential architectural fork has no applicable project precedent.
- Interaction quality depends on feel that a written argument cannot establish.
- Competing designs make different predictions about an important requirement.

## Decision procedure

1. Inspect relevant project patterns and accepted decisions first. State the unresolved question, its impact, and the cost of choosing incorrectly. If existing evidence settles it, reuse the established design and stop exploring.
2. Define the discriminating criteria before producing alternatives: task completion, access needs, ownership, latency, compatibility, or operational cost. Select only criteria material to this request.
3. Compare two cheap, genuinely different alternatives when evidence can resolve an important fork. A sketch, data-flow walkthrough, or small isolated prototype may suffice; choose the least expensive adequate form and a clear stopping bound.
4. Keep comparisons fair: use the same representative scenario, constraints, and failure case. Main owns prototypes and checks; domain advisors may answer concrete read-only questions. Do not create implementation-worker bakeoffs or new parallel CLI workers.
5. Choose when one alternative meets the acceptance constraints with a supported advantage, or further evidence would not justify its cost. Record the decisive evidence and remaining uncertainty through the existing context procedure; remove disposable exploration artifacts.

## Trade-offs

Routine edits and established patterns rarely benefit from prototypes. More variants can delay delivery without increasing confidence. Exploration cannot bypass required approval or authorize external services, dependency installation, or production experiments. A cheap prototype's omissions must not be mistaken for proven production properties.

## Examples

**Good:** Compare inline editing and a dialog using the same keyboard-driven correction task before committing to a novel grid interaction; use the observed focus and recovery behavior to choose.

**Problematic:** Build three full application branches for a familiar settings form, or select the prettiest happy-path prototype without testing its error path.

## Observable outcomes

The chosen design has an explicit reason tied to a material criterion. Rejected options illuminate real trade-offs, and exploration leaves no competing production implementations behind.

## Verification

Main validates discriminating observations with authorized installed tools under `skill://af-verification`, then verifies the implemented choice separately. Label unexecuted comparisons NOT-RUN and distinguish prototype findings from production evidence. The count of alternatives is not proof of design quality.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
