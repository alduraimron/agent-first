# Project correction ledger

Template target: `.agent-first/corrections.md`. Record observed failures and validated learning, not automatic instructions. One occurrence can justify a defect fix; broad behavioral-rule promotion needs repeated independent evidence and authorized review under `af-context`.

## <correction-id>: <failure pattern>

- State: <observed | proposed | implemented-unverified | validated-local | monitored | rejected>
- Scope: <task/project/tool/model and conditions where the pattern applies>
- Pattern/impact: <observable failure mechanism and consequence>
- Occurrences: <separate dates/run or task IDs, actual evidence links, and observed outcomes; count a cascading incident once>
- Counterevidence/limits: <successful contrasting cases and what recurrence is not established>
- Root cause: <confirmed with evidence or hypothesized; separate parser/provenance defects from model compliance, schema, runtime, and approval behavior>
- Placement: <architecture | code | tooling | workflow | skill; smallest effective layer and why>
- Proposed action: <specific change and target owner, or further discriminating observation>
- Authority: <approval needed/source; no automatic policy, runtime, or instruction rewriting>
- Actual change: <path/revision or known change description, or not implemented>
- Validation plan: <falsifiable check; include prior failing case and regression scope>
- Validation evidence: <actual verification entry/result and code state, or NOT-RUN with reason; parser replay is not a new model run>
- Disposition: <what is established, which earlier failures remain failures, residual risk, and next observation/revisit condition>
- Related: <issue/task/decision and superseding correction links>
