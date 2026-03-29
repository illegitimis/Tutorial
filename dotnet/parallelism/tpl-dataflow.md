# TPL Dataflow

**TPL** Dataflow (TDF) is a .NET library for building concurrent applications. It promotes actor/agent-oriented designs through primitives for in-process message passing, **dataflow**, and pipelining. TDF builds upon the APIs and scheduling infrastructure provided by the Task Parallel Library (`TPL`) in .NET 4, and integrates with the language support for asynchrony provided by C#, Visual Basic, and F#.

## Overview

The Task Parallel Library (`TPL`) was introduced in the .NET Framework 4, providing core building blocks and algorithms for parallel computation and asynchrony, centered around `System.Threading.Tasks.Task` and higher-level constructs (e.g. `Parallel.For`/`ForEach`).

`TPL` Dataflow (TDF) builds on that foundational layer, addressing scenarios best expressed with agent-based models or message-passing paradigms — prevalent in finance, biological sciences, oil & gas, and manufacturing. TDF utilizes tasks, concurrent collections, tuples, and other .NET 4 features to bring support for parallel **dataflow**-based programming into the framework.

TDF can be thought of as a logical evolution of the Concurrency & Coordination Runtime (CCR) for non-robotics scenarios, incorporating CCR's key concepts into `TPL` and augmenting the model with core aspects of the Asynchronous Agents Library (AAL) from Visual C++ 2010.

## Architecture

At its heart, TDF is based on two interfaces: `ISourceBlock<T>` and `ITargetBlock<T>`. Sources offer data; targets are offered data. Nodes in a **dataflow** network may be one, the other, or both (propagators).

Key capabilities enabled by this model:

- Parallel stream processing and multiple forms of data buffering
- Greedy and non-greedy receiving, joining, and batching from one or more sources
- Selecting a single datum from multiple sources
- Protecting concurrent operations without explicit locking via a declarative reader/writer model
- Automatically propagating data from operation to operation with configurable concurrency

## Getting Started

`TPL` Dataflow is packaged as `System.Threading.Tasks.Dataflow.dll`. Add a reference to this DLL from your managed project. Most functionality lives in the `System.Threading.Tasks.Dataflow` namespace.

### Introductory Examples

**Post data to an `ActionBlock`:**

```csharp
var ab = new ActionBlock<int>(i =>
{
    Compute(i);
});

ab.Post(1);
ab.Post(2);
ab.Post(3);
```

**Async producer/consumer with `BufferBlock<T>`:**

```csharp
private static BufferBlock<int> m_buffer = new BufferBlock<int>();

// Producer
private static void Producer()
{
    while (true)
    {
        int item = Produce();
        m_buffer.Post(item);
    }
}

// Consumer
private static async Task Consumer()
{
    while (true)
    {
        int item = await m_buffer.ReceiveAsync();
        Process(item);
    }
}
```

## Foundational Features

`TPL` Dataflow is comprised of **dataflow** blocks — data structures that buffer, process, and propagate data. They can be sources, targets, or both (propagators).

### Interfaces

All **dataflow** blocks implement `IDataflowBlock`:

```csharp
public interface IDataflowBlock
{
    void Complete();
    void Fault(Exception error);
    Task Completion { get; }
}
```

Source blocks implement `ISourceBlock<TOutput>`:

```csharp
public interface ISourceBlock<out TOutput> : IDataflowBlock
{
    bool TryReceive(out TOutput item, Predicate<TOutput> filter);
    bool TryReceiveAll(out IList<TOutput> items);

    IDisposable LinkTo(ITargetBlock<TOutput> target, bool unlinkAfterOne);

    bool ReserveMessage(DataflowMessageHeader messageHeader, ITargetBlock<TOutput> target);
    TOutput ConsumeMessage(DataflowMessageHeader messageHeader, ITargetBlock<TOutput> target, out bool messageConsumed);
    void ReleaseReservation(DataflowMessageHeader messageHeader, ITargetBlock<TOutput> target);
}
```

Target blocks implement `ITargetBlock<TInput>`:

