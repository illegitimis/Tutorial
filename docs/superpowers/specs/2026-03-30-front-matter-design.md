# Just The Docs Front Matter — Design Spec

**Date:** 2026-03-30
**Branch:** `feature/front-matter`
**Status:** Approved

## Overview

Add Just The Docs (JTD) YAML front matter to all content `.md` files in the repository. Create a new root `index.md` as the JTD home page, rewrite `README.md` as a lean GitHub-facing file, standardize backlinks, and update `_config.yml` time format. A reusable Python script handles the bulk operation.

## File Classification

Three categories:

| Category | Files | Treatment |
|----------|-------|-----------|
| **Untouched** | `CLAUDE.md`, `docs/superpowers/**/*.md` | No edits whatsoever |
| **Excluded** | `README.md`, `CONTRIBUTING.md`, `CONTRIBUTORS.md`, `STRUCTURE.md`, `CHANGELOG.md`, `bs-front-matter.md` | Front matter with `nav_exclude: true` + `search_exclude: true` only |
| **JTD pages** | New root `index.md`, all subdirectory `index.md` and leaf `.md` files (~149 files) | Full front matter |

## Front Matter Schema

### Root `index.md` (new home page)

```yaml
---
title: "Illegitimis' Dev Mnemonics"
layout: home
nav_order: 1
description: "Dev documentation, tutorial, memory pointers, inverse oblivion"
permalink: /
last_modified_date: 2026-03-30 00:00:00 +00:00
---
```

### Category `index.md` (e.g. `dotnet/index.md`)

```yaml
---
title: .NET
layout: minimal
nav_order: 1
has_children: true
last_modified_date: 2025-12-15 09:41:23 +00:00
---
```

### Subcategory `index.md` (e.g. `dotnet/parallelism/index.md`)

```yaml
---
title: Parallelism
layout: minimal
nav_order: 3
parent: .NET
has_children: true
last_modified_date: 2025-11-02 17:08:44 +00:00
---
```

### Leaf pages (e.g. `dotnet/parallelism/managed-threads.md`)

```yaml
---
title: Managed Threads
layout: default
nav_order: 2
parent: Parallelism
grand_parent: .NET
last_modified_date: 2025-10-20 08:12:55 +00:00
---
```

### Excluded root files (e.g. `CONTRIBUTING.md`)

```yaml
---
nav_exclude: true
search_exclude: true
---
```

## Front Matter Field Rules

- **`title`** — extracted from existing H1 heading in file content
- **`layout`** — `home` for root `index.md`, `minimal` for all other `index.md` files, `default` for leaf pages
- **`nav_order`** — starts at 1 everywhere. Root-level categories use the order from `README.md` link list: .NET (1), Architecture (2), Data (3), Web Services (4), Azure (5), Distributed Systems (6), Testing (7), JavaScript (8), DevOps (9). Within subfolders: alphabetical by H1 title, starting at 1
- **`last_modified_date`** — UTC datetime from `git log -1 --format="%ai"` converted to `YYYY-MM-DD HH:MM:SS +00:00`. New files (no git history) use `2026-03-30 00:00:00 +00:00`
- **`has_children: true`** — on any `index.md` that has child pages beneath it
- **`parent`** — title string of the parent `index.md` (omitted for root-level pages)
- **`grand_parent`** — title string of the grandparent `index.md` (only for depth-3 pages)
- **`description`** — only on root `index.md`
- **`permalink: /`** — only on root `index.md`

## README.md Restructuring

### New root `index.md`

Receives the current README.md content:
- H1 title "Illegitimis' Dev Mnemonics"
- Category link list (.NET, Architecture, Data, etc.)
- Full JTD `home` layout front matter

### Rewritten `README.md`

Lean GitHub-facing file:

````markdown
# Dev Mnemonics

A Jekyll-based documentation site covering software development topics —
C#/.NET, architecture, data, web services, Azure, distributed systems,
testing, JavaScript, and DevOps.

## Live Site

[illegitimis.github.io/Tutorial](https://illegitimis.github.io/Tutorial/)

## Local Development

```bash
gem install jekyll bundler
jekyll serve
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Resources

- [Wiki](https://github.com/illegitimis/Tutorial/wiki) — legacy documentation
````

Gets `nav_exclude: true` + `search_exclude: true` front matter.

## Backlink Standardization

Current pattern (varies by file):
```
[<<](./index.md) | [home](../../README.md)
```

New standardized format:
```
[<](./index.md) | [<<](/index.md)
```

Rules:
- `[<](./index.md)` — parent `index.md` in the same folder
- `[<<](/index.md)` — root home page
- Remove all `[home](...README.md)` variants
- Root `index.md` — no backlinks
- Category `index.md` files (e.g. `dotnet/index.md`) — only `[<<](/index.md)`, no `[<]`
- Files without existing backlinks — leave as-is
- Script uses regex to match all backlink variants

## Config Change

In `_config.yml`:

```yaml
# From:
last_edit_time_format: "%b %e %Y at %I:%M %p"
# To:
last_edit_time_format: "%Y-%m-%d %H:%M:%S"
```

## Python Script

**Location:** `docs/superpowers/scripts/add_front_matter.py`

**Responsibilities:**
1. Run a single bulk `git log` command upfront to collect last-modified UTC datetimes for all tracked `.md` files. Cache results in a dict keyed by file path. This query runs once, not per file.
2. Walk all `.md` files from repo root
3. Classify each file (untouched / excluded / JTD page)
4. Extract H1 title from file content
5. Look up last-modified datetime from the cached dict (new/untracked files get `2026-03-30 00:00:00 +00:00`)
6. Determine hierarchy (`parent`, `grand_parent`, `has_children`) from folder structure
7. Compute `nav_order` — root children from README link order, subfolders alphabetical by title
8. Prepend front matter block
9. Fix backlinks per standardization rules
10. Support `--dry-run` flag for preview without modification

**Does NOT handle:**
- Creating root `index.md` (manual)
- Rewriting `README.md` (manual)
- Updating `_config.yml` (manual)

## Artifacts

| Artifact | Location |
|----------|----------|
| Design spec | `docs/superpowers/specs/2026-03-30-front-matter-design.md` |
| Implementation plan | `docs/superpowers/plans/` |
| Python script | `docs/superpowers/scripts/add_front_matter.py` |
| Final report | `docs/superpowers/reports/` |
