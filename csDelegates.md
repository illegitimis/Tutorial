**Delegates**
[![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](csDelegates.md)

# Multicast
Derive from a base type called `MulticastDelegate`. 
As the name suggests, this means delegates can refer to more than one method. 
The multicast feature is available through the `Delegate` class’s static `Combine` method.
```cs    
    public static Delegate Combine(Delegate a,Delegate b)
    public static Delegate Remove(Delegate source, Delegate value)
```
Or use addition and subtraction operators, delegate combine=add, remove=subtract.

> From <https://gist.github.com/illegitimis/ed2aae068f24835776a57f99a9792077>

## Invocation

Although delegates are special types with runtime-generated code, 
there is ultimately nothing magical about invoking a delegate. 
The call happens on the _same thread_, and _exceptions propagate_ 
through methods that were invoked via a delegate in exactly the same way as they would if the method were invoked directly. 
Invoking a delegate with a single target method works as though your code had called the target method in the conventional way. 
**Invoking a multicast delegate is just like calling each of its target methods in turn**.
```cs
    // Invoking each delegate individually
    foreach (Predicate<int> p in userCallbacks.GetInvocationList()) 
    
    // Dynamically invokes (late-bound) the method represented by the current delegate
    public object DynamicInvoke(params object[] args ) 
```

# Construction
It’s only necessary in cases where the compiler cannot infer the delegate type. 

## Implicit delegate construction
```cs
// When code refers to a method by name like this, 
// the name is technically called a method group, 
// because multiple overloads may exist for a single name.
Predicate<int> p = IsGreaterThanZero;
// Delegates to static methods in another class
Predicate<int> p2 = Comparisons.IsLessThanZero;
```

## Implicit instance delegate
```cs
// refer to an instance method by name from a context in which that  method is in scope

    public class ThresholdComparer {
        public int Threshold { get; set; }
        public bool IsGreaterThan(int value) { return value > Threshold; }
        public Predicate<int> GetIsGreaterThanPredicate() { return IsGreaterThan; }
    }
```
## Explicit instance delegate
```cs
// can take any expression that evaluates to an object reference, and then just append .MethodName

    var zeroThreshold = new ThresholdComparer { Threshold = 0 };
    Predicate<int> greaterThanZero = zeroThreshold.IsGreaterThan;
```
## CreateDelegate
do not necessarily know which method or object you will use until runtime / many overloads
There are also overloads that accept the reflection API’s _MethodInfo_ object to identify the method instead of a string.
```cs
    var greaterThanZero = (Predicate<int>) Delegate.CreateDelegate(typeof(Predicate<int>), zeroThreshold, "IsGreaterThan");
```

# Conversion
## Delegate conversion and contra variance
The type parameters for the function’s parameters are all contravariant. [gist](https://gist.github.com/illegitimis/0b352a8ea439cd0135123697575217b8)

## Illegal delegate conversion
```cs
    Predicate<string> pred = IsLongString;
    Func<string, bool> f = pred; // Will fail with compiler error
```
The lack of type compatibility between ‘compatible’ delegate types may seem odd, 
but structurally identical delegate types don’t necessarily have the same semantics.

## anonymous function 
as an alternative name for an inline method with a non-void return type
an anonymous method is an inline method defined with the `delegate` keyboard
```cs
    public static int GetIndexOfFirstNonEmptyBin(int[] bins) {
        return Array.FindIndex( bins, delegate (int value) { return value > 0; } ); }
```
## lambda expression
other form of inline method is called a lambda expression
```cs
    return Array.FindIndex( bins, value => value > 0 );
```

# Framework
```cs
public delegate bool Predicate<in T>(T obj);
```

The angle brackets indicate that this is a generic type with a single _contravariant_ type argument T, and the
method signature has a single parameter of that type. You can use the new keyword to create a delegate, it needs a method with a bool return type.

```cs
public delegate void Action<in T1, in T2 >(T1 arg1, T2 arg2);

public delegate TResult Func<in T1, in T2, out TResult>(T1 arg1, T2 arg2);
```
