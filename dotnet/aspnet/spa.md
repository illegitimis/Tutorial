---
title: Single Page Apps
layout: default
nav_order: 12
parent: ASP.NET
grand_parent: .NET
last_modified_date: 2026-03-31 00:00:00 +00:00
---

# Single Page Apps

## .NET SPA Templates

.NET default templates for `dotnet new` [1] \
`dotnet new angular -f net7.0 --auth Individual --use-local-db --kestrelHttp(s)Port` \
Templates: ASP.NET Core with Angular \
Short name: `angular` \
Tags: Web/MVC/SPA \
Discontinued since 8.0

Overview of **Single Page Apps** (SPAs) in ASP.NET Core 8 [2] \
Overview of SPAs in ASP.NET Core 7 [3]

## ASP.NET Core with Angular

Use the Angular project template with ASP.NET Core [4] \
Use the `Visual Studio` project type for JavaScript and TypeScript (`.esproj`) for the frontend \
**JavaScript Project System** (JSPS) \
`dotnet run --launch-profile https`

Tutorial: create an ASP.NET Core app with `Angular` in `Visual Studio` [5] \
_Angular and ASP.NET Core_ \
ASP.NET Core API project + `Angular CLI` running `ng start` \
`MSBuild` reference for the JavaScript Project System [6] \
`ShouldRunNpmInstall` + `ShouldRunBuildScript`

Create an `Angular` project [7] \
`npm` + `Angular CLI`, _Angular App_ \
Template name was changed from Standalone TypeScript Angular Project to Angular App

## TypeScript Integration

JavaScript and TypeScript in `Visual Studio` [8] \
`Microsoft.TypeScript.MSBuild` 5.8.3 MSBuild task [9] \
Compile TypeScript code (ASP.NET Core) [10] \
`tsconfig.json` TypeScript JSON Configuration File \
Compile TypeScript code using `npm` [11]

## Vite

`Vite` [12] is a blazing fast frontend build tool powering the next generation of web applications.

[1]: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new-sdk-templates#spa
[2]: https://learn.microsoft.com/en-us/aspnet/core/client-side/spa/intro?view=aspnetcore-8.0&preserve-view=true
[3]: https://learn.microsoft.com/en-us/aspnet/core/client-side/spa/intro?view=aspnetcore-7.0&preserve-view=true#developing-single-page-apps
[4]: https://learn.microsoft.com/en-us/aspnet/core/client-side/spa/angular?view=aspnetcore-9.0&tabs=visual-studio
[5]: https://learn.microsoft.com/en-us/visualstudio/javascript/tutorial-asp-net-core-with-angular?view=vs-2022
[6]: https://learn.microsoft.com/en-us/visualstudio/javascript/javascript-project-system-msbuild-reference?view=vs-2022
[7]: https://learn.microsoft.com/en-us/visualstudio/javascript/tutorial-create-angular-app?view=vs-2022
[8]: https://learn.microsoft.com/en-us/visualstudio/javascript/javascript-in-visual-studio?view=vs-2022
[9]: https://www.nuget.org/packages/Microsoft.TypeScript.MSBuild
[10]: https://learn.microsoft.com/en-us/visualstudio/javascript/compile-typescript-code-nuget?view=vs-2022
[11]: https://learn.microsoft.com/en-us/visualstudio/javascript/compile-typescript-code-npm?view=vs-2022
[12]: https://vite.dev/

[<](./index.md) | [<<](/index.md)
