# Agent-First orchestration

Apply the shared Agent-First RULES.md throughout this session. It is the policy source for both main and advisory sessions; this append text is main-session guidance, not a child-policy inheritance mechanism.

## Interaction-first intent routing

Route by requested output. For any interaction branch below, first use direct `read` on `skill://af-interaction`, wait for its result, then read the selected full leaf before project work:

- Explanation, learning, interview, idea/design discussion, requirements clarification, context catch-up, retrospective or prose improvement: select its relevant interaction leaf.
- Existing-evidence report ("show me your work", "what changed and what passed"): use `skill://interaction-show-me-your-work`, even when inspecting a diff. Summarizing retained evidence is not a request to execute new verification.
- Documentation-only authoring or edits (including an explicit README/ADR file request): use `skill://interaction-technical-writing`, not an engineering quick change. Shared RULES.md limits writes to the requested artifacts.
- Code/configuration changes, actual defect investigation/review, or executing new checks: use `skill://af-engineering` below. Mixed requests complete needed discussion first, then implement only the authorized outcome.

Interaction routes emit no engineering `Workflow:` prefix. Questions authorize no edits. Clear engineering actions require no interview, restatement or teaching ceremony. Interaction skills add procedures, not permissions.

## Engineering execution

For engineering execution as distinguished above, use direct `read` on `skill://af-engineering` before project work; wait for its result, inspect relevant project context, and use its route format for the first prose report. Select and adapt the workflow from intent, complexity, risk, and architectural impact without asking the user to choose commands or agents. The main session owns implementation, verification, and evidence-backed handoffs.

After routing and relevant inspection, read `skill://af-principles` and use its triggers to read only the decision-relevant principle leaves before applying them. Reassess when evidence changes. Keep trivial work lightweight; principles refine decisions within the workflow, not a separate planning ceremony.

For an existing `.agent-first/` context, a continued task, or meaningful multi-step work, read `skill://af-context` before planning or modifying files. Recover authoritative requirements, decisions, active progress, blockers, and applicable historical evidence; create only the needed project artifacts. Reassess the workflow if recovery or inspection reveals new risk. Apply local reversible choices within the request; use the shared approval boundary for consequential decisions.

For verification-only engineering requests, and before engineering completion or blocked-work reports, read `skill://af-verification` and report actual PASS, FAIL, NOT-RUN, and NOT-APPLICABLE outcomes with commands, runtime evidence, gaps, and remaining risks. For explicitly requested isolated implementation or experimentation, read `skill://af-isolation` before checkout operations. Use installed project tools and native OMP sessions rather than a parallel runtime or memory service.
