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
- `AddFileParamTypes` operation filter [14] for _file upload_
- Modify Swagger with Request Context [15]
- Annotations [16] enrich operation, response and parameter metadata
- Extend Generator with Operation, Schema & Document Filters [17]
- Custom operation filters: AssignOperationVendor [18], RemoveVersionParameters [19], FormDataOperationFilter [20]
- Custom UI [21] website project

## Recipes

- _packages_

```csproj
<PackageReference Include="Swashbuckle" Version="5.5.3" />
<PackageReference Include="Swashbuckle.AspNetCore" Version="1.0.0" />
```

- _configure swagger middleware_
  - `ConfigureServices` permalink [22], bearer authorization ConfigureSwaggerGen.Bearer.cs [23]
  - `Configure` link [24]
  - operation filter SwaggerApiOperationIdFilter.cs [25]
  - header parameter [26]

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
