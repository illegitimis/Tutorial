---
title: Git
layout: default
nav_order: 3
parent: DevOps
last_modified_date: 2026-03-31 00:00:00 +00:00
---

# Git

## Git vs Svn

git | svn
--- | ---
push | commit
master | trunk
pull | update

## Links

+ Inspecting a repository [1], Git lets you completely ignore files by placing paths in a special file called `.gitignore`.
+ Saving changes [2], add, commit, stash.
+ Sync [3] with fetch, remote, push, pull

## Git Command Line

1. The common Git guides are:

guide | description
------------|------------------------------
attributes | Defining attributes per path
everyday   | Everyday Git With 20 Commands Or So
glossary   | A Git glossary
ignore     | Specifies intentionally untracked files to ignore
modules    | Defining submodule properties
revisions  | Specifying revisions and ranges for Git
tutorial   | A tutorial introduction to Git (for version 1.5.1 or newer)
workflows  | An overview of recommended workflows with Git

Run like `git help <guide_name>`.

1. **Git Bash**

```sh
git log -10
git diff HEAD
git add tools/git.md
git status
# commit everything with message and author overridden
git commit -a -m 'modified git.md' --author illegitimis
git help push
git push
git push origin
git reset HEAD^
git revert <commit>
# list local and remote branches verbose
git branch --list -a -vv
```

1. **update fork**. If using _SourceTree_ one can pull from remote origin, selecting the dev branch to pull.

```cmd
cd <dir_where_i_cloned_my_fork_of_a_repo>
git remote add bradyholt-cron-expression-descriptor-master https://github.com/bradyholt/cron-expression-descriptor
git pull bradyholt-cron-expression-descriptor-master master
# unstage_conflicts
```

1. git push SSL_ERROR_SYSCALL

```cmd
git config http.postBuffer 524288000
```

1. file **history**

+ GitLens [4] extension
+ file commit history with patches and beyond renames

  ```bat
  rem path to file is relative to root
  rem differentiates revisions from files
  $ git log --follow -p -- ./src/Proj/Validation/OrderRequestDtoValidator.cs
  ```

1. **stashes**

```sh
git stash list
git stash show stash@{0}
```

1. github _update fork_ from master

```sh
git remote -v
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
git remote -v
git fetch upstream
git checkout master
git merge upstream/master
git push -v --tags origin master:master
```

## Configuration

```sh
git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input # Linux
git config --global --edit
```

`.gitattributes` line endings:

```ini
* text=auto
* text eol=crlf
* text eol=lf
```

## Merge

```sh
git fetch origin
git merge origin/develop
git log develop..HEAD --oneline --no-merges
git rm --cached <file>
```

## File History

```sh
# Basic history
git log -- path/to/file.txt
# One-line summary per commit
git log --oneline -- path/to/file.txt
# With diffs (what changed in each commit)
git log -p -- path/to/file.txt
# Last N commits
git log -5 -- path/to/file.txt
# Follow renames
git log --follow -- path/to/file.txt
```

[1]: https://www.atlassian.com/git/tutorials/inspecting-a-repository
[2]: https://www.atlassian.com/git/tutorials/saving-changes
[3]: https://www.atlassian.com/git/tutorials/syncing
[4]: https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens

[<](./index.md) | [<<](/index.md)
