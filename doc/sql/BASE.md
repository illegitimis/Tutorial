# BASE

acronym | title | description
---|---|---
**BA** | Basic Availability | [The database appears to work most of the time](https://neo4j.com/blog/acid-vs-base-consistency-models-explained/).  
**S** | Soft-state | Stores _don’t have to be write-consistent_, nor do different replicas have to be ~mutually consistent~ all the time.
**E** | Eventual consistency | Stores [exhibit consistency at some later point](https://neo4j.com/blog/acid-vs-base-consistency-models-explained/) (e.g., lazily at read time).

- There is a computer science theorem that quantifies the inevitable trade-offs. [Eric Brewer’s CAP theorem](http://www.julianbrowne.com/article/viewer/brewers-cap-theorem) says that if you want consistency, availability, and partition tolerance, you have to settle for two out of three. (For a distributed system, partition tolerance means the [system will continue to work unless there is a total network failure](http://www.johndcook.com/blog/2009/07/06/brewer-cap-theorem-base/). A few nodes can fail and the system keeps going.)
- Forfeit the C and I in ACID for availability, in favor of [graceful degradation and performance](https://people.eecs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf).
- A BASE datastore values availability (since that’s important for scale), but it doesn’t offer guaranteed consistency of replicated data at write time. Overall, the BASE consistency model provides a **less strict assurance than ACID**, _data will be consistent in the future_
  - either at read time (e.g., Riak)
  - or [it will always be consistent](https://neo4j.com/blog/acid-vs-base-consistency-models-explained/) but only for certain processed past snapshots (e.g., Datomic)
- The BASE consistency model is primarily used by [aggregate stores](https://neo4j.com/blog/aggregate-stores-tour/)
  - including column family
  - [key-value](https://neo4j.com/developer/graph-db-vs-nosql/#_relate_key_value_stores_with_graph_databases)
  - and [document stores](https://neo4j.com/developer/graph-db-vs-nosql/#_navigate_document_stores_with_graph_databases)

[<<](../sql.md) | [home](../../README.md)