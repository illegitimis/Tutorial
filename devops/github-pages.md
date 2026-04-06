---
title: GitHub Pages
layout: default
nav_order: 12
parent: DevOps
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# GitHub Pages

- `GitHub Pages` and `Jekyll`: a detailed guide [1]
- ProUnity **Domain Events** catalog [2]
- `Jekyll` front matter [3]

## Just the Docs

> Just the Docs is a responsive `Jekyll` theme with built-in search that is easily customizable and hosted on `GitHub Pages`.

`Just the Docs` custom schemes [4]; configuration.md [5] has _title_ and _nav_order_; index.md [6]

```yml
title: Home
layout: home
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
```

- Template [7]
- `Jekyll` collections [8]
- Deployed docs [9]
- Config YML: illegitimis [10], official [11]

### Available Layout Values

Based on the `_layouts` directory, `Just the Docs` supports these layout options:

| Layout | Purpose |
|--------|---------|
| `default` | Main layout with navigation sidebar, search, and full theme styling (e.g. CHANGELOG, search, 404 page) |
| `page` | Basic page layout (minimal wrapper) |
| `home` | Homepage layout, only top level index.md |
| `post` | Post/blog layout |
| `minimal` | Minimal layout with navigation disabled by default |

### Front Matter Variables

| Variable | Type | Purpose |
|----------|------|---------|
| `nav_enabled` | boolean | Show/hide left navigation sidebar (page-level override); false for minimal layout |
| `has_toc` | boolean | Show/hide table of contents and child pages |
| `heading_anchors` | boolean | Generate anchor links for headings; default opt-in from template |
| `search_enabled` | boolean | Show/hide search footer |
| `mermaid` | object | Enable `Mermaid` diagram rendering; official has `version: "9.1.6"` |
| `lang` | string | HTML language attribute (default: `en-US`) |
| `nav_exclude` | boolean | Exclude page from navigation |
| `search_exclude` | boolean | Exclude page from search |
| `last_modified_date` | string | Display last modified date |

### Permalink Examples

Standard `Jekyll` permalink patterns (apply to `Just the Docs`):

```yaml
# Pretty URLs (most common)
permalink: /docs/getting-started/

# Custom URL
permalink: /guides/installation

# Date-based (posts)
permalink: /blog/:year/:month/:day/:title

# Category-based
permalink: /:categories/:title

# Flat structure
permalink: /:title

# With file extension
permalink: /docs/:title.html

# Nested path
permalink: /api/v1/:title

# Root level
permalink: /:title/
```

### Sample Front Matter

```yaml
---
layout: page
title: Getting Started
nav_order: 1
has_toc: true
search_exclude: false
permalink: /docs/getting-started/
last_modified_date: 2026-03-28
---
```

## MkDocs

`mkdocs-deploy-gh-pages` — GitHub Action to deploy an `MkDocs` site to `GitHub Pages` [12] \
`MkDocs` deploying your docs [13]

[<](./index.md) | [<<](/index.md)

[1]: https://pappater.github.io/docs/GitHub%20Pages%20and%20Jekyll/
[2]: https://andrei-popescu-pu-ddd-plan.pages.hfg.ghe.com/domain-events/
[3]: https://jekyllrb.com/docs/front-matter/
[4]: https://just-the-docs.com/docs/customization/#custom-schemes
[5]: https://github.com/just-the-docs/just-the-docs/blob/main/docs/configuration.md?plain=1
[6]: https://github.com/just-the-docs/just-the-docs/blob/main/index.md?plain=1
[7]: https://just-the-docs.github.io/just-the-docs-template/
[8]: https://jekyllrb.com/docs/collections/
[9]: https://just-the-docs.com/docs/navigation/main/
[10]: https://github.com/illegitimis/Tutorial/blob/master/_config.yml
[11]: https://github.com/just-the-docs/just-the-docs/blob/main/_config.yml
[12]: https://github.com/mhausenblas/mkdocs-deploy-gh-pages
[13]: https://www.mkdocs.org/user-guide/deploying-your-docs/
