# Entity Framework Core

## Links

- [Entity Framework Code First Migrations in Team Environments](https://msdn.microsoft.com/en-us/data/dn481501.aspx)
- [Entity Framework Core Tutorial](http://www.entityframeworktutorial.net/efcore/entity-framework-core.aspx)
- [ms docs ef core](https://docs.microsoft.com/en-us/ef/core/)

## recipes

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