---
title: "GitHub Docs/wiki & Markdown How-to"
layout: default
nav_order: 4
parent: DevOps
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# GitHub Docs/wiki & Markdown How-to

## Formatting

1. Markdown cheatsheet pdf [1],
git page GitHub page [2] by Adam Pritchard
2. Markdown tables generator [3]
3. Word to Markdown Converter [4]
4. html2md [5]
5. Footer [6]
6. Images [7]
7. Add pages [8]
8. Adding and editing wiki pages locally [9]
9. Sidebar [10]
10. Shields.io gist [11]
11. nice html basics [12]

## Meta

- Search a wiki [13]
- Viewing a wiki's history of changes [14]
- github/markup on GitHub [15]
- Topics [16] and language

## Mediawiki

- Supported MediaWiki formats [17]
- mediawiki Formatting [18]

## Utils

- DownGit - Create GitHub Directory Download Link [19], and original SO answer [20]

[1]: https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf
[2]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
[3]: http://www.tablesgenerator.com/markdown_tables
[4]: http://word-to-markdown.herokuapp.com/
[5]: https://domchristie.github.io/to-markdown/
[6]: https://help.github.com/articles/creating-a-footer/
[7]: https://help.github.com/articles/adding-images-to-wikis/
[8]: https://help.github.com/articles/adding-wiki-pages-via-the-online-interface/
[9]: https://help.github.com/articles/adding-and-editing-wiki-pages-locally/
[10]: https://help.github.com/articles/creating-a-sidebar/
[11]: https://gist.github.com/illegitimis/c227c46b9a495cc927244ab805e4358f
[12]: http://commonmark.org/help/tutorial/
[13]: https://help.github.com/articles/searching-wikis/
[14]: https://help.github.com/articles/viewing-a-wiki-s-history-of-changes/
[15]: https://github.com/github/markup
[16]: https://github.com/topics/graph-algorithms?l=c%23
[17]: https://help.github.com/articles/supported-mediawiki-formats/
[18]: https://www.mediawiki.org/wiki/Help:Formatting
[19]: https://minhaskamal.github.io/DownGit/#/home
[20]: https://stackoverflow.com/questions/7106012/download-a-single-folder-or-directory-from-a-github-repo#18194523

## Code Search

Understanding GitHub code search syntax [21] \
GitHub Code Search Cheat Sheet [27]

```txt
path:/(^|\/)Directory\.Build\.props$/ AND org:dotnet
path:/^MIT.txt$/ is:archived
owner:pacedgeless
path:/(^|\/)Dockerfile$/ AND org:dotnet AND Directory.Build.props
path:/.editorconfig$/ language:EditorConfig
path:/^*.csproj$/ AND ironpdf.slim
path:/^Directory.Packages.props$/ SonarAnalyzer.CSharp
path:/^*.http$/ "multipart/form-data"
path:**/*.cs
```

[21]: https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax

## GitHub Emoji

- Emoji web app search [22]
- GitHub asset example (Romania) [23]
- GitHub REST API — emojis [24] [25]
- Complete list of GitHub Markdown emoji markup [26]

[<](./index.md) | [<<](/index.md)

[22]: https://awes0mem4n.github.io/emojis-github.html
[23]: https://github.githubassets.com/images/icons/emoji/unicode/1f1f7-1f1f4.png?v8
[24]: https://docs.github.com/en/rest
[25]: https://docs.github.com/en/rest/reference/emojis
[26]: https://gist.github.com/rxaviers/7360908
[27]: https://karask.com/github-code-search-cheat-sheet
