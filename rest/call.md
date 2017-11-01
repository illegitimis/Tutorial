# Call a REST API

+ [`HttpClient`](https://msdn.microsoft.com/en-us/library/system.net.http.httpclient(v=vs.110).aspx)
  - [PowerBI Apiary mock tests](https://gist.github.com/illegitimis/de5975b9de77637d6d5f343c37d53273)
  - [`FormUrlEncodedContent`](https://stackoverflow.com/a/7929084) response on SO  
  - [Calling a Web API From a .NET Client (C#)](https://docs.microsoft.com/en-us/aspnet/web-api/overview/advanced/calling-a-web-api-from-a-net-client) 2014
  - [HttpClientExtensions.PostAsJsonAsync](https://msdn.microsoft.com/en-us/library/system.net.http.httpclientextensions.postasjsonasync.aspx)
  - `HttpRuntime.Cache` and [HttpClient.GetAsync: The underlying connection was closed](https://stackoverflow.com/a/30473478/2239678)
  - [System.Net.Http.HttpRequestException Error while copying content to a stream](https://stackoverflow.com/questions/33233780/system-net-http-httprequestexception-error-while-copying-content-to-a-stream) on SO
  - *scalability* with `ServicePointManager` [on SO](https://stackoverflow.com/questions/25195607/httpclient-scalability-problems)

+ `AutoRest/Swagger`
  - [AutoRest Command Line Interface Documentation](https://github.com/Azure/autorest/blob/master/docs/user/cli.md)

  ```shell
  # Install autorest and csharp generator extension 
  npm search autorest
  npm install -g autorest @microsoft.azure/autorest.csharp ms-rest ms-rest-azure
  # generate
  autorest --input-file=http://localhost:63300//swagger/v1.0/swagger.json --namespace=Generated --output-folder=Generated --csharp --client-side-validation=false
  ```
  - OpenAPI (f.k.a Swagger) [Specification code generator](https://github.com/Azure/autorest). Supports C#, Go, Java, Node.js, TypeScript, Python, Ruby and PHP.
  - Code Generation to consume the API is generated via [**Autorest**](https://github.com/Azure/autorest) and [**Swagger**](https://github.com/swagger-api/swagger-ui). Will be used for *integration* tests.
  - [ASP.NET Web API **Help Pages** using Swagger](https://docs.microsoft.com/en-us/aspnet/core/tutorials/web-api-help-pages-using-swagger?tabs=visual-studio)
  - How to use **Sandcastle** type xml comments in your Swagger generated API documentation: `summary` goes as top right description, `remarks` is listed as _implementation notes_, 
controller `Produces` attribute mapped to _Response Content Type_, _response messages_ controlled by a combo of `ProducesResponseType` attribute and the `response` xml tag.
```csharp
        /// <returns>a single feature configuration</returns>
        /// <response code="200">Feature Configuration found - body contains data</response>
        /// <response code="404">Feature Configuration does not exist</response>
        /// <response code="500">
        /// Internal Server Error. An unhandled exception occurred while processing the request.
        /// <![CDATA[
        /// AmbiguousActionException: Multiple actions matched.
        /// DependencyResolutionException: An error occurred during the activation of a particular registration.
        /// ]]>
        /// </response>
        [HttpGet]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(IEnumerable<FeatureConfigurationResponseDto>))]
        [ProducesResponseType(StatusCodes.Status404NotFound, Type = typeof(void))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError, Type = typeof(Exception))]
        public async Task<IActionResult> Get()
```
  - [Generating a client using AutoRest *Sample*](https://github.com/Azure/autorest/blob/master/docs/generating-a-client.md)

+ `RestSharp`
  - [home](http://restsharp.org/)
  - [SO example](https://stackoverflow.com/a/33812542) 
  ```csharp
     var request = new RestRequest(Method.POST);
     request.AddHeader("content-type", "application/x-www-form-urlencoded");
  ```
  - [projects using it](https://github.com/restsharp/RestSharp/wiki/Projects-Using-RestSharp)
  
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

