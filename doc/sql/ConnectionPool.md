# Connection Pool

[Connection pooling](http://www.techrepublic.com/article/take-advantage-of-adonet-connection-pooling/) maintains a _group_ (or pool) of _active database connections_.  
When an application tries to open a database connection, an open connection is retrieved from the pool (if available).  
_Closing_ a connection _returns it to the pool_ for other processes to utilize. 
Connection pooling is utilized (by default) unless otherwise specified.

## Pooling advice

You should be judicious in your use of connection pooling. Here are a few tips when using it: 

- Only open connections when needed. That is, timing is everything, so open a connection just before you need it and not any sooner. Also, close that connection as soon as you are finished with it—don't wait for the garbage collector to do it. 
- Close user-defined transactions before closing related connections. 
- To maintain the connection pool, you should keep at least one connection open. Therefore, do not close all your connections in the pool. If server resources become a problem, you may close all connections, and the pool will be recreated with the next request. 
- Do not use connection pooling if integrated security is utilized. This results in a unique connection string per user, so each user has a connection pool that is not available to other users. The end result is poor performance, so pooling should be avoided in this scenario.
- [`ClearPool`](https://msdn.microsoft.com/en-us/library/system.data.sqlclient.sqlconnection.clearpool%28v=vs.110%29.aspx) clears/empties the connection pool that is associated with the connection. 
If additional [connections](https://msdn.microsoft.com/en-us/library/system.data.sqlclient.sqlconnection%28v=vs.110%29.aspx) associated with connection are in use at the time of the call, 
they are marked appropriately and are discarded (instead of being returned to the pool) when `Close` is called on them.
```cs
public static void ClearPool ( SqlConnection connection)
```
+ [ClearAllPools](https://msdn.microsoft.com/en-us/library/system.data.sqlclient.sqlconnection.clearallpools%28v=vs.110%29.aspx) resets (or empties) the connection pool.
If there are connections in use at the time of the call, they are marked appropriately and will be discarded (instead of being returned to the pool) when Close is called on them. 
```cs
public static void SqlConnection.ClearAllPools() 
```
+ [Connection Pooling for OleDb](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/ole-db-odbc-and-oracle-connection-pooling#connection-pooling-for-oledb)
+ [Connection Pooling for Odbc](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/ole-db-odbc-and-oracle-connection-pooling#connection-pooling-for-odbc)
+ [Connection Pooling for OracleClient](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/ole-db-odbc-and-oracle-connection-pooling#connection-pooling-for-oracleclient)
+ [Pooled vs. Non-pooled connections](https://www.sqlskills.com/blogs/bobb/sql-server-and-pooled-vs-non-pooled-connections/) article
+ [`@@SPID`](https://docs.microsoft.com/en-us/sql/t-sql/functions/spid-transact-sql) Returns the session ID of the current user process
```sql
SELECT @@SPID AS 'ID', SYSTEM_USER AS 'Login Name', USER AS 'User Name'
```
+ `sp_who`. For each database connection, SQL Server creates a _server process_. 
This will contain the state associated with the connection.
[The SPID is like a process ID for that connection][1].
You can kill processes with the spid through KILL, 
you can identify unique connections from users with sp_who (similar to taskmgr in a query), you can figure out which process owns a lock with sp_lock, etc. 
For the ADO.net connection, the SPID will not be the same if you create/destroy the connection, just like a process ID is not always the same when you run an executable.
Each time you create the connection, you should execute `select @@SPID` to get the connection SPID if you are going to need it.
Note that MARS makes it possible for multiple commands to share the same SPID (sort of like how multiple threads can share the same process). 
If you want to retrieve database information about all the connected clients, I would suggest sp_who. 
It provides spid, user name, and the hostname of the client for all the current connections to the server. 
If you want to keep track of all clients that ever connected to the server, you would want a login trigger to insert into a table for that sort of thing.
For just listing who is currently connected, sp_who should give you what you need. 

[1]: (https://social.technet.microsoft.com/Forums/sqlserver/en-US/94692d7b-69c6-4c34-a1dd-495c652e7d9d/session-id-of-adonet-connection?forum=sqldataaccess) 

[<<](../sql.md) | [home](../../README.md)