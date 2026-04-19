# PRDC Links Catalog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a non-interactive Python tool (PRDC) that scans wiki Markdown under fixed top-level folders, extracts and classifies link destinations, merges results into `/_memoize/LINKS.json`, skips nav and `NONE` links per spec, rewrites `localhost` links to italics in source files, and passes a focused pytest suite.

**Architecture:** A small package `scripts/prdc/` with single-purpose modules (`normalize`, `classify`, `extract`, `scan`, `memo`, `localhost`, `nav_filter`, `cli`). `markdown-it-py` parses Markdown to tokens; hrefs are canonicalized then classified; `memo.merge` applies freeze rules; the CLI walks the repo, updates files and JSON, exits non-zero on unrecoverable errors.

**Tech Stack:** Python 3.11+, `markdown-it-py` 3.x, `pytest` 8.x, stdlib (`pathlib`, `urllib.parse`, `json`, `re`, `argparse`).

**Spec:** `docs/superpowers/specs/2026-04-20-prdc-links-memo-design.md`

**Note:** Optional git worktree (from superpowers brainstorming) is nice for isolation but not required; default is to implement on a clean branch in the main clone.

---

## File structure (create or modify)

| Path | Responsibility |
|------|------------------|
| `scripts/requirements-prdc.txt` | Pinned runtime + test deps for PRDC |
| `pytest.ini` | `pythonpath = scripts`, `testpaths = tests/prdc` |
| `scripts/prdc/__init__.py` | Package marker (empty) |
| `scripts/prdc/__main__.py` | Delegates to `cli.main()` |
| `scripts/prdc/cli.py` | argparse, orchestrates scan → merge → write |
| `scripts/prdc/normalize.py` | Canonical memo `url` for http(s), mailto, tel, path-like |
| `scripts/prdc/classify.py` | Maps canonical href + context → category string |
| `scripts/prdc/nav_filter.py` | Returns True if a link should be excluded as hub/nav |
| `scripts/prdc/extract.py` | Markdown-it token walk → list of `(href, link_text)` |
| `scripts/prdc/scan.py` | Enumerate in-scope `.md` paths under wiki dirs |
| `scripts/prdc/memo.py` | Load/save `LINKS.json`, deterministic sort, merge rules |
| `scripts/prdc/localhost.py` | Rewrite `http(s)://localhost:PORT` and `127.0.0.1` links to `*text*` |
| `tests/prdc/test_normalize.py` | Golden tests for normalization |
| `tests/prdc/test_memo.py` | Merge / freeze / `review` reassessment |
| `tests/prdc/test_classify.py` | Representative classification rows |
| `tests/prdc/test_localhost.py` | String rewrite before/after |
| `tests/prdc/test_nav_filter.py` | Nav link detection |
| `tests/prdc/test_extract.py` | Inline + reference link extraction (synthetic markdown) |

---

## Phase 1: Dependencies and layout

### Task 1: Pin dependencies and pytest discovery

**Files:**
- Create: `scripts/requirements-prdc.txt`
- Create: `pytest.ini`

- [ ] **Step 1: Add `scripts/requirements-prdc.txt`**

```text
markdown-it-py==3.0.0
pytest==8.3.5
```

- [ ] **Step 2: Add `pytest.ini` at repository root**

```ini
[pytest]
pythonpath = scripts
testpaths = tests/prdc
```

- [ ] **Step 3: Install deps (developer machine)**

Run:

```bash
pip install -r scripts/requirements-prdc.txt
```

Expected: installs `markdown-it-py` and `pytest` without errors.

- [ ] **Step 4: Commit**

```bash
git add scripts/requirements-prdc.txt pytest.ini
git commit -m "chore(prdc): add requirements and pytest config"
```

---

### Task 2: Package skeleton and empty `__init__`

**Files:**
- Create: `scripts/prdc/__init__.py`
- Create: `scripts/prdc/__main__.py`

- [ ] **Step 1: Create `scripts/prdc/__init__.py`**

```python
"""PRDC: scan wiki Markdown links, classify, memoize to /_memoize/LINKS.json."""
```

- [ ] **Step 2: Create `scripts/prdc/__main__.py`**

```python
from prdc.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Verify import path**

Run from repository root:

```bash
set PYTHONPATH=scripts
python -m prdc --help
```

Expected (after `cli.py` exists in Task 10): help text. Until `cli.py` lands, this step fails by design — re-run after Task 10.

- [ ] **Step 4: Commit**

```bash
git add scripts/prdc/__init__.py scripts/prdc/__main__.py
git commit -m "chore(prdc): add package entrypoints"
```

---

## Phase 2: Normalization (TDD)

### Task 3: HTTP(S) normalization and tracking strip — tests first

**Files:**
- Create: `tests/prdc/test_normalize.py`
- Create: `scripts/prdc/normalize.py` (minimal stubs until Step 4)

- [ ] **Step 1: Create stub `scripts/prdc/normalize.py`**

```python
from __future__ import annotations


