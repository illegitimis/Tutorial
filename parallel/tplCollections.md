# TPL Collections

## new concurrent collections lock-free?

All of the collections in the new `System.Collections.Concurrent` namespace employ lock-free techniques to some extent in order to achieve general performance benefits, [but traditional locks are used in some cases](https://blogs.msdn.microsoft.com/pfxteam/2010/01/26/faq-are-all-of-the-new-concurrent-collections-lock-free/).

It’s worth noting that _purely relying on lock-free techniques_ is _sometimes_ **not the most efficient solution**.  When we say “lock-free,” we mean that locks (in .NET, traditional _mutual exclusion_ locks are available via the `System.Threading.Monitor` class, typically via the C# `lock` keyword or the Visual Basic `SyncLock` keyword) have been avoided by using **memory barriers** and **compare-and-swap CPU instructions** (in .NET, “CAS” operations are available via the `System.Threading.Interlocked` class).

`ConcurrentQueue<T>` and `ConcurrentStack<T>` are **completely lock-free** in this way. They will never take a lock, but they _may end up spinning and retrying_ an operation when faced with **contention** (when the CAS operations fail).

`ConcurrentBag<T>` employs a multitude of mechanisms to _minimize the need for synchronization_. For example, it _maintains a local queue for each thread_ that accesses it, and under some conditions, a thread is able to access its local queue in a lock-free manner with _little or no contention_. Therefore, while `ConcurrentBag<T>` sometimes requires locking, it is a very efficient collection for certain concurrent scenarios (e.g. many threads both producing and consuming at the same rate).

`ConcurrentDictionary<TKey,TValue>` uses **fine-grained locking** when adding to or updating data in the dictionary, but it is **entirely lock-free for read operations**. In this way, it’s _optimized for scenarios where reading from the dictionary is the most frequent operation_.

[home](./README.md)
|
[<<](./parallel.md)
|
[wiki](https://github.com/illegitimis/Tutorial/wiki)