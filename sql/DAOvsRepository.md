# DAO vs Repository

## DAO

DAO = **Data Access Object**, _goal is to abstract and encapsulate all access to the data and provide an interface_.
The DAO is usually able to __create an instance__ of a data object ("[to read data][1]") and also to __persist__ data ("[to save data][1]") to the datasource.
Use when you want to separate a data resource's client interface from its data access mechanisms, it allows clean separation of concerns.

![BookDAO inheritance hierarchy UML diagram](http://best-practice-software-engineering.ifs.tuwien.ac.at/patterns/images/dao.jpg)

The *Data Access Layer* (**DAL**) is the layer of a system that exists between the _business logic_ layer and the *persistence* / storage layer. 
A DAL might be a single class, or it might be composed of _multiple Data Access Objects (DAOs)_. 
It may have a facade over the top for the business layer to talk to, hiding the complexity of the data access logic. 
It might be a third-party object-relational mapping tool (ORM) such as Hibernate. 

__DAL is an architectural term, DAOs are a design detail__.  

In computer software, a [data access object (DAO)][2] is an object that provides an abstract interface to some type of database or other persistence mechanism. 
By mapping application calls to the persistence layer, DAO provide some specific data operations without exposing details of the database. 
This isolation _supports_ the **Single responsibility principle**. 
It separates what data accesses the application needs, in terms of _domain-specific objects_ and data types (the public interface of the DAO), 
from how these needs can be satisfied with a specific DBMS, database schema, etc. (the implementation of the DAO). 

Although this design pattern is equally applicable to the following: 
1- most programming languages; 
2- most types of software with persistence needs; and 
3- most types of databases) 
it is *traditionally* associated with [Java EE applications][3] and with relational databases (accessed via the JDBC API because of its origin in Sun Microsystems' [best practice guidelines][3] "Core J2EE Patterns" for that platform). 

**But a DAL is more than a group of DAOs**. 
It contains EVERYTHING related to persistence: DAOs, _entities which model how the data is stored_, 
if you're using a (micro) ORM and other internal services used by the DAOs. 
However the app accesses the DAL only via DAOs, which can be considered the '_entry points_' of DAL. 

Note that the DAO itself is just a concept and it's used as an abstraction, that is _the application doesn't know about the concrete object, it knows about an interface providing the desired functionality_. 
The DAO has intimate knowledge about the storage system but it exposes only behaviour which makes sense for the application i.e a DAO **should never expose or require information that is tied to a specific storage system**. 
**While a Repository is a concept, it is implemented as a DAO, at least from the application point of view**. 
In fact **every object used to deal with the storage is a DAO**, but **the Repository is a specialized DAO**. 
__It deals only with Business Objects__ and [acts as a facade for other lower level DAOs][4] (such as an ORM). 

The ORM tries to present a relational database in an object oriented way. 
It abstracts actual database access (that's why it's a DAO) but still deals with specific database concepts as the entities defined model the storage structure, the way data is saved. 
For many (CRUD) applications it can be enough and the application can use the objects returned by the ORM without caring that they are modelling persistence. 
For applications with complex behaviour, usually business applications, the Repository is a better choice as most of the time a business object is different than the way it's persisted.

## Repository

> [A Repository mediates between the domain and data mapping layers, acting like an in-memory domain object collection][5]. 
Client objects construct query specifications declaratively and submit them to Repository for satisfaction. 
Objects can be added to and removed from the Repository, as they can from a simple collection of objects, 
and the mapping code encapsulated by the Repository will carry out the appropriate operations behind the scenes.

Purpose: **persistent ingonorance**.
Use a repository to **separate the logic** that _retrieves_ the data and _maps_ it to the entity model from the business logic that acts on the model. 
The business logic should be **agnostic** to the type of data that comprises the data source layer. 
For example, the data source layer can be a database, a SharePoint list, or a Web service.
**Repositories remove dependencies that the calling clients have on specific technologies**. 
A repository centralizes the access logic for a service and _provides a substitution point for unit tests_. 
Services are often _expensive to invoke_ and _benefit_ from caching strategies that are *implemented within the repository*.

[As the repository is an abstraction it should aways return whatever the layer above want to work with][6], which in most cases are domain entities, i.e. the objects which will encapsulate the logic in your business code.

db repository interactions | web services repository 
---|---
![MSDN repository interactions schema](https://i-msdn.sec.s-msft.com/dynimg/IC340233.png) | ![web services repository](https://i-msdn.sec.s-msft.com/dynimg/IC340239.png)

## Links
+ [griffin DAL generator](http://blog.gauffin.org/2016/02/griffin-dal-generator-take-2/#more-8418)
+ [code review for a simple repository](https://codereview.stackexchange.com/questions/33109/repository-service-design-pattern)
+ [griffin.data](https://github.com/jgauffin/Griffin.Data)
+ [Data Access Object @ tuwien.ac.at][1]
+ [DAL @ wikipedia][2]
+ [SO answer][4]
+ [martin fowler def][5]
+ [repo done right][6]


[1]: http://best-practice-software-engineering.ifs.tuwien.ac.at/patterns/dao.html "Data Access Object @ tuwien.ac.at"
[2]: https://en.wikipedia.org/wiki/Data_access_layer "DAL @ wikipedia"
[3]: https://en.wikipedia.org/wiki/Data_access_object#cite_note-1 "cite"
[4]: https://stackoverflow.com/questions/28599968/retrieving-and-caching-nested-objects-from-a-rest-api "SO answer"
[5]: https://martinfowler.com/eaaCatalog/repository.html "martin fowler def"
[6]: http://blog.gauffin.org/2013/01/repository-pattern-done-right/ "repo done right"


[<<](../SQL.md) 
| 
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 