---
title: Service Fabric
layout: default
nav_order: 12
parent: Distributed Systems
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Service Fabric

> `Service Fabric` is a distributed systems platform for packaging, deploying, and managing stateless and stateful distributed applications and containers at large scale.

- GitHub repository [1]
- Service Fabric home [2]
- Overview [3]
- Quickstart: Deploy a .NET reliable services application to Service Fabric [4]
- Programming model overview [5]
- Application scenarios [6]
- Prepare your development environment on Windows [7]

## Troubleshooting

- How to install and create Service Fabric cluster and nodes [8]
- How to attach Visual Studio Code to the ASP.NET Core process in the Service Fabric cluster [9]

## Init

- Install SDK, tools, runtime
- `sfproj` project types: stateless, stateful, actor, guest exe, container, stateless ASP.NET Core, stateful ASP.NET Core
- Setting up Local Dev Environment for running Service Fabric Projects [10]
- Service Fabric Onebox Docker image [11]

## Samples

- Browse Azure samples [12]
- Azure-Samples on GitHub [13]
- Getting Started samples [14]
- service-fabric-dotnet-quickstart `csproj` [15]
- service-fabric-dotnet-modernization `sfproj` [16]
- `aspnetcore-service-fabric-hosting` [17]
- How to use .NET Core's built-in Dependency Injection with Service Fabric [18]
- Set up Dependency Injection on Service Fabric using default ASP.NET Core DI container [19]

[1]: https://github.com/Microsoft/service-fabric
[2]: https://azure.microsoft.com/en-us/services/service-fabric/#overview
[3]: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-overview
[4]: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-quickstart-dotnet
[5]: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-choose-framework
[6]: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-application-scenarios
[7]: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-get-started
[8]: https://medium.com/a-layman/service-fabric-trouble-shooting-part-1-how-to-install-and-create-service-fabric-cluster-64aeaaf69657
[9]: https://medium.com/a-layman/how-to-attach-visual-studio-code-to-the-asp-net-core-process-in-the-service-fabric-cluster-831d83b7c0b0
[10]: https://eng.ms/docs/cloud-ai-platform/azure-core/azure-global-infrastructure/geneva-actions/geneva-actions-tsgs/tsgs/service-fabric/setting-up-local-dev-environment
[11]: https://hub.docker.com/_/microsoft-service-fabric-onebox
[12]: https://learn.microsoft.com/en-us/samples/browse/?filter-products=service%20fabric&languages=aspx%2Caspx-csharp%2Ccsharp&products=azure-service-fabric
[13]: https://github.com/orgs/Azure-Samples/repositories?language=&q=service-fabric&sort=&type=all
[14]: https://github.com/Azure-Samples/service-fabric-dotnet-getting-started/blob/classic/README.md
[15]: https://github.com/Azure-Samples/service-fabric-dotnet-quickstart/blob/master/VotingData/VotingData.csproj
[16]: https://github.com/Azure-Samples/service-fabric-dotnet-modernization/blob/master/sampleapp/app01/sfapp01/sfapp01.sfproj
[17]: https://github.com/coherentsolutionsinc/aspnetcore-service-fabric-hosting/blob/master/src/CoherentSolutions.Extensions.Hosting.ServiceFabric/CoherentSolutions.Extensions.Hosting.ServiceFabric.csproj
[18]: https://stackoverflow.com/questions/54696048/how-to-use-net-cores-built-in-dependency-injection-with-service-fabric
[19]: https://stackoverflow.com/questions/54185571/set-up-dependency-injection-on-service-fabric-using-default-asp-net-core-di-cont

[<](./index.md) | [<<](/index.md)
