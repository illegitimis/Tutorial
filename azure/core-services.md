# Core Azure Services

## Compute Services

Azure compute is an on-demand computing service for running cloud-based applications. It provides computing resources such as disks, processors, memory, networking, and operating systems. Resources are available on-demand and can typically be made available in minutes or even seconds.

Virtual Machine Scale Sets let you deploy and manage a set of identical virtual machines. With all VMs configured the same, scale sets support true autoscale with no pre-provisioning of VMs required.

Azure Virtual Desktop enables team members to run Windows in the cloud, with access to the required applications from various operating systems like macOS, Linux, and Windows.

Azure Functions is used when you need to perform work in response to an event (often via a REST request), timer, or message from another Azure service, and when that work can be completed quickly, within seconds or less.

## Networking Services

Azure provides core networking resources for connecting your cloud and on-premises environments.

### Virtual Network Settings

You can create and configure Azure Virtual Network instances from the Azure portal, Azure PowerShell, or Azure Cloud Shell. When you create a virtual network, you configure basic settings and can add advanced settings such as multiple subnets, DDoS protection, and service endpoints.

Key configuration elements:

- **Network name** -- must be unique in your subscription but does not need to be globally unique
- **Address space** -- defined in **CIDR** format; must be unique within your subscription and any connected networks
- **Subnets** -- partition the virtual network's address space; routing between subnets depends on default traffic routes or custom routes
- **DDoS protection** -- Basic or Standard tier (Standard is a premium service)
- **Service endpoints** -- enable connections to Azure Cosmos DB, Azure Service Bus, Azure Key Vault, and more

After creation, you can also configure network security groups, route tables, peerings, and connected devices.

### VPN Gateway Fundamentals

VPNs use an encrypted tunnel within another network, typically deployed to connect two or more trusted private networks over an untrusted network (the public internet).

A VPN gateway is a type of virtual network gateway deployed in Azure Virtual Network instances that enables:

- **Site-to-site** connections from on-premises datacenters to virtual networks
- **Point-to-site** connections from individual devices to virtual networks
- **Network-to-network** connections between virtual networks

When deploying a VPN gateway, you specify the VPN type:

- **Policy-based** -- statically specify IP addresses of packets that should be encrypted through each tunnel; supports IKEv1 only with static routing
- **Route-based** -- IPSec tunnels modeled as a network interface; IP routing decides which tunnel interface to use; preferred for on-premises devices and more resilient to topology changes

VPN Gateway SKU | Max Tunnels | Throughput | BGP Support
---|---|---|---
Basic | 10 | 100 Mbps | Not supported
VpnGw1/Az | 30 | 650 Mbps | Supported
VpnGw2/Az | 30 | 1 Gbps | Supported
VpnGw3/Az | 30 | 1.25 Gbps | Supported

High-availability options include active/standby (default), active/active with BGP, ExpressRoute failover, and zone-redundant gateways.

### ExpressRoute

Azure ExpressRoute provides high-bandwidth dedicated secure connections that do not traverse the public internet. It provides private connectivity but is not encrypted by default.

Virtual network peering can be used to link virtual networks together.

## Storage Services

Azure Storage provides several storage options for different use cases:

- **Azure Blob Storage** -- storage for very large objects such as video files or bitmaps. Best option for storing disaster recovery files and archives.
- **Azure Disk Storage** -- provides disks for Azure Virtual Machines
- **Azure Files Storage** -- file shares that can be accessed and managed like a file server

The first step to sharing data as a blob in Azure Storage is to create an Azure Storage account before you can use any Azure Storage features.

## Database Services

Azure offers a range of fully managed database services:

Service | Best For
---|---
Azure Cosmos DB | Graph-based applications using the `Gremlin` API, and globally distributed NoSQL workloads. Supports SQL, MongoDB, Cassandra, Tables, and Gremlin APIs.
Azure SQL Database | Enterprise relational database workloads with auto-scale and intelligent performance
Azure Database for MySQL | LAMP stack applications and MySQL workloads
Azure Database for PostgreSQL | PostgreSQL relational database workloads
Azure Synapse Analytics | Analyzing large volumes of data (millions of log entries)
Azure Database for MariaDB | MariaDB relational database workloads

Azure SQL Database and Azure SQL Managed Instance provide a [features comparison][1] for understanding the differences between the two services.

## Knowledge Check

1. Q: Which Azure compute resource can be deployed to manage a set of identical virtual machines?
   A: **Virtual Machine Scale Sets**. They let you deploy and manage a set of identical virtual machines.

2. Q: Which service should be used to perform work in response to an event that needs a response in a few seconds?
   A: **Azure Functions**. It is used when you need to perform work in response to an event, often via a REST request, timer, or message from another Azure service.

3. Q: Your team members use various operating systems and need to use Windows-based software. Which compute service helps?
   A: **Azure Virtual Desktop**. It enables team members to run Windows in the cloud, with access to required applications.

4. Q: Which technology cannot be used to create a secure communication tunnel between branch offices?
   A: **Implicit FTP over SSL**. FTP over SSL cannot be used to create a secure communication tunnel.

5. Q: Which is not an ExpressRoute model?
   A: **Site-to-site virtual private network** is not an ExpressRoute model.

6. Q: Which option can you use to link virtual networks?
   A: **Virtual network peering**.

7. Q: Which option is not a benefit of ExpressRoute?
   A: **Encrypted network communication**. ExpressRoute provides private connectivity but it is not encrypted.

8. Q: What is the first step to share an image file as a blob in Azure Storage?
   A: **Create an Azure Storage account**. You must create a Storage account before you can use any Azure Storage features.

9. Q: Which Azure Storage option is better for backup and restore, disaster recovery, and archiving?
   A: **Azure Blob Storage**.

10. Q: Your development team wants to write Graph-based applications using the Gremlin API. Which service?
    A: **Azure Cosmos DB**. It supports SQL, MongoDB, Cassandra, Tables, and Gremlin APIs.

11. Q: Tailwind Traders uses the LAMP stack for several of its websites. Which option is ideal for migration?
    A: **Azure Database for MySQL**.

12. Q: Tailwind Traders has millions of log entries to analyze. Which option is ideal?
    A: **Azure Synapse Analytics**.

[<<](./index.md) | [home](../README.md)

[1]: https://docs.microsoft.com/en-us/azure/azure-sql/database/features-comparison
[2]: https://docs.microsoft.com/en-us/learn/paths/az-900-describe-core-azure-services/