def normalize_http_url(href: str) -> str:
    raise NotImplementedError


def normalize_mailto_url(href: str) -> str:
    raise NotImplementedError


def normalize_tel_url(href: str) -> str:
    raise NotImplementedError


def normalize_path_destination(href: str, source_file: str, repo_root: str) -> str:
    raise NotImplementedError


def canonical_memo_url(href: str, source_file: str, repo_root: str) -> str:
    raise NotImplementedError
```

- [ ] **Step 2: Write failing tests in `tests/prdc/test_normalize.py`**

```python
import os

from prdc.normalize import normalize_http_url


def test_http_lowercase_scheme_host_strip_default_port():
    assert (
        normalize_http_url("HTTPS://EXAMPLE.COM:443/foo/")
        == "https://example.com/foo"
    )


def test_http_strip_tracking_sorts_query_keeps_meaningful():
    assert (
        normalize_http_url(
            "https://example.com/path?utm_source=x&foo=2&utm_medium=y&bar=1"
        )
        == "https://example.com/path?bar=1&foo=2"
    )


def test_http_retains_fragment():
    a = normalize_http_url("https://example.com/doc#a")
    b = normalize_http_url("https://example.com/doc#b")
    assert a == "https://example.com/doc#a"
    assert b == "https://example.com/doc#b"
    assert a != b


def test_http_root_path_normalization():
    assert normalize_http_url("https://example.com") in (
        "https://example.com/",
        "https://example.com",
    )
```

Pick one canonical root form in implementation and adjust this test to match the spec’s “bare host uses `/` consistently” rule (document the chosen string in a one-line comment in `normalize_http_url`).

- [ ] **Step 3: Run tests (expect failure)**

Run:

```bash
pytest tests/prdc/test_normalize.py -v
```

Expected: `NotImplementedError` or failures.

- [ ] **Step 4: Replace `normalize_http_url` with full implementation in `scripts/prdc/normalize.py`**

Use `urllib.parse.urlparse`, `urlunparse`, `parse_qsl`, `urlencode`, and `urllib.parse.unquote` for path decoding. Implement:

- Lowercase scheme and host (split userinfo if present; only lowercase hostname for IDNA use `encoding="idna"` on the host label string when it is ASCII-safe; if `UnicodeError`, leave host as lowercased original segment).
- Strip `:443` on `https` and `:80` on `http` from the host portion of `netloc`.
- Path: `unquote` once; normalize with `pathlib.PurePosixPath` when the path starts with `/`; if the path does not start with `/`, treat as empty or relative per URL rules (http paths should start with `/` after parse — if empty, set to `/`).
- Trailing slash: if `len(path) > 1` and path ends with `/`, remove one trailing `/`.
- Query: drop pairs whose **name** matches `TRACKING_KEYS` case-insensitively; sort remaining pairs by key case-insensitive, then key original byte order as tiebreaker; rebuild query with `urlencode(..., doseq=True)`.
- Fragment: keep unchanged (including empty vs missing distinction: preserve absence of `#` vs `#` with empty fragment if `urlparse` distinguishes; if not, do not invent fragments).

Define at module level:

```python
TRACKING_KEYS = frozenset({
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "gclid",
    "fbclid",
    "msclkid",
    "mc_eid",
    "yclid",
    "_ga",
    "spm",
})
```

- [ ] **Step 5: Run tests**

Run:

```bash
pytest tests/prdc/test_normalize.py::test_http_lowercase_scheme_host_strip_default_port -v
pytest tests/prdc/test_normalize.py::test_http_strip_tracking_sorts_query_keeps_meaningful -v
pytest tests/prdc/test_normalize.py::test_http_retains_fragment -v
pytest tests/prdc/test_normalize.py::test_http_root_path_normalization -v
```

Expected: all pass after aligning `test_http_root_path_normalization` with the chosen root canonicalization.

- [ ] **Step 6: Commit**

```bash
git add scripts/prdc/normalize.py tests/prdc/test_normalize.py
git commit -m "feat(prdc): normalize http(s) URLs for memo keys"
```

---

### Task 4: `mailto` / `tel` / path normalization tests and implementation

**Files:**
- Modify: `tests/prdc/test_normalize.py`
- Modify: `scripts/prdc/normalize.py` (mailto, tel, path helpers and `canonical_memo_url`)

- [ ] **Step 1: Append tests to `tests/prdc/test_normalize.py`**

