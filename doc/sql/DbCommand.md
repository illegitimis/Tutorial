# (I)DbCommand

## hierarchy

- [`System.Data.IDbCommand`](https://msdn.microsoft.com/en-us/library/system.data.idbcommand(v=vs.110).aspx)
  - [`System.Data.Common.DbCommand`](https://msdn.microsoft.com/en-us/library/system.data.common.dbcommand(v=vs.110).aspx)
    - System.Data.EntityClient.EntityCommand
    - System.Data.Odbc.OdbcCommand
    - System.Data.OleDb.OleDbCommand
    - System.Data.OracleClient.OracleCommand
    - System.Data.SqlClient.SqlCommand

## methods

1. [Executes](https://msdn.microsoft.com/en-us/library/system.data.sqlclient.sqlcommand.executenonquery(v=vs.110).aspx) 
a Transact-SQL statement against the connection and returns the number of rows affected. 
Perform catalog operations (for example, querying the structure of a database or creating database objects such as tables), 
or to change the data in a database without using a [DataSet](https://msdn.microsoft.com/en-us/library/system.data.dataset%28v=vs.110%29.aspx) 
by executing UPDATE, INSERT, or DELETE statements. 
```cs
ExecuteNonQuery 
BeginExecuteNonQuery 
EndExecuteNonQuery 
BeginExecuteNonQueryAsync
```

2. Sends the [`CommandText`](https://msdn.microsoft.com/en-us/library/system.data.sqlclient.sqlcommand.commandtext%28v=vs.110%29.aspx) 
to the [`Connection`](https://msdn.microsoft.com/en-us/library/system.data.sqlclient.sqlcommand.connection%28v=vs.110%29.aspx) 
and builds a [`SqlDataReader`](https://msdn.microsoft.com/en-us/library/system.data.sqlclient.sqldatareader%28v=vs.110%29.aspx).  
[Executes commands that return rows](https://msdn.microsoft.com/en-us/library/system.data.sqlclient.sqlcommand(v=vs.110).aspx). 
For increased performance, ExecuteReader invokes commands using the Transact-SQL `sp_executesql` system stored procedure. 
Therefore, ExecuteReader might not have the effect that you want if used to execute commands such as Transact-SQL SET statements 
```cs
ExecuteReader
BeginExecuteReader
EndExecuteReader(IAsyncResult)
ExecuteReaderAsync
```

3. Executes the query, and returns the first column of the first row in the result set returned by the query. 
Additional columns or rows are ignored.
[Retrieves a single value](https://msdn.microsoft.com/en-us/library/system.data.sqlclient.sqlcommand(v=vs.110).aspx) 
(for example, an aggregate value) from a database.
```cs
ExecuteScalar
ExecuteScalarAsync()
[Begin|End]ExecuteScalar
```

4. Sends the CommandText to the Connection and builds an [`XmlReader`](https://msdn.microsoft.com/en-us/library/system.xml.xmlreader%28v=vs.110%29.aspx) object. Use `SqlDbType.Xml` for parameters.

```cs
ExecuteXmlReader  
BeginExecuteXmlReader  
EndExecuteXmlReader  
ExecuteXmlReaderAsync()
```
5. ADO.NET 2 also provides **true asynchronous operations**. 
Unlike creating a background thread and blocking, ADO.NET 2 implements asynchronous operations by using ~IO Completion ports~, 
which are built into the .NET Framework but are truly asynchronous, _with no secondary thread being created_ and blocked while the UI continues on. 
The ADO.NET 2 solution follows the general look-and-feel for the other asynchronous commands within the .NET Framework, 
as the method names use the standard calling syntax of BeginABC/EndABC. 
The `SqlCommand` class provides support for asynchronous commands through the following methods:

```cs
BeginExecuteNonQuery/EndExecuteNonQuery
BeginExecuteReader/EndExecuteReader
BeginExecuteXmlReader/EndExecuteXmlReader
```

[<<](../sql.md) | [home](../../README.md)