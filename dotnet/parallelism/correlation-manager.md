---
title: CorrelationManager
layout: default
nav_order: 10
parent: Parallelism
grand_parent: .NET
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# CorrelationManager

`CorrelationManager` reference source [1] \
Start/StopLogicalOperation

`ExecutionContext` vs `SynchronizationContext` [2] \
`ExecutionContext` in dotnet/runtime [3]

_Eliding Async and Await_ [4]

`AsyncLocal<T>` [5]

`Application Insights` does not use `CorrelationManager.ActivityId`. Instead, it uses `System.Diagnostics.Activity` for correlation [6].

Activity User Guide [7]

_Implicit Async Context_ ("AsyncLocal") [8] \
`AsyncLocal.cs` archive implementation [9]

[1]: https://referencesource.microsoft.com/#System/compmod/system/diagnostics/CorrelationManager.cs,21
[2]: https://devblogs.microsoft.com/pfxteam/executioncontext-vs-synchronizationcontext/
[3]: https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.CoreLib/src/System/Threading/ExecutionContext.cs
[4]: https://blog.stephencleary.com/2016/12/eliding-async-await.html
[5]: https://learn.microsoft.com/en-us/dotnet/api/system.threading.asynclocal-1?view=net-7.0
[6]: https://github.com/Microsoft/ApplicationInsights-dotnet/issues/631
[7]: https://github.com/dotnet/runtime/blob/4f9ae42d861fcb4be2fcd5d3d55d5f227d30e723/src/libraries/System.Diagnostics.DiagnosticSource/src/ActivityUserGuide.md
[8]: https://blog.stephencleary.com/2013/04/implicit-async-context-asynclocal.html
[9]: https://github.com/StephenClearyArchive/AsyncLocal/blob/master/src/AsyncLocal/AsyncLocal.cs

[<](./index.md) | [<<](/index.md)