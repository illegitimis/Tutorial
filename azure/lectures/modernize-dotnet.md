# Modernize .NET Apps

## Q&A

> What is the difference between the Azure region and the geography specified in the Azure Migrate drop-down (when migrating a web app)?

Azure regions are organized into geographies. An [Azure geography][azure-geographies] ensures that data residency, sovereignty, compliance, and resiliency requirements are [honored within geographical boundaries][data-residency].

> Related to data residency — if my resource group is in the North Europe region and I start using the web app migrator choosing the Europe geography, does this mean the actual app could be physically hosted in West Europe?

When you do a data migration, you will select the exact Azure Region where data will be copied. If you want you can run the app in another region, but you need to take into account whether you are allowed from the legal/compliance point of view to have data in that geographical region or country.

## Web App Hosting

> Note: Diagram `lctrs/pics/l01/web.app.hosting.png` — web app hosting options diagram — would appear here.

## Migration Journey

> Note: Diagram `lctrs/pics/l01/migration.journey.png` — migration journey overview diagram — would appear here.

## Azure Resource Manager Architecture

![ARM Architecture][arm-arch]

## Misc

- Azure [migration center][migration-center]
- Azure Migrate is a hub; includes the Azure App Service Migration Assistant
- [Migrate machines as physical servers to Azure][migrate-physical]
- For SQL DB: download the `Data Migration Assistant` for small workloads
- For enterprise: use the `Database Migration Service`
- Features comparison: [Azure SQL Database and Azure SQL Managed Instance][sql-features-comparison]
- [SQL Server Service Broker][service-broker] — provides native support for messaging and queuing in the SQL Server Database Engine and Azure SQL Managed Instance. Developers can use Database Engine components to communicate between disparate databases and build distributed and reliable applications.
- .NET Core Portability Analyzer (extension)

[azure-geographies]: https://azure.microsoft.com/en-us/global-infrastructure/geographies/
[data-residency]: https://azure.microsoft.com/en-us/global-infrastructure/data-residency/#overview
[arm-arch]: https://docs.microsoft.com/en-us/learn/azure-fundamentals/azure-architecture-fundamentals/media/consistent-management-layer-feef9259.png
[migration-center]: https://azure.microsoft.com/en-us/migration/
[migrate-physical]: https://docs.microsoft.com/en-us/azure/migrate/tutorial-migrate-physical-virtual-machines
[sql-features-comparison]: https://docs.microsoft.com/en-us/azure/azure-sql/database/features-comparison
[service-broker]: https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-service-broker?view=sql-server-ver15

[<<](../index.md) | [home](../../README.md)
