---
alwaysApply: true
agents: [main]
---

# Agent-First orchestration

Follow `rule://agent-first-shared`, project instructions and native permissions. This main-only rule selects procedures; it never replaces OMP's system prompt, modifies settings or installs tools.

## Interaction-first routing

Route by requested output. For any interaction branch below, directly `read` `skill://af-interaction`, await its result, then `read` the selected full leaf before project work:

- Explanation, learning, interview, ideation/design discussion, requirements clarification, context catch-up, retrospective or prose refinement: use the smallest matching `skill://interaction-*` leaf.
- Existing-evidence summary ("show me your work", "what changed and what passed"): use `skill://interaction-show-me-your-work`, even when inspecting a diff; do not run new checks unless asked.
- Documentation-only authoring/edits (README, ADR, guides): use `skill://interaction-technical-writing`; write only the requested artifacts.
- Code/config changes, defect investigation/review or executing new checks: use `skill://af-engineering`. Mixed requests complete needed discussion first, then implement only the authorized outcome.

Interaction replies must **never** include a `Workflow:` prefix. Questions authorize no edits. Clear engineering requests need no interview, restatement or teaching ceremony.

## Engineering execution

1. Directly `read` `skill://af-engineering` before project work, await its result, and inspect relevant repository context.
2. Begin the **first visible prose** (including final or blocked-work reports) with the exact kebab-case `Workflow: <route>` literal from `af-engineering`'s table—never a paraphrase (e.g., use `Workflow: quick-change`, not `Workflow: quick fix`)—followed by a brief rationale. Main owns implementation, verification and handoffs.
3. After routing and inspection, `read` `skill://af-principles` and only decision-relevant leaves before applying them; keep trivial work lightweight.
4. For existing `.agent-first/` context, continued work or meaningful multi-step tasks, `read` `skill://af-context`; recover authoritative state and create only minimal needed records.
5. For verification-only requests and before any completion or blocked-work report, `read` `skill://af-verification` (and `skill://principle-prove-it-works`); report PASS, FAIL, NOT-RUN and NOT-APPLICABLE with exact evidence and gaps.
6. For explicitly requested isolated work, `read` `skill://af-isolation` first. Reuse native OMP sessions, task delegation and existing Tern hosting.

## Coexistence

Preserve unrelated skills, plugins, commands and project instructions. Honor operator disables; if an Agent-First skill, rule or agent is shadowed or disabled, inspect discovery/provenance and report the conflict instead of changing filters or claiming it loaded. Never activate Agent-First in another project implicitly.
