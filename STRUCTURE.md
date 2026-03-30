---
nav_exclude: true
search_exclude: true
---

# Repository Structure

> Full directory tree of the documentation repository. Max depth: 4 levels below README.

```text
Tutorial/
├── .gitattributes
├── .gitignore
├── .markdownlint.json
├── _config.yml
├── _includes/
│   └── mermaid_config.js
├── assets/
│   └── js/
│       ├── mermaid.min.js
│       └── mermaid.min.js.map
├── CHANGELOG.md
├── CLAUDE.md
├── CONTRIBUTING.md
├── CONTRIBUTORS.md
├── index.md
├── LICENSE
├── README.md
├── STRUCTURE.md
├── ai/
│   ├── index.md
│   └── slms.md
├── architecture/
│   ├── ddd.md
│   ├── design-patterns.md
│   ├── domain-strength.md
│   ├── index.md
│   ├── modular-monolith.md
│   ├── principles.md
│   ├── solid.md
│   ├── structurizr.md
│   └── uml.md
├── azure/
│   ├── lectures/
│   │   ├── hybrid-infrastructure.md
│   │   └── modernize-dotnet.md
│   ├── app-insights.md
│   ├── az-303.md
│   ├── az-900-summary.md
│   ├── cloud-concepts.md
│   ├── core-services.md
│   ├── cost-management.md
│   ├── dev-box.md
│   ├── durable-functions.md
│   ├── identity-and-governance.md
│   ├── index.md
│   ├── legend.md
│   ├── osi.md
│   ├── resources.md
│   ├── security.md
│   ├── solutions-and-tools.md
│   └── table-storage.md
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
│   │   ├── localdb.md
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
│   │   ├── virtual-memory.md
│   │   ├── windows-11-shortcuts.md
│   │   └── wsl.md
│   ├── acronyms.md
│   ├── azure-pipelines.md
│   ├── ci-cd.md
│   ├── docfx.md
│   ├── git.md
│   ├── github-docs.md
│   ├── github-pages.md
│   ├── google-api.md
│   ├── handle-sysinternals.md
│   ├── index.md
│   ├── john-the-ripper.md
│   ├── markdown-unicode.md
│   ├── mobile.md
│   ├── nuget.md
│   ├── visual-studio.md
│   └── yaml.md
├── distributed-systems/
│   ├── azure-services.md
│   ├── distributed-tracing.md
│   ├── docker.md
│   ├── index.md
│   ├── kafka.md
│   ├── kubernetes.md
│   ├── microservices-architecture.md
│   ├── microservices-dotnet.md
│   ├── nanoservices.md
│   ├── service-fabric.md
│   ├── signalr.md
│   ├── websockets.md
│   └── zeromq.md
├── dotnet/
│   ├── aspnet/
│   │   ├── auth0.md
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
│   │   ├── async-await.md
│   │   ├── background-foreground-threads.md
│   │   ├── correlation-manager.md
│   │   ├── index.md
│   │   ├── managed-threads.md
│   │   ├── thread-local-storage.md
│   │   ├── thread-pool.md
│   │   ├── thread-synchronization.md
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
│   ├── build/
│   │   ├── dotnet-cli.md
│   │   ├── editorconfig.md
│   │   ├── global-json.md
│   │   ├── index.md
│   │   ├── msbuild.md
│   │   ├── nuget.md
│   │   └── tfms.md
│   ├── fwks-libs/
│   │   ├── index.md
│   │   └── polly.md
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
│   ├── knockoutjs.md
│   ├── npm.md
│   ├── pwa.md
│   ├── redux.md
│   └── webpack.md
├── testing/
│   ├── index.md
│   ├── mstest.md
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
