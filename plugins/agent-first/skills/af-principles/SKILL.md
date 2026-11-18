---
name: af-principles
description: Select engineering decision principles from observed triggers after workflow routing; read only relevant leaves for design, implementation, diagnosis, verification, bounded autonomy and advisory context.
---

# Engineering principle selector

Principles improve a decision; `af-engineering` still owns workflow selection, domain skills own procedures, `af-verification` owns execution evidence, and shared `rule://agent-first-shared` owns authorization. A principle never grants permission, overrides accepted compatibility, or turns an advisor into an implementation worker.

## Select at the decision

1. Inspect the request and repository evidence, then choose the existing workflow. Match the concrete decision or uncertainty to a trigger below, not every concern the task could conceivably involve. An initial uncertain bug calls for root-cause analysis, not premise attacks merely because the user offers a tentative explanation.
2. Read each selected leaf in full with native `read` on its `skill://principle-NAME` URI before applying it. Usually one to three leaves suffice at a decision; introduce another only when its trigger actually appears. The index is a menu, not a checklist or a separate planning ceremony.
3. A trivial understood edit with an existing regression normally needs only `prove-it-works` before completion. Read a second leaf only for a real decision, such as resisting a proposed abstraction. A one-off edit alone does not trigger toolmaking, design exploration, context delegation or premise attacks.
4. Apply the leaf to a concrete choice and its observable consequence. Re-evaluate when inspection, a failed experiment or a domain consultation changes the facts. Reuse already-read applicable leaves; do not reload the whole catalog or create a principle log for routine work.
5. When the choice matters, explain the principle, what choice it changed and the evidence in the existing task/decision/handoff. A name in a report is not activation or proof. Main performs the checks; advice and proposed checks remain unexecuted until then.

## Advisory handoff

Use the shared `rule://agent-first-shared` principle handoff: pass only relevant selected leaf URIs, their evidence triggers and the decision question. Children receive the native skill registry, not the main-only orchestration or its leaf-read history. They read assigned leaves themselves before advice; additional leaves need a question-relevant trigger. The six custom advisors autoload this selector plus their domain skill; the bundled reviewer instead receives explicit context through main. Main evaluates advice and implements; all existing read-only, approval and concurrency boundaries remain.

Use this compact field in each assignment, substituting only leaves actually selected from this catalog:

```text
Principles: skill://principle-NAME - observed trigger -> assigned decision
Read each listed URI in full and inspect the cited source paths before advice.
```

Domain concerns such as accessibility or minimal change are not skill names. Copy exact existing URIs from the catalog; if no principle is relevant, write `Principles: none - reason`. Children report inaccessible/missing leaves and their impact rather than inventing names or treating the parent's reading as their own. Main checks the returned source/leaf evidence before accepting consultation.

## Core

