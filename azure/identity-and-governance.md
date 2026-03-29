# Identity and Governance

## Azure Active Directory

Identity has become the new primary security boundary. Accurately proving that someone is a valid user of your system, with an appropriate level of access, is critical to maintaining control of your data.

Microsoft introduced Active Directory in Windows 2000 to give organizations the ability to manage multiple on-premises infrastructure components and systems by using a single identity per user.

Azure Active Directory (Azure AD) is Microsoft's cloud-based identity and access management service. With Azure AD, you control the identity accounts, but Microsoft ensures that the service is available globally.

When you secure identities on-premises with Active Directory, Microsoft does not monitor sign-in attempts. When you connect Active Directory with Azure AD, Microsoft can help protect you by detecting suspicious sign-in attempts at no extra cost. For example, Azure AD can detect sign-in attempts from unexpected locations or unknown devices.

### Who Uses Azure AD?

Azure AD is for:

- **IT administrators** — control access to applications and resources based on business requirements.
- **App developers** — provide a standards-based approach for adding functionality to applications, such as adding SSO functionality or enabling an app to work with a user's existing credentials.
- **Users** — manage their own identities (for example, self-service password reset).
- **Online service subscribers** — Microsoft 365, Office 365, Azure, and Dynamics CRM Online tenants are automatically Azure AD tenants.

### Services Azure AD Provides

- **Authentication** — verifying identity to access applications and resources, including self-service password reset, multifactor authentication, a custom list of banned passwords, and smart lockout services.
- **Single sign-on (SSO)** — remember only one username and password to access multiple applications; a single identity is tied to the user.
- **Application management** — manage cloud and on-premises apps using Application Proxy, SaaS apps, the My Apps portal, and single sign-on.
- **Device management** — register devices to be managed through tools like Microsoft Intune; enables device-based Conditional Access policies.

### Authentication vs. Authorization

**Authentication (AuthN)** is the process of establishing the identity of a person or service that wants to access a resource. It establishes whether the user is who they say they are.

**Authorization (AuthZ)** is the process of establishing what level of access an authenticated person or service has. It specifies what data they are allowed to access and what they can do with it.

### Connecting Active Directory with Azure AD

Azure AD Connect synchronizes user identities between on-premises Active Directory and Azure AD. Azure AD Connect synchronizes changes between both identity systems, so you can use features like SSO, multifactor authentication, and self-service password reset under both systems.

Misc SSO notes:

- Directory sync: only usernames from on-prem AD to AAD
- Password hash sync: securely sync hashes of passwords to the cloud
- In both cases above, auth is in the cloud; if on-prem is needed, ADFS required
- Pass-through auth needs an agent on-premises and AAD Connect, with zero management, auto-update, and no additional infrastructure
- AAD Connect config: choose pass-through and enable SSO

## MFA and Conditional Access

### Multifactor Authentication

Multifactor authentication is a process where a user is prompted during sign-in for an additional form of identification. Examples include a code on their mobile phone or a fingerprint scan.

Multifactor authentication provides additional security for your identities by requiring two or more elements to fully authenticate. These elements fall into three "Something the user" categories:

| Category | Examples |
|---|---|
| knows | email address and password |
| has | a code sent to the user's mobile phone |
| is | biometric property such as a fingerprint or face scan |

Multifactor authentication increases identity security by limiting the impact of credential exposure. With multifactor authentication enabled, an attacker who has a user's password would also need to have possession of their phone or their fingerprint to fully authenticate.

### Azure AD Multi-Factor Authentication

Azure AD Multi-Factor Authentication is a Microsoft service that provides multifactor authentication capabilities. Users can choose an additional form of authentication during sign-in, such as a phone call or mobile app notification.

- **Azure Active Directory free edition** — enables Azure AD Multi-Factor Authentication for administrators with the global admin level of access, via the Microsoft Authenticator app, phone call, or SMS code. You can enforce MFA for all users via the Microsoft Authenticator app only by enabling security defaults.
- **Azure Active Directory Premium (P1 or P2)** — comprehensive and granular configuration through Conditional Access policies.
- **Multifactor authentication for Office 365** — a subset of Azure AD Multi-Factor Authentication capabilities.

### Conditional Access

Conditional Access is a tool that Azure Active Directory uses to allow (or deny) access to resources based on identity signals. These signals include who the user is, where the user is, and what device the user is requesting access from.

