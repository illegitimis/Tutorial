# Knowledge check

> https://docs.microsoft.com/en-us/learn/modules/build-cloud-governance-strategy-azure/11-knowledge-check

1. How can Tailwind Traders allow some users to control the virtual machines in each environment but prevent them from modifying networking and other resources in the same resource group or Azure subscription?
- [X] Create a **role assignment** through Azure role-based access control (Azure RBAC).  
That's correct.  
Azure RBAC enables you to create roles that define access permissions.  
You might create one role that limits access only to virtual machines  
and a second role that provides administrators with access to everything.
- [ ] Create a policy in Azure Policy that audits resource usage.  
That's **incorrect**.  
Although you might be able to audit how your resources are used,  
is there a way to prevent users from changing resources they're not meant to access?
- [ ] Split the environment into separate resource groups.
2. Which is the best way for Tailwind Traders to ensure that the team deploys only _cost-effective_ virtual machine SKU sizes?
- [X] **Create a policy in Azure Policy that specifies the allowed SKU sizes**.  
That's correct.   
After you enable this policy, that policy is applied when you create new virtual machines or resize existing ones.  
Azure Policy also evaluates any current virtual machines in your environment.
- [ ] Periodically inspect the deployment manually to see which SKU sizes are used.
- [ ] Create an Azure RBAC role that defines the allowed virtual machine SKU sizes.
3. Which is likely the best way for Tailwind Traders to identify which billing department each Azure resource belongs to?
- [ ] Track resource usage in a spreadsheet.
- [ ] *Split the deployment into separate Azure subscriptions*, where each subscription belongs to its own billing department.  
That's incorrect.  
Although you can use subscriptions to separate billing by department,  
is there another method that allows all resources to stay within the same subscription?
- [X] Apply a tag to each resource that includes the associated billing department.  
That's _correct_.  
Tags provide extra information, or metadata, about your resources.  
The team might create a tag that's named BillingDept whose value would be the name of the billing department.  
You can use `Azure Policy` to ensure that the proper tags are assigned when resources are provisioned.

[< 5: Describe identity, governance, privacy, and compliance features](./5-lp-az-900.md)