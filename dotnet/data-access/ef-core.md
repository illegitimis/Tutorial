---
title: Entity Framework Core
layout: default
nav_order: 3
parent: Data Access
grand_parent: .NET
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# Entity Framework Core

## Links

- Entity Framework Code First Migrations in Team Environments [1]
- Entity Framework Core Tutorial [2]
- ms docs ef core [3]
- Using Azure database for PostgreSQL in ASP.NET Core [4] (with EF Core) Jan18
- EF Core or micro-ORM? [5]
- Entity Framework Core 2.1 Roadmap [6]
- explicit loading [7]
- implement infrastructure persistence layer with Entity Framework Core [8]

## Recipes

- use an **in memory db** for _tests_

    ```cs
    public class MessagingDbContext : Microsoft.EntityFrameworkCore.DbContext { /* ... */ }

    return new MessagingDbContext(new DbContextOptionsBuilder<MessagingDbContext>().UseInMemoryDatabase(databaseName: DB_NAME).Options)
    ```

- Fix `$ dotnet ef database update` returning _No executable found matching command "dotnet-ef"_. Modify _csproj_.

    ```xml
    <PackageReference Include="Microsoft.EntityFrameworkCore.Tools.DotNet" Version="1.0.1"/>
    <DotNetCliToolReference Include="Microsoft.EntityFrameworkCore.Tools.DotNet">
        <Version>1.0.0-*</Version>
    </DotNetCliToolReference>  
    ```

- Generate migration from Powershell / Git Bash

    ```bat
    install-package entityframework.commands -pre
    dotnet ef migrations add "Initial" -o "Data\Migrations"
    dotnet ef database update
    ```

[1]: https://msdn.microsoft.com/en-us/data/dn481501.aspx
[2]: http://www.entityframeworktutorial.net/efcore/entity-framework-core.aspx
[3]: https://docs.microsoft.com/en-us/ef/core/
[4]: http://www.dotnetcurry.com/aspnet/1410/aspnet-core-app-postgresql-azure
[5]: https://docs.microsoft.com/en-us/dotnet/standard/modern-web-apps-azure-architecture/work-with-data-in-asp-net-core-apps#ef-core-or-micro-orm
[6]: https://blogs.msdn.microsoft.com/dotnet/2018/02/02/entity-framework-core-2-1-roadmap/
[7]: https://docs.microsoft.com/en-us/aspnet/core/data/ef-mvc/read-related-data?view=aspnetcore-2.0
## Data Seeding

> Custom initialization logic with `UseSeeding` and `UseAsyncSeeding`

Data Seeding [9] \
The New Way to Seed Your Database in EF Core 9 [10] \
How to Seed Data with EF Core 9 and `.NET Aspire` [11]

`UseAsyncSeeding` and `UseSeeding` are called as part of `EnsureCreated`, `Migrate`, and `dotnet ef database update`.

### OnConfiguring

```cs
protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)=>
    optionsBuilder
        .UseSqlServer("YourConnectionString")
        .UseAsyncSeeding(async (context, _, cancellationToken) =>
        {
            if (context.Set<T>().Any()) return;
            SeedT();
            await context.SaveChangesAsync(cancellationToken);
        });
```

### HasData

> Model-managed data

`HasData` method [12] for seeding via `OnModelCreating` [13] [14] \
Extension method pattern [15] \
Taking `EF Core` data seeding to the next level with `Bogus` [16]

### Migrations

Create and Drop APIs [17] — `EnsureCreated`/`EnsureDeleted` alternative to migrations \
`EF Core` tools reference — .NET CLI [18] \
Migrations Overview [19] \
`migrationBuilder.InsertData` for manual migration customization

### Compiled Models

Compiled models [20] — `dotnet ef dbcontext optimize` for startup performance

[8]: https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-implemenation-entity-framework-core
[9]: https://learn.microsoft.com/en-us/ef/core/modeling/data-seeding
[10]: https://medium.com/@ekondur/the-new-way-to-seed-your-database-in-ef-core-9-a92f483e6ed8
[11]: https://juliocasal.com/blog/how-to-seed-data-with-ef-core-9-and-net-aspire
[12]: https://www.learnentityframeworkcore.com/configuration/fluent-api/hasdata-method
[13]: https://www.ashgrennan.com/post/ef-core-seed-data-strategy/
[14]: https://github.com/zzzprojects/docs/blob/master/learnentityframeworkcore.com/pages/migrations/seeding.md
[15]: https://www.tektutorialshub.com/entity-framework-core/ef-core-data-seeding/
[16]: https://stenbrinke.nl/blog/taking-ef-core-data-seeding-to-the-next-level-with-bogus/
[17]: https://learn.microsoft.com/en-us/ef/core/managing-schemas/ensure-created
[18]: https://learn.microsoft.com/en-us/ef/core/cli/dotnet
[19]: https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/?tabs=dotnet-core-cli
[20]: https://learn.microsoft.com/en-us/ef/core/performance/advanced-performance-topics?tabs=with-di%2Cexpression-api-with-constant#compiled-models

[<](./index.md) | [<<](/index.md)
