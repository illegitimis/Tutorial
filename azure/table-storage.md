---
title: Table Storage
layout: default
nav_order: 15
parent: Azure
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Table Storage

What is Azure Table storage? [1] \
Data partitioning strategies by service [2] \
Design for data modification [3] \
Design for querying [4] \
Design a scalable partitioning strategy for Azure Table storage [5] \
Design scalable and performant tables [6] \
Guidelines for table design [7] \
**Index Table** pattern [8] \
Performance and scalability checklist for Table storage [9] \
Query operators supported for the Table service [10] \
Querying tables and entities [11] \
Scalability and performance targets for standard storage accounts [12] \
Scalability and performance targets for Table storage [13] \
Table design patterns [14] \
Understanding the Table service data model [15] \
Writing LINQ queries against the Table service [16]

## Table Design Patterns TOC

**Table design patterns** [17]:

- **Intra-partition secondary index** pattern
- **Inter-partition secondary index** pattern
- **Eventually consistent transactions** pattern
- **Index entities** pattern
- **Denormalization** pattern
- **Compound key** pattern
- **Log tail** pattern
- **High volume delete** pattern
- **Data series** pattern
- **Wide entities** pattern
- **Large entities** pattern
- **Prepend/append** anti-pattern
- **Log data** anti-pattern
- Implementation considerations
- Retrieving entities
- Modifying entities
- Working with heterogeneous entity types
- Controlling access with **Shared Access Signatures**
- Asynchronous and parallel operations

**Modeling relationships** [18]:

- One-to-many relationships
- One-to-one relationships
- Join in the client
- Inheritance relationships

**Performance and scalability checklist** [19]:

- Checklist
- Scalability targets
- Networking
- SAS and CORS
- Batch transactions
- .NET configuration
- Unbounded parallelism
- Client libraries and tools
- Handle service errors
- Configuration
- Schema

## Azure.Data.Tables v12.7.1

`TableEntity` public sealed class [20]: `Azure.Data.Tables.ITableEntity`, `IDictionary<string,object>` \
`Azure.Data.Tables` query [21] \
GitHub Pages samples [22] \
Announcing the new Azure Tables Libraries [23] \
Querying tables and entities [24]

## Entity Size Calculation

How the size of an entity is calculated in Windows Azure Table storage [25] \
Understanding Windows Azure Storage billing: bandwidth, transactions, and capacity [26] \
How to calculate the Azure Table storage row size [27]

```cs
int sizeInBytes = o switch
{
    // String|# of Characters * 2 bytes + 4 bytes for length of string
    string s => 4 + 2*s.Length,
    // DateTime|8 bytes
    DateTime _ => 8,
    // GUID|16 bytes
    Guid _ => 16,
    // Double|8 bytes
    double _ => 8,
    // Int|4 bytes
    int _ => 4,
    // INT64|8 bytes
    long _ => 8,
    // Bool|1 byte
    bool _ => 1,
    // Binary|sizeof(value) in bytes + 4 bytes for length of binary array
    byte[] x => 4 + x.Length,
    _ => throw new NotSupportedException(o.GetType().Name)
};
```

An entity always has the following system properties:

- `PartitionKey` (<1KiB, characters disallowed in key fields)
- `RowKey` (<1KiB)
- `Timestamp` (internal **optimistic concurrency**)

> Combined size of all data in entity properties **< 1MiB** (1,048,576 bytes)

Total entity size = overhead + lenKeys + properties:

- **Overhead**: 4 bytes for each entity (includes `Timestamp` and system metadata)
- **lenKeys**: Len(PartitionKey + RowKey) * 2 bytes (stored as UTF-16)
- **Properties**: for each property: 8 bytes + Len(Property Name) * 2 bytes + Sizeof(.NET Property Type)

| .NET Property Type | Sizeof() |
|---|---|
| String | # of Characters * 2 bytes + 4 bytes |
| DateTime | 8 bytes |
| GUID | 16 bytes |
| Double | 8 bytes |
| Int | 4 bytes |
| INT64 | 8 bytes |
| Bool | 1 byte |
| Binary | sizeof(value) + 4 bytes |

[1]: https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-overview
[2]: https://learn.microsoft.com/en-us/azure/architecture/best-practices/data-partitioning-strategies
[3]: https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-design-for-modification
[4]: https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-design-for-query
[5]: https://learn.microsoft.com/en-us/rest/api/storageservices/designing-a-scalable-partitioning-strategy-for-azure-table-storage
[6]: https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-design
[7]: https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-design-guidelines
[8]: https://learn.microsoft.com/en-us/azure/architecture/patterns/index-table
[9]: https://learn.microsoft.com/en-us/azure/storage/tables/storage-performance-checklist
[10]: https://learn.microsoft.com/en-us/rest/api/storageservices/query-operators-supported-for-the-table-service
[11]: https://learn.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities
[12]: https://learn.microsoft.com/en-us/azure/storage/common/scalability-targets-standard-account?toc=%2Fazure%2Fstorage%2Ftables%2Ftoc.json
[13]: https://learn.microsoft.com/en-us/azure/storage/tables/scalability-targets
[14]: https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-design-patterns
[15]: https://learn.microsoft.com/en-us/rest/api/storageservices/Understanding-the-Table-Service-Data-Model
[16]: https://learn.microsoft.com/en-us/rest/api/storageservices/writing-linq-queries-against-the-table-service
[17]: https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-design-patterns#large-entities-pattern
[18]: https://learn.microsoft.com/en-us/azure/storage/tables/table-storage-design-modeling
[19]: https://learn.microsoft.com/en-us/azure/storage/tables/storage-performance-checklist#schema
[20]: https://learn.microsoft.com/en-us/dotnet/api/azure.data.tables.tableentity?view=azure-dotnet
[21]: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/tables/Azure.Data.Tables#query-table-entities
[22]: https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/tables/Azure.Data.Tables/samples/Sample0Auth.md
[23]: https://devblogs.microsoft.com/azure-sdk/announcing-the-new-azure-data-tables-libraries/
[24]: https://learn.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities
[25]: https://learn.microsoft.com/en-us/archive/blogs/avkashchauhan/how-the-size-of-an-entity-is-caclulated-in-windows-azure-table-storage
[26]: https://learn.microsoft.com/en-us/archive/blogs/windowsazurestorage/understanding-windows-azure-storage-billing-bandwidth-transactions-and-capacity
[27]: https://github.com/MicrosoftDocs/azure-docs/issues/35190

[<](./index.md) | [<<](/index.md)
