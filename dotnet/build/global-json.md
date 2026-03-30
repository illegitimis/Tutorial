---
title: global.json
layout: default
nav_order: 4
parent: .NET Build
last_modified_date: 2026-03-30 23:07:00 +00:00
---

# global.json

`global.json` and the .NET CLI [1] \
`MSBuild` throws error: the SDK "Microsoft.NET.Sdk" specified could not be found [20]

```sh
dotnet new globaljson --sdk-version 6.0.401
```

```json
"sdk": { "version": "6.0.100", "rollForward": "latestPatch" }
```

Run `dotnet --list-sdks` in a shell to check installed versions \
**warning**: Unable to locate the .NET SDK version '**6.0.100**' as specified by global.json, please check that the specified version is installed. \
_error NETSDK1141_: Unable to resolve the .NET SDK version as specified in the global.json.

[1]: https://learn.microsoft.com/en-us/dotnet/core/tools/global-json
[20]: https://stackoverflow.com/questions/46257393/

[<](./index.md) | [<<](/index.md)