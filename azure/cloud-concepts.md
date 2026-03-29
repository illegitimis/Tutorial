# Cloud Concepts

## Tour of Azure Services

Azure provides a broad range of cloud services across multiple categories. The following
tables summarize the major service families.

### Compute

Service | Function
---|---
Azure Virtual Machines | Windows or Linux virtual machines hosted in Azure.
Azure Virtual Machine Scale Sets | Scaling for Windows or Linux VMs hosted in Azure.
Azure Kubernetes Service | Cluster management for VMs that run containerized services.
Azure Service Fabric | Distributed systems platform that runs in Azure or on-premises.
Azure Batch | Managed service for parallel and high-performance computing applications.
Azure Container Instances | Containerized apps run on Azure without provisioning servers or VMs.
Azure Functions | An event-driven, serverless compute service.

### Networking

Service | Function
---|---
Azure Virtual Network | Connects VMs to incoming **VPN** connections.
Azure Load Balancer | Balances inbound and outbound connections to applications or service endpoints.
Azure Application Gateway | Optimizes app server farm delivery while increasing application security.
Azure VPN Gateway | Accesses Azure Virtual Networks through high-performance VPN gateways.
Azure DNS | Provides ultra-fast DNS responses and ultra-high domain availability.
Azure Content Delivery Network | Delivers high-bandwidth content to customers globally.
Azure DDoS Protection | Protects Azure-hosted applications from **DDoS** attacks.
Azure Traffic Manager | Distributes network traffic across Azure regions worldwide.
Azure ExpressRoute | Connects to Azure over high-bandwidth dedicated secure connections.
Azure Network Watcher | Monitors and diagnoses network issues by using scenario-based analysis.
Azure Firewall | Implements high-security, high-availability firewall with unlimited scalability.
Azure Virtual WAN | Creates a unified wide area network (WAN) that connects local and remote sites.

### Storage

Service | Function
---|---
Azure `Blob` Storage | Storage service for very large objects, such as video files or bitmaps.
Azure `File` Storage | File shares that can be accessed and managed like a file server.
Azure `Queue` Storage | Data store for queuing and reliably delivering messages between applications.
Azure `Table` Storage | Stores non-relational structured data (structured NoSQL) in the cloud, providing a _key/attribute_ store with a schemaless design.

### Databases

Service | Function
---|---
Azure Cosmos DB | Globally distributed database that supports NoSQL options.
Azure SQL Database | Fully managed relational database with auto-scale, integral intelligence, and robust security.
Azure Database for MySQL | Fully managed and scalable MySQL relational database with high availability and security.
Azure Database for PostgreSQL | Fully managed and scalable PostgreSQL relational database with high availability and security.
SQL Server on Azure Virtual Machines | Hosts enterprise SQL Server apps in the cloud.
Azure Synapse Analytics | Fully managed data warehouse with integral security at every level of scale at no extra cost.
Azure Database Migration Service | Migrates databases to the cloud with no application code changes.
Azure Cache for Redis | Fully managed service that caches frequently used and static data to reduce data and application latency.
Azure Database for MariaDB | Fully managed and scalable MariaDB relational database with high availability and security.

### Web

Service | Function
---|---
Azure App Service | Quickly create powerful cloud web-based apps.
Azure Notification Hubs | Send push notifications to any platform from any back end.
Azure API Management | Publish APIs to developers, partners, and employees securely and at scale.
Azure Cognitive Search | Deploy this fully managed search as a service.
Web Apps feature of Azure App Service | Create and deploy mission-critical web apps at scale.
Azure SignalR Service | Add real-time web functionalities easily.

### IoT

Service | Function
---|---
IoT Central | Fully managed global IoT SaaS solution that makes it easy to connect, monitor, and manage IoT assets at scale.
Azure IoT Hub | Messaging hub that provides secure communications between and monitoring of millions of IoT devices.
IoT Edge | Fully managed service that allows data analysis models to be pushed directly onto IoT devices.

