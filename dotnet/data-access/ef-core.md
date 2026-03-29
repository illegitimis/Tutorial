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

[<<](../orm.md) | [home](../../README.md)

[1]: https://msdn.microsoft.com/en-us/data/dn481501.aspx
[2]: http://www.entityframeworktutorial.net/efcore/entity-framework-core.aspx
[3]: https://docs.microsoft.com/en-us/ef/core/
[4]: http://www.dotnetcurry.com/aspnet/1410/aspnet-core-app-postgresql-azure
[5]: https://docs.microsoft.com/en-us/dotnet/standard/modern-web-apps-azure-architecture/work-with-data-in-asp-net-core-apps#ef-core-or-micro-orm
[6]: https://blogs.msdn.microsoft.com/dotnet/2018/02/02/entity-framework-core-2-1-roadmap/
[7]: https://docs.microsoft.com/en-us/aspnet/core/data/ef-mvc/read-related-data?view=aspnetcore-2.0
[8]: https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-implemenation-entity-framework-core
