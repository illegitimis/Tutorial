# AutoRest/Swagger

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
        /// <response code="200">found - body contains data</response>
        /// <response code="404">does not exist</response>
        /// <response code="500">
        /// Internal Server Error. An unhandled exception occurred while processing the request.
        /// <![CDATA[
        /// AmbiguousActionException: Multiple actions matched.
        /// DependencyResolutionException: An error occurred during the activation of a particular registration.
        /// ]]>
        /// </response>
        [HttpGet]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(IEnumerable<ResponseDto>))]
        [ProducesResponseType(StatusCodes.Status404NotFound, Type = typeof(void))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError, Type = typeof(Exception))]
        public async Task<IActionResult> Get()
```
  - [Generating a client using AutoRest *Sample*](https://github.com/Azure/autorest/blob/master/docs/generating-a-client.md)
  - [Swagger UI - Adding multiple custom header parameters](https://groups.google.com/forum/#!topic/swagger-swaggersocket/ibuoVSYi9dw)
  - Generating Swagger example [requests](https://mattfrear.com/2016/01/25/generating-swagger-example-requests-with-swashbuckle/) & [responses](https://mattfrear.com/2015/04/21/generating-swagger-example-responses-with-swashbuckle/) with Swashbuckle

 

[<<](./call.md)
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 