# Foreign key mappings

1. WITH SQL SERVER 2000 TABLES. [ORIGINAL ANSWER does not ALLOW multiple column relationships](http://stackoverflow.com/questions/1026673/sql-2000-t-sql-to-get-foreign-key-relationships-for-a-table)
```sql
select  
C.constid RELATIONSHIP_ID,  
P.name SOURCE_TABLE,  
Q.name SPURCE_COLUMN,  
F.name TARGET_TABLE,  
G.name TARGET_COLUMN, 
K.keyno CARDINALITY 
from sysconstraints C                                                -- general constraint  
join sysforeignkeys K on C.constid = K.constid and K.fkeyid = C.id   -- foreign key constraint 
join sysobjects P on P.id = K.rkeyid                                 -- source table 
JOIN syscolumns Q ON P.id = Q.id and Q.colid = K.rkey                -- source column 
join sysobjects F on F.id = C.id                                     -- target table 
JOIN syscolumns G ON G.id = F.id and G.colid =  K.fkey               -- target column 
where P.xtype = 'U' and F.type='U'
```
2. with >2005 views
```sql
DECLARE @Intermediate TABLE (PRIMARY_KEY_NAME sysname, FOREIGN_KEY_NAME sysname, PRIMARY_TABLE sysname, PRIMARY_COLUMN sysname, FOREIGN_TABLE sysname, FOREIGN_COLUMN sysname, COLINDEX int) 
insert into @Intermediate 
select  
c.name PRIMARY_KEY_NAME, 
fk.name FOREIGN_KEY_NAME, 
tp.name PRIMARY_TABLE, 
pc.name PRIMARY_COLUMN, 
tf.name FOREIGN_TABLE, 
fc.name FOREIGN_COLUMN, 
fkc.constraint_column_id COLINDEX 
from sys.foreign_keys fk  
join sys.foreign_key_columns fkc on fk.object_id = fkc.constraint_object_id and fk.parent_object_id = fkc.parent_object_id and fk.referenced_object_id = fkc.referenced_object_id 
join sys.key_constraints kc on kc.parent_object_id = fk.referenced_object_id 
join sys.tables tp on tp.object_id = fk.referenced_object_id 
join sys.tables tf on tf.object_id = fk.parent_object_id 
join sys.columns pc on pc.object_id = fkc.referenced_object_id and pc.column_id=fkc.referenced_column_id 
join sys.columns fc on fc.object_id = fkc.parent_object_id and fc.column_id=fkc.parent_column_id 


SELECT I.PRIMARY_KEY_NAME, I.FOREIGN_KEY_NAME, i.PRIMARY_TABLE, I.FOREIGN_TABLE, 
stuff((select distinct ', '+I2.PRIMARY_COLUMN as [text()] from @Intermediate I2   
WHERE I2.PRIMARY_TABLE = I.PRIMARY_TABLE AND I2.FOREIGN_TABLE = I.FOREIGN_TABLE AND I2.FOREIGN_KEY_NAME = I.FOREIGN_KEY_NAME AND I2.PRIMARY_KEY_NAME = I.PRIMARY_KEY_NAME 
for xml path('')),1,1,'')  AS PRIMARY_COLUMN, 
stuff((select distinct ', '+I2.FOREIGN_COLUMN as [text()] from @Intermediate I2   
WHERE I2.PRIMARY_TABLE = I.PRIMARY_TABLE AND I2.FOREIGN_TABLE = I.FOREIGN_TABLE AND I2.FOREIGN_KEY_NAME = I.FOREIGN_KEY_NAME AND I2.PRIMARY_KEY_NAME = I.PRIMARY_KEY_NAME 
for xml path('')),1,1,'')  AS FOREIGN_COLUMN, 
COUNT(I.COLINDEX) AS CARDINALITY 
FROM @Intermediate I 
group by I.PRIMARY_KEY_NAME, I.FOREIGN_KEY_NAME, I.PRIMARY_TABLE, I.FOREIGN_TABLE
```
3. with information schema
```sql
SELECT  
     KCU1.CONSTRAINT_NAME AS 'FK_CONSTRAINT_NAME' 
   , KCU1.TABLE_NAME AS 'FK_TABLE_NAME' 
   , KCU1.COLUMN_NAME AS 'FK_COLUMN_NAME' 
   , KCU1.ORDINAL_POSITION AS 'FK_ORDINAL_POSITION' 
   , KCU2.CONSTRAINT_NAME AS 'UQ_CONSTRAINT_NAME' 
   , KCU2.TABLE_NAME AS 'UQ_TABLE_NAME' 
   , KCU2.COLUMN_NAME AS 'UQ_COLUMN_NAME' 
   , KCU2.ORDINAL_POSITION AS 'UQ_ORDINAL_POSITION' 
FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS RC 
JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE KCU1 
ON KCU1.CONSTRAINT_CATALOG = RC.CONSTRAINT_CATALOG  
   AND KCU1.CONSTRAINT_SCHEMA = RC.CONSTRAINT_SCHEMA 
   AND KCU1.CONSTRAINT_NAME = RC.CONSTRAINT_NAME 
JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE KCU2 
ON KCU2.CONSTRAINT_CATALOG =  RC.UNIQUE_CONSTRAINT_CATALOG  
   AND KCU2.CONSTRAINT_SCHEMA =  RC.UNIQUE_CONSTRAINT_SCHEMA 
   AND KCU2.CONSTRAINT_NAME =  RC.UNIQUE_CONSTRAINT_NAME 
   AND KCU2.ORDINAL_POSITION = KCU1.ORDINAL_POSITION
```
4. SQL Server 2012
```sql
exec SP_FKEYS @pktable_name = 'mpk' 
exec SP_FKEYS @fktable_name = 'mfk
```

5. [table hard dependency](https://blog.sqlauthority.com/2016/02/16/sql-server-view-dependencies-on-sql-server-hard-soft-way/)
```sql
SELECT 
	coalesce(OBJECT_SCHEMA_NAME(f.parent_object_id) + '.', '') + OBJECT_NAME(f.parent_object_id) PARENT, 
	coalesce(OBJECT_SCHEMA_NAME(f.referenced_object_id) + '.', '') + OBJECT_NAME(f.referenced_object_id) REF
FROM sys.foreign_keys f
WHERE 1=1 
--AND f.referenced_object_id = OBJECT_ID('dbo.Orders')
AND f.parent_object_id != referenced_object_id
```

6. [sys.sql_expression_dependencies](https://www.red-gate.com/simple-talk/sql/t-sql-programming/dependencies-and-references-in-sql-server/)
```sql
	SELECT
		  coalesce(object_schema_name(Referencing_ID)+'.','')+ --likely schema name
		    object_name(Referencing_ID)+ --definite entity name
		    coalesce('.'+col_name(referencing_ID,referencing_minor_id),'')
		       AS [referencing],
		  coalesce(Referenced_server_name+'.','')+ --possible server name if cross-server
		       coalesce(referenced_database_name+'.','')+ --possible database name if cross-database
		       coalesce(referenced_schema_name+'.','')+ --likely schema name
		       coalesce(referenced_entity_name,'') + --very likely entity name
		       coalesce('.'+col_name(referenced_ID,referenced_minor_id),'')AS [referenced]
		FROM sys.sql_expression_dependencies
		--WHERE referencing_id =object_id('Categories')
		ORDER BY [referenced]
```


[<<](../SQL.md)
|
[home](../README.md)
|
[wiki](https://github.com/illegitimis/Tutorial/wiki) 
