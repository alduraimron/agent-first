---
alwaysApply: true
agents: [main]
---

# Agent-First orchestration

Follow `rule://agent-first-shared`, project instructions and native permissions. This main-only rule selects procedures; it never replaces OMP's system prompt, modifies settings or installs tools.

## Agreement before changes

**A request for a nontrivial change starts a read-only planning turn, even if it specifies the full change and asks you to implement now.** End that turn with a direct question. Wait for the user to approve the proposed plan in a later message before writing any project files or `.agent-first/` records, dispatching implementation workers, or taking proposed external actions. Read-only investigation and advice can proceed within the request.

1. **Simple exception:** Proceed on a direct request only for an exact, local, low-risk correction with an obvious acceptance check, such as a typo or label replacement. New behavior or capabilities, contract changes, project standards, and delegated implementation always require plan approval, even if the patch is small and all requirements are explicit.
2. **Resolve decisions:** Inspect available evidence first. If an unresolved decision changes the outcome, scope, or approach, ask one focused question with a recommendation and its trade-off, then end the turn. Use the answer to decide what to ask next.
3. **Confirm the plan:** Once material choices are settled, state the goal, scope, approach, and observable definition of done. Ask whether to proceed and end the turn. Approval must refer to the specific plan already presented in this conversation. An initial implementation request, agreement with an individual design choice, or silence does not count.
4. **Stay in scope:** Start only the approved actions. Reopen the gate if new evidence changes the agreed outcome, scope, or approach materially. Routine execution choices within the approved plan need no new prompt. Plan approval never grants additional native permissions or replaces action-specific approval.

## Interaction-first routing

Route by requested output. For any interaction branch below, directly `read` `skill://af-interaction`, await its result, then `read` the selected full leaf before project work:

- Plan or start explicitly delegated code implementation: use `skill://af-engineering` and its delegated implementation procedure, even when this turn only prepares the plan.
- Project architecture or standards discussion, a follow-up that approves saving those decisions, or a request to record or revise a settled standard: use `skill://interaction-architect`, including for docs-only saves. General documentation requests use technical writing.
- Explanation, learning, interview, ideation, requirements clarification, context catch-up, retrospective or prose refinement: use the smallest matching `skill://interaction-*` leaf.
- Existing-evidence summary ("show me your work", "what changed and what passed"): use `skill://interaction-show-me-your-work`, even when inspecting a diff; do not run new checks unless asked.
- Documentation-only authoring/edits (README, ADR, guides): use `skill://interaction-technical-writing`; write only the requested artifacts.
- Code/config changes, defect investigation/review or executing new checks: use `skill://af-engineering`. Mixed requests complete needed discussion first, then implement only the authorized outcome.

Interaction replies must **never** include a `Workflow:` prefix. Discussion alone authorizes no edits.

## Engineering execution

1. Directly `read` `skill://af-engineering` before project work, await its result, and inspect relevant repository context.
2. Begin the **first visible prose** (including final or blocked-work reports) with the exact kebab-case `Workflow: <route>` literal from `af-engineering`'s table—never a paraphrase (e.g., use `Workflow: quick-change`, not `Workflow: quick fix`)—followed by a brief rationale. Main owns implementation, verification and handoffs.
3. After routing and inspection, `read` `skill://af-principles` and only decision-relevant leaves before applying them; keep trivial work lightweight.
   - For explicitly requested subagent implementation, `read` `skill://af-engineering/workflows/delegated-implementation.md` before editing or dispatching. Keep the normal workflow's prerequisites.
4. For existing `.agent-first/` context, continued work or meaningful multi-step tasks, `read` `skill://af-context`; recover authoritative state and create only minimal needed records.
5. For verification-only requests and before any completion or blocked-work report, `read` `skill://af-verification` (and `skill://principle-prove-it-works`); report PASS, FAIL, NOT-RUN and NOT-APPLICABLE with exact evidence and gaps.
6. For explicitly requested isolated work, `read` `skill://af-isolation` first. Reuse native OMP sessions, task delegation and existing Tern hosting.

## Coexistence

Preserve unrelated skills, plugins, commands and project instructions. Honor operator disables; if an Agent-First skill, rule or agent is shadowed or disabled, inspect discovery/provenance and report the conflict instead of changing filters or claiming it loaded. Never activate Agent-First in another project implicitly.
