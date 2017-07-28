# Mongo schema

## state of the art

+ [SQL to MongoDB Mapping Chart](https://docs.mongodb.com/manual/reference/sql-comparison/)
+ [MSSQL To MongoDB Tool](https://mssql2mongo.codeplex.com/) (SQL2Mongo)is a tool to migrate all schema & data from Microsoft SQL Server to MongoDB. It is easily to set Primary Key column and tables which you want to migrate. 
_Codeplex shutting down_, [download](https://mssql2mongo.codeplex.com/downloads/get/684290), or [1drv](https://1drv.ms/u/s!As0cxZAk26SzjMEzfosSkRmeiQbzCA), or [source](https://mssql2mongo.codeplex.com/SourceControl/latest).
+ [prantlf/Northwind.js](https://gist.github.com/prantlf/2afd29c30130c9beef64) Helps obtaining and using a local copy of the Northwind database in MongoDB and testing an OData server with JayData 
+ [MongoDB SQL Server Importer](https://sql2mongo.codeplex.com/SourceControl/latest#src/MongoSqlImporter/MongoSqlImporter/Program.cs) quick and dirty brute force importer. Duplicated [source on 1drv](https://1drv.ms/u/s!As0cxZAk26SzjME0fHrz5_fMUfpmjw).
+ [Migrating from Relational Databases to MongoDB](https://www.slideshare.net/matkeep/migrating-from-relational-databases-to-mongodb) slides
+ [Migration from SQL to MongoDB - A Case Study at TheKnot.com](https://www.slideshare.net/mongodb/migration-from-sql-to-mongodb-a-case-study-at-theknotcom) slides
+ [Migrating from RDBMS to MongoDB](https://www.slideshare.net/mongodb/migrating-from-rdbms-to-mongodb) slides
+ [Firehose](https://github.com/breinero/Firehose) An import and work generator for MongoDB. 
+ [mongomtimport](https://github.com/buzzm/mongomtimport/blob/master/README.md) Multithreaded Java file loader for mongoDB, [fork](https://github.com/mongodb-labs/mongomtimport)

## [MongoDB relationships: embed or reference?](http://stackoverflow.com/questions/5373198/mongodb-relationships-embed-or-reference#5373969)

This is more an art than a science. 
The Mongo Documentation on Schemas is a good reference, but here are some things to consider:
1. **Put as much in as possible**
   The joy of a Document database is that it eliminates lots of Joins. 
   Your first instinct should be to place as much in a single document as you can. 
   Because MongoDB documents have structure, and because you can efficiently query within that structure there is _no immediate need to normalize data_ like you would in SQL. 
   In particular _any data that is not useful apart from its parent document should be part of the same document_.
2. **Separate data that can be referred to from multiple places into its own collection**.
   This is not so much a "storage space" issue as it is a "_data consistency_" issue. 
   If many records will refer to the same data it is more efficient and less error prone to update a single record and keep references to it in other places.
3. Document size considerations
   MongoDB imposes a 4MB (16MB with 1.8) size limit on a single document. 
   In a world of GB of data this sounds small, but it is also 30 million tweets or 250 thousand typical Stack Overflow answers or 20 flicker photos. 
   On the other hand, this is far more information than one might want to present at one time on a typical web page. 
   First consider what will make your queries easier. In many cases concern about document sizes will be premature optimization.
4. Complex data structures:
   MongoDB can store arbitrary deep nested data structures, but cannot search them efficiently. 
   If your data forms a tree, forest or graph, you effectively need to store each node and its edges in a separate document. 
   (Note that there are data stores specifically designed for this type of data that one should consider as well)
   It has also been pointed out than it is impossible to return a subset of elements in a document. 
   If you need to pick-and-choose a few bits of each document, it will be easier to separate them out.
5. Data Consistency
   MongoDB makes a tradeoff between efficiency and consistency. 
   The rule is changes to a single document are always atomic, while updates to multiple documents should never be assumed to be atomic. 
   There is also no way to "lock" a record on the server (you can build this into the client's logic using for example a "lock" field). 
   When you design your schema consider how you will keep your data consistent. Generally, 
   the more that you keep in a document the better.

## linking vs embedding

Both solutions(_separate collections_ vs. _embedded documents_) have their strengths and weaknesses. Learn to use [both](http://openmymind.net/Multiple-Collections-Versus-Embedded-Documents/).
- [Separate collections offer the greatest querying flexibility](http://openmymind.net/Multiple-Collections-Versus-Embedded-Documents/#4)
- [Selecting embedded documents is more limited](http://openmymind.net/Multiple-Collections-Versus-Embedded-Documents/#5)
- A document, including all its embedded documents and arrays, cannot exceed 16MB
- Embedded documents are easy and fast (single seek)
- [Separate collections require more work](http://openmymind.net/Multiple-Collections-Versus-Embedded-Documents/#7)
- So, separate collections are good if you need to select individual documents, need more control over querying, or have huge documents.
Embedded documents are good when you want the entire document, the document with a $slice of comments, or with no comments at all.
- As a general rule, if you have a lot of "comments" or if they are large, a separate collection might be best. 
Smaller and/or fewer documents tend to be a natural fit for embedding.

## Embedded / nested / denormalized

1. [better performance for read operations](https://docs.mongodb.com/manual/core/data-model-design/), as well as the ability to request and retrieve related data in a single database operation
2. update related data in a single atomic write operation
3. [Person-Address pattern **(one to one)**](https://docs.mongodb.com/manual/tutorial/model-embedded-one-to-one-relationships-between-documents/#data-modeling-example-one-to-one)
```js
{
   _id: "joe",
   name: "Joe Bookreader",
   address: {
              street: "123 Fake Street",
              city: "Faketon",
              state: "MA",
              zip: "12345"
            }
}
``` 
4. [Person-Address pattern **(one to many)**](https://docs.mongodb.com/manual/tutorial/model-embedded-one-to-many-relationships-between-documents/)
```js
{
   _id: "joe",
   name: "Joe Bookreader",
   addresses: [
                {
                  street: "123 Fake Street",
                  city: "Faketon",
                  state: "MA",
                  zip: "12345"
                },
                {
                  street: "1 Some Other Street",
                  city: "Boston",
                  state: "MA",
                  zip: "12345"
                }
              ]
 }
```

## Normalized / linked / referenced

1. when embedding would result in **duplication** of data but would not provide sufficient _read performance advantages to outweigh the implications of the duplication_.
2. to represent more complex many-to-many relationships
3. [publisher and book relationship **(one to many)**](https://docs.mongodb.com/manual/tutorial/model-referenced-one-to-many-relationships-between-documents/#data-modeling-publisher-and-books)
Avoid repetition of publisher data
number of books per publisher is small with limited growth, store the book reference inside the publisher document… 
otherwise in a normal scenario a lot of books, small no publishers => keep a publisher ref inside the book
if the number of books per publisher is unbounded, this data model would lead to **mutable, growing arrays**
```js
{
   name: "O'Reilly Media",
   founded: 1980,
   location: "CA",
   books: [12346789, 234567890,    ]
}
``` 
4. When using references, the growth of the relationships determine where to store the reference
```js
{
   _id: 123456789,
   title: "MongoDB: The Definitive Guide",
   author: [ "Kristina Chodorow", "Mike Dirolf" ],
   published_date: ISODate("2010-09-24"),
   pages: 216,
   language: "English",
   publisher_id: "oreilly"
}
```
5. [Model Tree Structures with Parent References](https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-parent-references/) 
organizes documents in a tree-like structure by storing references to “parent” nodes in “child” nodes.
6. [Model Tree Structures with Child References](https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-child-references/)
organizes documents in a tree-like structure by storing references to “child” nodes in “parent” nodes.
7. [Model Tree Structures with an Array of Ancestors](https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-ancestors-array/)
tree-like structure by storing references to “parent” nodes and an array that stores all ancestors.
8. [Model Tree Structures with Materialized Paths](https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-materialized-paths/)
   storing full relationship paths between documents. 
   In addition to the tree node, each document stores the _id of the nodes ancestors or path as a string.
9. [Model Tree Structures with Nested Sets](https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-nested-sets/)
optimizes discovering subtrees at the expense of tree mutability.