### Big Data

Azure supports a broad range of technologies and services to provide big data and analytic solutions. Open-source **cluster** technologies have been developed to deal with large data sets where _traditional forms of processing and analysis are no longer appropriate_.

Service | Function
---|---
Azure Synapse Analytics | Cloud-based enterprise data warehouse that uses _massively parallel processing_ to run complex queries quickly across petabytes of data.
Azure HDInsight | Process massive amounts of data with managed clusters of `Hadoop` in the cloud.
Azure Databricks | Collaborative Apache `Spark`-based analytics service that integrates with other big data services in Azure.

### AI and Cognitive Services

Service | Function
---|---
Azure Machine Learning Service | Cloud-based environment to develop, train, test, deploy, manage, and track machine learning models. Can auto-generate and auto-tune models.
Azure ML Studio | _Collaborative_ visual workspace where you can build, test, and deploy machine learning solutions by using prebuilt algorithms and data-handling modules.

Cognitive Services provide prebuilt APIs for solving complex problems:

Service | Function
---|---
Vision | Image-processing algorithms to identify, caption, index, and moderate pictures and videos.
Speech | Convert spoken audio into text, use voice for verification, or add speaker recognition.
Knowledge mapping | Map complex information and data for intelligent recommendations and semantic search.
Bing Search | Comb billions of webpages, images, videos, and news with a single API call.
Natural Language Processing | Process natural language with prebuilt scripts, evaluate sentiment, and recognize user intent.

### DevOps

Service | Function
---|---
Azure DevOps | Development collaboration tools including high-performance pipelines, free private Git repositories, configurable Kanban boards, and extensive automated and cloud-based load testing.
Azure DevTest Labs | Quickly create on-demand Windows and Linux environments to test or demo applications directly from deployment pipelines.

## Azure Accounts and Subscriptions

Azure organizes resources into a hierarchy of management scopes:

Scope | Description
---|---
Resources | Instances of services that you create, like virtual machines, storage, or SQL databases.
Resource groups | Logical containers into which Azure resources like web apps, databases, and storage accounts are deployed and managed.
Subscriptions | Groups together user accounts and the resources created by those accounts. Each subscription has limits or quotas on the amount of resources you can create and use. Organizations use subscriptions to manage costs.
Management groups | Help you manage access, policy, and compliance for multiple subscriptions. All subscriptions in a management group automatically inherit the conditions applied to the management group.

A subscription is a **logical unit of Azure services** that links to an Azure account, which is an identity in Azure Active Directory. An account can have multiple subscriptions with different billing models and access-management policies.

There are two types of subscription boundaries:

- **Billing boundary** -- determines how an Azure account is billed. You can create multiple subscriptions for different billing requirements with separate billing reports and invoices.
- **Access control boundary** -- Azure applies access-management policies at the subscription level. You can create separate subscriptions to reflect different organizational structures.

### Management Groups

Management groups provide a level of scope above subscriptions. You organize subscriptions into containers called management groups and apply governance conditions to them. Key facts:

- 10,000 management groups can be supported in a single directory
- A management group tree can support up to six levels of depth (excluding root and subscription levels)
- Each management group and subscription can support only one parent
- Each management group can have many children

## Cloud Models

Deployment Model | Description | Comparison
---|---|---
Public cloud | Services offered over the public internet, available to anyone who wants to purchase them. Cloud resources are owned and operated by a third-party cloud service provider. | No capital expenditures to scale up. Applications can be quickly provisioned and deprovisioned. Pay only for what you use.
Private cloud | Computing resources used exclusively by users from one business or organization. Can be physically on-premises or hosted by a third-party service provider. | Hardware must be purchased for start-up and maintenance. Complete control over resources and security. Responsible for hardware maintenance and updates.
Hybrid cloud | Combines a public cloud and a private cloud by allowing data and applications to be shared between them. | Provides the most flexibility. Organizations determine where to run applications and control security, compliance, or legal requirements.