```python
from pathlib import Path

from prdc.normalize import (
    canonical_memo_url,
    normalize_mailto_url,
    normalize_path_destination,
    normalize_tel_url,
)


def test_mailto_trim_lowercase_scheme_and_host(tmp_path: Path):
    assert (
        normalize_mailto_url("  MAILTO:User@Example.COM?utm_source=1&subject=Hi  ")
        == "mailto:User@example.com?subject=Hi"
    )


def test_tel_strips_noise():
    assert normalize_tel_url("TEL:+1 (555) 444-3322") == "tel:+15554443322"


def test_path_strips_fragment_posix(tmp_path: Path):
    root = tmp_path
    src = root / "docs" / "a.md"
    target = root / "other" / "b.md"
    src.parent.mkdir(parents=True)
    target.parent.mkdir(parents=True)
    src.write_text("x", encoding="utf-8")
    target.write_text("y", encoding="utf-8")
    href = "../other/b.md#section"
    got = normalize_path_destination(
        href, source_file=str(src), repo_root=str(root)
    )
    assert got == "other/b.md"
    assert "#" not in got


def test_canonical_routes_https_mailto_path(tmp_path: Path):
    root = tmp_path
    d = root / "p"
    d.mkdir()
    (d / "x.md").write_text("z", encoding="utf-8")
    assert (
        canonical_memo_url(
            "HTTPS://Ex.AMple/", str(d / "x.md"), str(root)
        ).startswith("https://ex.ample/")
    )
    assert canonical_memo_url(
        "mailto:A@B.co", str(d / "x.md"), str(root)
    ).startswith("mailto:")
    assert canonical_memo_url("./x.md", str(d / "y.md"), str(root)) == "p/x.md"
```

Create `p/y.md` as an empty file in the test so `./x.md` resolves relative to `p/y.md`.

Adjust the last test: create `root/p/y.md` and `root/p/x.md`, call `canonical_memo_url("./x.md", str(root / "p" / "y.md"), str(root))`.

- [ ] **Step 2: Implement `normalize_mailto_url`**

Rules from spec:

- `strip()` ASCII whitespace on full href.
- Lowercase scheme `mailto:`.
- Parse `mailto:` localpart@host?query using regex or `urlparse` (note `mailto` bodies need care); lowercase **host** only.
- Apply the same tracking-key strip to query parameter names as HTTP.

- [ ] **Step 3: Implement `normalize_tel_url`**

- Lowercase scheme.
- Keep leading `+` if present.
- Remove ASCII space, `(`, `)`, `-` from the dial string; keep digits and leading `+`.

- [ ] **Step 4: Implement `normalize_path_destination`**

- Split href on `#`, keep only the path portion (**F2**).
- Resolve `(Path(source_file).parent / path_part).resolve()` then `relative_to(Path(repo_root))` when possible; return `as_posix()`.
- On `ValueError` from `relative_to`, return a best-effort POSIX string: normalize `./`, collapse separators using `PurePosixPath`, still without fragment, and let callers classify as `review` when file does not exist (classification layer checks existence with `Path(repo_root)/rel`).

- [ ] **Step 5: Implement `canonical_memo_url`**

```python
def canonical_memo_url(href: str, source_file: str, repo_root: str) -> str:
    h = href.strip()
    lower = h.lower()
    if lower.startswith("mailto:"):
        return normalize_mailto_url(h)
    if lower.startswith("tel:"):
        return normalize_tel_url(h)
    if lower.startswith("http://") or lower.startswith("https://"):
        return normalize_http_url(h)
    return normalize_path_destination(h, source_file, repo_root)
```

- [ ] **Step 6: Run full normalize tests**

```bash
pytest tests/prdc/test_normalize.py -v
```

Expected: all pass.

- [ ] **Step 7: Commit**

```bash
git add scripts/prdc/normalize.py tests/prdc/test_normalize.py
git commit -m "feat(prdc): mailto, tel, path memo keys"
```

---

## Phase 3: Memo merge semantics

### Task 5: Memo load, save, merge

**Files:**
- Create: `scripts/prdc/memo.py`
- Create: `tests/prdc/test_memo.py`

- [ ] **Step 1: Write failing tests `tests/prdc/test_memo.py`**

