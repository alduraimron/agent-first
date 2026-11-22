---
name: af-isolation
description: Explicitly requested isolated work using existing OVNFS; review diff and dry-run, obtain source-integration authorization, plan rollback and clean up only owned checkouts.
---

# Optional native OVNFS work

Apply `rule://agent-first-shared` and effective native permissions. This is a main-agent procedure, not another runtime or security sandbox. The plugin changes no isolation settings and never requests automatic application. Ordinary work starts with `omp` in the project.

Use `af-principles` only for an actual isolation decision, such as independently verifiable experimental units or safe work while integration awaits approval. No principle authorizes application, widens checkout scope, or turns OVNFS into a security sandbox.

## Opt in and capture scope

1. Require explicit isolation opt-in for the concrete source and experiment. Identify source, checkout name, intended change, permitted commands, verification and retention/cleanup owner. Resolve project scripts and runtime availability; task-required setup follows effective native permissions and user-authorized scope.
2. Check installed `ovnfs version` and command help when the installed interface differs. No installation, update, remote `send`/`attach`, daemon-wide configuration, or unrelated checkout cleanup is implied.
3. Inspect setup scripts and source/cache/secret rules. A checkout may expose ignored files, credentials, shared caches, sockets, host processes, network and outside paths. Resolve unknown setup effects before checkout creation; no global or unrelated provisioning is implied. Isolation is not a trust boundary.

## Create, work, inspect

With the source and name explicitly selected, use existing native commands:

```sh
ovnfs new /absolute/path/to/personal-project --name af-chosen-experiment
```

Use the actual printed checkout path, not a guessed mount. Run ordinary `omp --cwd PRINTED_CHECKOUT_PATH` there; the copied project-scoped plugin registration must resolve to its installed cache, so verify discovery before work. Main owns verification. Any explicitly delegated implementation uses the engineering workflow and native `task`, not parallel CLI workers or changes to operator isolation settings. Record checkout/source identity. The default checkout includes current work; select `--rev` explicitly when changing the tracked baseline.

```sh
ovnfs diff af-chosen-experiment
ovnfs diff af-chosen-experiment -p
```

Inspect additions/deletions, binary changes, excluded paths, changed contracts, and concurrent source edits. Complete review only when the exact intended source change and verification evidence are explained. An isolated pass is not verification of the integrated source.

## Dry-run, approval, integration

After reviewing the diff, explain the exact cwd, source/checkout targets, impact, risks and rollback. Use effective native permissions for a non-integrating preview; no custom Agent-First command policy is installed:

```sh
ovnfs apply af-chosen-experiment --dry-run
```

Retain actual output. Conflicts or unexpected changes block integration, not a reason to force/reset. Before real apply, present the exact source/checkout, reviewed diff, dry-run result, check outcomes, gaps and rollback plan; obtain explicit user authorization for this integration and honor any additional native prompt. Creation and dry-run do not authorize real integration:

```sh
ovnfs apply af-chosen-experiment
```

Recheck if source changed after review/dry-run. Preserve unrelated edits and obtain a new decision for materially changed patches. Run affected source checks after successful integration; unexecuted work stays NOT-RUN. `--branch` changes Git state and needs explicit task authority, not silent fallback. Honor native guards and stricter operator settings without disabling or bypassing them.

Explain consequential commands completely before submission. Native prompt details and headless refusal depend on operator settings; the plugin does not install an apply gate. If required authorization is unavailable, keep integration pending and finish independent safe work. Never reroute an actual refusal through eval, scripts, children or changed settings.

## Rollback and cleanup

Before integration, retain a recoverable checkpoint/backup including relevant uncommitted and untracked work using the existing approved backup/VCS process; any consequential commands require their own authorization. Preserve the exact patch and source baseline. For regression after apply, stop dependent work, compare current source with that record, prepare a targeted inverse or restore plan preserving later/user edits, and obtain native authorization for consequential execution. Blind Git reset/reverse-patch is not a rollback plan. Removing a checkout does not undo an applied change.

For abandoning an unintegrated experiment, preserve useful evidence and confirm this checkout is owned, unused and authorized for discard. Explain the exact `ovnfs rm NAME`, cwd, resolved checkout, impact/risk and recovery limit before authorized removal; honor native approval if configured. Creation does not authorize discard. Never prune unrelated checkouts or stop the shared daemon. Record whether integration and owned cleanup actually occurred or remain NOT-RUN.
