---
title: Architecture
layout: minimal
nav_order: 2
has_children: true
last_modified_date: 2026-04-05 00:00:00 +0000
---

# Architecture

> Software design principles, patterns, domain modeling, and diagramming techniques.

## Pages

- [Principles](./principles.md) — **OOP** principles: abstraction, encapsulation, inheritance, and polymorphism
- [SOLID](./solid.md) — **SOLID** programming principles for object-oriented application design
- [Domain Driven Design](./ddd.md) — *Domain-Driven Design* (Eric Evans): bounded contexts, aggregates, and ubiquitous language
- [Strengthening Your Domain](./domain-strength.md) — *Jimmy Bogard's* techniques for building rich domain models
- [Design Patterns](./design-patterns.md) — **GoF** (Gang of Four) design patterns: creational, structural, and behavioral
- [UML](./uml.md) — UML class diagrams: relationships, components, and notation
- [Structurizr](./structurizr.md) — `Structurizr` **C4 model** architecture-as-code tooling and static site generators
- [Modular Monoliths](./modular-monolith.md) — **modular monolith** architecture: blog series on _DDD_, migration to microservices, and bounded contexts
- [Event Sourcing](./event-sourcing.md) — `Marten` document DB and event store on PostgreSQL, **CQRS** command handler workflow, and the Critter Stack

## Resources

Awesome Software Architecture [1a] — a curated list of articles, videos, and resources to learn and practice software architecture, patterns, and principles; source [2a]

[1a]: https://awesome-architecture.com/
[2a]: https://github.com/mehdihadeli/awesome-software-architecture/tree/main

## CQRS

**CQRS** (Command Query Responsibility Segregation) topic on GitHub [cqrs-topic] \
Awesome .NET Tips — CQRS link collection [cqrs-awesome] \
`kgrzybek/modular-monolith-with-ddd` — full **modular monolith** application with _DDD_ and **CQRS** approach [kgrzybek-mm] \
ASP.NET Core CRUD with **CQRS** and `MediatR` [yogyogi-cqrs] \
`Xer.Cqrs.CommandStack` on NuGet [xer-nuget] / GitHub [xer-gh] \
`Its.Cqrs` library [its-cqrs] \
GitHub search examples for **CQRS** [cqrs-search]

`Revo` Framework Task List sample — **CQRS** and _event sourcing_ with `Revo` [revo-tasklist] \
**CQRS** with `MediatR` in ASP.NET Core (Code Maze) [cqrs-codemaze]

[<<](/index.md)

[cqrs-topic]: https://github.com/topics/ddd-cqrs
[cqrs-awesome]: https://github.com/AdrienTorworthy/awesome-dotnet-tips#cqrs
[kgrzybek-mm]: https://github.com/kgrzybek/modular-monolith-with-ddd
[yogyogi-cqrs]: https://www.yogihosting.com/aspnet-core-cqrs-mediatr/
[xer-nuget]: https://www.nuget.org/packages/Xer.Cqrs.CommandStack/
[xer-gh]: https://github.com/XerProjects/Xer.Cqrs.CommandStack
[its-cqrs]: https://github.com/AdemCatworthy/Its.Cqrs
[cqrs-search]: https://github.com/search?q=cqrs&type=repositories
[revo-tasklist]: https://github.com/revoframework/Revo/tree/develop/Examples/Revo.Examples.Todos
[cqrs-codemaze]: https://code-maze.com/cqrs-mediatr-in-aspnet-core/
