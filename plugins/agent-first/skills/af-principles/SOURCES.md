# Sources and adaptation

The `af-principles` selector and the 24 `principle-*` skills adapt engineering ideas from [pstack](https://github.com/cursor/plugins/tree/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack), Copyright (c) 2026 Lauren Tan, MIT licensed. The [complete license](skill://af-principles/LICENSE) accompanies these adaptations. This notice does not relicense unrelated Agent-First files.

Reference revision: `2f87c854fe3e2fcda44ca86b46ede35aad3c46b7`. The upstream [README](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/README.md), [poteto-mode selector](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/poteto-mode/SKILL.md), and each implementation below were inspected, not merely their titles.

## Principle implementations

Each link targets the inspected upstream `SKILL.md`:

- [laziness-protocol](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-laziness-protocol/SKILL.md)
- [foundational-thinking](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-foundational-thinking/SKILL.md)
- [redesign-from-first-principles](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-redesign-from-first-principles/SKILL.md)
- [attack-the-premise](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-attack-the-premise/SKILL.md)
- [subtract-before-you-add](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-subtract-before-you-add/SKILL.md)
- [minimize-reader-load](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-minimize-reader-load/SKILL.md)
- [outcome-oriented-execution](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-outcome-oriented-execution/SKILL.md)
- [experience-first](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-experience-first/SKILL.md)
- [exhaust-the-design-space](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-exhaust-the-design-space/SKILL.md)
- [build-the-lever](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-build-the-lever/SKILL.md)
- [model-the-domain](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-model-the-domain/SKILL.md)
- [boundary-discipline](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-boundary-discipline/SKILL.md)
- [type-system-discipline](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-type-system-discipline/SKILL.md)
- [make-operations-idempotent](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-make-operations-idempotent/SKILL.md)
- [migrate-callers-then-delete-legacy-apis](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md)
- [separate-before-serializing-shared-state](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md)
- [prove-it-works](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-prove-it-works/SKILL.md)
- [fix-root-causes](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-fix-root-causes/SKILL.md)
- [sequence-verifiable-units](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-sequence-verifiable-units/SKILL.md)
- [test-behavior-not-implementation](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-test-behavior-not-implementation/SKILL.md)
- [explain-the-number](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-explain-the-number/SKILL.md)
- [guard-the-context-window](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-guard-the-context-window/SKILL.md)
- [never-block-on-the-human](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-never-block-on-the-human/SKILL.md)
- [encode-lessons-in-structure](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/principle-encode-lessons-in-structure/SKILL.md)

## Native OMP adaptation

- Workflow procedures and domain skills remain authoritative for execution. Principles supply decision criteria, examples, observable outcomes, and checks rather than replacing those procedures.
- OMP 18.22.1 supports marketplace skill discovery, native `hide: true`, skill URIs and advisor `autoloadSkills`: [official skill documentation](https://github.com/can1357/oh-my-pi/blob/v18.22.1/docs/skills.md). The selector stays catalog-visible; leaves remain URI-readable. No Cursor commands, extensions or additional runtime are required.
- Design exploration and leverage are proportional to demonstrated uncertainty and recurring cost. A one-off edit does not need a framework, script, or alternatives ceremony.
- Shared `rule://agent-first-shared`, native denies, scope, consequential approval, and required compatibility outrank every principle. Continuing safe independent work never authorizes the blocked operation.
- Main owns verification. Read-only advisors receive selected skill URIs explicitly and read them in their own sessions. The principles do not authorize implementation delegation.
- Corrections prefer code, tests, constraints, and tooling over accumulating prompt rules. One failure does not authorize global policy rewriting.
