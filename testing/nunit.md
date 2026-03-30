---
title: NUnit
layout: default
nav_order: 1
parent: Testing
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# NUnit

`NUnit` uses a constraint model of assertions.
The logic necessary to carry out each assertion is embedded in the constraint object passed as the second parameter to that method.

- Constraint model [1]
- Constraints by category [2]
- Install [3]
- Visual Studio Test Generator [4]
- Visual Studio Test Adapter [5]

| NUnit | Assert.That |
|:---:|:---:|
| object **type** and properties | `Is.TypeOf<T>()`, `Is.InstanceOf<T>()`, `Has.Property("PropertyName")` |
| **exceptions** | Throws.Exception `Throws.TypeOf<TException>()` .With.Matches<TEx>(predicate) |
| strings | Is.EqualTo("expected") `Is.EqualTo("eXpeCTed").IgnoreCase` Is.Not.EqualTo("notExpected") |
| Numerical values | Is.EqualTo(int) Is.EqualTo(float).Within(tolerance) `Is.EqualTo(val).Within(p).Percent` Is.Positive / Is.Negative / Is.NaN |
| **Date**Time | Is.EqualTo(dt).Within(ts)  `Is.EqualTo(dt).Within(v).Milliseconds` |
| Ranges | Is.GreaterThan(v) / Is.LessThan(v)  Is.GreaterThanOrEqualTo(v)  Is.InRange(lo,hi) |
| Collections | Is.All.Empty Contains.Item(item) Has.Some.ContainsSubstring("sub_str") Has.Exactly(m).EndsWith("suffix") Is.Unique Has.None.EqualTo(val) Is.EquivalentTo(actualCollection) Is.Ordered |
| References | Is.SameAs Is.Not.SameAs |
| Nulls & booleans | `Is.Not.Empty`, `Is.Null`, `Is.True` |

## Official

Unit testing C# with `NUnit` and .NET Core [6] \
`Explicit` attribute [7] \
How to enable Trace and Debug output [8] \
**Classic** assertion model [9] \
`CollectionEquivalentConstraint` [10] \
`CollectionContainsConstraint` [11] \
Migration guidance to v4 [12] \
`SetUpFixture` [13] \
`Ignore` attribute (v2) [14]

## Data-Driven Tests

`NUnit` _parameterized tests_ tutorial with examples [15].

- `TestCase` — constant argument values
- `TestCaseSource` — static method returning `IEnumerable<TestCaseData>`
- `ValueSourceAttribute` — Cartesian product of individual values
- Test class constructor with parameters via `TestFixture` arguments
- Pass `ExpectedResult` to `TestCase`

Data-driven tests with `NUnit` [16] \
Dynamic test cases spec [17] \
**Template-Based Test Naming** [18] \
`TestCaseData` returns [19]

## Samples

> `[SetUpFixture] AND path:/^*.cs$/ AND nunit`

Global setup of `IServiceProvider` [20] \
Create database for _integration tests_ [21]

## default template

```csproj
 <ItemGroup>
    <PackageReference Include="coverlet.collector" Version="6.0.2" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.12.0" />
    <PackageReference Include="NUnit" Version="4.2.2" />
    <PackageReference Include="NUnit.Analyzers" Version="4.4.0" />
    <PackageReference Include="NUnit3TestAdapter" Version="4.6.0" />
  </ItemGroup>

  <ItemGroup>
    <Using Include="NUnit.Framework" />
  </ItemGroup>
```

[1]: https://github.com/nunit/docs/wiki/Constraint-Model
[2]: https://github.com/nunit/docs/wiki/Constraints#constraints-by-category
[3]: https://github.com/nunit/docs/wiki/Installation
[4]: https://github.com/nunit/docs/wiki/Visual-Studio-Test-Generator
[5]: https://github.com/nunit/docs/wiki/Visual-Studio-Test-Adapter
[6]: https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-csharp-with-nunit
[7]: https://docs.nunit.org/articles/nunit/writing-tests/attributes/explicit.html
[8]: https://docs.nunit.org/articles/nunit/technical-notes/usage/Trace-and-Debug-Output.html
[9]: https://docs.nunit.org/articles/nunit/writing-tests/assertions/assertion-models/classic.html
[10]: https://docs.nunit.org/articles/nunit/writing-tests/constraints/CollectionEquivalentConstraint.html
[11]: https://docs.nunit.org/articles/nunit/writing-tests/constraints/CollectionContainsConstraint.html
[12]: https://docs.nunit.org/articles/nunit/release-notes/Nunit4.0-MigrationGuide.html
[13]: https://docs.nunit.org/articles/nunit/writing-tests/attributes/setupfixture.html
[14]: https://nunit.org/nunitv2/docs/2.6.4/ignore.html
[15]: https://www.lambdatest.com/blog/nunit-parameterized-test-examples/
[16]: https://gigi.nullneuron.net/gigilabs/data-driven-tests-with-nunit/
[17]: https://docs.nunit.org/articles/nunit/technical-notes/nunit-internals/specs/Dynamic-Test-Cases-Spec.html
[18]: https://docs.nunit.org/articles/nunit/running-tests/Template-Based-Test-Naming.html
[19]: https://docs.nunit.org/articles/nunit/writing-tests/TestCaseData.html
[20]: https://github.com/Rick-van-Dam/TestExamplesDotnet/blob/master/Examples/Api/MsSql/Api.MsSql.Nunit/GlobalSetup.cs
[21]: https://github.com/busterwood/Mapper/blob/master/IntegrationTest/CreateDb.cs

[<](./index.md) | [<<](/index.md)
