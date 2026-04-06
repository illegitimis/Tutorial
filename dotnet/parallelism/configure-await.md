---
title: ConfigureAwait
layout: default
nav_order: 14
parent: Parallelism
grand_parent: .NET
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# ConfigureAwait

> `ConfigureAwait(false)` avoids capturing the synchronization context, improving performance in library code.

## Why No SynchronizationContext?

ASP.NET Core does not have a `SynchronizationContext` [1]. Library code should still use `ConfigureAwait(false)` for portability.

GitHub search: `repo:dotnet/aspnetcore .ConfigureAwait(false)`

## Runtime Internals

`Task.GetAwaiter` [2] returns `TaskAwaiter` \
`Task.ConfigureAwait(bool)` [3] returns `ConfiguredTaskAwaitable` \
`TaskAwaiter` struct [4] \
`ConfiguredTaskAwaitable.ConfiguredTaskAwaiter` struct [5]

### State Machine Difference

Without `ConfigureAwait(false)`, the compiler-generated state machine uses `TaskAwaiter`. With it, the state machine uses `ConfiguredTaskAwaitable.ConfiguredTaskAwaiter` — the key difference being whether `continueOnCapturedContext` is set.

`AsyncTaskMethodBuilder.AwaitUnsafeOnCompleted` [6] \
`AsyncTaskMethodBuilderT.AwaitUnsafeOnCompleted` [7] \
`Task.UnsafeSetContinuationForAwait` [8] \
`SynchronizationContext` source [9]

## ASP.NET Core Usage

`Server.IntegrationTesting` RetryHelper [10] \
`HealthCheckPublisherHostedService` [11] \
`TaskExtensions.TimeoutAfter` [12] \
`System.Private.CoreLib.TaskContinuation` [13] \
`TaskAwaiter` source [14] \
`AsyncTaskMethodBuilderT.AwaitUnsafeOnCompleted` [15]

[<](./index.md) | [<<](/index.md)

[1]: https://blog.stephencleary.com/2017/03/aspnetcore-synchronization-context.html
[2]: https://github.com/dotnet/dotnet/blob/main/src/runtime/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs#L2441-L2444
[3]: https://github.com/dotnet/dotnet/blob/main/src/runtime/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs#L2446-L2455
[4]: https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.taskawaiter?view=net-9.0
[5]: https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.configuredtaskawaitable.configuredtaskawaiter?view=net-9.0
[6]: https://github.com/dotnet/dotnet/blob/e12a7e57e6d9ff277f48002afed298cab668df86/src/runtime/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilder.cs#L62-L67
[7]: https://github.com/dotnet/dotnet/blob/e12a7e57e6d9ff277f48002afed298cab668df86/src/runtime/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs#L106-L115
[8]: https://github.com/dotnet/dotnet/blob/main/src/runtime/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs#L2557-L2603
[9]: https://github.com/dotnet/dotnet/blob/b0f34d51fccc69fd334253924abd8d6853fad7aa/src/runtime/src/libraries/System.Private.CoreLib/src/System/Threading/SynchronizationContext.cs
[10]: https://github.com/dotnet/aspnetcore/blob/main/src/Hosting/Server.IntegrationTesting/src/Common/RetryHelper.cs
[11]: https://github.com/dotnet/aspnetcore/blob/main/src/HealthChecks/HealthChecks/src/HealthCheckPublisherHostedService.cs#L146
[12]: https://github.com/dotnet/aspnetcore/blob/main/src/Shared/TaskExtensions.cs#L83
[13]: https://github.com/dotnet/dotnet/blob/main/src/runtime/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/TaskContinuation.cs#L453
[14]: https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/TaskAwaiter.cs
[15]: https://github.com/dotnet/dotnet/blob/main/src/runtime/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs#L96-L146
