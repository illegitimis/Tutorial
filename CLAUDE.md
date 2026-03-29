# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Jekyll-based documentation site ("Dev Mnemonics") published on GitHub Pages. Contains 212 Markdown files covering software development topics organized into a 4-level hierarchy.

## Architecture

- **Static site generator:** Jekyll with the just-the-docs remote theme
- **Deployment:** Automatic via GitHub Pages on push to `master`
- **No build step, test suite, or linting pipeline** — markdownlint is configured for editor use
- **Structure map:** See `STRUCTURE.md` for the full directory tree

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
- Every leaf file ends with `[<<](./index.md) | [home](../../README.md)` (depth-adjusted)

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