```python
import json
from pathlib import Path

from prdc.memo import load_links, merge_memo, save_links


def test_load_missing_returns_empty(tmp_path: Path):
    p = tmp_path / "LINKS.json"
    assert load_links(p) == []


def test_save_sorts_deterministically(tmp_path: Path):
    p = tmp_path / "LINKS.json"
    rows = [
        {"url": "b", "category": "z"},
        {"url": "a", "category": "m"},
    ]
    save_links(p, rows)
    data = json.loads(p.read_text(encoding="utf-8"))
    assert data == [
        {"url": "a", "category": "m"},
        {"url": "b", "category": "z"},
    ]


def test_merge_freezes_non_review(tmp_path: Path):
    existing = [{"url": "https://example.com/a", "category": "book"}]
    computed = {"https://example.com/a": "review"}
    merged = merge_memo(existing, computed)
    assert merged == [{"url": "https://example.com/a", "category": "book"}]


def test_merge_updates_review(tmp_path: Path):
    existing = [{"url": "https://example.com/a", "category": "review"}]
    computed = {"https://example.com/a": "book"}
    merged = merge_memo(existing, computed)
    assert merged == [{"url": "https://example.com/a", "category": "book"}]


def test_merge_preserves_stale_urls_not_in_computed(tmp_path: Path):
    existing = [{"url": "https://old.example/", "category": "gist"}]
    computed: dict[str, str] = {}
    merged = merge_memo(existing, computed)
    assert merged == [{"url": "https://old.example/", "category": "gist"}]


def test_merge_inserts_new(tmp_path: Path):
    existing: list[dict[str, str]] = []
    computed = {"https://new.example/": "review"}
    merged = merge_memo(existing, computed)
    assert merged == [{"url": "https://new.example/", "category": "review"}]
```

- [ ] **Step 2: Implement `scripts/prdc/memo.py`**

```python
from __future__ import annotations

import json
from pathlib import Path


def load_links(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("LINKS.json must be a JSON array")
    out: list[dict[str, str]] = []
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError("each row must be an object")
        if set(item.keys()) != {"url", "category"}:
            raise ValueError("rows must have only url and category keys")
        out.append({"url": str(item["url"]), "category": str(item["category"])})
    return out


def save_links(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    sorted_rows = sorted(rows, key=lambda r: (r["url"], r["category"]))
    path.write_text(
        json.dumps(sorted_rows, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def merge_memo(
    existing_rows: list[dict[str, str]],
    computed_categories: dict[str, str],
) -> list[dict[str, str]]:
    by_url: dict[str, str] = {}
    for row in existing_rows:
        by_url[row["url"]] = row["category"]
    for url, new_cat in computed_categories.items():
        old_cat = by_url.get(url)
        if old_cat is None:
            by_url[url] = new_cat
        elif old_cat == "review":
            by_url[url] = new_cat
    return [{"url": u, "category": c} for u, c in sorted(by_url.items())]
```

Verify against all six tests: URLs that appear only in `existing_rows` and not in `computed_categories` must remain because `by_url` is seeded from `existing_rows` and only keys present in `computed_categories` are updated.

- [ ] **Step 3: Run memo tests**

```bash
pytest tests/prdc/test_memo.py -v
```

Expected: all pass.

- [ ] **Step 4: Commit**

```bash
git add scripts/prdc/memo.py tests/prdc/test_memo.py
git commit -m "feat(prdc): LINKS.json load, save, merge semantics"
```

---

## Phase 4: Classification

### Task 6: Classification rules

**Files:**
- Create: `scripts/prdc/classify.py`
- Create: `tests/prdc/test_classify.py`

- [ ] **Step 1: Add tests `tests/prdc/test_classify.py`**

```python
from prdc.classify import classify_href, classify_image_destination


def test_none_badges_shields():
    assert (
        classify_href("https://img.shields.io/badge/cov-green.svg", is_image=True)
        is None
    )


def test_npm_package():
    assert (
        classify_href("https://www.npmjs.com/package/lodash", is_image=False)
        == "npm package"
    )


def test_github_repo_not_gist():
    assert (
        classify_href("https://github.com/jbogard/MediatR", is_image=False)
        == "github source repository"
    )


def test_stackoverflow_so():
    assert (
        classify_href("https://stackoverflow.com/questions/1/x", is_image=False) == "SO"
    )


def test_image_png_review():
    assert classify_image_destination("https://x/y.PNG") == "review"


def test_google_drive_resource():
    assert (
        classify_href("https://drive.google.com/file/d/abc/view", is_image=False)
        == "resource"
    )
```

Define `classify_image_destination` as a thin wrapper that forces image-like handling (`is_image=True`) for extension checks.

- [ ] **Step 2: Implement `scripts/prdc/classify.py`**

Implement `classify_href(href: str, *, is_image: bool) -> str | None`:

- Return `None` for **`NONE`** before other rules. Concrete `NONE` heuristics (first match returns `None`):

```python
import re
from urllib.parse import urlparse


def _is_none_href(href: str) -> bool:
    u = href.lower()
    if "img.shields.io" in u:
        return True
    if "codecov.io" in u and "/badge" in u:
        return True
    if "sonarcloud.io" in u and "api/project_badges" in u:
        return True
    if "travis-ci.org" in u or "api.travis-ci.com" in u:
        return True
    if "dev.azure.com" in u and "_build" in u:
        return True
    if "github.com" in u and "/workflows/" in u and "badge.svg" in u:
        return True
    return False
```

