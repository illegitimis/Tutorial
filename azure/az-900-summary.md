# AZ-900 Summary

> Azure Fundamentals — AZ-900 exam learning paths overview and knowledge check collection.

## Learning Paths

1. **Describe Core Azure Concepts** — cloud computing fundamentals, benefits, service models (IaaS, PaaS, SaaS), cloud deployment models.
2. **Describe Core Azure Services** — Azure compute, networking, storage, and database services.
3. **Describe Core Solutions and Management Tools on Azure** — IoT, AI, DevOps, Azure Monitor, Azure Advisor, Azure Resource Manager.
4. **Describe General Security and Network Security Features** — Azure Security Center, Sentinel, firewall, DDoS Protection, network security groups.
5. **Describe Identity, Governance, Privacy, and Compliance Features** — Azure Active Directory, MFA, Conditional Access, RBAC, Resource Locks, Tags, Azure Policy.
6. **Describe Azure Cost Management and Service Level Agreements** — TCO Calculator, Pricing Calculator, cost optimization, SLAs, service lifecycle.

See also: [cloud-concepts.md](./cloud-concepts.md) | [core-services.md](./core-services.md) | [solutions-and-tools.md](./solutions-and-tools.md) | [security.md](./security.md) | [identity-and-governance.md](./identity-and-governance.md) | [cost-management.md](./cost-management.md)

## Knowledge Check Collection

The following knowledge checks correspond to AZ-900 Microsoft Learn modules.

### LP1 — Core Azure Concepts

**117: Cloud Fundamentals**

1. True or false: You need to purchase an Azure account before you can use any Azure resources.
   - Correct: **False** — you can use a free Azure account or a Microsoft Learn sandbox to create resources.

2. What is meant by cloud computing?
   - Correct: **Delivery of computing services over the internet.**

3. Which of the following is not a feature of cloud computing?
   - Correct: **A limited pool of services** — the cloud offers a nearly limitless pool of raw compute, storage, and networking components.

**125A: Cloud Service Models and OpEx vs. CapEx**

1. Which of the following choices is not a cloud computing category?
   - Correct: **Networking-as-a-Service (NaaS)**

2. Which of the following statements is true?
   - Correct: **With Operating Expenses (OpEx), you are only responsible for the computing resources that you use.**

3. Which of the following options is not a type of cloud computing?
   - Correct: **Distributed cloud** — the three types are public, private, and hybrid.

4. Which of the following choices is not a benefit of using cloud services?
   - Correct: **Geographic isolation** — one of the primary advantages to cloud computing is geographic distribution, not isolation.

**125B: Cloud Deployment Models**

1. Which cloud deployment model is best for a short-term SQL server project requiring immediate deployment and no long-term commitment?
   - Correct: **Public cloud** — the need for quick deployment and the short lifecycle make public cloud the best option.

2. VMs networked together with cloud storage, a web server, and a VPN connecting to an on-premises datacenter — which model?
   - Correct: **Hybrid cloud** — uses both public and private cloud with a connection between the two.

3. Two private datacenters connected by a VPN through a cloud provider — which model?
   - Correct: **Private cloud** — the VPN is a public cloud resource, but because it is a private connection between two private datacenters, this is a private cloud deployment.

**136: Azure Architecture and Organization**

1. Which of the following can be used to manage governance across multiple Azure subscriptions?
   - Correct: **Management groups** — facilitate the hierarchical ordering of Azure resources into collections at a level of scope above subscriptions.

2. Which of the following is a logical unit of Azure services that links to an Azure account?
   - Correct: **Azure subscription** — a logical unit of Azure services that links to an Azure account, representing a container for resources.

3. Which of the following features does not apply to resource groups?
   - Correct: **Resource groups can be nested** — resource groups cannot be nested.

4. Which of the following statements is a valid statement about an Azure subscription?
   - Correct: **An Azure subscription is a logical unit of Azure services.**

### LP2 — Core Azure Services

Knowledge checks covered in [core-services.md](./core-services.md) (modules 218, 227, 237, 249).

### LP3 — Core Solutions and Management Tools

Knowledge checks covered in [solutions-and-tools.md](./solutions-and-tools.md) (modules 317, 327, 336, 347, 359, 367).

### LP4 — General Security and Network Security

Knowledge checks covered in [security.md](./security.md) (modules 417, 428).

