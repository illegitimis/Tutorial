# Immutable

+ _immutable_, meaning that it sets all of its fields during initialization and then never modifies them again 
compiler will generate an error if you attempt to modify that field from outside of a constructor.
+ `ToLookup` converts an `IEnumerable<T>` to a `Lookup<Key, Element>` type.  
`Lookup` is like a dictionary, but where a `Dictionary` uses a single key value, Lookup maps keys to a collection of values.  
Lookups have no public constructor and are _immutable_.  
You cannot add or remove elements or keys after they are created. 
+ Since value types should normally be immutable, a requirement for mutability is usually a good sign that you want a class rather than a struct
+  readonly protects the location of the field from being changed outside the type’s constructor, but does not protect the value at that location. 
+ Immutable types do not have any publicly exposed setters, such as int, double, or String.
+ All simple types are immutable. Any structs you create should also be immutable. 
+ ERIC LIPPERT 
> This is yet another reason why value types should be immutable: 
If a change is impossible, then the fact that changes made to an unboxed struct are not reflected in the boxed struct becomes irrelevant. 
Rather than dealing with the unexpected and confusing semantics, avoid them altogether.
```cs
//compile error
string s = "Hello"; s[0] = 'c'; 
```
+ The Regex class is the heart of the FCL regular expression support.  
Used both as an object instance and a static type, the Regex class represents an immutable, compiled instance of a regular expression that can be applied to a string via a matching process. 
Internally, the regular expression is stored as either a sequence of internal regular expression bytecodes that are interpreted at match time or as compiled MSIL opcodes that are JIT-compiled by the CLR at runtime.  
This allows you to make a tradeoff between worsened regular expression startup time and memory utilization versus higher raw match performance at runtime.


