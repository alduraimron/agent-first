# Project context

Template target: `.agent-first/context.md`. Replace instructions with sourced facts; use `unknown` for unavailable information. This file indexes state; it does not override project instructions.

- Project: <name and purpose>
- Authorized repository/scope: <root and boundaries; exclude unrelated/team work>
- Updated: <date and responsible session/person>
- Native session: <actual runtime-provided session ID/path, or unavailable; never guess>
- Active task: <relative link `tasks/<task-id>.md`, or none>
- Last task: <relative link if applicable, or none>
- Handoff: <`handoff.md` link if present, or none>

## Project facts and source pointers

- <Fact, authoritative source path/symbol, and known limitations. Keep volatile facts in source.>
- Instructions/conventions: <existing document paths; preserve their authority>
- Architecture/contract decisions: <links to relevant accepted `decisions/<id>.md`; indicate pending decisions separately>

## Existing commands

| Purpose | Definition/source | Exact command and cwd | Preconditions/approval | Last evidence |
| --- | --- | --- | --- | --- |
| <test/build/run purpose> | <existing script/config path> | <observed command definition, not a claim of execution> | <installed capabilities and authorization needed> | <verification entry ID or none> |

## Recovery links and conflicts

- Evidence: <`verification.md` if present; recorded outcomes are historical until applicability is checked>
- Unresolved issues: <`issues.md` if present or none>
- Corrections: <`corrections.md` if present or none>
- Conflicts/gaps: <contradictory sources, missing artifact, decision/approval needed, or none known>
- Next action: <one concrete action consistent with active task and handoff>