```csharp
public interface ITargetBlock<in TInput> : IDataflowBlock
{
    DataflowMessageStatus OfferMessage(
        DataflowMessageHeader messageHeader, TInput messageValue,
        ISourceBlock<TInput> source, bool consumeToAccept);
}
```

Propagator blocks implement both:

```csharp
public interface IPropagatorBlock<in TInput, out TOutput> :
    ITargetBlock<TInput>, ISourceBlock<TOutput> { }
```

Receivable sources additionally implement `IReceivableSourceBlock<TOutput>`:

```csharp
public interface IReceivableSourceBlock<TOutput> : ISourceBlock<TOutput>
{
    bool TryReceive(out TOutput item, Predicate<TOutput> filter);
    bool TryReceiveAll(out IList<TOutput> items);
}
```

## Built-in Dataflow Blocks

The built-in blocks fall into three categories: **pure buffering**, **execution**, and **grouping**.

### Pure Buffering Blocks

#### `BufferBlock<T>`

The most fundamental block — an unbounded or bounded FIFO buffer for `T`. Analogous to `Port<T>` in CCR and `unbounded_buffer<T>` in the native Agents library. Each buffered element is handed to exactly one receiver.

**Synchronous producer/consumer:**

```csharp
private static BufferBlock<int> m_buffer = new BufferBlock<int>();

private static void Producer()
{
    while (true) m_buffer.Post(Produce());
}

private static void Consumer()
{
    while (true) Process(m_buffer.Receive());
}

public static void Main()
{
    var p = Task.Factory.StartNew(Producer);
    var c = Task.Factory.StartNew(Consumer);
    Task.WaitAll(p, c);
}
```

**Asynchronous producer/consumer:**

```csharp
private static BufferBlock<int> m_buffer = new BufferBlock<int>();

private static void Producer()
{
    while (true) m_buffer.Post(Produce());
}

private static async Task Consumer()
{
    while (true) Process(await m_buffer.ReceiveAsync());
}

public static void Main()
{
    var p = Task.Factory.StartNew(Producer);
    var c = Consumer();
    Task.WaitAll(p, c);
}
```

**Throttled producer with `BoundedCapacity`:**

```csharp
private static BufferBlock<int> m_buffer = new BufferBlock<int>(
    new DataflowBlockOptions { BoundedCapacity = 10 });

private static async void Producer()
{
    while (true) await m_buffer.SendAsync(Produce());
}

private static async Task Consumer()
{
    while (true) Process(await m_buffer.ReceiveAsync());
}

private static async Task Run()
{
    await Task.WhenAll(Producer(), Consumer());
}
```

**Exposing ports from an agent type:**

```csharp
public class MyAgent
{
    public MyAgent()
    {
        IncomingMessages = new BufferBlock<int>();
        OutgoingMessages = new BufferBlock<string>();
        Run();
    }

    public ITargetBlock<int>    IncomingMessages { get; private set; }
    public ISourceBlock<string> OutgoingMessages { get; private set; }

    private async void Run()
    {
        while (true)
        {
            int message = await IncomingMessages.ReceiveAsync();
            OutgoingMessages.Post(message.ToString());
        }
    }
}

// Usage
MyAgent ma = new MyAgent();
ma.IncomingMessages.Post(42);
string result = ma.OutgoingMessages.Receive();
```

#### `BroadcastBlock<T>`

Broadcasts every element to all linked targets (each gets a copy via a user-provided `Func<T,T>` clone). Unlike `BufferBlock<T>`, it overwrites its "current" value and does not hold on to data unnecessarily. Equivalent to `overwrite_buffer<T>` in the native Agents library.

**Save images to disk and display in UI:**

```csharp
var ui = TaskScheduler.FromCurrentSynchronizationContext();
var bb = new BroadcastBlock<ImageData>(i => i);

var saveToDisk = new ActionBlock<ImageData>(item =>
    item.Image.Save(item.Path));

var showInUi = new ActionBlock<ImageData>(item =>
    imagePanel.AddImage(item.Image),
    new DataflowBlockOptions { TaskScheduler = ui });

bb.LinkTo(saveToDisk);
bb.LinkTo(showInUi);
```

**Exposing status from an agent:**

