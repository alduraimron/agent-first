# Skills catalog

Agent-First 2.0.0 preserves eleven domain/support skills, two selectors, 24 principle leaves and 20 interaction leaves: **57 native registry entries, 13 visible catalog entries and 44 hidden-but-readable leaves**. Use ordinary `omp` in a project with `agent-first@agent-first` installed at project scope, then ask naturally.

For engineering execution, the path is **workflow -> relevant domain procedure -> relevant principles -> main implementation and checks**. `af-engineering` owns workflow/domain routing; the [principle selector](../plugins/agent-first/skills/af-principles/SKILL.md) refines decision judgment, while the [interaction selector](../plugins/agent-first/skills/af-interaction/SKILL.md) owns explanations, discovery and communication. Summaries here are pointers, not replacement procedures or mandatory checklists. Read selected full leaves; trivial understood edits normally need proof and at most one justified extra principle, while ordinary questions need no engineering ceremony.

## Interaction & Reasoning (20 leaves + 1 selector)

[af-interaction](../plugins/agent-first/skills/af-interaction/SKILL.md) matches the requested output to the smallest relevant leaf. Default read-only scope, explicitly requested artifacts, mixed requests and advisor handoffs follow `rule://agent-first-shared`. These are procedures, not agents or permission grants.

| Native skill | Intent |
| --- | --- |
| [interaction-how](../plugins/agent-first/skills/interaction-how/SKILL.md) | Trace implementation flow from source |
| [interaction-why](../plugins/agent-first/skills/interaction-why/SKILL.md) | Explain rationale using recorded evidence |
| [interaction-teach](../plugins/agent-first/skills/interaction-teach/SKILL.md) | Build understanding with progressive practice |
| [interaction-blast-radius](../plugins/agent-first/skills/interaction-blast-radius/SKILL.md) | Separate direct and possible change consumers |
| [interaction-technical-writing](../plugins/agent-first/skills/interaction-technical-writing/SKILL.md) | Produce source-grounded engineering documentation |
| [interaction-bro](../plugins/agent-first/skills/interaction-bro/SKILL.md) | Explain accurately in plain language |
| [interaction-interview-me](../plugins/agent-first/skills/interaction-interview-me/SKILL.md) | Elicit requirements one material question at a time |
| [interaction-in-your-own-words](../plugins/agent-first/skills/interaction-in-your-own-words/SKILL.md) | Confirm intent and scope without implementing |
| [interaction-idea-refine](../plugins/agent-first/skills/interaction-idea-refine/SKILL.md) | Compare concepts and the smallest useful experiment |
| [interaction-sharpen](../plugins/agent-first/skills/interaction-sharpen/SKILL.md) | Define observable outcomes, constraints and non-goals |
| [interaction-architect](../plugins/agent-first/skills/interaction-architect/SKILL.md) | Discuss architectural alternatives before implementation |
| [interaction-figure-it-out](../plugins/agent-first/skills/interaction-figure-it-out/SKILL.md) | Find a cheap, safe next diagnostic step |
| [interaction-recall](../plugins/agent-first/skills/interaction-recall/SKILL.md) | Recover a specific documented past decision |
| [interaction-ketchup](../plugins/agent-first/skills/interaction-ketchup/SKILL.md) | Separate completed, active and blocked project work |
| [interaction-show-me-your-work](../plugins/agent-first/skills/interaction-show-me-your-work/SKILL.md) | Present changes and attributable verification evidence |
| [interaction-pause-safely](../plugins/agent-first/skills/interaction-pause-safely/SKILL.md) | Prepare a recoverable handoff without surprise actions |
| [interaction-reflect](../plugins/agent-first/skills/interaction-reflect/SKILL.md) | Derive evidence-backed execution lessons |
| [interaction-correct](../plugins/agent-first/skills/interaction-correct/SKILL.md) | Correct an observed mistake at its owning layer |
| [interaction-automate-me](../plugins/agent-first/skills/interaction-automate-me/SKILL.md) | Assess repeatable, safely bounded automation |
| [interaction-unslop](../plugins/agent-first/skills/interaction-unslop/SKILL.md) | Make prose concise without losing material risks |

## Original skills and selector

