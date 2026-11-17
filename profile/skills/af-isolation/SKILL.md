---
name: af-isolation
description: Explicitly requested isolated implementation or risky experimentation; use native OVNFS checkout, reviewed diff, per-call dry-run/integration approval, rollback planning, and authorized owned-checkout cleanup.
---

# Optional native OVNFS work

Apply shared RULES.md. This is a main-agent procedure, not another execution runtime or a security sandbox. Existing automatic task isolation/application stay disabled. Ordinary projects continue using `bin/af --cwd PROJECT` without OVNFS.

Use `af-principles` only for an actual isolation decision, such as independently verifiable experimental units or safe work while integration awaits approval. No principle authorizes application, widens checkout scope, or turns OVNFS into a security sandbox.

## Opt in and capture scope

1. Require an explicit request for isolation or obtain approval for the concrete source directory and experiment. Identify the source, native checkout name, intended change, permitted commands, verification, and retention/cleanup owner. Resolve project scripts and dependency/runtime availability first; opening an environment must not authorize provisioning.
2. Check installed `ovnfs version` and command help when the installed interface differs. No installation, update, remote `send`/`attach`, daemon-wide configuration, or unrelated checkout cleanup is implied.
3. Inspect repository policy/configuration for setup commands and source/cache/secret rules. A checkout may expose ignored files, credentials, shared caches, sockets, host processes, network, and paths outside its mount. If source policy could execute setup/install steps or reach unauthorized data, stop for a specific decision before checkout creation. Isolation is not a trust boundary.

## Create, work, inspect

With the source and name explicitly selected, use existing native commands:

```sh
ovnfs new /absolute/path/to/personal-project --name af-chosen-experiment
```

Use the path actually printed by OVNFS, not a guessed mount. Launch this same `bin/af` executable with `--cwd PRINTED_CHECKOUT_PATH`; main implements inside that path and verifies there. Advisors remain advisory; do not enable automatic task isolation or launch parallel CLI workers. Record checkout/source identity in the task/handoff. The default checkout includes current work; `--rev` deliberately changes tracked baseline and must be chosen explicitly.

```sh
ovnfs diff af-chosen-experiment
ovnfs diff af-chosen-experiment -p
```

Inspect additions/deletions, binary changes, excluded paths, changed contracts, and concurrent source edits. Complete review only when the exact intended source change and verification evidence are explained. An isolated pass is not verification of the integrated source.

## Dry-run, approval, integration

`profile/config.yml` is the settings authority: `ovnfs apply`, including `--dry-run`, is ASK, not automatic. After reviewing the diff, show the short exact command, cwd, resolved source/checkout targets, impact/risk and rollback before submitting this native per-call prompt:

```sh
ovnfs apply af-chosen-experiment --dry-run
```

Retain its actual output. Conflicts or unexpected changes block integration, not a reason to force/reset. Before real apply, present exact source/checkout, reviewed diff, dry-run result, check outcomes, known gaps and rollback plan, then obtain separate native per-call authorization. Creation and dry-run approval do not authorize real integration:

```sh
ovnfs apply af-chosen-experiment
```

Recheck if the source changed after review/dry-run. Preserve unrelated edits and get new approval for a materially changed patch. Run affected source checks after successful integration; describe unexecuted work as NOT-RUN, never completed. `--branch` changes Git branch state and needs its own explicit decision; it is not a silent fallback. `bash.gitGuard` stays true: branch/stash can refuse a shared main checkout after approval. Use reviewed operator action or explicitly opted-in private OVNFS where appropriate, never absolute Git paths, wrappers or environment bypass.

Native command display is truncated and does not infer semantics or show cwd; split/review long consequential commands before submission. Explicit prompts offer per-call Approve/Deny, not session approval. ASK fails closed without an interactive UI; keep dependent integration pending while independent safe work continues. Use operator fallback only for actual deny/guard or unavailable approval, not by default for a supported prompt. Do not reroute through eval, scripts, children or policy changes.

## Rollback and cleanup

Before integration, retain a recoverable checkpoint/backup including relevant uncommitted and untracked work using the existing approved backup/VCS process; any consequential commands require their own authorization. Preserve the exact patch and source baseline. For regression after apply, stop dependent work, compare current source with that record, prepare a targeted inverse or restore plan preserving later/user edits, and obtain native authorization for consequential execution. Blind Git reset/reverse-patch is not a rollback plan. Removing a checkout does not undo an applied change.

For abandoning an unintegrated experiment, preserve useful evidence and explicitly confirm this checkout is owned, no workers need it, and changes may be discarded. Cleanup/discard is consequential ASK, not implied by creation: show the exact `ovnfs rm NAME`, cwd, resolved checkout, impact/risk and recovery limits, then obtain native per-call authorization before removing only it. Never prune unrelated checkouts, stop the shared daemon, or delete Ghidra state. Record whether integration was applied, blocked, rejected, or NOT-RUN and whether owned cleanup completed.