- If `is_image` and destination has extension `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.svg` (case-insensitive) and `_is_none_href` is false, return `"review"` unless a higher-priority rule says diagram (optional: if `mermaid` in path, return `"diagram"`).
- If path ends with `.pdf` (case-insensitive), return `"resource"`.
- If href matches Google Drive / Docs / Sheets hosts or `1drv.ms` or `onedrive.live.com`, return `"resource"`.
- If path ends with a **sample code** extension: `.cs`, `.py`, `.js`, `.ts`, `.java`, `.go`, `.rs`, `.cpp`, `.cxx`, `.h`, `.sql`, `.ps1`, `.sh`, `.vb`, `.fs`, return `"sample"` (case-insensitive suffix).
- Apply **Appendix A url classify** in this **fixed order** (first match wins) on `http`/`https` **canonical** URLs:

```python
def classify_https(canonical: str) -> str:
    u = canonical.lower()
    if u.startswith("https://www.npmjs.com/package/"):
        return "npm package"
    if u.startswith("https://www.nuget.org/packages"):
        return "nuget package"
    if "blogspot." in urlparse(canonical).netloc.lower():
        return "blog"
    if u.startswith("http://blogs."):
        return "blog"
    if urlparse(canonical).path.lower().endswith(".pdf"):
        return "resource"
    if re.fullmatch(
        r"https?://github\.com/[^/]+/[^/]+/?",
        canonical,
        flags=re.IGNORECASE,
    ):
        return "github source repository"
    if "mongodb.github.io" in urlparse(canonical).netloc.lower():
        return "technical documentation"
    if u.startswith("http://en.wikipedia.org/wiki"):
        return "knowledge article"
    if "hub.docker.com/r/" in u:
        return "docker image"
    if u.startswith("https://learn.microsoft.com"):
        return "knowledge article"
    if u.startswith("https://social.technet.microsoft.com"):
        return "knowledge article"
    if u.startswith("https://docs.microsoft.com"):
        return "technical documentation"
    if "msdn.microsoft.com" in urlparse(canonical).netloc.lower():
        return "technical documentation"
    if "technet.microsoft.com" in urlparse(canonical).netloc.lower():
        return "technical documentation"
    if "developers.google.com" in urlparse(canonical).netloc.lower():
        return "technical documentation"
    if u.startswith("https://learning.oreilly.com"):
        return "book"
    if u.startswith("https://www.youtube.com") or u.startswith("https://youtu.be"):
        return "YT"
    if u.startswith("https://gist.github.com"):
        return "gist"
    if u.startswith("https://www.slideshare.net"):
        return "lecture"
    if "codereview.stackexchange.com" in urlparse(canonical).netloc.lower():
        return "SO"
    if "stackoverflow.com" in urlparse(canonical).netloc.lower():
        return "SO"
    if "experts-exchange" in urlparse(canonical).netloc.lower():
        return "SO"
    return "review"
```

- For non-http(s) schemes (except `mailto`/`tel` handled elsewhere), return `"review"` unless image/pdf/sample rules already matched.

Wire `classify_href` to call `_is_none_href` first, then image rules, then `https` rules if `canonical.lower().startswith("http")`, else `"review"`.

Add at module bottom:

```python
def classify_image_destination(href: str) -> str:
    c = classify_href(href, is_image=True)
    assert c is not None
    return c
```

For image destinations, `NONE` should not apply to normal PNG hosts; if `_is_none_href` is true for an image URL, return `"review"` anyway or skip — pick one: if `None`, treat as `"review"` for images so the function always returns `str`:

```python
def classify_image_destination(href: str) -> str:
    c = classify_href(href, is_image=True)
    return "review" if c is None else c
```

Update `tests/prdc/test_classify.py` `test_image_png_review` accordingly if shields return `None`.

- [ ] **Step 3: Run classification tests**

```bash
pytest tests/prdc/test_classify.py -v
```

Adjust regex or ordering until all tests pass.

- [ ] **Step 4: Commit**

```bash
git add scripts/prdc/classify.py tests/prdc/test_classify.py
git commit -m "feat(prdc): link classification and NONE filtering"
```

---

## Phase 5: Nav filter and localhost rewrite

### Task 7: Nav link filter

**Files:**
- Create: `scripts/prdc/nav_filter.py`
- Create: `tests/prdc/test_nav_filter.py`

- [ ] **Step 1: Tests `tests/prdc/test_nav_filter.py`**

```python
from prdc.nav_filter import is_navigation_link


def test_excludes_double_angle_index():
    assert is_navigation_link("<<", "./index.md") is True


def test_excludes_home_readme():
    assert is_navigation_link("home", "../README.md") is True


def test_does_not_exclude_normal_link():
    assert is_navigation_link("MediatR", "https://github.com/jbogard/MediatR") is False
```

- [ ] **Step 2: Implement `scripts/prdc/nav_filter.py`**

