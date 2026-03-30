---
name: import-notes
description: Use when importing loose markdown notes into the documentation tree — merges content using set-union semantics with category matching, section-level diffing, and CLAUDE.md normalization
---

# Import Notes

Merge loose markdown files into the documentation tree using set-union semantics: A = A + (B - A).

**Full spec:** `docs/superpowers/specs/2026-03-30-import-notes-design.md`

## Arguments

`$ARGUMENTS` contains file paths and optional flags.

Parse arguments:

- File paths: any arg not starting with `--`
- `--dry-run`: run stages 1-4 only, report proposed actions, write nothing
- `--auto`: skip prompts for >= 85% confidence, only pause for conflicts and < 70%
- `--review-rules`: show contents of `docs/superpowers/data/import-mappings.json`, ask which rules to keep/edit/delete, then exit

If no file paths provided (and not `--review-rules`), ask the user for files.

## Stage 1: PARSE

For each input file B:

1. Read the file
2. Extract heading tree (H1-H3) with content blocks under each heading
3. For each heading, note: level, text, content (everything until next same/higher-level heading), line number
4. Normalize heading text using title case rules from `docs/superpowers/scripts/fix_headings.py` (read its `TECH_TERMS` and `SMALL_WORDS` dicts for reference)

Report to user: parsed heading tree for each B file.

## Stage 2: MATCH

### Load learned rules

Read `docs/superpowers/data/import-mappings.json` if it exists. Apply:

- `category_rules`: boost matching categories by `confidence_boost` points when keywords match
- `heading_aliases`: use known heading mappings for direct placement
- `rejected_placements`: penalize previously-rejected category assignments

### Phase 2a: Category matching

For each B section, score against the 9 top-level categories using these keyword lists:

```txt
dotnet/        : c#, clr, asp.net, ef, entity framework, linq, blazor, razor, nuget, roslyn, .net, task, thread
javascript/    : angular, react, npm, webpack, css, dom, typescript, node, redux, pwa
architecture/  : solid, ddd, design pattern, oop, uml, coupling, cohesion, cqrs, event sourcing
distributed-systems/ : microservice, docker, kafka, signalr, zeromq, websocket, message queue, grpc
data/          : sql, nosql, mongodb, cosmos, index, query, stored proc, transaction, acid, cap theorem
web-services/  : rest, http, graphql, swagger, api, hateoas, etag, caching, webapi
azure/         : az-900, cloud, azure, resource group, arm, app service, functions
testing/       : nunit, xunit, tdd, bdd, mock, stub, integration test, unit test, assertion
devops/        : git, ci/cd, yaml, pipeline, visual studio, deployment, container
```

Scoring weights: 40% keyword hits, 30% learned rules, 30% heading overlap with existing files.

If B spans multiple categories with >= 70% confidence for different parts, propose a split (Stage 4).

### Phase 2b: File matching

Within the matched category, read index.md and all .md files. Compare B's headings against each file's headings:

- Text similarity (account for word reordering, extra/missing words)
- Hierarchy alignment (same H-level = bonus, off-by-one = acceptable, H1 vs H3 = suspicious)
- Sibling context (do neighboring headings also match?)

Composite: 60% heading text + 15% level match + 25% sibling context.

### Confidence thresholds

| Score | Action |
|---|---|
| >= 85% | Auto-place, report to user |
| 70-84% | Propose placement, ask user to confirm |
| < 70% | Show top 3 candidates, ask user to pick or type a path for a new file |

If `--auto` flag: treat 70-84% same as >= 85% (auto-place without prompting).

## Stage 3: DIFF

For each matched B section against its target in A:

### Tier 1: Heading dedup

- Compare B headings against A headings (fuzzy, threshold ~80% similarity)
- No match in A = entire section is NEW, go to Stage 5
- Match found = go to tier 2

### Tier 2: Block-level dedup

- Split content under matched heading into blocks (separated by blank lines)
- For each B block, compare against all A blocks under that heading
- Normalize before comparing: strip markdown formatting (`*_\`[]`), lowercase, collapse whitespace
- Scoring bands:
  - Similarity < 30% = clearly new content, include
  - 30-70% = partial overlap, show both to user and ask: [k]eep A / [r]eplace with B / [m]erge both / [s]kip
  - \> 70% = duplicate, skip

