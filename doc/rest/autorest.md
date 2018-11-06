# AutoRest

- [Generating clients for your APIs with AutoRest](https://dzimchuk.net/generating-clients-for-your-apis-with-autorest/)
- [AutoRest Command Line Interface Documentation](https://github.com/Azure/autorest/blob/master/docs/user/cli.md)
- Install autorest and csharp generator extension / generate

  ```shell
  npm search autorest
  npm install -g autorest @microsoft.azure/autorest.csharp ms-rest ms-rest-azure
  autorest --input-file=http://localhost:63300//swagger/v1.0/swagger.json --namespace=Generated --output-folder=Generated --csharp --client-side-validation=false
  ```

- OpenAPI (f.k.a Swagger) [Specification code generator](https://github.com/Azure/autorest).
  - Supports C#, Go, Java, Node.js, TypeScript, Python, Ruby and PHP.
  - Code Generation to consume the API is generated via [**Autorest**](https://github.com/Azure/autorest) and [**Swagger**](https://github.com/swagger-api/swagger-ui). Will be used for *integration* tests.
  
- How to use **Sandcastle** type xml comments in your Swagger generated API documentation: `summary` goes as top right description, `remarks` is listed as _implementation notes_, controller `Produces` attribute mapped to _Response Content Type_, _response messages_ controlled by a combo of `ProducesResponseType` attribute and the `response` xml tag.

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
- Azure/autorest [tracing](https://github.com/Azure/autorest/blob/master/docs/client/tracing.md)

[<](call.md) | [<<](../rest.md) | [home](../../README.md)