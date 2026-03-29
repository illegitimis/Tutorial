# Azure

+ [Azure Cosmos DB](./nosql/cosmos.md) 
  [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./nosql/cosmos.md)
+ Azure Stack: An extension of Azure [1] white paper
+ Modern Muse. Migrating an open source PaaS solution to Azure [2] pdf, June 2017

## Glossary

+ docker ce edge down [3]
+ docker id log [4]
+ affinity, round robin, sticky session
+ ingress controller
+ kubectl get services -w
+ kubectl {verb} {noun}
+ azure container service AKS vs `docker compose`
+ orchestrator kubernetes
+ shell.azure.com
+ rm blog [5], ws [6], kube-toolkit [7]
+ federation services for kubernetes, health probes ?
+ hypervisor
+ draft, helm, brigade
+ azure app service & ACI azure container instance
+ cluster, node, pod, shard
+ web app 4 containers from azure portal
+ autoscale, up-vertical and out-horizontal
+ brendab burns desifn distributed systems 2017 [8] Patterns and Paradigms for Scalable, Reliable Services, samples [9]
+ kubernetes-the-hard-way [10]
+ bzass/containerslab [11]
+ Microsoft Docs: Tutorial Kubernetes Deploy Cluster [12]
+ ms docs 1 [13], 2 [12], 3 [14], 4 [15], 5 [16]

```sh

msft@Azure:~$ az provider show -n Microsoft.Network -o table
msft@Azure:~$ az provider show -n Microsoft.Storage -o table
msft@Azure:~$ az provider show -n Microsoft.Compute -o table
az provider register -n Microsoft.ContainerService
az provider show -n Microsoft.ContainerService
az group create --name MsftEventsAcpopescuGroup --location "West US 2"
az aks create --resource-group MsftEventsAcpopescuGroup --name MsftEventsAcpopescuCluster --node-count 1 --generate-ssh-keys
```

[1]: https://azure.microsoft.com/mediahandler/files/resourcefiles/643b5d13-a28f-46e1-a215-4cde55435f97/Azure-Stack-white-paper-v3.pdf
[2]: https://1drv.ms/b/s!AnIyfO51kH7NlWAMoBEvw8wNJOmZ
[3]: https://store.docker.com/editions/community/docker-ce-desktop-windows
[4]: https://cloud.docker.com/swarm/dockeracpopescu/dashboard/onboarding/cloud-registry
[5]: https://radu-matei.com/categories/kubernetes/
[6]: https://github.com/radu-matei/workshop
[7]: https://github.com/radu-matei/kube-toolkit
[8]: https://azure.microsoft.com/mediahandler/files/resourcefiles/baf44271-3870-454f-868c-23d48e7672cb/Designing_Distributed_Systems.pdf
[9]: https://github.com/brendandburns/designing-distributed-systems
[10]: https://github.com/kelseyhightower/kubernetes-the-hard-way
[11]: https://github.com/bzass/containerslab
[12]: https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster
[13]: https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest
[14]: https://www.microsoftazurepass.com/Redeemed
[15]: https://www.microsoftevents.com/profile/form/index.cfm?PKformID=0x3795346abcd
[16]: https://portal.azure.com/#@msfteventsacpopescuoutlook.onmicrosoft.com/blade/HubsExtension/Resources/resourceType/Microsoft.Resources%2Fsubscriptions%2FresourceGroups


[<<](./index.md) | [home](../README.md)
