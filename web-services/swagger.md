---
title: Swagger
layout: default
nav_order: 11
parent: Web Services
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Swagger

- How to set up Swashbuckle vs Microsoft.AspNetCore.Mvc.Versioning [1]
- *SwaggerUI* authorization
  - Adding Basic Authorization for Swagger-UI [2] 2017-03-18
  - Customize Authentication Header in SwaggerUI using Swashbuckle [3] June 2015
  - HitBTC API 2.1.0 [4]
  - Adding Basic Authorization for Swagger-UI [5] jul 15
  - Adding a Authorization field to the Swagger UI [6] jan 16
  - Web API with OAUTH using Swagger / Swashbuckle [7]
  - Swagger and ASP.NET Web API - Part II: Enabling OAuth 2.0 [8]
- Swagger UI - Adding multiple custom header parameters [9]
- Generating Swagger example requests [10] & responses [11] with Swashbuckle
- ASP.NET Web API **Help Pages** using Swagger [12]
- Add JWT Bearer Authorization to Swagger and ASP.NET Core [13] Oct17
- `AddFileParamTypes` operation filter [14] for *file upload*
- Modify Swagger with Request Context [15]
- Annotations [16] enrich operation, response and parameter metadata
- Extend Generator with Operation, Schema & Document Filters [17]
- Custom operation filters: AssignOperationVendor [18], RemoveVersionParameters [19], FormDataOperationFilter [20]
- Custom UI [21] website project

## Recipes

- *packages*

```csproj
<PackageReference Include="Swashbuckle" Version="5.5.3" />
<PackageReference Include="Swashbuckle.AspNetCore" Version="1.0.0" />
```

- *configure swagger middleware*
  - `ConfigureServices` permalink [22], bearer authorization ConfigureSwaggerGen.Bearer.cs [23]
  - `Configure` link [24]
  - operation filter SwaggerApiOperationIdFilter.cs [25]
  - header parameter [26]

- *test swagger definitions*

```cs
public class SwaggerTests
{
    private const string TargetUrl = "/swagger/v1.0/swagger.json";

    [Fact, IsWarmUp]
    public async Task VerifySwaggerEndpoint()
    {
        string swaggerResult;
        using (var client = new System.Net.WebClient())
        {
            swaggerResult = await client.DownloadStringTaskAsync($"{Settings.Instance.SiteURL}{TargetUrl}");
        }

        swaggerResult.Should().NotBeNull();

        var obj = JsonConvert.DeserializeObject<JObject>(swaggerResult);
        var paths = obj["paths"];
        Assert.True(paths.Children().Count() > 1);
    }
}
```

- *better name generation* UI
  - Instead of `[ProducesResponseType((int)HttpStatusCode.BadRequest, Type = typeof(void))]` use `[SwaggerResponse(StatusCodes.Status401Unauthorized, null, "Unauthorized")]`.
  - Instead of `[Action("name")]` use `SwaggerOperation("Ping", Schemes = new[] { "http" })]`.

[1]: https://stackoverflow.com/questions/40929916/how-to-set-up-swashbuckle-vs-microsoft-aspnetcore-mvc-versioning
[2]: http://www.itkeyword.com/doc/5841486711643521478/adding-basic-authorization-for-swagger-ui
[3]: http://stevemichelotti.com/customize-authentication-header-in-swaggerui-using-swashbuckle/
[4]: https://api.hitbtc.com/api/2/explore/
[5]: https://stackoverflow.com/questions/31057343/adding-basic-authorization-for-swagger-ui#31175040
[6]: http://blog.sluijsveld.com/28/01/2016/CustomSwaggerUIField/
[7]: https://stackoverflow.com/questions/28033857/web-api-with-oauth-using-swagger-swashbuckle
[8]: http://wmpratt.com/part-ii-swagger-and-asp-net-web-api-enabling-oauth2/
[9]: https://groups.google.com/forum/#!topic/swagger-swaggersocket/ibuoVSYi9dw
[10]: https://mattfrear.com/2016/01/25/generating-swagger-example-requests-with-swashbuckle/
[11]: https://mattfrear.com/2015/04/21/generating-swagger-example-responses-with-swashbuckle/
[12]: https://docs.microsoft.com/en-us/aspnet/core/tutorials/web-api-help-pages-using-swagger?tabs=visual-studio
[13]: https://ppolyzos.com/2017/10/30/add-jwt-bearer-authorization-to-swagger-and-asp-net-core/
[14]: https://github.com/domaindrivendev/Swashbuckle/issues/120
[15]: https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/3c91969b10710c961486df4123c69929a669ce7e/README.md#modify-swagger-with-request-context
[16]: https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/3c91969b10710c961486df4123c69929a669ce7e/README.md#swashbuckleaspnetcoreannotations
[17]: https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/3c91969b10710c961486df4123c69929a669ce7e/README.md#extend-generator-with-operation-schema--document-filters
[18]: https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/c8d8edbf1a04ccf5662ad961fd373adaf0d12e32/test/WebSites/Basic/Swagger/AssignOperationVendorExtensions.cs
[19]: https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/c8d8edbf1a04ccf5662ad961fd373adaf0d12e32/test/WebSites/MultipleVersions/Swagger/RemoveVersionParameters.cs
[20]: https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/c8d8edbf1a04ccf5662ad961fd373adaf0d12e32/test/WebSites/Basic/Swagger/FormDataOperationFilter.cs
[21]: https://github.com/domaindrivendev/Swashbuckle.AspNetCore/tree/c8d8edbf1a04ccf5662ad961fd373adaf0d12e32/test/WebSites/CustomUIConfig
[22]: https://github.com/illegitimis/Qualysoft.Evaluation/blob/9c6d41243e6821ddac2d808351a9186834a19b0d/Qualysoft.Evaluation.Api/Startup.cs#L65
[23]: https://gist.github.com/illegitimis/2b919c8a6cd706008dcf27cae4a107b7
[24]: https://github.com/illegitimis/Qualysoft.Evaluation/blob/9c6d41243e6821ddac2d808351a9186834a19b0d/Qualysoft.Evaluation.Api/Startup.cs#L180
[25]: https://gist.github.com/illegitimis/d529815d6c1833b2eadf4327b7cdc139
[26]: https://gist.github.com/illegitimis/95d0929bf2234dc4245986e1b18afb91

