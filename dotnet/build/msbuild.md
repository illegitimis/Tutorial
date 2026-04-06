---
title: MSBuild
layout: default
nav_order: 2
parent: .NET Build
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# MSBuild

The Microsoft Build Engine (`MSBuild`) is the build platform for .NET and Visual Studio [2].
`MSBuild` is now part of Visual Studio [3].
`MSBuild` and 64-bit Visual Studio 2022 [4].

Project Files: *.proj;*.csproj; *.targets;*.props

```xml
<Import Project="$(SRCROOT)\Environments\QCustomExtensions.props" Condition="$(QCustomExtensionsImported) != 'true'"/>
<Import Project="$(SRCROOT)\Extensions\AzureAPI.targets" Condition="$(PreferSDP) != 'true'" />
```

[2]: https://github.com/dotnet/msbuild
[3]: https://devblogs.microsoft.com/visualstudio/msbuild-is-now-part-of-visual-studio/
## Package Dependencies

Manage package dependencies in .NET applications [5] \
Common `MSBuild` project properties [6]

[4]: https://devblogs.microsoft.com/dotnet/msbuild-and-64-bit-visual-studio-2022/
[5]: https://learn.microsoft.com/en-us/dotnet/core/tools/dependencies?view=aspnetcore-10.0
[6]: https://learn.microsoft.com/en-us/visualstudio/msbuild/common-msbuild-project-properties?view=visualstudio

[<](./index.md) | [<<](/index.md)