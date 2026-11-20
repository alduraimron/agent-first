---
name: af-verification
description: Evidence-based verification of fixes, features, designs, reviews, runtime/browser behavior and measurements; select installed project checks and report PASS, FAIL, NOT-RUN or NOT-APPLICABLE with evidence and remaining gaps.
---

# Evidence-based verification

Apply `rule://agent-first-shared`. Main executes checks; advisors only recommend them. Consult `approval.md` when authorization or native gates apply, `checks.md` for boundary-specific checks and `browser.md` before Tern flows.

## Mandatory pre-report principle gate

Before **any** engineering completion, verification-only or blocked-check report:
1. `read` `skill://af-principles` (if not already read).
2. `read` `skill://principle-prove-it-works` **in full** (if not already read).
3. Load additional triggered leaves only when relevant (e.g., `test-behavior-not-implementation` for test oracles, `explain-the-number` for measurements).

## Select and execute checks

1. **Map criteria to smallest falsifying checks:** Inspect manifests, tests and CI; prefer installed project commands. Use existing user reports/failing tests as repro—do not rerun unchanged failures just to confirm them. Add a regression only when current coverage misses the consumer-visible bug.
2. **Run finite checks cleanly:** Execute permitted commands in main and record exact args, cwd, exit/status and key output. Finite commands must **not** pass service `name` or `ready` metadata (service readiness is not test completion). Pre-execution argument errors, denials, timeouts and missing dependencies are `NOT-RUN`, never `PASS` or `FAIL`.
3. **Exercise the real boundary:** Run the actual changed CLI, API or UI flow—source reads, proposed commands, mock-only tests and advisor reports do not prove runtime behavior. For UI, follow `browser.md` with actual Tern backend and owned tab/runtime; never manufacture page state.
4. **Fix, recheck and clean up:** Re-run affected checks after edits or reviewer-driven fixes. Separate known unrelated failures from passes with evidence. Stop/close only resources created for this task (retaining artifacts first), then stop once acceptance criteria are covered. If a required check is blocked, finish independent reachable work and report the exact blocker.

## Outcome semantics

- **PASS:** Actual relevant check completed successfully on the current code/input/environment.
- **FAIL:** Executed check failed its expectation; preserve the failure separately from any later passing rerun.
- **NOT-RUN:** Required/proposed check was unavailable, denied, interrupted, unsupported or unsubmitted; state why.
- **NOT-APPLICABLE:** No relevant target for this task with a concrete reason (missing tools or denials are `NOT-RUN`, not `NOT-APPLICABLE`).

Scope every `PASS` strictly to the exercised boundary.

## Final evidence report

Keep the report concise and include all five fields (`none` or `not applicable` with reason where appropriate). If this report is the **first visible prose**, begin with the exact kebab-case `Workflow: <route>` literal from `af-engineering` plus rationale:

- **Changed:** Implemented behavior and key affected paths.
- **Checks:** Exact commands, cwd, status (`PASS`/`FAIL`/`NOT-RUN`/`NOT-APPLICABLE`) and key output. Keep planned, attempted, rejected-before-execution and completed runs distinct; tie evidence to current code state.
- **Runtime evidence:** Consumer entry point or browser flow exercised, expected vs observed output and artifact paths (distinct from source inspection).
- **Unverified requirements:** Uncovered criteria, blocked checks and source-only conclusions.
- **Remaining risks:** Unresolved failures, assumptions, compatibility/security/environment limits and pending approvals. Update `.agent-first/` via `skill://af-context` only when durable records matter.

Claim completion only for outcomes directly supported by evidence.
