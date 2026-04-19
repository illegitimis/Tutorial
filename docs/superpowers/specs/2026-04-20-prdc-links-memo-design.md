# PRDC — Links scan, classification, and memo design

## Overview

PRDC (name from `plan26041902.md`) is a **non-interactive** tool that scans the wiki’s Markdown, **classifies** every link destination, **persists** a mergeable ledger to disk, and applies one **content mutation**: `localhost` links are replaced with italic text. Prefer a **standalone Python** implementation, consistent with other repo maintenance scripts under `docs/superpowers/scripts/`.

This document is the **authoritative** description of memo behavior. It **refines** the plan note that `url` is “the same string the parser extracted”: in PRDC, `url` is the **canonical memo key** after the normalization rules below (parser output is an input, not the final key).

## Goals

- Scan all in-scope wiki Markdown, extract **inline and reference** link destinations (any scheme or relative path the Markdown layer exposes).
- Classify each extracted link per `plan26041902.md` (including the **url classify** table and non-URL rules).
- Maintain `/_memoize/LINKS.json` across runs with **stable merge semantics** and **no prompts**.
- Rewrite `localhost:[PORT]` links in source Markdown to italics **on every run**, with **no** dry-run mode and **no** separate CLI flag for that behavior (operator intent is “run PRDC = scan + classify + memo + localhost fix”).

## Non-goals

- Building or serving the Jekyll site as part of PRDC.
- Tracking links in category **`NONE`** (they never appear in JSON).
- Interactive confirmation, TTY prompts, or per-file approval gates.

## Scan scope

### Include

- Markdown files that are **wiki content**: topic trees such as `dotnet/`, `architecture/`, `data/`, and analogous content directories defined at implementation time (mirror `CLAUDE.md` / `STRUCTURE.md` reality).

### Exclude

Per `plan26041902.md`:

- GitHub / community root files at repository root: at minimum `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `CONTRIBUTORS.md`, `LICENSE`, `STRUCTURE.md`, and `plan*.md` scratch plans unless explicitly included later.
- Agent / Claude meta (e.g. `.claude/`, `CLAUDE.md` if treated as meta).
- Superpowers docs under `docs/superpowers/` (specs, plans, reports, scripts) unless explicitly re-scoped later.
- **Hub `index.md` files** anywhere under wiki content trees (including repository-root `index.md`): exclude the **entire file** from scanning.
- **Backward / forward navigation** between Markdown content (the plan’s “between md content” nav patterns — define precise patterns during implementation, e.g. same-folder `[<](./index.md)` / depth-adjusted root index links, so PRDC does not ledger or classify them).

## Extraction

- A **link** is any Markdown link destination: `https`, `http`, `mailto`, `tel`, relative paths, other schemes, fragments, autolinks if present, **including reference-style** link destinations.
- Parser choice is implementation detail; it must resolve reference definitions to a concrete href string before normalization.

## Classification

Apply the type → category table in `plan26041902.md` (images → review, mermaid/ascii → diagram, Google/Drive → resource, clear extensions → extension, CI/badge links → **NONE**, programming-language sample extensions → sample, else review unless **url classify** matches).

**url classify** uses the rules in `plan26041902.md` (npm, nuget, blog, pdf/resource, GitHub repo shape, Mongo docs hosts, Wikipedia, Docker Hub, Microsoft / Google doc hosts, O’Reilly, YouTube, gist, SlideShare, Stack Exchange family → mapped categories; **anything else** under web classification path → `review` unless another rule fires first).

**Ordering:** Define a **deterministic** rule order in implementation (e.g. `NONE` and special cases before generic `http` rules) so two runs on the same tree produce the same category for the same canonical `url`.

## Memo file

- **Path:** `/_memoize/LINKS.json` (create `/_memoize/` on first run if missing).
- **Shape:** JSON array of objects: `{ "url": "<string>", "category": "<string>" }` **only** (no `file` field).
- **Serialize** every in-scope extracted link **except** category **`NONE`** (those never appear).
- **Uniqueness:** at most one object per canonical `url` after normalization.
- **Determinism:** write JSON with **stable sorting** (e.g. sort by `url`, then `category`) so diffs are repeatable.

## Canonical `url` (memo key)

### `http` / `https` — aggressive normalization

Input: parser-extracted href for `http`/`https`.

- Lowercase **scheme** and **host**; apply **IDNA / punycode** for the host when applicable.
- Strip **default ports** (`:443` for `https`, `:80` for `http`).
- **Percent-decode** path segments where decoding is **idempotent and safe** (no double-decoding loops). If decoding would change semantics ambiguously, keep the encoded form for that segment (document edge cases in implementation tests).
- Resolve **dot segments** in the path (`/./`, `/../`) when purely hierarchical.
- **Path empty vs root:** normalize bare `https://host` to use path `/` consistently.
- **Trailing slash:** remove a single trailing `/` from the path when the path has **more than one** character and ends with `/` (e.g. `/wiki/foo/` → `/wiki/foo`; `/` remains `/`).
- **Fragment:** **retain** `#fragment` as part of the canonical web URL (different fragments ⇒ different memo rows).
- **Query:** retain query parameters, but **remove** query keys that match a **built-in only** blocklist (**T1**). Strip entire duplicate keys consistently; sort remaining keys for stable serialization. Initial built-in keys should include common trackers, including at minimum: `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`, `gclid`, `fbclid`, `msclkid`, `mc_eid`, `yclid`, `_ga`, `spm` (extend in code with comments; spec lists intent, code lists exact names).

