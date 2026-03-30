---
title: Interfaces
layout: default
nav_order: 8
parent: "C# Language"
grand_parent: .NET
last_modified_date: 2026-03-29 21:15:03 +00:00
---

# Interfaces

```cs
public interface IComparable {int  CompareTo(object obj );} 
public interface IComparable<in T> { int CompareTo( T other ); }

public interface IComparer { int Compare( object x, object y); } 
public interface IComparer<in T> { int Compare( T x, T y); }

// https://msdn.microsoft.com/en-us/library/s793z9y2(v=vs.110).aspx
public interface IEnumerable<out T> : IEnumerable
{ 
  IEnumerator<T> GetEnumerator();
}  

// https://msdn.microsoft.com/en-us/library/78dfe2yb(v=vs.110).aspx
public interface IEnumerator<out T> : IDisposable, IEnumerator  {  
  bool MoveNext();  
  T Current { get; }
}
```

[<](./index.md) | [<<](/index.md)