```csharp
public class MyAgent
{
    public MyAgent()
    {
        Status = new BroadcastBlock<string>();
        Run();
    }

    public ISourceBlock<string> Status { get; private set; }

    private void Run()
    {
        Status.Post("Starting");
        // ...
        Status.Post("Doing cool stuff");
        // ...
        Status.Post("Done");
    }
}
```

#### `WriteOnceBlock<T>`

Stores at most one value; once set it is immutable. All consumers may obtain a copy. Equivalent to `single_assignment<T>` in the native Agents library.

**Receive from any of multiple sources:**

```csharp
public T ReceiveFromAny<T>(params ISourceBlock<T>[] sources)
{
    var wob = new WriteOnceBlock<T>();
    foreach (var source in sources) source.LinkTo(wob, unlinkAfterOne: true);
    return wob.Receive();
}
```

**Splitting a task's potential outputs:**

```csharp
public static async void SplitIntoBlocks(this Task<T> task,
    out IPropagatorBlock<T> result,
    out IPropagatorBlock<Exception> exception)
{
    result    = new WriteOnceBlock<T>(i => i);
    exception = new WriteOnceBlock<Exception>(i => i);

    try   { result.Post(await task); }
    catch (Exception exc) { exception.Post(exc); }
}
```

**Request/response pattern:**

```csharp
// with WriteOnceBlock<T>
var request  = /* ... */;
var response = new WriteOnceBlock<TResponse>();
target.Post(Tuple.Create(request, response));
var result = await response.ReceiveAsync();

// with TaskCompletionSource<T>
var request  = /* ... */;
var response = new TaskCompletionSource<TResponse>();
target.Post(Tuple.Create(request, response));
var result = await response.Task;
```

### Execution Blocks

#### `ActionBlock<TInput>`

Executes a delegate (`Action<TInput>` or `Func<TInput,Task>`) for each input. By default processes one message at a time in FIFO order; can be configured for parallelism.

**Sequential synchronous download:**

```csharp
var downloader = new ActionBlock<string>(url =>
{
    byte[] imageData = Download(url);
    Process(imageData);
});

downloader.Post("http://msdn.com/concurrency");
downloader.Post("http://blogs.msdn.com/pfxteam");
```

**Sequential asynchronous download:**

```csharp
var downloader = new ActionBlock<string>(async url =>
{
    byte[] imageData = await DownloadAsync(url);
    Process(imageData);
});
```

**Throttled to at most 5 concurrent downloads:**

```csharp
var downloader = new ActionBlock<string>(async url =>
{
    byte[] imageData = await DownloadAsync(url);
    Process(imageData);
}, new DataflowBlockOptions { MaxDegreeOfParallelism = 5 });
```

**Load balancing across N workers:**

```csharp
var dbo     = new DataflowBlockOptions { BoundedCapacity = 1 };
var workers = (from i in Enumerable.Range(0, N)
               select new ActionBlock<int>(DoWork, dbo)).ToArray();

ISourceBlock<int> dataSource = /* ... */;
foreach (var worker in workers) dataSource.LinkTo(worker);
```

**Processing on the UI thread:**

```csharp
var ab = new ActionBlock<Bitmap>(image =>
{
    panel.Add(image);
    txtStatus.Text = "Added image #" + panel.Items.Count;
}, new DataflowBlockOptions
{
    TaskScheduler = TaskScheduler.FromCurrentSynchronizationContext()
});
```

#### `TransformBlock<TInput, TOutput>`

Like `ActionBlock<TInput>` but produces one output per input (`Func<TInput,TOutput>` or `Func<TInput,Task<TOutput>>`). Buffers both inputs and outputs. Preserves output order even when processing concurrently.

**Concurrent compression/encryption pipeline:**

```csharp
var compressor = new TransformBlock<byte[], byte[]>(input => Compress(input));
var encryptor  = new TransformBlock<byte[], byte[]>(input => Encrypt(input));
compressor.LinkTo(encryptor);
```

#### `TransformManyBlock<TInput, TOutput>`

Like `TransformBlock` but produces zero or more outputs per input (`Func<TInput,IEnumerable<TOutput>>` or async variant).

