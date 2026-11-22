# Delegated implementation

This is an opt-in execution mode for a code-edit workflow, not a new route. Keep the selected workflow's required consultation, approvals, review and checks. Main owns the plan, worker dispatch, integration and final verification; advisors and reviewers stay read-only.

## Plan before starting

1. Inspect the project and propose one slice per independently verifiable behavior, including when there is only one slice. Give each slice concrete write paths, a check, and actual blockers. Order slices that overlap in writes or depend on unaccepted work.
2. Show the shared outcome, non-goals, contracts, slices, blockers, and definition of done in chat. Apply **Agreement before changes** in `rule://agent-first-orchestrator`. Ask the user to approve the plan and select a worker model when ready to start; one reply can do both. Do not write records or dispatch workers before approval. If the user approves only saving the plan, save the records but wait for an explicit start instruction selecting a model.
3. Once authorized, read `skill://af-context` and its task template. Write one brief at `.agent-first/tasks/<task-id>.md` with the agreed outcome, non-goals, shared contracts, project guidance, and whole-task acceptance check. Link one `.agent-first/tasks/<task-id>/assignments/<slice>.md` per slice and write each using the [assignment template](skill://af-context/templates/assignment.md). Reuse the approved records if they were already saved without starting workers.

## Start on the selected model

Use native `task` to launch a fresh worker per ready assignment. Choose the route from the user's start instruction:

- **Tagged model:** Use the native `^` model tag's session alias (such as `m1`) in each task item's `agent` field. A plain display name or unregistered tag is not an alias. The tagged route can inherit native overrides and fallback; tell the user this when asking them to choose it.
- **Exact model with no main-loop fallback:** Use the exact `provider/model-id` in the task item's `model` field with the bundled general-purpose agent (or the matching unlevelled model tag). This requires operator-approved native per-call routing (`task.perCallModel: on` and model grants). Use it only if the tool advertises `model`. Report an unavailable or refused route as blocked; do not change config, strip the pin, pick a different model, or implement the assignment yourself without a new instruction.

Re-read the brief and current assignments before dispatch. Put the shared brief path in shared `context` when using the batch schema and include both paths in each actual assignment prompt. Require the worker to `read` both files and applicable project guidance before its first edit. Give the worker these boundaries in the prompt: edit only assigned paths using the native file tools; leave task records, commands/checks, Git and further delegation to main; return changed paths, acceptance notes, and blockers. Surface contradictions with repo instructions or scope instead of improvising. Write scope is an instruction, not a filesystem sandbox.

## Accept before unblocking

- Run at most two workers at once, and only if they have disjoint writes and neither consumes the other's unaccepted work. Wait for settled results. Main checks actual edits, including new files, against each slice's scope, spec and project standards. Record the native worker reference and observed provider/model from task metadata or the session record; don't infer it from the requested selector. Report model drift or unavailable identity; do not accept a worker whose actual model does not match the selection.
- Run the slice's acceptance check before marking it accepted and releasing its dependents. Record actual results in the shared brief. A failed, blocked, oversized or out-of-scope contribution stays unaccepted; preserve user changes and report the blocker, withhold dependent dispatches, and continue only independent work. Main can reassign a scoped correction on the authorized model; a different model or main implementation requires user authorization.
- Once all slices are accepted, review the combined changes against the shared brief and project standards, run the whole-task acceptance checks, and close the task only on applicable evidence. Keep Git actions under the usual authorization rules.
