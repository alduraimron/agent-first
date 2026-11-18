# Project initialization

## Entry and inputs
Use for authorized personal-project setup or missing context, not team/default-profile changes or unrelated host provisioning. Require intended outcome, repository root, existing manifests/configuration, scope and known runtime constraints.

## Steps and decision points
1. Inspect existing source, manifests, scripts, repository guidance, and context before proposing new structure. Distinguish an empty project from an existing project lacking records.
2. Derive initial acceptance criteria and a proportional plan. Reuse installed tools and established layout; task-required project dependencies are AUTO within verified workspace/venv scope under RULES.md. List missing global/runtime prerequisites and obtain the supported high-risk approval when needed rather than installing unrelated tools silently.
3. Load `skill://af-context` for relevant context/task artifacts, preserving existing facts and historical evidence. Record only observed commands and constraints, not prefilled successful results.
4. If implementation is requested, build the smallest runnable end-to-end skeleton using existing conventions. A new architectural boundary requires architecture-impacting consultation first. Context-only setup does not authorize application changes.
5. Document discovered entry points and the next executable action in the context contract.

## Consultation
Use af-architect for material initial boundary decisions, af-devops for uncertain runtime delivery requirements, and other advisors only for specific domain questions via the router.

## Verification
Use `skill://af-verification` to select existing startup/build/test checks appropriate to the authorized setup. Report missing dependencies as limitations, never as successful startup.

## Exit
Authorized setup artifacts and requested runnable behavior exist; commands, constraints, evidence status, and next action are recoverable.

## Failure and escalation
Resolve authorized project dependency needs under RULES.md; report still unavailable prerequisites or genuine approval blockers without changing shared profiles or bypassing a refusal. Preserve existing assets when setup conflicts with conventions; ask only about unresolved product intent or high-risk scope that inspection cannot establish.
