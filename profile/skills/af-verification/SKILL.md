---
name: af-verification
description: Evidence-based verification before reporting a fix or feature complete, after an adopted design or review finding, or when runtime/browser behavior is uncertain; select existing checks, exercise real behavior, and report pass/fail/not-run with remaining gaps.
---

# Evidence-based verification

Apply the shared Agent-First RULES.md, including execution approval, child scope, browser backend, and no-install boundaries. This execution procedure is for the main agent; an advisory child may recommend checks but cannot perform them.

## Establish the verification target

Map every requested outcome and adopted design constraint to observable evidence. Read the relevant project instructions, manifests, and existing tests/scripts to select commands and prerequisites; use the repository's own convention. For a fix, include a regression that exercises the reported failure. For a feature, cover the consumer-visible happy path and the material error/boundary path, not just isolated helper behavior.

Select the smallest set of checks that covers the changed behavior and affected integration points. Include build/type/lint checks when required by the project or needed for the affected code, rather than treating a broad suite as a substitute for targeted evidence. Distinguish source inspection, automated checks, and runtime evidence in the plan. If there is no meaningful runtime behavior, record why a runtime check is not applicable.

Complete selection when every acceptance criterion has a check or an explicit reason it cannot be exercised with the installed, authorized capabilities.

## Execute and observe

1. Run the selected permitted commands in the main session, recording the exact tool arguments, working directory, exit/result status, and relevant output. Attribute each result only to that actual command: a failed inspection command is not an attempted test. Approval denied, missing dependency, timeout, and interrupted execution are not passes. Preserve failures instead of replacing them with success-shaped summaries.
2. Exercise the actual changed entry point: the CLI, API, application flow, or other consumer path. Compare the observed result to the acceptance criterion. Source text, a proposed command, a mock-only test, or a child recommendation does not establish runtime success.
3. For UI behavior, use the existing eval browser API and follow the shared Browser boundary in RULES.md. Read `xd://eval/browser` before first use. Open a dedicated named tab with explicit `app: 'tern'`, observe before interacting, exercise the changed flow, and inspect the resulting page plus relevant error/console evidence supported by Tern. Record the actual URL, action, expected and observed outcome, and screenshot/artifact reference when useful. A screenshot alone does not prove an interactive flow works; a backend limitation is an evidence gap, not permission to switch or install.
4. Diagnose failed checks, make the relevant main-agent correction, and repeat the affected checks when code or conditions change. Resolve reviewer findings with the same evidence standard. Distinguish a known unrelated failure from a pass and explain the evidence for that distinction.
5. Release only resources created for this task, preserving useful evidence before disposable workspace cleanup. Stop once the acceptance criteria are covered; do not add unrelated audits.

A check completes only when its real result is available. If a required check cannot run, finish independent reachable work and retain that check as unverified with its precise blocker.

## Final evidence report

Keep the handoff concise but include each field, using `none` or `not applicable` with a reason when appropriate:

- **Changed**: implemented behavior and important affected paths.
- **Checks**: actual commands and working directory with `PASS`, `FAIL`, or `NOT-RUN`, plus relevant observed output. Separate commands submitted to a tool from commands merely requested or planned. For NOT-RUN, label an unsubmitted command as proposed and state the blocker; a refusal of a different command does not establish its execution or refusal.
- **Runtime evidence**: entry point or browser flow exercised, expected versus observed behavior, and useful artifact references. Separate this from source-only evidence.
- **Unverified requirements**: uncovered acceptance criteria, blocked checks, and any source-only conclusions.
- **Remaining risks**: unresolved failures, assumptions, compatibility/security concerns, or environmental limitations; do not hide them behind a general claim of completion.

Claim completion only for outcomes supported by the evidence. When required behavior remains unverified, state that limitation directly rather than calling the implementation fully verified.
