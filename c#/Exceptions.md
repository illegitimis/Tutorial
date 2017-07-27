# Exceptions

1) Call stack context [From SO](http://stackoverflow.com/questions/5152265/what-can-lead-throw-to-reset-a-callstack-im-using-throw-not-throw-ex#5154318). 
In short, **throw usually preserves the stack trace** of the original thrown exception, but _only if the exception didn't occur in the current stack frame_ (i.e. method). 

````chsarp
    //To preserve the full call stack information, you need to use the following method: 
    private static void PreserveStackTrace(Exception exception) { 
      System.Reflection.MethodInfo preserveStackTrace = typeof(Exception)
        .GetMethod("InternalPreserveStackTrace",  
        System.Reflection.BindingFlags.Instance | .Reflection.BindingFlags.NonPublic); 
      preserveStackTrace.Invoke(exception, null);
    }
````
**ExceptionCallStackTest.cs** [gist](https://gist.github.com/illegitimis/d65b01df24df6df90d4edced289820c9) | 
[MSTest raw file](https://gist.githubusercontent.com/illegitimis/d65b01df24df6df90d4edced289820c9/raw/6265c9c1b3f7e4861adc4ccbde11ef3de600c337/ExceptionCallStackTest.cs) 

2) How to decorate an exception: Use the `public virtual IDictionary Data { get; }` property. 
Gets a collection of key/value pairs that provide additional user-defined information about the  exception. 
[msdn](https://msdn.microsoft.com/en-us/library/system.exception.data%28v=vs.110%29.aspx?f=255&MSPPError=-2147217396)




[<<](../csdotnet.md) 
|
[home](https://github.com/illegitimis/Tutorial) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 