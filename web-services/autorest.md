# AutoRest

- Generating clients for your APIs with AutoRest [1]
- AutoRest Command Line Interface Documentation [2]
- Install autorest and csharp generator extension / generate

  ```shell
  npm search autorest
  npm install -g autorest @microsoft.azure/autorest.csharp ms-rest ms-rest-azure
  autorest --input-file=http://localhost:63300//swagger/v1.0/swagger.json --namespace=Generated --output-folder=Generated --csharp --client-side-validation=false
  ```

- OpenAPI (f.k.a Swagger) Specification code generator [3].
  - Supports C#, Go, Java, Node.js, TypeScript, Python, Ruby and PHP.
  - Code Generation to consume the API is generated via **Autorest** [3] and **Swagger** [4] UI. Will be used for *integration* tests.
- How to use **Sandcastle** type xml comments in your Swagger generated API documentation: `summary` goes as top right description, `remarks` is listed as _implementation notes_, controller `Produces` attribute mapped to _Response Content Type_, _response messages_ controlled by a combo of `ProducesResponseType` attribute and the `response` xml tag.

    ```cs
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

- Generating a client using AutoRest *Sample* [5]
- Azure/autorest tracing [6]

[<](call.md) | [<<](../rest.md) | [home](../../README.md)

[1]: https://dzimchuk.net/generating-clients-for-your-apis-with-autorest/
[2]: https://github.com/Azure/autorest/blob/master/docs/user/cli.md
[3]: https://github.com/Azure/autorest
[4]: https://github.com/swagger-api/swagger-ui
[5]: https://github.com/Azure/autorest/blob/master/docs/generating-a-client.md
[6]: https://github.com/Azure/autorest/blob/master/docs/client/tracing.md
