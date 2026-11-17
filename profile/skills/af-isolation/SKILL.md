---
name: af-isolation
description: Explicitly requested isolated implementation or risky experimentation; use native OVNFS checkout, diff and dry-run review, approved operator integration, rollback planning, and owned-checkout cleanup.
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

The profile explicitly denies `ovnfs apply`, including `--dry-run`. Respect that deny. Present commands for the human to run in their own terminal; do not reroute them through eval or another tool, and do not lower the policy:

```sh
ovnfs apply af-chosen-experiment --dry-run
```

Retain its actual output. Conflicts or unexpected changes block integration, not a reason to force/reset. Before a real apply, present exact source/checkout, reviewed diff, dry-run result, check outcomes, known gaps, and rollback plan. Obtain explicit approval for this integration; approval of creating the checkout is not approval of applying it. The operator then runs:

```sh
ovnfs apply af-chosen-experiment
```

Recheck if the source changed after review/dry-run. Preserve unrelated edits and get new approval for a materially changed patch. Run the affected source checks after successful integration; describe an unexecuted operator command as NOT-RUN, never as completed. `--branch` changes Git branch state and needs its own explicit decision; it is not a silent fallback.

## Rollback and cleanup

Before integration, the operator must retain a recoverable checkpoint/backup including relevant uncommitted and untracked work using their existing approved backup/VCS process. Preserve the exact patch and source baseline. For regression after apply, stop dependent work, compare the current source with that record, prepare a targeted inverse or restore plan preserving later/user edits, and obtain approval before applying it. Blind Git reset/reverse-patch is not a rollback plan. Removing a checkout does not undo an applied change.

For abandoning an unintegrated experiment, preserve useful evidence and explicitly confirm this checkout is owned, no workers need it, and changes may be discarded; then remove only it with `ovnfs rm NAME`. Never prune unrelated checkouts, stop the shared daemon, or delete Ghidra state. Record whether integration was applied, blocked, rejected, or NOT-RUN and whether owned cleanup completed.
