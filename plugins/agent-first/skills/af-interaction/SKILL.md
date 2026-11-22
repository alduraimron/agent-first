---
name: af-interaction
description: Route explanation, learning, requirement discovery, architectural discussion, history, context recovery, communication and reflection to focused interaction skills without turning conversation into implementation.
---

# Interaction & Reasoning selector

Apply `rule://agent-first-shared`. Use this selector when the primary requested output is **understanding, explanation, learning, discovery, discussion, context recovery, documentation/prose or reflection**—not code changes, defect diagnosis (`bug-investigation`), defect review (`code-review`) or executing new checks (which route to `skill://af-engineering`).

## Routing and boundaries

1. Honor explicit requests ("interview me", "teach me", "explain how", "show me your work"); otherwise pick the smallest matching `skill://interaction-*` leaf by desired output, not keywords alone.
2. `read` the selected full leaf before acting (at most one complementary leaf for a distinct need; multi-phase requests sequence leaves rather than loading the catalog). Never emit an engineering `Workflow:` prefix.
3. **Read-only by default:** Never convert discussion, explanation, recall, catch-up or reflection into edits or context-file writes. Explicit artifact requests (e.g., README/ADR/handoff) authorize **only** those artifacts—never code edits, commits, installs or external effects. Examples and documented commands are not execution instructions.
4. For mixed discuss-and-implement requests, finish needed discovery first, then route authorized implementation to `skill://af-engineering`. Clear engineering actions need no interview or teaching ceremony. Ask one material question at a time in interview mode.
5. Ground claims in actual source, records or observed results. Separate observations, inferences, unknowns and unexecuted checks; stored verification is historical until applicability is confirmed. Use `skill://af-context` only when durable recording/recovery needs it, and `skill://af-verification` outcome labels when reporting checks.

## Trigger catalog

| Skill | Group | Trigger |
| --- | --- | --- |
| [how](skill://interaction-how) | Understanding | How a feature, API, module or flow works in source |
| [why](skill://interaction-why) | Understanding | Rationale, history, design intent or surprising past decision |
| [teach](skill://interaction-teach) | Understanding | User asks to learn, be taught, practice or understand deeply |
| [blast-radius](skill://interaction-blast-radius) | Understanding | What will break or what consumers are affected before a contract change |
| [technical-writing](skill://interaction-technical-writing) | Understanding | Explicit request to write/edit a README, ADR, API guide or runbook |
| [bro](skill://interaction-bro) | Understanding | Simple, plain-language explanation or analogy |
| [interview-me](skill://interaction-interview-me) | Discovery | Explicit interview request or unresolved decisions block useful design |
| [in-your-own-words](skill://interaction-in-your-own-words) | Discovery | Confirm/restate intent or resolve a material ambiguous consequence |
| [idea-refine](skill://interaction-idea-refine) | Discovery | Brainstorm, refine or shape an early concept |
| [sharpen](skill://interaction-sharpen) | Discovery | Turn a chosen problem into measurable specs/acceptance criteria |
| [architect](skill://interaction-architect) | Discovery | Discuss project architecture or conventions, or record or revise approved project standards |
| [figure-it-out](skill://interaction-figure-it-out) | Discovery | Find a safe next diagnostic step with no known starting point |
| [recall](skill://interaction-recall) | Context | Recover a specific past decision, attempt or record |
| [ketchup](skill://interaction-ketchup) | Context | Summarize what is done, active, blocked and next |
| [show-me-your-work](skill://interaction-show-me-your-work) | Context | Summarize actual changes and existing verification evidence |
| [pause-safely](skill://interaction-pause-safely) | Context | Pause work and prepare a recoverable handoff |
| [reflect](skill://interaction-reflect) | Reflection | Retrospective or lessons from repeated demonstrated friction |
| [correct](skill://interaction-correct) | Reflection | Address an evidenced agent mistake or repeated failure pattern |
| [automate-me](skill://interaction-automate-me) | Reflection | Assess automating a documented recurring task |
| [unslop](skill://interaction-unslop) | Quality | Tighten prose, cut filler and improve clarity without losing risks |

## Disambiguation and advisor handoff

- `how` = mechanics; `why` = documented rationale (plausible benefits are not historical intent); `teach` = progressive practice.
- `interview-me` asks one question per turn; `in-your-own-words` confirms understanding in one compact reply—don't combine by default.
- `architect` is a discussion aid, **not** a substitute for `af-design` and mandatory `af-architect` consultation during architecture-changing implementation.
- `reflect`/`correct`/`automate-me` never rewrite global instructions without permission.
- **Optional advisors:** Delegate only for a material specialist question (never a checklist). Supply paths, observed facts, selected interaction leaf URI and read-only scope; children do not inherit the main-only orchestrator rule. Main owns any authorized artifact edits.

Adapted from the supplied Agent-First Interaction & Reasoning Skills package. See [source and attribution](skill://af-interaction/SOURCES.md).
