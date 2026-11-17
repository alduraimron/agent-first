---
name: af-database
description: Engineer schemas, migrations, transactions, and queries with explicit integrity, compatibility, concurrency, and query-plan checks.
---

# Data integrity

Use shared RULES.md; af-engineering owns requirements/routing and af-verification owns evidence execution/reporting. Main implements; advisors inspect and recommend.

Select through `af-principles` when domain invariants need representation, retries need idempotency, shared writes need ownership separation, or old/new callers need a migration boundary. These lenses refine the persistence decision; they do not replace this procedure or authorize a migration.

## Procedure
1. Read schema/model definitions, migrations, repository queries, transaction boundaries, and affected callers. Identify the actual database engine/version from project evidence and map entity ownership and data sensitivity.
2. Define cardinality, nullability, uniqueness, referential integrity, deletion/retention, and ordering requirements. Distinguish application assumptions from constraints enforced by the database.
3. For mutations, trace transaction atomicity, isolation, competing writers, retry/idempotency, and partial-failure behavior. Identify lost-update, duplicate-write, and inconsistent-read scenarios.
4. For schema changes, specify compatibility across old/new application versions, backfill ordering/batching, lock exposure, validation, cutover, and rollback limits. Account for existing rows and migration failure midway. Route architectural schema design through af-engineering.
5. For query changes, inspect predicates, joins, indexes, pagination stability, result cardinality, and N+1 access. Use measured plans/cardinality rather than assuming an index improves performance.
6. Return the concrete schema/query/transaction proposal, integrity constraints, migration hazards, unknowns, and recommended checks.

## Invariants
- Database constraints enforce durable uniqueness/references when required; application prechecks alone do not prevent races.
- A transaction covers all operations that must commit together; retry policy preserves side-effect semantics.
- Parameter binding separates data from query syntax. Dynamic identifiers follow an explicit allowlist.
- Pagination has deterministic ordering; destructive migrations identify data-loss and rollback limits before action.

## Verification recommendations
Recommend existing migration/test scripts against an authorized disposable database, including populated old schema, forward migration, failed migration, duplicate/concurrent writes, and rollback only where supported. Recommend safe EXPLAIN and representative query fixtures; EXPLAIN ANALYZE executes queries and needs appropriate authorization/environment. Never infer production safety from an empty database. Escalate unknown engine semantics, inaccessible representative data, and irreversible migration approval needs explicitly.
