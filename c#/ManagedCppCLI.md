# Managed C++, C++/CLI 

- Microsoft’s first set of .NET extensions for C++ attempted to resemble ordinary C++ more closely.   
In the end, it turned out to be less confusing to use a distinct syntax for something that is quite different from ordinary C++, 
so they  deprecated the first system (Managed C++) in favour of the newer, more distinctive syntax, which is called C++/CLI.
- C++/CLI is an extension to C++ that is an ECMA standard (ECMA 372). 
The big advantage of C++/CLI is the ability to mix native code with managed code.
- C++/CLI: Formerly known as the Managed Extensions for C++, allows C++ code to be executed on top of the .NET runtime, providing a great tool to deal with interoperability problems.
- C++ code that executes with the CLR is described as managed C++ because data and code is managed by the CLR.  
In CLR programs, the release of memory that you have allocated dynamically for storing data is taken care of automatically, thus eliminating a common source of error in native C++ applications.  
C++ code that executes outside of the CLR is sometimes described by Microsoft as unmanaged C++ because the CLR is not involved in its execution.  
With unmanaged C++ you must take care of all aspects allocating and releasing memory during execution of your program yourself,  
and you also forego the enhanced security provided by the CLR.  
You’ll also see unmanaged C++ referred to as native C++ because it compiles directly to native machine code.
- (multi language development) For example, you can easily sub-class a VB.NET class from C# and then use the resulting class in managed C++
- CLR benefit: GC, protection against uninitialized variables and dangling pointers, array access over its bounds (buffer overrun).
- The advantage of using managed C++ over C# code is that you can call unmanaged C++ classes from managed C++ code without having to resort to COM interop.
- ref keyword to define a managed class. You can create a reference type by defining ref class or ref struct.  
```cpp
ref class MyClass {};
value class MyStruct {};
```
-  Hello world in Managed Extensions for C++ 
```cs
#include "stdafx.h" 
using namespace System; 
int main(array<System::String ^> ^args) 
{ 
  Console::WriteLine(L"Hi from managed C++"); 
  return 0; 
}
```
CHRISTIAN NAGEL 
> C# defines protected internal to limit access to this assembly or classes derived from this class.  
The CLR also allows limiting access to this assembly and classes derived from this class. 
C++/CLI offers this CLR feature with the public private access modifier (or private public—the order is not relevant). 
Realistically, this access modifier is rarely used.
From a destructor, the C# compiler creates code to override the Finalize method of the base class.  
Overriding the Finalize method also means an overhead on object instantiation and keeps the object longer alive until the finalization was run.  
With C++/CLI, the code generated from the destructor implements the IDisposable interface, which has a better fit with deterministic cleanup

