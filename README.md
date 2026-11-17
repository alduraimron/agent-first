# Agent-First OMP: Phase 1

A personal, explicitly activated OMP profile. Native OMP remains the orchestrator: the main agent selects a workflow, consults advisory specialists only when justified, implements changes itself, and reports verification evidence. No extension, MCP server, Tern plugin, or parallel orchestration runtime is added.

## Files

```text
bin/af
profile/config.yml
profile/APPEND_SYSTEM.md
profile/RULES.md
profile/agents/af-architect.md
profile/skills/af-engineering/SKILL.md
profile/skills/af-verification/SKILL.md
eval/cases.json
eval/config.yml
eval/run.py
eval/README.md
eval/validation.md
README.md
.gitignore
```

Generated `eval/results/` artifacts are private and gitignored. Authentication, sessions, and caches stay in the native named-profile state, outside this repository.

## Activate and run

Prerequisites: installed OMP 18.22.0, Python 3.9+, Node 18+ and Git for the evaluations, and Tern for browser verification. The launcher installs nothing.

```sh
./bin/af --activate
./bin/af --cwd /absolute/path/to/personal-project --model PROVIDER/MODEL
./bin/af --cwd /absolute/path/to/personal-project --model PROVIDER/MODEL "Implement the requested behavior"
```

Replace `PROVIDER/MODEL` with an authorized native OMP selector. Authenticate separately using OMP's native login in this profile, for example `omp --profile agent-first login`. The launcher does not copy credentials. During implementation, one existing `opencode-go` API credential was transferred using native auth export/import into this profile only; OAuth and MCP credentials were not copied.

`--activate` registers symlinks for the five authored profile assets under `~/.omp/profiles/agent-first/agent/`. Existing entries pointing elsewhere are refused, not overwritten. Keep this checkout at a stable location. Native persistent settings writes can update the linked personal `profile/config.yml`; review those changes like other configuration edits.

Use `bin/af`, not just `omp --profile agent-first`, for the complete activation boundary. The launcher forces the named profile, base overlay, appended contract, non-yolo approval mode, and disabled extension discovery. It clears inherited profile-directory/config-overlay hints and does not forward arbitrary native flags, subcommands, alternate profiles, or safety-lowering options. Custom `PI_CONFIG_DIR` roots require a deliberate separate setup and are refused here.

Only select personal projects. This setup does not edit any target repository configuration. Project instruction files remain relevant; native profile isolation is not a universal configuration or filesystem sandbox. To avoid additive execution capabilities or agent shadowing, the launcher refuses native project tools and project agent definitions, and refuses unexpected personal-profile tools/MCP files. Other foreign discovery providers and project MCP loading are disabled by the profile.

### Sessions and headless runs

```sh
./bin/af --cwd /absolute/path/to/personal-project --continue
./bin/af --cwd /absolute/path/to/personal-project --resume PERSONAL_SESSION_ID
./bin/af --cwd /absolute/path/to/personal-project --model PROVIDER/MODEL --json --max-time 5m --max-cost 1 "Inspect this project"
```

Resume file paths must already exist inside the personal profile. `--json` implies native print mode and waits for this run's asynchronous work. Headless execution does not grant approval: ordinary shell, eval, and task calls requiring confirmation fail closed without an interactive UI. Use the interactive launcher for normal implementation approvals. The evaluation harness has separate, narrowly scoped grants for its synthetic projects.

## Agent-driven behavior

Users describe outcomes, not slash-command workflows. `af-engineering` selects and announces the smallest adequate route from project evidence:

- Quick Change: Inspect -> Modify -> Verify, without delegation for trivial work.
- Feature Development: Understand -> Plan -> Implement -> Verify.
- Architecture-Impacting Change: Inspect -> Consult `af-architect` -> Evaluate trade-offs -> Approval when required -> Implement -> Verify.

The route can change when inspection reveals new risk. The architect returns facts, assumptions, recommendations, enforceable constraints, and proposed checks. It has only native `read`, `grep`, and `glob` tools and no spawn permission. The main agent evaluates the advice and implements the chosen approach.

