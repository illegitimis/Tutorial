---
title: Event Sourcing
layout: default
nav_order: 9
parent: Architecture
last_modified_date: 2026-04-05 00:00:00 +0000
---

# Event Sourcing

## Marten

> .NET Transactional Document DB and Event Store on PostgreSQL

`Marten` on GitHub [1] \
`martendb.io` documentation [2]

### Samples

`FreightShipping` sample [3] \
Marten tutorial: Building a Freight and Delivery System [4] \
`AspNetCoreWithMarten` sample [5] \
`Helpdesk` sample [6] \
`EventSourcingTests.Aggregation` — aggregate stream into samples [7] \
`Core.Marten` at oskardudycz EventSourcing.NetCore [8]

### Learning

Understanding _Event Sourcing_ with `Marten` [9] \
Advanced considerations — _Optimistic Concurrency_ and deployment [10] \
**CQRS** command handler workflow for capturing events [11] \
_Integration testing_ with `Marten` [12] \
Unit testing `Query<T>` [13]

### Jargon

- **Stream aggregation process** = state rehydration / state rebuild
- _critter_ = creature (informal name for the JasperFx library ecosystem)

### The Critter Stack

The "Critter Stack" is the informal name for the set of `JasperFx` _open-source .NET libraries_ (all with animal/creature names) commonly used together to build _event-driven_, **CQRS** systems:

| Library | Role |
|---|---|
| `Marten` | PostgreSQL document DB + event store |
| `Wolverine` | Lightweight messaging / command and event bus |
| `Lamar` | Fast IoC/DI container |
| `Oakton` | Command-line / host utilities (runtime diagnostics and CLI commands) |
| `Alba` | _Integration testing_ harness for ASP.NET Core |
| `Weasel` | PostgreSQL schema management helpers (used internally by `Marten`) |

_Purpose_: Provide an opinionated, cohesive toolkit for building transactional, _event-sourced_, messaging-centric .NET applications without heavy framework overhead.

Usage pattern: `Marten` for persistence and events, `Wolverine` for commands/events and retries, `Lamar` for DI, `Oakton` for operational tooling, `Alba` for high-fidelity tests, `Weasel` for schema evolution.

## Event Sourcing with .NET

`EventSourcing.NetCore` — examples and tutorials of _Event Sourcing_ in .NET [14] \
Real-World **CQRS**/ES with ASP.NET and `Redis` Part 1 — Overview [15]

[1]: https://github.com/JasperFx/marten/tree/master
[2]: https://martendb.io/
[3]: https://github.com/JasperFx/marten/tree/master/docs/src/samples/FreightShipping
[4]: https://martendb.io/tutorials/
[5]: https://github.com/JasperFx/marten/tree/master/src/AspNetCoreWithMarten
[6]: https://github.com/JasperFx/marten/tree/master/src/samples/Helpdesk
[7]: https://github.com/JasperFx/marten/blob/master/src/EventSourcingTests/Aggregation/aggregate_stream_into_samples.cs
[8]: https://github.com/oskardudycz/EventSourcing.NetCore/tree/main/Core.Marten
[9]: https://github.com/JasperFx/marten/blob/master/docs/events/learning.md
[10]: https://martendb.io/tutorials/advanced-considerations.html
[11]: https://github.com/JasperFx/marten/blob/master/docs/scenarios/command_handler_workflow.md
[12]: https://martendb.io/testing/integration.html
[13]: https://github.com/JasperFx/marten/discussions/3428
[14]: https://github.com/oskardudycz/EventSourcing.NetCore
[15]: https://exceptionnotfound.net/real-world-cqrs-es-with-asp-net-and-redis-part-1-overview/

[<](./index.md) | [<<](/index.md)