- Capability to write unsafe code, allowing manipulation of pointers and so on.  
As the name implies, this kind of code is inherently unsafe with regard to type safety and usually is used only in advanced interoperability scenarios.  
Often, it’s just better to use other languages, such as C++/CLI, for such tasks.
- To import namespaces, C# uses the using keyword.  
C++/CLI is fully based on the C++ syntax with the using namespace statement.
- When using a reference type, a variable needs to be declared, and the object must be allocated on the managed heap. 
When declaring a handle to a reference type, C++/CLI defines the handle **operator ^**, which is somewhat similar to the **C++ pointer * **
The **gcnew** operator allocates the memory on the managed heap.
```cpp
MyClass^ obj = gcnew MyClass();
```
- With C++/CLI, you can allocate
```cpp
MyStruct ms1;                       // a value type on the stack 
MyStruct* pms2 = new MyStruct();    // on the native heap by using the new operator 
MyStruct^ hms3 = gcnew MyStruct();  // on the managed heap by using the gcnew operator
``` 
- If a value type that is passed as a parameter should be changed within a calling method, with C# you can use theparameter modifier ref. 
C++/CLI defines a managed reference **operator %**.  
This operator is similar to the **C++ reference operator &** except that % can be used with managed types and the garbage collector can keep track of these objects in case they are moved within the managed heap. 
```cpp
public ref class ParameterPassing 
{ 
public: 
  int ChangeVal(int% i) 
  { 
    i = 3; 
  } 
};
```
- C++/CLI defines **nullptr** (NULL is valid only for native objects)
- C++/CLI singleton 
```cpp
public ref class Singleton 
{ 
  private: 
    static SomeData^ hData; 

  public: 
    static SomeData^ GetData() 
    { 
      if (hData == nullptr) 
      { 
        hData = gcnew SomeData(); 
      }
      return hData; 
   } 
}; 

// use: 
// SomeData^ d = Singleton::GetData();
```
- The foreach statement makes use of the _interface IEnumerable_. 
foreach doesn ’ t exist with ANSI C++ but is an extension of ANSI C++/CLI. 
With C++/CLI, the _yield_ statement is not available.
```cpp
  array < int > ^ arr = {1, 2, 3}; 
  for each (int i in arr) 
```
- [/clr:safe](https://msdn.microsoft.com/en-us/library/85344whh%28VS.80%29.aspx?f=255&MSPPError=-2147217396) 
verifiable assemblies, guarantee that the code does not violate current security settings. 
C++ interop features are not available. 
Verifiable assemblies cannot contain any unmanaged functions or native data types, even if they are not referenced by the managed code.
Regardless of assembly type, calls made from managed assemblies to native DLLs via P/Invoke will compile, but may fail at runtime depending on security settings.  
- C++/CLI introduces the safe_cast operator that ensures that a cast operation results in verifiable code being generated.
The safe_cast operation is for explicit casts in the CLR environment.
- You _use native code from C#_ through a mechanism known as **platform invoke**.  
Using native code from C++/CLI is known as _It just works_.  
In a managed class, you can use both native and managed code. 
The same is true for a native class. 
To use managed classes as a member within native classes, C++/CLI defines the keyword _gcroot_, which is defined in the header file gcroot.h.  
gcroot wraps a `GCHandle` that keeps track of a CLR object from a native reference.
```cpp
#pragma once 
#include < iostream > // include this header file for cout 
using namespace std; // the iostream header defines the namespace std 
using namespace System; 

public ref class Managed 
{ 
public: 
	void AddNativeToManaged() 
	{ 
	cout < < “Native Code” < < endl; 
	Console::WriteLine(“Managed Code”); 
	} 
}; 
 

public class Native 
{ 
private: 
	gcroot < Managed^ > m_p; 
public: 
	Native() 
	{ 
	m_p = gcnew Managed(); 
	} 

	void AddManagedToNative() 
	{ 
		m_p- > AddNativeToManaged(); 
	}
}; 
```

- **CLS-Compliant Primitive Types**
 
Type | C# | VB | C++/CLI | F# 
---|---|---|---|---
System.Byte | byte | Byte | unsigned char | byte 
System.Int16 | short | Short | short | int16 
System.Int32 | int | Integer | int/long | int/int32 
System.Int64 | long | Long | __int64 | int64 
System.Single | float | Single | Float | single/float32 
System.Double |  double | Double | Double |  double/float 
System.Boolean | bool | Boolean | Bool | bool 
System.Char | char | Char | wchar_t |  char 
System.Decimal | decimal | Decimal | Decimal | decimal 
System.String | string | String | String^ |  string


- **IDisposable Interface Implementation**  
With C++/CLI the interface IDisposable is implemented as well,  
but this is done by the compiler if you just write a destructor 
With C++/CLI, the Dispose() method is invoked by using the delete statement 
** C++/CLI **
```cs
public class Resource : IDisposable 
{ 
  public void Dispose() { 
    // release resource 
  } 
}
```	
** C# **
```cpp
public ref class Resource { 
  public: 
    ~Resource() { 
      // release resource 
    } }; 
```	
- **Using Statement** 
The C# using statement implements an acquire/use/release pattern to release a resource as soon as it is no longer used, even in the case of an exception. 
The compiler creates a try/finally statement and invokes the Dispose method inside the finally. 
C++/CLI has an even more elegant approach to this problem. 
If a reference type is declared locally, the compiler creates a try/finally statement to invoke the Dispose() method at the end of the block. 
** C++/CLI **
```cs
using (Resource r = new Resource()) 
{ 
  r.Foo(); 
}
```	
** C# **
```cpp
{ 
  Resource r; 
  r.Foo(); 
}
```	
- **Override Finalize**
If a class contains native resources that must be freed, the class must override the Finalize() method from the Object class. 
With C#, this is done by writing a destructor. C++/CLI has a special syntax with the ! prefix to define a finalizer. 
Within a finalizer, you cannot dispose contained objects that have a finalizer as well because the order of finalization is not guaranteed. 
That’s why the Dispose pattern defines an additional Dispose() method with a Boolean parameter. 
With C++/CLI, it is not necessary to implement this pattern in the code because this is done by the compiler. 
The C++/CLI destructor implements both Dispose() methods. 
Writing a destructor with C# overrides the Finalize() method of the base class. 
A C++/CLI destructor implements the IDisposable interface. 
** C++/CLI **
```cs
public class Resource : IDisposable { 
    // override Finalize
	~Resource  {  
	  Dispose(false); 
	} 

    protected virtual void Dispose(bool disposing) { 
      if (disposing) { 
	    // dispose embedded members 
	  } 

      // release resources of this class 
	  GC.SuppressFinalize(this); 
    } 

    public void Dispose() { 
	  Dispose(true); 
	} 
} 
```	
** C# **
```cpp
public ref class Resource { 
public: 
  ~Resource() { 
    // implement IDisposable 
    this- > !Resource(); 
  } 
  // override Finalize 
  !Resource() { 
    // release resource 
  } 
};
```


[<<](../csdotnet.md) 
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 