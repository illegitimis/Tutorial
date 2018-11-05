# Microservices Architecture

Microservices Architecture pluralsight [![Microservices Architecture pluralsight](https://img.shields.io/badge/Pluralsight-course-lightgrey.svg)](https://app.pluralsight.com/library/courses/microservices-architecture/table-of-contents)


## services
+ services are **stateless**. No knowledge about previous requests is needed. All info about, customer, client type, previous interaction must be contained into the current request
+ interface contracts and backward compatibility

## Microservices
+ small service with a **single purpose**
+ **lightweight** communication mechanism, client/service to service
+ **technology agnostic** API, open protocol (like http rest)
+ has **its own** data storage
+ independently changeable/deployable: no upgrade of a single service will affect any interaction within the system
+ transactions are likely to be completed in a distributed fashion, by multiple pieces of software
![](https://g7xqqg.by3302.livefilestore.com/y4mM1Fa_CB3EE-CmgJq3TFUTmXdV3opFhbxt22QZXf6yoC0aEVGTEtMtfMopxrPgyxO6AJpAAnBl_gULXGCC6mCBQza1638iG9nYYiDqI69neYxlRttEMwLXZIql3nu_GpmFIgxpgGX9nCR-YTXgVZtBxN3gkYijNZ-ClkZhgMnXdXOfy3IdHgeMO9NcbeZ44WpzOSt55IgqeJh-z91Xfay8A?width=501&height=260&cropmode=none)
+ **high cohesion**: single responsibility principle and oop encapsulation, single thing done well.
![](https://hiqn5q.by3302.livefilestore.com/y4m-4jSFHJrEVLS0UkKEiqqhSH4abhQeJM4KaKdyyyc3RHSjdCRxLyZPQVHLfcDYgOgrPPgdqDf5xhS-WLqKR4E1arX8dngbYp0itlzKAiQst7jcwx-9cHco1ebN8AkLQ4QFt65FigW1gS4upFjcVZMK0oOukOfa4ZWcu94zFD0A64xymp3hnwdwMFw0rP0IexCnrxNLf9a6IZP_bIF-dRi3w?width=968&height=342&cropmode=none)
+ **autonomous**: a change in one microservice won't force a change in another, _loose coupling oop fulfillment_.
  - Honor contracts from one version to another, independently changeable & deployable.
  - Async communication with events publishing, notify of completion. 
  - _Focus on technology agnostic_ and not on client libraries. 
  - _Fixed and agreed interfaces_.
  - Shared models, clear input and output.
  - Avoid _chatty services_ and *sharing databases* between services.
![](https://jxhseg.by3302.livefilestore.com/y4m31-GeEimCISRH6m4QhyUNx-s9P_cD7nIbw2MAP9BLXdtrKE-NXi-D1BdO5OMTmi8DOKyfvANcGM2Ilnb8VUBXKctakGrh9AHOUg6ZJFSA9zDJEhln1Dv6kWDFIZy2_oOEfM9qw4JJxj1TOwNHo0qSwYwGp5WzXUbBoFyz2yHwnbgYpYhn0JD3WUnZRNiZ6DYxskFYH7Su0W5oyrvaA03vA?width=744&height=318&cropmode=none)
+ **versioning and ownership** 
  - each teams owns and is reponsible to make autonomous, agree on contracts, maintain long term, communicate data and contract requirements. 
  - When breaking changes occur you could have concurrent versions, slowly negotiate migrations. 
  - Semantic versioning: `major.minor.patch`. _Patch increase_ on **defect**, _minor increase_ if **backward compatible**, _major increase_ if **contract change**. 
![](https://wowttq.by3302.livefilestore.com/y4ms4cJyQrdMXkzIba3FRP-QdDi_Cr8TseuGdEtHXgP1W0MU9OKxj6JYcsOyQ3sXzrLdEaZnxIhHomULUhvWqCRYdJ0u4fCWVS7YbPpPx7rUnYqdcVYVzZB9JsiQHPwsz1n0bjJ_dZvzz8MUiXaZcHPedDPlut-RZUg0iiOtbTK015v-kGBBdqUz00atmdw4XU-bKKLoDscmUglQRTDdhrwtw?width=446&height=337&cropmode=none)
+ **business domain centric**: should represent a business function/domain. 
  - bounded context from ddd, identify boundaries or **seams**. Identify business domains in a coarse manner.
  - responsive to business change. Review subgroups of business functions as areas, review benefits of splitting further. Fix incorrect boundaries by merging or splitting. 
![](https://tcytqq.by3302.livefilestore.com/y4m9LtqiYH1URb0IGJlUooEKCuZH4ZAemUVjucYJZ024CuegKLCTgxTJWYQ-G4831UJIT9oe443FFH2MOxDm6ur4BaSMAgxtvjWeGA2cevugsafaVwE8SGe_gxFskLClfz3Dq7X9jETazX75voCvOe-xdqHoP1lAcxKwUCaDcJ_9wdp9yW1sBwfCiEYO_ISxyBdiwcrYuN0csMdEl--cTRs1A?width=968&height=341&cropmode=none)
+ **resilience**, embrace failure when it happens, **degrading functionality** or offering **defaults**. Many moving parts, we can't have one bad downstream system influence the whole.  
  - Design must be done for _known failures_. **Fail and recover fast**, no impact for end user. 
  - Use timeouts for interconnected systems. Different thresholds for communication type, s2c or s2s. 
  - Handle network outages differently. Network errors/unavailability, internet delays.
+ **observable**: quick deployment requires feedback. data used for planning and scaling. see system health. 
  - **central monitoring**: monitor cpu, host memory and disk usage in real time. expose some metrics: svc response times and timeouts, number of exceptions. you can expand to business data like no orders and average time from basket to timeout, collect and aggregate data, compare data across servers, trend visalisation and trigger alerts on some conditions. `Nagios/PRTG/Load balancers/New Relic.` 
  - **central logging**: log means info/story, monitor means collecting metrics. When to log: startup/shutdown, code path milestones. What: requests, responses and decisions, timeouts, exceptions. Structured logging: level, date and time, **correlation id**, service name and instance. Strongly typed model and traceable distributed transactions. `Elastic Log/Log stash/Splunk/Kibana/Graphite`. Serilog pushes and raises events against the centralised monitoring tool. 
+ **automation**: manual regression testing, integration feedback on check-in. CI/CD. Each microservice with its own CI build. CD with central control panel and VS integration.

## monolith
+ all modules packed together, no division, tightly coupled, intertwined
+ keeps growing as long as you add app functionality, no restriction in size
+ scaling implies duplication of the whole

| Typical eCommerce |  |
|--------------|-----|
| **monolith** | ![](https://vbp2kg.by3302.livefilestore.com/y4maefbFKJEPiUaYXT-nqQiAKoLY2c-jo_T_Vyj5MUm-XuiO7kTlTqXi6J_SPh1bMzJYtF43vpBMVb8Mi2J0vF22hWZiSSENDJ0OPIM8HTPET7te4dmjPujLctCyd2WaRYZo6-PVea1pRtBGiKE5aO0F-nzHD68Lesmut-SLprhAGBL801u6nH1pMKrsZZsDrdXL5dqxbbwlxZBiJmOFGbu2w?width=849&height=595&cropmode=none) |
| **microservice** | ![](https://uz5oia.by3302.livefilestore.com/y4mwpYOLH51_DGJjNMVJ_LjgFJxw_T4oxelkCQVgCAPYJcHReu4M4CMze0qhfr7DYtcbaL23Bg0YjbZcI4LjLVRAoBGUlLOk6T8fQQmSrll8j32Lw7cNQSjrlFv5gc_cqbqNC9ybP0IzArKRzkObl3g8qeY-1Cf57fy_VwcMLBiOGfTvBc1moE1NmJoeC1SmSPiEcwfkRrDYjhXJIX0Skokdw?width=740&height=530&cropmode=none) |

## Microservices technology

Sync or async? Both. RPC: distributed client server programs. vs Open protocols like REST/JSON, or Stomp? ATOM uses http to propagate events. message queuing protocol for async, decouples service and client, also publisher and subscriber since it's event based. Queue is another point of failure.

![](https://6ebvoa.by3302.livefilestore.com/y4mSeeVFYRSCCPf8DeATPpm3crLyd23VzgCm5iillg2XuDOf-5niAf7UoRJ1GiqLdKwgKq8-ZgRn-IozdPyDU5G56SiMeWfJ5o5gCvAjMef_3P36tHEyKFLmbrY3Zb7ym2lhcBo5_j7K4LKUDSAYVmbinpkaI1FuaIoTc0-EGIvDldG39FhIQ77Jnyt4hRS-c4AH_HrbdVqxOYUOboXVcPbvA?width=1000&height=360&cropmode=none)

**Virtualization**: PAAS with Azure/AWS/vSphere/Google Cloud.
**Containers**: Docker/Rocker/Glassware. Do not run an entire OS, just minimal. Single service per container.
**Registry and discovery**: host, port and version go to a svc registry db. Register on startup, deregister svc on failure, makes it self heal. Third party registration: man in he middle detects new instances and adds them to the svc registration database. _Client side discovery_: clients connect directly to that db or _Server side discovery_: a gateway or load balancer does the svc reg db queries.
**Scaling**. How to scale up? Either create multiple instances of the same or add resources to existing. If cloud then PAAS handles automated or on demand scaling options. 
**API gateway**: single point of entry into the SOA, manages caching and load balancing. Single interface to many services, routes to dynamic locations, may handle security or delegate to some security service or have some sort of security at each service level.

![](https://fpneua.by3302.livefilestore.com/y4mf9rb9J-3DSfOKD6Rd0TVKclfrIXbg1_WAvDt1GkXkbbJnLibsrf3e5PggEboGtdnJEAN9GumFG9surNClVL_msU9yQy0rX8m8jJCVl9g21P1ZArbOn8eaaVNnvTG8j1X2u0syXmBZ83FycclSdAp04-3UQlOh2xS9zx85pRXO1ULonXcr7PbM1mBOLMl37O85Js6KZVZIhG7nIpUk9XX4g?width=554&height=383&cropmode=none)

## Design

|  | Brownfield | Greenfield |
|--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Meaning | Migrate existing system, likely monolithic, lacks microservices design principles | Build from scratch |
| Approach | Identify seams, separation that reflect domains.  Start modularising domains and move code incrementally. Tidy up a section per release. Existing functionality needs to remain intact. Run unit/integration tests to validate change. Keep reviewing and identify bounded contexts | System boundaries will evolve. Start off with a monolith, develop areas into modules. Refine and refactor, split further when required. Promote shared libraries to a service. Review microservice principles at each stage. |
| Code Migration | Code organized into bounded contexts, Have clear interfaces between each. Code for each business domain is in one place. Start off with one, switchable, prioritize by risk/least dependency, incremental.  | ![pic1](https://uz5lia.by3302.livefilestore.com/y4mC0L-qFTh6dNesufI43oPPKr9kHOl1s2P56pogLZP3jYLpoFFQOvpwvDTF0yiCjTOf2eGR_5qelkr4q2F_M173_XQk0t04UGMQ7nYNZ1T7lY6R-lET6qBamPVk_FcSLUeYrtypzSCBUcHSJWbGkRrkaSh3SyPZ30eAktjYg_8aM7qGi12cLBBuaQ93-x3QrIY9MPElqaPK0po8CkqcrErMA?width=710&height=497&cropmode=none) |
| Database migration | Avoid shared databases. Relate tables to code seams. Tables that link across seams: API calls that can fetch data for a relationship. Data referential integrity: api call instead of sql cascade. | ![pic 2](https://g7x8qg.by3302.livefilestore.com/y4ms1v48EN7GGa-GhLXYoqhaF-WfPKrmnSTxUo_6HGLITUFPSpsSP1L0HVLOyk-F4pGwDmtNXbkdHrSmKQ2GeFuBG7J1BExBiF0Wr32nLWmjwPbrD9dmlxVtzlafp6JES7fOaEfJ_v_734Uaq0euV2N56Q0oQ2iEfxdy5SHWsZfDJFaAiZeB56ADcMpYJSOkXPU8JqRn6ILAeLku6O1C7jRPw?width=733&height=523&cropmode=none) |
| Transactions | Complex if spanning multiple microservices. Example: Orders-Promotions-Accounts-Products + TransactionManager.  Fail options: try again (cache it), abort (create undo transaction) TransactionManager software: delay, two phase commit, potential bottleneck. Distributed transaction compatibility: notify monolith of completion.  | ![pic 3](https://vbpzkg.by3302.livefilestore.com/y4mWzaPsKD43tdoZ4RnodLKtzLL1TrWdZtkf8tqVZzilqSXJh-2DOPkd9CsE27d6u9y-_-1zpc1wOA_NcNfh8lQUZnC82OIgO4eJKBtgr-CbMkDbBRxvYzFVnZIuiGXwYbVtqjkF9FcmOcMUNFqqGzKpjLL44DtMWnlr0HZJII9FU36AN47nKbIIEc5yrHEAQLOwlg0ddXu8H0c7VpvuK0WdQ?width=589&height=591&cropmode=none) |
| Reporting | No central database. Joins? Data pumps and a specialized ReportingService. Consolidation environment with a nightly job.  | ![pic 4](https://slcgww.by3302.livefilestore.com/y4myXm1Pa64HpHG7IO9QsSOg__pXCAI6GznxzDJHwQxgrcTRwYLcMlYL-8UheJVjdlwxMr_iOr5MqCIAPAZTg5Zu-SafYh_3qALMt5GM57jkwm3sUTZAUYQsnDICoaZVueHzQ_ZAG7UMAx1-h7sE-_dL1zx-RXowsM7eRg0zM2qNAQx7m-WXQRhaV_a4kuFGHHDh1rEWbM32hHyiOiWnjC62A?width=469&height=485&cropmode=none) |

[<<](../soa.md) | [home](../../README.md)