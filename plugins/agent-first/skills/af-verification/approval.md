# Authorization and native permissions

Apply `rule://agent-first-shared`. This main-agent procedure does not grant tools, classify commands into a new policy or modify OMP settings. Advisors do not execute checks or consequential actions.

## Resolve authority

1. Identify the requested effect, exact project/target, relevant user authorization and effective native permission decision. Inspect project instructions, script/lifecycle hooks, destinations, environment/account, symlinks and existing user changes. Cwd alone does not prove a Python venv, Docker endpoint, download destination or remote account.
2. Proceed with authorized routine work through available native tools. Do not add an Agent-First prompt to every ordinary operation, and do not assume YOLO if the operator configured another mode. Dependency operations, deletion and external effects follow task authority plus the operator's policies, not a plugin command matrix.
3. For a consequential action not already specifically authorized, explain the exact short command/action and cwd, resolved paths/account/ref, expected impact, data loss/network/code-execution risks and practical recovery boundary. Ask only for the material missing decision, never for repository facts inspection can establish. Commit/push require an explicit user request.
4. A user decision does not suppress any native per-call approval, restriction or guard. Submit only authorized operations through their normal tool route. If a native prompt is required but no interactive approver exists, leave the operation NOT-RUN, retain the actual refusal and continue independent work. Do not infer universal headless behavior from a particular main/child tier: inspect the actual result.

## Execution and refusal

Observe the real result and resulting state after execution; approval is not success. A rejected call is not an executed test. Respect deny, pending approval, guard, cancellation and refusal across eval, scripts, wrappers, subprocesses, aliases, executable paths, child agents and alternate tools. Never change flags, environment, settings or a tool route to perform the same refused effect.

For deletion or source integration, inventory literal targets and preserve a recoverable baseline where necessary. Ordinary authorized obsolete-file removal is implementation work, not permission to discard unrelated data. Unknown scope requires clarification before destructive effects. Native edit can remove files but has no deletion-only gate; it must not substitute for a refused destructive action. OVNFS opt-in, reviewed diff/dry-run and integration authorization follow `skill://af-isolation`.

## Native limitations

OMP resolves actual approval from tool declarations, operator/project settings and command policies. Explicit prompt/deny rules can remain effective in YOLO. Headless callers cannot answer interactive approvals; some native child/runtime tiers differ from main, so preserve actual results instead of promising automatic permission inheritance across every execution surface.

Command patterns do not prove arbitrary argv scope, secret flow, install destinations, SQL effects, production status or equivalence through code. Project isolation does not remove ambient filesystem, network, credentials or subprocess access. Behavioral rules are instructions, not enforceable OS containment. Honor stricter project/operator controls and report unavailable operations; do not edit permissions, provision a replacement runtime or claim this plugin makes untrusted code safe.
