---
title: GitHub Repository Practices
layout: default
nav_order: 19
parent: DevOps
last_modified_date: 2026-03-31 00:00:00 +00:00
---

# GitHub Repository Practices

Top-level GitHub repository conventions for best patterns and practices.

## Essential Files

`README.md` — project overview, setup instructions, usage examples; quick-start guide for new contributors

`LICENSE` — specifies legal terms (MIT, Apache 2.0, GPL, etc.); GitHub auto-detects and displays it

`CONTRIBUTING.md` — guidelines for submitting issues and PRs; code style standards, commit message conventions; testing and local development setup

`CHANGELOG.md` (or `HISTORY.md`) — documents changes for each release; _Semantic Versioning_ format (v1.2.3); breaking changes clearly marked

`CODE_OF_CONDUCT.md` — standards for community interaction; often uses _Contributor Covenant_ template

## Configuration and Governance

`.gitignore` — excludes build artifacts, secrets, dependencies; language/framework-specific templates available

`.github/workflows/` (GitHub Actions) — _CI/CD_ pipelines (tests, linting, builds); auto-deployment, release automation; branch protection rules configured in repo settings

`.github/ISSUE_TEMPLATE/` and `PULL_REQUEST_TEMPLATE/` — standardized issue/PR formats; automated checklists and fields

`CODEOWNERS` — specifies who reviews which files; auto-requested for PR reviews

## Git History Practices

- **Conventional Commits** — structured messages (`feat:`, `fix:`, `docs:`, `chore:`)
- **Semantic Versioning** — `v{major}.{minor}.{patch}`
- **Releases** — tagged commits with release notes on GitHub
- **Branch strategy** — main/master protected, feature branches, squash/rebase merging policy

## Architecture Documentation

`ARCHITECTURE.md` or `docs/ARCHITECTURE.md` — system design, component relationships, technology decisions and rationale

`docs/` directory — API documentation, _Architecture Decision Records_ (ADRs), troubleshooting guides

## Optional but Recommended

- `SECURITY.md` — vulnerability reporting process
- `SUPPORT.md` — how to get help
- `AUTHORS.md` or `CREDITS.md` — contributor attribution
- `Makefile` or `justfile` — common development tasks
- `renovate.json` or `dependabot.yml` — dependency updates

[<](./index.md) | [<<](/index.md)
