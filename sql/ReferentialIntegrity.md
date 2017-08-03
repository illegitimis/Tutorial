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
(TODO)

## inner platform effect

In the database world, developers are sometimes tempted to [bypass the RDBMS](http://en.wikipedia.org/wiki/Inner-platform_effect), 
for example by storing everything in one big table with three columns labelled entity ID, key, and value. 
While this entity-attribute-value model allows the developer to break out from the structure imposed by an SQL database, 
it loses out on all the benefits, since all of the work that could be done efficiently by the RDBMS is forced onto the application instead. 
Queries become much more convoluted, the indexes and query optimizer can no longer work effectively, and data validity constraints are not enforced. 
Performance and maintainability can be extremely poor.




[<<](../SQL.md) 
| 
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 