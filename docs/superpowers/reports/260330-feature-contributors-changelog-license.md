# Contributors, Changelog, and License Report

**Branch:** `feature/contributors-changelog-license`
**Date:** 2026-03-30
**Commits:** 5 (this task)

## Summary

Added four standard open-source repository files to the root: a compact table-format changelog generated from full git history, a contributors list with accurate commit counts, simple contribution guidelines, and a CC BY 4.0 license. The changelog was initially generated in an H2-section format in a prior session then reformatted to a compact Markdown table (date, short hash, description columns) per updated requirements.

## Stats

- **4 files added** to repository root
- **645 insertions** across the four new files
- **382 non-merge commits** captured in CHANGELOG.md (oldest: 150310, newest: 260330)
- **417 total commits** attributed across all contributors

## Files Added

| File | Purpose |
|------|---------|
| `CHANGELOG.md` | Compact table of all 382 non-merge commits, ordered newest-first, columns: date (YYMMDD), short hash, description |
| `CONTRIBUTORS.md` | Primary author (Andrei Ciprian Popescu, 416 commits) and external contributor (Josh Abernathy, 1 commit) |
| `CONTRIBUTING.md` | Fork-branch-PR workflow and content guidelines referencing CLAUDE.md conventions |
| `LICENSE` | Full Creative Commons Attribution 4.0 International Public License text |

## Key Decisions

- **Table format over H2 sections:** Original plan used `## YYMMDD — hash` sections. Changed to a single compact table for readability and scannability — one row per commit rather than three lines.
- **Changelog sourced from `git log --no-merges`:** Merge commits (pull requests, branch merges) excluded; 382 rows from 390+ raw commits.
- **Commit counts consolidated:** Five name/email variants for the primary author (`illegitimis`, `Illegitimis`, `ESHOPWORLD\apopescu`, `illegitimis@gmail.com`, `Andrei Ciprian Popescu`) summed to 416.
- **CC BY 4.0 full text:** Included the full legal text rather than a short reference, consistent with GitHub's license file convention.

## Commit History

```
11e9c78 docs: update plan with table format spec and report task
568c6c2 docs: add CC BY 4.0 license
0b2672a docs: add contribution guidelines
bb64dcf docs: add contributors list with commit counts
f0ab9b9 docs: reformat changelog as compact table (date, hash, description)
```
