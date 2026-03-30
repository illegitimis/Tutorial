---
title: Continuous Delivery
layout: default
nav_order: 2
parent: DevOps
last_modified_date: 2026-03-31 00:00:00 +00:00
---

# Continuous Delivery

- objective is to get around the **OODA** loop (Observe – Orient - Decide – Act) faster
- teams should be organised around microservices with a separate platform team exposing an API that all other teams use
- DevOps should be a reorganization of teams, contrary to the tendency that companies are organized in teams, product managers, developers, QA, etc., and getting something done requires a lot of meetings, a kind of waterfall approach that takes too long.
- end-to-end process of developing and releasing software is often long and cumbersome, it involves many people, departments and obstacles
- white paper continuous-delivery-maturity-model [1], 2014

![maturity model](https://res.infoq.com/articles/Continuous-Delivery-Maturity-Model/en/resources/fig1large.jpg)

[1]: https://developer.ibm.com/urbancode/docs/continuous-delivery-maturity-model/

## Deployment Strategies

**Canary Release** [2]: route a small percentage of traffic to the new version before full rollout \
**Blue-Green Deployment** [3]: maintain two identical environments; blue is the easily switchable _hot-standby_ \
**Evolutionary Database Design** [4]

Engineering Fundamentals Playbook on _Continuous Delivery_ [5] \
`App Service` auto swap [6] \
**Deployment rings** [7] \
Kubernetes rolling update [8]

[2]: https://martinfowler.com/bliki/CanaryRelease.html
[3]: https://martinfowler.com/bliki/BlueGreenDeployment.html
[4]: https://englishplusplus.jcj.uj.edu.pl/texts/evolutionary-database-design/fulltext/index.html
[5]: https://microsoft.github.io/code-with-engineering-playbook/CI-CD/continuous-delivery/
[6]: https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots?tabs=portal#configure-auto-swap
[7]: https://learn.microsoft.com/en-us/training/modules/manage-release-cadence/?view=azure-devops
[8]: https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/

[<](./index.md) | [<<](/index.md)