```python
def is_navigation_link(link_text: str, href: str) -> bool:
    t = link_text.strip()
    if t in {"<", "<<", ">", ">>"}:
        if "index.md" in href.replace("\\", "/").lower():
            return True
    if t.lower() == "home":
        h = href.replace("\\", "/").lower()
        if h.endswith("readme.md") or "/readme.md" in h:
            return True
    return False
```

- [ ] **Step 3: Run tests**

```bash
pytest tests/prdc/test_nav_filter.py -v
```

- [ ] **Step 4: Commit**

```bash
git add scripts/prdc/nav_filter.py tests/prdc/test_nav_filter.py
git commit -m "feat(prdc): exclude hub navigation links"
```

---

### Task 8: Localhost rewrite

**Files:**
- Create: `scripts/prdc/localhost.py`
- Create: `tests/prdc/test_localhost.py`

- [ ] **Step 1: Tests `tests/prdc/test_localhost.py`**

```python
from prdc.localhost import rewrite_localhost_links


def test_inline_localhost_to_italic():
    src = "See [click here](http://localhost:3000/foo) end."
    got = rewrite_localhost_links(src)
    assert got == "See *click here* end."


def test_reference_style():
    src = "[click]: http://localhost:8080/\n\n[click] here"
    got = rewrite_localhost_links(src)
    assert "http://localhost:8080" not in got
    assert "*click*" in got or "click" in got
```

Adjust the second assertion after picking exact reference rewrite behavior: either remove the ref definition line and convert `[click]` to `*click*` inline, or replace definition target with text-only. Document chosen behavior in a module docstring.

- [ ] **Step 2: Implement `scripts/prdc/localhost.py`**

Use regular expressions with a small state machine or sequential passes:

- Inline: `\[([^\]]*)\]\(\s*(https?://(?:localhost|127\.0\.0\.1):\d+[^)]*)\)` → `*\1*`
- Reference definitions: `^\[([^\]]+)\]:\s*(https?://(?:localhost|127\.0\.0\.1):\d+\S*)\s*$` (multiline `re.M`) — remove the line and ensure references `[label]` resolve by replacing occurrences of `[label]` not followed by `(` with `*label*` when the label was a localhost ref only (minimal approach: delete definition line; replace standalone `[foo]` with `*foo*` if `foo` had only localhost definition — keep scope tight to avoid breaking footnotes).

Minimal safe approach for v1:

- Only rewrite **inline** localhost links (first regex).
- For **reference** localhost destinations: remove the `^\[id\]: http://localhost:...$` line and replace every `[id]` (word boundary, not image) with `*id*` when `id` contains no spaces.

Implement exactly what makes both tests pass.

- [ ] **Step 3: Run tests**

```bash
pytest tests/prdc/test_localhost.py -v
```

- [ ] **Step 4: Commit**

```bash
git add scripts/prdc/localhost.py tests/prdc/test_localhost.py
git commit -m "feat(prdc): rewrite localhost links to italics"
```

---

## Phase 6: Markdown extraction

### Task 9: Token extraction

**Files:**
- Create: `scripts/prdc/extract.py`
- Create: `tests/prdc/test_extract.py`

- [ ] **Step 1: Tests `tests/prdc/test_extract.py`**

```python
from prdc.extract import extract_links


def test_inline_link():
    md = "Hello [t](https://example.com/x) there."
    assert extract_links(md) == [("https://example.com/x", "t")]


def test_reference_link():
    md = """[t][ref]

[ref]: https://example.com/y
"""
    got = extract_links(md)
    assert ("https://example.com/y", "t") in got
```

- [ ] **Step 2: Implement `scripts/prdc/extract.py`**

```python
from __future__ import annotations

from collections.abc import Iterator

from markdown_it import MarkdownIt


def _walk(tokens) -> Iterator:
    for t in tokens:
        yield t
        if t.children:
            yield from _walk(t.children)


def extract_links(markdown: str) -> list[tuple[str, str]]:
    md = MarkdownIt("commonmark")
    tokens = md.parse(markdown)
    out: list[tuple[str, str]] = []
    for tok in _walk(tokens):
        if tok.type == "inline" and tok.children:
            for child in tok.children:
                if child.type == "link_open":
                    href = child.attrGet("href") or ""
                    text = ""
                    sib = child.nxt
                    while sib and sib.type != "link_close":
                        if sib.type == "text":
                            text += sib.content
                        elif sib.type == "code_inline":
                            text += "`" + sib.content + "`"
                        sib = sib.nxt
                    out.append((href, text))
                if child.type == "image":
                    href = child.attrGet("src") or ""
                    alt = child.attrGet("alt") or ""
                    out.append((href, alt))
    return out
```

Validate `child.nxt` exists on markdown-it token objects; if the API differs, use index-based walk over `tok.children` list and track `link_open` / `link_close` pairs per markdown-it-py documentation.

- [ ] **Step 3: Run tests**

