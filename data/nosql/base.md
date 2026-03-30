---
title: BASE
layout: default
nav_order: 2
parent: NoSQL
grand_parent: Data
last_modified_date: 2026-03-29 21:39:07 +00:00
---

# BASE

acronym | title | description
---|---|---
**BA** | Basic Availability | [The database appears to work most of the time][1].
**S** | Soft-state | Stores _don’t have to be write-consistent_, nor do different replicas have to be _mutually consistent_ all the time.
**E** | Eventual consistency | Stores [exhibit consistency at some later point][1] (e.g., lazily at read time).

- Forfeit the C and I in **ACID** for availability => [AciD][2], in favor of _graceful degradation and performance_.
- A BASE datastore values _availability_ (since that’s important for **scale**)
- but it doesn’t offer _guaranteed consistency of replicated data_ at write time.
- Overall, the **BASE** consistency model provides a **less strict assurance than ACID**, _data will be consistent in the future_
  - Read time (e.g., `Riak`)
  - [always consistent][1] but only for certain processed past _snapshots_ (e.g., `Datomic`)
- The BASE consistency model is primarily used by [aggregate stores][3]

[1]: https://neo4j.com/blog/acid-vs-base-consistency-models-explained/
[2]: https://people.eecs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf
[3]: https://neo4j.com/blog/aggregate-stores-tour/

[<](./index.md) | [<<](/index.md)
