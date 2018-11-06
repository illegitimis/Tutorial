# xunit

- [Comparing xUnit.net to other frameworks](https://xunit.github.io/docs/comparisons.html)
- [Using xUnit with ASP.NET Core ](http://gunnarpeipman.com/2016/10/aspnet-core-xunit/), 2016.10
- [Unit testing C# in .NET Core using dotnet test and xUnit](https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test), 2017.09
- [Getting started with xUnit.net (.NET Core / ASP.NET Core)](http://xunit.github.io/docs/getting-started-dotnet-core.html)
- [End to end testing angular js apps with XUnit and Protractor.Net](https://dotnetthoughts.net/end-to-end-testing-angularjs-apps-with-xunit-protractor-net/), 2016.04
- [Assert.ThrowsAsync](https://github.com/nunit/docs/wiki/Assert.ThrowsAsync)
- [Introduction to integration testing with xUnit and TestServer in ASP.NET Core](https://andrewlock.net/introduction-to-integration-testing-with-xunit-and-testserver-in-asp-net-core/)
- `XunitException` Random **Warning** when running a test batch `System.Runtime.Serialization.SerializationException`: Type 'Xunit.Sdk.XunitException' in Assembly 'xunit.assert, Version=2.2.0.3545, Culture=neutral, PublicKeyToken=8d05b1bb7a6fdb6c' is not marked as **serializable**.
- [Deadlock when using parallelization and blocking on async code](https://github.com/xunit/xunit/issues/611)
  ```csharp
   public static object ApiVversionControllerNameGet(this IGeneratedAPI operations, string version) { 
     return operations.ApiVversionGetAsync(version).GetAwaiter().GetResult(); 
   }
  ```
- [test runner hangs on run all](https://github.com/xunit/xunit/issues/611)

__Resolution__ was to: 

1. **update test runner related packages** in the HLD template  
```xml
  <package id="xunit" version="2.3.1" targetFramework="net462" />
  <package id="xunit.abstractions" version="2.0.1" targetFramework="net462" />
  <package id="xunit.analyzers" version="0.7.0" targetFramework="net462" />
  <package id="xunit.assert" version="2.3.1" targetFramework="net462" />
  <package id="xunit.core" version="2.3.1" targetFramework="net462" />
  <package id="xunit.extensibility.core" version="2.3.1" targetFramework="net462" />
  <package id="xunit.extensibility.execution" version="2.3.1" targetFramework="net462" />
  <package id="xunit.runner.visualstudio" version="2.2.0" targetFramework="net462" developmentDependency="true" />
```
2. [Configure xUnit](https://xunit.github.io/docs/configuring-with-xml.html) to **not** participate in parallelization with other assemblies. Tests **in the same test collection** will be run **sequentially against each other**, but tests **in different test collections** will be run **in parallel** against each other. 
> All parallelization within this test assembly is disabled. 

```xml
  <!--https://xunit.github.io/docs/configuring-with-xml.html-->
  <appSettings>
    <add key="xunit.appDomain" value="ifAvailable" />
    <add key="xunit.diagnosticMessages" value="true" />
    <add key="xunit.methodDisplay" value="classAndMethod" />
    <add key="xunit.parallelizeTestCollections" value="false" />
    <add key="xunit.parallelizeAssembly" value="false" />
    <add key="xunit.preEnumerateTheories" value="true" />
    <add key="xunit.shadowCopy" value="true" />
    <add key="longRunningTestSeconds" value="10" />
  </appSettings>
```
Classes with a sensible number of tests have been isolated into collections, collection is `Xunit.CollectionAttribute`:
```cs
    [Collection("Some Collection")]
    [Trait("Controller", "Controller Name")]
    [Trait("Client", "AutoRest")]
    public class SomeControllerTests {...}
``` 
For a .NET Core project, a xUnit configuration would have been done via a `xunit.runner.json` file in the test project root.
```json
{
  "appDomain": "ifAvailable",
  "diagnosticMessages": true,
  "methodDisplay": "classAndMethod",
  "parallelizeTestCollections": true,
  "internalDiagnosticMessages": true,
  "parallelizeAssembly": true,
  "preEnumerateTheories": true,
  "shadowCopy": true
}
```