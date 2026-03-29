# Repository Reorganization Report

**Branch:** `feature/repo-reorganization`
**Date:** 2026-03-29
**Commits:** 18

## Summary

Reorganized ~200+ scattered markdown developer notes into a clean hierarchical structure with maximum 4 levels of nesting. Applied consistent formatting, linting, and naming conventions across all files.

## Stats

- **317 files changed** across 18 commits
- **8,426 insertions / 6,248 deletions**
- **148 markdown files** in final structure (down from ~200+ scattered files)
- **9 top-level categories** with 18 index.md hub pages
- **0 markdownlint errors** (down from 2,372 initial errors)
- **232 old files removed** (doc/, todo/, azure/learn/, azure/lctrs/, azure/pages/)

## Target Structure

```
├── architecture/        Design patterns, SOLID, DDD, UML
├── azure/               Cloud concepts, services, security, AZ-900
├── data/                SQL + NoSQL (Mongo, Cosmos, DocumentDB)
├── devops/              Git, CI/CD, NuGet, tools, OS, security
├── distributed-systems/ Docker, Kafka, microservices, SignalR, WebSockets
├── dotnet/              C# language, runtime, ASP.NET, data access, parallelism
├── javascript/          Angular, CSS, npm, webpack, Redux, PWA
├── testing/             NUnit, xUnit
├── web-services/        REST, GraphQL, Swagger, HTTP, WebAPI
```

## Key Transformations

### Category Merges and Absorptions

- **messaging + SOA** merged into `distributed-systems/`
- **ORM** absorbed into `dotnet/data-access/`
- **CSS** absorbed into `javascript/css.md`
- **CMS** absorbed into `dotnet/aspnet/`
- **OS** absorbed into `devops/`
- **ASP + netcore** consolidated into `dotnet/aspnet/`

### Azure Flattening

67 learning module files consolidated into 7 topic-based files:

| File | Content |
|------|---------|
| `cloud-concepts.md` | Cloud models, benefits, service types |
| `core-services.md` | Compute, networking, storage |
| `solutions-and-tools.md` | IoT, AI, serverless, DevOps |
| `security.md` | Network security, NSGs, firewalls, DDoS |
| `identity-and-governance.md` | Azure AD, MFA, RBAC, policies, compliance |
| `cost-management.md` | Pricing, TCO, SLAs |
| `az-900-summary.md` | Certification summary and knowledge checks |

### Non-Markdown Content

- **9 Docker PNGs** extracted to text/Mermaid/ASCII and merged into `distributed-systems/docker.md`; originals deleted
- **2 ASP.NET PNGs** (model binding, form data) converted to text descriptions in `dotnet/aspnet/mvc.md`; originals deleted
- **2 WebSocket PNGs** converted to Mermaid sequence diagrams in `distributed-systems/websockets.md`; originals deleted
- **TPL Dataflow PDF** extracted to `dotnet/parallelism/tpl-dataflow.md`
- **DocumentDB cheat sheet PDF** extracted to `data/nosql/document-db-cheat-sheet.md`
- **SQL scripts** kept as-is in `data/sql/scripts/`
- **mra.md** (Movie Review Aggregator personal project) dropped as out of scope

### Formatting Conventions Applied

- **Kebab-case filenames** for all markdown files
- **American English title case** for H1-H3 headings
- **Reference-style links** (bibliography format at bottom of files)
- **Semantic entity formatting**: bold for patterns/protocols/concepts, italic for methodologies, `code` for frameworks/tools
- **Emoji shortcodes** replaced with Unicode or removed
- **Bare URLs** labeled with descriptive text
- **39 unreachable images** (legacy livefilestore.com) marked with warning character
- **Image alt text** added where missing

### Root-Level Files Created/Updated

- **STRUCTURE.md** — Full directory tree
- **CLAUDE.md** — Updated with all conventions
- **README.md** — Links to 9 top-level index.md files
- **CHANGELOG.md** — Generated from git history

## Commit History

```
c0b9044 chore: remove old directory structure and extracted binaries
67baf1c fix: resolve markdownlint errors across all docs
2567d4d docs: update root-level files (STRUCTURE.md, CLAUDE.md, README.md)
771b21f fix: update breadcrumb navigation for new folder structure
71cb05b feat: create index.md hub pages for all categories
92ddbcd style: fix heading casing, remove emoji shortcodes, add image alt text
8d47cbb style: apply semantic entity formatting across all docs
71bf5b9 style: convert all external links to reference-style
20745f4 feat: complete Azure flattening (identity, cost, summary, lectures)
dd3a69c feat: convert embedded PNGs to Mermaid/ASCII in aspnet and websockets docs
6454b65 feat: extract PDF content to markdown (TPL Dataflow + DocumentDB cheat sheet)
a5bc609 feat: enrich Docker docs with content extracted from PNGs
1c46e08 chore: migrate javascript, architecture, distributed-systems, data, web-services, testing, and devops files
20f4cea chore: migrate C#, runtime, ASP.NET, ORM, and parallelism files to dotnet/
e97266a docs: add changelog from git history
858a860 chore: add markdownlint config and target directory structure
5baf9be Add repository reorganization implementation plan
bc9b316 Add emoji/unicode cleanup convention to design spec
9e2043b Add repository reorganization design spec
```
