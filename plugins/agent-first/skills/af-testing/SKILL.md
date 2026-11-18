---
name: af-testing
description: Diagnose failures through falsifiable hypotheses and design focused regression, integration, boundary, and failure-path tests using existing project tooling.
---

# Causal diagnosis and test design

Use shared `rule://agent-first-shared`; af-engineering owns scope/planning and af-verification owns check execution and evidence status. This skill designs diagnosis and coverage, not a second reporting protocol.

Select root-cause and behavioral-test lenses through `af-principles` for uncertain failures and new regression coverage. Attack a shared premise only when failed approaches actually expose it, not automatically after one failed check. Use proof to connect the diagnosis and resulting observable behavior.

## Procedure
1. Read the reported observation, stack/error output, affected implementation, test fixtures, and existing test scripts. Preserve the reported failure as ground truth; do not rerun solely to confirm it.
2. Define expected invariants and identify the first observed divergence. Build a short hypothesis set separating inputs, state, code, dependency, configuration, and environment causes.
3. Choose the smallest inspection or authorized experiment that distinguishes leading hypotheses. State predicted observations before execution; update conclusions from actual evidence, not agreement with the preferred theory.
4. Design a minimal deterministic regression reproducing the causal condition. Use the narrowest appropriate layer: pure unit behavior, integration contract, or consumer-visible end-to-end path. Keep real boundaries where mocks would hide the failure.
5. Add boundary/failure/concurrency cases proportional to the changed invariant. Specify setup, action, observable assertion, and teardown for each; test outcomes rather than implementation accidents.
6. Hand main a causal explanation, source locations, proposed correction constraints, and exact existing-tool verification recommendations. Reclassify through af-engineering if diagnosis reveals architecture changes.

## Invariants
- A test fails for the targeted defect, not unrelated fixture breakage; assertions distinguish correct from incorrect behavior.
- Time, randomness, shared state, and resource lifecycle are controlled where they affect determinism.
- Tests retain meaningful failures rather than weakening assertions, skipping hard cases, or masking exceptions.
- Unreproduced hypotheses remain labeled uncertain; a passing unrelated suite is not regression evidence.

## Verification recommendations
Discover actual project scripts and existing runners before suggesting commands. Recommend focused tests first, then directly affected integration/boundary cases; identify cwd, fixtures, and prerequisites. For flaky behavior recommend repeated samples with captured conditions, not retries that redefine failure as success. Escalate inaccessible diagnostics or missing reproducible inputs with the smallest needed observation. Main records results using af-verification.
