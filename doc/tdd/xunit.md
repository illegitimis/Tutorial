# xunit

> xUnit.net is a free, open source, community-focused unit testing tool for .NET.

- documentation @github [9]
- Comparing xUnit.net to other frameworks [1]
- Using xUnit with ASP.NET Core, [2] blog 2016
- Unit testing C# in .NET Core using dotnet test and xUnit [3] mslearn
- Getting Started with xUnit.net \
v3 .NET or .NET Framework with the .NET SDK command line [6] \
v2 .NET Core with Visual Studio [5] \
v2 .NET Framework with Visual Studio [4].
- End to end testing angular js apps with XUnit and Protractor.Net [7] _2016_
- `Assert.ThrowsAsync` [10]
- Creating parameterised tests in xUnit with `InlineData`, `ClassData` and `MemberData` [11], _2017_
- xUnit Theory: Working With `InlineData`, `MemberData`, `ClassData` [12], _2017_
- Introduction to integration testing with xUnit and TestServer in ASP.NET Core [13], _2016_
- Capturing Output [14]
- Shared Context between Tests [15]

## Deadlock when using parallelization and blocking on async code

VS runner hangs on Run All [#611](https://github.com/xunit/xunit/issues/611)

```csharp
  public static object ApiVversionControllerNameGet(this IGeneratedAPI operations, string version) { 
    return operations.ApiVversionGetAsync(version).GetAwaiter().GetResult(); 
  }
```

_Resolution_ was to: 

> **update test runner related packages** in the HLD template  

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

> [Configure xUnit](https://xunit.github.io/docs/configuring-with-xml.html) to **not** participate in parallelization with other assemblies. \
Tests **in the same test collection** will be run **sequentially against each other**, but tests **in different test collections** will be run **in parallel** against each other.

All parallelization within this test assembly is disabled.

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

[1]: https://xunit.net/docs/comparisons
[2]: http://gunnarpeipman.com/2016/10/aspnet-core-xunit/
[3]: https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test
[4]: https://xunit.net/docs/getting-started/v2/netfx/visual-studio
[5]: https://xunit.net/docs/getting-started/v2/netcore/visual-studio
[6]: https://xunit.net/docs/getting-started/v3/cmdline
[7]: https://dotnetthoughts.net/end-to-end-testing-angularjs-apps-with-xunit-protractor-net/
[9]: https://github.com/xunit/xunit/tree/gh-pages
[10]: https://github.com/xunit/xunit/blob/rel/v3-2.0.0/src/xunit.v3.assert.tests/Asserts/ExceptionAssertsTests.cs
[11]: https://andrewlock.net/creating-parameterised-tests-in-xunit-with-inlinedata-classdata-and-memberdata/
[12]: https://hamidmosalla.com/2017/02/25/xunit-theory-working-with-inlinedata-memberdata-classdata/
[13]: https://andrewlock.net/introduction-to-integration-testing-with-xunit-and-testserver-in-asp-net-core/
[14]: https://xunit.net/docs/capturing-output
[15]: https://xunit.net/docs/shared-context