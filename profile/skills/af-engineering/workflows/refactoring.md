# Refactoring

## Entry and inputs
Use for authorized structural change preserving behavior and existing boundaries. Require the maintenance objective, affected callers, observable invariants, compatibility constraints, and current characterization evidence.

## Steps and decision points
1. Map the affected call/data flow and define what must remain unchanged: outputs, errors, ordering, side effects, resource ownership, and public interfaces.
2. Load af-design for coupling/ownership questions and af-testing for characterization gaps. Choose a small sequence of transformations with an invariant check after the complete change.
3. Main updates implementation and all callers together; remove code rendered obsolete. Avoid combining unrelated behavior fixes with the refactor.
4. Reassess design impact explicitly. Internal restructuring preserving boundaries stays refactoring; a changed public contract, ownership boundary, or dependency direction becomes architecture-impacting before that implementation.
5. Compare the resulting structure against the maintenance objective, not just diff size.

## Consultation
Use advisors only for material uncertainty; architecture redesign requires af-architect through the router. Use bundled reviewer when subtle equivalence or compatibility risk merits independent inspection.

## Verification
Use `skill://af-verification` with existing characterization/regression checks. Include error and side-effect equivalence where relevant; a clean build alone does not prove preserved behavior.

## Exit
Maintenance objective is met, all callers use the new structure, obsolete code is removed, and each preserved invariant has an evidence status.

## Failure and escalation
Investigate changed behavior before expanding the transformation. If behavior preservation cannot be supported, report the missing coverage or evidence rather than declaring equivalence. Separate newly desired behavior into explicit requirements.
