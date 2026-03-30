---
title: Async and Await
layout: default
nav_order: 12
parent: Parallelism
grand_parent: .NET
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Async and Await

> Asynchronous programming patterns, deadlock avoidance, async locks, context switching, and the **Task-based Asynchronous Pattern**.

## Stephen Cleary

Concurrency in C# Cookbook [1]: Asynchronous, Parallel, and Multithreaded Programming \
Async and Await intro [2] \
Don't Block on Async Code [3]

## Stephen Toub

Should I expose asynchronous wrappers for synchronous methods? [4]

## Notes

> There's one other important guideline when it comes to async methods: once you start using `async`, it's _best to allow it to grow through your code_. If you call an async method, you should (eventually) await the task it returns. Resist the temptation to call `Task.Wait`, `Task<TResult>.Result`, or `GetAwaiter().GetResult()` — doing so could cause a deadlock.

Consider the following method:

```cs
async Task WaitAsync()
{
  // This await will capture the current context ...
  await Task.Delay(TimeSpan.FromSeconds(1));
  // ... and will attempt to resume the method here in that context.
}

void Deadlock()
{
  // Start the delay.
  Task task = WaitAsync();

  // Synchronously block, waiting for the async method to complete.
  task.Wait();
}
```

- The code in this example **will deadlock if called from a UI or ASP.NET Classic context** because both of those contexts only allow one thread in at a time
- `Deadlock` will call `WaitAsync`, which begins the delay
- `Deadlock` then (synchronously) waits for that method to complete, blocking the context thread
- When the delay completes, await attempts to resume `WaitAsync` within the captured context, but it cannot because there's already a thread blocked in the context, and the context only allows one thread at a time
- **Deadlock** can be prevented two ways:
  - use `ConfigureAwait(false)` within `WaitAsync` (which causes await to ignore its context)
  - or await the call to `WaitAsync` (making `Deadlock` into an async method)

> **WARNING** If you use async, it's best to use async all the way.

> **WARNING** Using `Task` for parallel processing is completely different than using `Task` for asynchronous processing.

The `Task` type serves two purposes in concurrent programming: it can be a parallel task or an asynchronous task.
Parallel tasks may use blocking members, such as `Task.Wait`, `Task.Result`, `Task.WaitAll`, and `Task.WaitAny`.
Parallel tasks also commonly use `AttachedToParent` to create parent/child relationships between tasks.
Parallel tasks should be created with `Task.Run` or `Task.Factory.StartNew`.

In contrast, **asynchronous tasks should avoid blocking members**, and prefer `await`, `Task.WhenAll`, and `Task.WhenAny`.
Asynchronous tasks should not use `AttachedToParent`, but they can form an implicit kind of parent/child relationship by awaiting another task.

## Async Locks

> Chapter 12.2 [5]

**Problem** You have some shared data and need to safely read and write it from multiple code blocks, which may be using await.

**Solution** The .NET framework `SemaphoreSlim` type has been updated in .NET 4.5 to be compatible with async:

```cs
class MyClass
{
  // This lock protects the _value field.
  private readonly SemaphoreSlim _mutex = new SemaphoreSlim(1);

  private int _value;

  public async Task DelayAndIncrementAsync()
  {
    await _mutex.WaitAsync();
    try
    {
      int oldValue = _value;
      await Task.Delay(TimeSpan.FromSeconds(oldValue));
      _value = oldValue + 1;
    }
    finally
    {
      _mutex.Release();
    }
  }
}
```

You can also use the `AsyncLock` type from the `Nito.AsyncEx` library:

```cs
class MyClass
{
  // This lock protects the _value field.
  private readonly AsyncLock _mutex = new AsyncLock();

  private int _value;

  public async Task DelayAndIncrementAsync()
  {
    using (await _mutex.LockAsync())
    {
      int oldValue = _value;
      await Task.Delay(TimeSpan.FromSeconds(oldValue));
      _value = oldValue + 1;
    }
  }
}
```

## Context Switch

- What is context switching in operating system? [6]
- `ThreadPool.GetAvailableThreads` [7]
- The cost of context switches [8]
- Does async/await increase context switching? [9]

## Task-Based Asynchronous Pattern

**TAP** in .NET: Introduction and overview [10] \
Implementing the Task-based Asynchronous Pattern [11] \
Consuming the Task-based Asynchronous Pattern [12] \
Interop with Other Asynchronous Patterns and Types [13] \
**Asynchronous Programming Model** (APM) [14] \
Cancel async tasks after a period of time [15]

### Cancellation

- `CancellationToken` timeout vs `Task.Delay` and timeout [16]
- Coalescing CancellationTokens from Timeouts [17]
- How to use CancellationTokens to cancel tasks in the Azure SDK for .NET [18]

### Async Enumerables

- Iterating with Async Enumerables in C# 8 [19]
- Pagination with the Azure SDK for .NET [20]
- `System.Linq.Async` [21]

Dynamic Parallelism [22]

[1]: https://learning.oreilly.com/library/view/concurrency-in-c/9781492054498/ch01.html#idm45458718736760
[2]: https://blog.stephencleary.com/2012/02/async-and-await.html
[3]: https://blog.stephencleary.com/2012/07/dont-block-on-async-code.html
[4]: https://devblogs.microsoft.com/pfxteam/should-i-expose-asynchronous-wrappers-for-synchronous-methods/
[5]: https://learning.oreilly.com/library/view/concurrency-in-c/9781492054498/ch12.html#recipe-async-locks
[6]: https://www.tutorialspoint.com/what-is-context-switching-in-operating-system
[7]: https://learn.microsoft.com/en-us/dotnet/api/system.threading.threadpool.getavailablethreads?redirectedfrom=MSDN&view=net-6.0#System_Threading_ThreadPool_GetAvailableThreads_System_Int32__System_Int32__
[8]: https://devblogs.microsoft.com/premier-developer/the-cost-of-context-switches/
[9]: https://stackoverflow.com/questions/39795286/does-async-await-increases-context-switching
[10]: https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/task-based-asynchronous-pattern-tap
[11]: https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/implementing-the-task-based-asynchronous-pattern
[12]: https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/consuming-the-task-based-asynchronous-pattern
[13]: https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types
[14]: https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/asynchronous-programming-model-apm
[15]: https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/cancel-async-tasks-after-a-period-of-time
[16]: https://stackoverflow.com/questions/23476576/cancellationtoken-timeout-vs-task-delay-and-timeout
[17]: https://devblogs.microsoft.com/pfxteam/coalescing-cancellationtokens-from-timeouts/
[18]: https://devblogs.microsoft.com/azure-sdk/how-to-use-cancellationtokens-to-cancel-tasks-in-the-azure-sdk-for-net/
[19]: https://learn.microsoft.com/en-us/archive/msdn-magazine/2019/november/csharp-iterating-with-async-enumerables-in-csharp-8
[20]: https://learn.microsoft.com/en-us/dotnet/azure/sdk/pagination
[21]: https://www.nuget.org/packages/System.Linq.Async
[22]: https://learning.oreilly.com/library/view/concurrency-in-c/9781492054498/ch04.html#recipe-parallel-dynamicparallelism

[<](./index.md) | [<<](/index.md)
