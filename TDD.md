# TDD

## Resources
+ 2010, Freeman & Pryce, **Growing Object-Oriented Software**, _Guided by Tests_, 
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!As0cxZAk26SzjMBnGhtcOwBkCZwT5Q),
[amazon](https://www.amazon.com/Growing-Object-Oriented-Software-Guided-Tests/dp/0321503627/ref=pd_sim_14_44?_encoding=UTF8&pd_rd_i=0321503627&pd_rd_r=7T6NVGV6TN7BKEPAGYFA&pd_rd_w=6auH8&pd_rd_wg=Fmfw0&psc=1&refRID=7T6NVGV6TN7BKEPAGYFA)
+ 2002, **Test Driven Development By Example**, _Kent Beck_, Three Rivers Institute  
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!AnIyfO51kH7NlVZNro7bHgrYuh3a)
+ mocking with moq samples, 
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/f/s!AnIyfO51kH7Nk2-MzT3eCed90XDe)
+ mocking with moq slides, 
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!AnIyfO51kH7Nk26pXdkFOO_LSPV-)

## Properties of a good unit test
|        properties of a        |                                                  good unit test                                                  |
|:-----------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| atomic                        |                     should target a small piece of functionality,  hard to maintain otherwise                    |
| deterministic                 |                                         pass or fail,  never inconclusive                                        |
| repeatable                    |                    consistent with dependent objects changing,  time passing and between runs                    |
| order independent  & isolated | should not run be forced to run in a specific order, other tests or dependencies should not prevent test passing |
|              fast             |                                                    order of ms                                                   |
|         easy to setup         |                                             should not be cumbersome                                             |

## NUnit

Constraint model of assertions. 
The logic necessary to carry out each assertion is embedded in the constraint object passed as the second parameter to that method.

- [Constraint model](https://github.com/nunit/docs/wiki/Constraint-Model)
- [Constraints by category](https://github.com/nunit/docs/wiki/Constraints#constraints-by-category)
- [Install](https://github.com/nunit/docs/wiki/Installation)
- [Visual Studio Test Generator](https://github.com/nunit/docs/wiki/Visual-Studio-Test-Generator)
- [Visual Studio Test Adapter](https://github.com/nunit/docs/wiki/Visual-Studio-Test-Adapter)


| NUnit | Assert.That |
|:--------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| object type and properties | `Is.TypeOf<T>()`, `Is.InstanceOf<T>()`, `Has.Property("PropertyName")` |
| exceptions | Throws.Exception Throws.TypeOf<TException>() .With.Matches<TEx>(predicate) |
| strings | Is.EqualTo("expected") Is.EqualTo("eXpeCTed").IgnoreCase Is.Not.EqualTo("notExpected") |
| Numerical values | Is.EqualTo(int) Is.EqualTo(float).Within(tolerance) Is.EqualTo(val).Within(p).Percent Is.Positive / Is.Negative / Is.NaN |
| DateTime | Is.EqualTo(dt).Within(ts)  Is.EqualTo(dt).Within(v).Milliseconds |
| Ranges | Is.GreaterThan(v) / Is.LessThan(v)  Is.GreaterThanOrEqualTo(v)  Is.InRange(lo,hi) |
| Collections | Is.All.Empty Contains.Item(item) Has.Some.ContainsSubstring("sub_str") Has.Exactly(m).EndsWith("suffix") Is.Unique Has.None.EqualTo(val) Is.EquivalentTo(actualCollection) Is.Ordered |
| References | Is.SameAs Is.Not.SameAs |
| Nulls & booleans | `Is.Not.Empty`, `Is.Null`, `Is.True` |

## xunit

- [Comparing xUnit.net to other frameworks](https://xunit.github.io/docs/comparisons.html)
- **FluentAssertions** [docs](http://fluentassertions.com/documentation.html#basic-assertions)
- [Using xUnit with ASP.NET Core ](http://gunnarpeipman.com/2016/10/aspnet-core-xunit/), 2016.10
- [Unit testing C# in .NET Core using dotnet test and xUnit](https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test), 2017.09
- [Getting started with xUnit.net (.NET Core / ASP.NET Core)](http://xunit.github.io/docs/getting-started-dotnet-core.html)
- [End to end testing angular js apps with XUnit and Protractor.Net](https://dotnetthoughts.net/end-to-end-testing-angularjs-apps-with-xunit-protractor-net/), 2016.04
- [Assert.ThrowsAsync](https://github.com/nunit/docs/wiki/Assert.ThrowsAsync)
+ [Introduction to integration testing with xUnit and TestServer in ASP.NET Core](https://andrewlock.net/introduction-to-integration-testing-with-xunit-and-testserver-in-asp-net-core/)
+ [Integration testing in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/testing/integration-testing) with `Microsoft.AspNetCore.TestHost`
+ `XunitException` Random **Warning** when running a test batch `System.Runtime.Serialization.SerializationException`: Type 'Xunit.Sdk.XunitException' in Assembly 'xunit.assert, Version=2.2.0.3545, Culture=neutral, PublicKeyToken=8d05b1bb7a6fdb6c' is not marked as **serializable**.
+ [Deadlock when using parallelization and blocking on async code](https://github.com/xunit/xunit/issues/611)
  ```csharp
   public static object ApiVversionControllerNameGet(this IGeneratedAPI operations, string version) { 
     return operations.ApiVversionGetAsync(version).GetAwaiter().GetResult(); 
   }
  ```
+ [tracing](https://github.com/Azure/autorest/blob/master/docs/client/tracing.md)
+ [test runner hangs on run all](https://github.com/xunit/xunit/issues/611)

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


## dotnet

Microsoft (R) Test Execution Command Line Tool
[VS 2017 free coverage](https://stackoverflow.com/questions/32369664/visual-studio-has-code-coverage-for-unit-tests)
[vs 2017 integrated coverage](https://msdn.microsoft.com/en-us/library/dd537628.aspx)
```shell
# run tests for framework and platform
dotnet test --no-build -v diag -o ./bin/x86/Release/
dotnet test --framework netcoreapp1.1 --runtime win10-x86
# new test project with enable pack
dotnet new xunit -p -lang c#
# list available project types
dotnet new -all 
# An open source code coverage tool (branch and sequence point) for all .NET Frameworks 2 and above (including Silverlight). 
# Also capable of handling 32 and 64 bit processes. Use ReportGenerator 1.9 for best viewing results (also available via Nuget).
dotnet add package OpenCover --version 4.6.519
```


[<<](README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki/)
