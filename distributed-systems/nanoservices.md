---
title: Nanoservices
layout: default
nav_order: 6
parent: Distributed Systems
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Nanoservices

> Nanoservice is an Anti-pattern where a service is **too fine grained**.
Nanoservice is a service whose **overhead** (communications, maintenance etc.) **outweighs its utility**.

Effects:

- _poor performance_:  
serialization on caller,  translation to the underlying network protocol, traveling on the network, deserialization on the called process, encryption, authorization, routing, retries, firewalls
- _fragmented logic_: break what should have been a meaningful cohesive service into minuscule steps
- _overhead_
Fallacies of distributed computing: **bandwith is infinite** and **transport cost is zero**.

Examples:

- calculator service
- send notifications to users via SMS througjh a svc, better encapsulate as a package
- 3-Tier **SOA** anti-pattern: trying to dress up 3-tier architectures of yore in SOA clothing


[<](./index.md) | [<<](/index.md)
