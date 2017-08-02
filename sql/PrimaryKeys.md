# Primary Keys

1. INFORMATION_SCHEMA 
```sql
SELECT DISTINCT 
	Constraint_Name AS [Constraint], 
	Table_Schema AS [Schema], 
	Table_Name AS [TableName] 
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE 
```

2. sys.objects 
```sql
SELECT 
	OBJECT_NAME(OBJECT_ID) AS NameofConstraint, 
	SCHEMA_NAME(schema_id) AS SchemaName, 
	OBJECT_NAME(parent_object_id) AS TableName, 
	type_desc AS ConstraintType 
FROM sys.objects  
```





<<](../SQL.md)
|
[home](../README.md)
|
[wiki](https://github.com/illegitimis/Tutorial/wiki) 
 



