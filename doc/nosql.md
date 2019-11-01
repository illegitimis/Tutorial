# No Sql

> The group of `NoSQL` [databases][1] collectively known as **aggregate stores** (term coined by Martin Fowler) includes **key-value** stores, **wide-column** stores and **document** stores.

- [Azure Cosmos DB](./nosql/cosmos.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./nosql/cosmos.md)
- [DocumentDB](./nosql/DocumentDB.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./nosql/DocumentDB.md)
- [**Mongo**](./nosql/Mongo.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./nosql/Mongo.md)
- [acid](./sql/ACID.md) vs [base](./nosql/BASE.md) & [CAP](./nosql/CAP.md) theorem
- [ranking](https://db-engines.com/en/ranking/relational+dbms)

Type | description | example
---|---|---
`KV` | large, _distributed_ **hashmap** data structures that store and retrieve values organized by identifiers known as _keys_ | Redis
`WC` | ![alt](https://s3.amazonaws.com/dev.assets.neo4j.com/wp-content/uploads/20181127035625/wide-column-store-example.png) | Apache Cassandra
`DOC` | natural hierarchies of structured documents | MongoDb

trait | pro / con
---|---
data relationship insight | KV  &#x2716;
high availability | KV &#x2714;
horizontal scaling | DOC &#x2716; explicit sharding plan
scale | KV &#x2714;, WC &#x2714;
sets of information for several records | KV &#x2716; (mapreduce+latency)

[home](../README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki)

[1]: https://neo4j.com/blog/aggregate-stores-tour/

  - [key-value](https://neo4j.com/developer/graph-db-vs-nosql/#_relate_key_value_stores_with_graph_databases)
  - and [document stores](https://neo4j.com/developer/graph-db-vs-nosql/#_navigate_document_stores_with_graph_databases)