# Web API

## Pages

- [Web API Versioning](webApiVersion.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](webApiVersion.md)
- [ETag](etag.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](etag.md)
- [Caching](cache.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](cache.md)
- [Web API upload & download files](./webApiUpDownLoad.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./webApiUpDownLoad.md)
- [Implementing an API in ASP.NET Web API by Shawn Wildermuth](./webapi-asp-net-course.md) TODO formatting

## Recipes

- One _exception_ to the **use nouns instead of verbs** rule when designing routes are actions like: `translate`, `compute`, `convert`. All non-resource actions which remind of some non-rest service should **use verbs instead of nouns**, e.g. `mybank.com: Convert [1].
- samples of _bad design_, `/getAccount`, `/createFolder`, `/updateGroup`, `/verifyEmail`, `/searchGroupsByName`
- fundamentally there are two types of resources: **collection** & **instance**
- _media types_ control format specification handles _content negotiation_ and parsing rules, by use of headers:
  - requests: _Accept_ [2]. Samples: `Accept:application/json, text/plain, applications/myResourceExtension.csv`, `Accept: application/myapp.v1.customer.json` or `Accept: vnd.myapp.v1.customer` (versioning with content negotiation)
  - response: _Content-Type_ [3] in the form `<content-type>: <media-type>;<options>`, like `Content-Type: text/html; charset=ISO-8859-4` or `Content-Type: application/json` or `Content-Type: application/foo+json` or `Content-Type: multipart/form-data; boundary=something`
- Better linking with hateoas, instead of just resource urls specify media type too: `200 OK GET /accounts/x7y8z9`

    ```json
    {
        meta: {
            href: 'https://api.andrei.com/v1/accounts/x7y8z9',
            mediaType: 'application/ion+json;version=2&schema=...'
        }
    }
    ```

- _reference expansion_ / entity expansion / link expansion / partial representation: `GET /accounts/x7y8z9?expand=someNode`, `GET /accounts/x7y8z9?fields=name,surname,directory(name)`
- as descriptive as possible, as much info, devs are customers, e.g. `POST /dirs 409 CONFLICT`

```json
{
    status: 409,
    code: 40924,
    property: 'name',
    message: 'A directory called "Avengers" already exists',
    dev: 'A directory called "Avengers" already exists. If you have a stale cache, expire it.',
    info: 'http://www.andrei.com/docs/api/errors/40924'
}
```

- Avoid sessions when possible. Authenticate every request if necessary. **Stateless Authorize** based on _resource content_, NOT URL! Use Existing Protocol: Oauth 1.0a, Oauth2, Basic over SSL only. Custom Authentication Scheme: Only if you provide client code / SDK Only if you really, really know what you‟re doing. Use _API Keys_ instead of Username/Passwords.
- **401 Unauthorize** means _UNAUTHENTICATED_ no valid credentials, while **403 Forbidden** means _UNAUTHORIZED_ no rights
- HTTP Authentication Schemes
  - Server response to issue challenge: WWW-Authenticate [4]. Format: `WWW-Authenticate: <scheme name> realm=<application name>`. Schemes: `Basic`, `Bearer`, `Digest`, `OAuth`.
  - Client request to submit credentials: Authorization [5]. Format: `Authorization: <scheme name|type> <data|credentials>`, e.g. `Authorization: Basic YWxhZGRpbjpvcGVuc2VzYW1l` where string is _base64 encoded_ from the username and the password are combined with a colon (`aladdin:opensesame`).
- Content Negotiation in ASP.NET Core 2.0
  - Code maze [6] article, Feb18
  - BSON Support in ASP.NET Web API  2.1 [7]
  - Microsoft/aspnet-api-versioning API Version Reader [8]
  - Shawn Wildermuth article [9]
  - `SwaggerReponseContentTypeAttribute` so answer [10]
  - media types [11] & rfc6838 [12]
  - Running ASP.NET Core content negotiation by hand [13]
  - ASP.NET Core MVC Protobuf Formatters git [14], blog [15]

## Unvisited Queue

- json:api [16] A specification for building APIs in JSON, 2017, v1.0 stable
  - Implementations [17] both client & server
  - JSON API .Net Core docs [18]
  - json-api-dotnet/JsonApiDotNetCore [19]. JSONAPI Framework for ASP.Net Core
  - vnd.api+json [20]

- Compressing Web API Response Using DotNetZip [21] jun16
- Tips And Tricks To Improve WEB API Performance [22] sep16

[<<](../rest.md) | [home](../../README.md)

[1]: http://mybank.com/convert?from=EUR&to=SGD&amount=100`
[2]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept
[3]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type
[4]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate
[5]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization
[6]: https://code-maze.com/content-negotiation-dotnet-core/
[7]: https://docs.microsoft.com/en-us/aspnet/web-api/overview/formats-and-model-binding/bson-support-in-web-api-21
[8]: https://github.com/Microsoft/aspnet-api-versioning/wiki/API-Version-Reader
[9]: https://wildermuth.com/2016/03/16/Content_Negotiation_in_ASP_NET_Core
[10]: https://stackoverflow.com/questions/34990291/swashbuckle-swagger-how-to-annotate-content-types
[11]: https://swagger.io/docs/specification/media-types/
[12]: https://tools.ietf.org/html/rfc6838
[13]: https://www.strathweb.com/2018/09/running-asp-net-core-content-negotiation-by-hand/
[14]: https://github.com/damienbod/AspNetCoreMvcProtobufFormatters
[15]: https://damienbod.com/2017/06/30/using-protobuf-media-formatters-with-asp-net-core/
[16]: http://jsonapi.org/
[17]: http://jsonapi.org/implementations/
[18]: https://json-api-dotnet.github.io/#/
[19]: https://github.com/json-api-dotnet/JsonApiDotNetCore
[20]: https://www.iana.org/assignments/media-types/application/vnd.api+json
[21]: http://www.c-sharpcorner.com/article/compressing-web-api-response-to-using-dotnetzip/
[22]: http://www.c-sharpcorner.com/article/important-steps-to-increasing-web-api-performance/