### Why Public Cloud

Public clouds can be deployed faster than on-premises infrastructures and with an almost infinitely scalable platform. Benefits include:

- **Service consumption through on-demand or subscription model** -- pay for the portion of CPU, storage, and other resources that you use or reserve
- **No up-front investment of hardware** -- the cloud service provider handles all management and maintenance
- **Automation** -- quickly provision infrastructure resources using a web portal, scripts, or automation
- **Geographic dispersity** -- store data near your users or in desired locations without maintaining your own datacenters

### Why Private Cloud

A private cloud can provide more flexibility. Your organization can customize its cloud environment to meet specific business needs with high levels of control and security. Use cases include:

- **Pre-existing environment** that cannot be replicated in the public cloud
- **Legacy applications** that cannot be easily relocated
- **Data sovereignty and security** where political borders and legal requirements dictate where data can physically exist
- **Regulatory compliance** such as PCI or HIPAA

### Why Hybrid Cloud

Hybrid cloud allows your organization to control and maintain a private infrastructure for sensitive assets while taking advantage of additional resources in the public cloud when needed. Use cases include:

- **Existing hardware investment** requiring continued use of an existing operating environment
- **Regulatory requirements** that data remain at a physical location
- **Unique operating environment** that public cloud cannot replicate
- Gradual migration of workloads to the cloud over time

## Service Models

Model | Definition | Description
---|---|---
IaaS | **Infrastructure-as-a-Service** | Closest to managing physical servers. The cloud provider keeps the hardware up-to-date, but operating system maintenance and network configuration is up to the cloud tenant. Setting up a new virtual machine is considerably faster than procuring, installing, and configuring a physical server.
PaaS | **Platform-as-a-Service** | A managed hosting environment. The cloud provider manages the virtual machines and networking resources. The cloud tenant deploys their applications into the managed hosting environment.
SaaS | **Software-as-a-Service** | The cloud provider manages all aspects of the application environment, such as virtual machines, networking resources, data storage, and applications. The cloud tenant only needs to provide their data.

### Service Model Comparison

Aspect | IaaS | PaaS | SaaS
---|---|---|---
Flexibility | Most flexible; you control the hardware | Focus on application development | Pay-as-you-go pricing model
Management | User manages provisioned services; provider manages cloud infrastructure | Platform management handled by cloud provider | Users pay for software on a subscription model
No CapEx | No up-front costs | No up-front costs | No up-front costs
Agility | Applications accessible quickly, deprovisioned when needed | More agile than IaaS; no server configuration needed | Provide staff with latest software quickly
Skills | No deep technical skills required to deploy | No deep technical skills required | No deep technical skills required

**Serverless computing** is like PaaS in that it enables developers to build applications faster by eliminating the need for them to manage infrastructure. With serverless applications, the cloud service provider automatically provisions, scales, and manages the infrastructure required to run the code. Serverless architectures are highly scalable and event-driven, only using resources when a specific function or trigger occurs.

## Regions and Availability Zones

### Azure Regions

A region is a _geographical area_ on the planet that contains at least one but potentially multiple datacenters that are nearby and networked together with a _low-latency network_. Azure intelligently assigns and controls the resources within each region to ensure workloads are appropriately balanced.

Some services or VM features are only available in certain regions. There are also some global Azure services that do not require you to select a particular region, such as Azure Active Directory, Azure Traffic Manager, and Azure DNS.

Azure has specialized regions for compliance or legal purposes, including:

- **US DoD Central, US Gov Virginia, US Gov Iowa** -- physical and logical network-isolated instances for U.S. government agencies and partners, operated by screened U.S. personnel
- **China East, China North** -- available through a unique partnership between Microsoft and 21Vianet

### Availability Zones

