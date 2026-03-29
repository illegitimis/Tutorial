# Repository Reorganization Design

## Overview

Reorganize a scattered collection of 200+ developer documentation files into a clean, hierarchical structure with a maximum tree height of 5 (README at level 0, deepest leaf at level 4). Apply consistent formatting conventions, markdownlint compliance, and semantic entity formatting across all files.

## Goals

- Maximum 4 levels of nesting below `README.md`
- Eliminate content overlap between categories
- Absorb thin categories into related larger ones
- Flatten Azure certification content into topic-based consolidated files
- Extract all binary content (PNGs, PDFs) into markdown
- Enforce consistent formatting conventions
- Lint all files with markdownlint (moderate strictness)

## Target Tree Structure

```
README.md                                    # L0 - root index
STRUCTURE.md                                 # L0 - full tree map
CLAUDE.md                                    # L0 - LLM context
.markdownlint.json                           # L0 - lint config
│
├── dotnet/                                  # L1
│   ├── index.md                             #   category hub
│   ├── language/                            # L2 - C# language features
│   │   ├── index.md
│   │   ├── delegates.md                     # L3
│   │   ├── events.md
│   │   ├── lambdas.md
│   │   ├── anonymous-types.md
│   │   ├── co-contra-variance.md
│   │   ├── collections-performance.md
│   │   ├── exceptions.md
│   │   ├── immutable-types.md
│   │   ├── interfaces.md
│   │   ├── managed-cpp-cli.md
│   │   └── rx.md
│   ├── runtime/                             # L2 - CLR, GC, assemblies
│   │   ├── index.md
│   │   ├── clr.md                           # L3
│   │   ├── garbage-collection.md
│   │   ├── finalize.md
│   │   ├── assemblies.md
│   │   └── app-domains.md
│   ├── aspnet/                              # L2 - ASP.NET + ASP.NET Core merged
│   │   ├── index.md
│   │   ├── mvc.md                           # L3
│   │   ├── razor.md
│   │   ├── openid-connect.md
│   │   ├── middleware.md
│   │   ├── authorization.md
│   │   ├── attributes.md
│   │   ├── blazor.md
│   │   ├── commands.md
│   │   └── web-app-mvc6-efcore-angular.md
│   ├── data-access/                         # L2 - ORM absorbed here
│   │   ├── index.md
│   │   ├── entity-framework.md              # L3
│   │   ├── ef-core.md
│   │   └── automapper.md
│   └── parallelism/                         # L2 - threads, tasks, TPL
│       ├── index.md
│       ├── managed-threads.md               # L3
│       ├── background-foreground-threads.md
│       ├── threads-vs-processes.md
│       ├── threads-vs-tasks.md
│       ├── ui-threads.md
│       ├── thread-pool.md
│       ├── thread-local-storage.md
│       ├── tpl-collections.md
│       └── tpl-dataflow.md
│
├── javascript/                              # L1
│   ├── index.md
│   ├── css.md                               # L2 - CSS absorbed as leaf
│   ├── pwa.md                               # L2
│   ├── npm.md                               # L2
│   ├── webpack.md                           # L2
│   ├── redux.md                             # L2
│   └── angular/                             # L2
│       ├── index.md
│       ├── fundamentals.md                  # L3
│       ├── angularjs.md
│       ├── angular2.md
│       └── angular4.md
│
├── architecture/                            # L1 - cross-cutting design
│   ├── index.md
│   ├── principles.md                        # L2 - OOP principles
│   ├── solid.md                             # L2
│   ├── ddd.md                               # L2
│   ├── domain-strength.md                   # L2
│   ├── design-patterns.md                   # L2
│   └── uml.md                               # L2
│
├── distributed-systems/                     # L1 - messaging + SOA merged
│   ├── index.md
│   ├── microservices-architecture.md        # L2
│   ├── microservices-dotnet.md              # L2
│   ├── docker.md                            # L2 - enriched with PNG content
│   ├── nanoservices.md                      # L2
│   ├── signalr.md                           # L2
│   ├── websockets.md                        # L2
│   ├── kafka.md                             # L2
│   ├── zeromq.md                            # L2
│   └── azure-services.md                    # L2 - SOA azure content
│
├── data/                                    # L1
│   ├── index.md
│   ├── sql/                                 # L2
│   │   ├── index.md
│   │   ├── acid.md                          # L3
│   │   ├── indexes.md
│   │   ├── connection-pool.md
│   │   ├── dao-vs-repository.md
│   │   ├── db-command.md
│   │   ├── foreign-key-mapping.md
│   │   ├── primary-keys.md
│   │   ├── referential-integrity.md
│   │   ├── service-broker.md
│   │   ├── string-search-stored-proc.md
│   │   ├── table-schema.md
│   │   ├── temporary-tables.md
│   │   ├── views.md
│   │   ├── samples.md
│   │   ├── mysql.md
│   │   ├── postgresql.md
│   │   └── scripts/                         # L3
│   │       ├── instnwnd.sql                 # L4 (max depth)
│   │       └── instpubs.sql
│   └── nosql/                               # L2
│       ├── index.md
│       ├── base.md                          # L3
│       ├── cap.md
│       ├── cosmos.md
│       ├── document-db.md
│       ├── document-db-cheat-sheet.md
│       ├── graph-db.md
│       ├── mongo/                           # L3 - sub-index
│       │   ├── index.md
│       │   ├── articles.md                  # L4 (max depth)
│       │   ├── recipes.md
│       │   └── schema.md
│       └── m101n.md
│
├── web-services/                            # L1 - REST, HTTP, APIs
│   ├── index.md
│   ├── http.md                              # L2
│   ├── hateoas.md                           # L2
│   ├── graphql.md                           # L2
│   ├── swagger.md                           # L2
│   ├── autorest.md                          # L2
│   ├── caching.md                           # L2
│   ├── etag.md                              # L2
│   ├── httpclient.md                        # L2
│   ├── calling-rest-apis.md                 # L2
│   ├── webapi.md                            # L2
│   ├── webapi-course.md                     # L2
│   ├── webapi-upload-download.md            # L2
│   └── webapi-versioning.md                 # L2
│
├── azure/                                   # L1 - flattened cert content
│   ├── index.md
│   ├── legend.md                            # L2 - glossary
│   ├── resources.md                         # L2
│   ├── cloud-concepts.md                    # L2 - LP1 consolidated
│   ├── core-services.md                     # L2 - LP2 consolidated
│   ├── solutions-and-tools.md               # L2 - LP3 consolidated
│   ├── security.md                          # L2 - LP4 consolidated
│   ├── identity-and-governance.md           # L2 - LP5 consolidated
│   ├── cost-management.md                   # L2 - LP6 consolidated
│   ├── az-900-summary.md                    # L2
│   ├── app-insights.md                      # L2
│   ├── osi.md                               # L2
│   └── lectures/                            # L2
│       ├── hybrid-infrastructure.md         # L3
│       └── modernize-dotnet.md              # L3
│
├── testing/                                 # L1 - was tdd
│   ├── index.md
│   ├── nunit.md                             # L2
│   └── xunit.md                             # L2
│
└── devops/                                  # L1 - tools + CI/CD
    ├── index.md
    ├── git.md                               # L2
    ├── github-docs.md                       # L2
    ├── ci-cd.md                             # L2
    ├── nuget.md                             # L2
    ├── visual-studio.md                     # L2
    ├── yaml.md                              # L2
    ├── google-api.md                        # L2
    ├── mobile.md                            # L2
    ├── john-the-ripper.md                   # L2
    ├── acronyms.md                          # L2
    └── os/                                  # L2 - OS absorbed here
        └── virtual-memory.md                # L3
```

