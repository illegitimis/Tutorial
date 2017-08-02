# StringSearchDb

```sql
/****** StoredProcedure ******/ 
SET ANSI_NULLS ON 
GO 
SET QUOTED_IDENTIFIER ON 
GO 
ALTER PROCEDURE [dbo].[StringSearchDb] 
    @DataToFind NVARCHAR(4000), 
    @ExactMatch BIT = 0 
AS 
SET NOCOUNT ON 
 

DECLARE @TempStringSearchDb TABLE(RowId INT IDENTITY(1,1), SchemaName sysname, TableName sysname, ColumnName SysName, DataType VARCHAR(100), DataFound BIT) 
 

INSERT  INTO @TempStringSearchDb(TableName,SchemaName, ColumnName, DataType) 
    SELECT  C.Table_Name,C.TABLE_SCHEMA, C.Column_Name, C.Data_Type 
    FROM    Information_Schema.Columns AS C 
            INNER Join Information_Schema.Tables AS T 
                ON C.Table_Name = T.Table_Name 
        AND C.TABLE_SCHEMA = T.TABLE_SCHEMA 
    WHERE   Table_Type = 'Base Table' 
            And Data_Type In ('ntext','text','nvarchar','nchar','varchar','char') 
 

DECLARE @i INT 
DECLARE @MAX INT 
DECLARE @TableName sysname 
DECLARE @ColumnName sysname 
DECLARE @SchemaName sysname 
DECLARE @SQL NVARCHAR(4000) 
DECLARE @PARAMETERS NVARCHAR(4000) 
DECLARE @DataExists BIT 
DECLARE @SQLTemplate NVARCHAR(4000) 
 

SELECT  @SQLTemplate = CASE WHEN @ExactMatch = 1 
                            THEN 'If Exists(Select * 
                                          From   ReplaceTableName 
                                          Where  Convert(nVarChar(4000), [ReplaceColumnName]) 
                                                       = ''' + @DataToFind + ''' 
                                          ) 
                                     Set @DataExists = 1 
                                 Else 
                                     Set @DataExists = 0' 
                            ELSE 'If Exists(Select * 
                                          From   ReplaceTableName 
                                          Where  Convert(nVarChar(4000), [ReplaceColumnName]) 
                                                       Like ''%' + @DataToFind + '%'' 
                                          ) 
                                     Set @DataExists = 1 
                                 Else 
                                     Set @DataExists = 0' 
                            END, 
        @PARAMETERS = '@DataExists Bit OUTPUT', 
        @i = 1 
 

SELECT @i = 1, @MAX = MAX(RowId) 
FROM   @TempStringSearchDb 
 

WHILE @i <= @MAX 
    BEGIN 
        SELECT  @SQL = REPLACE(REPLACE(@SQLTemplate, 'ReplaceTableName', QUOTENAME(SchemaName) + '.' + QUOTENAME(TableName)), 'ReplaceColumnName', ColumnName) 
        FROM    @TempStringSearchDb 
        WHERE   RowId = @i 
 

PRINT @SQL 
        EXEC SP_EXECUTESQL @SQL, @PARAMETERS, @DataExists = @DataExists OUTPUT 
 

IF @DataExists =1 
            UPDATE @TempStringSearchDb SET DataFound = 1 WHERE RowId = @i 
 

SET @i = @i + 1 
    END 
 

SELECT  SchemaName,TableName, ColumnName 
FROM    @TempStringSearchDb 
WHERE   DataFound = 1
```


[<<](../SQL.md)
|
[home](../README.md)
|
[wiki](https://github.com/illegitimis/Tutorial/wiki) 