**Async web crawler (self-linking):**

```csharp
var downloader = new TransformManyBlock<string, string>(async url =>
{
    Console.WriteLine("Downloading " + url);
    try { return ParseLinks(await DownloadContents(url)); }
    catch { }
    return Enumerable.Empty<string>();
});
downloader.LinkTo(downloader);
```

**Filter (1 → 0 or 1 element):**

```csharp
public IPropagatorBlock<T, T> CreateFilteredBuffer<T>(Predicate<T> filter)
{
    return new TransformManyBlock<T, T>(item =>
        filter(item) ? new[] { item } : Enumerable.Empty<T>());
}
```

### Grouping Blocks

#### `BatchBlock<T>`

Combines N single items into one batch (`T[]`). Supports greedy (default) and non-greedy modes. Can be configured with `MaxNumberOfGroups`.

**Batch database requests in groups of 100:**

```csharp
var batchRequests = new BatchBlock<Request>(batchSize: 100);
var sendToDb      = new ActionBlock<Request[]>(reqs => SubmitToDatabase(reqs));
batchRequests.LinkTo(sendToDb);
```

**Create a batch every second:**

```csharp
var batch = new BatchBlock<T>(batchSize: int.MaxValue);
new Timer(delegate { batch.TriggerBatch(); }).Change(1000, 1000);
```

#### `JoinBlock<T1, T2, ...>`

Groups data from multiple sources into output tuples — one element from each input target per tuple. Available as `JoinBlock<T1,T2>` and `JoinBlock<T1,T2,T3>`. Supports greedy and non-greedy modes with a two-phase commit protocol.

**Process requests with a pool of expensive objects:**

```csharp
var throttle = new JoinBlock<ExpensiveObject, Request>();
for (int i = 0; i < 10; i++)
    throttle.Target1.Post(new ExpensiveObject());

var processor = new TransformBlock<Tuple<ExpensiveObject, Request>, ExpensiveObject>(pair =>
{
    pair.Item2.ProcessWith(pair.Item1);
    return pair.Item1;
});

throttle.LinkTo(processor);
processor.LinkTo(throttle.Target1);
```

#### `BatchedJoinBlock<T1, T2, ...>`

Combines `BatchBlock<T>` and `JoinBlock` — gathers N inputs from all targets into tuples of collections (`ISourceBlock<Tuple<IList<T1>,IList<T2>>>`).

**Scatter/gather with error collection:**

```csharp
var batchedJoin = new BatchedJoinBlock<string, Exception>(10);

for (int i = 0; i < 10; i++)
{
    Task.Factory.StartNew(() =>
    {
        try   { batchedJoin.Target1.Post(DoWork()); }
        catch (Exception e) { batchedJoin.Target2.Post(e); }
    });
}

var results = await batchedJoin.ReceiveAsync();
foreach (string s    in results.Item1) Console.WriteLine(s);
foreach (Exception e in results.Item2) Console.WriteLine(e);
```

## Beyond the Basics

### Configuration Options

All configuration is done via `DataflowBlockOptions` (and its derived types `ExecutionDataflowBlockOptions`, `GroupingDataflowBlockOptions`) passed at construction.

| Option | Default | Description |
|---|---|---|
| `TaskScheduler` | `TaskScheduler.Default` | Scheduler for all block work. Use `FromCurrentSynchronizationContext()` for UI thread work; use `ConcurrentExclusiveSchedulerPair` for reader/writer scheduling across blocks. |
| `MaxDegreeOfParallelism` | `1` | Maximum concurrent messages. `-1` = unbounded (managed by the scheduler). |
| `MaxMessagesPerTask` | `-1` (unbounded) | Max messages processed per task before the task is retired and replaced, enabling fairness between blocks. Set to `1` for ultimate fairness. |
| `MaxNumberOfGroups` | `-1` (unbounded) | Grouping blocks auto-complete after producing this many groups. |
| `CancellationToken` | None | Token monitored during block lifetime. On cancellation, the block stops accepting work, purges buffered data, drops source/target links, and transitions to `Canceled` state. |
| `Greedy` | `true` | When `false`, join/batch blocks postpone offered messages and use a two-phase commit to atomically consume from all sources. Prevents starvation in fan-out scenarios. |
| `BoundedCapacity` | `-1` (unbounded) | Maximum items buffered + in-flight. Excess offers are postponed. Use with `BroadcastBlock<Frame>` + bounded `ActionBlock<Frame>` to process only the latest frame from a webcam. |

