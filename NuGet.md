# NuGet

## Commands

|  |  |
|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Get-Package -ListAvailable -Filter Hangfire.Mongo -AllVersions -PageSize 5` | deprecated, returns a paged list of packages available online, with a search term and version history |
| `Get-Package -Updates` | Returns a list of packages installed in the default project that have updates available in the current package source. |
| `Install-Package Hangfire.Mongo -IgnoreDependencies -Version 0.2.1` | install specific version without dependencies |
| `Install-package c:\temp\packages\jQuery.1.10.2.nupkg` | Installs jquery 1.10.2 package, using the .nupkg file under local path of c:\temp\packages. |
| `cd %LOCALAPPDATA%\NuGet\Cache\` | view local nupkg cache |
| `Uninstall-Package -RemoveDependencies Hangfire.Mongo -Version 0.2.1 -Force` | Forces an uninstall of the package even if another package depends on it. Uninstalls the package and its unused dependencies. If omitted, defaults to the latest version. |
| (pipe) `ft -AutoSize` | display tabular |
| (pipe) `fl` | display list details |
| `Find-Package jquery -AllVersions -ExactMatch` | (for NuGet 3.0 client or higher) Returns jquery package with all versions available from the package source. |
| <code>Find-Package -Id ZeroMQ -AllVersions &#124; Select-Object ID, Version, Description, DownloadCount &#124; Sort-Object -Descending -Property DownloadCount</code> | detailed relevant package search |
| uncheck '_Allow NuGet to download missing packages during build._' | To prevent NuGet from restoring packages during build, open the Visual Studio Options dialog, click on the Package Manager node |
| `Install-Package Microsoft.CodeDom.Providers.DotNetCompilerPlatform` `Install-Package Microsoft.Net.Compilers` | c# 6.0 |
| `Install-package NUnit -Version 2.6.4` `Install-package NUnitTestAdapter -Version 2.0.0` | NUnit inside MSTest |


## Links
- [Local feeds](https://docs.microsoft.com/ro-ro/nuget/hosting-packages/local-feeds)
- [host own nuget](https://docs.microsoft.com/ro-ro/nuget/hosting-packages/overview)
- [Creating a local Nuget cache/repository](https://joshilewis.wordpress.com/2012/01/13/creating-a-local-nuget-cacherepository/)
- [Local package sources](http://stackoverflow.com/questions/28592693/adding-nuget-package-sources-to-visual-studio-by-script) 

[<<](https://github.com/illegitimis/Tutorial/)