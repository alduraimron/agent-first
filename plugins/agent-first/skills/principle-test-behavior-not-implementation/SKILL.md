---
name: principle-test-behavior-not-implementation
description: Choose assertions that catch broken public behavior while surviving equivalent internal refactors when writing or reviewing tests.
hide: true
---

# Test Behavior, Not Implementation

## Purpose

Make tests express contracts callers can observe: values, errors, readable state, and effects on outside systems. Avoid tests that merely reproduce the implementation or freeze private structure without protecting a requirement.

## Triggers

- A test asserts internal helper calls, private state, or incidental ordering.
- Refactoring unchanged behavior breaks many tests.
- A test passes despite a wrong value, skipped action, or duplicated effect.

## Decision procedure

1. Identify the consumer and the behavior promised by the tested interface. Include operational contracts such as ordering or resource bounds only when they are genuine requirements.
2. Select concrete inputs and derive expected results independently from the requirement, not by calling the production calculation again.
3. Apply two counterfactuals: would breaking the behavior fail this test, and would changing internals while preserving behavior leave it passing? Strengthen or replace assertions that fail either test.
4. Cover the meaningful positive and negative branches through the public interface. Have the main agent implement and execute checks under the existing testing and verification procedures. Finish when retained assertions protect identifiable contracts rather than incidental mechanisms.

## Trade-offs

A boundary fake can expose what an external service receives without asserting private helper order. White-box checks can be justified for explicit invariants unavailable through ordinary outputs, but document the contract they protect. Preserve security, compatibility, and regression coverage when replacing brittle tests; deletion alone does not establish better coverage.

## Examples

**Good:** Submit an order and assert the returned total, persisted status, and single payment request sent to the payment boundary. For a declined payment, assert the error category callers handle and the absence of a committed order.

**Problematic:** Assert that `calculateSubtotal` ran twice, or compute the expected total using that same production helper. Both tests can reward an incorrect implementation while rejecting a harmless refactor.

## Observable outcomes

Internal reorganizations require fewer test edits. Broken results and missing or doubled external effects fail targeted assertions, while test names describe user-visible obligations.

## Verification

Review a plausible behavior-breaking edit and a behavior-preserving refactor against each changed test. Where practical, the main agent checks these through existing tooling. A test that survives the wrong total or fails solely on renamed private helpers does not meet the standard; unexecuted counterfactuals remain reasoned assessments, not passing runs.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
