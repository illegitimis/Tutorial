---
title: xUnit
layout: default
nav_order: 2
parent: Testing
last_modified_date: 2026-04-06 00:00:00 +0000
---

# xUnit

> `xUnit.net` is a free, open source, community-focused unit testing tool for .NET.

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
- Creating strongly typed xUnit theory test data with `TheoryData` [16]
- `TypedClassData` Typed Class Data Attribute for xUnit Test Framework [17]

## Deadlock When Using Parallelization and Blocking on Async Code

VS runner hangs on Run All [#611](https://github.com/xunit/xunit/issues/611)

```csharp
  public static object ApiVversionControllerNameGet(this IGeneratedAPI operations, string version) { 
    return operations.ApiVversionGetAsync(version).GetAwaiter().GetResult(); 
  }
```

_Resolution_ was to:

> **update test runner related packages** in the HLD template  
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

> [Configure xUnit](https://xunit.github.io/docs/configuring-with-xml.html) to **not** participate in parallelization with other assemblies. \
Tests **in the same test collection** will be run **sequentially against each other**, but tests **in different test collections** will be run **in parallel** against each other.

All parallelization within this test assembly is disabled. [18]

```xml
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

## About xUnit.net

`xUnit.net` is a free, open-source, community-focused unit testing tool for the .NET Framework. Written by the original inventor of `NUnit` v2, `xUnit.net` is the latest technology for unit testing C#, F#, VB.NET, and other .NET languages. `xUnit.net` works with `ReSharper`, `CodeRush`, `TestDriven.NET`, and `Xamarin` [19] [23].

## What's New in v3

What's New in v3 [24] \
`xUnit.net` v3 introduces major architectural changes including built-in support for the **Microsoft Testing Platform** (MTP), improved parallelization, and a new extensibility model. Key changes include:

- Native support for `Microsoft.Testing.Platform` as an alternative to `VSTest` [20]
- `TheoryData<T>` for type-safe theory data [16]
- Built-in **Roslyn analyzers** for common mistakes and best practices [21]
- Handle cancellation via `CancellationToken` in test methods [22]

## Roslyn Analyzer Rules

`xUnit.net` ships with `xunit.analyzers` that provide compile-time checks for common testing mistakes. Rules cover proper use of `Assert` methods, theory data compatibility, test class lifecycle, and collection fixtures [21].

## Theory

### TheoryData{T} Type Safety

Typesafety in xUnit with `TheoryData{T}` [27] \
`TheoryData<T>` provides a strongly typed alternative to `object[]` for theory data. Instead of relying on `MemberData` returning `IEnumerable<object[]>`, use `TheoryData<T1, T2>` to get compile-time checking of parameter types [16].

### Mixing Theory Data

Mixing theory data mechanisms, input and expected data [28] \
Theory data sources can be combined: `InlineData` for simple cases, `MemberData` for shared data sets, and `ClassData` for reusable data across test classes [11] [12].

### Clean Test Cases

Create clean test cases in xUnit with `TheoryData` [29] \
Keep theory test cases focused and self-documenting. Each `InlineData` entry should represent a distinct scenario with a clear expected outcome. Prefer `TheoryData<T>` with descriptive property names over raw `object[]` arrays [16].

## Custom Theory Data Serialization

Custom Theory Data Serialization [25] \
Custom theory data types that do not implement `IXunitSerializable` will not display correctly in test explorers. Implement custom serialization for complex types used in theory data to ensure test names are meaningful and test cases are individually identifiable.

## Code Coverage With MTP

Code Coverage with MTP [26] \
**Microsoft Testing Platform** enables integrated code coverage collection without external tooling. Use the `--collect "Code Coverage"` flag with `dotnet test` to generate coverage reports directly through MTP [20].

## Microsoft Testing Platform (v3)

v3 introduces first-class support for `Microsoft.Testing.Platform` (MTP) as an alternative runner to `VSTest`. MTP provides faster test execution, better diagnostics, and a more extensible architecture. Configure via `xunit.runner.json` or MSBuild properties [20].

## Miscellaneous

- Unit testing C# with `dotnet test` and `xUnit` [3] mslearn
- Handle cancellation in tests with `xUnit.net` v3 [30]: test methods can accept a `CancellationToken` parameter that signals when a test run is being cancelled, allowing graceful cleanup [22]

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
[16]: https://andrewlock.net/creating-strongly-typed-xunit-theory-test-data-with-theorydata/
[17]: https://github.com/ielcoro/xunitTypedClassData
[18]: https://xunit.github.io/docs/configuring-with-xml.html
[19]: https://xunit.net/#about
[20]: https://xunit.net/docs/getting-started/v3/microsoft-testing-platform
[21]: https://xunit.net/xunit.analyzers/rules/
[22]: https://xunit.net/docs/cancellation
[23]: https://xunit.net/?tabs=cs
[24]: https://xunit.net/docs/getting-started/v3/whats-new
[25]: https://xunit.net/docs/getting-started/v3/custom-serialization
[26]: https://xunit.net/docs/getting-started/v3/code-coverage-with-mtp
[27]: https://steven-giesel.com/blogPost/a8aa3385-8829-444a-b269-7ecb38aeaf2f
[28]: https://stackoverflow.com/questions/55298358/xunit-mixing-theory-data-mechanisms-input-and-expected-data
[29]: https://daninacan.com/create-clean-test-cases-in-xunit-with-theorydata/
[30]: https://anthonysimmon.com/xunit-cancellationtoken-support/

[<](./index.md) | [<<](/index.md)
