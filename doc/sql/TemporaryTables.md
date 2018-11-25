# TemporaryTables

Temporary tables are used by every DB developer, but they're not likely to be too adventurous with their use, [or exploit all their advantages][4].  
They can improve your code's performance and maintainability, but can be the source of grief to both developer and DBA if things go wrong and a process grinds away inexorably slowly.
They are used most often to provide workspace for the intermediate results when processing data within a batch or procedure. 
They are also used to pass a table from a table-valued function, to pass table-based data between stored procedures or, more recently in the form of Table-valued parameters, 
to send whole read-only tables from applications to SQL Server routines, or pass read-only temporary tables as parameters. 
Once finished with their use, they are discarded automatically. 
Temporary tables come in different flavours including 
+ local temporary tables (starting with #) 
+ global temporary tables (starting with ##) 
+ persistent temporary tables (prefixed by TempDB..)
+ table variables.(starting with (@) 

Before we get too deep into the technology, I’d advise that you should use table variables where possible. 
They’re easy, and SQL Server does the work for you. 
They also tend to cause fewer problems to a hard-working OLTP system. 
Just occasionally, you may need to fine-tune them to get good performance from them in joins.
However, if you are doing more complex processing on temporary data or likely to use more than reasonably small amounts of data in them, then  local temporary tables are likely to be  a better choice.

## Local temporary tables

_Prefixed_ with a **pound** sign (#). This tells SQL Server that this table is a local temporary table.  
This table is _only visible to this session_ of SQL Server. 
When I close this session, the table will be _automatically dropped_.  
You can treat this table just like any other table with a few exceptions.  
The only real major one is that **you can't have foreign key constraints on a temporary table**.  
Temporary tables are _created in tempdb_.  
SQL Server _stores the object with a some type of unique number appended on the end of the name_.  
It does all this for you automatically. You just have to refer to `#Yaks` in your code.  
If two different users both create a #Yaks table each will have _their own copy of it_. 
The exact same code will run properly on both connections.  
_Any temporary table created inside a stored procedure is automatically dropped when the stored procedure finishes executing._  
If stored procedure A creates a temporary table and calls stored procedure B, then B will be able to use the temporary table that A created.  
It's _generally considered good coding practice_ to **explicitly drop** every temporary table you create.
If you are running scripts through SQL Server Management Studio or Query Analyzer the temporary tables are kept until you explicitly drop them or until you close the session. 
The _best way_ to use a temporary table is to **create it and then fill it with data**. 
Temporary tables are usually pretty quick.  
**Since you are creating and deleting them on the fly, they are usually only cached in memory.**

```sql
CREATE TABLE #Yaks (YakID int, YakName char(30))
select name from tempdb..sysobjects where name like '#yak%'  
drop table #yaks

CREATE TABLE #TibetanYaks(YakID int,YakName char(30)) 
INSERT INTO #TibetanYaks (YakID, YakName) 
SELECT YakID, YakName FROM dbo.Yaks WHERE YakType = 'Tibetan' 
-- Do some stuff with the table
drop table #TibetanYaks
```

With Local temporary table (names that begin with #), what goes on under the hood is surprisingly similar to table variables. 
As with Table Variables, Local Temporary tables are private to the process that created it. 
They cannot therefore be used in views and you cannot associate triggers with them. 

They are handier than table variables if you like using SELECT INTO to create them, 
but I’m slightly wary about using SELECT INTO in a system that is likely to require modification, 
I’d much rather create my temporary tables explicitly, along with all the constraints that are needed. 

You cannot easily tell which session or procedure has created these tables. 
This is because, if the same stored procedure is executed simultaneously by several processes, the Database Engine needs to be able to distinguish the same tables created by the different processes. 
The Database Engine does this by internally appending a left-padded numeric suffix to each local temporary table name. 
The full name of a temporary table as stored in the sys.objects view in TempDB is made up of the table name specified in the CREATE TABLE statement and the system-generated numeric suffix. 
To allow for the suffix, the table name specified for a local temporary name must be less than 116 characters. 

You get housekeeping with Local Temporary tables; they are automatically dropped when they go out of scope, unless explicitly dropped by using DROP TABLE. 
Their scope is more generous than a table Variable so you don’t have problems referencing them within batches or in dynamic SQL. 
Local temporary tables are dropped automatically at the end of the current session or procedure. 
Dropping it at the end of the procedure that created it can cause head-scratching: 
a local temporary table that is created within a stored procedure or session is dropped when it is finished so it cannot be referenced by the process that called the stored procedure that created the table. 
It can, however, be referenced by any nested stored procedures executed by the stored procedure that created the table. 
If the nested procedure references a temporary table and two temporary tables with the same name exist at that time, which table is the query is resolved against? 

As a curiosity, you can also create Local Temporary Stored Procedures with the same scope and lifetime as a local temporary table. You can’t do the same for other routines.

## Global temporary tables

You can also create global temporary tables. 
These are named with **two pound signs**. 
For example, `##YakHerders` is a global temporary table. 
Global temporary tables are _visible to all SQL Server connections_. 
When you create one of these, _all the users can see it_.
[These are rarely used in SQL Server][3].

Like Local temporary tables, Global temporary tables (they begin with ##) are automatically dropped when the session that created the table ends: 
However, because global tables aren’t private to the process that created it, they must persist thereafter until the last Transact-SQL statement that was actively referencing the table at the time when the creating session ended has finished executing and the locks are dropped. Anyone who has access to TempDB at the time these Global Temporary tables exist can directly query, modify or drop these temporary objects.  
You can associate rules, defaults, and indexes with temporary tables, but you cannot create views on temporary tables or associate triggers with them. You can use a user-defined datatype when creating a temporary table only if the datatype exists in TempDB 
Stored procedures can reference temporary tables that are created during the current session. Within a stored procedure, you cannot create a temporary table, drop it, and then create a new temporary table with the same name. 
Although this works…. 
```sql
CREATE table #Color( 
Color varchar(10) PRIMARY key) 
INSERT INTO #color SELECT 'Red' UNION SELECT 'White' 
 UNION SELECT 'green'UNION SELECT'Yellow'UNION SELECT'blue' 
DROP TABLE #color 
go 
CREATE table #Color( 
Color varchar(10) PRIMARY key) 
INSERT INTO #color SELECT 'Red' UNION SELECT 'White' 
 UNION SELECT 'green'UNION SELECT'Yellow'UNION SELECT'blue' 
DROP TABLE #color 
…this doesn’t 
 
CREATE PROCEDURE MisbehaviourWithTemporaryTables  AS 
 CREATE table #Color( 
Color varchar(10) PRIMARY key) 
INSERT INTO #color SELECT 'Red' UNION SELECT 'White' 
 UNION SELECT 'green'UNION SELECT'Yellow'UNION SELECT'blue' 
DROP TABLE #color 
CREATE table #Color( 
Color varchar(10) PRIMARY key) 
INSERT INTO #color SELECT 'Red' UNION SELECT 'White' 
 UNION SELECT 'green'UNION SELECT'Yellow'UNION SELECT'blue' 
DROP TABLE #color 
go
```
You can, by using local temporary tables, unintentionally  force recompilation on the stored procedure every time it is used. 
This isn’t good because the stored procedure is unlikely to perform well. To avoid recompilation, avoid referring to a temporary table created in a calling or called stored procedure: 
If you can’t do so, then put the reference in a string that is then executed using the EXECUTE statement or sp_ExecuteSQL stored procedure. 
Also, make sure that the temporary table is created in the stored procedure or trigger before it is referenced and dropped after these references. 
Don’t create a temporary table within a control-of-flow statement such as IF... ELSE or WHILE.  
You are allowed to create Global Temporary Stored Procedures, but I’ve yet to find a use for them. Global temporary functions aren’t permitted.

## Table Variables 

If you are using SQL Server 2000 or higher, you can take advantage of the new TABLE variable type.  
These are similar to temporary tables except with more flexibility and _they always stay in memory_.
Table variables _don't need to be dropped when you are done with them_.
```sql
DECLARE @TibetanYaks TABLE (YakID int, YakName char(30)) 
INSERT INTO @TibetanYaks (YakID, YakName) 
SELECT YakID, YakName FROM dbo.Yaks WHERE YakType = 'Tibetan' 
```

Table variables are used within the scope of the routine or batch within which they are defined, and were originally created to make table-valued functions possible. 
However, they are good for many of the uses that the traditional temporary table was put to. 
They behave like other variables in their scoping rules. Once out of scope, they are disposed of. 
These are much easier to work with, and pretty secure, and they trigger fewer recompiles in the routines where they’re used than if you were to use temporary tables. 
Table variables require less locking resources as they are ‘private’ to the process that created them. 
Transaction rollbacks do not affect them because table variables have limited scope and are not part of the persistent database, 
so they are handy for creating or storing data that ought to survive roll backs such as log entries. 
The downside of table variables is that they are often disposed of before you can investigate their contents for debugging, or use them to try out different SQL expressions interactively. 

If your application is conservative and your data volumes light you’ll never want anything else. However, you can hit problems. 
One difficulty is that table variables can only be referenced in their local scope, so you cannot process them using dynamic SQL as you might with a temporary table or table-valued parameter. 
This is because you can’t refer an externally-defined table variable within dynamic SQL that you then execute via the EXEC statement 
or the sp_ExecuteSQL stored procedure because the dynamic SQL is executed outside the scope of the table variable. 
You can, of course, create, and then use, the table variable inside the dynamic SQL because  the table variable would be in scope. 
However, once the dynamic SQL is run, there would be no table variable.

There are a few anomalies to be aware of too. 
You can’t, for example, change the table definition after the initial DECLARE statement. 
In SQL Server 2000,  a table variable can’t be the destination of a `SELECT INTO` statement or a `INSERT EXEC` (now fixed); 
You can’t call user-defined functions from CHECK constraints, DEFAULT values, and computed columns in the table variable. 
The only constraints that you’re allowed beyond CHECK constraints are PRIMARY KEY, UNIQUE KEY, and NULL / NOT NULL 

The trickiest problems, though, come with increasing size of the tables, because you can’t declare an index explicitly and distribution statistics aren’t maintained on them. 
The Query Optimiser assumes that there is only one row in the table. 
You also cannot generate parallel query plans for a SQL expression that is modifying the table’s contents. 
To partially get around the index restriction, you can use constraints to do the same thing. 
Most essential is the Primary Key constraint which allows you to impose a clustered index, but unique constraints are useful for performance. 
The Query optimiser will happily use them if they are around. The biggest problem with table variables is that statistics aren’t maintained on the columns. 
This means that the query optimiser has to make a guess as to the size and distribution of the data and if it gets it wrong, then you’re going to see poor performance on joins: 
If this happens, there is little you can do other than to revert to using classic local temporary tables. 
One thing you can try is to add option (recompile) to the statement that involves the table variable joining with other tables. 
By doing this, SQL Server will be able to detect number of rows at recompile because the rows will have already been populated. 
This doesn’t entirely solve the problem since the optimiser still has no distribution statistics and can, usually where the distribution is skewed, produce a bad plan. 
In this demo, the join was reduced in time by three quarters simply by adding the `OPTION (RECOMPILE)`.

```sql
SET nocount ON 
DECLARE @FirstTable TABLE (RandomInteger INT) 
DECLARE @SecondTable TABLE (RandomInteger INT) 
DECLARE @WhenWeStarted DATETIME 
DECLARE @ii INT 

BEGIN TRANSACTION 

SET @ii = 0 
WHILE @ii < 100000  
  BEGIN 
    INSERT  INTO @FirstTable 
    VALUES  (RAND() * 10000) 
    SET @ii = @ii + 1 
  END 

SET @ii = 0 
WHILE @ii < 100000  
  BEGIN 
    INSERT  INTO @SecondTable 
    VALUES  (RAND() * 10000) 
    SET @ii = @ii + 1 
  END 

COMMIT TRANSACTION 

SELECT  @WhenWeStarted = GETDATE() 

SET STATISTICS PROFILE ON 

SELECT  COUNT(*) 
FROM    @FirstTable first 
        INNER JOIN @SecondTable second  
        ON first.RandomInteger = second.RandomInteger OPTION (RECOMPILE) 
  -- 153Ms  as opposed to 653Ms without the hint 

SET STATISTICS PROFILE OFF 
SELECT  'That took '  
    + CONVERT(VARCHAR(8), DATEDIFF(ms, @WhenWeStarted, GETDATE()))  
    + ' ms' 
```

Now if you can make what goes into the tables unique, you can then use a primary key constraint on these tables. 
This allowed the optimiser to use a clustered index seek instead of a table scan and the execution time was too rapid to measure.
Start with table variables, but drop back to using local temporary tables if you hit performance problems. 
Some people are bold enough to give advice in terms of the number of rows in a table, and I’ve seen 100 or 1000 offered as a maximum; 
but  I’ve seen far larger table variables perform perfectly satisfactorily over time, and far smaller ones give trouble. 
However, in smaller tables, the trouble is less detectable!

## Table-Valued Parameters

The Table-Valued Parameter (TVP) is a special type of  table variable that extends its use. 
When table variables are passed as parameters, the table is materialized in the TempDB system database as a table variable and passed by reference,  a pointer to the table in the TempDB. 
Table-valued parameters have been  used since SQL Server 2008 to send several rows of data to a Transact-SQL routine or to a batch via sp_ExecuteSQL.
Their particular value to the programmer is that they **can be used  within TSQL code as well as in the client application**, so they are good for sending client tables to the server.  
From TSQL, you can declare table-valued variables, insert data into them, and  pass these variables as table-valued parameters to stored procedures and functions.
Their more general usefulness is limited by the fact that they are only passed as  read-only. 
You can’t do UPDATE, DELETE, or INSERT statements on a table-valued parameter in the body of a routine. 

You need to create a _User-Defined Table Type_ and define a table structure to use them. 
```sql
CREATE TYPE Names AS TABLE (Name VARCHAR(10)); 

/* Next, Create a procedure to receive data for the table-valued parameter, the table of names and select one item from the table*/ 
CREATE PROCEDURE ChooseAName  @CandidateNames Names READONLY 
AS  
DECLARE @candidates TABLE (NAME VARCHAR(10), theOrder UNIQUEIDENTIFIER) 

INSERT  INTO @candidates (name, theorder) 
        SELECT  name, NEWID() 
        FROM    @CandidateNames 
SELECT TOP 1 
        NAME 
FROM    @Candidates 
ORDER BY theOrder 

/* Declare a variable that references the type for our list of cows. */ 
DECLARE @MyFavouriteCowName AS Names ; 

/* Add data to the table variable. */ 
INSERT  INTO @MyFavouriteCowName (Name) 
 SELECT 'Bossy' UNION SELECT 'Bessy' UNION SELECT 'petal' 
 UNION SELECT 'Daisy' UNION SELECT 'Lulu' UNION SELECT 'Buttercup' UNION SELECT 'Bertha' 
 UNION SELECT 'Bubba' UNION SELECT 'Beauregard' UNION SELECT 'Brunhilde' UNION SELECT 'Lore' 
 UNION SELECT 'Lotte' UNION SELECT 'Rosa' UNION SELECT 'Thilde' UNION SELECT 'Lisa' 
 UNION SELECT 'Peppo' UNION SELECT 'Maxi' UNION SELECT 'Moriz' UNION SELECT 'Marla' 

/* Pass the table with the list of traditional nemes of cows to the stored procedure. */ 
EXEC chooseAName @MyFavouriteCowName
```

As with Table Variables, the table-valued parameter ceases to exist once it is out of scope but the type definition remains until it is explicitly  dropped. 
Like Table Variables they do not acquire locks when the data is being populated from a client, and  statistics aren’t maintained  on columns of table-valued parameters. 
You cannot use a table-valued parameter as target of a SELECT INTO or INSERT EXEC statement. 
As you’d expect, a table-valued parameter can be in the FROM clause of SELECT INTO or in the INSERT EXEC string or stored-procedure.  

The TVP solves the common problem of wanting to pass a local variable to dynamic SQL that is then executed  by a sp_ExecuteSQL. 
It is poorly documented by Microsoft, so I’ll show you a worked example to get you started.

```sql
DECLARE @SeaAreas TABLE (NAME Varchar(20)) 
INSERT INTO @SeaAreas (name) 
SELECT 'Viking' UNION SELECT 'North Utsire' UNION SELECT 'South Utsire' UNION SELECT 'Forties' UNION SELECT 'Cromarty' UNION SELECT 'Forth' UNION SELECT 'Tyne' UNION SELECT 'Dogger' UNION SELECT 'Fisher' UNION SELECT 'German Bight' UNION SELECT 'Humber' UNION SELECT 'Thames' UNION SELECT 'Dover' UNION SELECT 'Wight' UNION SELECT 'Portland' UNION SELECT 'Plymouth' UNION SELECT 'Biscay' UNION SELECT 'Trafalgar' UNION SELECT 'Finisterre' UNION SELECT 'Sole' UNION SELECT 'Lundy' UNION SELECT 'Fastnet' UNION SELECT 'Irish Sea' UNION SELECT 'Shannon' UNION SELECT 'Rockall' UNION SELECT 'Malin' UNION SELECT 'Hebrides' UNION SELECT 'Bailey' UNION SELECT 'Fair Isle' UNION SELECT 'Faeroes' UNION SELECT 'Southeast Iceland'  

CREATE TYPE seanames AS TABLE (Name VARCHAR(20)) ; 

DECLARE @SeaAreaNames AS SeaNames ; 
INSERT  INTO @SeaAreaNames (name) 
        SELECT  * 
        FROM    @SeaAreas 

EXEC sp_executesql N'SELECT * FROM @MySeaAreas', N'@MySeaAreas [dbo].[seanames] READONLY', @MySeaAreas = @SeaAreaNames
```

## TempDB

Temporary tables and table variables are created in the TempDB database, which is really just another database with simple recovery: 
With TempDB, only sufficient ‘minimal’  logging is done to allow rollback, and other ACID niceties. 
The special difference of TempDB is that any objects such as tables are cleared out on startup. 
Because TempDB always uses the simple recovery model, the completed transaction are cleared from the log log on the next TempDB checkpoint, and only the live transactions are retained. 
This all means that temporary tables behave like any other sort of base table in that they are logged, and stored just like them. 
In practice, temporary tables are likely to remain cached in memory, but only if they are frequently-used: same as with a base table. 
TempDB operates a system called temporary object reuse, which will cache a portion of the temporary objects with the plan, if there is sufficient memory. 
This may account for the legend that temporary objects exist only in memory. The truth as ever is ‘it depends…’. 

A lot of other things go on in TempDB: The database engine can use it  for placing work tables for DBCC checks, for creating or rebuilding  indexes, cursors,  for example. 
Intermediate tables in queries described as ‘hashes’, ‘sorts’ and ‘spools’ are materialized in TempDB, for example, along with those required for several ‘physical’ operations in executing SQL Statements. 
It is also used as a version store for Snapshot isolation, Multiple Active Results Sets (MARS), triggers and online-index-build.  

Because temporary tables are stored just like base tables, there are one or two things you need to be wary of. You must, for example, have CREATE TABLE permission in TempDB in order to create a normal table. 
To save you the trouble, this is assigned by default to the DBO (db owner) role, but you may need to do it explicitly for users who aren’t assigned the DBO role. 
All users have permissions to create local or global temporary tables in TempDB because this is assigned to them via the GUEST  user security context. 

The classic temporary table comes in two flavors, the Global, or shareable, temporary table, prefixed by ‘##’, and the local temporary table, whose name is prefixed with ‘#’.
The local temporary tables are less like normal tables than the Global temporary tables: You cannot create views on them, or associate triggers with them. 
It is a bit tricky to work out which process, session or procedure created them. We’ll give you a bit of help with that later. 
Most importantly, they are more secure than a global temporary table as only the owning process can see it.  

Another oddity of the local temporary table (and the local temporary stored procedure)  is that it has a different name in the metadata to the one you give it in your routine or batch. 
If the same routine is executed simultaneously by several processes, the Database Engine needs to be able to distinguish between the identically-named local temporary tables created by the different processes. 
It does this by adding a numeric string to each local temporary table name left-padded by underscore characters. 
Although you specify the short name such as #MyTempTable, what is actually stored in TempDB is made up of the table name specified in the CREATE TABLE statement and the suffix. 
Because of this suffix, local temporary table names must be 116 characters or less. 

If you’re interested in seeing what is going on, you can view the tables in TempDB just the same way you would any other table. 
You can even use sp_help work on temporary tables only if you invoke them from TempDB. 

```sql
USE TempDB 
go 
execute sp_Help #mytemp  
or you can find them in the system views of TempDB without swithching databases. 
 
SELECT name, create_date FROM TempDB.sys.tables WHERE name LIKE '#%' 
Or the Information Schema 
 
SELECT * FROM TempDB.information_schema.tables 

--Even better, you can find out what process, and user, is holding on to enormous temporary tables in TempDB and refusing to give up the space 
-- Find out who created the temporary table,and when; the culprit and SPId. 
SELECT DISTINCT te.name, t.Name, t.create_date, SPID, SessionLoginName 
FROM ::fn_trace_gettable(( SELECT LEFT(path, LEN(path)-CHARINDEX('\', REVERSE(path))) + '\Log.trc'  
                            FROM    sys.traces -- read all five trace files 
                            WHERE   is_default = 1  
                          ), DEFAULT) trace 
INNER JOIN sys.trace_events te on trace.EventClass = te.trace_event_id 
INNER JOIN TempDB.sys.tables  AS t ON trace.ObjectID = t.OBJECT_ID  
WHERE trace.DatabaseName = 'TempDB' 
  AND t.Name LIKE '#%' 
  AND te.name = 'Object:Created'  
  AND DATEPART(dy,t.create_date)= DATEPART(Dy,trace.StartTime)  
  AND ABS(DATEDIFF(Ms,t.create_date,trace.StartTime))<50 --sometimes slightly out 
ORDER BY t.create_date
```
**You cannot use user-defined datatypes in temporary tables unless the datatypes exist in TempDB; that is, unless the datatypes have been explicitly created.**

### User Tables in TempDB 

In normal use, you will create temporary tables, or table variables without thinking too deeply about it. 
However, it is interesting, though, that TempDB is there for any sort of sandbox activity. 
You can create ordinary base tables, views, or anything else you want. You can create schemas, stored procedures and so on. 
You’re unlikely to want to do this, but it is certainly possible since TempDB is just another database. 
I’ve just had to restart my development SQL Server after proving this to myself by installing AdventureWorks onto it. 
This means that it is possible to create a base table in TempDB, a sort of ..er… temporary permanent table. 
Unlike the global temporary table, you’d have to do all your own housekeeping on it: you’re on your own. The same is true of routines. 
The advantage of doing this is that any processing that you do uses TempDB’s simple recovery so that, if you fail to mop up, SQL Server acts as mother on the next startup: though this could be a very long time. 
The next stage is to have what I call a ‘persistent temporary’ table. 
In this table, the data itself is volatile when the server restarts, but the table itself persists. 
Probably the most common way to create a persistent Temporary table is to recreate on startup a global temporary table. 
This can be done automatically when all databases are recovered and the “Recovery is completed” message is logged. 
Even though this is a ‘global temporary’, it isn’t deleted when all connections using it have disappeared, because the process that runs it never disappears. 
Arguably, it is better to create this kind of  work table in the database that uses it, though, if you are using full recovery, the temporary work will remain in the log. 
You can, of course, just create an ordinary table in TempDB. You can create these ‘persistent’ tables on startup by defining a stored procedure in master that creates the global temporary table.

```sql
USE master 
go 
CREATE PROCEDURE createMyGlobalTables  AS 
   CREATE TABLE ##globalTemporary1 
      (-- Blah blah (insert DDL here) 
   CREATE TABLE ##globalTemporary2 
      (-- Blah blah (insert DDL here) 
--and so on.... 
   CREATE TABLE ##globalTemporaryn 
      (-- Blah blah (insert DDL here) 
  
go 
EXEC sp_procoption 'createMyGlobalTables', 'startup', 'true' 
-- A stored procedure that is set to autoexecution runs every time an instance of SQL Server is started
``` 
Why use this sort of hybrid table? 
There are, for example, a number of techniques for passing tables between procedures via ‘persistent’ tables in a multiprocess-safe way, so as to do a series of processing to the data. 
These are referred to a Process-keyed tables (see ‘How to Share Data Between Stored Procedures: [Process-Keyed table][6] by  Erland Sommarskog). 
They will initially raise the eyebrows of any seasoned DBA but they are an effective and safe solution to a perennial problem, when they are done properly. 

As well as temporary tables, there are also a number of  table types that aren’t directly derived from base tables, such as ‘fake’ tables and derived tables: 
some of these are so fleeting that they are best thought of as ephemeral rather than temporary. 
The CTE uses ephemeral tables that are ‘inline’ or ‘derived’ and aren’t materialised. 
BOL refers to them as ‘temporary named result sets’. 
They exist only within the scope of the expression. 
In a CTE, they have the advantage over derived tables in that they can be accessed more than once.


## Conclusions
+    **If you have less than 100 rows generally use a table variable**._Otherwise use a temporary table_. This is because ~SQL Server won't create statistics on table variables~. 
+    **If you need to create indexes on it then you must use a temporary table**. 
+    When using temporary tables always create them and create any indexes and then use them. This will help reduce recompilations. The impact of this is reduced starting in SQL Server 2005 but it's still a good idea.

In any shared playground, be very careful how you swing that bat. You’ll have realized, whilst reading this, that a lot of activity goes on in TempDB, and you can cause havoc to the whole SQL Server by using long-running processes that fill temporary tables, whatever type they are, with unnecessary quantities of data. In fact, I’ve given you clues in this article how to really, really, upset your DBA by inconsiderate use of that precious shared resource, the TempDB. (In the old days before S2005, using SELECT INTO with a huge table was the great V-weapon (Vergeltungswaffe) 

I’m always wary of providing over-generalized advice, but I always prefer my databases to use Table Variables, and TVPs wherever possible,  They require less resource, and you’re less likely to hold onto them when you’re finished with them.  I like to use them to the max, with column and table checks and constraints. You may find times when they run out of steam, especially when table sizes get larger. In cases like this, or where it isn’t practical to use table variables because of their restricted scope, then I’ll use local temporary tables. It takes a lot of pursed lips and shaking of heads before I’ll agree to a global temporary table or persistent temporary table. They have a few valid and perfectly reasonable uses, but they place reliance on the programmer to do the necessary housekeeping 

Always bear in mind that misuse of temporary tables, such as unnecessarily large, or too long-lived,  can have effects on other processes, even on other databases on the server. You are, after all, using a shared resource, and you wouldn’t treat your bathroom  that way would you?

[1]: http://example.com/  "Optional Title Here"
[2]: http://www.sqlteam.com/author/bill-graziano
[3]: http://www.sqlteam.com/article/temporary-tables
[4]: https://www.red-gate.com/simple-talk/author/phil-factor/
[5]: http://sqlserverplanet.com/optimization/temp-table-recompiles
[6]: http://www.sommarskog.se/share_data.html#prockeyed
[7]: https://www.red-gate.com/simple-talk/sql/t-sql-programming/temporary-tables-in-sql-server/

[<<](../sql.md) | [home](../../README.md)