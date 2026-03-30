---
title: Distributed Systems
layout: minimal
nav_order: 6
has_children: true
last_modified_date: 2026-03-30 00:00:00 +00:00
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

[<<](/index.md)
