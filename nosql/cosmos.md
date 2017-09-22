# Azure Cosmos DB

## Abstract

+ A **multi-model**, **schema-free**, fully schema agnostic database.
![multi model](https://tctechcrunch2011.files.wordpress.com/2017/05/2017-05-08_1533.png)
+ A _globally distributed_ database designed for _scalable_, _broadly distributed_, _highly responsive_ and _highly available_ applications.
+ ~Superset data service of DocumentDB~. Earlier, Microsoft offered DocumentDB as _Data as a Service_ (*DaaS*), which supported a _limited set of features_ and functionalities. 
Microsoft’s engineers shared their challenges, _running the company’s cloud-based services_, 
such as Bing, Azure and Office 365 using DocumentDB. 
Microsoft understood their engineer’s challenges and marketed the opportunity to take DocumentDB [to the next level][1].
Being geo-distributed across Azure regions/data centers it's already available in all of them, 
and [will be automatically available in new regions as they come online][8], 
because it's a foundational service for Microsoft's own properties.
Configuring geo-distribution is as simple as clicking on a map to add or drop regions, 
while the application continues to run. Microsoft aptly calls this feature "**global distribution turnkey**"
+ Azure Cosmos DB also supports _several NoSQL APIs_ including DocumentDB SQL, MongoDB, Apache Gremlin, and Azure Tables/Table Storage.
+ Can handle a variety of data to store (all four NoSql models), **key-value**, **document**, **columnar**, and **graph** types. 
This database engine is based on the _atom-record-sequence_ (**ARS**) data model. 
+  ?? ~Cosmos DB provides a method to the user to _distinguish between transactions with high latency_ vs. a database being unavailable~ ??
+ Azure Cosmos DB engine is _designed to manage_ **elastically scaled throughput**, based on the [application traffic patterns][1] 
across different geographical regions, to _support fluctuating workloads_ varying both by geography and time.
+ MS advertises **guaranteed single-digit millisecond latency**, SLAs for latency at the 99th percentile, 
together with five well-defined consistency levels: _strong, bounded staleness, session, consistent-prefix and eventual_.
![different consistency models](https://tctechcrunch2011.files.wordpress.com/2017/05/2017-05-08_1535.png)
+ It's _optimized for low-latency database reads and writes_. 
It does this through the use of [Solid State Disk storage and with "latchless" and "lockless" data structures][8] 
which, interestingly, bear some resemblance to those used by SQL Server's In-Memory OLTP model, as well.
+ DocumentDB can [determine the schema][3] and index data as documents are inserted, and lets you query against that index. 
This is possible due to DocumentDB's deep commitment to the JSON data model.
**Cosmos DB indexes every column by default**.
+ Cosmos DB supports relational, hierarchical, and spatial querying of JSON documents using SQL 
without specifying a schema or secondary indexes, 
JavaScript user defined functions (UDFs), JavaScript operators, and a multitude of built-in functions. 
The SQL type system, expression evaluation, function invocation (UDFs), and other aspects of DocumentDB mirror that of JavaScript. 
DocumentDB is a **JSON document database** _capable of executing JavaScript directly in the database engine_, using JavaScript's programming model as the foundation for the query language.

## Links

+ [Azure Cosmos DB: Getting started with the DocumentDB API and .NET Core](https://docs.microsoft.com/en-us/azure/cosmos-db/documentdb-dotnetcore-get-started)
+ [Azure Cosmos DB With SQL Query Cheat Sheet](./microsoft-documentdb-sql-query-cheat-sheet-v4.pdf) pdf.
+ [SQL queries for Azure Cosmos DB DocumentDB API][4] ms docs.
+ [Connect a MongoDB application to Azure Cosmos DB][5]
+ [Sample - Customer Reviews App with Cognitive Services (Azure Functions tools for Visual Studio 2017)][6]
+ DocumentDB index management [sample][7]
+ [DocumentDB API][2] docs
+ [todo](https://techcrunch.com/2017/05/10/with-cosmos-db-microsoft-wants-to-build-one-database-to-rule-them-all/)
+ [pdf todo](https://softwareengineeringdaily.com/wp-content/uploads/2017/06/SEDT22-Cosmos-DB.pdf)
+ [default indexing](http://blog.ulriksen.net/default-indexing-in-cosmos-db/)

[1]: http://www.databasejournal.com/features/mssql/introduction-to-azure-cosmos-db.html
[2]: https://docs.microsoft.com/en-us/azure/cosmos-db/documentdb-introduction
[3]: http://www.c-sharpcorner.com/article/azure-cosmos-db-with-sql-query-cheat-sheet-pdf/
[4]: https://docs.microsoft.com/en-us/azure/cosmos-db/documentdb-sql-query
[5]: https://docs.microsoft.com/en-us/azure/cosmos-db/connect-mongodb-account
[6]: https://azure.microsoft.com/en-us/resources/samples/functions-customer-reviews/
[7]: https://github.com/Azure/azure-documentdb-dotnet/blob/master/samples/code-samples/IndexManagement/Program.cs
[8]: http://www.zdnet.com/article/inside-cosmos-db/


[<<](../nosql.md)
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 