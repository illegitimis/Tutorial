---
title: Cost Management
layout: default
nav_order: 5
parent: Azure
last_modified_date: 2026-03-29 21:15:03 +00:00
---

# Cost Management

## Pricing Models

### How to Purchase Azure Services

There are three main ways to purchase Azure services:

- **Enterprise Agreement** — larger customers sign an Enterprise Agreement with Microsoft, committing to a predefined amount of cloud services over a period of three years and typically paying annually.
- **From the web** — purchase Azure services directly from the Azure website and pay standard prices.
- **Through a Cloud Solution Provider (CSP)** — Microsoft partner that helps you build solutions on top of Azure.

### Factors That Affect Cost

Several factors affect the cost of Azure resources:

- **Resource type** — costs are resource-specific; usage meters track different aspects (CPU time, disk size, write operations, network traffic, etc.).
- **Usage meters** — when you provision a resource, Azure creates meters to track that resource's usage.
- **Resource usage** — you are charged for what you use; deallocating a VM stops compute/network billing but storage may still be billed.
- **Azure subscription types** — some subscription types include usage allowances.
- **Azure Marketplace** — third-party services may include billing for both Azure infrastructure costs and the vendor's services.
- **Location** — different Azure regions can have different associated prices.
- **Bandwidth** — some inbound data transfers (data going into Azure data centers) are free; outbound data transfer pricing is based on zones.
- **Reserved instances** — committing to one-year or three-year plans can save money compared to pay-as-you-go pricing.
- **Azure Hybrid Benefit** — bring Windows Server and SQL Server on-premises licenses with Software Assurance to Azure to save costs.

### Bandwidth Pricing Zones

| Zone | Regions |
|---|---|
| Zone 1 | Australia Central, West US, East US, Canada West, West Europe, France Central, and others |
| Zone 2 | Australia East, Japan West, Central India, Korea South, and others |
| Zone 3 | Brazil South, South Africa North, South Africa West, UAE Central, UAE North |
| DE Zone 1 | Germany Central, Germany Northeast |

## TCO Calculator

The Total Cost of Ownership (TCO) Calculator helps you estimate the cost savings of operating your solution on Azure over time instead of in your on-premises datacenter.

You enter the details of your on-premises workloads, and the TCO Calculator suggests industry-average cost for related operational costs. You then review the suggested industry-average cost and adjust to match your environment.

### Using the TCO Calculator

The process involves three steps:

1. **Define your workloads** — enter the specifications of your on-premises infrastructure into the TCO Calculator: servers, databases, storage, and outbound network bandwidth.
2. **Adjust assumptions** — specify whether your current on-premises licenses are enrolled for Software Assurance, if you need to replicate your storage to another Azure region, your software development and testing costs, the cost of IT labor, and other details.
3. **View the report** — the report shows a side-by-side comparison of on-premises vs. Azure costs over time.

### Pricing Calculator

The Pricing Calculator helps you estimate the cost of Azure products. The options that you can configure in the Pricing Calculator vary between products, but basic configuration options include:

- **Region** — the geographic location in which you can provision a service.
- **Tier** — Free tier, Basic tier, etc.
- **Billing options** — different ways to pay for or license a service.
- **Support options** — different support plan options.
- **Programs and offers** — available discounts or other special offers.
- **Azure Dev/Test pricing** — significant discounts on development and testing workloads.

## Cost Optimization

### Managing and Minimizing Total Cost on Azure

Best practices for understanding and minimizing your Azure bill:

