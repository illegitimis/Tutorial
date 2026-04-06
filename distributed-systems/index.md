---
title: Distributed Systems
layout: minimal
nav_order: 6
has_children: true
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# Distributed Systems

> Microservices architecture, containerization, messaging systems, real-time communication, and cloud services.

## Pages

- [Microservices Architecture](./microservices-architecture.md) — Pluralsight course on *microservices architectural style*: decomposition, patterns, and trade-offs
- [Microservices with .NET](./microservices-dotnet.md) — implementing microservices in .NET: independently deployable services built around business capabilities
- [Docker](./docker.md) — `Docker` containers for independent deployment, scalability, and portability of microservices
- [Nanoservices](./nanoservices.md) — **nanoservice** anti-pattern: services too fine-grained where overhead outweighs utility
- [SignalR](./signalr.md) — `SignalR` for real-time web: hub protocol, ASP.NET Core integration, and Angular demo
- [WebSockets](./websockets.md) — full-duplex messaging: no connection limit, multi-data-type support
- [Kafka](./kafka.md) — `Apache Kafka` distributed event streaming: .NET clients and Pluralsight course notes
- [ZeroMQ](./zeromq.md) — `ZeroMQ` high-performance asynchronous messaging library
- [Azure Services](./azure-services.md) — Azure distributed services: Cosmos DB, Azure Stack, and cloud integrations
- [Distributed Tracing](./distributed-tracing.md) — **distributed tracing** with `OpenTelemetry`, W3C **Trace Context**, and `System.Diagnostics.Activity`
- [Kubernetes](./kubernetes.md) — `Kubernetes` container orchestration: courses, resources, and architecture origins
- [Service Fabric](./service-fabric.md) — `Service Fabric` distributed platform for stateless and stateful applications at scale

## Messaging Patterns

- **CQRS** (Command Query Responsibility Segregation) and **Event Sourcing** with `NServiceBus` and `EventStore`
- `NServiceBus` — message handling pipeline, Azure Service Bus transport, and publishing from web applications
- `MassTransit` — open-source service bus for .NET; compared with NServiceBus
- `Hangfire` — background job processing and recurring task scheduling in ASP.NET
- **Brighter** — Command Dispatcher, Processor, and Distributed Task Queue with RabbitMQ gateway
- *Event-Driven API Architectures*: WebSockets, WebHooks, Pub-Sub, and SSE (Server-Sent Events)
- **Streaming APIs**: HTTP streaming with long-lived connections for continuous data push

## SOA References

- `Apache Thrift` — scalable cross-language services implementation
- **Integration Events** — event-based communication between microservices using an event bus abstraction
- *JustSaying* — lightweight message bus on top of AWS SNS and SQS

## Game Server Resources

`NetCoreServer` — cross-platform UDP/TCP/HTTP server [1d]; HTTP server docs [2d] \
`Stateless` 3.0 — state machine library for .NET [3d] \
`Akka.NET` discovery [4d] \
PoisonousJohn/TanksNetworkingInAzure [5d] \
`Photon` server framework [6d] [7d] \
Asynchronous server socket example [8d] \
Game engine best practices [9d]

[<<](/index.md)

[1d]: https://github.com/chronoxor/NetCoreServer#example-udp-multicast-server
[2d]: https://chronoxor.github.io/NetCoreServer/#example-http-server
[3d]: https://www.hanselman.com/blog/stateless-30-a-state-machine-library-for-net-core
[4d]: https://getakka.net/articles/discovery/index.html
[5d]: https://github.com/PoisonousJohn/TanksNetworkingInAzure
[6d]: https://github.com/t13ka/photon_server_framework/tree/master/YourGame.Server/packages
[7d]: https://doc.photonengine.com/en-us/realtime/current/getting-started/onpremises-or-saas
[8d]: https://docs.microsoft.com/en-us/dotnet/framework/network-programming/asynchronous-server-socket-example
[9d]: https://stackoverflow.com/questions/4576982/are-there-best-practices-for-implementing-an-asynchronous-game-engine-loop
