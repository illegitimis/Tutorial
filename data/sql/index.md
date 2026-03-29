# SQL

> Relational database fundamentals, SQL Server patterns, schema management, and platform-specific guides.

## Pages

- [ACID](./acid.md) — **ACID** properties: Atomicity, Consistency, Isolation, and Durability
- [Indexes](./indexes.md) — index types, unique constraints, and `GetIndices.sql` reference
- [Connection Pool](./connection-pool.md) — **connection pooling**: pool management, reuse, and lifetime
- [DAO vs Repository](./dao-vs-repository.md) — **DAO** (Data Access Object) vs **Repository** pattern comparison
- [DbCommand](./db-command.md) — `IDbCommand` hierarchy and command execution patterns
- [Foreign Key Mapping](./foreign-key-mapping.md) — SQL Server foreign key queries and multi-column relationship patterns
- [Primary Keys](./primary-keys.md) — primary key queries via `INFORMATION_SCHEMA`
- [Referential Integrity](./referential-integrity.md) — referential integrity enforcement with indices and primary keys
- [Service Broker](./service-broker.md) — SQL Server **Service Broker** for asynchronous messaging within the database
- [String Search Stored Proc](./string-search-stored-proc.md) — stored procedure for searching text across database objects
- [Table Schema](./table-schema.md) — `sysobjects` vs `sys.objects` and schema introspection queries
- [Temporary Tables](./temporary-tables.md) — temporary table types, scope, and performance advantages
- [Views](./views.md) — SQL views: parameterized defaults and view-based query patterns
- [Samples](./samples.md) — Microsoft sample databases: Northwind and pubs for SQL Server 2000
- [MySQL](./mysql.md) — `MySQL` setup, configuration, and .NET integration
- [PostgreSQL](./postgresql.md) — `PostgreSQL` with `Npgsql` and `Npgsql.EntityFrameworkCore.PostgreSQL`

## Scripts

The `scripts/` folder contains sample SQL installation scripts:

- `instnwnd.sql` — Northwind sample database installation script
- `instpubs.sql` — pubs sample database installation script

[<<](../index.md) | [home](../../README.md)
