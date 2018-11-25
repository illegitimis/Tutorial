# Interfaces

```cs
public interface IComparable {int  CompareTo(object obj );} 
public interface IComparable<in T> { int CompareTo(	T other ); }

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

[<<](../csdotnet.md) | [home](../../README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki)