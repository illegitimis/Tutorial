---
title: Build and Configuration
layout: default
nav_order: 6
parent: .NET
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Build and Configuration

## global.json

`global.json` in the code repository root [1]:

```json
"sdk": { "version": "6.0.100", "rollForward": "latestPatch" }
```

Run `dotnet --list-sdks` in a shell to check installed versions:

```txt
3.1.426 [C:\Program Files\dotnet\sdk]
5.0.416 [C:\Program Files\dotnet\sdk]
6.0.310 [C:\Program Files\dotnet\sdk]
7.0.202 [C:\Program Files\dotnet\sdk]
```

DstsAuthenticationLibrary.csproj
**warning**: Unable to locate the .NET SDK version '**6.0.100**' as specified by global.json, please check that the specified version is installed.
_error NETSDK1141_: Unable to resolve the .NET SDK version as specified in the global.json.
Done building project "DstsAuthenticationLibrary.csproj" -- FAILED.

## MSBuild

The Microsoft Build Engine (`MSBuild`) is the build platform for .NET and Visual Studio [2].
`MSBuild` is now part of Visual Studio [3].
`MSBuild` and 64-bit Visual Studio 2022 [4].

## NuGet

```sh
dotnet nuget locals all --list
```

## Project Files

*.proj; *.csproj; *.targets; *.props

`QCustomExtensionsImported` variable defined in _QCustomExtensions.props_

In _ExtensionPackaging.targets_, instead of:

```xml
<Import Project="$(SRCROOT)\Environments\QCustomExtensions.props" Condition="$(QCustomExtensionsImported) != 'true'"/>
<Import Project="$(SRCROOT)\Extensions\AzureAPI.targets" />
```

Have this:

```xml
<Import Project="$(SRCROOT)\Extensions\AzureAPI.targets" Condition="$(PreferSDP) != 'true'" />
<Import Project="$(SRCROOT)\Extensions\AzureAPI.SDP.targets" Condition="$(PreferSDP) != 'true'" />
```

[1]: https://learn.microsoft.com/en-us/dotnet/core/tools/global-json
[2]: https://github.com/dotnet/msbuild
[3]: https://devblogs.microsoft.com/visualstudio/msbuild-is-now-part-of-visual-studio/
[4]: https://devblogs.microsoft.com/dotnet/msbuild-and-64-bit-visual-studio-2022/

[<](./index.md) | [<<](/index.md)