```bash
pytest tests/prdc/test_extract.py -v
```

Fix traversal until both cases pass.

- [ ] **Step 4: Commit**

```bash
git add scripts/prdc/extract.py tests/prdc/test_extract.py
git commit -m "feat(prdc): extract markdown links via markdown-it-py"
```

---

## Phase 7: Scanning and CLI

### Task 10: Enumerate wiki markdown files

**Files:**
- Create: `scripts/prdc/scan.py`
- Create: `tests/prdc/test_integration_scan.py`

- [ ] **Step 1: Implement `scripts/prdc/scan.py`**

```python
from __future__ import annotations

from pathlib import Path

WIKI_TOP_LEVEL_DIRS = (
    "ai",
    "architecture",
    "azure",
    "data",
    "devops",
    "distributed-systems",
    "dotnet",
    "javascript",
    "testing",
    "web-services",
)

ROOT_EXCLUDE_NAMES = {
    "README.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "CONTRIBUTORS.md",
    "LICENSE",
    "STRUCTURE.md",
}


def iter_wiki_markdown_files(repo_root: Path) -> list[Path]:
    out: list[Path] = []
    for name in WIKI_TOP_LEVEL_DIRS:
        base = repo_root / name
        if not base.is_dir():
            continue
        for p in base.rglob("*.md"):
            rel = p.relative_to(repo_root).as_posix()
            if p.name == "index.md":
                continue
            if rel in ROOT_EXCLUDE_NAMES:
                continue
            out.append(p)
    return sorted(out)
```

Note: `ROOT_EXCLUDE_NAMES` only applies to paths whose relative POSIX equals those names (files at repo root); `rel` for nested files never equals `README.md` unless a folder contains that exact leaf — safe.

- [ ] **Step 2: Add smoke test in `tests/prdc/test_integration_scan.py`**

```python
from pathlib import Path

from prdc.scan import iter_wiki_markdown_files


def test_finds_leaf_not_index(tmp_path: Path):
    root = tmp_path
    (root / "dotnet").mkdir()
    (root / "dotnet" / "index.md").write_text("# hub", encoding="utf-8")
    leaf = root / "dotnet" / "leaf.md"
    leaf.write_text("x", encoding="utf-8")
    got = iter_wiki_markdown_files(root)
    assert leaf in got
    assert (root / "dotnet" / "index.md") not in got
```

This test requires copying `WIKI_TOP_LEVEL_DIRS` behavior — it uses `dotnet` which exists in the tuple. Good.

- [ ] **Step 3: Run test**

```bash
pytest tests/prdc/test_integration_scan.py -v
```

- [ ] **Step 4: Commit scan**

```bash
git add scripts/prdc/scan.py tests/prdc/test_integration_scan.py
git commit -m "feat(prdc): enumerate wiki markdown files"
```

---

### Task 11: CLI orchestration

**Files:**
- Create: `scripts/prdc/cli.py`
- Modify: `scripts/prdc/cli.py` (fill `main`)

- [ ] **Step 1: Implement `main()` in `scripts/prdc/cli.py`**

Behavior:

1. `argparse` argument `--repo-root` default `os.getcwd()`.
2. `repo_root = Path(args.repo_root).resolve()`.
3. `memo_path = repo_root / "_memoize" / "LINKS.json"`.
4. `existing = load_links(memo_path)`.
5. `computed: dict[str, str] = {}`.
6. For each `md_path` in `iter_wiki_markdown_files(repo_root)`:
   - `text = md_path.read_text(encoding="utf-8")`.
   - `new_text = rewrite_localhost_links(text)`; if `new_text != text`, write `md_path` with UTF-8.
   - `work_text = new_text` (re-parse after rewrite is unnecessary if rewrite only affects localhost strings and extract runs on post-rewrite text — use `new_text` for extraction).
   - For each `(href, label)` in `extract_links(new_text)`:
     - If `is_navigation_link(label, href)`: continue.
     - `key = canonical_memo_url(href, str(md_path), str(repo_root))`.
     - Determine `is_image` if this tuple came from an image token (adjust `extract_links` to return `("image", href, text)` or a small dataclass — implement minimal flag).
     - `cat = classify_href(key, is_image=...)`.
     - If `cat is None`: continue (`NONE`).
     - `computed[key] = cat` — if duplicates, last wins only if same category; assert same category for duplicates in debug mode, else prefer first non-`review` then `review` rule: if key already in `computed` and values differ, keep the more specific by preferring existing if existing != `review`.
7. `merged = merge_memo(existing, computed)`.
8. `save_links(memo_path, merged)`.
9. Print counts: files scanned, links extracted, rows written, files changed by localhost.

Return `0` on success; on `UnicodeDecodeError` print path and return `1`.

- [ ] **Step 2: Wire imports at top of `cli.py`**

