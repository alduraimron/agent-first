# Disposable OVNFS evaluation

Run in an operator terminal with an existing OVNFS installation. Do not invoke this procedure inside `agent-first` as a way around its explicit apply deny. No install, shared daemon reconfiguration, remote checkout transport, or team/production folder is authorized.

1. Create a new temporary personal folder containing one known text fixture. Initialize a local Git repository if testing Git handling; do not clone or copy a real project. Record exact source path and original contents.
2. Inspect `ovnfs config list` and `ovnfs plan SOURCE` for setup/provisioning, transfer and cache behavior. Stop before creation if any unauthorized setup or secret exposure is possible. The installed `ovnfs version` identifies the tested interface.
3. Run `ovnfs --json new SOURCE --name UNIQUE_OWNED_NAME` and use the returned path. Change only the fixture inside that checkout. Verify the original source remains unchanged.
4. Capture `ovnfs diff NAME -p`. From the operator terminal, run `ovnfs apply NAME --dry-run`; retain exit/output and verify the source is still unchanged. Conflicts block integration.
5. Present source, name, exact reviewed patch, dry-run result and rollback/cleanup scope for explicit approval. If declined, record integration NOT-RUN and retain or separately approve cleanup. Approval to create a checkout is not apply approval.
6. Only after approval, run `ovnfs apply NAME`; inspect the actual source contents and run its meaningful check. Record PASS only on observed results.
7. In this disposable fixture, an approved targeted restore of the one original text file demonstrates the recorded inverse; verify it. For real projects preserve uncommitted/untracked state, review overlap with subsequent edits and follow af-isolation's separate restore approval.
8. After evidence is retained and no worker uses the owned checkout, remove only it using `ovnfs rm NAME`, then remove only the owned temporary source if authorized. Verify ownership/paths; never prune unrelated state or treat checkout removal as undoing apply.

The executed full-implementation probe used OVNFS 0.7.0 and explicit user approval for one disposable file's apply/restore/cleanup. Its preparation, dry-run, actual apply, restoration and cleanup records are in private `results/ovnfs-m5zrwt0s/`; portable results appear in full-validation.md. Normal profile auto-isolation/application and apply deny were not changed. This proves that local fixture lifecycle, not OS containment or conflict handling for arbitrary repositories.
