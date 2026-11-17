# Skills catalog

Agent-First preserves eleven original domain/support skills and adds `af-principles` plus 24 independent principle leaves: **36 native registry entries, 12 visible catalog entries**. Normal use remains `af` and an outcome, without manual skill commands or a new runtime.

The path is **workflow -> relevant domain procedure -> relevant principles -> main implementation and checks**. The [selector](../profile/skills/af-principles/SKILL.md) is the authoritative activation map, including workflow/domain applicability. The summaries below are discovery pointers, not replacement procedures. Main reads selected leaves in full through native `skill://principle-NAME` before applying them. Usually one to three suffice per decision; trivial understood edits normally need only `prove-it-works`, with at most one additional justified leaf. The catalog is not a checklist or planning ceremony.

## Original skills and selector

| Skill | Purpose and trigger |
| --- | --- |
| [af-engineering](../profile/skills/af-engineering/SKILL.md) | Route engineering requests, derive acceptance and choose a proportional workflow |
| [af-design](../profile/skills/af-design/SKILL.md) | Assess boundaries, public contracts, ownership and compatibility |
| [af-database](../profile/skills/af-database/SKILL.md) | Model data, queries, transactions and migrations |
| [af-frontend](../profile/skills/af-frontend/SKILL.md) | Design interaction state, semantics, accessibility and responsive behavior |
| [af-testing](../profile/skills/af-testing/SKILL.md) | Diagnose uncertain defects and design regression tests |
| [af-security](../profile/skills/af-security/SKILL.md) | Inspect trust boundaries, authorization and sensitive data paths |
| [af-performance](../profile/skills/af-performance/SKILL.md) | Measure bottlenecks and compare behavior-preserving optimizations |
| [af-operations](../profile/skills/af-operations/SKILL.md) | Plan deployment, lifecycle, health, observability and recovery |
| [af-context](../profile/skills/af-context/SKILL.md) | Recover and maintain meaningful project/task/decision/handoff records |
| [af-verification](../profile/skills/af-verification/SKILL.md) | Execute relevant checks and report attributable evidence and gaps |
| [af-isolation](../profile/skills/af-isolation/SKILL.md) | Manage explicitly requested optional OVNFS checkout work |
| [af-principles](../profile/skills/af-principles/SKILL.md) | Match observed decision triggers to the relevant independent leaves |

## Core principles

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-laziness-protocol](../profile/skills/principle-laziness-protocol/SKILL.md) | Choose the smallest sufficient mechanism | An extra layer or oversized fix is proposed |
| [principle-foundational-thinking](../profile/skills/principle-foundational-thinking/SKILL.md) | Choose data and ownership shape first | A core representation or resource owner is being designed |
| [principle-redesign-from-first-principles](../profile/skills/principle-redesign-from-first-principles/SKILL.md) | Integrate requirements coherently | Repeated exceptions expose a mismatched boundary |
| [principle-attack-the-premise](../profile/skills/principle-attack-the-premise/SKILL.md) | Test a shared failed assumption | Two distinct fixes sharing a premise fail the same gate |
| [principle-subtract-before-you-add](../profile/skills/principle-subtract-before-you-add/SKILL.md) | Simplify before extending | Owned obsolete or duplicate mechanisms obstruct a change |
| [principle-minimize-reader-load](../profile/skills/principle-minimize-reader-load/SKILL.md) | Reduce tracing and hidden state | Forwarding layers or mutable state obscure a concrete question |
| [principle-outcome-oriented-execution](../profile/skills/principle-outcome-oriented-execution/SKILL.md) | Deliver a complete authorized target state | A coordinated rewrite has explicit cutover boundaries |
| [principle-experience-first](../profile/skills/principle-experience-first/SKILL.md) | Improve the consumer's actual journey | Feedback, focus, errors or API ergonomics drive a trade-off |
| [principle-exhaust-the-design-space](../profile/skills/principle-exhaust-the-design-space/SKILL.md) | Resolve consequential empirical forks | Cheap alternatives can settle an important novel choice |
| [principle-build-the-lever](../profile/skills/principle-build-the-lever/SKILL.md) | Make repeated work reproducible | A repeatable transformation or evidence gap exceeds existing tools |

