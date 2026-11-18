# Minimal risk-based approval

This is a main-agent procedure under shared RULES.md. Advisors never execute consequential operations. `profile/config.yml` owns the actual native policies; this procedure does not grant permission or replace a native gate.

## Classify the effect, not its spelling

1. Apply RULES.md's AUTO/ASK/DENY boundary to the actual effect, target and data, not the command name alone. Task-required project dependencies, downloads, pinned project runners and ordinary local Docker/Git work are AUTO within verified scope. Normal commit/push still require an explicit user request, not another routine approval popup.
2. Verify workspace destinations, package lifecycle hooks, Python venv identity, Docker endpoint and volume ownership before acting. Cwd alone does not establish those targets. Project dependency autonomy is not authorization for global tooling, unrelated analysis/browser/runtime provisioning, remote deployment, credential transmission or unknown external effects.
3. For high-risk ASK, inspect the relevant diff/data inventory/infrastructure plan/OVNFS patch and identify exact account/environment and recoverable state. Destructive Git, recursive/mass/data deletion, global/system/privileged effects, remote/cloud/publication and source integration stay protected.
4. Refuse DENY effects before submission: unscopable system/disk destruction, force/destructive remote history in any spelling, credential exfiltration, permission bypass and unauthorized protected configuration changes. Existing native denies remain absolute. Unknown high-risk scope or an effect without a reliable native gate stays operator-only.

## Present then request

For an ASK effect, before the tool call show the developer:

- The exact short command and cwd, without secrets in arguments or output.
- Resolved literal targets, selected remote/ref, account/environment or integration source as applicable.
- Expected changes, potential data loss/network transfer/code execution and other material risks.
- A practical recovery/rollback boundary, or state that the effect cannot be undone.

Then submit the operation through its supported native prompt. In interactive OMP, explicit prompt rules ask for this invocation only; no cached/session-wide answer is offered. Task/chat authorization does not suppress the native per-call gate. Never manufacture approval by altering flags, settings, environment, tool route or command spelling.

OMP 18.22.0's bash prompt displays the tool, matched-policy reason and command. It does not infer semantic impact or include cwd, and long commands are truncated to 2,000 characters. The pre-submit explanation is necessary context, not an assertion that native UI computes risk. Keep consequential commands short enough to review completely; separate genuinely independent operations rather than hiding effects in compound lines, heredocs or scripts.

After the actual answer, check the real tool result and resulting state. Approval is not completion. A denial, unavailable headless approver, cancellation, timeout or independent native Git-guard refusal leaves that action NOT-RUN. Preserve the refusal, stop dependent effects and finish genuinely independent permitted work. Do not repeat a rejected operation through eval, scripts, subprocesses, aliases, an absolute executable path, children or another interface.

## Deletion and configuration scope

Inventory intended paths, resolve them and their ancestors, and inspect symlinks, ownership and user changes before deleting. Authorized ordinary single-file removals and empty-directory cleanup are AUTO, not mandatory prompts. For valuable data loss, recursive/mass removal or persistent-volume deletion, retain a recoverable baseline and submit the relevant native ASK operation. Use literal project-relative operands and an explicit cwd; refuse unknown scope, globs/substitutions or protected targets. Existing absolute/parent/home/variable deny patterns remain unchanged.

Native `edit` treats file removal and content updates as the same write tier, so ordinary authorized obsolete-file cleanup can use it. It cannot grant approval for a high-risk loss effect. Never use edit REM, eval, wrappers, scripts or a different command spelling to replace an actual ASK/DENY/guard refusal.

Native `*` command patterns cannot express a literal-star-only restriction, prove arbitrary argv containment or inspect every Git flag cluster/refspec, alias, script or subprocess. Known dangerous spellings have explicit denies; the semantic refusal above remains binding for equivalent forms. Protected-folder gates resolve path-tool symlinks, but shell/eval/browser check cwd rather than embedded paths. Active profile assets can resolve through symlinks outside configured roots. Unauthorized configuration modification, credential extraction/transmission and code-based equivalents are forbidden, not claimed to be structurally contained.

## Remaining native restrictions

- Keep `bash.gitGuard` enabled. Shared/main checkouts may refuse branch moves, stash or resets even after permission. Offer a reviewed operator action or separately approved private OVNFS workflow; never disable the guard or use another Git executable/route.
- Coarse native families such as checkout/restore/rebase, SSH/cloud clients, global tooling and privilege/service management can still prompt harmless variants. The command glob cannot distinguish every destructive path, install destination or production target. Ordinary branch switching, project installs/downloads and owned Docker development are not inherently ASK; all remain subject to actual scope and guards.
- Project installation may run lifecycle scripts with ambient authority. Inspect manifest/lockfile/bootstrap effects and install only dependencies needed for the authorized task in its verified project/venv target. A bare pip command or Docker executable is not target proof. Unscoped/global targets and new tools/runtimes/analysis/browser engines require the supported high-risk approval path; unsupported denied backends remain unavailable.
- Known recursive flags have native prompts, but `*` matching does not recognize every combined flag, Git alias, subprocess or SQL program. Scope-sensitive high-risk effects with no supported native per-operation gate remain operator-only. Do not manufacture a prompt or use automatic code/internal helpers to replace a gated operation.
- Prompts and behavioral rules are not filesystem, process, credential or network isolation. Use trusted personal projects; hostile-code containment needs a separate architecture decision.
