# cap theorem

> Computer science [theorem][3] that quantifies the _inevitable trade-offs_. [Eric Brewer’s CAP theorem][4] says that if you want _CAP_ you have to settle for two out of three.

acronym | title | description
---|---|---
**C** | consistency/sequential consistency | _All_ the replicas are in _sync_ and maintain the _same state_ of _any given object_ at **any given point of time**. _Every node_ contains same data at the same time. Simply put, performing _a read operation will return the value of the most recent write_ operation causing all nodes to return the same data. A system has consistency if a transaction starts with the system in a consistent state, and ends with the system in a consistent state. In this model, a system can (and does) shift into an inconsistent state during a transaction, but the entire transaction gets rolled back if there is an error during any stage in the process.
**A** | availability | A request will _eventually_ complete _successfully_. A read/write request on any node of the system will never be rejected as long as the particular node is up and running. _Every_ request receives a response indicating success or failure. _At least one node must be available to serve data every time_.
**P** | partition tolerance | (distributed system) _will continue to work unless there is a total network failure_. A few nodes can fail and the system keeps going. When the network connecting the nodes goes down, the system will still continue to operate even though some/all nodes can NO longer communicate with each other. This condition states that the system continues to run, despite the number of messages being delayed by the network between nodes. A system that is partition-tolerant can sustain any amount of network failure that doesn’t result in a failure of the entire network. Data records are **sufficiently replicated** across combinations of nodes and networks to keep the system up through _intermittent outages_. When dealing with modern distributed systems, Partition Tolerance is not an option. It’s a [necessity](5). Hence, we have to trade between Consistency and Availability.

## todo

masterX-masterY setup
X-Y comm down
can't sync data/updates
P is a must
either allow out-of-sync: lose C gain A
report the system as unavailable: keep C lose A

## 2pc

- http://dbmsmusings.blogspot.com/2019/01/its-time-to-move-on-from-two-phase.html
- https://docs.mongodb.com/v3.4/tutorial/perform-two-phase-commits/
- https://www.kamilgrzybek.com/design/the-outbox-pattern/
- https://docs.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/subscribe-events


[sql](../sql.md) | [nosql](../nosql.md) | [home](../../README.md)

[1]: https://neo4j.com/blog/acid-vs-base-consistency-models-explained/
[2]: https://people.eecs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf
[3]: https://www.quora.com/What-Is-CAP-Theorem-1
[4]: http://www.julianbrowne.com/article/viewer/brewers-cap-theorem
[5]: https://towardsdatascience.com/cap-theorem-and-distributed-database-management-systems-5c2be977950e
[6]: https://www.innoarchitech.com/blog/how-choose-right-database-system-relational-rdbms-vs-nosql-vs-newsql
[7]: http://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf
[8]: https://www.quora.com/q/ebzrgpkirtzpthyb/Distributed-Systems-Part-2-Consistency-versus-Availability-A-Pragmatic-Example
[9]: https://fenix.tecnico.ulisboa.pt/downloadFile/1126518382178117/10.e-CAP-3.pdf
[10]: http://ksat.me/a-plain-english-introduction-to-cap-theorem/
[11]: https://github.com/dotnetcore/CAP
[12]: http://cap.dotnetcore.xyz/user-guide/en/getting-started/quick-start/
[13]: https://stackoverflow.com/questions/11292215/where-does-mongodb-stand-in-the-cap-theorem
[14]: https://aphyr.com/posts/322-call-me-maybe-mongodb-stale-reads
[15]: https://gist.github.com/armon/11059431
[16]: https://github.com/etcd-io/etcd/issues/741
[17]: https://blog.nahurst.com/visual-guide-to-nosql-systems
