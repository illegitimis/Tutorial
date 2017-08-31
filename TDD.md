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
- **FluentAssertion** [docs](http://fluentassertions.com/documentation.html#basic-assertions)


[<<](README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki/)
