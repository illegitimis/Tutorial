# Entity Framework (Core)

## Links

* [Entity Framework Code First Migrations in Team Environments](https://msdn.microsoft.com/en-us/data/dn481501.aspx)
* [Looking Ahead to Entity Framework 7](https://www.pluralsight.com/courses/entity-framework-7-looking-ahead), 
  [![Looking Ahead to Entity Framework 7](https://img.shields.io/badge/Pluralsight-course-lightgrey.svg)](https://www.pluralsight.com/courses/entity-framework-7-looking-ahead)
* [efcore and EF6 feature comparison](https://docs.microsoft.com/en-us/ef/efcore-and-ef6/features)
* [Data Points - EF7 Migrations](https://msdn.microsoft.com/magazine/mt614250)
* [NuGet/DNX Commands](https://github.com/aspnet/EntityFramework/wiki/Design-Meeting-Notes---July-23,-2015)
* [ef-core 4 'Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular'](../netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#ef-core)
[![Pluralsight course wiki page](https://img.shields.io/badge/Pluralsight-wiki-red.svg)](../netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#ef-core)

## Recipes

+ use an **in memory db** for _tests_
```cs
public class MessagingDbContext : Microsoft.EntityFrameworkCore.DbContext { /* ... */ }

return new MessagingDbContext(
	new DbContextOptionsBuilder<MessagingDbContext>()
            .UseInMemoryDatabase(databaseName: DB_NAME) 
            .Options;
)
```
+ Fix `$ dotnet ef database update` returning _No executable found matching command "dotnet-ef"_.
Modify _csproj_.
```xml
	<PackageReference Include="Microsoft.EntityFrameworkCore.Tools.DotNet" Version="1.0.1"/>
	<DotNetCliToolReference Include="Microsoft.EntityFrameworkCore.Tools.DotNet">
		<Version>1.0.0-*</Version>
	</DotNetCliToolReference>  
```




[<<](../ORM.md)
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 

