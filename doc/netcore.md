# .Net Core

## links

- [Building a Web App with ASP.NET Core, MVC 6, EF Core, and Angular](./netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md) [![Pluralsight course wiki page](https://img.shields.io/badge/Pluralsight-wiki-red.svg)](./netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md)
- [AspNetCore Rest](rest.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](rest.md)
- [blazor](./netcore/blazor.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./netcore/blazor.md)
- [Northwind Traders](https://github.com/JasonGT/NorthwindTraders) is a sample application built using ASP.NET Core and Entity Framework Core.
- [eShopOnWeb](https://github.com/dotnet-architecture/eShopOnWeb) Sample ASP.NET Core 2.1 reference application, powered by Microsoft, demonstrating a layered application architecture with monolithic deployment model.

## dotnet commands

[dotnet command ms docs](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet)

- **migrate** _Migrates_ a *project.json* (and _xproj_) based project to a *msbuild* based project.
- **add|list|remove reference** Adds a project reference, or deletes one, or lists all.
- **add|remove** Adds or Removes a NuGet package.
- **new console** - Initialize a sample .NET Core console application that can be compiled and run
- **build** - Build a project and its dependencies in a given directory:
- **sln** modifies a .Net Core solution file

```bash
dotnet sln toAddToMultipleProjects.sln todo-app/todo-app.csproj back-end/back-end.csproj
dotnet sln toRemoveFromWithGlobbingPattern.sln remove **/*.csproj
dotnet sln toList.sln list
```

## middleware

- Middleware samples from aspnet docs [Jan18](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?tabs=aspnetcore2x), [old](https://github.com/aspnet/Docs/tree/master/aspnetcore/fundamentals/middleware/sample)
- [Writing Custom Middleware in ASP.NET Core 1.0](https://www.exceptionnotfound.net/writing-custom-middleware-in-asp-net-core-1-0/)
- [App startup in ASP.NET Core](https://github.com/aspnet/Docs/blob/master/aspnetcore/fundamentals/startup.md), Aug17
- basic middleware samples docs [2x](https://github.com/aspnet/Docs/blob/master/aspnetcore/fundamentals/middleware/index.md), [old](https://github.com/aspnet/Docs/blob/master/aspnetcore/fundamentals/middleware.md)
- _Migrating HTTP handlers and modules to ASP.NET Core middleware_ [on Github](https://github.com/aspnet/Docs/blob/master/aspnetcore/migration/http-modules.md) and [MsDocs](https://docs.microsoft.com/en-us/aspnet/core/migration/http-modules)

## Authorization

- ASP.NET Core MVC: [Authentication And Role Based Authorization With ASP.NET Core Identity](https://social.technet.microsoft.com/wiki/contents/articles/36804.asp-net-core-mvc-authentication-and-role-based-authorization-with-asp-net-core-identity.aspx) Jan18 
- [Introduction to authorization in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/introduction)
- [ASP.NET Core Authorization with Barry Dorrans](https://channel9.msdn.com/Blogs/Seth-Juarez/ASPNET-Core-Authorization-with-Barry-Dorrans) channel9, 2016
- [blowdart/AspNetAuthorizationWorkshop](https://github.com/blowdart/AspNetAuthorizationWorkshop) github src
- [Extending Identity Accounts and Implementing Role-Based Authentication in ASP.NET MVC 5](http://johnatten.com/2013/11/11/extending-identity-accounts-and-implementing-role-based-authentication-in-asp-net-mvc-5/) nov13
- [Claims-based authorization in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/claims?view=aspnetcore-2.1) 2.1
- [Authorize](https://www.tutorialspoint.com/asp.net_core/asp.net_core_authorize_attribute.htm) attribute
- [Authorize with a specific scheme in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?tabs=aspnetcore2x)

## attributes

- Microsoft.AspNetCore.Mvc.ProducesResponseTypeAttribute

```cs
using static Microsoft.AspNetCore.Http.StatusCodes;

    [ProducesResponseType(Status200OK, Type = typeof(CommandResponse<List<SomeDto>>))]
    [ProducesResponseType(Status400BadRequest, Type = typeof(JsonErrorResponse))]
    [ProducesResponseType(Status401Unauthorized, Type = typeof(string))]
    [ProducesResponseType(Status403Forbidden, Type = typeof(string))]
    [ProducesResponseType(Status500InternalServerError, Type = typeof(JsonErrorResponse))]
```

- Microsoft.AspNetCore.Mvc.FromQuery/Body/Attribute specifies how a parameter or property should be bound, query params, request body or route-data from the current request.

```cs
public IActionResult Get([FromQuery]MessagesRequest request)
public IActionResult Get([FromQuery] int id, [FromQuery] MessageRequest request)
public async Task<IActionResult> Create([FromBody] BatchRequest batch)
[HttpPost("reject/{id:guid}")]
public async Task<IActionResult> Reject(Guid id, [FromBody] string reason)
// constructor takes a template as parameter
[HttpPut("{facilityId}/{bandwidthChange}")] 
// use multiple FromRoute attributes, one for each parameter you are expecting to be bound from the routing data
public void UpdateBandwidthChangeHangup([FromRoute] int facilityId, [FromRoute] int bandwidthChange)
```

- Microsoft.AspNetCore.Authorization.AuthorizeAttribute

```cs
[Authorize]
[Authorize(AuthenticationSchemes = "Bearer")]
[Authorize(AuthenticationSchemes = JwtBearerDefaults.AuthenticationScheme, Policy = Function.CanReject)]
```

## misc

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
- [Middleware Filters in ASP.Net Core](http://www.intstrings.com/ramivemula/articles/middleware-filters-in-asp-net-core/) dec16
- [Custom ASP.NET Core Middleware Example](https://blogs.msdn.microsoft.com/dotnet/2016/09/19/custom-asp-net-core-middleware-example/) sep16
- [ASP.NET - Use Custom Middleware to Detect and Fix 404s in ASP.NET Core Apps](https://msdn.microsoft.com/en-us/magazine/mt707525.aspx) jun16
- [Filters](https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/filters) dec16
- [Exploring Middleware as MVC Filters in ASP.NET Core 1.1](https://andrewlock.net/exploring-middleware-as-mvc-filters-in-asp-net-core-1-1/)
- [Hot Chocolate](https://github.com/ChilliCream/hotchocolate) is a GraphQL server for .NET Core and .NET Classic
- An implementation of [GraphQL for .NET](https://github.com/ckimes89/graphql-net) and IQueryable
- [graphql](https://graphql.org/code/#c-net)


[home](../README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki)