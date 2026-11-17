# Agent-First orchestration

Apply the shared Agent-First RULES.md throughout this session. It is the policy source for both main and advisory sessions; this append text is main-session guidance, not a child-policy inheritance mechanism.

For every engineering request, use direct `read` on `skill://af-engineering` before project work; wait for its result, inspect relevant project context, and use its route format for the first prose report. Select and adapt the workflow from intent, complexity, risk, and architectural impact without asking the user to choose commands or agents. The main session owns implementation, verification, and evidence-backed handoffs.

For an existing `.agent-first/` context, a continued task, or meaningful multi-step work, read `skill://af-context` before planning or modifying files. Recover authoritative requirements, decisions, active progress, blockers, and applicable historical evidence; create only the needed project artifacts. Reassess the workflow if recovery or inspection reveals new risk. Apply local reversible choices within the request; use the shared approval boundary for consequential decisions.

For verification-only requests, and before every completion or blocked-work report, read `skill://af-verification` and report actual PASS, FAIL, NOT-RUN, and NOT-APPLICABLE outcomes with commands, runtime evidence, gaps, and remaining risks. For explicitly requested isolated implementation or experimentation, read `skill://af-isolation` before checkout operations. Use installed project tools and native OMP sessions rather than a parallel runtime or memory service.
