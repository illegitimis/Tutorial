# .Net Core

## links

+ [dotnet command ms docs](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet)
+ [Building a Web App with ASP.NET Core, MVC 6, EF Core, and Angular](./netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md)
[![Pluralsight course wiki page](https://img.shields.io/badge/Pluralsight-wiki-red.svg)](./netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md)
+ [AspNetCore Rest](./netcore/rest.md)
[![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./netcore/rest.md)


## dotnet commands

- **migrate** _Migrates_ a *project.json* (and _xproj_) based project to a *msbuild* based project.
- **add|list|remove reference** Adds a project reference, or deletes one, or lists all.
- **add|remove** Adds or Removes a NuGet package.
- **new console** - Initialize a sample .NET Core console application that can be compiled and run
- **build** - Build a project and its dependencies in a given directory:
- **sln** modifies a .Net Core solution file
  ```cmd
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

## project

+ [Mapping between csproj and project.json](https://docs.microsoft.com/en-us/dotnet/core/tools/project-json-to-csproj)
+ [Setting `EnableDefaultCompileItems` to False doesn't remove the files from solution Explorer](https://github.com/dotnet/sdk/issues/1157)

## misc
+ 
+ [reverse package search](https://packagesearch.azurewebsites.net/)



[home](README.md)
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 