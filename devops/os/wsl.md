---
title: WSL
layout: default
nav_order: 18
parent: DevOps
last_modified_date: 2026-03-31 00:00:00 +00:00
---

# WSL

## Windows

```powershell
wsl --list --all
# Windows Subsystem for Linux Distributions:
# Ubuntu (Default)
wsl --list --running
# There are no running distributions.
wsl --list --online
wsl -l -o
wsl -l -v
wsl --list --verbose
#  NAME    STATE     VERSION
# Ubuntu   Running   2
# Auto-login as root
wsl --distribution Ubuntu --default-user root
# To revert later
wsl --distribution Ubuntu --default-user youruser
# Run other distro
wsl -d docker-desktop
wsl -d docker-desktop -- uname -a
wsl --distribution Ubuntu -- whoami
```

## Ubuntu

### Claude Code

```sh
# 1. Install Node.js in WSL
curl -fsSL https://deb.nodesource.com/setup_22.x -o /tmp/nodesource_setup.sh
bash /tmp/nodesource_setup.sh
apt-get install -y nodejs
# 2. Install Claude Code in WSL
npm install -g @anthropic-ai/claude-code
```

### Terminal

```sh
cat /etc/passwd
# devcontainers:x:1000:1000:,,,:/home/devcontainers:/bin/bash
```

[<](../index.md) | [<<](/index.md)