## Merges and Absorptions

| Action | Source | Destination |
|--------|--------|-------------|
| Merge | `doc/ASP.md` + `doc/asp/` + `doc/netcore.md` + `doc/netcore/` | `dotnet/aspnet/` |
| Merge | `doc/messaging.md` + `doc/msg/` + `doc/soa.md` + `doc/soa/` | `distributed-systems/` |
| Absorb | `doc/orm.md` + `doc/orm/` | `dotnet/data-access/` |
| Absorb | `doc/CSS.md` | `javascript/css.md` |
| Absorb | `doc/CMS.md` | `dotnet/aspnet/index.md` (CMS list folded into ASP.NET hub) |
| Absorb | `doc/os.md` + `doc/os/` | `devops/os/` |
| Move | `doc/c#/automapper.md` | `dotnet/data-access/automapper.md` |
| Move | `doc/c#/rx.md` | `dotnet/language/rx.md` (Rx.NET, stays in .NET) |
| Drop | `doc/tools/mra.md` | Personal project (Movie Review Aggregator), not dev documentation |

## Azure Flattening

Consolidate 67 numbered learning modules into 6 topic-based files:

| Target File | Source Modules | Content |
|-------------|---------------|---------|
| `cloud-concepts.md` | `1-lp-az-900.md`, `114-tour.md`, `115-account.md`, `117-kc.md`, `tocm.md`, `service-models.md`, `125A-kc.md`, `125B-kc.md`, `133-region.md`, `136-kc.md` | Cloud models, service models, regions, availability zones |
| `core-services.md` | `2-lp-az-900.md`, `218-kc.md`, `227-kc.md`, `237-kc.md`, `249-kc.md` | Compute, networking, storage, database services |
| `solutions-and-tools.md` | `3-lp-az-900.md`, `317-kc.md`, `327-kc.md`, `336-kc.md`, `347-kc.md`, `359-kc.md` | IoT, AI, serverless, DevTools, monitoring |
| `security.md` | `4-lp-az-900.md`, `akv.pass.md`, `43-*.md`, `44-*.md`, `45-*.md`, `46-*.md`, `47-*.md`, `48-*.md`, `49-*.md` | Firewall, DDoS, NSGs, Key Vault, defense in depth |
| `identity-and-governance.md` | `5-lp-az-900.md`, `511-*.md` through `539-*.md` | AAD, MFA, RBAC, resource locks, tags, policy, compliance |
| `cost-management.md` | `6-lp-az-900.md`, `617-kc.md`, `626-kc.md` | Pricing, TCO, cost optimization |

