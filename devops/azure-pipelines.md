---
title: Azure Pipelines
layout: default
nav_order: 17
parent: DevOps
last_modified_date: 2026-03-31 00:00:00 +00:00
---

# Azure Pipelines

Build, test, and deploy .NET Core apps [1] \
Build Azure Repos Git or TFS Git repositories [2] \
For an Azure Repos Git repo, you cannot configure a PR trigger in the YAML file \
PR definition [3]; use branch policies [4] instead

Install Azure CLI on Windows [5] \
`az pipelines` [6] \
Manage Azure CLI extensions: install, update, and remove [7] \
`azure-pipelines-agent` output variable [8] \
`steps.task` [9] \
Auto detect configuration and git aliases [10] \
**JMESPath** tutorial [11] \
Manage security in Azure Pipelines [12] \
View permissions for yourself or others [13]

[1]: https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops&tabs=yaml-editor
[2]: https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/azure-repos-git?view=azure-devops&tabs=yaml#pr-triggers
[3]: https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/pr?view=azure-pipelines#remarks
[4]: https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops&tabs=browser#build-validation
[5]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&pivots=msi
[6]: https://learn.microsoft.com/en-us/cli/azure/pipelines?view=azure-cli-latest
[7]: https://learn.microsoft.com/en-us/cli/azure/azure-cli-extensions-overview?view=azure-cli-latest
[8]: https://github.com/Microsoft/azure-pipelines-agent/blob/master/docs/preview/outputvariable.md
[9]: https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/steps-task?view=azure-pipelines#common-task-properties
[10]: https://learn.microsoft.com/en-us/azure/devops/cli/auto-detect-and-git-aliases?view=azure-devops
[11]: https://jmespath.org/tutorial.html
[12]: https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/permissions?view=azure-devops#pipeline-permissions-reference
[13]: https://learn.microsoft.com/en-us/azure/devops/organizations/security/view-permissions?view=azure-devops&tabs=preview-page

[<](./index.md) | [<<](/index.md)
