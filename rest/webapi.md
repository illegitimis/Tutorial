# Web API

## Recipes

+ One _exception_ to the **use nouns instead of verbs** rule when designing routes are actions like: `translate`, `compute`, `convert`. All non-resource actions which remind of some non-rest service should **use verbs instead of nouns**, e.g. 
`http://mybank.com/convert?from=EUR&to=SGD&amount=100`.
+ samples of _bad design_, `/getAccount`, `/createFolder`, `/updateGroup`, `/verifyEmail`, `/searchGroupsByName`
+ fundamentally there are two types of resources: **collection** & **instance**
+ _media types_ control format specification handles _content negotiation_ and parsing rules, by use of headers: 
  - requests: [_Accept_](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept). Samples: `Accept:application/json, text/plain, applications/myResourceExtension.csv`, `Accept: application/myapp.v1.customer.json` or `Accept: vnd.myapp.v1.customer` (versioning with content negotiation) 
  - response: [_Content-Type_](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) in the form `<content-type>: <media-type>;<options>`, like `Content-Type: text/html; charset=ISO-8859-4` or `Content-Type: application/json` or `Content-Type: application/foo+json` or `Content-Type: multipart/form-data; boundary=something`
+ Better linking with hateoas, instead of just resource urls specify media type too
200 OK GET /accounts/x7y8z9
```json
{
    meta: {
        href: 'https://api.andrei.com/v1/accounts/x7y8z9',
        mediaType: 'application/ion+json;version=2&schema=...'
    }
}
```
+ _reference expansion_ / entity expansion / link expansion / partial representation
- `GET /accounts/x7y8z9?expand=someNode`
- `GET /accounts/x7y8z9?fields=name,surname,directory(name)`
+ as descriptive as possible, as much info, devs are customers, e.g. `POST /dirs 409 CONFLICT`
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
+ Avoid sessions when possible. Authenticate every request if necessary. Stateless Authorize based on resource content, NOT URL! Use Existing Protocol: Oauth 1.0a, Oauth2, Basic over SSL only. Custom Authentication Scheme: Only if you provide client code / SDK Only if you really, really know what you‟re doing. Use API Keys instead of Username/Passwords
+ **401 Unauthorize** means _UNAUTHENTICATED_ no valid credentials, while **403 Forbidden** means _UNAUTHORIZED_ no rights
+ HTTP Authentication Schemes 
  - Server response to issue challenge: [WWW-Authenticate](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate). Format: `WWW-Authenticate: <scheme name> realm=<application name>`. Schemes: `Basic`, `Bearer`, `Digest`, `OAuth`.     
  - Client request to submit credentials: [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization). Format: `Authorization: <scheme name|type> <data|credentials>`, e.g. `Authorization: Basic YWxhZGRpbjpvcGVuc2VzYW1l` where string is _base64 encoded_ from the username and the password are combined with a colon (`aladdin:opensesame`).
+ [ETag](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14\.19)
  - server initial response: `ETag: "01234567890abcdef"`
  - client later request : `If-None-Match: "01234567890abcdef"`
  - server later response : `304 Not Modified`

## Versioning
See versioning chapter in Wildermuth's __Web API Design__ [slides](https://onedrive.live.com/embed?cid=B3A4DB2490C51CCD&resid=B3A4DB2490C51CCD%21204889&authkey=AJdXhKx3Nh8gzvo&em=2) 
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://onedrive.live.com/embed?cid=B3A4DB2490C51CCD&resid=B3A4DB2490C51CCD%21204889&authkey=AJdXhKx3Nh8gzvo&em=2)
  - URL path, `https://api.stormpath.com/v1`, `http://api.tumblr.com/v2/user/`
  - Uri parameter, `http://api.netflix.com/catalog/titles/series/70023522?v=1.5`
  - Media Type/Content Negotiation `application/foo+json;application&v=1`, `Content Type: application/vnd.github.1.param+json`
  - Request/Custom Header, like Azure `x-ms-version: 2011-08-18`, `x-MyApp-Version: 2.1`



## Unvisited Queue

+ [json:api](http://jsonapi.org/) A specification for building APIs in JSON, 2017, v1.0 stable and [Implementations](http://jsonapi.org/implementations/) both client & server
+ [Compressing Web API Response Using DotNetZip](http://www.c-sharpcorner.com/article/compressing-web-api-response-to-using-dotnetzip/) jun16
+ [Tips And Tricks To Improve WEB API Performance](http://www.c-sharpcorner.com/article/important-steps-to-increasing-web-api-performance/) sep16

[<<](../REST.md)
|
[home](../README.md) 