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
- 3-Tier SOA anti-pattern: trying to dress up 3-tier architectures of yore in SOA clothing

[<<](../SOA.md)
|
[home](README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki)