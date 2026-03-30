# `/import-notes` Skill — Design Spec

**Date:** 2026-03-30
**Status:** Draft

## Overview

Given one or more loose `.md` files (B), merge their content into the existing documentation tree (A) using set-union semantics. Only content in B that doesn't already exist in A is added. The skill enforces CLAUDE.md conventions, generates JTD front matter, and learns from user corrections.

## Invocation

```
/import-notes fileB1.md fileB2.md ...
```

Arguments are paths to loose markdown files. No front matter expected. Files are typically small (<200 lines).

**Flags:**

| Flag | Behavior |
|---|---|
| (default) | Interactive — prompts for all decisions below 85% confidence |
| `--dry-run` | Runs stages 1-4 (parse, match, diff, split), reports proposed actions, writes nothing |
| `--auto` | Skips prompts for >= 85% confidence matches, only pauses for conflicts and low-confidence |

## Pipeline Stages

### Stage 1: PARSE

Parse each B file into a heading tree with content blocks.

**Data structure:**

```python
@dataclass
class Section:
    level: int          # 1, 2, or 3
    heading: str        # raw heading text
    content: str        # everything under this heading until next same/higher level
    children: list      # nested sub-sections
    source_file: str    # which B file this came from
    line_start: int     # for traceability
```

**Implementation:** `mistletoe` for AST-based heading tree extraction. Its native tree structure maps directly to the heading/content/children model. Falls back to regex splitter on `^#{1,3}\s` if mistletoe is not installed.

**Reuse:** `fix_headings.py` `title_case_heading()` + `TECH_TERMS` dict runs on each heading during parse (normalize before matching).

### Stage 2: MATCH

For each B section, find the best target location in A.

**Two-phase matching:**

#### Phase 2a — Category matching (which directory?)

Score each B section against the 9 top-level categories. Sources of signal:

| Signal | Weight | Method |
|---|---|---|
| Keyword hits | 40% | Check B's heading + first 200 chars against category keyword lists |
| Learned rules | 30% | `import-mappings.json` `category_rules` with `confidence_boost` |
| Heading overlap | 30% | Count how many B headings fuzzy-match headings in files under each category |

Keyword lists (bootstrapped, then refined by learning):

```python
CATEGORY_KEYWORDS = {
    "dotnet/": ["c#", "clr", "asp.net", "ef", "entity framework", "linq",
                "blazor", "razor", "nuget", "roslyn", ".net", "task", "thread"],
    "javascript/": ["angular", "react", "npm", "webpack", "css", "dom",
                     "typescript", "node", "redux", "pwa"],
    "architecture/": ["solid", "ddd", "design pattern", "oop", "uml",
                       "coupling", "cohesion", "cqrs", "event sourcing"],
    "distributed-systems/": ["microservice", "docker", "kafka", "signalr",
                              "zeromq", "websocket", "message queue", "grpc"],
    "data/": ["sql", "nosql", "mongodb", "cosmos", "index", "query",
              "stored proc", "transaction", "acid", "cap theorem"],
    "web-services/": ["rest", "http", "graphql", "swagger", "api",
                       "hateoas", "etag", "caching", "webapi"],
    "azure/": ["az-900", "cloud", "azure", "resource group", "arm",
               "app service", "functions", "devops"],
    "testing/": ["nunit", "xunit", "tdd", "bdd", "mock", "stub",
                  "integration test", "unit test", "assertion"],
    "devops/": ["git", "ci/cd", "yaml", "pipeline", "visual studio",
                "nuget", "deployment", "container"]
}
```

#### Phase 2b — File matching (which .md file within the category?)

Once category is selected, compare B sections against all files in that directory:

| Signal | Method |
|---|---|
| Heading text similarity | `rapidfuzz.fuzz.token_set_ratio` on heading text pairs |
| Hierarchy alignment | Bonus if H-level matches (H2 in B -> H2 in A) |
| Content token overlap | Jaccard similarity on word-level 3-gram shingles (top 50 words from each section) |

**Composite confidence score:**

```python
def composite_score(heading_sim, level_match, sibling_context_sim):
    """
    heading_sim: rapidfuzz score 0-100
    level_match: 1.0 if same heading level, 0.8 if off by one, 0.5 otherwise
    sibling_context_sim: avg similarity of neighboring headings (structural context)
    """
    return (
        0.60 * (heading_sim / 100) +
        0.15 * level_match +
        0.25 * sibling_context_sim
    )
```

Sibling context helps disambiguate generic headings like "Overview" or "Resources" — if surrounding headings also match, confidence is much higher.

**Batch optimization:** Use `rapidfuzz.process.cdist` to compute the full similarity matrix between all B headings and all A headings in one C++-optimized call, rather than looping `extractOne`.

**Confidence thresholds:**

| Score | Action |
|---|---|
| >= 85% | Auto-place, log decision |
| 70-84% | Propose placement, ask user to confirm |
| < 70% | Show top 3 candidates, ask user to pick or specify new file |

#### Optimization: Pre-computed heading index

On first run (or when stale), build and cache `docs/superpowers/data/heading-index.json`:

```json
{
  "version": "0dfc850",
  "generated": "2026-03-30",
  "files": {
    "dotnet/data-access/ef-core.md": {
      "fingerprint": "mtime_ns:size",
      "headings": [
        {"level": 1, "text": "EF Core", "normalized": "ef core", "line": 10},
        {"level": 2, "text": "Migrations", "normalized": "migrations", "line": 25},
        {"level": 3, "text": "Connection Strings", "normalized": "connection strings", "line": 55}
      ],
      "top_tokens": ["ef", "core", "migration", "dbcontext", "entity"]
    }
  }
}
```

Staleness check: `mtime_ns + size` per file (cheap stat call, avoids re-reading 150 files). Keyed by git HEAD — full rebuild when HEAD changes. Incremental update for individual file changes.

**Optional TF-IDF weighting (stdlib only):**

Weight keywords by how discriminating they are across the collection. "the" appears everywhere; "TPL" appears only in `dotnet/parallelism/`. No library needed:

```python
import math
from collections import Counter

def build_tfidf(files: dict[str, list[str]]) -> dict[str, dict[str, float]]:
    N = len(files)
    df = Counter()
    for words in files.values():
        df.update(set(words))
    tfidf = {}
    for path, words in files.items():
        tf = Counter(words)
        tfidf[path] = {
            w: (1 + math.log(c)) * math.log(N / df[w])
            for w, c in tf.items()
        }
    return tfidf
```

Cosine similarity between B's heading tokens and each file's TF-IDF vector gives a strong category signal with zero external deps.

### Stage 3: DIFF

Given a matched B section and its target A section, compute B - A.

**Three-tier comparison:**

#### Tier 1 — Heading dedup (exact or fuzzy)

```python
from rapidfuzz import fuzz

def headings_match(h_a: str, h_b: str) -> bool:
    return fuzz.token_sort_ratio(h_a.lower(), h_b.lower()) >= 80
```

If a heading in B already exists in A, move to tier 2. If no match, the entire section is new -> insert.

#### Tier 2 — Block-level dedup (paragraphs / bullet groups)

Split content under each heading into blocks (separated by blank lines). For each B block, check if A already has it:

```python
from difflib import SequenceMatcher

def block_is_duplicate(block_b: str, blocks_a: list[str], threshold=0.75) -> bool:
    b_normalized = normalize(block_b)
    for block_a in blocks_a:
        ratio = SequenceMatcher(None, normalize(block_a), b_normalized).ratio()
        if ratio >= threshold:
            return True
    return False

def normalize(text: str) -> str:
    text = re.sub(r'[*_`\[\]]', '', text.lower())
    return re.sub(r'\s+', ' ', text).strip()
```

**Three-band Jaccard thresholds for shingle-based comparison:**

| Jaccard score | Interpretation | Action |
|---|---|---|
| < 0.3 | Clearly new content | Insert into A |
| 0.3 - 0.7 | Partial overlap | Fall back to `difflib.ndiff` for line-level delta |
| > 0.7 | Duplicate | Skip |

Shingle size k=3 (3-word sliding window). k=2 is too noisy, k=4 misses short bullets.

```python
def shingle_set(text, k=3):
    words = text.lower().split()
    return frozenset(' '.join(words[i:i+k]) for i in range(max(len(words)-k+1, 1)))

def jaccard(set_a, set_b):
    if not set_a and not set_b:
        return 1.0
    return len(set_a & set_b) / len(set_a | set_b)
```

#### Tier 3 — Bullet-level dedup (within matching list blocks)

If both A and B have a bullet list under the same heading, compare individual bullets:

```python
def diff_bullet_lists(bullets_a: list[str], bullets_b: list[str]) -> list[str]:
    new_bullets = []
    for b in bullets_b:
        b_norm = normalize(b)
        if not any(fuzz.ratio(b_norm, normalize(a)) >= 80 for a in bullets_a):
            new_bullets.append(b)
    return new_bullets
```

**Paragraph fingerprinting for fast skip:**

Hash each paragraph after normalization. If hash matches, skip SequenceMatcher entirely:

```python
import hashlib

def fingerprint(block: str) -> str:
    normalized = re.sub(r'\s+', ' ', block.lower().strip())
    normalized = re.sub(r'[*_`\[\]()]', '', normalized)
    return hashlib.md5(normalized.encode()).hexdigest()
