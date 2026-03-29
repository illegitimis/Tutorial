# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Jekyll-based documentation site ("Dev Mnemonics") published on GitHub Pages at https://illegitimis.github.io/Tutorial/. Contains 200+ Markdown files covering software development topics: ASP.NET, C#/.NET, Azure, JavaScript, design patterns, OOP/SOLID/DDD, SQL/NoSQL, REST, SOA, messaging, TDD, CI/CD, and more.

## Architecture

- **Static site generator:** Jekyll with the [just-the-docs](https://github.com/just-the-docs/just-the-docs) remote theme
- **Deployment:** Automatic via GitHub Pages on push to `master`
- **No build step, test suite, or linting** — this is a pure documentation repository

### Directory Layout

- `doc/` — Core technical documentation. Index files (e.g., `ASP.md`, `csdotnet.md`, `JS.md`) link to topic subdirectories (`asp/`, `c#/`, `js/`, `oop/`, `sql/`, etc.)
- `azure/` — Azure learning materials (AZ-900 path). `az.md` is the entry point; `learn/` has numbered modules and knowledge checks; `lctrs/` has lecture notes; `pages/` has service-specific docs
- `todo/` — Reference images (Docker diagrams, architecture visuals)
- `_config.yml` — Jekyll/theme configuration (dark scheme, search enabled with Ctrl+K, copy-code buttons, heading anchors)

## Local Preview

```bash
gem install jekyll bundler
jekyll serve
# => http://localhost:4000
```

## Content Conventions

- All content is Markdown with Jekyll front matter where needed for navigation (`title`, `parent`, `nav_order`, `last_modified_date`)
- Navigation is sorted case-sensitive (capitals before lowercase) per `_config.yml`
- Pages include breadcrumb-style links back to parent index and `README.md`
- The site uses dark color scheme by default
