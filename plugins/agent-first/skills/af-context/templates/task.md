# Task <task-id>: <title>

Template target: `.agent-first/tasks/<task-id>.md`. Replace instructions; distinguish planned work, actual work, and evidence.

- State: <planned | active | blocked | completed | cancelled; select one on facts>
- Updated/owner: <date and main session/person>
- Request/source: <user request reference; do not invent a transcript location>
- Workflow and rationale: <selected route and why>
- Scope/non-goals: <authorized paths/behavior and explicit exclusions>
- Code state: <known revision plus relevant uncommitted-state description, or unknown; never claim clean without evidence>

## Requirements and acceptance

| ID | Required observable behavior | Acceptance check | Disposition and evidence |
| --- | --- | --- | --- |
| <AC-ID> | <behavior including failure/edge cases> | <proposed method; not executed evidence> | <pending, or actual outcome with verification entry ID and applicability> |

## Inputs, constraints, and decisions

- Source facts: <paths/symbols and relevant current behavior>
- Decisions: <`../decisions/<id>.md` links and acceptance/supersession status>
- Unknowns/approval: <specific missing input, why needed, decision owner>

## Plan and actual progress

| Step | Intended result | State | Actual change/result and links |
| --- | --- | --- | --- |
| <ordered step> | <checkable completion criterion> | <choose: not-started, in-progress, done, blocked> | <facts or pending; no prechecked completion> |

For delegated implementation, link each assignment in the plan and use slice acceptance results to track progress. Record the selected worker route and, after each run, the native worker reference, actual provider/model and acceptance evidence. Omit worker details for work done in main.

## Consultation disposition

- <Advisor/question, actual native task ID if available, evidence/reference, recommendation adopted/rejected/deferred and why. Use none if not needed; proposed consultation is not completed advice.>

## Verification and unresolved work

- Current applicable evidence: <`../verification.md` entry IDs; distinguish main checks from independent checks>
- Historical-only evidence: <IDs, code state, and why not current>
- Acceptance still unverified: <AC IDs and exact missing check>
- Issues/blockers: <`../issues.md` IDs, impact, owner/approval>
- Next action: <concrete action; prerequisite if blocked>

## Exit disposition

<Fill only when closing: acceptance outcomes, actual verification, remaining limitations/issues, completion or cancellation reason, and successor task if any. Keep historical failures intact.>