During sign-in, Conditional Access collects signals from the user, makes decisions based on those signals, and then enforces that decision by allowing or denying the access request or challenging for a multifactor authentication response.

The signal might be:

- the user's location
- the user's device
- the application that the user is trying to access

Use Conditional Access when you need to:

- Require multifactor authentication to access an application (for all users or only certain users).
- Require access to services only through approved client applications.
- Require users to access your application only from managed devices.
- Block access from untrusted sources, such as access from unknown or unexpected locations.

Conditional Access comes with a **What If** tool, which helps you plan and troubleshoot your Conditional Access policies.

> To use Conditional Access, you need an Azure AD Premium P1 or P2 license. If you have a Microsoft 365 Business Premium license, you also have access to Conditional Access features.

## RBAC

Azure role-based access control (Azure RBAC) enables you to control access to cloud resources. Instead of defining the detailed access requirements for each individual, Azure enables you to control access through Azure RBAC.

Azure provides built-in roles that describe common access rules for cloud resources. You can also define your own roles. Each role has an associated set of access permissions. When you assign individuals or groups to one or more roles, they receive all of the associated access permissions.

### How Role-Based Access Control Is Applied to Resources

Role-based access control is applied to a scope, which is a resource or set of resources that this access applies to.

Scopes include:

- A management group (a collection of multiple subscriptions).
- A single subscription.
- A resource group.
- A single resource.

When you grant access at a parent scope, those permissions are inherited by all child scopes.

Examples:

- When you assign the Owner role to a user at the management group scope, that user can manage everything in all subscriptions within the management group.
- When you assign the Reader role to a group at the subscription scope, the members of that group can view every resource group and resource within the subscription.
- When you assign the Contributor role to an application at the resource group scope, the application can manage resources of all types within that resource group, but not other resource groups within the subscription.

### When to Use Azure RBAC

Use Azure RBAC when you need to:

- Allow one user to manage VMs in a subscription and another user to manage virtual networks.
- Allow a database administrator group to manage SQL databases in a subscription.
- Allow a user to manage all resources in a resource group, such as virtual machines, websites, and subnets.
- Allow an application to access all resources in a resource group.

### Managing Azure RBAC Permissions

You manage access permissions on the Access control (IAM) pane in the Azure portal. This pane shows who has access to what scope and what roles apply. You can also grant or remove access from this pane.

## Resource Locks

A resource lock prevents resources from being accidentally deleted or changed.

Even with Azure RBAC policies in place, there is still a risk that people with the right level of access could delete critical cloud resources. Think of a resource lock as a warning system that reminds you that a resource should not be deleted or changed.

### Managing Resource Locks

You can manage resource locks from the Azure portal, PowerShell, the Azure CLI, or from an Azure Resource Manager template.

To view, add, or delete locks in the Azure portal, go to the Settings section of any resource's Settings pane.

### Lock Levels

You can apply locks to a subscription, a resource group, or an individual resource. You can set the lock level to:

- **CanNotDelete** — authorized people can still read and modify a resource, but they cannot delete the resource without first removing the lock.
- **ReadOnly** — authorized people can read a resource, but they cannot delete or change the resource. Applying this lock is like restricting all authorized users to the permissions granted by the Reader role in Azure RBAC.

### Deleting or Changing a Locked Resource

To modify a locked resource, you must first remove the lock. After you remove the lock, you can apply any action you have permissions to perform. Resource locks apply regardless of RBAC permissions — even if you are an owner of the resource, you must still remove the lock before you can perform the blocked activity.

### Combining Resource Locks with Azure Blueprints

To make the protection process more robust, you can combine resource locks with Azure Blueprints. Azure Blueprints enables you to define the set of standard Azure resources that your organization requires. For example, you can define a blueprint that specifies that a certain resource lock must exist. Azure Blueprints can automatically replace the resource lock if that lock is removed.

### Exercise: Protect a Storage Account From Accidental Deletion

This exercise demonstrates resource locks by:

1. Creating a resource group (`my-test-rg`) in the Azure portal.
2. Adding a delete lock (`rg-delete-lock`) to the resource group.
3. Verifying the resource group cannot be deleted.
4. Adding a storage account (`mysaNNN`) to the resource group and confirming the parent lock prevents deletion.
5. Removing the lock and then deleting the resource group (and its child storage account).

> Note: `524-payasyougo.png` — diagram of pay-as-you-go pricing would appear here.

## Tags

