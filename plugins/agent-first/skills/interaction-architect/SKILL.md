---
name: interaction-architect
description: Discuss project architecture and conventions, compare trade-offs before implementation, and record or revise project standards when the user approves and authorizes saving them.
hide: true
---

# architect - Requirement Discovery

## Intent and trigger

Facilitate initial architecture and convention choices, or revisit one standard in an existing project. Keep the design discussion separate from implementation.

## Procedure

1. Inspect existing project instructions, relevant guides and code. Identify decisions the user needs to make, the constraints and where each decision belongs.
2. Compare viable options where there is a material trade-off. Turn preferences into concrete rules: what they apply to, what to do instead, and any exceptions. Resolve open decisions with the user under **Agreement before changes** in `rule://agent-first-orchestrator`.
3. Summarize the decisions and intended files. Ask the user to confirm the proposed standards and authorize saving them, unless they already approved that specific proposal and asked to save it. Discussion alone leaves files unchanged.
4. Update the existing authoritative section in place. Keep short project-wide rules in the project's instruction file (`AGENTS.md` by default). Put area-specific rules and examples in the area's guide, and put architecture boundaries and data flow in the architecture doc. For each changed or new guide, ensure the instruction file has a direct, scoped pointer such as “Before editing React components, read [React conventions](docs/react.md).” Keep the details in the guide, not in the pointer. Use an ADR only when a consequential trade-off needs a separate rationale. Create files only as needed.
5. Check that changed pointers resolve, the saved wording matches the approved scope and exceptions, and unrelated content remains intact. If the decision describes a target architecture that is not yet implemented, label it as such. Saving a standard does not authorize changing application code, lint configuration or `.agent-first/` records.

## Output contract

During discussion: options, recommendation, open choices and proposed destinations. After an authorized save: exact files changed and any unresolved conflicts. Refer substantive domain questions to `skill://af-design` or the `af-architect` advisor when needed.

## Boundaries and failure modes

Read `skill://af-interaction` for shared boundaries if not already loaded. Follow shared `rule://agent-first-shared`, accepted project decisions, and native permissions. Discussion-only requests do not authorize code edits. This skill does not substitute for mandatory architect advisory in an engineering workflow; interaction-only consultation remains optional. Label observations, inferences, unknowns, and unexecuted checks separately. Keep answers proportional to the request.

## Example invocation

- User: Compare monolith versus service boundaries without coding.
- Success: Deliver decision options and a recommendation without implementation or permission escalation.
