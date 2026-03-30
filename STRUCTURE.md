---
nav_exclude: true
search_exclude: true
---

# Repository Structure

> Full directory tree of the documentation repository. Max depth: 4 levels below README.

```text
Tutorial/
├── architecture/
│   ├── ddd.md
│   ├── design-patterns.md
│   ├── domain-strength.md
│   ├── index.md
│   ├── principles.md
│   ├── solid.md
│   └── uml.md
├── azure/
│   ├── learn/
│   │   ├── 114-tour.md
│   │   ├── 115-account.md
│   │   ├── 117-kc.md
│   │   ├── 125A-kc.md
│   │   ├── 125B-kc.md
│   │   ├── 133-region.md
│   │   ├── 136-kc.md
│   │   ├── 1-lp-az-900.md
│   │   ├── 218-kc.md
│   │   ├── 227-kc.md
│   │   ├── 237-kc.md
│   │   ├── 249-kc.md
│   │   ├── 2-lp-az-900.md
│   │   ├── 317-kc.md
│   │   ├── 327-kc.md
│   │   ├── 336-kc.md
│   │   ├── 347-kc.md
│   │   ├── 359-kc.md
│   │   ├── 367-kc.md
│   │   ├── 3-lp-az-900.md
│   │   ├── 417-kc.md
│   │   ├── 428-kc.md
│   │   ├── 43-Protect-virtual-networks-by-using-Azure-firewall.md
│   │   ├── 44-Protect-from-DDoS-attacks-by-using-Azure-ddos-protection.md
│   │   ├── 45-Filter-network-traffic-by-using-nsg.md
│   │   ├── 46-ex-vm-nsg.md
│   │   ├── 47-combine-az-svc-nsec.md
│   │   ├── 48-Knowledge-check.md
│   │   ├── 49-summary.md
│   │   ├── 4-lp-az-900.md
│   │   ├── 511-intro.md
│   │   ├── 512-auth.md
│   │   ├── 513-aad.md
│   │   ├── 514-mfa-ca.md
│   │   ├── 515-kc.md
│   │   ├── 516-summary.md
│   │   ├── 521-intro.md
│   │   ├── 522-rbac.md
│   │   ├── 523-rsrc-locks.md
│   │   ├── 524-ex-del-protect.md
│   │   ├── 525-tags.md
│   │   ├── 526--policy.md
│   │   ├── 527-ex-restrict-geo.md
│   │   ├── 52B-kc.md
│   │   ├── 52C-summary.md
│   │   ├── 531-intro.md
│   │   ├── 532-compliance-terms.md
│   │   ├── 538-kc.md
│   │   ├── 539-summary.md
│   │   ├── 5-lp-az-900.md
│   │   ├── 617-kc.md
│   │   ├── 626-kc.md
│   │   ├── 6-lp-az-900.md
│   │   ├── akv.pass.md
│   │   ├── az900.md
│   │   ├── az900-kc.md
│   │   ├── service-models.md
│   │   ├── smg.md
│   │   ├── tocm.md
│   │   ├── vnet.settings.md
│   │   └── vpn.gateway.fndmnt.md
│   ├── lectures/
│   │   ├── hybrid-infrastructure.md
│   │   └── modernize-dotnet.md
│   ├── lctrs/
│   │   ├── hybrid.infra.md
│   │   └── mdrnz.net.md
│   ├── pages/
│   │   ├── app.insight.md
│   │   └── osi.md
│   ├── app-insights.md
│   ├── az.md
│   ├── az-900-summary.md
│   ├── cloud-concepts.md
│   ├── core-services.md
│   ├── cost-management.md
│   ├── identity-and-governance.md
│   ├── index.md
│   ├── learn.md
│   ├── lectures.md
│   ├── legend.md
│   ├── osi.md
│   ├── resources.md
│   ├── security.md
│   └── solutions-and-tools.md
├── data/
│   ├── nosql/
│   │   ├── mongo/
│   │   │   ├── articles.md
│   │   │   ├── index.md
│   │   │   ├── recipes.md
│   │   │   └── schema.md
│   │   ├── base.md
│   │   ├── cap.md
│   │   ├── cosmos.md
│   │   ├── document-db.md
│   │   ├── document-db-cheat-sheet.md
│   │   ├── graph-db.md
│   │   ├── index.md
│   │   └── m101n.md
│   ├── sql/
│   │   ├── scripts/
│   │   │   ├── instnwnd.sql
│   │   │   └── instpubs.sql
│   │   ├── acid.md
│   │   ├── connection-pool.md
│   │   ├── dao-vs-repository.md
│   │   ├── db-command.md
│   │   ├── foreign-key-mapping.md
│   │   ├── index.md
│   │   ├── indexes.md
│   │   ├── mysql.md
│   │   ├── postgresql.md
│   │   ├── primary-keys.md
│   │   ├── referential-integrity.md
│   │   ├── samples.md
│   │   ├── service-broker.md
│   │   ├── string-search-stored-proc.md
│   │   ├── table-schema.md
│   │   ├── temporary-tables.md
│   │   └── views.md
│   └── index.md
├── devops/
│   ├── os/
│   │   └── virtual-memory.md
│   ├── acronyms.md
│   ├── ci-cd.md
│   ├── git.md
│   ├── github-docs.md
│   ├── google-api.md
│   ├── index.md
│   ├── john-the-ripper.md
│   ├── mobile.md
│   ├── nuget.md
│   ├── visual-studio.md
│   └── yaml.md
├── distributed-systems/
│   ├── azure-services.md
│   ├── docker.md
│   ├── index.md
│   ├── kafka.md
│   ├── microservices-architecture.md
│   ├── microservices-dotnet.md
│   ├── nanoservices.md
│   ├── signalr.md
│   ├── websockets.md
│   └── zeromq.md
├── dotnet/
│   ├── aspnet/
│   │   ├── attributes.md
│   │   ├── authorization.md
│   │   ├── blazor.md
│   │   ├── commands.md
│   │   ├── index.md
│   │   ├── middleware.md
│   │   ├── mvc.md
│   │   ├── openid-connect.md
│   │   ├── razor.md
│   │   └── web-app-mvc6-efcore-angular.md
│   ├── data-access/
│   │   ├── automapper.md
│   │   ├── ef-core.md
│   │   ├── entity-framework.md
│   │   └── index.md
│   ├── language/
│   │   ├── anonymous-types.md
│   │   ├── co-contra-variance.md
│   │   ├── collections-performance.md
│   │   ├── delegates.md
│   │   ├── events.md
│   │   ├── exceptions.md
│   │   ├── immutable-types.md
│   │   ├── index.md
│   │   ├── interfaces.md
│   │   ├── lambdas.md
│   │   ├── managed-cpp-cli.md
│   │   └── rx.md
│   ├── parallelism/
│   │   ├── background-foreground-threads.md
│   │   ├── index.md
│   │   ├── managed-threads.md
│   │   ├── thread-local-storage.md
│   │   ├── thread-pool.md
│   │   ├── threads-vs-processes.md
│   │   ├── threads-vs-tasks.md
│   │   ├── tpl-collections.md
│   │   ├── tpl-dataflow.md
│   │   └── ui-threads.md
│   ├── runtime/
│   │   ├── app-domains.md
│   │   ├── assemblies.md
│   │   ├── clr.md
│   │   ├── finalize.md
│   │   ├── garbage-collection.md
│   │   └── index.md
│   └── index.md
├── javascript/
│   ├── angular/
│   │   ├── angular2.md
│   │   ├── angular4.md
│   │   ├── angularjs.md
│   │   ├── fundamentals.md
│   │   └── index.md
│   ├── css.md
│   ├── index.md
│   ├── npm.md
│   ├── pwa.md
│   ├── redux.md
│   └── webpack.md
├── testing/
│   ├── index.md
│   ├── nunit.md
│   └── xunit.md
└── web-services/
    ├── autorest.md
    ├── caching.md
    ├── calling-rest-apis.md
    ├── etag.md
    ├── graphql.md
    ├── hateoas.md
    ├── http.md
    ├── httpclient.md
    ├── index.md
    ├── swagger.md
    ├── webapi.md
    ├── webapi-course.md
    ├── webapi-upload-download.md
    └── webapi-versioning.md
```
