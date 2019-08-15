# dotnet commands

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

[<< home](../../README.md) | [< netcore](../netcore.md)