Standalone files `az900.md` and `az900-kc.md` merge into `az-900-summary.md`.

## Non-Markdown Content Handling

### Docker PNGs (9 files in `todo/`)

Extract content into `distributed-systems/docker.md`. Conversion strategy per file:

| File | Content | Strategy |
|------|---------|----------|
| `automated-workflow-docker.PNG` | CI/CD pipeline: App -> Repo -> Testing -> Registry -> Deployment | Mermaid flowchart |
| `dockerCompose.PNG` | "Docker Compose - Compose multi-container apps" | Inline text (too simple for diagram) |
| `dockerContentTrust.PNG` | "Docker Content Trust - Verify content and publisher" | Inline text |
| `dockerEcosystem.PNG` | Ecosystem table: Startups vs Big names | ASCII art table |
| `dockerInc.PNG` | Build/Ship/Run: Cloud vs On-Prem matrix | Mermaid flowchart or ASCII table |
| `dockerIncSol.PNG` | Docker Inc. products grid | ASCII art table |
| `dockerMachine.PNG` | "Docker Machine - Provisions Docker hosts/engines" | Inline text |
| `dockerSwarm.PNG` | "Docker Swarm - Native clustering, v1.0+, scales well" | Inline text |
| `widerEcosystem.PNG` | Wider ecosystem company logos | Inline list (logos have no text equivalent) |

Delete PNGs after extraction if conversion is meaningful. Keep if not.

### PDFs (2 files)

| File | Treatment |
|------|-----------|
| `doc/parallel/TPLDataflow.pdf` | Extract text to `dotnet/parallelism/tpl-dataflow.md`, link to original source URL, delete PDF |
| `doc/nosql/microsoft-documentdb-sql-query-cheat-sheet-v4.pdf` | Extract text to `data/nosql/document-db-cheat-sheet.md`, link to original source URL, delete PDF |

### Azure Lecture PNGs (18 files)

| Category | Files | Treatment |
|----------|-------|-----------|
| Text-only slides | Most `l02/h*.png` files | Extract as markdown content into consolidated lecture pages |
| Diagrams | Network topology diagrams (e.g., `h11.png`) | Convert to Mermaid inline; fallback to ASCII art |
| Tabular/journey | `l01/migration.journey.png` | ASCII art table |
| Web app hosting | `l01/web.app.hosting.png` | Mermaid or ASCII depending on complexity |

### Azure Learn PNGs (2 files)

| File | Treatment |
|------|-----------|
| `524-payasyougo.png` | Extract text into `identity-and-governance.md` |
| `adfs-aad-spo-federated-sso.png` | Convert to Mermaid diagram in `identity-and-governance.md` |

### Doc-Embedded PNGs (4 files)

| File | Treatment |
|------|-----------|
| `doc/asp/binding.posted.form.data.png` | Mermaid/ASCII in `dotnet/aspnet/mvc.md` |
| `doc/asp/model.binding.png` | Mermaid/ASCII in `dotnet/aspnet/mvc.md` |
| `doc/soa/js.fetch.listen.png` | Mermaid in `distributed-systems/websockets.md` |
| `doc/soa/send.events.async.png` | Mermaid in `distributed-systems/websockets.md` or relevant page |

### SQL Scripts (2 files)

Keep as-is. Move to `data/sql/scripts/`.

### Inline Image References

- Check reachability of all image URLs in markdown files
- Add ⚠ warning character next to unreachable URLs
- Add descriptive alt text to all images with empty alt text (`![](url)` becomes `![short description](url) ⚠`)

