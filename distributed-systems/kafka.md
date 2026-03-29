# Apache Kafka

_Getting Started with Apache Kafka_ by _Ryan Plant_ Pluralsight course page [1]

## .Net clients

List maintained by Apache [2]

`find-package kafka | Select-Object ID, Version, Description, DownloadCount | Sort-Object -Descending -Property DownloadCount | fl`

**ExactTargetDev/kafka-net [3]**
This is a .NET implementation of a client for Kafka using C# for Kafka 0.8. It provides for an implementation that covers most basic functionalities to include a simple Producer and Consumer.

**Microsoft/CSharpClient-for-Kafka [4]**
.Net implementation of the Apache Kafka Protocol that provides basic functionality through Producer/Consumer classes. The project also offers balanced consumer implementation. The project is a fork from ExactTarget's Kafka-net Client.

Jroland/kafka-net [5]
Pure C# client with full protocol support.  Includes consumer, producer, lower level components and gzip support (no snappy)
> From cwiki.apache.org: Clients [2]

**ah-/rdkafka-dotnet on GitHub [6]**  is a C# client for  Apache Kafka [7] based on  librdkafka [8].

**Microsoft/Kafkanet on GitHub [9]**
.NET implementation of the Apache Kafka Protocol that provides basic functionality through Producer/Consumer classes.
The project also offers balanced consumer implementation. The project is a fork from ExactTarget's Kafka-net Client. 

**ntent-ad/kafka4net on GitHub [10]** 
C# client, asynchronous, all 3 compressions supported (read and write), tracks leader partition changes transparently, long time in production.

**criteo/kafka-sharp on GitHub [11]**
kafka-sharp - High Performance .NET Kafka Driver

## Background

- Kafka is a **distributed**, **partitioned**, **replicated** _commit log service_. It provides the functionality of a _messaging system_, but with a unique design. What does all that mean?
- Apache™ Kafka is a fast, scalable, durable, and fault-tolerant publish-subscribe messaging system.
- Kafka is often used in place of traditional message brokers like JMS and **AMQP** because of its higher throughput, reliability and replication.
- Kafka works in combination with Apache Storm, Apache HBase and Apache Spark for real-time analysis and rendering of streaming data.
- Kafka can message geospatial data from a fleet of long-haul trucks or sensor data from heating and cooling equipment in office buildings.
- Whatever the industry or use case, Kafka brokers massive message streams for low-latency analysis in Enterprise Apache Hadoop.

> From  _http://hortonworks.com/apache/kafka/_ [12]
- **Apache Kafka** is an open-source [13] message broker [14] project developed by the Apache Software Foundation [15] written in Scala [16].
- The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds. It is, in its essence, **a massively scalable pub/sub message queue** _architected as a distributed transaction log_ 2 [17], making it highly valuable for enterprise infrastructures to **process streaming data**.
- The design is heavily influenced by transaction logs [18]. 3 [19]

>From _https://en.wikipedia.org/wiki/Apache\_Kafka_ [20]

***

First let's review some basic messaging terminology:

- Kafka maintains feeds of messages in categories called _topics_.
- We&#39;ll call processes that publish messages to a Kafka topic _producers_.
- We&#39;ll call processes that subscribe to topics and process the feed of published messages _consumers_.
- Kafka is run as a cluster comprised of one or more servers each of which is called a _broker_.

