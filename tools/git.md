# GIT

## git vs svn
git | svn
--- | ---
push | commit
master | trunk
pull | update

## Links
+ [Inspecting a repository](https://www.atlassian.com/git/tutorials/inspecting-a-repository), 
Git lets you completely ignore files by placing paths in a special file called `.gitignore`.
+ [Saving changes](https://www.atlassian.com/git/tutorials/saving-changes), add, commit, stash.
+ [Sync](https://www.atlassian.com/git/tutorials/syncing) with fetch, remote, push, pull

## Git command line

1. The common Git guides are:

| guide | description |
|------------|------------------------------|
| attributes | Defining attributes per path |
|everyday    | Everyday Git With 20 Commands Or So|
|glossary    | A Git glossary|
|ignore      | Specifies intentionally untracked files to ignore|
|modules     | Defining submodule properties|
|revisions   | Specifying revisions and ranges for Git|
|tutorial    | A tutorial introduction to Git (for version 1.5.1 or newer)|
|workflows   | An overview of recommended workflows with Git|
Run like `git help <guide_name>`.

2. Git Bash
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
# file commit history with patches and beyond renames
# path to file is relative to root
# -- differentiates revisions from files
$ git log --follow -p -- ./src/esw.Shipping.Api/Validation/OrderRequestDtoValidator.cs
```

3. update fork
```cmd
cd <dir_where_i_cloned_my_fork_of_a_repo>
git remote add bradyholt-cron-expression-descriptor-master https://github.com/bradyholt/cron-expression-descriptor
git pull bradyholt-cron-expression-descriptor-master master
# unstage_conflicts
```
If using ~SourceTree~ one can pull from remote origin, selecting the dev branch to pull.

4. git push SSL_ERROR_SYSCALL 
```cmd
git config http.postBuffer 524288000
```


[<<](../tools.md)
|
[home](../README.md)
|
[wiki](https://github.com/illegitimis/Tutorial/wiki)