# cap theorem

> Computer science [theorem][3] that quantifies the _inevitable trade-offs_. [Eric Brewer’s CAP theorem][4] says that if you want _CAP_ you have to settle for two out of three.

acronym | title | description
---|---|---
**C** | consistency/sequential consistency | _All_ the replicas are in _sync_ and maintain the _same state_ of _any given object_ at **any given point of time**.
**A** | availability | A request will _eventually_ complete _successfully_. A read/write request on any node of the system will never be rejected as long as the particular node is up and running.
**P** | partition tolerance | (distributed system) [will continue to work unless there is a total network failure](http://www.johndcook.com/blog/2009/07/06/brewer-cap-theorem-base/). A few nodes can fail and the system keeps going. When the network connecting the nodes goes down, the system will still continue to operate even though some/all nodes can NO longer communicate with each other.

[sql](../sql.md) | [nosql](../nosql.md) | [home](../../README.md)

[1]: https://neo4j.com/blog/acid-vs-base-consistency-models-explained/
[2]: https://people.eecs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf
[3]: https://www.quora.com/What-Is-CAP-Theorem-1
[4]: http://www.julianbrowne.com/article/viewer/brewers-cap-theorem
