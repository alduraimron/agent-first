# Bug investigation

## Entry and inputs
Use for unexpected behavior whose cause is uncertain. Require reported observation, expected behavior, available failing evidence, affected environment/revision, and whether the request authorizes a fix or diagnosis only.

## Steps and decision points
1. Load `skill://af-testing`. Treat user-reported failures as evidence; inspect the failing path and existing diagnostics rather than rerunning merely to confirm the report.
2. Separate observations from hypotheses. Trace input, state transitions, dependencies, and the first divergence from the expected invariant.
3. Select a discriminating inspection or focused experiment for the leading hypothesis. Update the causal explanation from actual results; investigate upstream causes rather than patching symptoms.
4. For diagnosis-only requests, return the supported cause, uncertainty, and recommended next check without edits. For authorized fixes, define a regression criterion and implement the smallest causal correction.
5. Reassess architecture explicitly: a local correction preserving a boundary stays here; a boundary/design change routes architecture-impacting before implementation.

## Consultation
Use the relevant domain advisor when evidence exposes a material unresolved question. Bundled reviewer is conditional on a concrete subtle-risk question; follow router protocol.

## Verification
Use `skill://af-verification` for a focused regression and adjacent boundary/failure checks; recommend existing scripts and af-testing's minimal reproducer design.

## Exit
The causal chain is evidence-backed, authorized remediation is complete when requested, and regression evidence or exact uncertainty is reported.

## Failure and escalation
When evidence is insufficient, state which hypotheses remain and the smallest missing observation. Do not claim a root cause from correlation or bypass access barriers to obtain diagnostics. Record unresolved issues through af-context when continuation requires durable state.
