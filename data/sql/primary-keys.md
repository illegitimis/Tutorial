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

[<<](../sql.md) | [home](../../README.md)