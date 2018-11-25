# NUnit

Constraint model of assertions.
The logic necessary to carry out each assertion is embedded in the constraint object passed as the second parameter to that method.

- [Constraint model](https://github.com/nunit/docs/wiki/Constraint-Model)
- [Constraints by category](https://github.com/nunit/docs/wiki/Constraints#constraints-by-category)
- [Install](https://github.com/nunit/docs/wiki/Installation)
- [Visual Studio Test Generator](https://github.com/nunit/docs/wiki/Visual-Studio-Test-Generator)
- [Visual Studio Test Adapter](https://github.com/nunit/docs/wiki/Visual-Studio-Test-Adapter)

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

[<<](../tdd.md) | [home](../../README.md)