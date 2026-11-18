# Code review

## Entry and inputs
Use for read-only assessment of a patch or scoped code. Require actual changed/new-file content or explicit review scope, intended behavior, relevant contracts, base/context, and available verification evidence.

## Steps and decision points
1. Read the supplied changes and affected surrounding paths. Trace concrete failure scenarios through callers, state, trust boundaries, and error handling; distinguish introduced defects from pre-existing issues.
2. Load domain skills for touched concerns. Check each acceptance criterion and compatibility invariant against implementation, not naming or stylistic preference.
3. For each supported finding, capture severity, precise location, triggering conditions, impact, evidence, and a focused recommended check. Mark uncertainty instead of presenting speculation as fact.
4. Resolve contradictory evidence and remove duplicate findings. Review-only authorization does not permit fixes or running side-effecting checks.

## Consultation
Main may use bundled reviewer for a concrete independent-review question under the engineering reviewer protocol, supplying actual patch/new-file content. Use other advisors only for material domain uncertainty. A narrow straightforward review can remain inline.

## Verification
Use `skill://af-verification` to account for supplied versus executed evidence and recommend existing focused checks. Run checks only when authorized; a review verdict is not a runtime result.

## Exit
Return actionable evidence-backed findings and an overall assessment with explicit scope/limitations. No findings means no supported defects within the reviewed scope, not proof of correctness.

## Failure and escalation
If the patch/base is missing, inspect accessible source or request the exact unavailable input. Report inaccessible paths and unresolved risk. Do not manufacture findings, edit code, or broaden the review silently.
