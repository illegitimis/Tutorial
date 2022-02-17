# Control and audit your resources by using Azure Policy

> https://docs.microsoft.com/en-us/learn/modules/build-cloud-governance-strategy-azure/6-control-audit-resources-azure-policy

In a previous exercise in this module, you identified your governance and business requirements. How do you ensure that your resources stay compliant? Can you be alerted if a resource's configuration has changed?

[Azure Policy](https://azure.microsoft.com/en-us/services/azure-policy/#overview) is a service in Azure that enables you to create, assign, and manage policies that control or audit your resources. These policies enforce different rules across all of your resource configurations so that those configurations stay compliant with corporate standards.

## How does Azure Policy define policies?

Azure Policy enables you to define both individual policies and *groups of related policies*, known as **initiatives**. Azure Policy evaluates your resources and highlights resources that aren't compliant with the policies you've created. Azure Policy can also prevent noncompliant resources from being created.

Azure Policy comes with built-in policy and initiative definitions for Storage, Networking, Compute, Security Center, and Monitoring. For example, if you define a policy that allows only a certain SKU (stock-keeping unit) size for the virtual machines (VMs) to be used in your environment, that policy is invoked when you create a new VM and whenever you resize existing VMs. Azure Policy also evaluates and monitors all current VMs in your environment.

In some cases, Azure Policy can automatically remediate noncompliant resources and configurations to ensure the integrity of the state of the resources. For example, if all resources in a certain resource group should be tagged with AppName tag and a value of "SpecialOrders" Azure Policy will automatically reapply that tag if it was missing.

Azure Policy also integrates with Azure DevOps by applying any continuous integration and delivery pipeline policies that pertain to the pre-deployment and post-deployment phases of your applications.

## Azure Policy in action

Implementing a policy in Azure Policy involves three tasks:

- Create a policy definition.
- Assign the definition to resources.
- Review the evaluation results.

### Task 1. Create a policy definition

A policy definition expresses what to evaluate and what action to take.
For example, you could prevent VMs from being deployed in certain Azure regions.
You also could audit your storage accounts to verify that they only accept connections from allowed networks.

Every policy definition has conditions under which it's enforced.
A policy definition also has an accompanying effect that takes place when the conditions are met.
Here are some example policy definitions:

- **Allowed virtual machine SKUs** This policy enables you to specify a set of VM SKUs that your organization can deploy.
- **Allowed locations** This policy enables you to restrict the locations that your organization can specify when it deploys resources. Its effect is used to enforce your *geographic compliance* requirements.
- **MFA should be enabled on accounts with write permissions on your subscription** This policy requires that multifactor authentication (MFA) be enabled for all subscription accounts with write privileges to prevent a breach of accounts or resources.
- **CORS should not allow every resource to access your web applications** Cross-origin resource sharing (CORS) is an HTTP feature that enables a web application running under one domain to access resources in another domain. For security reasons, modern web browsers restrict cross-site scripting by default. This policy allows only required domains to interact with your web app.
- **System updates should be installed on your machines** This policy enables Azure Security Center to recommend missing security system updates on your servers.
  
### Task 2. Assign the definition to resources

To implement your policy definitions, you assign definitions to resources. A *policy assignment* is a policy definition that takes place within a specific scope. This scope could be a management group (a collection of multiple subscriptions), a single subscription, or a resource group.

Policy assignments are *inherited by all child resources within that scope*.
If a policy is applied to a resource group, that policy is applied to all resources within that resource group.
You can exclude a subscope from the policy assignment if there are specific child resources you need to be exempt from the policy assignment.

### Task 3. Review the evaluation results

When a condition is evaluated against your existing resources, each resource is marked as compliant or noncompliant.
You can review the noncompliant policy results and take any action that's needed.

*Policy evaluation happens about once per hour*.
If you make changes to your policy definition and create a policy assignment, that policy is evaluated over your resources within the hour.

## How do I define an initiative?

You define initiatives by using the Azure portal or command-line tools.
From the Azure portal, you can search the list of built-in initiatives that are built into Azure.
You also can create your own custom policy definition.

The following image shows a few example Azure Policy initiatives in the Azure portal.

![Screenshot showing Azure portal defining initiatives and definitions.](https://docs.microsoft.com/en-us/learn/azure-fundamentals/build-cloud-governance-strategy-azure/media/3-define-initiatives-a834dde7.png)

## How do I assign an initiative?

Like a policy assignment, an initiative assignment is an initiative definition that's assigned to a specific scope of a management group, a subscription, or a resource group.

Even if you have only a single policy, an initiative enables you to increase the number of policies over time.
Because the associated initiative remains assigned, it's easier to add and remove policies without the need to change the policy assignment for your resources.

[< 5: Describe identity, governance, privacy, and compliance features](./5-lp-az-900.md)