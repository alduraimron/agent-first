---
name: af-verification
description: Evidence-based verification of fixes, features, designs, reviews, runtime/browser behavior and measurements; select installed project checks and report PASS, FAIL, NOT-RUN or NOT-APPLICABLE with evidence and remaining gaps.
---

# Evidence-based verification

Apply the shared Agent-First RULES.md, including scoped autonomy, point-of-risk authorization, explicit native prompts/denies, child scope, browser backend, and no-install boundaries. This execution procedure is for the main agent; an advisory child may recommend checks but cannot perform them.

Read `skill://af-principles` if not already read, including verification-only or denied-check requests. Before a completion or blocked-check report, read `skill://principle-prove-it-works` in full unless already read. Select other triggered lenses through the selector, such as behavior-not-implementation for test oracles and explain-the-number for quantitative claims. Leaves guide the evidence decision; this skill remains the verification and final-report procedure.

## Establish the verification target

Map every acceptance criterion and adopted constraint to observable evidence. Inspect project instructions, manifests, tests and CI; use installed project tools and existing conventions. Consult `checks.md` for the relevant static/type/lint/build, testing/debugging, API/database, security, performance, and deployment branches. For UI work, use `browser.md` before the actual Tern flow. Load the matching engineering skill when domain uncertainty affects check design.

Select the smallest set covering the change and affected consumer path. Existing failure/user reports are repro evidence, not a reason to rerun unchanged failures. Add a regression only when current coverage misses the consumer-visible bug. Separate source inspection from runtime/measurement proof; identify any required but unavailable check before execution.

Complete selection when every acceptance criterion has a check or an explicit reason it cannot be exercised with the installed, authorized capabilities.

## Execute and observe

1. Run the selected permitted commands in the main session, recording the exact tool arguments, working directory, exit/result status, and relevant output. Finite checks use ordinary execution without service `name` or `ready` metadata; service readiness is not test completion. Attribute each result only to that actual command: a pre-execution argument error or failed inspection is not an executed test. Approval denied, missing dependency, timeout, and interrupted execution are not passes. Preserve failures instead of replacing them with success-shaped summaries.
2. Exercise the actual changed entry point: the CLI, API, application flow, or other consumer path. Compare the observed result to the acceptance criterion. Source text, a proposed command, a mock-only test, or a child recommendation does not establish runtime success.
3. For UI behavior follow `browser.md` and the shared browser boundary: actual Tern backend, owned tab/runtime, observe/action/result, relevant keyboard/accessibility/error evidence and screenshot. Scripts may inspect the page, not manufacture successful state. State unsupported/manual checks as gaps.
4. Diagnose failed checks, make the relevant main-agent correction, and repeat the affected checks when code or conditions change. Resolve reviewer findings with the same evidence standard. Distinguish a known unrelated failure from a pass and explain the evidence for that distinction.
5. Release only resources created for this task, preserving useful evidence before disposable workspace cleanup. Stop once the acceptance criteria are covered; do not add unrelated audits.

A check completes only when its real result is available. If a required check cannot run, finish independent reachable work and retain that check as unverified with its precise blocker.

## Outcome semantics

- **PASS**: the actual relevant check completed successfully on the recorded source/input/environment.
- **FAIL**: an executed check failed its expectation; preserve the error and any later corrected result separately.
- **NOT-RUN**: a required/proposed check was unavailable, denied, interrupted, unsupported, or never submitted; explain which and why.
- **NOT-APPLICABLE**: a check has no relevant target for this task; give a concrete reason. Missing tools or a denied check are not this status.

Use explicit outcomes for relevant categories, including static/types/lint/build, unit/integration, API/database, security, performance, and browser/accessibility. Do not invent irrelevant work to fill a checklist. Scope a PASS to the exercised boundary, not the whole application or accessibility/security compliance.

## Final evidence report

Keep the handoff concise but include each field, using `none` or `not applicable` with a reason when appropriate. If this report is the first visible prose, begin with `af-engineering`'s selected row's exact route prefix and rationale before these fields.

- **Changed**: implemented behavior and important affected paths.
- **Checks**: actual commands and cwd with PASS, FAIL, NOT-RUN, or NOT-APPLICABLE and useful observed output. Record planned/attempted/completed separately; a refusal of a different command does not establish test execution. Tie evidence to task/source state; invalidated historical results are not current passes.
- **Runtime evidence**: entry point or browser flow exercised, expected versus observed behavior, and useful artifact references. Separate this from source-only evidence.
- **Unverified requirements**: uncovered acceptance criteria, blocked checks, and any source-only conclusions.
- **Remaining risks**: unresolved failures, assumptions, compatibility/security concerns, environmental limitations, and any required approval; do not hide them behind a general claim of completion. Update the task/handoff and applicable evidence/issues records using `af-context`; record a repeated correction pattern with actual validation rather than silently changing global policy.

Claim completion only for outcomes supported by the evidence. When required behavior remains unverified, state that limitation directly rather than calling the implementation fully verified.
