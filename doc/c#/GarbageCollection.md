# Garbage Collection

- [Provides memory safety by making sure that an object cannot use the content of another object](https://msdn.microsoft.com/en-us/library/ee787088(v=vs.110).aspx). (immutable?)
- _Each process_ has its own, **separate virtual address space**. All processes on the same computer share the same physical memory, and share the page file if there is one. All threads in the process allocate memory for objects on the same heap. (The area of memory reserved for reference data is called the heap)
- By default, on 32-bit computers, each process has a _2-GB user-mode virtual address space_. 
- If you are writing native code, you use Win32 functions to work with the virtual address space. These functions allocate and free virtual memory for you on native heaps. 
- Virtual memory states: _free_, _reserved_ (for your use only, not any other app request), _committed_ (assigned to physical storage).
- `OutOfMemoryException`: run out of virtual address space or physical storage to commit
- 1st time physical memory pressure high => OS makes room in Physical Storage by backing up to page file.
- There is a **managed heap** _for each managed process_. _All threads in the process_ allocate memory for objects on the _same heap_.
- Conditions for GC
  - Low PhStor, physical memory
  - Allocated objects size on managed heap GT process threshold
  - `GC.Collect` call 
- GC initialized by CLR, _allocates a memory segment for each process_, to store and manage objects, which is the **managed heap**
- GC uses Win32 `VirtualAlloc`/`Free`.
- 2 heaps, large > 80KB, usually _arrays_, and **small object heap**
- Up until now, two techniques have been used on the Windows platform for _deallocating memory_ that processes have dynamically requested from the system:
  - Make the application code do it all _manually_.
  - Make objects maintain _reference counts_.
- The garbage collector runs through variables _currently in scope_ in your code, examining references to objects stored on the heap to identify which ones are accessible from your code, that is, _which objects have references that refer to them_. Any objects that are **not referred to** are deemed to be _no longer accessible_ from your code and can therefore be removed. Java uses a system of garbage collection similar to this.
- One important aspect of garbage collection is that it is **not deterministic**. In other words, you cannot guarantee when the garbage collector will be called; it will be called when the CLR decides that it is needed, though _it is also possible to override this process_ and call up the garbage collector in your code.
- Worry about GC? This is fine for the memory used by our objects, but might present a problem for the **system resources** in use. For example, the creation of a `Bitmap` object requires that a file be opened and loaded into memory. This requires file and other ~system resources~. Since such resources can be limited, it is a good idea to release them when you are finished. Since some objects use critical system resources such as _file handles_ or _database connections_, _handle from a Win32-style API_ that should be cleaned up as quickly as possible, a `Dispose` method is provided to do just this. Normally the _Dispose_ method is used to clean up **nonmemory** resources. For file objects such as `FileStream` and `StreamWriter`, the more traditional `Close` method is used. By definition, _Close_ is **equivalent to** _Dispose_ in the .NET Framework. Classes that provide a Close method are _automatically disposed of_ when the Close method is called.
- Although most code can remain oblivious to the garbage collector, it is _sometimes useful to be notified when an object is about to be collected_, which C# makes possible through **destructors**. The underlying runtime mechanism that supports this is called **finalization**, and it has some important pitfalls, so I’ll show how and how not to use destructors.
- **Value types** sometimes end up acting like reference types (_outlive method scope_), and being managed by the garbage collector, the **boxing mechanism** that makes it possible.
- A **heap block** contains all the _non-static fields for the object_. The CLR also adds a **header** which is _not directly visible to your program_. This includes a _pointer_ to a structure describing the object’s type. This supports operations that depend on the real type of an object. For example, if you call `GetType` on a reference of type object, the CLR uses this pointer to find out the type. It’s also used to work out which method to use when you invoke a **virtual method** or an interface member. The CLR also uses this to know how large the heap block is. The header does not include the block size, because the CLR can work that out from the object’s type. Most types are **fixed size**. There are only two exceptions, **strings** and **arrays**, which the CLR handles as special cases. The header contains one other field which is used for a variety of diverse purposes, including **multithreaded synchronization**, and **default hash code generation**. Heap block headers are just an _implementation detail_, and other CLI implementations could choose different strategies. However, it’s useful to know what the overhead is. On a 32-bit system, the header is 8 bytes long, and if you’re running in a 64-bit process, it takes 16 bytes. So an object that contained just one field of type double (an 8-byte type) would consume 16 bytes in a 32-bit process, and 24 bytes in a 64-bit process.
- A _variable_ is described as **live** from the first point where it receives a value up until the last point at which it is used. This information enables the runtime to determine at any time which objects are **reachable**, i.e., those which the program could conceivably get access to in order to use its fields and other members.
- **determining reachability**
  - a reference type static field is a **root reference**
  - root is a storage location, such as a local variable, which could contain a reference, and which is known to have been initialized, and that your program could use at some point in the future, without needing to go via some other object reference first.
  - Temporary objects created as a result of evaluating expressions need to stay alive for as long as necessary to complete the evaluation  
  - GCHandle class lets you create new roots explicitly
  - **Interop** with _COM objects_ can establish root references implicitly, COM wrappers for .Net code
  - Calls into unmanaged code may also involve passing pointers to memory on the heap, which will mean that the relevant heap block needs to be treated as reachable for the duration of the call
  - GC reachability vs COM reference counting, circular references scenario
- Ordinarily, the **large object heap** is _not compacted_, because copying large objects imposes a [performance penalty](https://msdn.microsoft.com/en-us/library/ee787088(v=vs.110).aspx). use the `GCSettings.LargeObjectHeapCompactionMode` > 4.5.1
- The garbage collector uses the following information to determine whether objects are live:
  - **Stack roots**. Stack variables provided by the just-in-time (JIT) compiler and stack walker.
  - **Garbage collection handles**. Handles that point to managed objects and that can be allocated by user code or by the common language runtime.
  - **Static data**. Static objects in application domains that could be referencing other objects. _Each application domain keeps track of its static objects_.
  
_Todo_ Pcs50 bw8 weak ref, reclaiming memory

[<<](../csdotnet.md) | [home](../../README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki)
