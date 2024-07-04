# Graph databases

- [cayley](https://github.com/cayleygraph/cayley) An open-source graph database
- [List of Graph Database Management Systems](https://database.guide/list-of-graph-database-management-systems/)
- HyperGraphDB [Documentation](http://www.hypergraphdb.org/?project=hypergraphdb&page=LearnHyperGraphDB)
- `HyperGraphDB` is a general purpose, extensible, portable, distributed, embeddable, open-source data storage mechanism. It is a graph database designed specifically for artificial intelligence and semantic web projects, it can also be used as an [embedded object-oriented database for projects of all sizes](https://github.com/hypergraphdb/hypergraphdb).
- https://slashdot.org/software/p/HyperGraphDB/alternatives
- `Trinity` and [graph engine](https://www.graphengine.io/docs/manual/TSL/index.html)
- graph db landscape [2013 pdf](http://www.odbms.org/wp-content/uploads/2013/11/Sones-AchimFriedland.pdf)
- Modelling Data with Hypergraphs. A closer look at `Grakn` Labs hypergraph data model. [2017 blog](https://medium.com/vaticle/modelling-data-with-hypergraphs-edff1e12edf0)
- Hypergraph [wiki](https://en.wikipedia.org/wiki/Hypergraph) & [kobrix](http://kobrix.com/hgdb.jsp)
  
## TigerGraph

> A complete, distributed, parallel graph computing platform supporting web-scale data analytics in real-time.

- doc [RESTful API User Guide](https://docs.tigergraph.com/dev/restpp-api), [cors](https://www.tigergraph.com/blog/working-with-tigergraph-rest-api-and-cors-cross-origin-resource-sharing/), [yt playlists](https://www.youtube.com/c/TigerGraph/playlists)
- integrations: [REST API server](https://github.com/canbax/tiger-api), [c# connector](https://github.com/gpadvorac/TigerGraphConnector_CSharp), [TigerGraph.NET](https://github.com/allisterb/TigerGraph.NET)
- host [tgcloud](https://tgcloud.io/)
- GSQL Language Reference [3.6](https://docs.tigergraph.com/gsql-ref/current/intro/intro)
- Built-in Endpoints [JSON Catalog](https://docs.tigergraph.com/tigergraph-server/current/api/json-catalog)

## Neo4j

> install

Neo4j [Enterprise 4.4.8](https://neo4j.com/download/) for Developers \
[How-To](https://neo4j.com/developer/docker-run-neo4j/): Run Neo4j in [Docker](https://neo4j.com/developer/docker/)

```sh
docker pull neo4j:4.4.8-enterprise
docker run --name testneo4j448e -p 7474:7474 -p 7687:7687 -d --env NEO4J_AUTH=neo4j/s3cr3t neo4j:4.4.8-enterprise --env=NEO4J_ACCEPT_LICENSE_AGREEMENT=yes
docker stop testneo4j448e
docker restart testneo4j448e
# then open http://localhost:7474 to connect with Neo4j Browser
docker pull neo4j:4.4.8-community
docker run --name testneo4j448c -p 7474:7474 -p 7687:7687 -d --env NEO4J_AUTH=neo4j/secr3T~ neo4j:4.4.8-community
```

> intro

Neo4j Graph [Platform](https://neo4j.com/developer/graph-platform/)

> model

Graph [Modeling](https://neo4j.com/developer/guide-data-modeling/) Guidelines \
Graph Data [Modeling](https://neo4j.com/developer/data-modeling/) \
Neo4j - [Building Blocks](https://www.tutorialspoint.com/neo4j/neo4j_building_blocks.htm) \
Modelling Data in Neo4j: Bidirectional Relationships [2013](https://graphaware.com/neo4j/2013/10/11/neo4j-bidirectional-relationships.html) \
neo4j/cypher: Aggregating relationships within a path [2013](https://www.markhneedham.com/blog/2013/06/27/neo4jcypher-aggregating-relationships-within-a-path/)

> .net

.net driver [4.4.0](https://neo4j.com/download-center/#drivers) \
Using Neo4j from [.NET](https://neo4j.com/developer/dotnet/)

> sample

[Guide](https://neo4j.com/developer/example-data/): Example Datasets \
Managing [Multiple Databases](https://neo4j.com/developer/manage-multiple-databases/) in Neo4j \
Built-in Movie Graph Example [home](https://github.com/neo4j-graph-examples/movies), [src](https://github.com/neo4j-graph-examples/movies/blob/main/code/csharp/Example.cs)

[<< home](../../README.md) | [< nosql](../nosql.md)