## OpenAPI Specification

> Source of truth is YML / JSON OAS

`Swagger` editor (Petstore v2) [27] \
`Swagger` Petstore 2.0 [28]

### .NET Core

`Swashbuckle.AspNetCore.SwaggerUI` \
SwaggerEndpoint \
`IApplicationBuilder.UseOpenApiSwagger` \
`app.UseSwaggerUI(c => c.SwaggerEndpoint(x, "title"))` \
x: /local yml or json in www root \
default is /swagger/v1/swagger.json

### .NET Framework 4.0 (Swashbuckle.Core 5.6.0)

`SwaggerConfig.cs` \
`HttpConfiguration.EnableSwagger` \
`CustomProvider` and/or `RootUrl`

`Swashbuckle.Core` [29] — not updated since Oct 2016 \
`Swashbuckle.WebApi` ISwaggerProvider search [30]

Swagger repositories at GitHub [31]

SwaggerConfig sample — all possible options .NET 4 [32] \
`CachingSwaggerProvider` [33] \
`SwaggerUiHandler` [34] \
`SwaggerDocsHandler` [35] \
`SwaggerGenerator` (official) [36] \
`HttpConfigurationExtensions` (OWIN) [37] \
`ISwaggerProvider` [38]

[27]: https://editor-next.swagger.io/
[28]: https://editor.swagger.io/
[29]: https://www.nuget.org/packages/Swashbuckle.Core#versions-body-tab
[30]: https://github.com/domaindrivendev/Swashbuckle.WebApi/search?q=%3A+ISwaggerProvider
[31]: https://github.com/orgs/swagger-api/repositories?type=all
[32]: https://github.com/domaindrivendev/Swashbuckle.WebApi/blob/master/Swashbuckle.Dummy.Core/App_Start/SwaggerConfig.cs
[33]: https://github.com/domaindrivendev/Swashbuckle.WebApi/blob/master/Swashbuckle.Dummy.Core/App_Start/CachingSwaggerProvider.cs
[34]: https://github.com/domaindrivendev/Swashbuckle.WebApi/blob/master/Swashbuckle.Core/Application/SwaggerUiHandler.cs
[35]: https://github.com/domaindrivendev/Swashbuckle.WebApi/blob/master/Swashbuckle.Core/Application/SwaggerDocsHandler.cs
[36]: https://github.com/domaindrivendev/Swashbuckle.WebApi/blob/master/Swashbuckle.Core/Swagger/SwaggerGenerator.cs
[37]: https://github.com/domaindrivendev/Swashbuckle.WebApi/blob/master/Swashbuckle.Core/Application/HttpConfigurationExtensions.cs
[38]: https://github.com/domaindrivendev/Swashbuckle.WebApi/blob/master/Swashbuckle.Core/Swagger/ISwaggerProvider.cs

## Contract-First Development

> **API/contract first** — OpenAPI-Driven API Design

Contract first OpenAPI development (but still use `Swagger` UI with ASP.NET Core) [39]

### Code Generation

`Swagger Codegen` — generate server stubs and client SDKs from **OpenAPI** specifications [40]

### NSwag

Get started with `NSwag` and ASP.NET Core [41]

### Documentation

Enriched Web API Documentation using Swagger/OpenAPI in ASP.NET Core [42]

[39]: https://blog.codingmilitia.com/2023/04/02/contract-first-openapi-development-but-still-use-swagger-ui-with-asp.net-core/
[40]: https://swagger.io/tools/swagger-codegen/
[41]: https://learn.microsoft.com/en-us/aspnet/core/tutorials/getting-started-with-nswag?view=aspnetcore-8.0&tabs=visual-studio
[42]: https://www.dotnetnakama.com/blog/enriched-web-api-documentation-using-swagger-openapi-in-asp-dotnet-core/

[<](./index.md) | [<<](/index.md)
