# Delegated implementation

This is an opt-in execution mode for a code-edit workflow, not a new route. Keep the selected workflow's required consultation, approvals, review and checks. Main owns the plan, worker dispatch, integration and final verification; advisors and reviewers stay read-only.

## Plan before starting

1. Read `skill://af-context` and its task template. Write one shared brief at `.agent-first/tasks/<task-id>.md`: outcome, non-goals, shared contracts, project guidance and how to prove the whole task is done. Link each assignment in the brief's plan.
2. Read the [assignment template](skill://af-context/templates/assignment.md). Write one `.agent-first/tasks/<task-id>/assignments/<slice>.md` per independently verifiable behavior, including when there is only one slice. Split by a behavior that can be demonstrated, not by technical layer. Name actual blockers and give each slice concrete write paths. Order slices with overlapping writes or unfinished contract dependencies; never infer independence from different ticket names.
3. Show the user the slices, blockers and definition of done. End the planning turn without dispatching workers or editing implementation files. Wait for a follow-up that authorizes starting with a selected worker model. The task brief and assignments are the only new context records needed for this handoff.

## Start on the selected model

Use native `task` to launch a fresh worker per ready assignment. Choose the route from the user's start instruction:

- **Tagged model:** Use the native `^` model tag's session alias (such as `m1`) in each task item's `agent` field. A plain display name or unregistered tag is not an alias. The tagged route can inherit native overrides and fallback; tell the user this when asking them to choose it.
- **Exact model with no main-loop fallback:** Use the exact `provider/model-id` in the task item's `model` field with the bundled general-purpose agent (or the matching unlevelled model tag). This requires operator-approved native per-call routing (`task.perCallModel: on` and model grants). Use it only if the tool advertises `model`. Report an unavailable or refused route as blocked; do not change config, strip the pin, pick a different model, or implement the assignment yourself without a new instruction.

Re-read the brief and current assignments before dispatch. Put the shared brief path in shared `context` when using the batch schema and include both paths in each actual assignment prompt. Require the worker to `read` both files and applicable project guidance before its first edit. Give the worker these boundaries in the prompt: edit only assigned paths using the native file tools; leave task records, commands/checks, Git and further delegation to main; return changed paths, acceptance notes, and blockers. Surface contradictions with repo instructions or scope instead of improvising. Write scope is an instruction, not a filesystem sandbox.

## Accept before unblocking

- Run at most two workers at once, and only if they have disjoint writes and neither consumes the other's unaccepted work. Wait for settled results. Main checks actual edits, including new files, against each slice's scope, spec and project standards. Record the native worker reference and observed provider/model from task metadata or the session record; don't infer it from the requested selector. Report model drift or unavailable identity; do not accept a worker whose actual model does not match the selection.
- Run the slice's acceptance check before marking it accepted and releasing its dependents. Record actual results in the shared brief. A failed, blocked, oversized or out-of-scope contribution stays unaccepted; preserve user changes and report the blocker, withhold dependent dispatches, and continue only independent work. Main can reassign a scoped correction on the authorized model; a different model or main implementation requires user authorization.
- Once all slices are accepted, review the combined changes against the shared brief and project standards, run the whole-task acceptance checks, and close the task only on applicable evidence. Keep Git actions under the usual authorization rules.
