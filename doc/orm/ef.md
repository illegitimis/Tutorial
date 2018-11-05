# Entity Framework

## Links

- [Looking Ahead to Entity Framework 7](https://www.pluralsight.com/courses/entity-framework-7-looking-ahead), [![Looking Ahead to Entity Framework 7](https://img.shields.io/badge/Pluralsight-course-lightgrey.svg)](https://www.pluralsight.com/courses/entity-framework-7-looking-ahead)
- [efcore and EF6 feature comparison](https://docs.microsoft.com/en-us/ef/efcore-and-ef6/features)
- [Data Points - EF7 Migrations](https://msdn.microsoft.com/magazine/mt614250)
- [NuGet/DNX Commands](https://github.com/aspnet/EntityFramework/wiki/Design-Meeting-Notes---July-23,-2015)
- [ef-core 4 'Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular'](../netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#ef-core) [![Pluralsight course wiki page](https://img.shields.io/badge/Pluralsight-wiki-red.svg)](../netcore/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#ef-core)
- [Seed Database in Code-First](http://www.entityframeworktutorial.net/code-first/seed-database-in-code-first.aspx)
- [Data Annotations versus Fluent API](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-implemenation-entity-framework-core#data-annotations-versus-fluent-api)
- [learn ef](https://www.learnentityframeworkcore.com/)

## Recipes

- Generate migration from Package Manager Console

    ```cmd
    Add-Migration -Name "MigrationName" -OutputDir "Migrations" -Project EFProj
    Update-Database -Migration "MigrationName" -Project EFProj
    Remove-Migration -Force -Project EFProj
    ```

- **multiple column index** with `OnModelCreating`

    ```cs
    class SomeEntityContext : DbContext {
        protected override void OnModelCreating(ModelBuilder modelBuilder) {
            modelBuilder.Entity<MultiKeyIndexEntity>()
                    .HasIndex(u => new { u.Id1, u.Id2, u.SomeReference})
                    .IsUnique();
        }
    }
    ```

- **multiple column index** by _adding a separate migration_
    ```cs
    public partial class OrderTableBrandIdMerchantIdOrderReferenceUniqueIndexAdded : Migration {
            protected override void Up(MigrationBuilder migrationBuilder) {
                migrationBuilder.CreateIndex(
                    name: "IX",
                    table: "SomeTable",
                    columns: new[] { "Id1", "Id2", "SomeReference" },
                    unique: true);
            }

            protected override void Down(MigrationBuilder migrationBuilder) {
                migrationBuilder.DropIndex(
                    name: "IX",
                    table: "SomeTable");
            }
        }
    ```

- A Model Snapshot is the current state of the model stored in a class file named `{YourContext}ModelSnapshot.cs`

    ```cs
    [DbContext(typeof(SomeEntityContext))]
    partial class ShippingEntityContextModelSnapshot : ModelSnapshot {
        protected override void BuildModel(ModelBuilder modelBuilder) {
            modelBuilder.Entity("EFProj.Models.BusinessEntities.Order", b => {
                b.HasIndex("Id1", "Id2", "SomeReference").IsUnique();
            });
        }
    }
    ```

[<<](../orm.md) | [home](../../README.md)