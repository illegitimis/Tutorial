# Call a REST API

+ [`HttpClient`](https://msdn.microsoft.com/en-us/library/system.net.http.httpclient(v=vs.110).aspx)
  - [PowerBI Apiary mock tests](https://gist.github.com/illegitimis/de5975b9de77637d6d5f343c37d53273)
  - [`FormUrlEncodedContent`](https://stackoverflow.com/a/7929084) response on SO  
  - [Calling a Web API From a .NET Client (C#)](https://docs.microsoft.com/en-us/aspnet/web-api/overview/advanced/calling-a-web-api-from-a-net-client) 2014
  - [HttpClientExtensions.PostAsJsonAsync](https://msdn.microsoft.com/en-us/library/system.net.http.httpclientextensions.postasjsonasync.aspx)
+ `AutoRest/Swagger`
  - [AutoRest Command Line Interface Documentation](https://github.com/Azure/autorest/blob/master/docs/user/cli.md)
  - OpenAPI (f.k.a Swagger) [Specification code generator](https://github.com/Azure/autorest). Supports C#, Go, Java, Node.js, TypeScript, Python, Ruby and PHP.
  - Code Generation to consume the API is generated via [**Autorest**](https://github.com/Azure/autorest) and [**Swagger**](https://github.com/swagger-api/swagger-ui). Will be used for *integration* tests.

```shell
# Install autorest and csharp generator extension 
npm search autorest
npm install -g autorest @microsoft.azure/autorest.csharp ms-rest ms-rest-azure
# generate
autorest --input-file=http://localhost:63300//swagger/v1.0/swagger.json --namespace=Generated --output-folder=Generated --csharp
```
+ `RestSharp`
  - [SO example](https://stackoverflow.com/a/33812542)
  - [home](http://restsharp.org/)
+ `cURL`
  - [libcurl.NET](https://sourceforge.net/projects/libcurl-net/)
  - [CurlSharp - .Net binding and object-oriented wrapper for libcurl. ](https://github.com/masroore/CurlSharp)
  - [CURLE_SSL_CERTPROBLEM](https://curl.haxx.se/mail/lib-2007-01/0156.html)
+ `WebClient`
+ [`HttpWebRequest`](https://msdn.microsoft.com/en-us/library/system.net.httpwebrequest.aspx) / [`HttpWebResponse`](https://msdn.microsoft.com/en-us/library/system.net.httpwebresponse.aspx)
  - [WebRequest & Json.Linq](https://stackoverflow.com/a/30770354)




[<<](../REST.md)
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 