As your cloud usage grows, it is increasingly important to stay organized. Resource tags are a way to organize resources. Tags provide extra information, or metadata, about your resources. This metadata is useful for:

- **Resource management** — locate and act on resources that are associated with specific workloads, environments, business units, and owners.
- **Cost management and optimization** — group resources to report on costs, allocate internal cost centers, track budgets, and forecast estimated cost.
- **Operations management** — group resources according to how critical their availability is to your business; helps formulate service-level agreements (SLAs).
- **Security** — classify data by its security level, such as public or confidential.
- **Governance and regulatory compliance** — identify resources that align with governance or regulatory compliance requirements, such as ISO 27001.
- **Workload optimization and automation** — visualize all of the resources that participate in complex deployments.

### Managing Resource Tags

You can add, modify, or delete resource tags through PowerShell, the Azure CLI, Azure Resource Manager templates, the REST API, or the Azure portal.

You can also manage tags by using Azure Policy — for example, to ensure that a resource inherits the same tags as its parent resource group, or to require that certain tags be added to new resources as they are provisioned.

### Example Tagging Structure

| Name | Value |
|---|---|
| AppName | The name of the application that the resource is part of |
| CostCenter | The internal cost center code |
| Owner | The name of the business owner responsible for the resource |
| Environment | An environment name, such as "Prod," "Dev," or "Test" |
| Impact | How important the resource is to business operations |

## Azure Policy

Azure Policy is a service in Azure that enables you to create, assign, and manage policies that control or audit your resources. These policies enforce different rules across all of your resource configurations so that those configurations stay compliant with corporate standards.

Azure Policy enables you to define both individual policies and groups of related policies, known as **initiatives**. Azure Policy evaluates your resources and highlights resources that are not compliant with the policies you have created. Azure Policy can also prevent noncompliant resources from being created.

Azure Policy comes with built-in policy and initiative definitions for Storage, Networking, Compute, Security Center, and Monitoring. In some cases, Azure Policy can automatically remediate noncompliant resources and configurations.

### Implementing a Policy

Implementing a policy in Azure Policy involves three tasks:

1. **Create a policy definition** — expresses what to evaluate and what action to take. For example, you could prevent VMs from being deployed in certain Azure regions, or audit storage accounts to verify they only accept connections from allowed networks.

   Example policy definitions:
   - **Allowed virtual machine SKUs** — specify a set of VM SKUs that your organization can deploy.
   - **Allowed locations** — restrict the locations that your organization can specify when it deploys resources (enforces geographic compliance).
   - **MFA should be enabled on accounts with write permissions on your subscription** — require MFA for all subscription accounts with write privileges.
   - **CORS should not allow every resource to access your web applications** — allow only required domains to interact with your web app.
   - **System updates should be installed on your machines** — recommend missing security system updates.

2. **Assign the definition to resources** — a policy assignment takes place within a specific scope (management group, subscription, or resource group). Policy assignments are inherited by all child resources within that scope.

3. **Review the evaluation results** — each resource is marked as compliant or noncompliant. Policy evaluation happens about once per hour.

### Initiatives

An initiative is a group of related policies. You define initiatives using the Azure portal or command-line tools. Like a policy assignment, an initiative assignment is assigned to a specific scope. An initiative enables you to increase the number of policies over time without needing to change the policy assignment for your resources.

### Exercise: Restrict Deployments to a Specific Location

This exercise creates a policy in Azure Policy that restricts deployment of Azure resources to a specific location (East US region), then verifies the policy by attempting to create a storage account in a location that violates the policy.

## Compliance and Privacy

### Governance Introduction

Governance describes the general process of establishing rules and policies and ensuring that those rules and policies are enforced. Compliance means to adhere to a law, standard, or set of guidelines. Regulatory compliance refers to the discipline and process of ensuring that a company follows the laws that governing bodies enforce.

Governance is most beneficial when you have:

- Multiple engineering teams working in Azure.
- Multiple subscriptions to manage.
- Regulatory requirements that must be enforced.
- Standards that must be followed for all cloud resources.

### Compliance Categories on Azure

Azure compliance offerings are grouped under four categories: Global, US Government, Industry, and Regional.

Key resources for compliance and privacy:

