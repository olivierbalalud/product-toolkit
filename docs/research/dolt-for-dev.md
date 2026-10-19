# Dolt / Doltgres as a Dev Database

Status: fact check, 2026-10-20 (WebFetch, WebSearch, GitHub API). Question: could Dolt replace PostgreSQL 16 **for development only**, with one database branch per git worktree, for a FastAPI + SQLAlchemy 2 + Alembic + psycopg stack that uses pgvector, RLS policies and roles/GRANTs? Nothing was installed or run. "(inferred)" marks a point that was not verified directly.

## Sources

| # | Source | URL |
|---|---|---|
| S1 | Doltgres README | <https://github.com/dolthub/doltgresql> |
| S2 | Doltgres releases (GitHub API) | <https://api.github.com/repos/dolthub/doltgresql/releases> |
| S3 | Doltgres 1.0 launch post (2026-08-06) | <https://www.dolthub.com/blog/2026-08-06-doltgres-1-0/> |
| S4 | "Doltgres 1.0 Coming August 6th" (2026-06-26) | <https://www.dolthub.com/blog/2026-06-26-doltgres-1-0-coming-this-fall/> |
| S5 | "Doltgres is as Fast as MySQL is Slow" (2026-08-13) | <https://www.dolthub.com/blog/2026-08-13-doltgres-as-fast-as-mysql-is-slow/> |
| S6 | Dolt/Doltgres roadmap | <https://www.dolthub.com/docs/other/roadmap/> |
| S7 | Q4 roadmap update (2026-10-07) | <https://www.dolthub.com/blog/2026-10-07-roadmap-update/> |
| S8 | Doltgres supported SQL commands | <https://www.doltgres.com/docs/reference/sql-support/supported-commands> |
| S9 | Doltgres supported types | <https://www.doltgres.com/docs/reference/sql-support/supported-types> |
| S10 | Doltgres v1.3.0 release notes (pgvector emulation, PR #3126) | <https://github.com/dolthub/doltgresql/releases/tag/v1.3.0> |
| S11 | "Doltgres Now Emulates Extensions" (2026-09-03) | <https://dolthub.com/blog/2026-09-03-doltgres-extensions-update/> |
| S12 | Doltgres v1.4.0 release notes | <https://github.com/dolthub/doltgresql/releases/tag/v1.4.0> |
| S13 | "Getting Started: SQLAlchemy and Doltgres" (2025-07-18) | <https://www.dolthub.com/blog/2025-07-18-sql-alchemy-getting-started-doltgres/> |
| S14 | psycopg issue #1422 (segfault with Doltgres 1.0) | <https://github.com/psycopg/psycopg/issues/1422> |
| S15 | Doltgres PR #3614 (bot QA report: DDL survives ROLLBACK) | <https://github.com/dolthub/doltgresql/pull/3614> |
| S16 | Doltgres issues #3544, #3608, #3279, #3617 | <https://github.com/dolthub/doltgresql/issues> |
| S17 | Dolt README | <https://github.com/dolthub/dolt> |
| S18 | Dolt releases (GitHub API) | <https://api.github.com/repos/dolthub/dolt/releases> |
| S19 | Dolt docs: branches | <https://www.dolthub.com/docs/sql-reference/version-control/branches> |
| S20 | Dolt docs: merges | <https://www.dolthub.com/docs/sql-reference/version-control/merges> |
| S21 | Dolt vector indexes / VECTOR type posts | <https://www.dolthub.com/blog/2025-01-16-announcing-vector-indexes/>, <https://www.dolthub.com/blog/2025-08-08-vector-type/> |
| S22 | DoltHub pricing; DoltHub Pro $5/month (2026-04-24) | <https://www.dolthub.com/pricing>, <https://www.dolthub.com/blog/2026-04-24-announcing-dolthub-pro-for-5-dollars-per-month/> |
| S23 | "PostgreSQL Database Clones vs. Doltgres Branches" (2026-10-01) | <https://www.dolthub.com/blog/2026-10-01-postgres-cheap-database-clones/> |
| S24 | PostgreSQL 18: CREATE DATABASE; `file_copy_method` | <https://www.postgresql.org/docs/current/sql-createdatabase.html>, <https://www.postgresql.org/docs/18/runtime-config-resource.html> |
| S25 | Neon repo (self-host, branching) | <https://github.com/neondatabase/neon> |
| S26 | testcontainers-python Postgres module | <https://testcontainers-python.readthedocs.io/en/latest/modules/postgres/README.html> |
| S27 | NAlexPear/pg_branch | <https://github.com/NAlexPear/pg_branch> |
| S28 | Dolt docs: SQL procedures (implicit commits) | <https://docs.dolthub.com/sql-reference/version-control/dolt-sql-procedures> |
| S29 | Doltgres Beta launch (2025-04-16) | <https://www.dolthub.com/blog/2025-04-16-doltgres-goes-beta/> |

## 1. Dolt vs Doltgres, licence, offerings

| | Dolt | Doltgres (DoltgreSQL) |
|---|---|---|
| What | Git-style versioned SQL database, **MySQL**-compatible (S17) | Same engine, **PostgreSQL**-flavoured: "Dolt for Postgres" (S1) |
| Interface | SQL server + git-like CLI (S17) | SQL only, **no git-style CLI** (S1) |
| Licence | **Apache 2.0** (S17) | **Apache 2.0** (S1, LICENSE file) |
| Latest version | v2.5.0, 2026-10-17 (S18) | **v1.4.0, 2026-10-01** (S2) |
| Free edition limits | None documented. The open-source server is the full product (inferred) | Same (inferred) |

- Dolt (MySQL) does not fit this team at all: MySQL dialect, no pgvector, no RLS. The rest of this file covers **Doltgres**.
- Paid, for context (S22, read through a search snippet of the pricing page): **Hosted Dolt** from $50/month (trial instance, 50 GB), larger instances priced by size. **DoltHub Pro** $5/month above 100 MB of private data. **DoltLab** (self-hosted DoltHub) is free; Enterprise is $5,000/month. Whether Hosted Dolt offers Doltgres was not checked.

## 2. Doltgres maturity

| Signal | Value | Source |
|---|---|---|
| Stage | Alpha, then **Beta in April 2025**, then **1.0 on 2026-08-06** | S4, S3 |
| DoltHub's claim | "Doltgres is 1.0", "ready for your production use case" | S1, S3 |
| 1.0 criteria | 99% SQL Logic Test, sysbench within 3x of Postgres, storage stability (no breaking storage change in 1.x) | S4, S3 |
| Correctness | sqllogictest (5.6M queries checked against Postgres) **99.317%**, 13,197 "not ok", 7 timeouts | S1, S3 |
| Target dialect | **PostgreSQL 15** | doltgres.com SQL support page |
| Speed | sysbench mean **~2.6–2.7x Postgres latency**. Writes 2.9–3.8x, most reads 2.3–2.9x (vs Postgres 15.5) | S5, S3 |
| Since 1.0 | 1.1 → 1.4 in eight weeks. A 2026-09-04 post-mortem covers a data-loss bug hitting early Beta users who upgraded to 1.0 (not read) | S2, search result |
| Stale signal | The Dolt README still calls Doltgres "now in its Beta release" | S17 |

The listed limits are "limited extension support", no GSSAPI, and some syntax, types and functions not implemented yet (S1).

## 3. Compatibility with this team's stack

| Feature | Status | Detail | Source |
|---|---|---|---|
| PG wire protocol, PG16 clients | **Partial** | Emulates a Postgres server. It targets PG15, but the v3 wire protocol is the same for PG16 clients (inferred) | S1, SQL support page |
| psycopg 3 | **Partial** | Not on DoltHub's list (psycopg2 and asyncpg are). psycopg[binary] segfaulted on `timestamptz` because Doltgres 1.0 sends no `TimeZone` ParameterStatus. A psycopg fix closed it on 2026-09-30. The maintainer says Doltgres "is still not a supported database and is not tested" | S4, S14 |
| SQLAlchemy 2 | **Partial** | DoltHub demo uses `postgresql+psycopg2` with the 2.0 API. Workarounds: `autoincrement=False` (sequences are shared across branches), raw `text()` for ALTER | S13, S4 |
| Alembic | **Not documented** | No DoltHub material. Issues that hurt migrations: panic on ALTER COLUMN when the default calls a UDF (#3544), `DO` blocks unsupported (#3279), identity column reassigned on UPDATE (#3608) | S16 |
| Transactional DDL | **Not supported (reported)** | A bot QA run (2026-10-15) found that ROLLBACK removed the rows but kept the tables created in the same transaction. That is not an official statement | S15 |
| Transaction semantics | **Partial** | `BEGIN` isolation options are not supported. READ COMMITTED and `SELECT … FOR UPDATE` row locks are "early next year". There is an opt-in setting to ignore locking statements. Concurrent `ON CONFLICT DO UPDATE` loses updates (#3617) | S8, S7, S12, S16 |
| pgvector: type, operators | **Partial** | v1.3.0 (2026-08-28) "emulates a majority of the `pgvector` extension". Most of pgvector's own tests are ported | S10, S11 |
| pgvector: HNSW / IVFFlat indexes | **Not supported** | "the special index types which we cannot support at this moment (HNSW and IVFFlat)". Only btree `CREATE INDEX` is supported. Vector indexes are on the roadmap | S10, S8, S3 |
| `CREATE EXTENSION` | **Partial** | Supported, but not with a non-public SCHEMA, VERSION or CASCADE. Extensions are built in and emulated, not loaded: uuid-ossp and pgvector done, PostGIS in progress, pgcrypto/citext/hstore planned | S8, S11 |
| Row-level security (`CREATE/ALTER POLICY`) | **Not supported** | ❌ in the command list. Roadmap: "before the end of the year" (Q4 2026) | S8, S7, S6 |
| Roles, GRANT/REVOKE | **Partial** | CREATE/ALTER ROLE ✅. GRANT ✅ on tables, schemas, databases, sequences, routines and role grants, but not cross-database. **SET ROLE ❌, ALTER DEFAULT PRIVILEGES ❌** | S8 |
| JSON / JSONB, UUID, arrays | Supported | `json`, `jsonb`, `uuid` and their arrays. Multidimensional arrays and JSON_TABLE since v1.4.0 | S9, S12 |
| Sequences, serial | Supported | `CREATE SEQUENCE`, serial2/4/8. Identity columns are not listed among the types | S8, S9 |
| Enum types | Supported | `CREATE TYPE` covers composite, enum and shell types; not range or base types | S8 |
| Triggers, functions | Partial | Row-level BEFORE/AFTER INSERT/UPDATE/DELETE triggers only. Functions in PL/pgSQL, SQL and C | S8 |
| CTEs | Not documented here | Listed as a gap at the 2025 beta. Current status not found | S29 (search snippet) |
| LISTEN/NOTIFY, COPY TO | Not supported | LISTEN/NOTIFY due Q1 2027. COPY FROM works for text and CSV | S8, S6 |

## 4. Branching model

| Topic | Fact | Source |
|---|---|---|
| Model | Commits, branches, three-way merge with a common ancestor. Cheap branching: `SELECT dolt_branch('x','main')` only adds a pointer | S20, S23 |
| Diff | `dolt_diff_<table>` system tables and the `dolt_diff()` table function. Row-level diffs across history | S13, S23 |
| Merge | `DOLT_MERGE()`. Cell-level data conflicts land in `dolt_conflicts_<table>`, schema conflicts in `dolt_schema_conflicts` (resolving takes a whole table from one side), FK/unique violations in `dolt_constraint_violations` | S20 |
| Selecting a branch | Connection string `dbname/branch`, `USE "db/branch"`, or `dolt_checkout()` per session. DoltHub recommends the connection string over checkout, because of pooled sessions | S19, S13 |
| Many branches, one server | Yes. Each branch behaves as its own isolated database, and clients on different branches work concurrently. One transaction may commit to only one branch | S19 |
| Fit for worktrees | One Doltgres server with one branch per worktree, set through each worktree's `DATABASE_URL` (inferred from S19) | — |
| Caveats | ~2.6x Postgres latency (S5). Sequence/auto-increment values are shared across branches (S13). `dolt_branch` and `dolt_checkout -b` implicitly commit the open transaction (S28). Branch metadata is not versioned; recover with `dolt_reflog()` (S19) | S5, S13, S19 |

## 5. Postgres-native alternatives (one DB per worktree)

| Option | How | Limits | Source |
|---|---|---|---|
| `CREATE DATABASE wt1 TEMPLATE dev` | Copies a whole DB inside one cluster. Default `WAL_LOG` strategy (best for small DBs). Extensions, policies and grants inside the DB are copied (inferred) | **No other session may be connected to the template.** Roles are cluster-wide, so they are shared by all copies | S24, S23 |
| `STRATEGY FILE_COPY` + `file_copy_method = CLONE` | PG18 only. Uses `copy_file_range()`, so copy-on-write on XFS, Btrfs or ZFS | Checkpoints before and after the copy. The team runs PG16 | S24, S23 |
| Neon | Copy-on-write branches, each with its own Postgres endpoint. **Apache 2.0, self-hostable** through `cargo neon` local setup (pageserver, safekeeper, broker) | Self-host means building from source. "Neon Local" is a proxy to Neon cloud, not offline | S25 |
| Testcontainers | `PostgresContainer("postgres:16")` gives a throwaway container per test run or worktree. Any image works, e.g. one with pgvector (inferred) | Docker needed. Default driver is psycopg2; set `driver=` | S26 |
| pg_branch (NAlexPear) | Extension that turns `CREATE DATABASE` into a Btrfs snapshot | Experimental, Linux only, last update 2023 | S27 |

DoltHub's own comparison: clones suit migration development, CI and disposable copies. Dolt branches add diff and merge between copies (S23).

## Fit for this team

**Blockers (facts as of 2026-10-20):**
- **RLS not supported** (`CREATE POLICY` ❌). It is only promised for Q4 2026.
- **pgvector partial**: no HNSW or IVFFlat indexes. Similarity search works without them (inferred), but index DDL in migrations would fail.
- **SET ROLE and ALTER DEFAULT PRIVILEGES unsupported**, so role-switching tests and default-privilege migrations cannot run.
- **psycopg 3 and Alembic are not on any DoltHub list**. psycopg 3 already hit a crash. DDL appears to be non-transactional, so a failed Alembic migration can leave a half-applied schema.
- Targets **PG15**, not PG16. Dev/prod divergence: different isolation and locking, plus open correctness issues.

**Advantages:**
- Apache 2.0, free, 1.0 with a storage-stability promise.
- One server serves many branches at once, selected by connection string. That maps directly to one `DATABASE_URL` per worktree.
- Branches are cheap, and data and schema can be diffed and merged. Plain PG clones have no merge.

## Unverified

- Whether `CREATE EXTENSION vector` and pgvector operators (`<->`, `<=>`, `<#>`) work exactly as in pgvector. The release notes say "majority".
- Whether Doltgres now sends the `TimeZone` ParameterStatus (the psycopg side is fixed).
- Whether `ALTER TABLE … ENABLE ROW LEVEL SECURITY` parses (the command list does not mention it).
- Current CTE status, and the details of the 2026-09-04 data-loss post-mortem.
- Pricing figures: read through a search snippet, the page itself did not render. Whether Hosted Dolt offers Doltgres.
- Whether Doltgres DDL is transactional: only a bot QA report, no official statement.
