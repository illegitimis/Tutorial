# Threads vs Processes

Threads are **miniprocesses**.

An _application_ consists of **one or more processes**. 
A process, in the simplest terms, is an executing program. One or more threads run in the context of the process. 
A thread is the _basic unit_ to which the operating system _allocates processor time_. 
A thread can execute any part of the process code, including parts currently being executed by another thread. 
> From <https://msdn.microsoft.com/en-us/library/windows/desktop/ms684841(v=vs.85).aspx>

Each process provides the resources needed to execute a program. 
A process has a **virtual address space**, **executable code**, **open handles to system objects**, a **security context**, a unique process identifier, **environment variables**, a **priority** class, minimum and maximum working set sizes, and _at least one thread of execution_. Each process is started with a single thread, often called the **primary** thread, but **can create additional threads from any of its threads**.

A thread is the **entity within a process that can be scheduled for execution**. 
All threads of a process _share its virtual address space and system resources_. 
In addition, **each** thread _maintains exception handlers_, a scheduling priority, **thread local storage**, a unique thread identifier, and a _set of structures_ the system will use to **save the thread context until it is scheduled**. 
The thread context includes the thread's set of _machine registers_, the **kernel stack**, a thread environment block, and a _user stack in the address space of the thread's process_. 
Threads can also have their own **security context**, which can be used for _impersonating_ clients.
Microsoft Windows supports **preemptive multitasking**, which creates the effect of simultaneous execution of multiple threads from multiple processes. 
On a multiprocessor computer, the system can simultaneously execute as many threads as there are processors on the computer.
> From <https://msdn.microsoft.com/en-us/library/windows/desktop/ms681917(v=vs.85).aspx>

A thread is analogous to the operating system process in which your application runs. 
Just as processes run in parallel on a computer, threads run in parallel within a single process. 
Processes are fully isolated from each other; threads have just a limited degree of isolation. 
In particular, threads **share (heap) memory with other threads running in the same application**. 
This, in part, is why threading is useful: one thread can fetch data in the background, for instance, while another thread can display the data as it arrives.

Processes executing on Windows can have multiple threads inside them. 
**Threads are where code is executed**, and multiple threads can carry out different tasks at the same time. 
This is achieved by running code on different cores or creating a multicore illusion using (preemptive) operating system scheduling. 

The operating system kernel is responsible for scheduling threads according to a policy that consists of various factors threads can have relative priorities, causing the scheduler to favor one thread over another / can be boosted.
it should be clear that processes are merely some collection of threads and some associated data structures, but threads are really what gets scheduled and run by the operating system.

When the scheduler decides to take away a thread from a processor on which it’s running, it stores away the thread’s state so that it can be rehydrated when the thread is assigned to a processor for execution again. 
Preemptive / time slice / taken away from the processor forcefully by the kernel’s scheduler.

**Context switch** = The mechanism of storing one thread’s state and restoring another one’s to give the latter a chance to execute.
**Fiber** = lightweight threads but suffer from quite a few limitations (for example, thread-local storage becomes problematic)

[<<](../parallel.md) | [home](../../README.md)