| Principle | Purpose | Evidence trigger | Applicable workflows | Domain concerns |
| --- | --- | --- | --- | --- |
| [laziness-protocol](skill://principle-laziness-protocol) | Smallest sufficient mechanism | Proposed extra layer, repeated decision or oversized fix | quick-change, feature-development, refactoring | API surface, configuration, maintenance |
| [foundational-thinking](skill://principle-foundational-thinking) | Choose the data/ownership shape first | New core representation, access pattern or resource owner | project-initialization, feature-development, architecture-impacting | entities, collections, lifecycle |
| [redesign-from-first-principles](skill://principle-redesign-from-first-principles) | Integrate a requirement coherently | Repeated exceptions reveal a mismatched boundary | architecture-impacting, refactoring | ownership, contracts, dependency direction |
| [attack-the-premise](skill://principle-attack-the-premise) | Test a shared failed assumption | Two distinct fixes assuming the same thing fail the same gate | bug-investigation, performance-optimization | causal models, experiment design |
| [subtract-before-you-add](skill://principle-subtract-before-you-add) | Simplify before extending | Owned obsolete paths or duplicated mechanisms obstruct the change | refactoring, architecture-impacting, feature-development | dead code, duplicated sources of truth |
| [minimize-reader-load](skill://principle-minimize-reader-load) | Reduce tracing and hidden state | Forwarding layers or mutable state obscure a real question | refactoring, code-review, feature-development | local reasoning, dependencies, state |
| [outcome-oriented-execution](skill://principle-outcome-oriented-execution) | Deliver a complete target state | Authorized coordinated rewrite with explicit cutover boundaries | architecture-impacting, refactoring | migrations, consumers, transitional state |
| [experience-first](skill://principle-experience-first) | Optimize the consumer's actual journey | Error/focus/feedback/API ergonomics or scope trade-off | feature-development, project-initialization, code-review | UI, CLI, accessibility, API consumers |
| [exhaust-the-design-space](skill://principle-exhaust-the-design-space) | Resolve a consequential empirical fork | Important novel choice without precedent that cheap alternatives can settle | architecture-impacting, feature-development | interaction feel, expensive design choices |
| [build-the-lever](skill://principle-build-the-lever) | Make repeated/error-prone work reproducible | A repeatable transformation or evidence gap exceeds existing tools | refactoring, architecture-impacting, performance-optimization | codemods, reproducible analysis, checks |

## Architecture

| Principle | Purpose | Evidence trigger | Applicable workflows | Domain concerns |
| --- | --- | --- | --- | --- |
| [model-the-domain](skill://principle-model-the-domain) | Represent actual domain invariants | Synchronized booleans, branch growth or repeated shape assumptions | feature-development, architecture-impacting, refactoring | state machines, identity, ownership |
| [boundary-discipline](skill://principle-boundary-discipline) | Put parsing/enforcement at ingress | Untrusted input, transport adapters or repeated internal validation | feature-development, bug-investigation, architecture-impacting, code-review | CLI/API parsing, trust, error semantics |
| [type-system-discipline](skill://principle-type-system-discipline) | Enforce semantic states with available types | Typed API/state design permits mismatched IDs or missing variants | feature-development, architecture-impacting, code-review | typed languages, schema authority |
| [make-operations-idempotent](skill://principle-make-operations-idempotent) | Reconcile repeated/partial operations | A state-changing command can repeat or resume after interruption | project-initialization, architecture-impacting, bug-investigation | migrations, jobs, setup, side effects |
| [migrate-callers-then-delete-legacy-apis](skill://principle-migrate-callers-then-delete-legacy-apis) | Complete an authorized consumer cutover | An internal replacement leaves callers or obsolete exports behind | architecture-impacting, refactoring | API ownership, compatibility, rollout |
| [separate-before-serializing-shared-state](skill://principle-separate-before-serializing-shared-state) | Remove unnecessary shared mutation | Independent actors publish into the same file/key/object | architecture-impacting, bug-investigation, performance-optimization | concurrency, transactions, process state |

## Verification

| Principle | Purpose | Evidence trigger | Applicable workflows | Domain concerns |
| --- | --- | --- | --- | --- |
| [prove-it-works](skill://principle-prove-it-works) | Support claims with the real artifact | About to report completion, a finding, a measurement or a blocked check | all eight workflows | consumer paths, native runtime, honest gaps |
| [fix-root-causes](skill://principle-fix-root-causes) | Correct the first causal divergence | An uncertain defect or a fix that would suppress a symptom | bug-investigation, code-review, performance-optimization | state lifetime, data flow, legitimate errors |
| [sequence-verifiable-units](skill://principle-sequence-verifiable-units) | Make coherent progress checkable | Multiple dependent changes need explicit behavior checkpoints | project-initialization, feature-development, architecture-impacting, refactoring | migration ordering, acceptance boundaries |
| [test-behavior-not-implementation](skill://principle-test-behavior-not-implementation) | Assert consumer-observable invariants | Designing/changing tests, or brittle tests obstruct a legitimate refactor | feature-development, bug-investigation, refactoring, code-review | test layers, negative cases, real boundaries |
| [explain-the-number](skill://principle-explain-the-number) | Establish what a measurement means | A timing, resource count or evaluation score will guide a decision | performance-optimization, code-review | baselines, sample spread, confounders |

## Delegation

| Principle | Purpose | Evidence trigger | Applicable workflows | Domain concerns |
| --- | --- | --- | --- | --- |
| [guard-the-context-window](skill://principle-guard-the-context-window) | Keep evidence useful without flooding context | Large read sets/payloads threaten the active decision | any workflow with material inspection volume | bounded reads, summaries, read-only consultation |
| [never-block-on-the-human](skill://principle-never-block-on-the-human) | Continue independent authorized work | Routine permission-seeking or one approval-dependent branch stalls safe work | any workflow with that actual blockage | reversible choices, dependency separation, approvals |

## Meta

| Principle | Purpose | Evidence trigger | Applicable workflows | Domain concerns |
| --- | --- | --- | --- | --- |
| [encode-lessons-in-structure](skill://principle-encode-lessons-in-structure) | Prevent recurrence at the enforcing layer | Repeated evidenced corrections or a concrete enforceable local defect | bug-investigation, refactoring, code-review, project-initialization | code/types/tests/lint, architecture, correction ledger |

## Native loading and provenance

Native marketplace discovery registers every principle independently. Each leaf carries `hide: true`: OMP 18.22.1 omits its catalog metadata while keeping `skill://` reads and explicit invocation available. This selector stays visible; no leaf bodies are injected into the system prompt and no skill include/ignore settings are changed.

Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source, license and adaptation boundaries](skill://af-principles/SOURCES.md).
