---
title: Primary Keys
layout: default
nav_order: 10
parent: SQL
grand_parent: Data
last_modified_date: 2026-03-29 21:39:07 +00:00
---

# Primary Keys

- INFORMATION_SCHEMA

```sql
SELECT DISTINCT 
  Constraint_Name AS [Constraint],
  Table_Schema AS [Schema],
  Table_Name AS [TableName]
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
```

- sys.objects

```sql
SELECT
  OBJECT_NAME(OBJECT_ID) AS NameofConstraint,
  SCHEMA_NAME(schema_id) AS SchemaName,
  OBJECT_NAME(parent_object_id) AS TableName,
  type_desc AS ConstraintType
FROM sys.objects  
```

[<](./index.md) | [<<](/index.md)
