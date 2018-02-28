# To do

+ [ASP.NET Core](https://github.com/aspnet/home) The Home repository is the starting point for people to learn about ASP.NET Core. 
+ [NET Core 2.1 Roadmap](https://blogs.msdn.microsoft.com/dotnet/2018/02/02/net-core-2-1-roadmap/) February 2, 2018 by Rich Lander [MSFT] on .NET Blog
+ [Entity Framework Core 2.1 Roadmap](https://blogs.msdn.microsoft.com/dotnet/2018/02/02/entity-framework-core-2-1-roadmap/)
+ [How Well Do You Know C#?](http://www.dotnetcurry.com/csharp/1417/csharp-common-mistakes) Feb 2018
+ [ASP.NET Core 2.1 roadmap](https://blogs.msdn.microsoft.com/webdev/2018/02/02/asp-net-core-2-1-roadmap/) Feb 2018
+ [ASP.NET Core vs Go data ingestion benchmark](https://stefanprodan.com/2016/aspnetcore-vs-golang-data-ingestion-benchmark/)
+ [Middleware Filters in ASP.Net Core](http://www.intstrings.com/ramivemula/articles/middleware-filters-in-asp-net-core/) dec16
+ [Custom ASP.NET Core Middleware Example](https://blogs.msdn.microsoft.com/dotnet/2016/09/19/custom-asp-net-core-middleware-example/) sep16
+ [ASP.NET - Use Custom Middleware to Detect and Fix 404s in ASP.NET Core Apps](https://msdn.microsoft.com/en-us/magazine/mt707525.aspx) jun16
+ [Filters](https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/filters) dec16
+ [Exploring Middleware as MVC Filters in ASP.NET Core 1.1](https://andrewlock.net/exploring-middleware-as-mvc-filters-in-asp-net-core-1-1/)
+ [52 tips & tricks to boost .net performance](https://drive.google.com/file/d/0B_u1rzdqYCnzOUdfS3pFeWN2Nkk/view)
+ [EF Core or micro-ORM?](https://docs.microsoft.com/en-us/dotnet/standard/modern-web-apps-azure-architecture/work-with-data-in-asp-net-core-apps#ef-core-or-micro-orm)
+ [Integration Testing for ASP.NET Core Applications](http://www.dotnetcurry.com/aspnet-core/1420/integration-testing-aspnet-core) Feb18
+ [Using Azure database for PostgreSQL in ASP.NET Core](http://www.dotnetcurry.com/aspnet/1410/aspnet-core-app-postgresql-azure) (with EF Core) Jan18

## Caching

+ [Using Cache in ASP.NET Core 1.0 RC1](https://wildermuth.com/2016/04/14/Using-Cache-in-ASP-NET-Core-1-0-RC1) apr16
+ [Response Caching Middleware in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/performance/caching/middleware#conditions-for-caching) Jan17
+ [Custom response caching in ASP.NET Core (with cache invalidation)](https://www.devtrends.co.uk/blog/custom-response-caching-in-asp.net-core-with-cache-invalidation)
+ [ASP.NET Core: In-Memory Caching](https://social.technet.microsoft.com/wiki/contents/articles/37349.asp-net-core-in-memory-caching.aspx) mar17
+ [ASP.NET Core Response Cache ](http://gunnarpeipman.com/2017/03/aspnet-core-response-cache/) sep17
+ [ASP.NET Monsters #32 - In-Memory Caching with ASP.NET Core](https://www.youtube.com/watch?v=oIvoy5v0WZE) nov16
+ [InMemory Caching in ASP.NET MVC 6](http://www.dotnetcurry.com/aspnet-mvc/1246/inmemory-caching-aspnet-mvc-6-core) jan16
+ [How to use in-memory caching in ASP.Net Core](https://www.infoworld.com/article/3230129/application-development/how-to-use-in-memory-caching-in-aspnet-core.html) oct17
+ [Detect changes with change tokens in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/primitives/change-tokens) oct17

## Authorization
- [ASP.NET Core MVC: Authentication And Role Based Authorization With ASP.NET Core Identity](https://social.technet.microsoft.com/wiki/contents/articles/36804.asp-net-core-mvc-authentication-and-role-based-authorization-with-asp-net-core-identity.aspx) Jan18
- [Add JWT Bearer Authorization to Swagger and ASP.NET Core](https://ppolyzos.com/2017/10/30/add-jwt-bearer-authorization-to-swagger-and-asp-net-core/) Oct17 
- [1](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/introduction)
- [2](https://channel9.msdn.com/Blogs/Seth-Juarez/ASPNET-Core-Authorization-with-Barry-Dorrans)
- [3](https://github.com/blowdart/AspNetAuthorizationWorkshop)
- [4](https://github.com/blowdart/AspNetAuthorizationWorkshop/tree/core2)
- [Extending Identity Accounts and Implementing Role-Based Authentication in ASP.NET MVC 5](http://johnatten.com/2013/11/11/extending-identity-accounts-and-implementing-role-based-authentication-in-asp-net-mvc-5/) nov13
- [Authorization in ASP.NET Core: Simple, role, claims-based, and custom oct16](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/)
- [Authorize](https://www.tutorialspoint.com/asp.net_core/asp.net_core_authorize_attribute.htm)
- [5](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?tabs=aspnetcore2x)

## mvc 
**project.json**
```json
"commands": {
    "web": "Microsoft.AspNet.Server.Kestrel"
}
```

ConfigureServices, authorization _before_ mvc
```cs
services.AddAuthorization();
services.AddMvc();
```



## angular
observables and behaviorsubject
https://stackoverflow.com/a/40231605/2239678
https://github.com/Reactive-Extensions/RxJS/blob/master/doc/api/subjects/behaviorsubject.md

[<<](./README.md) 