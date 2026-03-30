# Feature Report: JTD Front Matter

**Branch:** `feature/front-matter`
**PR:** [#29](https://github.com/illegitimis/Tutorial/pull/29) — Add JTD front matter to all content pages
**Date:** 2026-03-30
**Status:** Approved and merged

## Summary

Added Just The Docs YAML front matter to all content `.md` files in the repository. Created a new root `index.md` as the JTD home page, rewrote `README.md` as a lean GitHub-facing file, standardized backlinks across all pages, and updated the `_config.yml` time format. A reusable Python script handled the bulk operation.

## What Changed

### Files Created
- `index.md` — new root home page with `layout: home` front matter and category link list
- `docs/superpowers/scripts/add_front_matter.py` — reusable Python script for bulk front matter operations

### Files Modified
- **144 content pages** — full JTD front matter added (title, layout, nav_order, hierarchy, last_modified_date)
- **5 excluded root files** (CONTRIBUTING.md, CONTRIBUTORS.md, STRUCTURE.md, CHANGELOG.md, bs-front-matter.md) — `nav_exclude: true` + `search_exclude: true`
- **README.md** — rewritten as minimal GitHub-facing file with nav/search exclusion
- **_config.yml** — `last_edit_time_format` changed to `"%Y-%m-%d %H:%M:%S"`

### Files Untouched
- `CLAUDE.md` — orthogonal to JTD
- `docs/superpowers/**/*.md` — plugin artifacts, not JTD content

## Front Matter Schema

| Page Type | Layout | Hierarchy Fields | Example |
|-----------|--------|-----------------|---------|
| Root index.md | `home` | none (top-level) | `index.md` |
| Category index | `minimal` | `has_children: true` | `dotnet/index.md` |
| Subcategory index | `minimal` | `parent`, `has_children: true` | `dotnet/parallelism/index.md` |
| Leaf page | `default` | `parent`, `grand_parent` (depth 3) | `dotnet/parallelism/managed-threads.md` |
| Excluded root file | n/a | `nav_exclude`, `search_exclude` | `CONTRIBUTING.md` |

## Key Decisions

- **JTD 3-level nav limit:** `data/nosql/mongo/` files (depth 3) flattened as level-3 siblings under NoSQL to stay within JTD's max navigation depth.
- **Directories without index.md:** `azure/lectures/` and `devops/os/` files assigned to the nearest ancestor index (Azure and DevOps respectively).
- **Nav order:** Root categories follow the README link order (.NET=1 through DevOps=9). Subfolders sorted alphabetically by H1 title.
- **Last modified dates:** Bulk-cached from one `git log` query, converted to UTC `YYYY-MM-DD HH:MM:SS +00:00` format. New files default to `2026-03-30 00:00:00 +00:00`.
- **Backlinks standardized:** `[<](./index.md)` for parent, `[<<](/index.md)` for home. Category index files get only `[<<](/index.md)`.

## Commits

| SHA | Message |
|-----|---------|
| `5f0a030` | feat: create root index.md as JTD home page |
| `5306818` | feat: rewrite README.md as lean GitHub-facing file |
| `27492ab` | feat: update last_edit_time_format to YYYY-MM-DD HH:MM:SS |
| `eb89c67` | feat: add Python script for bulk JTD front matter |
| `81b633c` | fix: prevent spurious parent field on category index pages |
| `48accad` | feat: add JTD front matter to all content pages and fix backlinks |

## Artifacts

| Artifact | Path |
|----------|------|
| Design spec | `docs/superpowers/specs/2026-03-30-front-matter-design.md` |
| Implementation plan | `docs/superpowers/plans/2026-03-30-front-matter.md` |
| Python script | `docs/superpowers/scripts/add_front_matter.py` |
| This report | `docs/superpowers/reports/260330-feature-front-matter.md` |