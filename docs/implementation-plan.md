# Native marketplace cutover plan

## Fixed release architecture

Release 2.0.0 uses only `agent-first@agent-first`, sourced from `alduraimron/agent-first`, at explicit **project scope** on OMP 18.22.1. The current checkout is local until publication. Native OMP owns execution, sessions, task scheduling, model routing, discovery and approvals; no new runtime, executable extension, package dependencies or settings authority is added.

1. Package `.omp-plugin/marketplace.json` with `./plugins/agent-first` and native `.omp-plugin/plugin.json` metadata. Discover conventional rules, agents and skills through native marketplace support, including v18.22.1 `discovery/claude-plugins.ts` `loadRules`.
2. Preserve all 57 skills, 13 visible entries, 44 frontmatter-hidden but URI-readable leaves, eight workflows, context templates and attribution. Keep selector-led proportional full reads, not eager prompt bundles.
3. Replace main appended text with main-filtered orchestrator rules; place common authorization/advisory/evidence contracts in shared rules targeting main, six advisors and bundled reviewer. Preserve read/grep/glob and no-spawn advisors with native structured yield. Reuse, never clone, reviewer.
4. Inherit native operator/project config, permissions, models, tools and providers. Install no profile config or custom AUTO/ASK/DENY patterns. Honor disables and native collisions; never overwrite `AGENTS.md`, settings or existing definitions.
5. Validate replacement through isolated native local marketplace add/install/discovery/upgrade/uninstall and project-boundary/preservation checks before retiring launcher/profile distribution. Never delete real user launcher/profile symlinks automatically; document optional verified-target operator cleanup only.
6. Adapt evaluation to native project installation with explicit independent evaluation controls. Retain all route, full-read/child chronology, consumer, read-only, approval-denied and executed-failure expectations plus historical failures. Separate `--policy native` from restrictive `--policy strict`; neither is installed plugin policy.
7. Publish current usage/architecture/catalog/evaluation guidance and a useful evidence-based backlog. Parent records actual integrated results in a separate migration validation report. Commands and source inspection alone do not establish passing behavior or a published release.

## Authority and scope

The nearest ancestor `.omp/`, otherwise nearest Git root, is the project anchor; its descendants inherit the install. The manifest cannot enforce project-only installation. Marketplace registry and caches are native user storage, not global approval settings changes. Use explicit `--scope project`; do not silently add user installs or change unrelated config.

Local reversible choices within the authorized outcome proceed proportionally. Consequential/external effects require precise scope and native gates when configured; refusal cannot be bypassed. OVNFS stays explicit opt-in with no automatic apply or OS-sandbox claim. Tern uses existing hosting with backend checks and no automatic provisioning.

## Acceptance and handoff

Run integrated checks only after all migration slices land. Retain actual command/cwd/version/status, native context and referenced task journals, consumer/process results, exact config-preservation comparisons and disposable filesystem observations. Report PASS/FAIL/NOT-RUN/NOT-APPLICABLE distinctly. Keep prior reports and corrections unchanged; historical launcher/custom-policy evidence is not evidence for inherited native behavior. No automatic commit, push or publication.

References: [usage](../README.md), [architecture](architecture.md), [evaluation](../eval/README.md), [native marketplace](omp://marketplace.md), [task discovery](omp://task-agent-discovery.md), [skills](omp://skills.md).