```python
from __future__ import annotations

import argparse
import os
from pathlib import Path

from prdc.classify import classify_href
from prdc.extract import extract_links
from prdc.localhost import rewrite_localhost_links
from prdc.memo import load_links, merge_memo, save_links
from prdc.nav_filter import is_navigation_link
from prdc.normalize import canonical_memo_url
from prdc.scan import iter_wiki_markdown_files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="PRDC: wiki link catalog")
    parser.add_argument(
        "--repo-root",
        default=os.getcwd(),
        help="Repository root (default: current working directory)",
    )
    args = parser.parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    # ... fill using Step 1 narrative ...
    return 0
```

Fill the body completely (no ellipsis comments) so the file runs.

- [ ] **Step 3: Extend `extract.py` to mark images**

Change return type to `list[tuple[str, str, bool]]` as `(href, text, is_image)` and update **all** callers plus `tests/prdc/test_extract.py` assertions in the same commit.

- [ ] **Step 4: Run full suite**

```bash
pytest tests/prdc -v
```

- [ ] **Step 5: Run PRDC against real repo (smoke)**

```bash
set PYTHONPATH=scripts
python -m prdc --repo-root .
```

Expected: creates `_memoize/LINKS.json`, may modify files with localhost links; exits `0`.

- [ ] **Step 6: Commit**

```bash
git add scripts/prdc/cli.py scripts/prdc/extract.py tests/prdc/
git commit -m "feat(prdc): CLI scan, classify, memo, localhost rewrite"
```

---

## Phase 8: Documentation and housekeeping

### Task 12: Document how to run PRDC

**Files:**
- Modify: `CLAUDE.md` (short subsection under Local Preview or new “Maintenance scripts”)

- [ ] **Step 1: Append subsection to `CLAUDE.md`**

Add 5–8 lines:

- Install `pip install -r scripts/requirements-prdc.txt`.
- Run `PYTHONPATH=scripts python -m prdc --repo-root .` from repo root.
- Output `_memoize/LINKS.json`; localhost links rewritten in place.

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: document PRDC usage"
```

---

### Task 13: Changelog row

**Files:**
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Update the existing `260420` changelog row** (do not add a second `260420` row) so the description states that the PRDC **implementation plan** was added, the design spec gained **Appendix A** (classification rules), and the scratch **`plan26041902.md`** file was removed.

- [ ] **Step 2: Commit**

```bash
git add CHANGELOG.md docs/superpowers/plans/2026-04-20-prdc-links-catalog.md docs/superpowers/specs/2026-04-20-prdc-links-memo-design.md
git status
git commit -m "docs: add PRDC implementation plan and fold classification into design spec"
```

If `plan26041902.md` is still tracked as deleted, include it in the same commit:

```bash
git add -u plan26041902.md
```

---

## Plan self-review (spec coverage)

| Spec section | Tasks covering it |
|--------------|-------------------|
| Scan include wiki dirs | Task 10 `WIKI_TOP_LEVEL_DIRS`, `iter_wiki_markdown_files` |
| Exclude root community files | Task 10 `ROOT_EXCLUDE_NAMES` (extend if spec list grows) |
| Exclude `.claude/`, `CLAUDE.md` | Implicit: not under wiki dirs; add explicit skip if `scan` ever broadens |
| Exclude `docs/superpowers/` | Implicit: not walked |
| Exclude hub `index.md` | Task 10 skip `index.md` |
| Exclude nav links | Tasks 7, 11 |
| Canonical URL rules | Tasks 3–4 |
| `mailto` / `tel` | Task 4 |
| Path POSIX + strip fragment | Task 4 |
| Merge freeze / `review` | Task 5 |
| `NONE` omitted | Tasks 6, 11 |
| Localhost rewrite always | Tasks 8, 11 (no flags) |
| Non-interactive / exit codes | Task 11 |
| Deterministic JSON | Task 5 `save_links` |
| Classification Appendix A | Task 6 |
| Tests minimum | Tasks 3–9, 11 |

**Placeholder scan:** No `TBD` / `TODO` tokens were intentionally left; Task 9 and Task 11 call out verifying markdown-it-py token field names against real objects (adjust code, not placeholders).

**Type consistency:** `extract_links` signature change in Task 11 must propagate to tests in Task 9 — when implementing, update `tests/prdc/test_extract.py` in the same commit as `extract.py` signature change.

---

**Plan complete and saved to `docs/superpowers/plans/2026-04-20-prdc-links-catalog.md`. Two execution options:**

1. **Subagent-Driven (recommended)** — dispatch a fresh subagent per task, review between tasks, fast iteration. **Required sub-skill:** superpowers:subagent-driven-development.

2. **Inline Execution** — execute tasks in this session using executing-plans, batch execution with checkpoints. **Required sub-skill:** superpowers:executing-plans.

**Which approach do you want?**
