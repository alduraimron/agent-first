# Quick change

## Entry and inputs
Use for an understood localized low-risk edit, or verification-only request. Require the requested outcome, affected paths, current behavior, and narrow acceptance check.

## Steps and decision points
1. Inspect implementation and immediate callers/tests until the cause and effect are explainable. If the cause is uncertain, use bug-investigation; if scope grows, use feature-development.
2. State the narrow criterion. For verification-only work, proceed directly to verification without editing.
3. Main makes the smallest complete authorized change, including directly obsolete callers or tests. Reassess architectural boundaries before changing a contract.

## Consultation
No delegation for trivial work. If a material specialist question appears, use the router's consultation protocol and reconsider whether this route remains adequate.

## Verification
Load `skill://af-verification`; select the existing focused check for the changed behavior and relevant regression. Inspection alone does not establish runtime success.

## Exit
The requested behavior and relevant failure case are addressed, or each unverified criterion has an explicit evidence limitation under shared reporting rules.

## Failure and escalation
Stop the affected action on permission or safety blockers. Report the exact failed operation; diagnose failed checks rather than suppressing them. Escalate scope through the router when uncertainty or boundary change emerges.
