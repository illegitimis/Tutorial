---
title: Frameworks and Libraries
layout: default
nav_order: 7
parent: .NET
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Frameworks and Libraries

## .NET at GitHub

`Microsoft.Extensions.Logging.Abstractions` [1] \
Logging.Abstractions source [2] \
`ILoggerFactory.cs` [3] \
`ILogger.cs` [4] \
`ILogger<T>` [5] \
Logging in .NET [6] \
`ILogger<T>` API reference [7] \
Logging in ASP.NET Core [8]

`HttpRequestJsonExtensions.cs` [9] \
`ApplicationBuilder.cs` [10] \
`UseWhenExtensions.cs` [11] \
`MapWhenMiddleware.cs` [12] \
`HttpContext.cs` [13]

## .NET Frameworks

Target frameworks in SDK-style projects [14] \
`NuGet` target frameworks [15] \
Conditional compilation [16] \
Check SDK versions [17] \
`global.json` and the .NET CLI [18]

```sh
dotnet new globaljson --sdk-version 6.0.401
```

.NET support policy [19]

`MSBuild` throws error: the SDK "Microsoft.NET.Sdk" specified could not be found [20]

Allow overriding a centrally defined package version [21]

`System.Runtime.Versioning.FrameworkName` [22] \
`FrameworkName.cs` [23]

[1]: https://www.nuget.org/packages/Microsoft.Extensions.Logging.Abstractions/3.1.12
[2]: https://github.com/dotnet/runtime/tree/main/src/libraries/Microsoft.Extensions.Logging.Abstractions/src
[3]: https://github.com/dotnet/runtime/blob/main/src/libraries/Microsoft.Extensions.Logging.Abstractions/src/ILoggerFactory.cs
[4]: https://github.com/dotnet/runtime/blob/main/src/libraries/Microsoft.Extensions.Logging.Abstractions/src/ILogger.cs
[5]: https://github.com/dotnet/runtime/blob/main/src/libraries/Microsoft.Extensions.Logging.Abstractions/src/ILoggerT.cs
[6]: https://learn.microsoft.com/en-us/dotnet/core/extensions/logging?tabs=command-line
[7]: https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger-1?view=dotnet-plat-ext-7.0
[8]: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/logging/?view=aspnetcore-7.0
[9]: https://github.com/dotnet/aspnetcore/blob/main/src/Http/Http.Extensions/src/HttpRequestJsonExtensions.cs
[10]: https://github.com/dotnet/aspnetcore/blob/main/src/Http/Http/src/Builder/ApplicationBuilder.cs
[11]: https://github.com/dotnet/aspnetcore/blob/main/src/Http/Http.Abstractions/src/Extensions/UseWhenExtensions.cs
[12]: https://github.com/dotnet/aspnetcore/blob/main/src/Http/Http.Abstractions/src/Extensions/MapWhenMiddleware.cs
[13]: https://github.com/dotnet/aspnetcore/blob/main/src/Http/Http.Abstractions/src/HttpContext.cs
[14]: https://learn.microsoft.com/en-us/dotnet/standard/frameworks
[15]: https://learn.microsoft.com/en-us/nuget/reference/target-frameworks
[16]: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/preprocessor-directives
[17]: https://learn.microsoft.com/en-us/dotnet/core/install/how-to-detect-installed-versions?pivots=os-windows#check-sdk-versions
[18]: https://learn.microsoft.com/en-us/dotnet/core/tools/global-json
[19]: https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core
[20]: https://stackoverflow.com/questions/46257393/msbuild-throws-error-the-sdk-microsoft-net-sdk-specified-could-not-be-found
[21]: https://github.com/NuGet/Home/issues/11516
[22]: https://github.com/dotnet/dotnet-api-docs/blob/main/xml/System.Runtime.Versioning/FrameworkName.xml
[23]: https://github.com/microsoft/referencesource/blob/master/System/sys/system/runtime/versioning/FrameworkName.cs

[<](./index.md) | [<<](/index.md)