```

Store fingerprints in the heading index cache. On re-import of the same content, dedup is instant.

#### Heading-tree structural comparison

Greedy top-down alignment for shallow trees (max depth 3-4):

```python
def align_trees(tree_a, tree_b, threshold=65):
    alignments = []
    root_score = fuzz.token_set_ratio(tree_a["heading"], tree_b["heading"])
    if root_score < threshold:
        return []

    alignments.append((tree_a, tree_b, root_score))

    used_a = set()
    for child_b in tree_b["children"]:
        best_score, best_a = 0, None
        for i, child_a in enumerate(tree_a["children"]):
            if i in used_a:
                continue
            s = fuzz.token_set_ratio(child_b["heading"], child_a["heading"])
            if s > best_score:
                best_score, best_a = s, i

        if best_score >= threshold and best_a is not None:
            used_a.add(best_a)
            alignments.append((tree_a["children"][best_a], child_b, best_score))
            sub = align_trees(tree_a["children"][best_a], child_b, threshold)
            alignments.extend(sub[1:])
        else:
            alignments.append((None, child_b, 0))  # new section in B

    for i, child_a in enumerate(tree_a["children"]):
        if i not in used_a:
            alignments.append((child_a, None, 0))

    return alignments
```

**Hierarchy-aware scoring bonus:**

```python
def hierarchy_bonus(level_a: int, level_b: int) -> float:
    if level_a == level_b:
        return 1.0
    if abs(level_a - level_b) == 1:
        return 0.7   # adjacent levels (H2 vs H3) — common
    return 0.3        # H1 vs H3 — suspicious
```

#### Conflict handling

If B has content under a heading that exists in A but differs substantially (SequenceMatcher ratio between 0.3 and 0.75):

```
!! Conflict in dotnet/data-access/ef-core.md -> ## Migrations

A has:
  > Run `dotnet ef migrations add` to create a new migration.

B has:
  > Use the PMC command `Add-Migration` in Visual Studio.

[k]eep A / [r]eplace with B / [m]erge both / [s]kip?
```

### Stage 4: SPLIT

If a B file's sections map to different categories with high confidence (>= 70% for each part, and different categories):

```
fileB.md spans multiple categories:
  ## Docker Networking  -> distributed-systems/docker.md (92%)
  ## Azure Container Instances  -> azure/ (new file) (88%)

