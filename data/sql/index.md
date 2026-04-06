---
title: SQL
layout: minimal
nav_order: 2
has_children: true
parent: Data
last_modified_date: 2026-04-06 00:00:00 +00:00
---

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
- [SQL LocalDB](./localdb.md) — SQL Server Express `LocalDB` instances, firewall configuration, and Azure Storage Emulator

## Scripts

The `scripts/` folder contains sample SQL installation scripts:

- `instnwnd.sql` — Northwind sample database installation script
- `instpubs.sql` — pubs sample database installation script

## Distributed Transactions

Port Windows/MSDTC distributed transactions support [1] \
`TransactionScope` distributed transactions exception [2] \
Implement distributed/promoted transactions in `System.Transactions` [3] \
Distributed Transactions: .NET Framework vs .NET Core [4]

[<](../index.md) | [<<](/index.md)

[1]: https://github.com/dotnet/runtime/pull/72051
[2]: https://stackoverflow.com/questions/56328832/transactionscope-throwing-exception-this-platform-does-not-support-distributed-t
[3]: https://github.com/dotnet/runtime/issues/715
[4]: https://stackoverflow.com/questions/59135418/distributed-transactions-net-framework-vs-net-core
