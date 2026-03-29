# Table Schema

## sysobjects vs sys.objects

`sysobjects` is just a system table in SQL Server 2000. 
In SQL Server 2005, [there is no such system table](https://social.msdn.microsoft.com/Forums/sqlserver/en-US/a965676e-d4d9-4365-ad0a-58ca26ec4701/differenece-between-sysobjects-and-sysobjects-in-sql-server-2005-?forum=sqlkjmanageability) named `sysobjects`, it is implemented as a system view, just as background compatibility view only.

```sql
select distinct xtype from sysobjects
--TR--SQ--FN--TT--S --D --IT--F --PK--P --U --TF--C --SN--UQ--IF--V
```

```sql
select distinct type, type_desc from sys.objects

--TYPE    TYPE_DESC 
--C     CHECK_CONSTRAINT 
--D     DEFAULT_CONSTRAINT 
--F     FOREIGN_KEY_CONSTRAINT 
--FN    SQL_SCALAR_FUNCTION 
--IT    INTERNAL_TABLE 
--P     SQL_STORED_PROCEDURE 
--PK    PRIMARY_KEY_CONSTRAINT 
--S     SYSTEM_TABLE 
--SQ    SERVICE_QUEUE 
--TR    SQL_TRIGGER 
--U     USER_TABLE 
--UQ    UNIQUE_CONSTRAINT 
--V     VIEW
```

## Todo

```sql
SELECT '['+TABLE_SCHEMA+'].['+TABLE_NAME+']' [Table] FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'
SELECT distinct table_type FROM INFORMATION_SCHEMA.TABLES
--BASE TABLE--VIEW
select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id)
```

[<<](../sql.md) | [home](../../README.md)