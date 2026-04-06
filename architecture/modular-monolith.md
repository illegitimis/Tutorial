---
title: Modular Monoliths
layout: default
nav_order: 8
parent: Architecture
last_modified_date: 2026-04-05 00:00:00 +0000
---

# Modular Monoliths

> A **modular monolith** combines the simplicity of a monolithic deployment with the modularity of well-defined bounded contexts.

Daniel _dandoescode_ Mackay: 01 A Gentle Introduction [1], 02 Implementation Deep Dive [2], 03 Simplifying the Inner Development Loop with `.NET Aspire` [3]; blog source [4]

Milan Jovanovic: 01 What Is a Modular Monolith? [5], 02 Monolith to Microservices: How a Modular Monolith Helps [6], 02A Breaking It Down: How to Migrate Your Modular Monolith to Microservices [7], 03 Communication Patterns [8], 03A **Outbox Pattern** for Reliable Microservices Messaging [9], 04 Data Isolation [10], 04A Using Multiple `EF Core` DbContexts in a Single Application [11]

Norbert Debosz 4 _itnext_ **Easy Modular Monolith**: code [12]; 01 MVP [13]; 02 The **Outbox Pattern** [14]; 03 Logging (`Serilog` and `Seq`) [15]; 04 Global Exception Handling [16]; 05 **JWT** Authentication/Authorization [17]; 06 Synchronous Communication Between Modules [18]

Kamil Grzybek: root [19]; 01 A Primer [20], 02 Architectural Drivers [21], 03 Architecture Enforcement [22], 04 Integration Styles [23], 05 _Domain-Centric Design_ [24]; full **modular monolith** application with _Domain-Driven Design_ approach [25]

_The Reformed Programmer_ 01 Using **Modular Monolith** and _DDD_ Architectures [26]; 02 Using _Clean Architecture_ with a **Modular Monolith** [27]; Evolving Modular Monoliths: 1. An Architecture for .NET [28]; 2. Breaking Up Your App into Multiple Solutions [29]; 3. Passing Data Between Bounded Contexts [30]

## Additional Resources

GitHub monolith topic [31] \
The Majestic Monolith [32] \
Majestic Modular Monoliths [33] \
Towards Modern Development of Cloud Applications [34] \
_Monolith First_ [35] \
A Practical Guide to Modular Monoliths with .NET [36] \
`AdaptiveClient` — library and pattern for creating a scalable, loosely coupled service layer [37] \
`MediatR.Examples.Lamar` sample [38] \
Cloud Computing — Building Distributed Applications With .NET Services (MSDN, 2009) [39]

[<](./index.md) | [<<](/index.md)

[1]: https://www.dandoescode.com/blog/modular-monolith/a-gentle-introduction
[2]: https://www.dandoescode.com/blog/modular-monolith/implementation-deep-dive
[3]: https://www.dandoescode.com/blog/modular-monolith/simplifying-the-inner-dev-loop-with-aspire
[4]: https://github.com/danielmackay/nextjs-personal-blog/tree/main/data/blog/modular-monolith
[5]: https://www.milanjovanovic.tech/blog/what-is-a-modular-monolith
[6]: https://www.milanjovanovic.tech/blog/monolith-to-microservices-how-a-modular-monolith-helps
[7]: https://www.milanjovanovic.tech/blog/breaking-it-down-how-to-migrate-your-modular-monolith-to-microservices
[8]: https://www.milanjovanovic.tech/blog/modular-monolith-communication-patterns
[9]: https://www.milanjovanovic.tech/blog/outbox-pattern-for-reliable-microservices-messaging
[10]: https://www.milanjovanovic.tech/blog/modular-monolith-data-isolation
[11]: https://www.milanjovanovic.tech/blog/using-multiple-ef-core-dbcontext-in-single-application
[12]: https://github.com/Ridikk12/ModularMonolith/blob/modules_communication/README.md
[13]: https://itnext.io/easy-modular-monolith-part-1-mvp-d57f47935e24
[14]: https://itnext.io/easy-modular-monolith-part-2-the-outbox-pattern-b4566724fb68
[15]: https://itnext.io/easy-modular-monolith-part-3-logging-57caceac1ff5
[16]: https://itnext.io/easy-modular-monolith-part-4-global-exception-handling-8355cc4905d4
[17]: https://itnext.io/easy-modular-monolith-part-5-jwt-authentication-authorization-f7a0a275226f
[18]: https://itnext.io/easy-modular-monolith-part-5-synchronous-communication-between-modules-7af876f06c16
[19]: https://www.kamilgrzybek.com/blog/categories/modular-monolith
[20]: https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer
[21]: https://www.kamilgrzybek.com/blog/posts/modular-monolith-architectural-drivers
[22]: https://www.kamilgrzybek.com/blog/posts/modular-monolith-architecture-enforcement
[23]: https://www.kamilgrzybek.com/blog/posts/modular-monolith-integration-styles
[24]: https://www.kamilgrzybek.com/blog/posts/modular-monolith-domain-centric-design
[25]: https://github.com/kgrzybek/modular-monolith-with-ddd
[26]: https://www.thereformedprogrammer.net/my-experience-of-using-modular-monolith-and-ddd-architectures/
[27]: https://www.thereformedprogrammer.net/my-experience-of-using-the-clean-code-architecture-with-a-modular-monolith/
[28]: https://www.thereformedprogrammer.net/evolving-modular-monoliths-1-an-architecture-for-net/
[29]: https://www.thereformedprogrammer.net/evolving-modular-monoliths-2-breaking-up-your-app-into-multiple-solutions/
[30]: https://www.thereformedprogrammer.net/evolving-modular-monoliths-3-passing-data-between-bounded-contexts/
[31]: https://github.com/topics/monolith
[32]: https://signalvnoise.com/svn3/the-majestic-monolith/
[33]: https://hajdu.tech/post/majestic-modular-monolith/
[34]: https://dl.acm.org/doi/pdf/10.1145/3593856.3595909
[35]: https://martinfowler.com/bliki/MonolithFirst.html
[36]: https://www.reddit.com/r/dotnet/comments/197brd5/a_practical_guide_to_modular_monoliths_with_net/
[37]: https://github.com/leaderanalytics/adaptiveclient
[38]: https://github.com/LuckyPennySoftware/MediatR/tree/main/samples/MediatR.Examples.Lamar
[39]: https://learn.microsoft.com/en-us/archive/msdn-magazine/2009/june/cloud-computing-building-distributed-applications-with-net-services
