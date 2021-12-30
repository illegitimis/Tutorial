# .Net Core

## links

- [Building a Web App with ASP.NET Core, MVC 6, EF Core, and Angular](./netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md) [![Pluralsight course wiki page](https://img.shields.io/badge/Pluralsight-wiki-red.svg)](./netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md)
- [AspNetCore Rest](rest.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](rest.md)
- [blazor](./netcore/blazor.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./netcore/blazor.md)
- [Northwind Traders](https://github.com/JasonGT/NorthwindTraders) is a sample application built using ASP.NET Core and Entity Framework Core.
- [eShopOnWeb](https://github.com/dotnet-architecture/eShopOnWeb) Sample ASP.NET Core 2.1 reference application, powered by Microsoft, demonstrating a layered application architecture with monolithic deployment model.
- [commands](./netcore/commands.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./netcore/commands.md)
- [middleware](./netcore/middleware.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./netcore/middleware.md)
- [authorization](./netcore/authorization.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./netcore/authorization.md)
- [attributes](./netcore/attrib.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./netcore/attrib.md)
- [reverse package search](https://packagesearch.azurewebsites.net/)
- [Mapping between csproj and project.json](https://docs.microsoft.com/en-us/dotnet/core/tools/project-json-to-csproj)
- [Setting `EnableDefaultCompileItems` to False doesn't remove the files from solution Explorer](https://github.com/dotnet/sdk/issues/1157)
- In-memory caching in ASP.NET Core
  - add `microsoft.extensions.caching.memory`
  - [In-memory caching is a service](https://docs.microsoft.com/en-us/aspnet/core/performance/caching/memory) that is referenced from your app using `Dependency Injection`. Call `AddMemoryCache` in `ConfigureServices`
- [ASP.NET Core](https://github.com/aspnet/home) The Home repository is the starting point for people to learn about ASP.NET Core.
- [NET Core 2.1 Roadmap](https://blogs.msdn.microsoft.com/dotnet/2018/02/02/net-core-2-1-roadmap/) February 2, 2018 by Rich Lander [MSFT] on .NET Blog
- [ASP.NET Core 2.1 roadmap](https://blogs.msdn.microsoft.com/webdev/2018/02/02/asp-net-core-2-1-roadmap/) Feb 2018
- [ASP.NET Core vs Go data ingestion benchmark](https://stefanprodan.com/2016/aspnetcore-vs-golang-data-ingestion-benchmark/)
- [Filters](https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/filters) dec16
- **Options** _pattern_ in ASP.NET Core
  - official [docs](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options?view=aspnetcore-2.2) 2.2
  - How to use the `IOptions` pattern for configuration in ASP.NET Core RC2 [blog](https://andrewlock.net/how-to-use-the-ioptions-pattern-for-configuration-in-asp-net-core-rc2/) 2016
  - Access services inside `ConfigureServices` using `IConfigureOptions` in ASP.NET Core [blog](https://andrewlock.net/access-services-inside-options-and-startup-using-configureoptions/)
  - populating `IOptions<T>` from external data source [blog](https://tpodolak.com/blog/2017/02/26/asp-net-core-populating-ioptions-external-data-source/)

[home](../README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki)
