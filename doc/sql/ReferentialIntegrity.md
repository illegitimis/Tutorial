# Referential Integrity

## indices and primary keys

### Difference between an Index and a Primary Key

Indexes can be used for fast retrieval based on other columns. A primary key must be unique and cannot be nullable.  
A primary key is always indexed, meaning that a primary key is also always an index key.  
Keys are frequently good candidates for indexing and some DBMSs automatically create indexes for keys, but that doesn't have to be so. 
A key (minimal super key) is a set of attributes, the values of which are unique for every tuple.  
[An index is a performance optimization feature that enables data to be accessed faster](http://itknowledgeexchange.techtarget.com/sql-server/difference-between-an-index-and-a-primary-key/).  

Oracle Database enforces a UNIQUE key or PRIMARY KEY integrity constraint on a table by creating a unique index on the unique key or primary key.  
This index is automatically created by the database when the constraint is enabled.  
You can create indexes explicitly (outside of integrity constraints) using the SQL statement CREATE INDEX .  
Indexes can be unique or non-unique.  
Unique indexes guarantee that no two rows of a table have duplicate values in the key column (or columns).  
Non-unique indexes do not impose this restriction on the column values.  
Use the CREATE UNIQUE INDEX statement to create a unique index.

[The Primary Key is a logical object](https://msdn.microsoft.com/en-us/library/ms188783.aspx). 
By that I mean that is simply defines a set of properties on one column or a set of columns to require that the columns which make up the primary key are unique and that none of them are null. Because they are unique and not null, these values (or value if your primary key is a single column) can then be used to identify a single row in the table every time.  
In most if not all database platforms the Primary Key will have an index created on it. 
An index on the other hand doesn’t define uniqueness.  
An index is used to more quickly find rows in the table based on the values which are part of the index.  
When you create an index within the database, you are creating a physical object which is being saved to disk. 


### Difference between Key, Primary Key, Unique Key and Index in MySQL 

[Primary key does not allow null value but unique key allows null value](https://stackoverflow.com/questions/3844899/difference-between-key-primary-key-unique-key-and-index-in-mysql).  
We can declare only one primary key in a table but a table can have multiple unique key(column assign).  
Primary key makes the table row unique.  
Unique key makes the table column in a table row unique.  
An index is typically created on columns used in JOIN, WHERE, and ORDER BY clauses.  
Primary keys and unique keys are similar.  
A primary key is a column, or a combination of columns, that can uniquely identify a row.  
It is a special case of unique key.  
Also note that columns defined as primary keys or unique keys are automatically indexed in MySQL.

## foreign keys

You **should** always enforce referential integrity by using [_normal_ foreign keys][1].
We use referential integrity to validate data. But does that really help or hinder performance? 
The answers to these questions are Yes, they can and No, they don’t. 
**Foreign key constraint improve performance at the time of reading data** but at the same time it **slows down the performance at the time of inserting / modifying / deleting data**. 
In case of reading the query, the _optimizer can use foreign key constraints to create more efficient query plans_ as foreign key constraints are pre declared rules. 
This usually involves skipping some part of the query plan because for example the optimizer can see that because of a foreign key constraint, it is unnecessary to execute that particular part of the plan.
run the following query from Query menu and include _Actual Execution plan_.

```sql
create table Employee(EmployeeID int primary key)  
create table EmployeeOrder(OrderID int primary key, EmployeeID int not null constraint fkOrderCust references Employee(EmployeeID)) 
Select * from EmployeeOrder eo  
where exists  
(  
  select * From Employee e  
  where eo.EmployeeID = e.EmployeeID  
) 
```
You can notice that ~optimizer did not access Employee table~ and is not shown in execution plan. 
This is because the optimizer knows that it is _not necessary to execute the EXISTS operator_ in this query because the foreign key constraint(Trusted constraint) requires all EmployeeOrders to refer to an existing Employee, which is what the WHERE clause checks.

[Yes, having foreign key constraints in place can improve query performance](http://stackoverflow.com/a/8154375/2239678). 
There are various transforms that are open to the optimizer when appropriate foreign key constraints exist that are not generally available. 
For example, if you were to join A and B but only select data from B, the optimizer could eliminate A from the query plan entirely if there was a foreign key constraint in place 
(this sort of thing comes in very handy when you've got useful views that join in more tables than your current query strictly needs because 
you don't have to trade the performance costs of the extra joins against the code reuse from using an existing view). 
They also come in handy when you're doing things like using things like query rewrite to rewrite a query to use a materialized view in a data warehouse/ DSS type system. 

Foreign Keys **are a referential integrity tool, not a performance tool**. 
[At least in SQL Server](http://stackoverflow.com/a/507197/2239678), the creation of an FK does not create an associated index, and you should create indexes on all FK fields to improve look up times.  

SQL Server 7.0 / 2000 came with '[index tuning wizard](http://gotoanswer.stanford.edu/?q=Improving+SQL+Server+query+performance)' this functionality has been around for a long time. 
I'd recommend having a look at `select * from sys.dm_db_missing_index_details`. 
It tells you which indexes are 'missing', it's trivial to look in that table and then create indexes.

pro | con 
---|---
They are already implemented within the DBMS  | You are duplicating the work that has already been done. 
[They are declarative, self-documenting and "obvious"][2]. | It's imperative, probably "buried" deep in your application source code, and harder to maintain. 
They cannot be bypassed (unless explicitly disabled or dropped). | A single client application that has a bug can break the referential integrity ([and corrupt the data][3]). 
[They are correct][4]. | You are likely to implement them incorrectly in your application code. It looks simple from the outset, but in a concurrent environment, [it is easy to introduce race conditions][6]. 
They are [fast][5]. | Even if you have implemented them correctly, you probably used some form of locking to avoid race conditions, which is likely to be slower / less scalable than specially optimized FKs built into the DBMS. 
They support cascading referential actions (such as ON DELETE CASCADE). | You have to implement cascading yourself. 
The DBMS knows the data is related, [allowing it to find a better query][7] plan in some cases. | The DBMS doesn't know the data is related, which may produce sub-optimal query plan. 
If you are using an ORM tool, it can automatically generate references between objects. | You may need to do more manual work in your ORMt ool of choice.

## inner platform effect

In the database world, developers are sometimes tempted to [bypass the RDBMS](http://en.wikipedia.org/wiki/Inner-platform_effect), 
for example by storing everything in one big table with three columns labelled entity ID, key, and value. 
While this entity-attribute-value model allows the developer to break out from the structure imposed by an SQL database, 
it loses out on all the benefits, since all of the work that could be done efficiently by the RDBMS is forced onto the application instead. 
Queries become much more convoluted, the indexes and query optimizer can no longer work effectively, and data validity constraints are not enforced. 
Performance and maintainability can be extremely poor.


[1]: https://stackoverflow.com/questions/20842756/sql-indirect-foreign-key "Sql - Indirect Foreign Key"
[2]: https://stackoverflow.com/questions/15653245/no-foreign-key-constraints-in-database "no fk constraints"
[3]: https://www.experts-exchange.com/articles/4293/Can-Foreign-key-improve-performance.html "Can Foreign key improve performance?"
[4]: https://stackoverflow.com/questions/22020218/foreign-keys-are-evil "evil fk"
[5]: https://stackoverflow.com/questions/3434951/foreign-keys-what-do-they-do-for-me "Foreign Keys - What do they do for me?"
[6]: https://stackoverflow.com/a/20777244 "Database FK Constraints vs Programmatic FK Constraints"
[7]: https://stackoverflow.com/a/8154375 "Do foreign key constraints influence query transformations in Oracle?"

[<<](../sql.md) | [home](../../README.md)