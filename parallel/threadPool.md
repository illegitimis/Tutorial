# Thread Pool

The _thread pool_ is used to reduce such costs and even to **avoid excessive context switching** by _multiplexing multiple units of work onto the same physical operating system thread_ that gets reused.

![Thread Pool Work Item Queue](https://1drv.ms/i/s!As0cxZAk26SzjMAeydTKsgDTy8YCYw)
![Thread Pool Work Item Queue](https://tcy0qq.by3302.livefilestore.com/y4m_9fMJVZOgAI1hocCPcUqbKYwkPqHBLJbdY0dfUfUwy02QcW6XZeJ06Yrgn7UNkmj4W9rpr9zdoarZkCY_r4YuzvfLAD4Q1vqck6WAwDiykHWAFusp_NM1tZyHpNzQu8qk5Ll4LWGFqsDY3wqQlgKTzpu91HqK0-sNySc0M7LzdQs3nXVm9SQXWSgEMAp4q1xdLCTUlsczR8IQ9YE5hXcgA?width=255&height=255&cropmode=none)

Creation of new threads is a _fairly expensive_ operation.
Allocation of the thread’s stack and various data structures requires the _scheduler database_ to be updated to gain knowledge about the thread’s existence.
Typical use of the thread pool is to deal with _relatively short-lived_ work items that _need to execute in the background_.
Reuses physical operating system threads.
**The .NET thread pool multiplexes work items onto system threads**.

_Using the thread pool for long-running work used to be problematic_ because you were stealing away a worker in the thread pool for a long time. 
The engineering done to the task infrastructure (and the underlying revamped thread pool on top of which the TPL and tasks are built) means that tasks can now be used for long-running work, too.



[<<](../parallel.md) 
| 
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 