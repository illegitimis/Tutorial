# Swagger

- Rest calls with AutoRest/Swagger [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](../rest/autorest.md).
- [Generating clients for your APIs with AutoRest](https://dzimchuk.net/generating-clients-for-your-apis-with-autorest/)
- [How to set up Swashbuckle vs Microsoft.AspNetCore.Mvc.Versioning](https://stackoverflow.com/questions/40929916/how-to-set-up-swashbuckle-vs-microsoft-aspnetcore-mvc-versioning)

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