### Tier 3: Bullet-level dedup

- If both A and B have bullet lists under the same heading, compare individual bullets
- New bullets (< 80% match to any existing bullet) get appended
- Duplicate bullets get skipped

Report: for each B section, list what will be inserted, what was skipped as duplicate, and any conflicts.

If `--dry-run`: stop here and show the full report. Do not proceed to stages 5-8.

## Stage 4: SPLIT

If Stage 2a found that B sections map to different categories:

```txt
fileB.md spans multiple categories:
  ## Docker Networking  -> distributed-systems/docker.md (92%)
  ## Azure Container Instances  -> azure/ (new file) (88%)

Split into 2 targets? [y/n]
```

If confirmed, process each part through stages 2-3 independently.

## Stage 5: NORMALIZE

Apply CLAUDE.md conventions to all new content BEFORE writing:

1. **Heading title case** — H1-H3 use American English title case. Reference `TECH_TERMS` from `fix_headings.py` for correct casing of technical terms
2. **Reference-style external links** — convert any `[text](https://...)` to reference-style: `text [N]` inline + `[N]: url` at end of file. Relative links stay inline
3. **Semantic entity formatting** — bold for patterns/protocols/concepts, italic for methodologies/practices, code for frameworks/packages/tools, plain for languages
4. **No bare URLs** — wrap in reference-style links
5. **No emoji shortcodes** — strip `:shortcode:` patterns
6. **Kebab-case filenames** — for any new files: lowercase, hyphens, no dots except `.md`

## Stage 6: WRITE

### Existing files (upsert sections)

1. Read the target file
2. Find insertion point: after the last existing section at the same heading level, before nav backlinks (`[<]` line)
3. Insert new sections with a blank line separator
4. Update `last_modified_date` in front matter to today's date (`YYYY-MM-DD HH:MM:SS +00:00`)
5. If the file has reference-style links, renumber to avoid collisions with new links

### New files

1. Create the file with content
2. Generate JTD front matter by running:

   ```bash
   python docs/superpowers/scripts/add_front_matter.py --dry-run
   ```

   Or manually construct front matter matching the schema:
   - `title`: from H1 or filename
   - `layout: default`
   - `nav_order`: next available number in parent directory
   - `parent`: parent category title
   - `grand_parent`: if depth >= 3
   - `last_modified_date`: today
3. Add nav backlinks at end of file. Use depth-based pattern:
   - Depth 2: `[<](./index.md) | [<<](/index.md)`
   - Depth 3: `[<](./index.md) | [<<](/index.md)`
   - Depth 4: `[<](./index.md) | [<<](/index.md)`

## Stage 7: HOUSEKEEP

1. **STRUCTURE.md** — add new files to the ASCII tree in alphabetical order within their directory
2. **verify_nav.py** — run `python docs/superpowers/scripts/verify_nav.py` to confirm backlinks
3. **Report** — summarize to user:
   - Files created (count + paths)
   - Files modified (count + paths)
   - Sections added (count)
   - Sections skipped as duplicate (count)
   - Conflicts resolved (count)

## Stage 8: LEARN

After the import completes, update `docs/superpowers/data/import-mappings.json`:

### Automatic (every run)

Append to `import_log`:

```json
{"date": "YYYY-MM-DD", "source": "filename.md", "actions": [
  {"type": "insert|skip_dup|new_file|conflict", "target": "path.md", "heading": "## Heading"}
]}
```

### On user corrections

When the user corrects a proposed placement during Stage 2 or 3:

1. Ask: "Save this as a rule for future imports? [y/n]"
2. If yes, append to the appropriate array:
   - Category correction -> `category_rules` (extract keywords from B section, target = user's choice, confidence_boost = 20)
   - Heading mismatch -> `heading_aliases` or `rejected_placements`

Create the JSON file if it doesn't exist. Initialize with:

```json
{"category_rules": [], "heading_aliases": [], "rejected_placements": [], "import_log": []}
```

## Error handling

- If a B file doesn't exist or can't be read, report and skip it
- If no headings found in B, treat the entire file as one section under its filename
- If `rapidfuzz` or `mistletoe` are not installed, rely on your own judgment for matching (you ARE a language model — semantic similarity is native to you)
- If `import-mappings.json` is malformed, back it up and reinitialize