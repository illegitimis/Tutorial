# Swagger

- Rest calls with AutoRest/Swagger [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](../rest/autorest.md).
- [Generating clients for your APIs with AutoRest](https://dzimchuk.net/generating-clients-for-your-apis-with-autorest/)
- [How to set up Swashbuckle vs Microsoft.AspNetCore.Mvc.Versioning](https://stackoverflow.com/questions/40929916/how-to-set-up-swashbuckle-vs-microsoft-aspnetcore-mvc-versioning)
- *SwaggerUI* authorization
  + [Adding Basic Authorization for Swagger-UI](http://www.itkeyword.com/doc/5841486711643521478/adding-basic-authorization-for-swagger-ui) 2017-03-18
  + [Customize Authentication Header in SwaggerUI using Swashbuckle](http://stevemichelotti.com/customize-authentication-header-in-swaggerui-using-swashbuckle/) June 2015
  + [HitBTC API 2.1.0 ](https://api.hitbtc.com/api/2/explore/)
  + [Adding Basic Authorization for Swagger-UI](https://stackoverflow.com/questions/31057343/adding-basic-authorization-for-swagger-ui#31175040) jul 15
  + [Adding a Authorization field to the Swagger UI](http://blog.sluijsveld.com/28/01/2016/CustomSwaggerUIField/) jan 16
  + [Web API with OAUTH using Swagger / Swashbuckle](https://stackoverflow.com/questions/28033857/web-api-with-oauth-using-swagger-swashbuckle)
  + [Swagger and ASP.NET Web API - Part II: Enabling OAuth 2.0](http://wmpratt.com/part-ii-swagger-and-asp-net-web-api-enabling-oauth2/)

## Recipes

_packages_
```csproj
<PackageReference Include="Swashbuckle" Version="5.5.3" />
<PackageReference Include="Swashbuckle.AspNetCore" Version="1.0.0" />
```

_configure swagger middleware_
```cs
using Swashbuckle.AspNetCore.Swagger;

app.UseSwagger();

app.UseSwaggerUI(c => 
	c.SwaggerEndpoint("/swagger/v1.0/swagger.json", "API V1.0");
});
services.AddSwaggerGen(c => {
	c.SwaggerDoc("v1.0", new Info { Version = "v1.0", Title = "API V1.0" });

	var xmlDocFile = Path.Combine(CurrentDomain.BaseDirectory, "generated.Api.xml");
	if (System.IO.File.Exists(xmlDocFile)) c.IncludeXmlComments(xmlDocFile); 

	c.DescribeAllEnumsAsStrings();
});
```

_test swagger definitions_
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
            swaggerResult = await client.DownloadStringTaskAsync(Settings.Instance.SiteURL + TargetUrl);
        }

        swaggerResult.Should().NotBeNull();

        var obj = JsonConvert.DeserializeObject<JObject>(swaggerResult);
        var paths = obj["paths"];
        Assert.True(paths.Children().Count() > 1);
    }
}
```
_AutoRest strongly typed API better name generation_
  
  Instead of `[ProducesResponseType((int)HttpStatusCode.BadRequest, Type = typeof(void))]` use `[SwaggerResponse(StatusCodes.Status401Unauthorized, null, "Unauthorized")]`.
  
  Instead of `[Action("name")]` use `SwaggerOperation("Ping", Schemes = new[] { "http" })]`.





[<<](../SOA.md)
|
[home](README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki)