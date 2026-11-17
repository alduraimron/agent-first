---
name: af-frontend
description: Engineer UI interactions, accessibility, responsive layouts, and client state with explicit loading, error, keyboard, and browser verification paths.
---

# Usable interfaces

Use shared RULES.md, af-engineering requirements/routing, and af-verification evidence handling. Main owns edits and any browser activity; advisors remain read-only.

Select through `af-principles`: experience-first for a changed user journey, domain modeling for ambiguous interaction state, and boundary discipline for client/server or component ownership. Explore competing interactions only when an important unresolved difference warrants it; static advice is not browser evidence.

## Procedure
1. Trace the requested user journey through routes, components, state, data fetching, and existing design tokens. Identify supported viewports, input modes, and accessibility conventions from the project.
2. Define visible states and transitions: initial, loading, empty, success, validation failure, server failure, disabled, and retry where applicable. Specify URL/history behavior and state ownership.
3. Match semantic controls to actions: links navigate, buttons act, forms submit. Define accessible names, labels, error associations, focus order/restoration, keyboard behavior, and announcements for asynchronous changes.
4. Design responsive behavior using existing layout/token conventions. Check long text, localization, overflow, zoom, reduced motion, and touch target implications rather than assuming a desktop happy path.
5. Trace async lifecycle and races: stale requests, cancellation/unmount, optimistic rollback, duplicate submission, and cache invalidation. Keep server-authoritative data distinct from derived UI state.
6. Return component/state changes, accessibility invariants, concrete interaction scenarios, and relevant source locations.

## Invariants
- Every interactive control is keyboard reachable and has a programmatic name; focus remains visible and does not become trapped accidentally.
- Errors identify the affected field/action and preserve user input where safe. Status is not conveyed by color alone.
- Stale responses cannot overwrite newer intent; repeated submission cannot create unintended duplicate side effects.
- Sensitive data does not leak through client logs, markup, or unauthorized rendered states.

## Verification recommendations
Recommend existing component/UI/accessibility tests and app scripts. Main can inspect the actual journey in the existing browser integration under shared browser rules, including keyboard-only interaction, focus, narrow/wide viewport, loading/error states, and screenshots of actual results. Static markup review does not establish browser behavior; automated accessibility checks do not replace interaction checks. Report missing app/runtime access and unsupported viewport evidence explicitly.
