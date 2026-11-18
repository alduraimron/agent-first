# Feature development

## Entry and inputs
Use for new or changed behavior within established boundaries. Require user outcomes, existing entry points/consumers, constraints, compatibility needs, and known verification commands.

## Steps and decision points
1. Trace the end-to-end path and derive observable acceptance criteria using the engineering requirements procedure. Include invalid input and relevant failure states.
2. Plan the smallest complete vertical slice: data/logic, interface, consumers, tests, and documentation where behavior changes. Identify a check for each criterion.
3. Load the touched domain skills. If the design changes boundaries or public contracts, reclassify architecture-impacting before implementing that part.
4. Main implements each planned slice, migrating every affected caller and removing superseded mechanisms. Track meaningful task state through `skill://af-context`.
5. Compare implementation coverage to every criterion; resolve gaps before verification.

## Consultation
Use router protocol only for material domain uncertainty. Independent reviewer is conditional on concrete risk, not feature size alone.

## Verification
Use `skill://af-verification` for focused tests, integration paths, and consumer-visible behavior. Recommend existing project commands; distinguish missing infrastructure from failed behavior.

## Exit
Every requested outcome has an implemented path and evidence status, with compatibility and remaining limitations stated.

## Failure and escalation
Investigate failing criteria through af-testing. Escalate unresolved intent only after source inspection; preserve working scope when a separate action is blocked. Reclassify newly discovered architectural impact rather than quietly extending the plan.
