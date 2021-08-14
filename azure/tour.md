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

**TODO:** big data and ai

[< back](./az.md)