---
title: Testing
layout: minimal
nav_order: 7
has_children: true
last_modified_date: 2026-04-06 00:00:00 +0000
---

# Testing

> Unit testing frameworks, assertion libraries, mocking, and test-driven development methodology.

## Pages

- [NUnit](./nunit.md) — `NUnit` constraint-based assertion model and test framework for .NET
- [xUnit](./xunit.md) — `xUnit.net` free, open-source, community-focused unit testing tool for .NET
- [MSTest](./mstest.md) — `MSTest` unit testing framework for Visual Studio

## TDD and Supporting Tools

*Test-Driven Development* methodology: write tests first, then implement to make them pass.

Key properties of a good unit test: atomic, deterministic, repeatable, order-independent, fast, and easy to set up.

**Recommended reading:**

- *Growing Object-Oriented Software, Guided by Tests* — Freeman & Pryce (2010)
- *Test Driven Development By Example* — Kent Beck (2002)

**Mocking and assertion libraries:**

- `MOQ` (Moq) — mocking framework for .NET using lambda-based setup and verification
- **FluentAssertions** — fluent assertion library for expressive, readable test assertions
- `Microsoft.AspNetCore.TestHost` — integration testing host for ASP.NET Core applications
- `OpenCover` — open-source code coverage tool for all .NET frameworks

## FakeItEasy

`FakeItEasy` — the easy mocking library for .NET [1].

- Throwing exceptions [2]
- `MustHaveHappened` with `A<T>.That.Contains` for collection argument matching [3]

[1]: https://github.com/FakeItEasy/FakeItEasy
[2]: https://fakeiteasy.github.io/docs/8.3.0/throwing-exceptions/
[3]: https://stackoverflow.com/questions/47860005/how-to-assert-musthavehappendcollection-that-containsobject-in-fake-it-easy

[<<](/index.md)
