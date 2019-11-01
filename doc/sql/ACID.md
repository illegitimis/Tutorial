# ACID

## principles

acronym | title | description
---|---|---
**A** | ATOMICITY | _all or nothing_ rule. If a part of the transaction fails, whole/entire transaction fails. Atomic nature of transactions. All operations in a transaction succeed or every operation is rolled back. All transaction operations are a [whole unit or atom][2]. An atomic transaction is either [fully completed][6], or is not begun at all. e.g.: transfer money from account A to account B. if system fails after subtracting from A, money gets returned to A.
**C** | CONSISTENCY | Only **valid data** is written to the database. When a transaction results in [invalid data][3], the database _reverts to its previous state_, which abides by all customary rules and constraints. On the completion of a transaction, the database is structurally sound. [A transaction cannot leave the database in an inconsistent state][5]. e.g.: Looking again at the account transfer system, the system is consistent if the total of all accounts is constant. If an error occurs and the money is removed from account A and not added to account B, then the total in all accounts would have changed. [The system would no longer be consistent][6]. By rolling back the removal from account A, the total will again be what it should be, and the system back in a consistent state.
**I** | ISOLATION | multiple transactions occurring at the same time not impact each other’s execution. No [interference][2]. Does not ensure their order. Transactions _do not contend_ with one another. _Contentious access_ to data is [moderated by the database][1] so that transactions appear to run sequentially. [If transactions are executed concurrently, the result is equivalent to their serial execution][4].
**D** | DURABILITY | ensures that any transaction committed to the database will not be lost. [Db backups and transaction logs][2] facilitate restoration. Completed transactions [persist][5], even when servers restart etc. [The results of applying a transaction are permanent, even in the presence of failures][1].

## glossary

- **write-ahead logging** ([WAL][2]) in which any transaction detail is first written to a log that includes both redo and undo information.
- **shadow-paging** in which a shadow page is created when data is to be modified. The query's updates are written to the shadow page rather than to the real data in the database. The database itself is modified only when the edit is complete.
- For many domains and use cases, ACID transactions are far more [pessimistic][1] (i.e., they’re more worried about data safety) than the domain actually requires.
- In the NoSQL world, ACID transactions are less fashionable as [some databases have loosened the requirements][1] for _immediate consistency_, _data freshness_ and _accuracy_ in order to gain other benefits, like **scale** and **resilience**. Notably, the .NET-based RavenDB has [bucked the trend](http://idioms.thefreedictionary.com/buck+the+trend)(_to be noticeably different from the way that a situation is developing generally_) among aggregate stores in supporting ACID transactions.

[< sql](../sql.md) | [> nosql](../nosql.md) | [home](../../README.md)

[1]: https://neo4j.com/blog/acid-vs-base-consistency-models-explained/
[2]: http://databases.about.com/od/specificproducts/a/acid.htm
[3]: https://www.techopedia.com/definition/23949/atomicity-consistency-isolation-durability-acid
[4]: https://dzone.com/articles/how-acid-mongodb
[5]: http://www.johndcook.com/blog/2009/07/06/brewer-cap-theorem-base/
[6]: https://msdn.microsoft.com/en-us/library/aa480356.aspx
