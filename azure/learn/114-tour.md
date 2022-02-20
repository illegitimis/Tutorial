# tour

> [tour-of-azure-services](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/tour-of-azure-services)

## diagram

![az svc](https://docs.microsoft.com/en-us/learn/azure-fundamentals/intro-to-azure-fundamentals/media/azure-services-6c41a736.png)

## compute

Service name | Service function
---|---
Azure Virtual Machines | Windows or Linux virtual machines (VMs) hosted in Azure.
Azure Virtual Machine Scale Sets | Scaling for Windows or Linux VMs hosted in Azure.
Azure Kubernetes Service | Cluster management for VMs that run containerized services.
Azure Service Fabric | Distributed systems platform that runs in Azure or on-premises.
Azure Batch | Managed service for parallel and high-performance computing applications.
Azure Container Instances | Containerized apps run on Azure without provisioning servers or VMs.
Azure Functions | An event-driven, serverless compute service.

## networking

Service name | Service function
---|---
Azure Virtual Network | Connects VMs to _incoming virtual private network_ (VPN) connections.
Azure Load Balancer | Balances inbound and outbound connections to applications or service endpoints.
Azure Application Gateway | Optimizes app server farm delivery while increasing application security.
Azure VPN Gateway | Accesses Azure Virtual Networks through high-performance VPN gateways.
Azure DNS | Provides ultra-fast DNS responses and ultra-high domain availability.
Azure Content Delivery Network | Delivers _high-bandwidth_ content to customers globally.
Azure DDoS Protection | Protects Azure-hosted applications from distributed denial of service (DDOS) attacks.
Azure Traffic Manager | Distributes network traffic across Azure regions worldwide.
Azure ExpressRoute | Connects to Azure over high-bandwidth _dedicated secure connections_.
Azure Network Watcher | Monitors and diagnoses network issues by using scenario-based analysis.
Azure Firewall | Implements high-security, high-availability firewall with unlimited scalability.
Azure Virtual WAN | Creates a unified wide area network (WAN) that connects local and remote sites.

## storage

Service name | Service function
---|---
Azure `Blob` storage | Storage service for very large objects, such as video files or bitmaps.
Azure `File` storage | File shares that can be accessed and managed like a file server.
Azure `Queue` storage | data store for queuing and reliably delivering messages between applications.
Azure `Table` storage | Table storage is a service that stores non-relational structured data (also known as structured NoSQL data) in the cloud, providing a _key/attribute_ store with a schemaless design.

## databases

Service name | Service function
---|---
Azure Cosmos DB | Globally distributed database that supports NoSQL options.
Azure SQL Database | Fully managed relational database with auto-scale, integral intelligence, and robust security.
Azure Database for MySQL | Fully managed and scalable MySQL relational database with high availability and security.
Azure Database for PostgreSQL | Fully managed and scalable PostgreSQL relational database with high availability and security.
SQL Server on Azure Virtual Machines | Service that hosts enterprise SQL Server apps in the cloud.
Azure Synapse Analytics | Fully managed data warehouse with integral security at every level of scale at no extra cost.
Azure Database Migration Service | Service that migrates databases to the cloud with no application code changes.
Azure Cache for Redis | Fully managed service caches frequently used and static data to reduce data and application latency.
Azure Database for MariaDB | Fully managed and scalable MariaDB relational database with high availability and security.

## web

Service name | Service function
---|---
Azure App Service | Quickly create powerful cloud web-based apps.
Azure Notification Hubs | Send push notifications to any platform from any back end.
Azure API Management | Publish APIs to developers, partners, and employees securely and at scale.
Azure Cognitive Search | Deploy this fully managed search as a service.
Web Apps feature of Azure App Service | Create and deploy mission-critical web apps at scale.
Azure SignalR Service | Add real-time web functionalities easily.

## IoT

Service name | Service function
---|---
IoT Central | Fully managed global IoT software as a service (SaaS) solution that makes it easy to connect, monitor, and manage IoT assets at scale.
Azure IoT Hub | Messaging hub that provides secure communications between and monitoring of millions of IoT devices.
IoT Edge | Fully managed service that allows data analysis models to be pushed directly onto IoT devices, which allows them to react quickly to state changes without needing to consult cloud-based AI models.

## Big data

Data comes in all formats and sizes. \
When we talk about big data, we're referring to large volumes of data. \
Data from weather systems, communications systems, genomic research, imaging platforms, and many other scenarios generate hundreds of gigabytes of data. \
This amount of data makes it hard to analyze and make decisions. \
It's often so large that _traditional forms of processing and analysis are no longer appropriate_. \
Open-source **cluster** technologies have been developed to deal with these _large data sets_. \
Azure supports a broad range of technologies and services to provide big data and analytic solutions.

Service name | Description
---|---
Azure Synapse Analytics | Run *analytics* at a massive scale by using a cloud-based enterprise data warehouse that takes advantage of *massively parallel processing* to run complex queries quickly across petabytes of data.
Azure HDInsight | Process massive amounts of data with _managed clusters_ of `Hadoop` clusters in the cloud.
Azure Databricks | Integrate this collaborative Apache `Spark`-based analytics service with other big data services in Azure.

## AI

AI, in the context of cloud computing, is based around a broad range of services, the core of which is machine learning. \
Machine learning is a data science technique that allows computers to use existing data to forecast future behaviors, outcomes, and trends. \
Using machine learning, computers learn without being explicitly programmed.

Forecasts or predictions from machine learning can make apps and devices smarter. \
For example, when you shop online, machine learning helps recommend other products you might like based on what you've purchased. \
Or when your credit card is swiped, machine learning compares the transaction to a database of transactions and helps detect fraud. \
And when your robot vacuum cleaner vacuums a room, machine learning helps it decide whether the job is done.

Service name | Description
---|---
Azure Machine Learning Service | Cloud-based environment you can use to develop, train, test, deploy, manage, and track machine learning models. It can auto-generate a model and auto-tune it for you. It will let you start training on your local machine, and then scale out to the cloud.
Azure ML Studio | *Collaborative* visual workspace where you can build, test, and deploy machine learning solutions by using prebuilt machine learning algorithms and data-handling modules.

## Cognitive

A closely related set (to AI) of products are the cognitive services. \
You can use these prebuilt APIs in your applications to solve complex problems.

Service name | Description
---|---
Vision | Use *image-processing* algorithms to smartly identify, caption, index, and moderate your pictures and videos.
Speech | Convert spoken audio into text, use voice for verification, or add speaker recognition to your app.
Knowledge mapping | Map complex information and data to solve tasks such as intelligent recommendations and semantic search.
Bing Search | Add Bing Search APIs to your apps and harness the ability to comb billions of webpages, images, videos, and news with a single API call.
Natural Language processing | Allow your apps to process natural language with prebuilt scripts, evaluate sentiment, and learn how to recognize what users want.

## DevOps

DevOps brings together people, processes, and technology by automating software delivery to provide continuous value to your users. \
With Azure DevOps, you can create build and release pipelines that provide continuous integration, delivery, and deployment for your applications. \
You can integrate repositories and application tests, perform application monitoring, and work with build artifacts. \
You can also work with and backlog items for tracking, automate infrastructure deployment, and integrate a range of third-party tools and services such as Jenkins and Chef. \
All of these functions and many more are closely integrated with Azure to allow for consistent, repeatable deployments for your applications to provide streamlined build and release processes.

Service name | Description
---|---
Azure DevOps | Use development collaboration tools such as high-performance pipelines, free private Git repositories, configurable Kanban boards, and extensive automated and cloud-based load testing. Formerly known as Visual Studio Team Services.
Azure DevTest Labs | Quickly create on-demand Windows and Linux environments to test or demo applications directly from deployment pipelines.

[<< home](../az.md) | [< LP1 AZ900](./1-lp-az-900.md)