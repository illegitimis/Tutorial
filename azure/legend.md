# legend

> glossary

## AAS

as a service

## ACI

azure container instances

## ACR

Azure Container Registry. \
ACR is a service that keeps track of current valid container images. \
It manages files and artifacts for containers. \
When your Azure container instances and Kubernetes service need to create a new container, the images come from ACR.

## ADFS

Active Directory Federation Services

## AHB

Azure Hybrid Benefit

## AKS

Azure Kubernetes Service. simplest deployment of a managed Kubernetes cluster in Azure.

## Application Gateway

Build secure, scalable, highly available web front ends in Azure \
load balancing? \
[documentation](https://docs.microsoft.com/en-us/azure/application-gateway/), [home](https://azure.microsoft.com/en-us/services/application-gateway/#overview) 

## App Service

`App Service` is an HTTP-based service that enables you to build and host many types of web-based solutions without managing infrastructure. For example, you can host web apps, mobile back ends, and RESTful APIs in several supported programming languages. Applications developed in .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python can run in and scale with ease on both Windows-based and Linux-based environments.

## APM

Application Performance Management

## ARM

Azure Resource Manager templates

## ARS

atom-record-sequence format

## Availability zones

- physically separate datacenters within an Azure region.
- Each availability zone is made up of one or more datacenters equipped with independent power, cooling, and networking.
- An availability zone is set up to be an isolation boundary.
- If one zone goes down, the other continues working.
- Availability zones are connected through high-speed, private fiber-optic networks.

## BGP

*Border Gateway Protocol* works with Azure VPN gateways or ExpressRoute to propagate on-premises BGP routes to Azure virtual networks.

## Blueprints

Enabling quick, repeatable creation of governed environments [*](https://azure.microsoft.com/en-us/services/blueprints/#overview)

## CapEx

- Capital Expenditure
- is the up-front spending of money on physical infrastructure, and then deducting that up-front expense over time.
- The up-front cost from CapEx has a value that reduces over time.

## CCM 

Cloud Controls Matrix

## CEF

Common Event Format

## CDN

Content Delivery Network

## CIAM

customer identity access management

## CJIS

FBI's Criminal Justice Information Services

## COGS

cost of goods sold

## Compute

https://azure.microsoft.com/en-gb/product-categories/compute/

## CSA

Cloud Security Alliance

## CSF

Cybersecurity Framework

## CSP

Cloud Solution Provider

## CSV

Cluster Shared Volumes

##  DDoS Protection

protect your Azure resources from distributed denial of service attacks.

## Dedicated Host

 [Azure Dedicated Host]() provides _dedicated_ physical servers to host your Azure VMs for Windows and Linux. Default hardware shared, workloads isolated. A dedicated host is mapped to a physical server in an Azure datacenter. A *host group* is a collection of dedicated hosts.

 ![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/protect-against-security-threats-azure/media/6-dedicated-hosts-cab8e670.png)

You're charged per dedicated host, independent of how many VMs you deploy to it [*](https://docs.microsoft.com/en-us/learn/modules/protect-against-security-threats-azure/6-host-virtual-machines-dedicated-hosts).

## DFS

- Distributed File System
- desktop file sync :(

## DIB

Defense Industrial Base

## DMZ

perimeter network

## DoD

Department of Defense

## DPA

Data Protection Addendum

## ExpressRoute

- greater bandwidth and even higher levels of security
- dedicated private connectivity to Azure that doesn't travel over the internet

## EAI

enterprise application integration

## fabric controller

- data center racks of servers
- each server has a hypervisor to run multiple VMs
- a network switch provides connectivity to all of those servers
- one server in each rack runs a special piece of software called `fabric controller`
- `orchestrator` manages links to all fabric controllers, user requests

## FedRAMP

Federal Risk and Authorization Management Program

## Firewall 

control what traffic is allowed on the network.

## FQDN

fully qualified domain names

## front door

Fast, reliable, and more secure cloud content delivery service with intelligent threat protection.

## FRS

File Replication Service

## FSLogix

[docs](https://docs.microsoft.com/en-us/fslogix/overview)

## functions

https://docs.microsoft.com/en-us/azure/azure-functions/

## GA

general availability

## GRS

Geo-redundant storage

## HCI

???

## HITRUST

Health Information Trust Alliance

## hypervisor

- abstraction layer OS talks to hardware
- emulates all functions of a computer and its CPU in a virtual machine

## IAM

Access control pane in portal

## IRS

Internal Revenue Service

## ITAR

International Traffic in Arms Regulations

## KPI

key performance indicator

## LAMP

stack (Linux, Apache, MySQL, PHP)

## LOB

line of business

## Logic Apps

makes it easy to create a workflow across well-known services with less effort than writing code and manually orchestrating all the steps yourself.

## LUIS

Language Understanding

## Marketplace

- `Azure Marketplace` is an online store that hosts applications that are certified and optimized to run in Azure.
- Many types of applications are available, ranging from AI and machine learning to web applications.
- deployments from the store are done via the Azure portal by using a wizard-style user interface.

## MCU

micro controller unit

## Monitor Workbooks 

[Azure Monitor Workbooks](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/workbooks-overview/) automates responses to threats.

## MTCS

Multi-Tier Cloud Security Certification Body

## NIST

National Institute of Standards and Technology

## NSG

network security group

## NVA

Network Virtual Appliance

## OIDC

OpenID Connect

## OpEx

- Operational Expenditure
- is spending money on services or products now, and being billed for them now.
- You can deduct this expense in the same year you spend it.
- There is no up-front cost, as you pay for a service or product as you use it.

## OSI

layers:

1. Physical
2. Data link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

## OST

Online Services Terms

## PAYG

pay-as-you-go

## PCI DSS

Payment Card Industry's Data Security Standard

## Policy

Achieve real-time cloud compliance at scale with consistent resource governance [*](https://azure.microsoft.com/en-us/services/azure-policy/#overview)

## RBAC

role based access control

## RCA

root cause analysis

## RDVH

remote desktop virtualization host

## redundancy

duplicate components across several regions => ensure high availability

## Resource group

- A container that holds related resources for an Azure solution.
- The resource group includes resources that you want to manage as a group.
- You decide which resources belong in a resource group based on what makes the most sense for your organization.
- A resource group is a _logical container_ for resources deployed on Azure.
- These resources are anything you create in an Azure subscription like VMs, Azure Application Gateway instances, and Azure Cosmos DB instances.
- All resources must be in a resource group, and a resource can only be a member of a single resource group.
- Many resources can be moved between resource groups with some services having specific limitations or requirements to move.
- Resource groups _can't be nested_.
- Before any resource can be provisioned, you need a resource group for it to be placed in.
- If you delete a resource group, all resources contained within it are also deleted

## RUS

Request Units per second

## SAML

???

## SAN

storage area network

## SAS

Shared Access Signature

## Security Center

monitoring [service](https://azure.microsoft.com/services/security-center) that provides visibility of your security posture across all of your services, both on Azure and on-premises.

## Secure score

measurement of an organization's security posture [*](https://docs.microsoft.com/en-us/azure/security-center/secure-score-security-controls/)

## Sentinel

[Azure Sentinel](https://azure.microsoft.com/en-us/services/microsoft-sentinel/#overview) is Microsoft's cloud-based SIEM system. \
It uses intelligent security analytics and threat analysis.

## Serverless computing

- **the abstraction of servers, infrastructure, and operating systems.**
- Azure takes care of managing the server infrastructure and the allocation and deallocation of resources based on demand.
- Infrastructure isn't your responsibility.
- Scaling and performance are handled automatically.
- You're billed only for the exact resources you use.
- There's no need to even reserve capacity.
- Azure Cosmos DB serverless [*](https://docs.microsoft.com/en-us/azure/cosmos-db/serverless)

## SIEM

security information and event management

## Sku

Represents a purchasable *Stock Keeping Unit* (SKU) under a product. These represent the different shapes of the product.

## SLA

service level agreement, uptime, availability

## SLO

Service Level Objective

## SMB

Server Message Block

## SOC

Service Organization Controls

## TCO

Total Cost of Ownership

## UDR

user-defined Routing. \
significant update to Azure’s Virtual Networks as this allows network admins to control the routing tables between subnets within a VNet, \
as well as between VNets, thereby allowing for greater control over network traffic flow.

## VHD

virtual hard disk

## Virtual Desktop

https://docs.microsoft.com/en-us/azure/virtual-desktop/

## Virtual machines

https://docs.microsoft.com/en-us/azure/virtual-machines/

## Virtual machine scale sets

let you deploy and manage a set of **identical** virtual machines.

## Virtual Network (Azure)

- Isolation and segmentation (named subnet)
- Internet communications (For VM management, you can connect via the Azure CLI, Remote Desktop Protocol, or Secure Shell.)
- Communicate between Azure resources
- Communicate with on-premises resources
- Route network traffic
- Filter network traffic
- Connect virtual networks

## VPN Gateway (Azure)

## WAF

web application firewall

## zone

geographical grouping of Azure regions for billing purposes

[< back](./az.md)