## Architecture principles

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-model-the-domain](../profile/skills/principle-model-the-domain/SKILL.md) | Represent domain invariants explicitly | Synchronized flags or growing branches expose an implicit model |
| [principle-boundary-discipline](../profile/skills/principle-boundary-discipline/SKILL.md) | Parse and enforce at ingress | Untrusted input or transport adapters cross a boundary |
| [principle-type-system-discipline](../profile/skills/principle-type-system-discipline/SKILL.md) | Enforce semantic states with available types | Typed APIs allow mismatched identities or missing variants |
| [principle-make-operations-idempotent](../profile/skills/principle-make-operations-idempotent/SKILL.md) | Reconcile repeated or partial operations | A state-changing command can repeat or resume after interruption |
| [principle-migrate-callers-then-delete-legacy-apis](../profile/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Complete an authorized consumer cutover | A replacement leaves callers or obsolete exports behind |
| [principle-separate-before-serializing-shared-state](../profile/skills/principle-separate-before-serializing-shared-state/SKILL.md) | Remove unnecessary shared mutation | Independent actors publish into the same file, key or object |

## Verification principles

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-prove-it-works](../profile/skills/principle-prove-it-works/SKILL.md) | Support claims with the real artifact | Reporting completion, a finding, measurement or blocked check |
| [principle-fix-root-causes](../profile/skills/principle-fix-root-causes/SKILL.md) | Correct the first causal divergence | A defect is uncertain or a proposed fix suppresses symptoms |
| [principle-sequence-verifiable-units](../profile/skills/principle-sequence-verifiable-units/SKILL.md) | Make coherent progress checkable | Dependent changes need explicit behavior checkpoints |
| [principle-test-behavior-not-implementation](../profile/skills/principle-test-behavior-not-implementation/SKILL.md) | Assert consumer-observable invariants | Tests are being designed or brittle tests obstruct a valid refactor |
| [principle-explain-the-number](../profile/skills/principle-explain-the-number/SKILL.md) | Establish what a measurement means | Timing, resource counts or evaluation scores guide a choice |

## Delegation principles

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-guard-the-context-window](../profile/skills/principle-guard-the-context-window/SKILL.md) | Keep decision evidence useful | Large read sets or payloads threaten active context |
| [principle-never-block-on-the-human](../profile/skills/principle-never-block-on-the-human/SKILL.md) | Continue independent authorized work | Routine permission-seeking or an approval-dependent branch stalls safe work |

## Meta principle

| Leaf | Purpose | Read when |
| --- | --- | --- |
| [principle-encode-lessons-in-structure](../profile/skills/principle-encode-lessons-in-structure/SKILL.md) | Prevent recurrence at the enforcing layer | Repeated evidenced corrections or an enforceable local defect warrant a structural fix |

## Loading, sharing and authority

On OMP 18.22.0, `skills.manualSkills: [principle-*]` hides leaf catalog metadata, not native URI access. Exact names in `includeSkills` retain every leaf in the registry. Start a fresh session after profile changes; running-session hot-reload is not established.

All six custom advisors autoload their domain skill plus the selector. Main passes only relevant selected leaf URIs, observed triggers and the decision question under [RULES.md](../profile/RULES.md); children read assigned leaves themselves. Registry access does not inherit main's append text or read history. The bundled reviewer receives explicit handoff rather than a cloned definition. Main owns implementation and checks; principles leave safety, compatibility, read-only advice and consultation limits unchanged. [Architecture](architecture.md) explains the boundaries; [evaluation guidance](../eval/README.md) distinguishes native-read evidence from decision quality and records actual results in [Principles validation](../eval/principles-validation.md).

## Attribution

The selector and 24 leaves adapt [pstack at revision `2f87c854fe3e2fcda44ca86b46ede35aad3c46b7`](https://github.com/cursor/plugins/tree/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack), Copyright (c) 2026 Lauren Tan, MIT. [Sources and adaptation boundaries](../profile/skills/af-principles/SOURCES.md) and the [complete preserved MIT notice](../profile/skills/af-principles/LICENSE) accompany that material. This attribution does not relicense unrelated Agent-First files.