- **Microsoft Privacy Statement** — provides information relevant to specific services, including data Microsoft collects, how it uses it, and for what purposes.
- **Trust Center** — a resource for people in your organization who play a role in security, privacy, and compliance.
- **Online Services Terms** — a legal agreement between Microsoft and the customer detailing obligations with respect to the processing and security of customer data and personal data.
- **Azure compliance documentation** — provides reference blueprints, or policy definitions, for common standards that you can apply to your Azure subscription.
- **Azure Government** — a separate instance of Azure that meets the security and compliance needs of US federal agencies.
- **Azure China 21Vianet** — a physically separated instance of Azure cloud services operated and transacted by a local company in China.

### Cloud Governance Summary

Services and features in Azure supporting governance:

- Azure RBAC — create roles that define access permissions.
- Resource locks — prevent resources from being accidentally deleted or changed.
- Resource tags — provide extra information, or metadata, about your resources.
- Azure Policy — create, assign, and manage policies that control or audit your resources.
- Azure Blueprints — define a repeatable set of governance tools and standard Azure resources that your organization requires.

## Knowledge Check

**Module 1: Secure Access**

1. How can the IT department ensure that employees at the company's retail stores can access company applications only from approved tablet devices?
   - Correct: **Conditional Access** — enables you to require users to access your applications only from approved, or managed, devices.

2. How can the IT department use biometric properties, such as facial recognition, to enable delivery drivers to prove their identities?
   - Correct: **Multifactor authentication** — authenticating through MFA can include something the user knows, something the user has, and something the user is.

3. How can the IT department reduce the number of times users must authenticate to access multiple applications?
   - Correct: **SSO** — enables a user to remember only one ID and one password to access multiple applications.

**Module 2: Cloud Governance**

1. How can Tailwind Traders allow some users to control the virtual machines in each environment but prevent them from modifying networking and other resources?
   - Correct: **Create a role assignment through Azure RBAC** — enables you to create roles that limit access only to virtual machines.

2. Which is the best way to ensure that the team deploys only cost-effective virtual machine SKU sizes?
   - Correct: **Create a policy in Azure Policy that specifies the allowed SKU sizes** — applied when you create new virtual machines or resize existing ones.

3. Which is likely the best way for Tailwind Traders to identify which billing department each Azure resource belongs to?
   - Correct: **Apply a tag to each resource that includes the associated billing department** — tags provide extra information or metadata about your resources.

**Module 3: Compliance and Privacy**

1. Where can the team access details about the personal data Microsoft processes and how it processes it, including for Cortana?
   - Correct: **Microsoft Privacy Statement** — provides information relevant to specific services, including Cortana.

2. Where can the legal team access information around how the Microsoft cloud helps them secure sensitive data and comply with applicable laws and regulations?
   - Correct: **Trust Center** — a great resource for people in your organization who might play a role in security, privacy, and compliance.

3. Where can the IT department find reference blueprints that it can apply directly to its Azure subscriptions?
   - Correct: **Azure compliance documentation** — provides reference blueprints, or policy definitions, for common standards that you can apply to your Azure subscription.

[aad-free]: https://azure.microsoft.com/en-us/free/
[aad-compare]: https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-compare-azure-ad-to-ad
[aad-overview]: https://azure.microsoft.com/en-us/services/active-directory/#overview
[sso-what]: https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on
[sso-seamless]: https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-sso
[aad-connect]: https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-azure-ad-connect
[mfa-docs]: https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks
[conditional-access]: https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/
[mfa-licensing]: https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-licensing#available-versions-of-azure-multi-factor-authentication
[rbac-overview]: https://docs.microsoft.com/en-us/azure/role-based-access-control/overview
[resource-locks]: https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json
[azure-policy]: https://azure.microsoft.com/en-us/services/azure-policy/#overview
[privacy-statement]: https://privacy.microsoft.com/en-US/privacystatement
[online-services]: https://www.microsoft.com/licensing/terms/product/ForallOnlineServices
[trust-center]: https://www.microsoft.com/ro-ro/trust-center
[compliance-offerings]: https://docs.microsoft.com/en-us/compliance/regulatory/offering-home
[azure-compliance]: https://docs.microsoft.com/en-us/azure/compliance/
[azure-government]: https://azure.microsoft.com/global-infrastructure/government
[azure-geographies]: https://azure.microsoft.com/en-us/global-infrastructure/geographies/#geographies
[built-in-roles]: https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles
[tag-policies]: https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-policies
[policy-samples]: https://docs.microsoft.com/en-us/azure/governance/policy/samples/


[<<](./index.md) | [home](../README.md)
