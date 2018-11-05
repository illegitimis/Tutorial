# Web API

## Recipes

- [Web API Versioning](webApiVersion.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](webApiVersion.md)
- [ETag](etag.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](etag.md)
- [Caching](cache.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](cache.md)
- [Web API upload & download files](./webApiUpDownLoad.md) [![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./webApiUpDownLoad.md)
- One _exception_ to the **use nouns instead of verbs** rule when designing routes are actions like: `translate`, `compute`, `convert`. All non-resource actions which remind of some non-rest service should **use verbs instead of nouns**, e.g. `http://mybank.com/convert?from=EUR&to=SGD&amount=100`.
- samples of _bad design_, `/getAccount`, `/createFolder`, `/updateGroup`, `/verifyEmail`, `/searchGroupsByName`
- fundamentally there are two types of resources: **collection** & **instance**
- _media types_ control format specification handles _content negotiation_ and parsing rules, by use of headers: 
  - requests: [_Accept_](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept). Samples: `Accept:application/json, text/plain, applications/myResourceExtension.csv`, `Accept: application/myapp.v1.customer.json` or `Accept: vnd.myapp.v1.customer` (versioning with content negotiation) 
  - response: [_Content-Type_](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) in the form `<content-type>: <media-type>;<options>`, like `Content-Type: text/html; charset=ISO-8859-4` or `Content-Type: application/json` or `Content-Type: application/foo+json` or `Content-Type: multipart/form-data; boundary=something`
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
  - Server response to issue challenge: [WWW-Authenticate](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate). Format: `WWW-Authenticate: <scheme name> realm=<application name>`. Schemes: `Basic`, `Bearer`, `Digest`, `OAuth`.
  - Client request to submit credentials: [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization). Format: `Authorization: <scheme name|type> <data|credentials>`, e.g. `Authorization: Basic YWxhZGRpbjpvcGVuc2VzYW1l` where string is _base64 encoded_ from the username and the password are combined with a colon (`aladdin:opensesame`).

## Unvisited Queue

- [json:api](http://jsonapi.org/) A specification for building APIs in JSON, 2017, v1.0 stable and [Implementations](http://jsonapi.org/implementations/) both client & server
- [Compressing Web API Response Using DotNetZip](http://www.c-sharpcorner.com/article/compressing-web-api-response-to-using-dotnetzip/) jun16
- [Tips And Tricks To Improve WEB API Performance](http://www.c-sharpcorner.com/article/important-steps-to-increasing-web-api-performance/) sep16
- [Implementing an API in ASP.NET Web API by Shawn Wildermuth](xyz.md) TODO

[<<](../rest.md) | [home](../../README.md)