# Domain Driven Design

## Books

- 2003 - Eric Evans - Domain-Driven Design - Tackling Complexity in the Heart of Software, [gdrds](https://www.goodreads.com/book/show/179133.Domain_Driven_Design), [1drv](https://1drv.ms/b/s!As0cxZAk26SzjMBp0PF88ubDcye0PA)
- 2013.VaughnVernon.**Implementing Domain-Driven Design**, [amazon](https://www.amazon.com/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577/ref=s9u_psimh_gw_i2?_encoding=UTF8&fpl=fresh&pd_rd_i=0321834577&pd_rd_r=DSAP65H1JA0MXN8BX491&pd_rd_w=fHcI2&pd_rd_wg=kOyxf&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=E11CJ6Q3S8VB3B0KQC41&pf_rd_t=36701&pf_rd_p=2a4fafb6-9fdc-425a-aee8-c82daa7b18ed&pf_rd_i=desktop), [1DRV](https://1drv.ms/b/s!As0cxZAk26SzjMBeDqClRqeMZggYfA)
- 2015.1ed.Millett.Tune.Patterns, Principles and Practices of Domain-Driven Design [1drv](https://1drv.ms/b/s!As0cxZAk26SzjMBorG7WxjcpxYpRKg)
- 2016.VaughnVernon.**DomainDrivenDesignDistilled**, [1drv](https://onedrive.live.com/embed?cid=B3A4DB2490C51CCD&resid=B3A4DB2490C51CCD%21204895&authkey=AJxhhLaCMUQdqEY&em=2)
- [Strengthening your domain](./domain-strength.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./domain-strength.md) series by Jimmy Bogards

## Videos and other online material

- [TechEd Europe 2014: Architecting and Implementing Domain-Driven Design Patterns with Microsoft .NET](https://channel9.msdn.com/Events/TechEd/Europe/2014/DEV-B211)
- [VaughnVernon/IDDD_Samples_NET](https://github.com/VaughnVernon/IDDD_Samples_NET)
- [naa4e SDD](http://sddconf.com/brands/sdd/library/Architecting_Implementing_DDD_Patterns.pdf)
- [Master's thesis, CS Department, University of Copenhagen, spring 2009, Domain-driven design in action: Designing an identity provider](http://www.diku.dk/forskning/performance-engineering/Klaus/speciale.pdf)
- [DDD insights blog](http://effective-ddd.blogspot.ro/2015/12/strategic-domain-driven-design.html)
- [Colorado slides](https://www.cs.colorado.edu/~kena/classes/5448/f12/presentation-materials/roads.pdf)
- [IDDD excerpt](http://ptgmedia.pearsoncmg.com/images/9780321834577/samplepages/0321834577.pdf)
- [IDDD excerpt 2](https://books.google.ro/books?id=X7DpD5g3VP8C&pg=PA1&hl=ro&source=gbs_toc_r&cad=4#v=onepage&q&f=false)
- [Tackling Business Complexity in a Microservice with DDD and CQRS Patterns](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/microservice-ddd-cqrs-patterns/) msdn
- [eShopOnContainers](https://github.com/dotnet-architecture/eShopOnContainers/tree/master/src/Services/Ordering) sample `Ordering API`
- [jbogard/MediatR](https://github.com/jbogard/MediatR) Simple, unambitious mediator implementation in .NET
- A [.NET implementation of Domain Driven Design (DDD) sample application](https://github.com/SzymonPobiega/DDDSample.Net) based on Eric Evans' examples included in his great book.
- [ndddsample](https://code.google.com/archive/p/ndddsample/) on google code


## Principles

- model _a single sub-domain at a time_, focus on _autonomous pieces_ of the domain, resulting software is closer to business understanding, often no side effects
- It describes _independent_ problem areas as **Bounded Contexts** (each Bounded Context correlates to a microservice)
- _avoid chatty_ communications between microservices
- you should create a _boundary_ around things that need _cohesion_. It is similar to the [Inappropriate Intimacy](https://sourcemaking.com/refactoring/smells/inappropriate-intimacy) code smell when implementing classes. If _two microservices need to collaborate a lot with each other_, they _should probably be the same microservice_.
- **Persistence Ignorance** (PI): classes modeling the _business domain_ should not be impacted by how they might be persisted. Thus, their design should reflect as closely as possible the ideal design needed to solve the business problem at hand, and should not be tainted by concerns related to how the objects’ state is saved and later retrieved. Some common violations include domain objects that _must inherit from a particular base class_, or which _must expose certain properties_. Sometimes, the persistence knowledge takes the form of **attributes that must be applied to the class**, or support for only certain types of collections or property visibility levels. There are degrees of persistence ignorance, with the highest degree being described as _Plain Old CLR Objects_ (POCOs) in .NET, and Plain Old Java Objects (POJOs) in the Java world.

[<<](../design.md) | [home](../../README.md)