| Skill | Purpose and trigger |
| --- | --- |
| [af-engineering](../plugins/agent-first/skills/af-engineering/SKILL.md) | Route engineering requests, derive acceptance and choose a proportional workflow |
| [af-design](../plugins/agent-first/skills/af-design/SKILL.md) | Assess boundaries, public contracts, ownership and compatibility |
| [af-database](../plugins/agent-first/skills/af-database/SKILL.md) | Model data, queries, transactions and migrations |
| [af-frontend](../plugins/agent-first/skills/af-frontend/SKILL.md) | Design interaction state, semantics, accessibility and responsive behavior |
| [af-testing](../plugins/agent-first/skills/af-testing/SKILL.md) | Diagnose uncertain defects and design regression tests |
| [af-security](../plugins/agent-first/skills/af-security/SKILL.md) | Inspect trust boundaries, authorization and sensitive data paths |
| [af-performance](../plugins/agent-first/skills/af-performance/SKILL.md) | Measure bottlenecks and compare behavior-preserving optimizations |
| [af-operations](../plugins/agent-first/skills/af-operations/SKILL.md) | Plan deployment, lifecycle, health, observability and recovery |
| [af-context](../plugins/agent-first/skills/af-context/SKILL.md) | Recover and maintain meaningful project/task/decision/handoff records |
| [af-verification](../plugins/agent-first/skills/af-verification/SKILL.md) | Execute relevant checks and report attributable evidence and gaps |
| [af-isolation](../plugins/agent-first/skills/af-isolation/SKILL.md) | Manage explicitly requested optional OVNFS checkout work |
| [af-principles](../plugins/agent-first/skills/af-principles/SKILL.md) | Match observed decision triggers to the relevant independent leaves |

## Core principles

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-laziness-protocol](../plugins/agent-first/skills/principle-laziness-protocol/SKILL.md) | Choose the smallest sufficient mechanism | An extra layer or oversized fix is proposed |
| [principle-foundational-thinking](../plugins/agent-first/skills/principle-foundational-thinking/SKILL.md) | Choose data and ownership shape first | A core representation or resource owner is being designed |
| [principle-redesign-from-first-principles](../plugins/agent-first/skills/principle-redesign-from-first-principles/SKILL.md) | Integrate requirements coherently | Repeated exceptions expose a mismatched boundary |
| [principle-attack-the-premise](../plugins/agent-first/skills/principle-attack-the-premise/SKILL.md) | Test a shared failed assumption | Two distinct fixes sharing a premise fail the same gate |
| [principle-subtract-before-you-add](../plugins/agent-first/skills/principle-subtract-before-you-add/SKILL.md) | Simplify before extending | Owned obsolete or duplicate mechanisms obstruct a change |
| [principle-minimize-reader-load](../plugins/agent-first/skills/principle-minimize-reader-load/SKILL.md) | Reduce tracing and hidden state | Forwarding layers or mutable state obscure a concrete question |
| [principle-outcome-oriented-execution](../plugins/agent-first/skills/principle-outcome-oriented-execution/SKILL.md) | Deliver a complete authorized target state | A coordinated rewrite has explicit cutover boundaries |
| [principle-experience-first](../plugins/agent-first/skills/principle-experience-first/SKILL.md) | Improve the consumer's actual journey | Feedback, focus, errors or API ergonomics drive a trade-off |
| [principle-exhaust-the-design-space](../plugins/agent-first/skills/principle-exhaust-the-design-space/SKILL.md) | Resolve consequential empirical forks | Cheap alternatives can settle an important novel choice |
| [principle-build-the-lever](../plugins/agent-first/skills/principle-build-the-lever/SKILL.md) | Make repeated work reproducible | A repeatable transformation or evidence gap exceeds existing tools |

## Architecture principles

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-model-the-domain](../plugins/agent-first/skills/principle-model-the-domain/SKILL.md) | Represent domain invariants explicitly | Synchronized flags or growing branches expose an implicit model |
| [principle-boundary-discipline](../plugins/agent-first/skills/principle-boundary-discipline/SKILL.md) | Parse and enforce at ingress | Untrusted input or transport adapters cross a boundary |
| [principle-type-system-discipline](../plugins/agent-first/skills/principle-type-system-discipline/SKILL.md) | Enforce semantic states with available types | Typed APIs allow mismatched identities or missing variants |
| [principle-make-operations-idempotent](../plugins/agent-first/skills/principle-make-operations-idempotent/SKILL.md) | Reconcile repeated or partial operations | A state-changing command can repeat or resume after interruption |
| [principle-migrate-callers-then-delete-legacy-apis](../plugins/agent-first/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Complete an authorized consumer cutover | A replacement leaves callers or obsolete exports behind |
| [principle-separate-before-serializing-shared-state](../plugins/agent-first/skills/principle-separate-before-serializing-shared-state/SKILL.md) | Remove unnecessary shared mutation | Independent actors publish into the same file, key or object |

## Verification principles

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-prove-it-works](../plugins/agent-first/skills/principle-prove-it-works/SKILL.md) | Support claims with the real artifact | Reporting completion, a finding, measurement or blocked check |
| [principle-fix-root-causes](../plugins/agent-first/skills/principle-fix-root-causes/SKILL.md) | Correct the first causal divergence | A defect is uncertain or a proposed fix suppresses symptoms |
| [principle-sequence-verifiable-units](../plugins/agent-first/skills/principle-sequence-verifiable-units/SKILL.md) | Make coherent progress checkable | Dependent changes need explicit behavior checkpoints |
| [principle-test-behavior-not-implementation](../plugins/agent-first/skills/principle-test-behavior-not-implementation/SKILL.md) | Assert consumer-observable invariants | Tests are being designed or brittle tests obstruct a valid refactor |
| [principle-explain-the-number](../plugins/agent-first/skills/principle-explain-the-number/SKILL.md) | Establish what a measurement means | Timing, resource counts or evaluation scores guide a choice |

## Delegation principles

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-guard-the-context-window](../plugins/agent-first/skills/principle-guard-the-context-window/SKILL.md) | Keep decision evidence useful | Large read sets or payloads threaten active context |
| [principle-never-block-on-the-human](../plugins/agent-first/skills/principle-never-block-on-the-human/SKILL.md) | Continue independent authorized work | Routine permission-seeking or an approval-dependent branch stalls safe work |

## Meta principle

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-encode-lessons-in-structure](../plugins/agent-first/skills/principle-encode-lessons-in-structure/SKILL.md) | Prevent recurrence at the enforcing layer | Repeated evidenced corrections or an enforceable local defect warrant a structural fix |

## Loading, sharing and authority

On OMP 18.22.1, frontmatter `hide: true` keeps all 44 leaves out of the model catalog while retaining native URI access. The 13 domain/support and selector entries remain visible in an unfiltered, non-colliding installation. No `manualSkills` or inclusion config is installed. Operator provider/plugin/skill disables and include/ignore filters remain authoritative; unavailable material is a limitation, not permission to override settings. See [native skills semantics](omp://skills.md). Restart after CLI lifecycle changes; TUI `/reload-plugins` refreshes supported capabilities and a restart rebuilds complete rule context.

All six read-only advisors autoload their domain skill plus `af-principles`, expose read/grep/glob, prohibit spawning and declare `structured: true` plus an explicit native `{report: string}` output schema for native yield (the boolean alone does not supply yield). Main passes selected principle URIs/triggers and any interaction purpose/leaf explicitly under [shared rules](../plugins/agent-first/rules/agent-first-shared.md); children read assigned material themselves. Main-only routing lives in [orchestrator rules](../plugins/agent-first/rules/agent-first-orchestrator.md), not inherited append text. Reuse bundled `reviewer` with explicit patch/leaf handoff, without a cloned definition. Native name shadowing and additive capabilities still apply. Main owns implementation/checks; concurrency two and one delegation level are instructions, not config overrides. See [architecture](architecture.md), [task discovery](omp://task-agent-discovery.md), [evaluation guidance](../eval/README.md) and [migration validation](../eval/plugin-migration-validation.md); historical interaction validation is not current plugin evidence.

## Attribution

The selector and 24 leaves adapt [pstack at revision `2f87c854fe3e2fcda44ca86b46ede35aad3c46b7`](https://github.com/cursor/plugins/tree/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack), Copyright (c) 2026 Lauren Tan, MIT. [Sources and adaptation boundaries](../plugins/agent-first/skills/af-principles/SOURCES.md) and the [complete preserved MIT notice](../plugins/agent-first/skills/af-principles/LICENSE) accompany that material. This attribution does not relicense unrelated Agent-First files.

The interaction layer comes from the supplied Interaction & Reasoning Skills source overlay. Its package provenance and adaptation boundaries are documented [separately](../plugins/agent-first/skills/af-interaction/SOURCES.md); the principle-layer MIT notice does not automatically license that package.