Split into 2 targets? [y/n]
```

If user confirms, process each part independently through stages 2-3.

### Stage 5: NORMALIZE

Apply CLAUDE.md conventions to all new content before writing:

| Convention | Implementation |
|---|---|
| Heading title case | Call `fix_headings.py` `title_case_heading()` + `TECH_TERMS` |
| Reference-style external links | Regex: find `[text](https?://...)`, extract to end of file as `[N]: url`, replace with `text [N]` |
| Semantic entity formatting | LLM pass: bold patterns/concepts, italic practices, code for tools/frameworks |
| Kebab-case filenames | `re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-') + '.md'` |
| No emoji shortcodes | `re.sub(r':[a-z_]+:', '', text)` |
| No bare URLs | Detect and wrap in reference-style links |

### Stage 6: WRITE

**For existing files (upsert sections):**

1. Read target file
2. Find insertion point (after the last existing section at same level, or at end before nav backlinks)
3. Insert new sections
4. Update `last_modified_date` in front matter to current date
5. Preserve existing content untouched

**For new files:**

1. Generate JTD front matter — reuse `add_front_matter.py` functions:
   - `extract_title()` from H1 or filename
   - `build_hierarchy()` for parent/grand_parent from directory
   - `compute_nav_order()` for alphabetical ordering within parent
   - `generate_front_matter()` for full YAML block
2. Add nav backlinks — call `update_nav2.py` `get_correct_nav()` for depth-appropriate links
3. Write file

### Stage 7: HOUSEKEEP

1. Update `STRUCTURE.md` tree (patch incrementally for new files)
2. Run `verify_nav.py` to confirm all new/modified files have correct backlinks
3. Update `CHANGELOG.md` with import summary
4. Report: files created, files modified, sections added, sections skipped as duplicates

### Stage 8: LEARN

After each import run, update `docs/superpowers/data/import-mappings.json`.

#### Automatic logging (every run)

```json
{
  "import_log": [
    {
      "date": "2026-03-30",
      "source": "notes-docker.md",
      "actions": [
        {"type": "insert", "target": "distributed-systems/docker.md", "heading": "## Overlay Networks"},
        {"type": "skip_dup", "target": "distributed-systems/docker.md", "heading": "## Volumes"},
        {"type": "new_file", "target": "distributed-systems/docker-compose.md"}
      ]
    }
  ]
}
```

#### User correction capture (on prompt)

When the skill proposes a placement and the user corrects it:

```
Proposed: devops/ci-cd.md (65%)
User chose: distributed-systems/docker.md

Save as rule for future imports? [y/n]
```

If yes, appends to `category_rules`:

```json
{
  "keywords": ["docker compose", "compose file", "docker-compose.yml"],
  "target": "distributed-systems/",
  "confidence_boost": 20,
  "source": "user_correction",
  "date": "2026-03-30"
}
```

When the skill proposes a heading match and the user corrects:

```
Proposed: ## EF Migrations -> dotnet/data-access/ef-core.md ## Migrations
User said: no, this is about Flyway, put it in data/sql/

Save heading alias? [y/n]
```

If yes, appends to `rejected_placements` to avoid the same mistake.

#### Mappings file schema

```json
{
  "category_rules": [
    {
      "keywords": ["entity framework", "ef core", "dbcontext", "migration"],
      "target": "dotnet/data-access/",
      "confidence_boost": 15,
      "source": "user_correction",
      "date": "2026-03-30"
    }
  ],
  "heading_aliases": [
    {
      "incoming": "EF Migrations",
      "canonical": "## Migrations",
      "target_file": "dotnet/data-access/ef-core.md",
      "source": "user_correction"
    }
  ],
  "rejected_placements": [
    {
      "keywords": ["docker compose"],
      "rejected_target": "devops/",
      "correct_target": "distributed-systems/",
      "reason": "user said docker content belongs in distributed-systems"
    }
  ]
}
```

#### How the skill improves over runs

```
Run 1:  User imports 5 files, corrects 3 placements
        -> 3 category_rules, 1 rejected_placement saved

Run 2:  Same domain, 3 new files. The 3 rules boost
        correct categories by 20 points each. 0 corrections needed.

Run 5:  User imports a file touching a new topic (e.g. gRPC).
        No rules match -> low confidence -> prompt.
        User says: distributed-systems/
        -> new rule: ["grpc", "protobuf", "proto"] -> distributed-systems/

Run 10: import-mappings.json has 15 rules. Category matching
        is essentially deterministic for this repo's domain.
```

Rules can be reviewed via `--review-rules` flag or by directly editing the JSON. Rules older than 6 months without reuse can be flagged for review.

Feedback memories at `~/.claude/projects/D--GIT-Tutorial/memory/` are also read as supplementary context at the start of each run.

## Reuse From Existing Scripts

| Script | What the skill reuses |
|---|---|
| `add_front_matter.py` | `extract_title()`, `build_hierarchy()`, `compute_nav_order()`, `generate_front_matter()`, `yaml_value()` |
| `fix_headings.py` | `title_case_heading()`, `TECH_TERMS` dict, `SMALL_WORDS` set |
| `update_nav2.py` | `get_correct_nav()`, `update_file()` |
| `verify_nav.py` | Post-import validation pass |

## Dependencies

| Package | Type | Purpose | Size |
|---|---|---|---|
| `rapidfuzz` | pip install | Heading matching, confidence scoring, `process.cdist` | ~2MB, C++ extension |
| `mistletoe` | pip install (optional) | Markdown AST, heading tree extraction | ~50KB, pure Python |
| `difflib` | stdlib | Line-level and block-level content comparison | 0 |
| Python 3.10+ | system | dataclasses, pathlib, json, hashlib, math | 0 |

Regex-based heading parser as fallback if `mistletoe` is not installed.

## File Layout

```
docs/superpowers/
├── data/
│   ├── import-mappings.json      # learned rules + import log
│   └── heading-index.json        # cached A heading tree (auto-generated)
├── scripts/
│   ├── add_front_matter.py       # existing — reuse functions
│   ├── fix_headings.py           # existing — reuse title_case_heading
│   ├── update_nav2.py            # existing — reuse get_correct_nav
│   ├── verify_nav.py             # existing — post-import validation
│   └── import_helpers.py         # NEW — shared functions for parse/match/diff
└── specs/
    └── 2026-03-30-import-notes-design.md  # this file

.claude/commands/
└── import-notes.md               # skill file (orchestration + LLM judgment)
```

The skill file (`.claude/commands/import-notes.md`) orchestrates the pipeline interactively, calling Python scripts for deterministic operations and using LLM judgment for semantic matching, normalization, and conflict resolution.

## What NOT to over-engineer

- **No embeddings or ML** — keyword heuristics + rapidfuzz + learned rules are sufficient for 150 files in 9 well-defined categories
- **No MinHash/LSH** — direct Jaccard on shingle sets is fast enough at this scale (~3000 paragraphs)
- **No full tree edit distance** — greedy top-down alignment handles max-depth-4 trees
- **No external services** — everything runs locally, offline