# Azure

+ [Azure Cosmos DB](./nosql/cosmos.md) 
  [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./nosql/cosmos.md)
+ [Azure Stack: An extension of Azure](https://azure.microsoft.com/mediahandler/files/resourcefiles/643b5d13-a28f-46e1-a215-4cde55435f97/Azure-Stack-white-paper-v3.pdf) white paper
+ Modern Muse. [Migrating an open source PaaS solution to Azure](https://1drv.ms/b/s!AnIyfO51kH7NlWAMoBEvw8wNJOmZ) pdf, June 2017

## Glossary

+ docker ce edge [down](https://store.docker.com/editions/community/docker-ce-desktop-windows)
+ docker id [log](https://cloud.docker.com/swarm/dockeracpopescu/dashboard/onboarding/cloud-registry)
+ affinity, round robin, sticky session
+ ingress controller
+ kubectl get services -w
+ kubectl {verb} {noun}
+ azure container service AKS vs `docker compose`
+ orchestrator kubernetes
+ shell.azure.com
+ rm [blog](https://radu-matei.com/categories/kubernetes/), [ws](https://github.com/radu-matei/workshop), [kube-toolkit](https://github.com/radu-matei/kube-toolkit)
+ federation services for kubernetes, health probes ?
+ hypervisor
+ draft, helm, brigade
+ azure app service & ACI azure container instance
+ cluster, node, pod, shard
+ web app 4 containers from azure portal
+ autoscale, up-vertical and out-horizontal
+ [brendab burns desifn distributed systems 2017](https://azure.microsoft.com/mediahandler/files/resourcefiles/baf44271-3870-454f-868c-23d48e7672cb/Designing_Distributed_Systems.pdf) Patterns and Paradigms for Scalable, Reliable Services, [samples](https://github.com/brendandburns/designing-distributed-systems)
+ [kubernetes-the-hard-way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
+ [bzass/containerslab](https://github.com/bzass/containerslab)
+ https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster
+ ms docs [1](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest), [2](https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster), [3](https://www.microsoftazurepass.com/Redeemed), [4](https://www.microsoftevents.com/profile/form/index.cfm?PKformID=0x3795346abcd), [5](https://portal.azure.com/#@msfteventsacpopescuoutlook.onmicrosoft.com/blade/HubsExtension/Resources/resourceType/Microsoft.Resources%2Fsubscriptions%2FresourceGroups)

```sh

msft@Azure:~$ az provider show -n Microsoft.Network -o table
msft@Azure:~$ az provider show -n Microsoft.Storage -o table
msft@Azure:~$ az provider show -n Microsoft.Compute -o table
az provider register -n Microsoft.ContainerService
az provider show -n Microsoft.ContainerService
az group create --name MsftEventsAcpopescuGroup --location "West US 2"
az aks create --resource-group MsftEventsAcpopescuGroup --name MsftEventsAcpopescuCluster --node-count 1 --generate-ssh-keys
```