The bundled `reviewer` is reused without a replacement definition. Independent review is conditional on concrete risk, not required for every task. The main agent supplies the actual patch and context; children do not execute checks. Native structured task output is enabled for the reviewer's yield contract. Concurrency is capped at two and recursion at one level.

Shared requirements live in `RULES.md`: native task children do not inherit the main append text or `AGENTS.md`. `af-verification` owns the completion report: actual commands/cwd, pass/fail/not-run, runtime evidence, unverified requirements, and remaining risks. Child opinions and screenshots alone are not proof that a change works.

## Safety policy

- Main approval mode is `write`, not yolo. Shell, eval, and task dispatch require interactive approval unless a more specific operator policy permits them.
- Explicit denies cover commits/pushes, destructive Git/file commands, privilege escalation, package installers, transient package execution, remote shell downloads, and OVNFS apply. Native commit/checkpoint helpers are disabled. Chat instructions do not override a deny.
- Headless children use native yolo tier handling, but explicit prompts and denies still fail closed. The architect's tool list, the reviewer's scoped assignment, shared rules, and observed child activity all matter; a parent task grant is not unrestricted child authority.
- Automatic OVNFS isolation and automatic application are both disabled. No checkout, merge, or cleanup from the earlier Ghidra incident is performed.
- Disassembler backend is `none`; binary analysis and desktop control are outside Phase 1. LSP startup, Python eval, managed eval provisioning, automatic memory capture, and extension discovery are disabled to avoid implicit tooling/provisioning paths. Use installed project checks; enable additional tooling only after a separate policy decision.
- Browser work is main-only through the existing eval browser API with explicit `app: 'tern'`. Read its API guidance, observe and exercise the real page, retain evidence, and close only owned tabs. Do not silently fall back or download a browser when Tern is unavailable.
- Approval patterns do not govern arbitrary code inside an approved eval or shell. They are not OS containment. Only approve code and project scripts you trust. Neither this profile nor its tests establish safety for hostile repositories.

## Evaluate

See [the evaluation procedure](eval/README.md) and [the executed validation record](eval/validation.md). The record distinguishes successful checks, retained failures, and unverified requirements.

```sh
python3 -B eval/run.py --model PROVIDER/MODEL --max-time 600 --max-cost 1.5
```

The runner creates fresh synthetic Git projects, stages initial files without committing, and runs three native OMP cases. Expected routes stay outside the user prompts. It checks actual delegation/tool journals and independent consumer behavior, retains failed runs, and exits nonzero on failure. Evaluation-only grants allow parent advisory tasks and exact test/diff commands; general eval and other shell commands are denied. Synchronous evaluation task settlement is explicitly recorded and does not change normal profile async behavior.

Read retained advice and review disposition as well as automated scores: consultation chronology cannot establish reasoning quality. Artifacts may include synthetic source, model usage, and pseudonymous session/account metadata. Review them before sharing.

Executed results: all three routing scenarios passed across the recorded runs, including actual implementation and independent consumer checks. The architecture scenario used the custom architect and native bundled reviewer. Earlier failed batches and recovered tool errors remain documented; this is not a claim of error-free or deterministic model behavior.

## Known limits and Phase 2 recommendations

- OMP/Tern versions are independently managed and may change. Revalidate the relevant native interfaces after upgrades; the discovery report observed background OVNFS version drift.
- Tern WebKit lacks full Chromium/CDP parity. Report unsupported tracing, network, emulation, or platform behavior as gaps rather than switching or installing automatically.
- Profile isolation retains project instructions and OMP's documented keybinding inheritance. It does not isolate host processes, network access, or all ambient filesystem paths.
- Native bundled reviewer tool metadata is broader than the advisory policy. Normal headless exec prompts reject it; evaluation checks also flag attempted non-advisory tools. This is not a security boundary against a malicious model or project.
- Evaluation grants are deliberately limited to synthetic projects. They must not be reused as a production approval policy. Generated tests themselves are executable code.

Phase 2 candidates, not implemented: expand real-task benchmarks and human reasoning assessment; investigate model/provider reliability from retained failures; evaluate explicitly approved, manual-apply OVNFS use; and separately design OS containment or deterministic policy gates if an actual requirement justifies them. Add specialists only when repeated evidence warrants them.