### LP5 — Identity, Governance, Privacy, and Compliance

**515: Secure Access**

1. How can the IT department ensure that employees can access company applications only from approved tablet devices?
   - Correct: **Conditional Access** — enables you to require users to access your applications only from approved, or managed, devices.

2. How can the IT department use biometric properties to enable delivery drivers to prove their identities?
   - Correct: **Multifactor authentication** — can include something the user knows, something the user has, and something the user is.

3. How can the IT department reduce the number of times users must authenticate to access multiple applications?
   - Correct: **SSO** — enables a user to remember only one ID and one password to access multiple applications.

**52B: Cloud Governance Strategy**

1. How can Tailwind Traders allow some users to control virtual machines but prevent them from modifying networking and other resources?
   - Correct: **Create a role assignment through Azure RBAC** — enables you to create roles that limit access only to virtual machines.

2. Which is the best way to ensure that the team deploys only cost-effective virtual machine SKU sizes?
   - Correct: **Create a policy in Azure Policy that specifies the allowed SKU sizes** — applied when you create new VMs or resize existing ones.

3. Which is the best way for Tailwind Traders to identify which billing department each Azure resource belongs to?
   - Correct: **Apply a tag to each resource that includes the associated billing department.**

**538: Compliance and Privacy**

1. Where can the team access details about the personal data Microsoft processes and how the company processes it, including for Cortana?
   - Correct: **Microsoft Privacy Statement** — provides information relevant to specific services, including Cortana.

2. Where can the legal team access information around how the Microsoft cloud helps them secure sensitive data and comply with applicable laws and regulations?
   - Correct: **Trust Center** — a great resource for people in your organization who might play a role in security, privacy, and compliance.

3. Where can the IT department find reference blueprints that it can apply directly to its Azure subscriptions?
   - Correct: **Azure compliance documentation** — provides reference blueprints, or policy definitions, for common standards that you can apply to your Azure subscription.

### LP6 — Cost Management and Service Level Agreements

**617: Plan and Manage Azure Costs**

1. Which is the best first step to compare the cost of running environments on Azure versus in a datacenter?
   - Correct: **Run the Total Cost of Ownership Calculator.**

2. What is the best way to ensure that the development team does not provision too many virtual machines at the same time?
   - Correct: **Apply spending limits to the development team's Azure subscription.**

3. Which is the most efficient way for the testing team to save costs on virtual machines on weekends?
   - Correct: **Deallocate virtual machines when they are not in use.**

4. Resources in Dev and Test environments are paid for by different departments. What is the best way to categorize costs by department?
   - Correct: **Apply a tag to each virtual machine that identifies the appropriate billing department.**

**626: SLAs and Service Lifecycle**

1. What is the SLA for Azure Maps in terms of guaranteed uptime?
   - Correct: **99.9 percent.**

2. What is the composite SLA after adding a third virtual machine and Azure Maps?
   - Correct: **99.58 percent.** To compute the composite SLA, multiply the SLA of each individual service.

3. Adding a third virtual machine reduces the composite SLA. How can Tailwind Traders offset this reduction?
   - Correct: **Deploy extra instances of the same virtual machines across different availability zones in the same Azure region.**

4. What approach might the company take in adding an augmented reality (AR) preview service?
   - Correct: **The development team can create a prototype version of the app that includes the AR service that it tests out with select retail employees.** After the AR service reaches general availability (GA), the team can roll it out to production.

[az900-ms-learn]: https://docs.microsoft.com/en-us/learn/certifications/azure-fundamentals/
[lp1]: https://docs.microsoft.com/en-us/learn/paths/az-900-describe-cloud-concepts/
[lp2]: https://docs.microsoft.com/en-us/learn/paths/az-900-describe-core-azure-services/
[lp3]: https://docs.microsoft.com/en-us/learn/paths/az-900-describe-core-solutions-management-tools-azure/
[lp4]: https://docs.microsoft.com/en-us/learn/paths/az-900-describe-general-security-network-security-features/
[lp5]: https://docs.microsoft.com/en-us/learn/paths/az-900-describe-identity-governance-privacy-compliance-features/
[lp6]: https://docs.microsoft.com/en-us/learn/paths/az-900-describe-azure-cost-management-service-level-agreements/


[<<](./index.md) | [home](../README.md)
