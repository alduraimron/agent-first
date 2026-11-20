---
name: af-principles
description: Select engineering decision principles from observed triggers after workflow routing; read only relevant leaves for design, implementation, diagnosis, verification, bounded autonomy and advisory context.
---

# Engineering principle selector

Principles refine decisions; `af-engineering` owns workflow routing, domain skills own procedures, `af-verification` owns execution evidence and `rule://agent-first-shared` owns authorization. A principle never expands permissions or turns advisors into implementers.

## Selection rules

1. Route the workflow and inspect repo facts first. Match **only** concrete observed triggers below—never load a fixed bundle or speculative list. An initial uncertain bug triggers `fix-root-causes`, not `attack-the-premise`.
2. `read` each selected `skill://principle-NAME` leaf **in full** before applying it. Usually 1–3 leaves suffice per decision; reuse already-read leaves and reassess only when evidence changes.
3. Trivial understood edits normally need only `prove-it-works` before completion (plus at most one justified extra leaf); they do not trigger `exhaust-the-design-space`, `build-the-lever`, `guard-the-context-window` or `attack-the-premise`.
4. Name mentions do not prove application—apply each leaf to an observable choice and cite it only where material.

## Advisory handoff

Children do **not** inherit main's read history or orchestrator rule. Include this exact field in every advisor or bundled `reviewer` assignment, copying **only exact catalog URIs below** (never invent domain labels like `accessibility` or `minimal-change`):

```text
Principles: skill://principle-NAME - observed trigger -> assigned decision
Read each listed URI in full and inspect the cited source paths before advice.
```

If no leaf applies, write `Principles: none - reason`. Children must read every listed URI and cited source themselves before advising (or report inaccessible leaves). Main checks returned evidence before accepting advice.

## Core

| Principle | Trigger | Workflows |
| --- | --- | --- |
| [laziness-protocol](skill://principle-laziness-protocol) | Smallest sufficient mechanism: proposed extra layer, repeated decision or oversized fix | quick-change, feature-development, refactoring |
| [foundational-thinking](skill://principle-foundational-thinking) | Data/ownership shape first: new core representation, access pattern or resource owner | project-initialization, feature-development, architecture-impacting |
| [redesign-from-first-principles](skill://principle-redesign-from-first-principles) | Coherent boundary redesign: repeated exceptions reveal a mismatched boundary | architecture-impacting, refactoring |
| [attack-the-premise](skill://principle-attack-the-premise) | Test a shared failed assumption: **two distinct fixes** assuming the same thing fail the same gate | bug-investigation, performance-optimization |
| [subtract-before-you-add](skill://principle-subtract-before-you-add) | Simplify before extending: owned obsolete paths or duplicate mechanisms obstruct the change | refactoring, architecture-impacting, feature-development |
| [minimize-reader-load](skill://principle-minimize-reader-load) | Reduce tracing/hidden state: forwarding layers or mutable state obscure a concrete question | refactoring, code-review, feature-development |
| [outcome-oriented-execution](skill://principle-outcome-oriented-execution) | Deliver complete target state: authorized coordinated rewrite with explicit cutover boundaries | architecture-impacting, refactoring |
| [experience-first](skill://principle-experience-first) | Consumer journey first: error/focus/feedback/accessibility or CLI/API ergonomics trade-off | feature-development, project-initialization, code-review |
| [exhaust-the-design-space](skill://principle-exhaust-the-design-space) | Resolve an empirical fork: important novel choice without precedent that cheap options can settle | architecture-impacting, feature-development |
| [build-the-lever](skill://principle-build-the-lever) | Make repeated work reproducible: a repeatable transform or evidence gap exceeds existing tools | refactoring, architecture-impacting, performance-optimization |

## Architecture

| Principle | Trigger | Workflows |
| --- | --- | --- |
| [model-the-domain](skill://principle-model-the-domain) | Explicit domain invariants: synchronized booleans, growing branches or implicit state shapes | feature-development, architecture-impacting, refactoring |
| [boundary-discipline](skill://principle-boundary-discipline) | Parse/enforce at ingress: untrusted input, transport adapters or repeated internal validation | feature-development, bug-investigation, architecture-impacting, code-review |
| [type-system-discipline](skill://principle-type-system-discipline) | Semantic types: typed API/state permits mismatched IDs or missing variants | feature-development, architecture-impacting, code-review |
| [make-operations-idempotent](skill://principle-make-operations-idempotent) | Reconcile repeated/partial runs: state-changing command/migration/job can repeat or resume | project-initialization, architecture-impacting, bug-investigation |
| [migrate-callers-then-delete-legacy-apis](skill://principle-migrate-callers-then-delete-legacy-apis) | Complete consumer cutover: internal replacement leaves callers or obsolete exports behind | architecture-impacting, refactoring |
| [separate-before-serializing-shared-state](skill://principle-separate-before-serializing-shared-state) | Eliminate shared mutation: independent actors write to the same file, key or object | architecture-impacting, bug-investigation, performance-optimization |

## Verification

| Principle | Trigger | Workflows |
| --- | --- | --- |
| [prove-it-works](skill://principle-prove-it-works) | Direct artifact proof: about to report completion, a finding, measurement or blocked check | all eight workflows |
| [fix-root-causes](skill://principle-fix-root-causes) | First causal divergence: uncertain defect or proposed fix would only suppress a symptom | bug-investigation, code-review, performance-optimization |
| [sequence-verifiable-units](skill://principle-sequence-verifiable-units) | Checkable progress: dependent changes need explicit behavior checkpoints/migration order | project-initialization, feature-development, architecture-impacting, refactoring |
| [test-behavior-not-implementation](skill://principle-test-behavior-not-implementation) | Consumer-observable tests: designing/changing tests, or brittle tests block a valid refactor | feature-development, bug-investigation, refactoring, code-review |
| [explain-the-number](skill://principle-explain-the-number) | Ground quantitative claims: a timing, resource count or eval score guides a decision | performance-optimization, code-review |

## Delegation & Meta

| Principle | Trigger | Workflows |
| --- | --- | --- |
| [guard-the-context-window](skill://principle-guard-the-context-window) | Protect active context: large read sets/payloads threaten the active decision | any workflow with material read volume |
| [never-block-on-the-human](skill://principle-never-block-on-the-human) | Continue safe independent work: routine permission-seeking or one blocked branch stalls progress | any workflow with that actual blockage |
| [encode-lessons-in-structure](skill://principle-encode-lessons-in-structure) | Enforce at the owning layer: repeated evidenced corrections or concrete enforceable local defect | bug-investigation, refactoring, code-review, project-initialization |

## Loading and provenance

Each leaf carries `hide: true` (omitted from the visible catalog while remaining readable via `skill://`). Adapted from pstack, Copyright (c) 2026 Lauren Tan, MIT. [Source, license and adaptation boundaries](skill://af-principles/SOURCES.md).
