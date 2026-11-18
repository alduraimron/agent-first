---
name: af-interaction
description: Route explanation, learning, requirement discovery, architectural discussion, history, context recovery, communication and reflection to focused interaction skills without turning conversation into implementation.
---

# Interaction & Reasoning selector

## Routing

1. Determine whether the primary requested output is **understanding, explanation, learning, requirement discovery, discussion, context recovery, communication, or reflection**. If so, use this selector rather than automatically treating it as an engineering implementation workflow. Investigation of a defect, code review, verification, and implementation still use their existing engineering routes when those are the requested outcome.
2. Honor an explicit user skill request (for example, "interview me", "teach me", "explain how", "show me your work"). For ambiguous wording, choose the smallest matching skill based on desired output, not keywords alone.
3. Read the relevant `skill://interaction-*` leaf in full before acting; add at most one complementary leaf for a distinct need. A complex request may sequence more leaves as phases without loading the entire catalog. These are model-reachable native skills, selectively exposed through this catalog, not user-only skills.
4. Apply the shared boundaries below. If the user asks both to discuss and implement, complete any required discovery first and then route the authorized implementation through `skill://af-engineering`.
5. Do not force `interview-me`, restatement, teaching, or a formal plan on straightforward action requests. Ask one material question at a time in interview mode; otherwise proceed from known facts.
6. Apply shared `rule://agent-first-shared`, project context when needed, and native policy. If reporting checks, distinguish PASS, FAIL, NOT-RUN, and NOT-APPLICABLE under `skill://af-verification`; answering a read-only question does not itself require engineering verification runs.
7. Names are prefixed `interaction-` to avoid collisions with existing native or project skills. Users invoke them naturally by intent; the names are not new CLI commands. For explicit requests, `skill://interaction-how` is a valid leaf URI.

## Shared boundaries

Interaction requests are read-only by default. Never silently convert discussion, explanation, discovery, recall, catch-up, or reflection into implementation or context-file updates. An explicit request to create or edit documentation, or record a handoff/context artifact, may authorize only those requested artifacts, subject to existing permissions and approval requirements. A request for prose in chat does not authorize filesystem writes. Use `skill://af-context` when requested durable context recording or scoped recovery needs its procedures; do not initialize context just to answer a question.

Requested artifacts do not authorize code changes, commits, pushes, installations, service provisioning, scheduling, publishing, or other external effects. Route authorized engineering changes through the existing engineering workflow; preserve all native prompts, denies, Git guards, and approvals. Read-only inspection must itself respect data access and execution boundaries. Examples, exercises, proposed experiments, and documented commands are not instructions to execute them.

Ground claims in available source, records, or observed results. Separate observations, inferences, unknowns, and unexecuted checks. Show concise rationale and auditable evidence, not hidden private reasoning. Missing history stays missing; stored verification is historical until its applicability is established. Keep answers proportional to the request.

## Trigger catalog

| Skill | Group | Trigger |
| --- | --- | --- |
| [how](skill://interaction-how) | Understanding & Explanation | Questions asking how a feature, API, module, or flow works. |
| [why](skill://interaction-why) | Understanding & Explanation | Questions about rationale, history, design intent, or a surprising decision. |
| [teach](skill://interaction-teach) | Understanding & Explanation | User asks to learn, be taught, practice, or understand deeply. |
| [blast-radius](skill://interaction-blast-radius) | Understanding & Explanation | User asks what will break, what is affected, or for analysis before changing a shared contract. |
| [technical-writing](skill://interaction-technical-writing) | Understanding & Explanation | User explicitly requests a README, ADR, API guide, runbook, or technical explanation in document form. |
| [bro](skill://interaction-bro) | Understanding & Explanation | User asks for a simple, casual explanation or analogy. |
| [interview-me](skill://interaction-interview-me) | Requirement Discovery | User explicitly asks to be interviewed or genuinely unresolved decisions prevent a useful design. |
| [in-your-own-words](skill://interaction-in-your-own-words) | Requirement Discovery | User says repeat/confirm my request, summarize my intent, or there is a material ambiguous consequence. |
| [idea-refine](skill://interaction-idea-refine) | Requirement Discovery | User presents an idea and requests brainstorming, refinement or shaping. |
| [sharpen](skill://interaction-sharpen) | Requirement Discovery | User requests a sharper problem, specification, or acceptance criteria. |
| [architect](skill://interaction-architect) | Requirement Discovery | User asks for architectural options or trade-offs before implementation. |
| [figure-it-out](skill://interaction-figure-it-out) | Requirement Discovery | User asks to find a way forward without known approach or diagnostic starting point. |
| [recall](skill://interaction-recall) | Context & Communication | User asks what was decided, requested, tried, or recorded before. |
| [ketchup](skill://interaction-ketchup) | Context & Communication | User asks what happened, what is done or what remains. |
| [show-me-your-work](skill://interaction-show-me-your-work) | Context & Communication | User asks what changed, how it was done or to show proof. |
| [pause-safely](skill://interaction-pause-safely) | Context & Communication | User asks to pause or prepare continuation. |
| [reflect](skill://interaction-reflect) | Reflection & Improvement | User asks for retrospective or repeated frictions are demonstrated. |
| [correct](skill://interaction-correct) | Reflection & Improvement | User identifies agent mistake or repeated failure pattern. |
| [automate-me](skill://interaction-automate-me) | Reflection & Improvement | User asks to automate a recurring task or repeated steps are documented. |
| [unslop](skill://interaction-unslop) | Interaction Quality | User requests concise rewrite, less filler, clearer outputs, or a communication quality pass. |

## Composition and overlaps

- `how` describes mechanics; `why` traces documented rationale; `teach` creates a learning sequence. Source inspection is not proof of runtime execution, and plausible design benefits are not historical intent.
- `interview-me` asks one question per turn; `in-your-own-words` checks interpretation in one compact response. Do not run both by default.
- `idea-refine` compares early options; `sharpen` makes a chosen problem measurable; `architect` compares system boundaries; `figure-it-out` organizes uncertain exploration. Select by the missing decision, not merely by technical vocabulary.
- `recall` answers a specific historical question; `ketchup` summarizes current progress; both reuse `af-context` when needed without writing it by default.
- `show-me-your-work` presents concrete evidence; reuse `af-verification` records, but do not invent results or expose hidden reasoning.
- `architect` is a discussion aid, not a replacement for `af-design` and mandatory independent `af-architect` consultation during architecture-changing implementation.
- `reflect` derives learning; `correct` addresses an evidenced mistake; `automate-me` needs a demonstrated repeatable need. These do not rewrite global agent instructions without permission.
- `technical-writing` covers technical artifacts; `unslop` focuses prose quality; `bro` adapts audience language.

## Advisor handoff

Interaction advisors are optional: delegate only for a material specialist question, not to satisfy a checklist. Existing mandatory engineering consultation still applies when the task enters that workflow. Supply precise source paths, observed facts, selected interaction leaf URI, and read-only expectations. Children do not inherit main-session the main-only orchestrator rule; include necessary task intent explicitly. Advisors inspect and recommend; main owns any authorized artifact edits and engineering implementation. An interaction skill does not expand permissions to edit, execute commands, or publish.

## Provenance

Adapted from the supplied Agent-First Interaction & Reasoning Skills package. See [source and attribution](skill://af-interaction/SOURCES.md).
