# ACID

## principles

acronym | title | description
---|---|---
**A** | ATOMICITY | “_all or nothing_” rule. If a part of the transaction fails, whole/entire transaction fails. 
Atomic nature of transactions. All transaction operations are a [whole unit or atom](http://databases.about.com/od/specificproducts/a/acid.htm). 
An atomic transaction is either [fully completed](https://msdn.microsoft.com/en-us/library/aa480356.aspx), or is not begun at all.
e.g.: transfer money from account A to account B. if system fails after subtracting from A, money gets returned to A.
**C** | CONSISTENCY | Only **valid data** is written to the database.
When a transaction results in [invalid data](https://www.techopedia.com/definition/23949/atomicity-consistency-isolation-durability-acid), 
the database _reverts to its previous state_, which abides by all customary rules and constraints. 
[A transaction cannot leave the database in an inconsistent state](http://www.johndcook.com/blog/2009/07/06/brewer-cap-theorem-base/). 
e.g.: Looking again at the account transfer system, the system is consistent if the total of all accounts is constant. 
If an error occurs and the money is removed from account A and not added to account B, then the total in all accounts would have changed. 
[The system would no longer be consistent](https://msdn.microsoft.com/en-us/library/aa480356.aspx). 
By rolling back the removal from account A, the total will again be what it should be, and the system back in a consistent state. 
**I** | ISOLATION | multiple transactions occurring at the same time not impact each other’s execution 
No [interference](http://databases.about.com/od/specificproducts/a/acid.htm). Does not ensure their order.
Transactions ~do not contend~ with one another. 
_Contentious access_ to data is [moderated by the database](https://neo4j.com/blog/acid-vs-base-consistency-models-explained/) so that transactions appear to run sequentially.
[If transactions are executed concurrently, the result is equivalent to their serial execution](https://dzone.com/articles/how-acid-mongodb). 
**D** | DURABILITY | ensures that any transaction committed to the database will not be lost. 
[Db backups and transaction logs facilitate restoration](http://databases.about.com/od/specificproducts/a/acid.htm). 
[Completed transactions persist](http://www.johndcook.com/blog/2009/07/06/brewer-cap-theorem-base/), even when servers restart etc. 
[The results of applying a transaction are permanent, even in the presence of failures](https://neo4j.com/blog/acid-vs-base-consistency-models-explained/). 

## glossary

- **write-ahead logging** ([WAL](http://databases.about.com/od/specificproducts/a/acid.htm)) 
in which any transaction detail is first written to a log that includes both redo and undo information. 
- **shadow-paging** in which a shadow page is created when data is to be modified. 
The query's updates are written to the shadow page rather than to the real data in the database. 
The database itself is modified only when the edit is complete.
- For many domains and use cases, ACID transactions are far more [pessimistic](https://neo4j.com/blog/acid-vs-base-consistency-models-explained/) 
(i.e., they’re more worried about data safety) than the domain actually requires.  
- In the NoSQL world, ACID transactions are less fashionable as [some databases have loosened the requirements](https://neo4j.com/blog/acid-vs-base-consistency-models-explained/) 
for _immediate consistency_, _data freshness_ and _accuracy_ in order to gain other benefits, like **scale** and **resilience**.  
(Notably, the .NET-based RavenDB has [bucked the trend](http://idioms.thefreedictionary.com/buck+the+trend) among aggregate stores in supporting ACID transactions.) 
_to be noticeably different from the way that a situation is developing generally_



[<<](../SQL.md)
|
[home](../README.md)
|
[wiki](https://github.com/illegitimis/Tutorial/wiki)