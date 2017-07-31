# Finalizers

```cs
// method of `Object` class.
protected virtual void Finalize()
```

Allows an object to try to _free resources and perform other cleanup operations_ **before** _it is reclaimed by garbage collection_. 
The Finalize method is used to perform cleanup operations on **unmanaged resources** _held by the current object_ before the object is destroyed. 
The only reason finalization exists is to make it possible to write .NET types that are wrappers for entities that are traditionally represented by handles—things like files, and sockets. 
Finalizers = they are a place to put code that tells the system that’s **external to the CLR** that the entity represented by the handle is no longer in use.

The method is protected and therefore is accessible only through this class or through a derived class. 
The _finalization queue_ contains entries for all the objects in the managed heap whose finalization code must run before the garbage collector can reclaim their memory.

`GC.ReRegisterForFinalize` / `GC.SuppressFinalize` / unless finalize runs only once.

If a `SafeHandle` object is available that wraps your unmanaged resource, the _recommended_ alternative is to **implement the dispose pattern with a safe handle and not override** `Finalize`.

CLR only finalizes reference types. _Every implementation of Finalize must call base class impl of finalizer_. 
[Unhandled system exceptions](https://msdn.microsoft.com/en-us/library/system.object.finalize%28v=vs.110%29.aspx) such as `OutOfMemoryException` and `StackOverflowException` terminate the finalizer. 

Complicates matters by introducing a twilight zone in which the object has been determined to be unreachable, but has not yet gone. 
If the finalization thread hasn’t managed to run all extant finalizers _within two seconds_ of the program trying to finish, it just gives up and exits anyway => no guarantees.

Finalization = the CLR can first tell an object that it is about to be removed. To exploit it, **you must write a destructor**. 

> Traditionally, the term “_destructor_” refers to a deterministic cleanup method and a “_finalizer_” refers to a nondeterministic cleanup method called by a garbage collector. 
“Destructor” is a bit of an unfortunate misnomer in C#; 
Ideally these methods would be called “finalizers” and the **Dispose** method of `IDisposable` would be called a “_destructor_.” 
(ERIC LIPPERT)

Finalizers run on a _dedicated thread_, and this finalization thread runs with _low priority_, meaning that it will only run when the system has at least one logical CPU with nothing better to do. 
Also, since there’s only one finalization thread, regardless of which `GC` mode you choose, _a slow finalizer will cause other finalizers to wait_.

Finalizers are always required to call the base implementation of Finalize that they override. 
C# generates that call for us to prevent us from violating the rule, which is why it doesn’t let us simply write a Finalize method directly. 
_Finalizers are not invoked directly_—they are called by the CLR, so we do not specify an accessibility level for the destructor.

> Calling Dispose doesn’t influence garbage collection in any way. An object becomes eligible for automatic garbage collection when (and only when) no other object refers to it. 
Likewise, garbage collection doesn’t influence disposal: 
The garbage collector will not call Dispose unless you write a finalizer (destructor) that explicitly makes this call. 
The two activities most commonly performed within a Dispose method are releasing unmanaged resources and calling Dispose on other referenced or “owned” objects. 
It is also possible to release unmanaged resources from within a finalizer, although such an operation means waiting an indeterminate amount of time for the garbage collector to fire. 
This is why IDisposable exists. 
(JoSEPH ALBAHARI)

**Critical Finalizers** =  guaranteed to run, must derive from `CriticalFinalizerObject`, CLR will run critical finalizers after it has finished running noncritical ones.

`SafeHandle` Is critical. 
Wrapped handle will still be valid when your finalizer runs. 
**Finalization useful only for stuff outside of CLR control**. For the rest `IDisposable`.

A destructor is a member that implements the actions required to destruct an instance of a class. 
Destructors **cannot have parameters**, they **cannot have accessibility modifiers**, and they **cannot be invoked explicitly**. 
The destructor for an instance is _invoked automatically during garbage collection_. 
The garbage collector is allowed wide latitude in deciding when to collect objects and run destructors. 
Specifically, the _timing of destructor invocations is not deterministic_, and destructors may be executed on any thread. 
For these and other reasons, classes should implement destructors only when no other solutions are feasible.

> Destructors are sometimes called “finalizers.” 
This name also appears in the garbage collector API—for example, `GC.WaitForPendingFinalizers`. 
The using statement provides a better approach to object destruction. (VLADIMIR RESHETNIKOV)



### dispose pattern

````csharp
    /// <summary> 
    /// Flag: Has Dispose already been called?  
    /// </summary> 
    bool disposed = false; 

    /// <summary> 
    /// https://msdn.microsoft.com/en-us/library/b1yfkh5e%28v=vs.110%29.aspx 
    /// </summary> 
    public void Dispose() 
    { 
        Dispose(true); 
        GC.SuppressFinalize(this); 
    } 

   //https://msdn.microsoft.com/en-us/library/fs2xkftw%28v=vs.110%29.aspx 
    protected override void Dispose(bool disposing) 
    { 
        if (disposed) 
            return; 

        DisposeUnmanaged(); 

        if (disposing) 
        { 
            DisposeManaged(); 
        }  

        disposed = true; 
    }

/// <summary> 
/// A block that frees unmanaged resources.  
/// This block executes regardless of the value of the disposing parameter. 
/// </summary> 
private void DisposeUnmanaged();

/// <summary> 
/// A conditional block that frees managed resources.  
/// This block executes if the value of disposing is true.  
/// The managed resources that it frees can include: 
/// 1) Managed objects that implement IDisposable. 
/// The conditional block can be used to call their Dispose implementation.  
/// If you have used a safe handle to wrap your unmanaged resource,  
/// you should call the SafeHandle.Dispose(Boolean) implementation here.  
/// 2) Managed objects that consume large amounts of memory or consume scarce resources. 
/// Freeing these objects explicitly in the Dispose method releases them faster  
/// than if they were reclaimed non-deterministically by the garbage collector.  
/// </summary> 
    private void DisposeManaged();
````


[<<](../csdotnet.md) 
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 