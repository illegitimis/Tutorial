# Control access to cloud resources by using Azure role-based access control

> https://docs.microsoft.com/en-us/learn/modules/build-cloud-governance-strategy-azure/2-control-access-azure-rbac

When you have multiple IT and engineering teams, how can you control what access they have to the resources in your cloud environment? It's a good security practice to *grant users only the rights they need to perform their job*, and only to the relevant resources.

Instead of defining the detailed access requirements for each individual, and then updating access requirements when new resources are created, Azure enables you to control access through [Azure role-based access control](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) (Azure RBAC).

Azure provides built-in roles that describe *common access rules for cloud resources*.
You can also define your own roles. Each role has an associated set of access permissions that relate to that role.
When you assign individuals or groups to one or more roles, they receive all of the associated access permissions.

## How is role-based access control applied to resources?

Role-based access control is applied to a scope, which is a resource or set of resources that this access applies to.

Here's a diagram that shows the relationship between roles and scopes.

![](https://docs.microsoft.com/en-us/learn/azure-fundamentals/build-cloud-governance-strategy-azure/media/4-role-scope-0223bfae.png)

A diagram showing scopes along the Y axis and roles across the X axis. Role and scope combinations each map to a specific kind of user or account, such as an observer or an administrator.

Scopes include:

- A management group (a collection of multiple subscriptions).
- A single subscription.
- A resource group.
- A single resource.

*Observers, Users managing resources, Admins, and Automated processes* illustrate the _kinds of users or accounts_ that would typically be assigned each of the various roles.

**When you grant access at a parent scope, those permissions are inherited by all child scopes.**

For example:

- When you assign the Owner role to a user at the management group scope, that user can manage everything in all subscriptions within the management group.
- When you assign the Reader role to a group at the subscription scope, the members of that group can view every resource group and resource within the subscription.
- When you assign the Contributor role to an application at the resource group scope, the application can manage resources of all types within that resource group, but not other resource groups within the subscription.

## When should I use Azure RBAC?

Use Azure RBAC when you need to:

- Allow one user to manage VMs in a subscription and another user to manage virtual networks.
- Allow a database administrator group to manage SQL databases in a subscription.
- Allow a user to manage all resources in a resource group, such as virtual machines, websites, and subnets.
- Allow an application to access all resources in a resource group.

These are just a few examples. You'll find the complete list of built-in roles at the end of this module.

## Who does Azure RBAC apply to?

You can apply Azure RBAC to an individual person or to a group.
You can also apply Azure RBAC to other special identity types, such as service principals and managed identities.
These identity types are used by applications and services to automate access to Azure resources.

Tailwind Traders has the following teams with an interest in some part of their overall IT environment:

- IT Administrators This team has ultimate ownership of technology assets, both on-premises and in the cloud.
The team requires full control of all resources.
- Backup and Disaster Recovery
This team is responsible for managing the health of regular backups and invoking any data or system recoveries.
- Cost and Billing People
in this team track and report on technology-related spend. They also manage the organization's internal budgets.
- Security Operations
This team monitors and responds to any technology-related security incidents.
The team requires ongoing access to log files and security alerts.

## How do I manage Azure RBAC permissions?

You manage access permissions on the Access control (IAM) pane in the Azure portal.
This pane shows who has access to what scope and what roles apply.
You can also grant or remove access from this pane.

The following screenshot shows an example of the Access control (IAM) pane for a resource group.
In this example, Alain Charon has been assigned the Backup Operator role for this resource group.
In the Access Control pane, settings and permissions for a user are shown.

![A screenshot that shows the Access Control Role Assignment pane](https://docs.microsoft.com/en-us/learn/azure-fundamentals/build-cloud-governance-strategy-azure/media/4-role-based-access-control-blade-360b5130.png).

[< 5: Describe identity, governance, privacy, and compliance features](./5-lp-az-900.md)