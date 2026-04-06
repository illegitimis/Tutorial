---
title: Static Code Analysis
layout: default
nav_order: 7
parent: .NET Build
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# Static Code Analysis

## Roslyn Analyzers

`dotnet/roslyn-analyzers` [1] \
`StyleCopAnalyzers` [2] \
`IDisposableAnalyzers` [3] \
DotNetAnalyzers organization [4]

The Roslyn analyzers I use in my projects [5] \
Enforcing asynchronous code good practices using a Roslyn analyzer [6] \
Enforce .NET code style in CI with `dotnet format` [7] \
Write Better Code Faster with Roslyn Analyzers [8]

## Source Code Analysis

Overview of source code analysis [9] \
Source code analysis overview [10] \
Code-style rule options [11] \
Configuration options for code analysis [12]

## Migration and Setup

Migrate from legacy analysis (`FxCop`) to source analysis (.NET analyzers) [13] [14] \
Enable or install first-party .NET analyzers [15] \
`SonarAnalyzer.CSharp` [16] \
`SonarLint` for Visual Studio [17] \
Use rule sets to group code analysis rules [18]

[<](./index.md) | [<<](/index.md)

[1]: https://github.com/dotnet/roslyn-analyzers
[2]: https://github.com/DotNetAnalyzers/StyleCopAnalyzers
[3]: https://github.com/DotNetAnalyzers/IDisposableAnalyzers
[4]: https://github.com/orgs/DotNetAnalyzers/repositories?type=all
[5]: https://www.meziantou.net/the-roslyn-analyzers-i-use.htm
[6]: https://www.meziantou.net/enforcing-asynchronous-code-good-practices-using-a-roslyn-analyzer.htm
[7]: https://www.meziantou.net/enforce-dotnet-code-style-in-ci-with-dotnet-format.htm
[8]: https://devblogs.microsoft.com/dotnet/write-better-code-faster-with-roslyn-analyzers/
[9]: https://learn.microsoft.com/en-us/visualstudio/code-quality/roslyn-analyzers-overview?view=vs-2022
[10]: https://learn.microsoft.com/en-us/visualstudio/code-quality/use-roslyn-analyzers?source=recommendations&view=vs-2022
[11]: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/code-style-rule-options?preserve-view=true&view=vs-2019#convention-categories
[12]: https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-options
[13]: https://learn.microsoft.com/en-us/visualstudio/code-quality/migrate-from-legacy-analysis-to-net-analyzers?view=vs-2022
[14]: https://learn.microsoft.com/en-us/visualstudio/code-quality/net-analyzers-faq?view=vs-2022
[15]: https://learn.microsoft.com/en-us/visualstudio/code-quality/install-net-analyzers?view=vs-2022
[16]: https://www.nuget.org/packages/SonarAnalyzer.CSharp/#versions-body-tab
[17]: https://www.sonarsource.com/products/sonarlint/features/visual-studio/
[18]: https://learn.microsoft.com/en-us/visualstudio/code-quality/using-rule-sets-to-group-code-analysis-rules?view=vs-2022