Availability zones are **physically separate datacenters within an Azure region**. Each availability zone is made up of one or more datacenters equipped with **independent power, cooling, and networking**. They are connected through high-speed, private fiber-optic networks.

Availability zones are primarily for VMs, managed disks, load balancers, and SQL databases. Azure services that support availability zones fall into three categories:

- **Zonal** services -- resource pinned to a specific zone (e.g., VMs, managed disks, IP addresses)
- **Zone-redundant** services -- platform replicates automatically across zones (e.g., zone-redundant storage, SQL Database)
- **Non-regional** services -- always available from Azure geographies and resilient to zone-wide and region-wide outages

### Region Pairs

Each Azure region is always paired with another region within the same geography at least 300 miles away. This allows for the replication of resources across a geography to help reduce the likelihood of interruptions from events such as natural disasters, civil unrest, power outages, or physical network outages. If a region in a pair is affected by a natural disaster, services would **automatically failover** to the other region.

Additional advantages of region pairs:

- If an extensive Azure outage occurs, one region out of every pair is prioritized for restoration
- Planned Azure updates are rolled out to paired regions one region at a time to minimize downtime
- Data continues to reside within the same geography as its pair (except for Brazil South) for tax- and law-enforcement jurisdiction purposes

## Knowledge Check

1. Q: True or false -- you need to purchase an Azure account before you can use any Azure resources.
   A: **False**. You can use a free Azure account or a Microsoft Learn sandbox to create resources.

2. Q: What is meant by cloud computing?
   A: Delivery of computing services over the internet.

3. Q: Which of the following is not a feature of cloud computing?
   A: A limited pool of services. The cloud offers a nearly limitless pool of raw compute, storage, and networking components.

4. Q: Which of the following choices is not a cloud computing category?
   A: **Networking-as-a-Service** (NaaS) is not a cloud computing category.

5. Q: With Operating Expenses (OpEx), what are you responsible for?
   A: With OpEx, you are only responsible for the computing resources that you use.

6. Q: Which of the following options is not a type of cloud computing?
   A: Distributed cloud is not a type of cloud computing.

7. Q: Which of the following choices is not a benefit of using cloud services?
   A: Geographic isolation. One of the primary advantages of cloud computing is geographic distribution.

8. Q: Which cloud deployment model is best for a short-term SQL server database project that needs quick deployment?
   A: **Public cloud**. The need for quick deployment and short lifecycle makes public cloud the best option.

9. Q: You create VMs in the cloud with access to cloud storage and a VPN connecting to your on-premises datacenter. What deployment model is this?
   A: **Hybrid cloud**. This scenario uses both public and private cloud with a connection between them.

10. Q: Two datacenters connected by a VPN, where one datacenter has regulatory-required data. What deployment model?
    A: **Private cloud**. The VPN is a public cloud resource, but because it is a private connection between two private datacenters, this is a private cloud deployment.

11. Q: Which can be used to manage governance across multiple Azure subscriptions?
    A: **Management groups**. They facilitate the hierarchical ordering of Azure resources at a level of scope above subscriptions.

12. Q: Which is a logical unit of Azure services that links to an Azure account?
    A: **Azure subscription**.

13. Q: Which feature does not apply to resource groups?
    A: Resource groups **cannot be nested**.

14. Q: Which is a valid statement about an Azure subscription?
    A: An Azure subscription is a logical unit of Azure services, bundled together for tracking and billing purposes.

[<<](./index.md) | [home](../README.md)

[1]: https://docs.microsoft.com/en-us/learn/paths/az-900-describe-cloud-concepts/
[2]: https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-fundamentals/tour-of-azure-services
[3]: https://docs.microsoft.com/en-us/learn/modules/azure-architecture-fundamentals/regions-availability-zones
[4]: https://azure.microsoft.com/en-us/global-infrastructure/geographies/#geographies
[5]: https://docs.microsoft.com/en-us/azure/availability-zones/cross-region-replication-azure