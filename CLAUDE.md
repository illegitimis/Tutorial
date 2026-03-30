# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Jekyll-based documentation site ("Dev Mnemonics") published on GitHub Pages. Contains 151 Markdown files covering software development topics organized into a 4-level hierarchy.

## Architecture

- **Static site generator:** Jekyll with the just-the-docs remote theme
- **Deployment:** Automatic via GitHub Pages on push to `master`
- **No build step, test suite, or linting pipeline** — markdownlint is configured for editor use
- **Structure map:** See `STRUCTURE.md` for the full directory tree
- **Home pages:** `index.md` (JTD site home) and `README.md` (GitHub-facing)
- **Front matter:** All content pages carry JTD front matter (`title`, `parent`, `nav_order`, etc.)
- **Mermaid:** Enabled via `_includes/mermaid_config.js` and bundled `assets/js/mermaid.min.js`
- **Community files:** `CHANGELOG.md`, `CONTRIBUTING.md`, `CONTRIBUTORS.md`, `LICENSE` (CC BY 4.0)

### Top-Level Categories

| Directory | Content |
|-----------|---------|
| `dotnet/` | C#, CLR, ASP.NET, EF, parallelism |
| `javascript/` | JS, Angular, CSS, npm, Webpack |
| `architecture/` | OOP, SOLID, DDD, design patterns, UML |
| `distributed-systems/` | Microservices, Docker, messaging, SignalR |
| `data/` | SQL, NoSQL, MongoDB |
| `web-services/` | REST, HTTP, GraphQL, Swagger |
| `azure/` | AZ-900 learning paths, Azure services |
| `testing/` | NUnit, xUnit, TDD |
| `devops/` | Git, CI/CD, NuGet, Visual Studio, YAML |

### Max Depth

4 levels below `README.md`. Example deepest path: `data/nosql/mongo/articles.md`

## Local Preview

```bash
gem install jekyll bundler
jekyll serve
```

## Content Conventions

### File Naming

- Kebab-case only: `managed-threads.md`, `entity-framework.md`
- No PascalCase, no dots (except `.md`)

### Heading Casing

- H1-H3 use American English title case

### Links

- All external URLs use reference-style links at end of file
- No bare URLs
- No inline `[text](url)` for external links
- Relative links (`[<<](../index.md)`) stay inline

### Navigation

- Every folder has an `index.md` hub page
- Every leaf file ends with backlinks: \
`[<](./index.md)` for the index in the same folder \
(depth-adjusted) `[<<]({path-to-root-level-index.md})` 

### Semantic Entity Formatting

| Entity Type | Format |
|-------------|--------|
| Architectural patterns, protocols, concepts | **bold** |
| Methodologies/practices | _italic_ |
| Frameworks/packages/tools | `code` |
| Cloud services | `code` when external, plain in owning doc |
| Programming languages | plain text |

### Markdownlint

Config: `.markdownlint.json` — MD013 (line length) and MD033 (inline HTML) disabled; all other rules default enabled.

### Emoji

No GitHub emoji shortcodes — they don't render on Jekyll/GitHub Pages.

### incremental updates

- update STRUCTURE.md ascii art file tree when files are added or deleted
- update `last_modified_date` in content mds when changed
- do not include co-authored by claude in commit messages
- keep CHANGELOG.md in sync with new commits
