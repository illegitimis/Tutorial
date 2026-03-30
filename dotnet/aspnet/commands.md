---
title: Dotnet Commands
layout: default
nav_order: 5
parent: ASP.NET
grand_parent: .NET
last_modified_date: 2026-03-29 21:39:07 +00:00
---

# Dotnet Commands

dotnet command ms docs [1]

- **migrate** _Migrates_ a _project.json_ (and _xproj_) based project to a _msbuild_ based project.
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

[1]: https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet

[<](./index.md) | [<<](/index.md)