### `mailto` / `tel` — light normalization (W2)

- **`mailto:`:** lowercase **scheme**; trim ASCII whitespace around the full href; for `mailto:user@host`, lowercase **host** part; preserve `?subject=` / `&body=` query semantics with the same **tracking-key strip** as `http` where applicable.
- **`tel:`** strip ASCII whitespace, parentheses, and hyphens from the **tel-national** portion while preserving leading `+` and digits; scheme lowercased.

These remain `mailto:...` / `tel:...` strings — **not** repo-relative paths.

### Path-like / in-repo keys

For destinations that are **not** `http`, `https`, `mailto`, or `tel` (relative paths, root-anchored site paths, other schemes classified into the path pipeline):

- Resolve relative to the **source Markdown file’s directory** to a path under the **repository root**.
- Emit **repo-relative POSIX** paths (`folder/file.md`), **even on Windows** (**P1**).
- **Strip `#fragment`** from identity for these keys (**F2**): canonical `url` is the file path only.
- If a path cannot be resolved to an existing repo file: emit a **best-effort** repo-relative POSIX path (after syntactic normalization) and classify as **`review`** unless a higher-priority rule applies.

## `localhost:[PORT]` mutation

- When a link destination matches `localhost` with an explicit port (pattern fixed in implementation, aligned with the plan’s intent), **remove the Markdown link** and replace the **link text** with *italic* using the same visible text (or the literal `localhost:port` if link text is empty — edge case defined in implementation).
- Apply **whenever PRDC runs**, in the same pass as scanning, **without** a dry-run default and **without** a dedicated “fix localhost” flag.

## Merge semantics (`LINKS.json`)

On startup:

1. If `LINKS.json` is missing, start from an **empty** array.
2. Otherwise load existing rows.

During the run:

- Compute canonical `url` → category for every extracted in-scope link (skipping **`NONE`** for persistence).
- **Insert** rows for new canonical `url` values.
- **Update** `category` when the newly computed category **differs** from the stored one, **except**:
  - If an existing row has `category != "review"`, **do not re-classify**; keep stored `category` and row as-is for that `url`.
- Rows with `category == "review"` are **re-evaluated every run** until the computed category becomes something other than `review`, at which point the row updates and then participates in the frozen non-review rule above.

Write the merged array back to `LINKS.json` with stable sorting.

## CLI / execution

- **Non-interactive:** never prompt; failures print a clear message and exit non-zero.
- **No** dry-run mode and **no** separate flag for localhost rewriting (**approved** operator model: running PRDC applies fixes).

Exact invocation (`python -m …`, script name, arguments such as repo root defaulting to cwd) is left to the implementation plan phase.

## Testing (minimum)

- **Golden tests** for normalization: representative `http`/`https`, `mailto`/`tel`, and POSIX path keys (including fragment strip for paths, fragment keep for https).
- **Merge tests**: frozen non-review, `review` reassessed, `NONE` omitted.
- **Fixture** Markdown snippets: inline + reference links, at least one `localhost:PORT` before/after rewrite.

## Open items for implementation plan only

- Exact directory glob list for “wiki content” vs excluded roots (derived from `STRUCTURE.md` / current tree).
- Precise regex or AST patterns for **nav exclusion** (hub and sibling nav).
- Parser library choice and version pinning.
