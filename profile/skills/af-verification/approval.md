# Ask when needed

This is a main-agent procedure under shared RULES.md. Advisors never execute consequential operations. `profile/config.yml` owns the actual native policies; this procedure does not grant permission or replace a native gate.

## Classify the effect, not its spelling

1. Inspect the intended operation, arguments, invoked script and current project context. Ordinary trusted workspace edits/checks, owned servers/debugging, read-only consultation and authorized Tern verification remain AUTO. A task's desired outcome does not authorize installation, publication, deployment or expanded access.
2. For a reviewable ASK effect, identify the exact workspace/account/environment and current state. Read relevant package scripts, manifests, diffs, Docker context, infrastructure plan or OVNFS patch before requesting execution. Package lifecycle hooks, test bootstraps and downloaded code can execute more than the visible command.
3. Refuse DENY effects before submission: unscopable system/disk destruction, force push or destructive remote history in any flag/refspec/alias spelling, credential exfiltration, control bypass and unauthorized protected configuration changes. Unknown consequential scope is not a reason to request blanket approval. Native denies stay absolute after user authorization.

## Present then request

Before the tool call, show the developer:

- The exact short command and cwd, without secrets in arguments or output.
- Resolved literal targets, selected remote/ref, account/environment or integration source as applicable.
- Expected changes, potential data loss/network transfer/code execution and other material risks.
- A practical recovery/rollback boundary, or state that the effect cannot be undone.

Then submit the operation through its supported native prompt. In interactive OMP, explicit prompt rules ask for this invocation only; no cached/session-wide answer is offered. Task/chat authorization does not suppress the native per-call gate. Never manufacture approval by altering flags, settings, environment, tool route or command spelling.

OMP 18.22.0's bash prompt displays the tool, matched-policy reason and command. It does not infer semantic impact or include cwd, and long commands are truncated to 2,000 characters. The pre-submit explanation is necessary context, not an assertion that native UI computes risk. Keep consequential commands short enough to review completely; separate genuinely independent operations rather than hiding effects in compound lines, heredocs or scripts.

After the actual answer, check the real tool result and resulting state. Approval is not completion. A denial, unavailable headless approver, cancellation, timeout or independent native Git-guard refusal leaves that action NOT-RUN. Preserve the refusal, stop dependent effects and finish genuinely independent permitted work. Do not repeat a rejected operation through eval, scripts, subprocesses, aliases, an absolute executable path, children or another interface.

## Deletion and configuration scope

For whole-file/directory deletion, inventory the exact intended paths, resolve them and their ancestors within the selected workspace, inspect symlinks, ownership and current changes, and establish that no protected or unrelated work is included. Use literal relative operands with an explicit cwd and native `rm`/`rmdir`/`unlink` approval. Refuse unknown scope, globs, variable/substitution targets, parent/home/absolute escapes and recursive system targets. Preserve a recoverable baseline where deletion can lose work.

Normal content-line removal remains an ordinary edit. Native local `edit` treats both content updates and whole-file removal as write-tier: it cannot prompt only for removal while leaving content edits AUTO. Never use edit removal operations or arbitrary code to avoid the deletion gate.

Native `*` command patterns cannot express a literal-star-only restriction, prove arbitrary argv containment or inspect every Git flag cluster/refspec, alias, script or subprocess. Known dangerous spellings have explicit denies; the semantic refusal above remains binding for equivalent forms. Protected-folder gates resolve path-tool symlinks, but shell/eval/browser check cwd rather than embedded paths. Active profile assets can resolve through symlinks outside configured roots. Unauthorized configuration modification, credential extraction/transmission and code-based equivalents are forbidden, not claimed to be structurally contained.

## Remaining native restrictions

- Keep `bash.gitGuard` enabled. Shared/main checkouts may refuse branch moves, stash or resets even after permission. Offer a reviewed operator action or separately approved private OVNFS workflow; never disable the guard or use another Git executable/route.
- Provision-capable runners and coarse network/cloud command families can still prompt for apparently harmless variants. Prefer an already-installed independent check when it has no denied consequential effect; do not use it to reproduce a refused download, installation or transfer.
- Unsupported analysis/authentication/key/control surfaces and raw disk/erasure/host-wide destructive tools remain denied. Routine debugging with installed project commands is not permission to provision a new backend.
- If an unmatched consequential script/helper has no supported native per-operation gate, leave that effect operator-only. Do not use automatic eval or internal helpers to replace a gated Git, installation, transfer or integration operation.
- Prompts and behavioral rules are not filesystem, process, credential or network isolation. Use trusted personal projects; hostile-code containment needs a separate architecture decision.
