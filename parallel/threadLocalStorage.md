# Thread Local Storage

_Static state_ is **isolated** on a _per-application domain_ basis. 
```cs
	//each thread has its own copy of the field
	[ThreadStatic] static int s_i; 
```

The managed code abstraction that sits the closest to operating system primitives 
for thread-local storage is known as data slots.
```cs
    // Initialization code.
    LocalDataStoreSlot slot = Thread.AllocateNamedDataSlot(“logger”);
    Thread.SetData(slot, new Logger() /* type definition omitted for brevity */);
    // use
    var slot = Thread.GetNamedDataSlot(“logger”);
    var logger = (Logger)Thread.GetData(slot);
    logger.WriteLine(“Diagnostic message”);
```
   

Closely related to the `Lazy<T>` class, the `ThreadLocal<T>` class was introduced in .NET 4. 
Essentially, this type addresses the shortcomings of the `ThreadStatic` attribute when 
**initialization code is required for the per-thread state**. 
The `ThreadLocal<T>` class acts as a _factory for per-thread state_, 
using a `Func<T>` delegate that’s invoked once per thread upon calling the `Value` property. 
```cs
    static ThreadLocal<TextWriter> s_log = new ThreadLocal<TextWriter>(() => {
        string name = Thread.CurrentThread.Name ?? Thread.CurrentThread.ManagedThreadId.ToString();
        // More complicated initialization logic could be dreamed up.
        // What matters is the fact this method will run multiple times  on different threads, initializing that thread’s logger.
        return File.CreateText(name + “.log”);
    });
```
    

	
[<<](../csdotnet.md) 
|
[home](https://github.com/illegitimis/Tutorial) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 