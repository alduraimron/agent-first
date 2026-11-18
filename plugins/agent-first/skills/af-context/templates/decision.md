# Decision <id>: <title>

Template target: `.agent-first/decisions/<id>.md`. A written proposal is not approval. Replace instructions with evidence and explicit status.

- Status: <proposed | pending-approval | accepted | rejected | superseded>
- Date/owner: <date and decision owner>
- Task: <relative `../tasks/<task-id>.md` link>
- Supersedes: <decision link or none>
- Superseded by: <decision link or none; update old record when superseding>

## Context and decision question

<Requirement, existing boundary, relevant source paths, uncertainty, and why a decision is needed now.>

## Options

| Option | Benefits | Costs/risks | Compatibility and rollback |
| --- | --- | --- | --- |
| <smallest viable change> | <specific> | <specific> | <consumer/migration impact and reversibility> |
| <viable alternative> | <specific> | <specific> | <impact and reversibility> |

## Chosen option and rationale

<Proposed choice while pending, accepted choice only after authority is recorded. Explain trade-offs, rejected option, assumptions that would change the choice, and rollout sequence.>

## Authority and approval

- Approval required: <specific action/compatibility/scope change and owner, or why within existing authorization>
- Approval source/status: <actual user/authorized decision reference and date, or pending; never infer consent from advice>

## Enforceable constraints and checks

| Constraint ID | Source/mandatory or proposed | Boundary and observable invariant | Check and evidence |
| --- | --- | --- | --- |
| <ID> | <requirement or proposal reference> | <precise behavior> | <proposed check; actual verification entry link only when available> |

## Revisit conditions

<Triggers, unresolved assumptions, approval gaps, or conditions that require a new superseding decision. Preserve this record's original rationale.>
