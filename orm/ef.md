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
* [Seed Database in Code-First](http://www.entityframeworktutorial.net/code-first/seed-database-in-code-first.aspx)

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
+ Generate migration from Package Manager Console
```cmd
Add-Migration -Name "PackageInfoShipmentPurpose" -OutputDir "Migrations" -Project esw.Shipping.Api
update-database -Migration "PackageInfoShipmentPurpose" -Project esw.Shipping.Api
```
+ Generate migration from Powershell / Git Bash
```bat
install-package entityframework.commands -pre

dotnet ef migrations add "Initial" -o "Data\Migrations"
dotnet ef database update
```
+ cs MultiKeyIndexEntity
```cs
class SomeEntityContext : DbContext {
	protected override void OnModelCreating(ModelBuilder modelBuilder) {
		 modelBuilder.Entity<MultiKeyIndexEntity>()
                .HasIndex(u => new { u.Id1, u.Id2, u.SomeReference})
                .IsUnique();
	}
}

public partial class OrderTableBrandIdMerchantIdOrderReferenceUniqueIndexAdded : Migration {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateIndex(
                name: "IX",
                table: "SomeTable",
                columns: new[] { "Id1", "Id2", "SomeReference" },
                unique: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropIndex(
                name: "IX",
                table: "SomeTable");
        }
    }

 [DbContext(typeof(SomeEntityContext))]
partial class ShippingEntityContextModelSnapshot : ModelSnapshot {
	protected override void BuildModel(ModelBuilder modelBuilder) {
		  modelBuilder.Entity("esw.Shipping.Api.Models.BusinessEntities.Order", b => {
			b.HasIndex("Id1", "Id2", "SomeReference").IsUnique();
		  });		 
	}
}	
```


[<<](../ORM.md)
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 

