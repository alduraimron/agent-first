---
name: af-context
description: Recover a personal project's active task and decisions across sessions; initialize, update, or hand off durable repository context; record verification history, unresolved issues, and evidence-backed corrections.
---

# Durable project context

Use repository files as a small, inspectable memory, not a new runtime or policy engine. Shared safety is inherited from RULES.md; evidence execution and outcome meanings belong to `af-verification`. Main maintains these artifacts within the authorized personal project. Advisors can inspect them and recommend updates but cannot write them.

## Recovery first

1. Locate the authorized repository root with native inspection. Look for `.agent-first/context.md`; if absent, inspect existing project documentation and the requested scope before deciding whether initialization is useful. Trivial quick changes need no new paperwork. Existing context still needs relevant task/evidence updates.
2. Read context, its one active task, `.agent-first/handoff.md` if present, and the decisions that task references. Load relevant issues and verification rows by their linked IDs, not every historical file. A missing linked artifact is a gap to resolve, not an invitation to invent history.
3. Reconcile stored state against the current request, existing project instructions, source/configuration, and available native session metadata. Context and handoff are indexes, not authority to override instructions. Accepted, unsuperseded decisions constrain the task; draft proposals do not. Verify a decision's acceptance source before treating it as accepted. A source conflict is recorded explicitly; obtain required approval before changing an accepted constraint. Continue independent work that does not depend on the conflict.
4. Identify the current task's requirements, acceptance, completed work, outstanding blockers, next action, and relevant constraints. Check that context and handoff name the same active task. Prefer the task record for work state and the decision record for rationale, after reconciling any newer evidence; timestamps alone do not resolve contradictory claims. Finish recovery when these items are known or their exact gaps are recorded.
5. Treat all stored command/test/browser results as historical. Compare their task, revision or described working state, last relevant edit, environment, inputs, and coverage with the current task. Cite history accurately; only current applicable evidence can support a current verification claim under `af-verification`. A recorded PASS is never inherited simply by opening a new session.

## Create the minimum relevant files

For meaningful new work or recovery, use the templates below. Read only the templates needed for this task. Copy their structure into new target files with real known facts, leaving unavailable fields explicitly unknown and planned checks unexecuted. Fill or remove instruction placeholders before handoff. Do not generate an empty tree or unrelated artifacts.

| Artifact and fixed target | Load template when |
| --- | --- |
| `.agent-first/context.md` | Establishing a project's durable index: [context](skill://af-context/templates/context.md) |
| `.agent-first/tasks/<task-id>.md` | Tracking meaningful requirements/work: [task](skill://af-context/templates/task.md) |
| `.agent-first/decisions/<id>.md` | Recording a material choice/approval: [decision](skill://af-context/templates/decision.md) |
| `.agent-first/verification.md` | Recording evidence or an explicitly unrun required check: [verification](skill://af-context/templates/verification.md) |
| `.agent-first/handoff.md` | Pausing, transferring, or recovering work: [handoff](skill://af-context/templates/handoff.md) |
| `.agent-first/issues.md` | Tracking an unresolved defect, uncertainty, or blocker: [issues](skill://af-context/templates/issues.md) |
| `.agent-first/corrections.md` | Recording an observed failure pattern and validated correction: [corrections](skill://af-context/templates/corrections.md) |

Use stable descriptive IDs, such as `<date>-<short-slug>`, unique among existing files. Inspect the target before creation; update existing relevant files without replacing unrelated content. Set context's active-task link only when that task exists. Link paths relative to their containing file. These are ordinary project files: they neither load instructions automatically nor require a session hook, extension, database, or global write. Initialization does not edit AGENTS.md, team instructions, profile policy, or defaults. If meaningful work is read-only, propose context creation rather than writing it.

Record only task-relevant facts. Keep credentials, tokens, personal data, and raw sensitive output out of tracked context. For raw evidence use an already confirmed private/gitignored location or an authorized external location; verify its privacy before storing sensitive artifacts. A reference must resolve to actual retained evidence or say unavailable. Gitignore is not secret redaction. Do not create ignore rules or relocate existing user files merely to populate a template.

## Update during work

1. Keep context short: project purpose/boundaries, source pointers, existing command definitions, actual native session pointer if available, and one active task. Use native session metadata supplied by the runtime; if inaccessible, record unavailable instead of guessing an ID or path. A session pointer aids recovery but cannot replace the task/decision/evidence files.
2. Put requirements, non-goals, acceptance, plan/progress, specialist advice disposition, edits, and next action in the task record. Track completed versus remaining work explicitly. Main still owns verification and final disposition.
3. Record a decision when a material choice would otherwise be rediscovered: options, rationale, compatibility/rollback, enforceable constraints, approval source, and proposed checks. Keep pending approval distinct from accepted. Supersede explicitly with links in both records; preserve the old rationale rather than rewriting history.
4. Append verification entries after actual results or a concrete blocked/unrun requirement. Include exact command/action and cwd, task and code-state identity, outcome/exit or tool error, evidence location, covered acceptance criteria, and limits. For an attempted command rejected before execution, record the attempt/error and NOT-RUN for the check, not a test failure or success. Keep proposed checks in the task/decision until attempted or explicitly dispositioned.
5. Preserve prior evidence rows and failed runs. If an attribution/result was wrong, append a dated correction referencing the original row and reason; do not silently replace it. Record applicability changes after relevant edits without erasing prior observations. Separate independent acceptance checks, model-authored tests, advisory inspection, and browser evidence.
6. Record unresolved issues with impact, evidence, owner/approval needed, next action, and links. A repeated issue can motivate a correction but is not itself permission to change policy.

The update is complete when the task and linked decisions describe the actual current state, evidence is attributable without interpreting a chat transcript, and unfinished work is discoverable.

## Handoff and close

Refresh handoff with the active task link, code-state identity, verified facts and evidence IDs, historical-only observations, remaining acceptance gaps, blockers/approval, and the next executable action. Update task state first, then context's active task and handoff together. For completion, record acceptance disposition and unresolved limitations; clear active task to `none` and retain a last-task link. For interruption, leave the active task and explicit next action. Never mark completion because the session is ending. Finish when a fresh session can recover work from these files without treating pending proposals or old results as current proof.

## Corrections: observe, diagnose, validate

Use `.agent-first/corrections.md` for project learning. The system's seeded Phase 1 examples and provenance caveats are in `docs/corrections.md` in the Agent-First source repository, not an assumed file in every project.

1. Record an actual occurrence with evidence and impact. Label root cause confirmed or hypothesized. Separate implementation/parser defects from model compliance, schema mistakes, unavailable approval, and runtime timeouts; a passing program test does not discharge a workflow failure.
2. Group independent occurrences of the same mechanism. A tool-error cascade in one run is one occurrence. One failure can justify a local defect fix; it does not establish a general model pattern or justify a new always-loaded rule.
3. Choose the lowest effective placement: architecture for a boundary, code for behavior, tooling for parsing/enforcement, workflow for ordering, skill for a missing domain procedure. Prefer removing the cause to adding reminders; retain exact approval boundaries.
4. Propose promotion only with repeated attributable evidence for a broad behavioral rule, a diagnosed mechanism, a minimal change at its owner, and a falsifiable validation plan. State counterexamples and scope limits. Approval and editing authority still apply; no automatic policy, prompt, skill, runtime, or configuration rewriting.
5. Link the actual change and validation result before marking fixed. A parser replay can establish the parser correction, not model compliance. A successful targeted model run establishes that scenario only; retain broader risk as monitored and failed history as failed. Untested changes remain proposed or implemented-unverified, never validated.
