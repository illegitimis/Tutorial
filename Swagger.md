[Generating clients for your APIs with AutoRest](https://dzimchuk.net/generating-clients-for-your-apis-with-autorest/)
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
{
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

_autorest batch files_
```cmd
autorest --input-file=http://localhost:51228/swagger/docs/v1 --csharp --output-folder=./Generated/ --namespace=webApi.ClientAPI --debug
autorest --input-file=http://localhost:63300/swagger/v1.0/swagger.json --csharp --output-folder=./Generated/ --namespace=webApi.ClientAPI --debug
autorest --input-file=http://vs-qa1-app1.dev.eshopworld.com:51221/swagger/docs/v1 --csharp --output-folder=./Generated/ --namespace=webApi.ClientAPI.Processing --debug
autorest --input-file=http://vs-qa1-app1.dev.eshopworld.com:51222/swagger/docs/v1 --csharp --output-folder=./Generated/ --namespace=webApi.ClientAPI.Routing --debug
```