### Static Methods on `DataflowBlock`

| Method | Description |
|---|---|
| `Choose` | Atomically accept one message across multiple sources, executing the associated action delegate. |
| `Encapsulate` | Create a propagator from a separate target block and source block. |
| `LinkTo` (extension) | Link source to target with optional filter predicate and behavior-on-no-match. |
| `OutputAvailableAsync` | Async notification when data is available (or will never be) on a source; data is not removed. |
| `Post` (extension) | Synchronously post to a target; returns immediately with accept/reject result. |
| `SendAsync` (extension) | Async post with buffering — if the target postpones, the data is held until the target can consume it. |
| `Receive` (extension) | Synchronously receive from a source; blocks until data arrives (with optional timeout/cancellation). |
| `ReceiveAsync` (extension) | Async version of `Receive`; returns `Task<TOutput>`. |
| `AsObservable` (extension) | Expose an `ISourceBlock<T>` as `IObservable<T>` for Rx integration. |
| `AsObserver` (extension) | Expose an `ITargetBlock<T>` as `IObserver<T>` — `OnNext` sends, `OnError` faults, `OnCompleted` completes. |

### Debugging

- **`DebuggerDisplayAttribute`** — All relevant types show buffer counts at a glance (e.g. `ActionBlock` shows messages waiting; `TransformBlock` shows input and output queue depths).
- **Debugger Type Proxies** — Drill-in views expose buffered data, processing state, and linked blocks (e.g. `JoinBlock` tooltip shows each target's queue).

## Developing Custom Dataflow Blocks

Custom blocks can be built by composing existing blocks with `Encapsulate`, or by directly implementing `ITargetBlock<TInput>` / `ISourceBlock<TOutput>` / `IPropagatorBlock<TInput,TOutput>`.

**Sliding window using `Encapsulate`:**

```csharp
private static IPropagatorBlock<T, T[]> CreateSlidingWindow<T>(int windowSize)
{
    var queue  = new Queue<T>();
    var source = new BufferBlock<T[]>();
    var target = new ActionBlock<T>(item =>
    {
        queue.Enqueue(item);
        if (queue.Count >  windowSize) queue.Dequeue();
        if (queue.Count == windowSize) source.Post(queue.ToArray());
    });

    target.Completion.ContinueWith(t =>
    {
        if (queue.Count > 0 && queue.Count < windowSize) source.Post(queue.ToArray());
        if (t.IsFaulted) source.Fault(t.Exception);
        else source.Complete();
    });

    return DataflowBlockExtensions.Encapsulate(target, source);
}
```

**Custom class implementing `IPropagatorBlock`:**

```csharp
public class SlidingWindowBlock<T> : IPropagatorBlock<T, T[]>
{
    private readonly int m_windowSize;
    private readonly ITargetBlock<T>   m_target;
    private readonly ISourceBlock<T[]> m_source;

    public SlidingWindowBlock(int windowSize)
    {
        var queue  = new Queue<T>();
        var source = new BufferBlock<T[]>();
        var target = new ActionBlock<T>(item =>
        {
            queue.Enqueue(item);
            if (queue.Count >  windowSize) queue.Dequeue();
            if (queue.Count == windowSize) source.Post(queue.ToArray());
        });

        m_windowSize = windowSize;
        m_target     = target;
        m_source     = source;
    }

    // ... delegate ITargetBlock and ISourceBlock members to m_target / m_source
}
```

By correctly implementing one or more of the **dataflow** interfaces, custom blocks integrate into a **dataflow** network exactly like built-in blocks, and all extension methods "just work".

---

[1]: https://docs.microsoft.com/en-us/dotnet/standard/parallel-programming/dataflow-task-parallel-library


[<<](./index.md) | [home](../../README.md)
