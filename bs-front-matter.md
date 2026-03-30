---
nav_exclude: true
search_exclude: true
---

i want to add just the docs theme front matter to all of the md files in the solution except top level readme.
JTD = just the docs, just-the-docs
FM = front matter
exempt README.md, CLAUDE.md, CONTRIBUTING.md, CONTRIBUTORS.md, STRUCTURE.md, all md produce of superpowers plugin: docs\superpowers\**\*.md from JTD front matter.
use fenced yml code blocks without '```yml```' md markup, like:

---
title: Home
layout: home
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
---

see [sample](https://raw.githubusercontent.com/just-the-docs/just-the-docs/refs/heads/main/index.md)

so FM should prefix targeted md files in between '---' blocks.

## actions

in top level README.md:

- keep old wiki mention
- move 'Illegitimis' Dev Mnemonics' h1 and list below to a new root file index.md
- add Project overview, setup instructions, usage examples, link to hosted github pages deployment
- add Quick-start guide for new contributors

## front matter

- layout: root index.md: `layout: home`, all other index.md: `layout: minimal`, rest of md: `layout: default`
- `last_modified_date`  Display last modified date. not sure about format. use smth that JTD, jekyll support. probably date only part like '2026-03-28' works. infer this from git log for every md file not at root level. _config.yml already has last_edit_timestamp and last_edit_time_format set up. i would prefer last_edit_time_format to be YYYY-MM-dd HH:mm:ss. utc date, no mention of time zone.
- add also `title` front matter. infer from file contents h1. e.g. data\sql\mysql.md has `# MySQL` title, therefore produce: `title: MySQL` for FM.
- `nav_order`: int. start at 1. use alphabetical ordering in the existing folder if the folder has an index.md file. for root level, infer the order from the order of item links in README.md