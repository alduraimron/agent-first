---
name: af-context
description: Recover a personal project's active task and decisions across sessions; initialize, update, or hand off durable repository context; record verification history, unresolved issues, and evidence-backed corrections.
---

# Durable project context

Use `.agent-first/` files as lightweight, inspectable project memory—not a runtime or policy engine. Inherit `rule://agent-first-shared` and `af-verification`. Main writes artifacts within the authorized project; advisors inspect and recommend only. Keep bookkeeping proportional so it never crowds out implementation or verification.

## Recovery first

1. Check for `.agent-first/context.md`. If absent, inspect project docs and scope before deciding whether initialization helps (skip paperwork for trivial edits).
2. Read `context.md`, its active task, `handoff.md` (if present) and decisions/issues/verification rows referenced by ID—not every historical file. Missing linked files are gaps, never invented history.
3. Reconcile stored state against the current request, project instructions, source code and native session metadata. Context/handoff are indexes, not authority over instructions; only accepted (with acceptance source), unsuperseded decisions constrain work. Surface conflicts and get approval before changing accepted constraints while continuing independent work.
4. Confirm `context.md` and `handoff.md` agree on the active task (prefer task record for work state, decision record for rationale after reconciling newer evidence).
5. Treat all stored check results as **historical** until applicability to current source, revision, environment and inputs is verified under `af-verification`.

## Minimal templates

Read only the templates needed for this task; create only relevant files with real known facts (leave unknowns explicit, remove placeholders, never generate an empty tree). On read-only tasks, propose records instead of writing them.

| Artifact | Load template when |
| --- | --- |
| `.agent-first/context.md` | Creating project index: [context](skill://af-context/templates/context.md) |
| `.agent-first/tasks/<task-id>.md` | Tracking meaningful work: [task](skill://af-context/templates/task.md) |
| `.agent-first/decisions/<id>.md` | Recording material choice/approval: [decision](skill://af-context/templates/decision.md) |
| `.agent-first/verification.md` | Recording check evidence or unrun requirements: [verification](skill://af-context/templates/verification.md) |
| `.agent-first/handoff.md` | Pausing, transferring or recovering work: [handoff](skill://af-context/templates/handoff.md) |
| `.agent-first/issues.md` | Tracking unresolved defects/blockers: [issues](skill://af-context/templates/issues.md) |
| `.agent-first/corrections.md` | Recording repeated failure patterns and validated fixes: [corrections](skill://af-context/templates/corrections.md) |

Use unique descriptive IDs (`<date>-<short-slug>`) and relative links. Never edit `AGENTS.md`, team instructions or native config to initialize context. Keep secrets, tokens and private customer data out of tracked files (gitignore is not redaction); cite only real retained evidence paths.

## Update, handoff and close

- **Context (`context.md`):** Short index—purpose/boundaries, source pointers, commands, actual session pointer (or `unavailable`) and one active task link.
- **Task (`tasks/<id>.md`):** Requirements, non-goals, acceptance, plan/progress, advisor disposition, edits and next action.
- **Decisions (`decisions/<id>.md`):** Material choices that would otherwise be rediscovered—options, rationale, compatibility/rollback, enforceable constraints, approval source (keep pending distinct from accepted) and proposed checks. Supersede with mutual links rather than rewriting history.
- **Verification (`verification.md`):** Append actual runs or concrete blocked/unrun checks (exact command/cwd, code state, outcome/error, evidence path, covered criteria, limits). Preserve failed rows; append dated corrections rather than erasing history.
- **Issues (`issues.md`):** Unresolved blockers with impact, evidence, owner/approval needed and next action.
- **Handoff & close (`handoff.md`):** Update task state first, then `context.md` and `handoff.md` together with code state, verified vs historical evidence, gaps, blockers and next action. On completion, set active task to `none` with a last-task link; on interruption, keep the active task open—never mark complete because a session is ending.

## Corrections ledger

Use `.agent-first/corrections.md` for project learning (Agent-First's own seeded examples live in `docs/corrections.md` in its source repo):

1. Record observed occurrence, evidence, impact and confirmed vs hypothesized root cause. Group independent occurrences (one tool-error cascade = one occurrence); separate code/parser bugs from model compliance, schema errors, denials and timeouts.
2. Fix at the lowest effective layer (architecture > code > tooling > workflow > skill). Promote a broad behavioral rule only with repeated attributable evidence, diagnosed mechanism, minimal placement, owner approval and a falsifiable validation plan—never auto-rewrite global policy.
3. Link the actual change and validation before marking fixed (parser replays prove parser fixes, not model compliance; preserve failed history).
