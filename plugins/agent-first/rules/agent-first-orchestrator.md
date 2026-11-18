---
alwaysApply: true
agents: [main]
---

# Agent-First orchestration

Follow `rule://agent-first-shared`, project instructions and effective native permissions. This main-only rule selects procedures; it does not replace OMP's system prompt, modify settings or install anything.

## Interaction-first intent routing

Route by requested output. For an interaction branch below, first directly `read` `skill://af-interaction`, await the result, then read the selected full leaf before project work:

- Explanation, learning, interview, idea/design discussion, requirements clarification, context catch-up, retrospective or prose improvement: select the relevant interaction leaf.
- Existing-evidence report ("show me your work", "what changed and what passed"): use `skill://interaction-show-me-your-work`, even when inspecting a diff. Summarizing retained evidence is not a request to execute new checks.
- Documentation-only authoring or edits, including README/ADR file requests: use `skill://interaction-technical-writing`, not an engineering quick change. Writes stay within the requested artifacts.
- Code/configuration changes, actual defect investigation/review or executing new checks: use `skill://af-engineering`. Mixed requests complete needed discussion first, then implement only the authorized outcome.

Interaction routes emit no engineering `Workflow:` prefix. Questions authorize no edits. Clear engineering actions need no interview, restatement or teaching ceremony.

## Engineering execution

For engineering execution, directly `read` `skill://af-engineering` before project work; await its result, inspect relevant repository context and use its route format for the first prose report. Select and adapt the workflow from intent, complexity, risk and architectural impact without asking the user to choose commands or agents. Main owns implementation, verification and evidence-backed handoffs.

After routing and relevant inspection, read `skill://af-principles` and only the decision-relevant leaves before applying them. Reassess when evidence changes. Keep trivial work lightweight; principles refine workflow decisions rather than adding a planning ceremony.

For existing `.agent-first/` context, continued work or meaningful multi-step tasks, read `skill://af-context` before planning or modifying files. Recover authoritative requirements, decisions, active progress, blockers and applicable historical evidence; create only needed artifacts. Reassess the route when recovery reveals new risk. Use reversible local choices within scope and obtain consequential decisions under the shared contract.

For verification-only work and before engineering completion or blocked-work reports, read `skill://af-verification`; report actual PASS, FAIL, NOT-RUN and NOT-APPLICABLE with commands, runtime evidence, gaps and remaining risks. For explicitly requested isolated work, read `skill://af-isolation` before checkout operations. Reuse native OMP sessions, task delegation and the existing Tern browser, not a parallel runtime.

## Coexistence

Keep unrelated skills, plugins, commands and project instructions intact. Operator exclusions and unavailable capabilities remain effective. If an Agent-First skill/rule/agent name is shadowed or disabled, inspect native discovery/provenance and report the conflict instead of changing filters, overwriting definitions or claiming the missing procedure loaded. Do not activate or install Agent-First in another project implicitly.
