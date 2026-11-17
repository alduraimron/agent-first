---
name: principle-experience-first
description: Resolve feature and interaction trade-offs around the consumer's core workflow rather than implementation convenience.
---

# Experience First

## Purpose

Make the consumer's task successful, understandable, and recoverable. Consumers include end users, API callers, operators, and the next maintainer. Foundations determine implementation sequence; the experience determines the target they must serve.

## Triggers

- Feature count competes with the quality of the central workflow.
- An implementation shortcut exposes internal complexity to consumers.
- A UI interaction, API contract, or error path is technically functional but difficult to use.
- Controls or options exist without a demonstrated consumer need.

## Decision procedure

1. Name the consumer and central task. Describe success, waiting, failure, and recovery from that consumer's perspective, including relevant accessibility and operational needs.
2. Evaluate proposed controls and features against that task. Prefer a focused, coherent experience over optional breadth, while preserving accepted scope. Propose scope reductions explicitly rather than silently dropping requested behavior.
3. Where an important interaction remains uncertain, use the cheapest authorized sketch or prototype that can answer it. Reuse project tools and keep exploratory work separate from production behavior.
4. Choose defaults, feedback, terminology, and error handling that reduce consumer effort. For interfaces include meaningful loading and failure states; for libraries include predictable contracts and actionable errors. Respect security and compatibility constraints.
5. Complete the design decision when the entire required core loop, including failure and recovery, has an observable acceptance criterion. Existing workflows govern implementation and domain consultation.

## Trade-offs

Polish cannot override correctness, accessibility, safety, or an explicit requirement. Consumer preferences can conflict: a convenient caller API may burden operators or maintainers. Make that cost visible rather than treating visual novelty or fewer controls as universal improvement.

## Examples

**Good:** A file importer preserves the selected file after a parsing error, points to the offending row, and offers correction without restarting the task.

**Problematic:** Add five import modes while failures show only "invalid input," or hide required advanced controls to make a screenshot look cleaner.

## Observable outcomes

The core task requires fewer unexplained decisions. Waiting, errors, and recovery are legible, and required consumers can complete the workflow without knowing internal implementation details.

## Verification

Main uses `skill://af-verification` to exercise the actual consumer path, including a realistic failure and recovery. For UI work follow the existing browser procedure and include relevant keyboard/accessibility evidence. For APIs inspect real caller outputs and error contracts. A polished mockup alone does not establish the delivered experience.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source and license](skill://af-principles/SOURCES.md).
