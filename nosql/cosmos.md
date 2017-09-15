# Azure Cosmos DB

+ A **multi-model**, **schema-free**, fully schema agnostic database.
+ A _globally distributed_ database designed for _scalable_, _broadly distributed_, _highly responsive_ and _highly available_ applications.
+ ~Superset data service of DocumentDB~. Earlier, Microsoft offered DocumentDB as _Data as a Service_ (*DaaS*), which supported a _limited set of features_ and functionalities. Microsoft’s engineers shared their challenges, running the company’s cloud-based services, such as Bing, Azure and Office 365 using DocumentDB. Microsoft understood their engineer’s challenges and marketed the opportunity to take DocumentDB [to the next level][1].
+ Azure Cosmos DB also supports _several NoSQL APIs_ including DocumentDB SQL, MongoDB, Gremlin, and Azure Tables/Table Storage.
+ can handle a variety of data to store, like key-value, document, columnar, and graph types. This database engine is based on the _atom-record-sequence_ (**ARS**) data model. 
+  ?? Cosmos DB provides a method to the user to _distinguish between transactions with high latency_ vs. a database being unavailable ??
+ Azure Cosmos DB engine is designed to manage elastically scaled throughput, based on the [application traffic patterns][1] across different geographical regions, to support fluctuating workloads varying both by geography and time.
+ MS advertises **guaranteed single-digit millisecond latency**, SLAs for latency at the 99th percentile, together with five well-defined 
consistency levels: _strong, bounded staleness, session, consistent-prefix and eventual_.
+ [Azure Cosmos DB With SQL Query Cheat Sheet](./microsoft-documentdb-sql-query-cheat-sheet-v4.pdf) pdf.
+ DocumentDB can [determine the schema][3] and index data as documents are inserted, and lets you query against that index. This is possible due to DocumentDB's deep commitment to the JSON data model.
+ Cosmos DB supports relational, hierarchical, and spatial querying of JSON documents using SQL without specifying a schema or secondary indexes, JavaScript user defined functions (UDFs), JavaScript operators, and a multitude of built-in functions. The SQL type system, expression evaluation, function invocation (UDFs), and other aspects of DocumentDB mirror that of JavaScript. DocumentDB is a JSON document database capable of executing JavaScript directly in the database engine, using JavaScript's programming model as the foundation for the query language.
+ [SQL queries for Azure Cosmos DB DocumentDB API][4] ms docs.
+ [Connect a MongoDB application to Azure Cosmos DB][5]
+ [Sample - Customer Reviews App with Cognitive Services (Azure Functions tools for Visual Studio 2017)][6]
+ DocumentDB index management [sample][7]
+ [DocumentDB API][2] docs
+ [todo](http://www.zdnet.com/article/inside-cosmos-db/)
+ [todo](https://techcrunch.com/2017/05/10/with-cosmos-db-microsoft-wants-to-build-one-database-to-rule-them-all/)
+ [pdf todo](https://softwareengineeringdaily.com/wp-content/uploads/2017/06/SEDT22-Cosmos-DB.pdf)
+ [Azure Cosmos DB: Getting started with the DocumentDB API and .NET Core](https://docs.microsoft.com/en-us/azure/cosmos-db/documentdb-dotnetcore-get-started)
+ [default indexing](http://blog.ulriksen.net/default-indexing-in-cosmos-db/)

[1]: http://www.databasejournal.com/features/mssql/introduction-to-azure-cosmos-db.html
[2]: https://docs.microsoft.com/en-us/azure/cosmos-db/documentdb-introduction
[3]: http://www.c-sharpcorner.com/article/azure-cosmos-db-with-sql-query-cheat-sheet-pdf/
[4]: https://docs.microsoft.com/en-us/azure/cosmos-db/documentdb-sql-query
[5]: https://docs.microsoft.com/en-us/azure/cosmos-db/connect-mongodb-account
[6]: https://azure.microsoft.com/en-us/resources/samples/functions-customer-reviews/
[7]: https://github.com/Azure/azure-documentdb-dotnet/blob/master/samples/code-samples/IndexManagement/Program.cs


[<<](../nosql.md)
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 