# NuGet

## Recipes

- NuGet feeds sources: _%APPDATA%\NuGet\NuGet.Config_
- VS package sources: 
  - _%ProgramData%\NuGet\Config\VisualStudio\14.0\Microsoft.VisualStudio.config_ 
  - _%Program Files%\NuGet\Config\Microsoft.VisualStudio.Offline.config_
- To prevent NuGet from restoring packages during build, open the Visual Studio Options dialog, click on the Package Manager node uncheck '_Allow NuGet to download missing packages during build._'

## Commands

- deprecated, returns a paged list of packages available online, with a search term and version history 

```ps
Get-Package -ListAvailable -Filter Hangfire.Mongo -AllVersions -PageSize 5
```

- Returns a list of packages installed in the default project that have updates available in the current package source.

```ps
Get-Package -Updates
```

- install specific version without dependencies

```ps
Install-Package Hangfire.Mongo -IgnoreDependencies -Version 0.2.1
```

- Installs jquery 1.10.2 package, using the .nupkg file under local path of c:\temp\packages. 

```ps
Install-package c:\temp\packages\jQuery.1.10.2.nupkg
```

- view local nupkg cache

```bat
cd %LOCALAPPDATA%\NuGet\Cache\
```

- Forces an uninstall of the package even if another package depends on it. Uninstalls the package and its unused dependencies. If omitted, defaults to the latest version.

```ps
Uninstall-Package -RemoveDependencies Hangfire.Mongo -Version 0.2.1 -Force
``` 

- display tabular / list details

```ps
| ft -AutoSize
| fl
```

- (for NuGet 3.0 client or higher) Returns jquery package with all versions available from the package source.

```ps
Find-Package jquery -AllVersions -ExactMatch
```

- **detailed** relevant package search 

```ps
Find-Package -Id ZeroMQ -AllVersions | Select-Object ID, Version, Description, DownloadCount | Sort-Object -Descending -Property DownloadCount
```

- NUnit inside MSTest, c# 6.0

```ps
Install-Package Microsoft.CodeDom.Providers.DotNetCompilerPlatform
Install-Package Microsoft.Net.Compilers
Install-package NUnit -Version 2.6.4
Install-package NUnitTestAdapter -Version 2.0.0
```

## Links

- Local feeds [1]
- host own nuget [2]
- Creating a local Nuget cache/repository [3]
- Local package sources [4] 
- Configure machine wide packages and Visual Studio package sources [5]

[<<](../tools.md) | [home](../../README.md)

[1]: https://docs.microsoft.com/ro-ro/nuget/hosting-packages/local-feeds
[2]: https://docs.microsoft.com/ro-ro/nuget/hosting-packages/overview
[3]: https://joshilewis.wordpress.com/2012/01/13/creating-a-local-nuget-cacherepository/
[4]: http://stackoverflow.com/questions/28592693/adding-nuget-package-sources-to-visual-studio-by-script
[5]: https://docs.microsoft.com/en-us/nuget/consume-packages/configuring-nuget-behavior
