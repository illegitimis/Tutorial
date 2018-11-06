# TDD

## Resources

- 2010, Freeman & Pryce, **Growing Object-Oriented Software**, _Guided by Tests_
  - [![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!As0cxZAk26SzjMBnGhtcOwBkCZwT5Q)
  - [amazon](https://www.amazon.com/Growing-Object-Oriented-Software-Guided-Tests/dp/0321503627/ref=pd_sim_14_44?_encoding=UTF8&pd_rd_i=0321503627&pd_rd_r=7T6NVGV6TN7BKEPAGYFA&pd_rd_w=6auH8&pd_rd_wg=Fmfw0&psc=1&refRID=7T6NVGV6TN7BKEPAGYFA)
- 2002, **Test Driven Development By Example**, _Kent Beck_, Three Rivers Institute
  - [![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!AnIyfO51kH7NlVZNro7bHgrYuh3a)
- mocking with moq
  - samples [![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/f/s!AnIyfO51kH7Nk2-MzT3eCed90XDe)
  - slides [![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!AnIyfO51kH7Nk26pXdkFOO_LSPV-)

## Properties of a good unit test

| properties of a | good unit test |
|:--:|:---:|
| atomic | should target a small piece of functionality,  hard to maintain otherwise |
| deterministic | pass or fail,  never inconclusive |
| repeatable | consistent with dependent objects changing,  time passing and between runs |
| order independent  & isolated | should not run be forced to run in a specific order, other tests or dependencies should not prevent test passing |
| fast | order of ms |
| easy to setup | should not be cumbersome |

## Pages

- [NUnit](tdd/nunit.md)
- [xunit](tdd/xunit.md)
- **FluentAssertions** [docs](http://fluentassertions.com/documentation.html#basic-assertions)
- [Integration testing in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/testing/integration-testing) with `Microsoft.AspNetCore.TestHost`
- EF in memory providers
  - [DbSetExtensionMethods](https://gist.github.com/illegitimis/5f88a89a90781b2228b42225ff9ebce5)
  - [InMemoryProviders](https://gist.github.com/illegitimis/2e53194506faf6060b7a5ecc7a8400d7)
  - EFCore [in memory provider](https://docs.microsoft.com/en-us/ef/core/miscellaneous/testing/in-memory). The InMemory provider is missing from EF though.
  - How to mock a db context / set?

    ```cs
    var mediatorHandler = Substitute.For<IMediatorHandler>();
    MyContext context = Substitute.For<MyContext>(mediatorHandler);
    var stubbedEntities = new List<TEntityIAmInterestedIn> { /* do populate here */ };
    var set = Substitute.For<
      DbSet<TEntityIAmInterestedIn>,
      IQueryable<TEntityIAmInterestedIn>,
      IDbAsyncEnumerable<TEntityIAmInterestedIn>>()
      .Initialize(stubbedEntities.AsQueryable());
    context.Set<TEntityIAmInterestedIn>().Returns(set);
    // further on, you might test your EF repository queries using your custom configured data stubs.
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

[<<](../README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki/)
