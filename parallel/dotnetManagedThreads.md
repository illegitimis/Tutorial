# Managed Threads

In reality, it is always worth keeping in mind that multithreading is most commonly an _illusion_
provided by the OS. Machines that host a single CPU do not have the ability to literally handle multiple threads at the same exact time. Rather, _a single CPU_ will execute one thread for a unit of time
(called a **time slice**) based on the thread’s priority level. When a thread’s time slice is up, the existing
thread is suspended to allow another thread to perform its business. For a thread to remember what
was happening before it was kicked out of the way, each thread is given the ability to write to Thread
Local Storage (**TLS**) and is provided with a separate call stack, as illustrated in the figure.
If the subject of threads is new to you, don’t sweat the details. At this point, just remember that
a thread is a **unique path of execution within a Win32 process**. Every process has a primary thread
(created via the executable’s entry point) and may contain additional threads that have been programmatically created.

![thread local storage](https://jxhveg.by3302.livefilestore.com/y3mDWyO5mGmDnnpv6nupmw0vnyJk4_qHZ3gIk_QjzEGXHV4MoT7NfY2NeaRwB5ZHYSePt7fU16i731x52_cug2KLQfzEHTJFkBCjkraH8Yll6R1ZH_qIJAHRLizdXCgyzVSPO5K-wlBBa7sN618kntE3vgzsj8jIUNdNzJN9poSDHo?width=747&height=284&cropmode=none)

The common language runtime itself creates a number of threads (for example, for finalization and garbage collection). 
Threads running managed code are typically referred to as managed threads, while others are called native threads
Managed threads happen to be backed by native threads on which the CLR piggybacks, allowing the operating system’s threading facilities to offer their benefits. Each (native or managed) thread has its own call stack.

Upon calling `Abort`, the CLR will throw a `ThreadAbortException` in the target thread. This is often referred to as an **asynchronous exception** because it can occur at any point in the target thread.



**The closest you can get to a “raw thread” is using the `Thread` class**

![native and managed threads coexisting](https://wowwtq.by3302.livefilestore.com/y3m49V0QN666YktnskCe9_14hLbA45yTDdOTEanwgJYiSXlbwlYIchaez8T27_sKhsfwUF7bC_4UquHlAzYwc7Zly1MfqucWNMUH3N8s3LMd-0Dbx1vmAXeGjXVnvBGRRiUmtJlAQKApuKZoqKfns4UnZtZ826AdbgNCQ0K20A6NPg?width=400&height=232&cropmode=none)