## Formatting Conventions

### Reference-Style Links (Bibliography)

All URLs use reference-style links at the end of the file:

```markdown
## Content

**CQRS** and _Event Sourcing_ with `NServiceBus` [1]

`Hangfire` ServerProcessExtensions.cs [2]

[<<](../index.md) | [home](../../README.md)

[1]: https://code.msdn.microsoft.com/CQRS-and-Event-Sourcing-3d194cc1
[2]: https://github.com/HangfireIO/Hangfire/blob/.../ServerProcessExtensions.cs#L57
```

Rules:
- No inline `[text](url)` links — all converted to `text [n]`
- No bare URLs — every URL gets a descriptive label
- Numbered ascending per file starting at `[1]`
- Placed after bottom navigation links, separated by a blank line

### Semantic Entity Formatting

| Entity Type | Format | Examples |
|-------------|--------|---------|
| Architectural patterns | **bold** | **CQRS**, **MVC**, **HATEOAS**, **Pub/Sub**, **Repository** |
| Protocols | **bold** | **HTTP**, **REST**, **GraphQL**, **WebSocket**, **TCP/IP** |
| Concepts/theorems | **bold** | **CAP theorem**, **ACID**, **BASE**, **SOLID** |
| Methodologies/practices | _italic_ | _Event Sourcing_, _Domain-Driven Design_, _TDD_, _Continuous Delivery_ |
| Frameworks/packages/tools | `code` | `NServiceBus`, `Angular`, `Entity Framework`, `Docker`, `xUnit` |
| Cloud services/platforms | `code` external, plain in owning doc | `Cosmos DB` in data pages; Cosmos DB in azure pages |
| Programming languages | plain text | C#, JavaScript, SQL, Python |

### File Naming

- All file names in kebab-case: `managed-threads.md`, `entity-framework.md`, `angular-fundamentals.md`
- No PascalCase, no dots (except `.md`), no mixed casing

### Heading Casing

- H1-H3 use American English title case: `# Thread-Local Storage`, `## Background vs Foreground Threads`

### Bottom Navigation

- Preserve existing `[<<](../parent.md) | [home](../../README.md)` pattern
- Update all relative paths for new folder structure

### Index Files

- Every folder gets an `index.md` hub page
- Lists child pages with brief descriptions
- Includes navigation links

## Markdownlint Configuration

File: `.markdownlint.json` at repo root. Moderate strictness.

```json
{
  "default": true,
  "MD013": false,
  "MD033": false,
  "MD024": { "siblings_only": true },
  "MD034": true,
  "MD041": true,
  "MD025": true
}
```

| Rule | Setting | Rationale |
|------|---------|-----------|
| MD013 (line length) | disabled | Documentation paragraphs should not be hard-wrapped |
| MD033 (inline HTML) | disabled | Jekyll/just-the-docs sometimes needs HTML for badges, anchors |
| MD034 (bare URLs) | enabled | Aligns with bibliography convention |
| MD041 (first line H1) | enabled | Every file starts with a title heading |
| MD025 (single H1) | enabled | One title per file |
| MD024 (duplicate headings) | siblings only | Allow same heading text in different sections |
| All others | default (enabled) | Consistent heading hierarchy, blank lines, proper lists, trailing whitespace |

## Root-Level Files

### STRUCTURE.md

New file at repo root containing the full folder tree. Kept up to date as the repo map.

### CLAUDE.md

Updated with:
- New folder structure description
- Formatting conventions (reference links, entity formatting, heading casing, kebab-case filenames)
- Markdownlint config reference
- Max depth constraint (4 levels below README)
- Index file pattern
- Navigation link pattern

### README.md

Updated to link to new top-level categories instead of old `doc/` index files.

## Cleanup

| Action | Target |
|--------|--------|
| Delete | `todo/` folder (after meaningful PNG extraction) |
| Delete | `doc/parallel/TPLDataflow.pdf` (after text extraction) |
| Delete | `doc/nosql/microsoft-documentdb-sql-query-cheat-sheet-v4.pdf` (after text extraction) |
| Delete | `azure/lctrs/pics/` (after content extraction) |
| Delete | `azure/learn/*.png` (after content extraction) |
| Delete | `doc/asp/*.png` (after Mermaid/ASCII conversion) |
| Delete | `doc/soa/*.png` (after Mermaid/ASCII conversion) |
| Delete | Old `doc/` and `azure/` folder structure (after all files migrated) |

## Out of Scope

- Content authoring (no new documentation written beyond index pages)
- External link validation beyond reachability check
- Jekyll theme configuration changes
- GitHub Pages deployment changes
