# Exercise - Restrict deployments to a specific location by using Azure Policy

> https://docs.microsoft.com/en-us/learn/modules/build-cloud-governance-strategy-azure/7-restrict-location-azure-policy

In this exercise, you create a policy in Azure Policy that restricts the deployment of Azure resources to a specific location.
You verify the policy by attempting to create a storage account in a location that violates the policy.

Tailwind Traders wants to *limit the location where resources can be deployed to the East US region*.

It has two reasons:

- **Improved cost tracking** To track costs, Tailwind Traders uses different subscriptions to track deployments to each of its regional locations. The policy will ensure that all resources are deployed to the East US region.
- **Adhere to data residency and security compliance**
Tailwind Traders must adhere to a compliance rule that states where customer data can be stored.
Here, customer data must be stored in the East US region.
Recall that you can assign a policy to a management group, a single subscription, or a resource group.
Here, you assign the policy to a resource group so that policy doesn't affect any other resources in your Azure subscription.