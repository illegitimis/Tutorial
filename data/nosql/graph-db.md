# Graph Databases

- cayley [1] An open-source graph database
- List of Graph Database Management Systems [2]
- HyperGraphDB Documentation [3]
- `HyperGraphDB` is a general purpose, extensible, portable, distributed, embeddable, open-source data storage mechanism. It is a graph database designed specifically for artificial intelligence and semantic web projects, it can also be used as an embedded object-oriented database for projects of all sizes [4].
- slashdot.org: Alternatives [5]
- `Trinity` and graph engine [6]
- graph db landscape 2013 pdf [7]
- Modelling Data with Hypergraphs. A closer look at `Grakn` Labs hypergraph data model. 2017 blog [8]
- Hypergraph wiki [9] & kobrix [10]
  
## TigerGraph

> A complete, distributed, parallel graph computing platform supporting web-scale data analytics in real-time.

- doc **REST**ful API User Guide [11], cors [12], yt playlists [13]
- integrations: REST API server [14], c# connector [15], TigerGraph.NET [16]
- host tgcloud [17]
- GSQL Language Reference 3.6 [18]
- Built-in Endpoints JSON Catalog [19]

## Neo4j

> install

Neo4j Enterprise 4.4.8 [20] for Developers \
How-To [21]: Run Neo4j in Docker [22]

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

Neo4j Graph Platform [23]

> model

Graph Modeling [24] Guidelines \
Graph Data Modeling [25] \
Neo4j - Building Blocks [26] \
Modelling Data in Neo4j: Bidirectional Relationships 2013 [27] \
neo4j/cypher: Aggregating relationships within a path 2013 [28]

> .net

.net driver 4.4.0 [29] \
Using Neo4j from .NET [30]

> sample

Guide [31]: Example Datasets \
Managing Multiple Databases [32] in Neo4j \
Built-in Movie Graph Example home [33], src [34]

[1]: https://github.com/cayleygraph/cayley
[2]: https://database.guide/list-of-graph-database-management-systems/
[3]: http://www.hypergraphdb.org/?project=hypergraphdb&page=LearnHyperGraphDB
[4]: https://github.com/hypergraphdb/hypergraphdb
[5]: https://slashdot.org/software/p/HyperGraphDB/alternatives
[6]: https://www.graphengine.io/docs/manual/TSL/index.html
[7]: http://www.odbms.org/wp-content/uploads/2013/11/Sones-AchimFriedland.pdf
[8]: https://medium.com/vaticle/modelling-data-with-hypergraphs-edff1e12edf0
[9]: https://en.wikipedia.org/wiki/Hypergraph
[10]: http://kobrix.com/hgdb.jsp
[11]: https://docs.tigergraph.com/dev/restpp-api
[12]: https://www.tigergraph.com/blog/working-with-tigergraph-rest-api-and-cors-cross-origin-resource-sharing/
[13]: https://www.youtube.com/c/TigerGraph/playlists
[14]: https://github.com/canbax/tiger-api
[15]: https://github.com/gpadvorac/TigerGraphConnector_CSharp
[16]: https://github.com/allisterb/TigerGraph.NET
[17]: https://tgcloud.io/
[18]: https://docs.tigergraph.com/gsql-ref/current/intro/intro
[19]: https://docs.tigergraph.com/tigergraph-server/current/api/json-catalog
[20]: https://neo4j.com/download/
[21]: https://neo4j.com/developer/docker-run-neo4j/
[22]: https://neo4j.com/developer/docker/
[23]: https://neo4j.com/developer/graph-platform/
[24]: https://neo4j.com/developer/guide-data-modeling/
[25]: https://neo4j.com/developer/data-modeling/
[26]: https://www.tutorialspoint.com/neo4j/neo4j_building_blocks.htm
[27]: https://graphaware.com/neo4j/2013/10/11/neo4j-bidirectional-relationships.html
[28]: https://www.markhneedham.com/blog/2013/06/27/neo4jcypher-aggregating-relationships-within-a-path/
[29]: https://neo4j.com/download-center/#drivers
[30]: https://neo4j.com/developer/dotnet/
[31]: https://neo4j.com/developer/example-data/
[32]: https://neo4j.com/developer/manage-multiple-databases/
[33]: https://github.com/neo4j-graph-examples/movies
[34]: https://github.com/neo4j-graph-examples/movies/blob/main/code/csharp/Example.cs


[<<](./index.md) | [home](../../README.md)
