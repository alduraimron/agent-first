# Verification history

Template target: `.agent-first/verification.md`. Append entries; preserve prior failures and superseded observations. Outcome meanings and execution procedure come from `af-verification`. A historical PASS does not establish current applicability. Leave planned checks in task/decision records unless explicitly recording why required execution is NOT-RUN or NOT-APPLICABLE.

## <evidence-id>: <check name>

- Recorded: <date, session/person>
- Task/acceptance: <relative task link and AC IDs>
- Kind/performer: <main command | independent acceptance | project tests | browser | advisory inspection | other; actual actor/native child ID where relevant>
- Code state: <known revision plus relevant working-state description, last relevant edit, or unknown>
- Environment/inputs: <relevant runtime, configuration, data/workload; do not store secrets>
- Exact command/action: <literal command and arguments, or actual browser/tool observation/action sequence; say not attempted where applicable>
- Cwd/target: <actual working directory or authorized target>
- Execution: <executed | rejected-before-execution | not-attempted; describe actual tool/error result>
- Outcome: <PASS | FAIL | NOT-RUN | NOT-APPLICABLE; select from actual evidence, never prefill success>
- Exit/error: <actual exit code/tool error, or unavailable/not applicable with reason>
- Evidence: <retained result/artifact path or native result reference; unavailable if not retained; no invented links>
- Observed result: <what the tool actually established; distinguish output from interpretation>
- Coverage/limits: <which requirements/cases this covers and what it does not>
- Applicability: <applicable-to-described-state | historical-only | unresolved, with reason and any later entry link>
- Next check: <remaining action or none justified by evidence>

## <correction-entry-id>: correction to <earlier evidence-id>

<Append only when needed. Identify the erroneous attribution/outcome, actual evidence and reason, corrected interpretation, date/owner, and affected acceptance claims. Retain the original entry; a corrected parser interpretation is not a new model execution.>
