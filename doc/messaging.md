# Messaging 

- [Apache Kafka](./msg/ApacheKafka.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./msg/ApacheKafka.md)
- [MPI](./msg/MPI.md), _todo_
- [ZeroMQ](./msg/ZeroMQ.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./msg/ZeroMQ.md)

## todo

- [CQRS and Event Sourcing Pattern with NServiceBus, EventStore, WebAPI and Unity](https://code.msdn.microsoft.com/CQRS-and-Event-Sourcing-3d194cc1/sourcecode?fileId=137884&pathId=1747397666)
- [5 Protocols For Event-Driven API Architectures](https://nordicapis.com/5-protocols-for-event-driven-api-architectures/): WebSockets, WebHooks, [Rest hooks](http://resthooks.org/code/), Pub-sub and SSE
- [RestMS](http://www.restms.org/specs:stable) specs. _RESTful Messaging Service_ provides web applications with enterprise-level messaging via an asynchronous RESTful interface that works over standard HTTP/HTTPS. Hintjens @ [imatix](http://www.imatix.com/)
- [EventStore](https://eventstore.org/) The open-source, functional database with Complex Event Processing in JavaScript. [Connecting to a Server](https://eventstore.org/docs/dotnet-api/connecting-to-a-server/index.html), [Rolling Snapshots](https://eventstore.org/docs/event-sourcing-basics/rolling-snapshots/index.html), [get started](https://eventstore.org/docs/getting-started/index.html?tabs=tabid-1%2Ctabid-dotnet-client%2Ctabid-dotnet-client-connect%2Ctabid-4)
- [How to run Background Tasks in ASP.NET](https://www.hanselman.com/blog/HowToRunBackgroundTasksInASPNET.aspx)
- Brighter [home](https://www.goparamore.io/). _Command Dispatcher, Processor, and Distributed Task Queue_. [git](https://github.com/BrighterCommand/Brighter). [MessagingGateway.RESTMS](https://libraries.io/nuget/Paramore.Brighter.MessagingGateway.RESTMS), [CommandInvoker](http://servicedesignpatterns.com/WebServiceImplementationStyles/CommandInvoker)
soa design pattern. [cqrs](https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf) pdf. [basic](https://paramore.readthedocs.io/en/latest/BasicConfiguration.html) conf. [messaginggateway.rmq](https://libraries.io/nuget/paramore.brighter.commandprocessor.messaginggateway.rmq) messaging gateway for decoupled invocation in the Paramore.Brighter.CommandProcessor pipeline, using RabbitMQ. aspnetcore/nginx [tutorial](https://github.com/iancooper/ProgNetNginx). `topshelf` [docs](https://topshelf.readthedocs.io/en/latest/configuration/config_api.html#service-identity).
.NET Core [integration](https://github.com/BrighterCommand/Paramore.Brighter.Extensions) for `Brighter`. [Darker](https://github.com/BrighterCommand/Darker) The query-side counterpart of Brighter [src](https://github.com/BrighterCommand/Brighter/tree/master/src), [tooling](https://github.com/BrighterCommand/Tools). Implementing a Distributed Task Queue [docs](https://paramore.readthedocs.io/en/latest/ImplementingDistributedTaskQueue.html#what-happens-when-the-consumer-receives-the-message). `todo project` implementations [1](https://github.com/BrighterCommand/todo-backend-aspnetcore-brighter), [2](https://github.com/BrighterCommand/FutureStack/tree/master/ToDoBackend/src/ToDoCore), [main](https://www.todobackend.com/index.html#implementations)


https://github.com/HangfireIO/Hangfire/blob/f970f56a1bacbfa762a9db9030cadabc5e0b9cb2/src/Hangfire.Core/Server/ServerProcessExtensions.cs#L57

[home](README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki) 
