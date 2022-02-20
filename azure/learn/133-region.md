# Azure regions, availability zones, and region pairs

> https://docs.microsoft.com/en-us/learn/modules/azure-architecture-fundamentals/regions-availability-zones

Resources are created in regions, which are different geographical locations around the globe that contain Azure datacenters. \
Azure is made up of datacenters located around the globe. \
When you use a service or create a resource such as a SQL database or virtual machine (VM), you're using physical equipment in one or more of these locations. \
These specific datacenters aren't exposed to users directly. \
Instead, Azure organizes them into regions. \
As you'll see later in this unit, some of these regions offer availability zones, which are different Azure datacenters within that region.

## Azure regions

A region is a _geographical area_ on the planet that contains at least one but potentially multiple datacenters that are _nearby and networked together with a low-latency network_. \
Azure intelligently assigns and controls the resources within each region to ensure workloads are appropriately balanced. \
When you deploy a resource in Azure, you'll often need to choose the region where you want your resource deployed.

Some services or VM features are only available in certain regions, such as specific VM sizes or storage types. \
There are also some global Azure services that _don't require you to select a particular region_, such as Azure Active Directory, Azure Traffic Manager, and Azure DNS.

A few examples of regions are West US, Canada Central, West Europe, Australia East, and Japan West. \
Here's a view of all the available regions as of June 2020.

![Global map of available Azure regions as of June 2020.](https://docs.microsoft.com/en-us/learn/azure-fundamentals/azure-architecture-fundamentals/media/regions-small-be724495.png)

Azure has more global regions than any other cloud provider. \
These regions give you the flexibility to bring applications closer to your users no matter where they are. \
Global regions provide _better scalability_ and _redundancy_. \
They also preserve _data residency_ for your services.

### Special Azure regions

Azure has specialized regions that you might want to use when you build out your applications for compliance or legal purposes. \
A few examples include:
- US DoD Central, US Gov Virginia, US Gov Iowa and more \
These regions are physical and logical network-isolated instances of Azure for U.S. government agencies and partners. \
These datacenters are operated by screened U.S. personnel and include additional compliance certifications.
- China East, China North, and more \
These regions are available through a unique partnership between Microsoft and 21Vianet, whereby Microsoft doesn't directly maintain the datacenters. \
Regions are what you use to identify the location for your resources. \
There are two other terms you should also be aware of: **geographies** and availability zones.

## Availability zones

You want to ensure your services and data are **redundant** so you can protect your information in case of *failure*. \
When you host your infrastructure, setting up your own redundancy *requires that you create duplicate hardware environments*. \
Azure can help make your app highly available through availability zones.

Availability zones are **physically separate datacenters within an Azure region**. \
Each availability zone is made up of one or more datacenters equipped with **independent power, cooling, and networking**. \
An availability zone is set up to be an *isolation boundary*. \
If one zone goes down, the other continues working. \
Availability zones are *connected through high-speed*, **private fiber-optic networks**.

![Diagram showing three datacenters connected in a single Azure region representing an availability zone.](https://docs.microsoft.com/en-us/learn/azure-fundamentals/azure-architecture-fundamentals/media/availability-zones-5c3c490c.png)

Not every region has support for availability zones. \
For an updated list, see [Regions that support availability zones in Azure](https://docs.microsoft.com/en-us/azure/availability-zones/az-region).

You can use availability zones to run mission-critical applications and build high-availability into your application architecture \
by co-locating your compute, storage, networking, and data resources within a zone and replicating in other zones. \
Keep in mind that there could be a cost to duplicating your services and _transferring data between zones_.

Availability zones are **primarily for VMs, managed disks, load balancers, and SQL databases**. \
Azure services that support availability zones fall into three categories:
- **Zonal** services: You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
- **Zone-redundant** services: The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database).
- **Non-regional** services: Services are *always available* from Azure geographies and are *resilient to zone-wide outages* as well as region-wide outages.

## Region pairs

Availability zones are created by using one or more datacenters. \
There's a **minimum of three zones within a single region**. \
It's possible that a large disaster could cause an outage big enough to affect even two datacenters. \
_That's why Azure also creates region pairs_.

Each Azure region is always _paired with another region within the same geography_ (such as US, Europe, or Asia) at least 300 miles away. \
This approach _allows for the replication of resources_ (such as VM storage) across a geography that helps reduce the likelihood of interruptions \
because of events such as natural disasters, civil unrest, power outages, or physical network outages that affect both regions at once. \
If a region in a pair was affected by a natural disaster, for instance, services would **automatically failover** to the other region in its region pair. \
Examples of region pairs in Azure are West US paired with East US and SouthEast Asia paired with East Asia.

![Diagram showing relationship between geography, region pair, region, and datacenter.](https://docs.microsoft.com/en-us/learn/azure-fundamentals/azure-architecture-fundamentals/media/region-pairs-d9eb9728.png)

Because the pair of regions is directly connected and far enough apart to be isolated from regional disasters, \
you can use them to provide _reliable services_ and data redundancy. \
Some services offer automatic geo-redundant storage by using region pairs.

Additional advantages of region pairs:

- If an extensive Azure outage occurs, one region out of every pair is prioritized to make sure at least one is restored as quickly as possible for applications hosted in that region pair.
- Planned Azure updates are rolled out to paired regions one region at a time to minimize downtime and risk of application outage.
- Data continues to reside within the same geography as its pair (except for Brazil South) for tax- and law-enforcement jurisdiction purposes.

Having a broadly distributed set of datacenters allows Azure to provide a high guarantee of availability.

- [Azure geographies](https://azure.microsoft.com/en-us/global-infrastructure/geographies/#geographies)
- [Azure cross-region replication pairings for all geographies](https://docs.microsoft.com/en-us/azure/availability-zones/cross-region-replication-azure)



[<< home](../az.md) | [< LP1 AZ900](./1-lp-az-900.md)