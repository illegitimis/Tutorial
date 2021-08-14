# legend

> glossary

## AAS

as a service

## App Service

`App Service` is an HTTP-based service that enables you to build and host many types of web-based solutions without managing infrastructure. For example, you can host web apps, mobile back ends, and RESTful APIs in several supported programming languages. Applications developed in .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python can run in and scale with ease on both Windows-based and Linux-based environments.

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

## Azure Marketplace

- `Azure Marketplace` is an online store that hosts applications that are certified and optimized to run in Azure.
- Many types of applications are available, ranging from AI and machine learning to web applications.
- deployments from the store are done via the Azure portal by using a wizard-style user interface.

## BGP

*Border Gateway Protocol* works with Azure VPN gateways or ExpressRoute to propagate on-premises BGP routes to Azure virtual networks.

## CapEx

- Capital Expenditure
- is the up-front spending of money on physical infrastructure, and then deducting that up-front expense over time.
- The up-front cost from CapEx has a value that reduces over time.

## CEF

Common Event Format

## Compute

https://azure.microsoft.com/en-gb/product-categories/compute/

## CSV

Cluster Shared Volumes

## DFS

- Distributed File System
- desktop file sync :(

## DMZ

perimeter network

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

## FRS

File Replication Service

## FSLogix

[docs](https://docs.microsoft.com/en-us/fslogix/overview)

## functions

https://docs.microsoft.com/en-us/azure/azure-functions/

## HCI

???

## hypervisor

- abstraction layer OS talks to hardware
- emulates all functions of a computer and its CPU in a virtual machine

## KPI

key performance indicator

## LUIS

Language Understanding

## MCU

micro controller unit

## NSG

network security group

## NVA

Network Virtual Appliance

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

## PCI DSS

Payment Card Industry's Data Security Standard

## RBAC

role based access control

## RCA

root cause analysis

## RDVH

remote desktop virtualization host

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

## SAS

Shared Access Signature

## Serverless computing

- **the abstraction of servers, infrastructure, and operating systems.**
- Azure takes care of managing the server infrastructure and the allocation and deallocation of resources based on demand.
- Infrastructure isn't your responsibility.
- Scaling and performance are handled automatically.
- You're billed only for the exact resources you use.
- There's no need to even reserve capacity.

## SIEM

security information and event management

## Sku

Represents a purchasable *Stock Keeping Unit* (SKU) under a product. These represent the different shapes of the product.

## TCO

Total Cost of Ownership

## UDR

user-defined Routing. significant update to Azure’s Virtual Networks as this allows network admins to control the routing tables between subnets within a VNet, as well as between VNets, thereby allowing for greater control over network traffic flow.

## VHD

virtual hard disk

## Virtual Desktop

https://docs.microsoft.com/en-us/azure/virtual-desktop/

## Virtual machines

https://docs.microsoft.com/en-us/azure/virtual-machines/

## Virtual machine scale sets

let you deploy and manage a set of **identical** virtual machines.

## Azure Virtual Network

- Isolation and segmentation (named subnet)
- Internet communications (For VM management, you can connect via the Azure CLI, Remote Desktop Protocol, or Secure Shell.)
- Communicate between Azure resources
- Communicate with on-premises resources
- Route network traffic
- Filter network traffic
- Connect virtual networks

## Azure VPN Gateway

[< back](./az.md)
