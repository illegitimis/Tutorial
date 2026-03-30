---
title: Thread Synchronization
layout: default
nav_order: 11
parent: Parallelism
grand_parent: .NET
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Thread Synchronization

```cs
public sealed class ReentranceGuard
{
    private int executionStatus = 0;

    public int ExecutionStatus => this.executionStatus;

    /// <summary>
    /// Returns true if no other thread has called <see cref="TryEnter"/> without calling <see cref="Exit"/>
    /// Note that the caller takes responsibility for calling Exit anytime TryEnter returns true,
    /// or all subsequent calls to TryEnter will return false.
    /// </summary>
    public bool TryEnter()
    {
        return 0 == Interlocked.CompareExchange(ref this.executionStatus, 1, 0);
    }

    /// <summary>
    /// Exits the timer callback by resetting the status. Call this in a finally clause when
    /// (and only when) TryEnter returns true.
    /// </summary>
    public void Exit()
    {
        Interlocked.Exchange(ref this.executionStatus, 0);
    }
}
```

`Interlocked.MemoryBarrier` [1] \
`Interlocked.MemoryBarrierProcessWide` [2] \
`AsymmetricLock` gist by jkotas [3] \
Add `Interlocked.MemoryBarrierProcessWide` method [4] \
`Interlocked.CompareExchange` [5] \
LogoFX `ReentranceGuard.cs` [6] \
`Interlocked.CompareExchange` missing for uint, ulong and general structs [7]

[1]: https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.memorybarrier?view=net-7.0
[2]: https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.memorybarrierprocesswide?view=net-7.0#system-threading-interlocked-memorybarrierprocesswide
[3]: https://gist.github.com/jkotas/aff2ca3774414807be7312fa00d3d521
[4]: https://github.com/dotnet/runtime/issues/20500
[5]: https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange?view=net-7.0
[6]: https://github.com/godrose/LogoFX.Sample/blob/master/LogoFX.Core/ReentranceGuard.cs
[7]: https://github.com/dotnet/runtime/issues/24694

[<](./index.md) | [<<](/index.md)