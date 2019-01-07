# Service Oriented Architectures / Microservices

- [Microservices Architecture (Pluralsight Course)](./soa/Microservices-Architecture.md) [![Pluralsight course wiki page](https://img.shields.io/badge/Pluralsight-wiki-red.svg)](./soa/Microservices-Architecture.md)
- [Microservices with .NET (recipes)](./soa/Microservices-with-.NET.md), work in progress
- [Docker](./soa/Docker.md) [![page](https://img.shields.io/badge/wiki-page-green.svg)](soa/Docker.md)
- test APIs with [Swagger](./soa/Swagger.md) [![page](https://img.shields.io/badge/wiki-page-green.svg)](soa/Swagger.md)
- [Nanoservices](./soa/nanosvc.md) anti-pattern
- [REST](rest.md) [![page](https://img.shields.io/badge/wiki-page-green.svg)](rest.md)
- [Azure](soa/azure.md) [![page](https://img.shields.io/badge/wiki-page-green.svg)](soa/azure.md)
- [REST vs XML-RPC vs SOAP](https://maxivak.com/rest-vs-xml-rpc-vs-soap/)  – pros and cons
- [REST vs. RPC](https://cloud.google.com/blog/products/application-development/rest-vs-rpc-what-problems-are-you-trying-to-solve-with-your-apis): what problems are you trying to solve with your APIs?
- [apache/thrift](https://github.com/apache/thrift/tree/master/tutorial), Thrift: Scalable Cross-Language Services Implementation [paper](https://thrift.apache.org/static/files/thrift-20070401.pdf)
- apache [aurora](http://aurora.apache.org/documentation/latest/features/service-discovery/) svc discovery
- Apache [Parquet](https://parquet.apache.org/) is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language.
- The [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) API, C# Websockets for all platforms using native bridges [PCL](https://github.com/NVentimiglia/Websockets.PCL), Building Real-time Web Apps with ASP.NET [WebAPI and WebSockets](https://blogs.msdn.microsoft.com/youssefm/2012/07/17/building-real-time-web-apps-with-asp-net-webapi-and-websockets/), [signalr](http://signalr.net/), [Bringing Sockets to the Web](https://www.html5rocks.com/en/tutorials/websockets/basics/), [SuperWebSocket](https://archive.codeplex.com/?p=superwebsocket), [desktop to web socket](https://isolasoftware.it/2012/05/04/how-to-send-live-data-from-a-c-desktop-application-to-web-using-websockets/)

## todo

- [Event Hubs](https://azure.microsoft.com/en-us/services/event-hubs/) Simple, secure, and scalable real-time data ingestion
- [Azure Service Fabric](https://azure.microsoft.com/en-us/services/service-fabric/) Build and operate always-on, scalable, distributed apps
- *NServiceBus* [quickstart](https://docs.particular.net/tutorials/quickstart/), [Message Handling Pipeline](https://docs.particular.net/nservicebus/pipeline/), [transport](https://docs.particular.net/transports/azure-service-bus/), versus [MassTransit](http://looselycoupledlabs.com/2014/11/masstransit-versus-nservicebus-fight/)
- `NServiceBus.Transport.AzureServiceBus` Azure Service Bus transport for NServiceBus, [nuget](https://www.nuget.org/packages/NServiceBus.Transport.AzureServiceBus/) & [docs](https://docs.particular.net/nservicebus/hosting/publishing-from-web-applications)
- [JustSaying](https://github.com/justeat/JustSaying) A light-weight message bus on top of AWS services (SNS and SQS).
- Implementing event-based communication between microservices: [integration events](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/multi-container-microservice-net-applications/integration-event-based-microservice-communications)
- eShopOnContainers/src[/BuildingBlocks/EventBus/](https://github.com/dotnet-architecture/eShopOnContainers/tree/master/src/BuildingBlocks/EventBus)
- [store app secrets](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/secure-net-microservices-web-applications/developer-app-secrets-storage) ASP.NET Core
- [Infrastructure Ignorance](https://ayende.com/blog/3137/infrastructure-ignorance)
- **Streaming APIs** [gitter.im](https://developer.gitter.im/docs/streaming-api), [http-streaming](https://realtimeapi.io/hub/http-streaming/). HTTP Streaming provides a _long-lived connection_ for _continuous data push_. The client sends a request to the server and the _server holds the response open for an indefinite length_. This connection will stay open until _a client closes it_ or a _server side-side event occurs_.
- [By 2020, 50% of Managed APIs Projected to be Event-Driven](https://realtimeapi.io/2020-50-percent-managed-apis-projected-event-driven/)
- [Real-time applications using ASP.NET Core, SignalR & Angular ](https://chsakell.com/2016/10/10/real-time-applications-using-asp-net-core-signalr-angular/) oct 16 & [demo app](https://github.com/chsakell/aspnet-core-signalr-angular)
- [awesome-dotnet](https://github.com/quozd/awesome-dotnet) A collection of awesome .NET libraries, tools, frameworks and software
- [.NET/C# Realtime Resources](https://realtimeapi.io/hub/dotnet-c-realtime-resources/)
- [Getting Started with Building Realtime API Infrastructure](https://realtimeapi.io/getting-started-with-building-realtime-api-infrastructure/)

[home](../README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki)