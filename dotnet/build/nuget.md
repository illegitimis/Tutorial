---
title: NuGet
layout: default
nav_order: 3
parent: .NET Build
last_modified_date: 2026-03-31 00:00:00 +00:00
---

# NuGet

```sh
dotnet nuget locals all --list
```

`NuGet` target frameworks [15] \
Allow overriding a centrally defined package version [21]

## CLI Commands

```sh
dotnet nuget locals http-cache --clear
dotnet nuget why <solution>.sln <PackageName>
# Lists all configured NuGet sources
dotnet nuget list source
dotnet nuget --version
dotnet nuget locals global-packages --list
```

## Cache Paths

```txt
%USERPROFILE%\.nuget\packages
%LOCALAPPDATA%\NuGet\v3-cache
%TEMP%\NuGetScratch
```

| Cache | Path |
|---|---|
| http-cache | `%LOCALAPPDATA%\NuGet\v3-cache` |
| packages-cache | `%LOCALAPPDATA%\NuGet\Cache` |
| global-packages | `%USERPROFILE%\.nuget\packages\` |
| temp | `%TEMP%\NuGetScratch` |

`NUGET_PACKAGES` environment variable overrides the global-packages path.

## Pipeline Error NETSDK1005

```txt
error NETSDK1005: Assets file 'obj\project.assets.json'
doesn't have a target for 'net9.0'.
Ensure that restore has run and that you have included 'net9.0'
in the TargetFrameworks for your project.
```

[15]: https://learn.microsoft.com/en-us/nuget/reference/target-frameworks
[21]: https://github.com/NuGet/Home/issues/11516

[<](./index.md) | [<<](/index.md)