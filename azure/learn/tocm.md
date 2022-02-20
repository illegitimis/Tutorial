# What are public, private, and hybrid clouds?

Deployment model | Description | comparison
---|---|---
Public cloud | Services are offered over the _public internet_ and available to anyone who wants to purchase them. Cloud resources, such as servers and storage, are owned and operated by a third-party cloud service provider, and delivered over the internet. | No capital expenditures to scale up. Applications can be quickly provisioned and deprovisioned. Organizations pay only for what they use.
Private cloud | A private cloud consists of computing resources used exclusively by users from one business or organization. A private cloud can be physically located at your organization's on-site (on-premises) datacenter, or it can be hosted by a third-party service provider. | Hardware must be purchased for start-up and maintenance. Organizations have complete control over resources and security. Organizations are responsible for hardware maintenance and updates.
Hybrid cloud | A hybrid cloud is a computing environment that combines a public cloud and a private cloud by allowing data and applications to be shared between them. | Provides the most flexibility. Organizations determine where to run their applications. Organizations control security, compliance, or legal requirements

category \ Deployment Model | Public | Hybrid | Private
---|---|---|---
Services offered | public internet | integration is generally through a secure VPN between cloud providers like Azure and on-premises datacenters | network infrastructure that the business owns and maintains
Availabilty | anyone who wants to purchase |  | computing resources used exclusively by users from one business or organization
Ownership | 3rd party CSP | resources they temporarily use publicly vs owned and needing maintenance | on prem / csp
Price | free/on-demand | manage which resources are local versus resources in the cloud | hardware

## Why public cloud?

Public clouds can be deployed faster than on-premises infrastructures and with an almost infinitely scalable platform. \
Every employee of a company can use the same application from any office or branch using their device of choice as long as they can access the internet.

Examples of why you would use public cloud:

**Service consumption through on-demand or subscription model** \
The on-demand or subscription model allows you to pay for the portion of CPU, storage, and other resources that you use or reserve. \
**No up-front investment of hardware** \
No requirement to purchase, manage, and maintain on-premises hardware and application infrastructure. \
The cloud service provider is held responsible for all management and maintenance of the system. \
**Automation** \
Quickly provision infrastructure resources using a web portal, scripts, or via automation. \
**Geographic dispersity** \
Store data near your users, or in desired locations without having to maintain your own datacenters. \
Reduced hardware maintenance: The service provider is responsible for hardware maintenance.

## Why private cloud?

A private cloud can provide more flexibility to an organization. \
Your organization can customize its cloud environment to meet specific business needs. \
Since resources are not shared with others, high levels of control and security are possible. \
Also, private clouds can provide a level of scalability and efficiency.

Examples of why you would use private cloud:

**Pre-existing environment** \
An existing operating environment that can't be replicated in the public cloud.\
A large investment in hardware and employees with solution expertise. \
A large organization may choose to commoditize their computing resources.\
**Legacy applications**\
Business-critical legacy applications that can't easily be physically relocated.\
**Data sovereignty and security**\
Political borders and legal requirements may dictate where data can physically exist.\
**Regulatory compliance** / certification\
PCI or HIPAA compliance. Certified on-premises datacenter.

## Why hybrid cloud?

Hybrid cloud allows your organization to control and maintain a private infrastructure for sensitive assets. \
It also gives you the flexibility to take advantage of additional resources in the public cloud when you need them.\
With the ability to scale to the public cloud, you pay for extra computing power only when needed. \
It can also ease transitioning to the cloud. You can migrate gradually by phasing in workloads over time.

Examples of why you would use hybrid cloud:

**Existing hardware investment**\
Business reasons require that you use an existing operating environment and hardware.\
**Regulatory requirements**\
Regulation requires that the data needs to remain at a physical location.\
**Unique operating environment**\
Public cloud can't replicate a legacy operating environment.\
Migration: Move workloads to the cloud over time.

[< az home](../az.md) | [LP1 AZ900](./1-lp-az-900.md)

