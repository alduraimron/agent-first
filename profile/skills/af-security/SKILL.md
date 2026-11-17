---
name: af-security
description: Analyze trust boundaries, authorization, sensitive data, injection, and abuse paths; derive enforceable security controls and focused negative checks.
---

# Trust-boundary engineering

Use shared RULES.md and af-engineering for authorization/routing; main owns implementation and evidence execution through af-verification. Advisors inspect and recommend within scope.

## Procedure
1. Map assets, actors, entry points, trust boundaries, privileged operations, and sensitive-data flow from source. Distinguish authentication, authorization, validation, and encoding controls.
2. State attacker-controlled inputs and required capabilities. Trace realistic paths to data exposure, cross-tenant access, privilege escalation, injection, resource exhaustion, or unsafe outbound access.
3. Inspect enforcement at each authoritative server/data boundary, including object-level authorization, default-deny behavior, session/token lifecycle, secret handling, and audit/redaction paths. Client checks are usability, not authorization.
4. Evaluate parsing/canonicalization, parameterized queries, contextual output encoding, path containment, upload handling, and outbound destination restrictions where those inputs exist. Use relevant abuse cases, not a disconnected checklist.
5. Propose minimal controls preserving intended behavior. Identify residual risks, compatibility effects, and explicit approval needs; architectural trust changes route through af-engineering.
6. Return evidence-backed findings or constraints with location, prerequisites, exploit/failure scenario, impact, and safe verification recommendations. Separate supported defects from untested possibilities.

## Invariants
- Authorization is checked for each protected operation/object in the authoritative layer and cannot be bypassed by alternate entry points.
- Secrets and sensitive values stay out of logs, errors, client bundles, and review artifacts.
- Untrusted data remains data across query, shell, path, template, and markup boundaries.
- Failure paths fail closed for protected actions without silently granting access or suppressing security errors.

## Verification recommendations
Recommend existing security/unit/integration checks for unauthenticated, wrong-role, cross-owner/tenant, malformed input, expired credentials, and abuse limits as relevant. Use synthetic non-sensitive fixtures and authorized local targets; avoid destructive exploit execution or external scanning. Include legitimate access regression checks. Missing authorization/environment limits proof and must remain explicit, not be replaced with a claim of safety.