- **Understand estimated costs before deploying** — use the Pricing Calculator and Total Cost of Ownership Calculator to estimate costs.
- **Use Azure Advisor to monitor usage** — Azure Advisor identifies unused or underutilized resources and recommends unused resources that you can remove.
- **Use spending limits** — apply spending limits to development team Azure subscriptions; if you exceed your spending limit, active resources are deallocated.
- **Use Azure Reservations to prepay** — Azure Reservations offer discounted prices on certain Azure services. Prepaying for one-year or three-year plans provides savings compared to pay-as-you-go pricing.
- **Choose low-cost locations and regions** — the cost of Azure products, services, and resources can vary across locations and regions.
- **Research available cost-saving offers** — explore the Azure customer and subscription offers and stay current with the latest Azure customer and subscription offers.
- **Use Azure Cost Management + Billing** — a free service that helps you understand your Azure bill, manage your account and subscriptions, monitor and control Azure spending, and optimize resource use.
- **Apply tags to identify cost owners** — apply tags to groups of Azure resources to organize billing data.
- **Resize underutilized virtual machines** — a common recommendation from Azure Advisor is to resize or shut down VMs that are underutilized or idle.
- **Deallocate VMs during off-hours** — stop (deallocate) virtual machines during off-peak hours; when deallocated, the associated hard disks and data are still kept in Azure, but you do not pay for CPU or network consumption.
- **Delete unused resources** — delete unused resources such as old VMs, storage accounts, or databases.
- **Migrate IaaS to PaaS services** — PaaS services typically reduce your operational and management overhead, freeing up budget for other uses.
- **Use Azure Hybrid Benefit** — apply on-premises Windows Server and SQL Server licenses with Software Assurance to Azure.

### Service-Level Agreements (SLAs)

A service-level agreement (SLA) is a formal agreement between a service company and the customer. For Azure, this agreement defines the performance standards that Microsoft commits to for you and your workloads.

Key concepts:

- **SLAs define performance targets** — uptime and connectivity guarantees, typically expressed as a percentage (e.g., 99.9%, 99.99%).
- **Composite SLA** — for a set of services, multiply the SLA of each individual service to calculate the composite SLA. Example: 99.9% x 99.9% x 99.99% x 99.99% = 99.78%.
- **Free and Preview services** — free products and services typically do not have an SLA. Services in preview are not covered by SLAs.
- **Availability Zones** — deploying extra instances of the same virtual machines across different availability zones in the same Azure region can improve composite SLA.

### Service Lifecycle

- **Private preview** — available to specific Azure customers for evaluation purposes.
- **Public preview** — available to all Azure customers; use preview services in testing but not in production, as they are not covered by SLAs.
- **General availability (GA)** — after a service is released to GA, it is available to all Azure customers as a generally available service and is covered by SLAs.

## Knowledge Check

**Module 1: Plan and Manage Azure Costs**

1. Which is the best first step the team should take to compare the cost of running environments on Azure versus in their datacenter?
   - Correct: **Run the Total Cost of Ownership Calculator.**

2. What is the best way to ensure that the development team does not provision too many virtual machines at the same time?
   - Correct: **Apply spending limits to the development team's Azure subscription.** If you exceed your spending limit, active resources are deallocated.

3. Which is the most efficient way for the testing team to save costs on virtual machines on weekends, when testers are not at work?
   - Correct: **Deallocate virtual machines when they are not in use.** When you deallocate virtual machines, the associated hard disks and data are still kept in Azure. But you do not pay for CPU or network consumption, which can help save costs.

4. Resources in the Dev and Test environments are each paid for by different departments. What is the best way to categorize costs by department?
   - Correct: **Apply a tag to each virtual machine that identifies the appropriate billing department.** You can apply tags to groups of Azure resources to organize billing data.

**Module 2: SLAs and Service Lifecycle**

1. What is the SLA for Azure Maps in terms of guaranteed uptime?
   - Correct: **99.9 percent.**

2. What is the new composite SLA after adding a third virtual machine and Azure Maps?
   - Correct: **99.58 percent.** To compute the composite SLA for a set of services, you multiply the SLA of each individual service.

3. Adding a third virtual machine reduces the composite SLA. How can Tailwind Traders offset this reduction?
   - Correct: **Deploy extra instances of the same virtual machines across the different availability zones in the same Azure region.** If one availability zone is affected, your virtual machine instance in the other availability zone should be unaffected.

4. What approach might the company take in adding an augmented reality (AR) preview service to its architecture?
   - Correct: **The development team can create a prototype version of the app that includes the AR service that it tests out with select retail employees.** After the AR service reaches general availability (GA), the team can roll it out to production.

[<](./index.md) | [<<](/index.md)