So, at a high level, producers send messages over the network to the Kafka cluster which in turn serves them up to consumers like this:

 ![alt text](https://g7udqw.by3302.livefilestore.com/y3m_iO5d-2s1tGAmB3j_oWs7hffUi0_wTY1WT6dDmB17-gQpGbfqyTHKCuxhMLGw6ZipuN-5QP9VmYDe0Co21SMvJ6XAa2pV1C4edIfTebgNWGb4Cld_TJMWiqGslN0-jP90NaP7EhpotLjvntRQEPf8pCrPLFDmYJEpxC79Yxjl1M?width=258&height=180&cropmode=none)

Communication between the clients and the servers is done with a simple, high-performance, language agnostic **TCP** protocol [21].

We provide a Java client for Kafka, but clients are available in many languages [22].

>From _http://kafka.apache.org/documentation.html#introduction_ [23] 

See our web site [24] for details on the project.
You need to have Gradle [25] and Java [26] installed. Kafka requires Gradle 2.0 or higher. Java 7 should be used for building in order to support both Java 7 and Java 8 at runtime.

>From _https://github.com/apache/kafka_ [27]

**The Log: What every software engineer should know about real-time data&#39;s unifying abstraction**

> From _https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying_ [28]

## What Kafka Does

Apache Kafka supports a wide range of use cases as a general-purpose messaging system for scenarios where high throughput, reliable delivery, and horizontal scalability are important. Apache Storm and Apache HBase both work very well in combination with Kafka. Common use cases include:

- Stream Processing
- Website Activity Tracking
- Metrics Collection and Monitoring
- Log Aggregation

Some of the important characteristics that make Kafka such an attractive option for these use cases include the following:

| **Feature** | **Description** |
| --- | --- |
| Scalability | Distributed system scales easily with no downtime |
| Durability | Persists messages on disk, and provides intra-cluster replication |
| Reliability | Replicates data, supports multiple subscribers, and automatically balances consumers in case of failure |
| Performance | High throughput for both publishing and subscribing, with disk structures that provide constant performance even with many terabytes of stored messages |

_From &lt;_ _http://hortonworks.com/apache/kafka/#section\_1_ [29]_&gt;_

## How Kafka Works

Kafka&#39;s system design can be thought of as that of a distributed commit log, where incoming data is written sequentially to disk. There are four main components involved in moving data in and out of Kafka:

- Topics
- Producers
- Consumers
- Brokers

 ![partition diagram](https://vbp6kg.by3302.livefilestore.com/y3mnzaqcjL9GHqNp7L5Oiqi8hn4focoT733Y-C_t-78oWrgFq61k_5lmF_Hnltu5uYEal1VYBy7XwVrJ2IJJ_VUMF-kLn_Z9UR_es_OZxF0OQJFp5vDV1JAhjQPzWRYIpeyMdLoeiAgiLe0y9Z_VB-4AH7K4Pj4buh8JoUFRrj_TD8?width=469&height=462&cropmode=none)

For Kafka consumers, keeping track of which messages have been consumed (processed) is simply a matter of keeping track of an **Offset** , which is a sequential id number that uniquely identifies a message within a partition. Because Kafka retains all messages on disk (for a configurable amount of time), consumers can rewind or skip to any point in a partition simply by supplying an offset value. Finally, this design eliminates the potential for back-pressure when consumers process messages at different rates.

> From _http://hortonworks.com/apache/kafka/#section\_2_ [30]

One of the keys to Kafka&#39;s high performance is the simplicity of the brokers&#39; responsibilities. In Kafka, topics consist of one or more Partitions that are ordered, immutable sequences of messages. Since writes to a partition are sequential, this design greatly reduces the number of hard disk seeks (with their resulting latency).

Another factor contributing to Kafka&#39;s performance and scalability is the fact that Kafka brokers are not responsible for keeping track of what messages have been consumed – that responsibility falls on the consumer. In traditional messaging systems such as JMS, the broker bore this responsibility, severely limiting the system&#39;s ability to scale as the number of consumers increased.

 ![broker diagram](https://hiqr5q.by3302.livefilestore.com/y3mL2zZ0kKbHelziORap8E_JcGlfWffIRMJ_1YMAyu4FquwOXE6O73jkHMzUzrZqe6WdOLVTJ29Uyn6IL9RQsqclmLgMQieF8yXj5pKbgFHBFNCgVepeppBPCXsJYulzLMreJi5OrHyzwi3aAso5JrtMI-xqfymEfAAs5Qe7kPefac?width=844&height=484&cropmode=none)

For Kafka consumers, keeping track of which messages have been consumed (processed) is simply a matter of keeping track of an Offset, which is a sequential id number that uniquely identifies a message within a partition. Because Kafka retains all messages on disk (for a configurable amount of time), consumers can rewind or skip to any point in a partition simply by supplying an offset value. Finally, this design eliminates the potential for back-pressure when consumers process messages at different rates.

## to-do

Apache Kafka for Beginners [31]

[<<](../messaging.md) | [home](../../README.md)

[1]: https://app.pluralsight.com/library/courses/apache-kafka-getting-started/table-of-contents
[2]: https://cwiki.apache.org/confluence/display/KAFKA/Clients#Clients-.NET
[3]: https://github.com/ExactTargetDev/kafka-net
[4]: https://github.com/Microsoft/CSharpClient-for-Kafka
[5]: https://github.com/Jroland/kafka-net
[6]: https://github.com/ah-/rdkafka-dotnet
[7]: http://kafka.apache.org/
[8]: https://github.com/edenhill/librdkafka
[9]: https://github.com/Microsoft/Kafkanet
[10]: https://github.com/ntent-ad/kafka4net
[11]: https://github.com/criteo/kafka-sharp
[12]: http://hortonworks.com/apache/kafka/
[13]: https://en.wikipedia.org/wiki/Open_source
[14]: https://en.wikipedia.org/wiki/Message_broker
[15]: https://en.wikipedia.org/wiki/Apache_Software_Foundation
[16]: https://en.wikipedia.org/wiki/Scala_%28programming_language%29
[17]: https://en.wikipedia.org/wiki/Apache_Kafka#cite_note-2
[18]: https://en.wikipedia.org/wiki/Transaction_log
[19]: https://en.wikipedia.org/wiki/Apache_Kafka#cite_note-3
[20]: https://en.wikipedia.org/wiki/Apache_Kafka
[21]: https://kafka.apache.org/protocol.html
[22]: https://cwiki.apache.org/confluence/display/KAFKA/Clients
[23]: http://kafka.apache.org/documentation.html#introduction
[24]: http://kafka.apache.org
[25]: http://www.gradle.org/installation
[26]: http://www.oracle.com/technetwork/java/javase/downloads/index.html
[27]: https://github.com/apache/kafka
[28]: https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
[29]: http://hortonworks.com/apache/kafka/#section_1
[30]: http://hortonworks.com/apache/kafka/#section_2
[31]: http://blog.cloudera.com/blog/2014/09/apache-kafka-for-beginners/
