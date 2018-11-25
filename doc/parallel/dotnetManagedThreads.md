# Managed Threads

In reality, it is always worth keeping in mind that multithreading is most commonly an _illusion_
provided by the OS. Machines that host a single CPU do not have the ability to literally handle multiple threads at the same exact time. 
Rather, _a single CPU_ will execute one thread for a unit of time (called a **time slice**) based on the thread’s priority level. 
When a thread’s time slice is up, the existing thread is suspended to allow another thread to perform its business. 
For a thread to remember what was happening before it was kicked out of the way, each thread is given the ability to write to Thread Local Storage (**TLS**) and is provided with a separate call stack, as illustrated in the figure.
If the subject of threads is new to you, don’t sweat the details. 
At this point, just remember that a thread is a **unique path of execution within a Win32 process**. 
Every process has a primary thread (created via the executable’s entry point) and may contain additional threads that have been programmatically created.

![thread local storage](https://jxhveg.by3302.livefilestore.com/y4mDWyO5mGmDnnpv6nupmw0vnn6XxllbvdptSjIDSfFDp5iHO_gRAQuC5-3t9AviZW7Ru9Q04J-IyJteqKKw5ZHT7fXl0fvquP3FVwzaTZr-5j-Kqc6Uw8qMN-Y4utwPFX9t97BlaC0e8dHSexzdGP8KU5SePnS-6-rkGww_3wiAQxEDFBFc4nmr2TZLcvGp0wU_lR2EkcbM6fPxnDnnfGw1A?width=660&height=251&cropmode=none)
![thread local storage](https://1drv.ms/i/s!As0cxZAk26SzjMAcyWdBFOuPKpav1g)

The common language runtime itself creates a number of threads (for example, for finalization and garbage collection). 
Threads running managed code are typically referred to as _managed threads_, while others are called _native threads_.
Managed threads happen to be backed by native threads on which the CLR piggybacks, allowing the operating system’s threading facilities to offer their benefits. 
Each (native or managed) thread has its own call stack.

Upon calling `Abort`, the CLR will throw a `ThreadAbortException` in the target thread. 
This is often referred to as an **asynchronous exception** because it can occur at any point in the target thread.

**The closest you can get** to a “raw thread” is using the `Thread` class.

![native and managed threads coexisting](https://wowwtq.by3302.livefilestore.com/y4m49V0QN666YktnskCe9_14nP7ecAfFBClpxWVoRMimn_qcWjhjkEUVdVlBUum-RdFsTORm6Nvx8cpPjpPaKsXcIXo7jhm12NVHZYEDgOMwRr8Vkp_L20iGpJByekm5pRtFvi4V4cIThv1C0ooL5eRWlSjKQtihjQoECXYE_Mehw-fl55g2Y2vnU3PV00lmdZrWVms2ip_Z4S3FeDFw61lLg?width=400&height=232&cropmode=none)
![native and managed threads coexisting](https://1drv.ms/i/s!As0cxZAk26SzjMAdXvDFkmDp2NOBnQ)

[<<](../parallel.md) | [home](../../README.md)