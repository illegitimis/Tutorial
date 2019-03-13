# Swagger

- [How to set up Swashbuckle vs Microsoft.AspNetCore.Mvc.Versioning](https://stackoverflow.com/questions/40929916/how-to-set-up-swashbuckle-vs-microsoft-aspnetcore-mvc-versioning)
- *SwaggerUI* authorization
  - [Adding Basic Authorization for Swagger-UI](http://www.itkeyword.com/doc/5841486711643521478/adding-basic-authorization-for-swagger-ui) 2017-03-18
  - [Customize Authentication Header in SwaggerUI using Swashbuckle](http://stevemichelotti.com/customize-authentication-header-in-swaggerui-using-swashbuckle/) June 2015
  - [HitBTC API 2.1.0](https://api.hitbtc.com/api/2/explore/)
  - [Adding Basic Authorization for Swagger-UI](https://stackoverflow.com/questions/31057343/adding-basic-authorization-for-swagger-ui#31175040) jul 15
  - [Adding a Authorization field to the Swagger UI](http://blog.sluijsveld.com/28/01/2016/CustomSwaggerUIField/) jan 16
  - [Web API with OAUTH using Swagger / Swashbuckle](https://stackoverflow.com/questions/28033857/web-api-with-oauth-using-swagger-swashbuckle)
  - [Swagger and ASP.NET Web API - Part II: Enabling OAuth 2.0](http://wmpratt.com/part-ii-swagger-and-asp-net-web-api-enabling-oauth2/)
- [Swagger UI - Adding multiple custom header parameters](https://groups.google.com/forum/#!topic/swagger-swaggersocket/ibuoVSYi9dw)
- Generating Swagger example [requests](https://mattfrear.com/2016/01/25/generating-swagger-example-requests-with-swashbuckle/) & [responses](https://mattfrear.com/2015/04/21/generating-swagger-example-responses-with-swashbuckle/) with Swashbuckle
- [ASP.NET Web API **Help Pages** using Swagger](https://docs.microsoft.com/en-us/aspnet/core/tutorials/web-api-help-pages-using-swagger?tabs=visual-studio)
- [Add JWT Bearer Authorization to Swagger and ASP.NET Core](https://ppolyzos.com/2017/10/30/add-jwt-bearer-authorization-to-swagger-and-asp-net-core/) Oct17
- `AddFileParamTypes` [operation filter](https://github.com/domaindrivendev/Swashbuckle/issues/120) for _file upload_ 
- [Modify Swagger with Request Context](https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/3c91969b10710c961486df4123c69929a669ce7e/README.md#modify-swagger-with-request-context)
- [Annotations](https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/3c91969b10710c961486df4123c69929a669ce7e/README.md#swashbuckleaspnetcoreannotations) enrich operation, response and parameter metadata
- Extend Generator with [Operation, Schema & Document Filters](https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/3c91969b10710c961486df4123c69929a669ce7e/README.md#extend-generator-with-operation-schema--document-filters)
- Custom operation filters: [AssignOperationVendor](https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/c8d8edbf1a04ccf5662ad961fd373adaf0d12e32/test/WebSites/Basic/Swagger/AssignOperationVendorExtensions.cs), [RemoveVersionParameters](https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/c8d8edbf1a04ccf5662ad961fd373adaf0d12e32/test/WebSites/MultipleVersions/Swagger/RemoveVersionParameters.cs), [FormDataOperationFilter](https://github.com/domaindrivendev/Swashbuckle.AspNetCore/blob/c8d8edbf1a04ccf5662ad961fd373adaf0d12e32/test/WebSites/Basic/Swagger/FormDataOperationFilter.cs)
- [Custom UI](https://github.com/domaindrivendev/Swashbuckle.AspNetCore/tree/c8d8edbf1a04ccf5662ad961fd373adaf0d12e32/test/WebSites/CustomUIConfig) website project

## Recipes

- _packages_

```csproj
<PackageReference Include="Swashbuckle" Version="5.5.3" />
<PackageReference Include="Swashbuckle.AspNetCore" Version="1.0.0" />
```

- _configure swagger middleware_
  - `ConfigureServices` [permalink](https://github.com/illegitimis/Qualysoft.Evaluation/blob/9c6d41243e6821ddac2d808351a9186834a19b0d/Qualysoft.Evaluation.Api/Startup.cs#L65), bearer authorization [ConfigureSwaggerGen.Bearer.cs](https://gist.github.com/illegitimis/2b919c8a6cd706008dcf27cae4a107b7)
  - `Configure` [link](https://github.com/illegitimis/Qualysoft.Evaluation/blob/9c6d41243e6821ddac2d808351a9186834a19b0d/Qualysoft.Evaluation.Api/Startup.cs#L180)
  - operation filter [SwaggerApiOperationIdFilter.cs](https://gist.github.com/illegitimis/d529815d6c1833b2eadf4327b7cdc139)
  - [header parameter](https://gist.github.com/illegitimis/95d0929bf2234dc4245986e1b18afb91)

- _test swagger definitions_

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

- _better name generation_ UI
  - Instead of `[ProducesResponseType((int)HttpStatusCode.BadRequest, Type = typeof(void))]` use `[SwaggerResponse(StatusCodes.Status401Unauthorized, null, "Unauthorized")]`.
  - Instead of `[Action("name")]` use `SwaggerOperation("Ping", Schemes = new[] { "http" })]`.

[<<](../rest.md) | [home](../../README.md)