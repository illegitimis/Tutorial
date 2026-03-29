# Parallelism

> Managed threading model, task-based asynchrony, thread pool, concurrent collections, and TPL Dataflow.

## Pages

- [Managed Threads](./managed-threads.md) — OS thread scheduling, time slices, and the .NET threading model
- [Background vs Foreground Threads](./background-foreground-threads.md) — lifetime differences: foreground threads keep a process alive; background threads do not
- [Threads vs Processes](./threads-vs-processes.md) — process and thread relationships; threads as miniprocesses sharing an address space
- [Threads vs Tasks](./threads-vs-tasks.md) — **Tasks** as lightweight abstractions over OS threads running on the thread pool
- [UI Threads](./ui-threads.md) — WinForms and WPF UI thread dispatching and cross-thread UI updates
- [Thread Pool](./thread-pool.md) — thread pool work-item queue, context switching reduction, and multiplexing
- [Thread Local Storage](./thread-local-storage.md) — per-thread state isolation using `ThreadLocal<T>` and `[ThreadStatic]`
- [TPL Collections](./tpl-collections.md) — `System.Collections.Concurrent` lock-free concurrent collections
- [TPL Dataflow](./tpl-dataflow.md) — **TPL Dataflow** actor/agent model: in-process message passing, dataflow pipelines, and `C#` async integration

[<<](../index.md) | [home](../../README.md)
