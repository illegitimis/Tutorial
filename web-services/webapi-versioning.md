# API Versioning

See versioning chapter in Wildermuth's __Web API Design__ [slides](https://onedrive.live.com/embed?cid=B3A4DB2490C51CCD&resid=B3A4DB2490C51CCD%21204889&authkey=AJdXhKx3Nh8gzvo&em=2)
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://onedrive.live.com/embed?cid=B3A4DB2490C51CCD&resid=B3A4DB2490C51CCD%21204889&authkey=AJdXhKx3Nh8gzvo&em=2).

Move the version with a 'v' prefix all the way to the left in the URL so that it has the **highest scope** (e.g. /v1/dogs).

Use a simple ordinal number - v1, v2, and so on. _Don't use the dot notation like v1.2_ because it implies a granularity of versioning that doesn't work well with APIs, _it's an interface not an implementation_. Make the version _mandatory_.

type | example | info | pro | con
--- | --- | --- | --- | ---
URL path | `https://api.stormpath.com/v1`<br> `http://api.tumblr.com/v2/user/`<br/> `http://.../api/v1/Customers?type=Current&id=123`<br> `http://.../api/v2/CurrentCustomers/123` | version embedded in URI path<br> everything after `v` subject to change | Simple to segregate old APIs for backwards compatibility | a lot of client changes on version upgrade<br> increases URI surface to support(tech debt), upgraded v2 and former v1 bug fixes<br>
Uri parameter | `http://api.netflix.com/catalog/titles/series/70023522?v=1.5`<br/> `http://.../api/Customers`<br/> `http://.../api/Customers?v=2.1` | semantically same with URI path versioning | without version => latest<br/> Little client change as versions mature | surprise clients with changes not expected<br/>
Media Type/Content Negotiation | `application/foo+json;application&v=1`<br> `Content Type: application/vnd.github.1.param+json`<br/> `Accept: application/myapp.v1.customer.json`<br/> `Accept: vnd.myapp.v1.customer` | Instead of using standard MIME types, use custom.<br/> Can include information in Accept Header<br/> Alternatively can create own MIME type. | Increasingly popular because separated from the surface area of the API itself<br/> Packages API and Resource Versioning in one<br/> Removes versioning from API so clients don't have to change | Can encourage increased versioning which causes more code churning
Request/Custom Header | Azure `x-ms-version: 2011-08-18`<br> `x-MyApp-Version: 2.1` | Should be a header value that is only of value to your API<br/> Common to use API Date instead of number | Separates Versioning from API call signatures<br/> Not tied to resource versioning (e.g. Content Type) | Adds complexity - adding headers isn't easy on all platforms


## Abstract

from _Implementing an API in ASP.NET Web API_ by Shawn Wildermuth on [Pluralsight](https://app.pluralsight.com/library/courses/implementing-restful-aspdotnet-web-api/)

So, what do we mean by API Versioning? Once you expose an API through Web API, or really any REST-based API technology, it is done. You have customers and users that rely on it so you can't change it. You have an implicit contract between you and these users and customers, those developers out there that have developed their applications against your API, which means that API can't go away. But, of course, the requirements of what you're trying to build are likely to change, so you need to have a way to evolve them without breaking the implicit contract between you and those developers.

_API Versioning isn't Product Versioning_, so you're not just going to release a new version of the API every time you release a new product version. With luck, you're going to do less API Versioning than you are going to do Product Versioning, but there's going to be cases where you're going to need evolve and do both. It is typically a bad idea to tie the two concepts together.

So, the problem with API versioning is that it is _very different from typical code versioning_ (assemblies).
You're going to be exposing out, in most cases, multiple versions of your API within the same ASP.NET project.
So you have to have a way to deal with that versioning.
Your API needs to support both new users that are going to use the latest version, as well as keep happy those developers that use the earlier versions of your API.
_You can't really do side-by-side deployment_. You're going to be creating and supporting different versions of the API going forward. At some point, you may be able to sunset certain versions of the API, but you have to give developers a lot of notice that they'll have to change their code.
This need to have both versions in the same code base means you're going to have similar functionality in different parts of your code base, and then have to have a way for Web API to detect which version the users are using, and have them come in.

Even more difficult is they may be using the original API you released, but you may be able to actually _forward users_ to the new version of the API, and that'll be fine. And so, the versioning may not be the entire API changes.

## Creating A Versioned Controller

  ```cs
  // CountingKsAuthorizeAttribute : AuthorizationFilterAttribute
#if DEBUG 
 define DISABLE_SECURITY
#endif
// also mock CountingKsIdentityService
Thread.CurrentPrincipal.Identity.Name
// extend model class
MeasureV2Model : MeasureModel
// separate controlller class
public class MeasuresV2Controller : BaseApiController
// Some of the other techniques have a MeasuresController inside of a V1, and a V2, and a V3 namespace.
// WebApiConfig.Register (HttpConfiguration cfg)
cfg.Routes.MapHttpRoute(name: "Food",
    routeTemplate: "api/v1/nutrition/foods/{foodid}",
    defaults: new { controller="foods", ...}
);
CustomControllerSelector : System.Web.HttpDispatcher.DefaultHttpControllerSelector
// web api cfg (URL path)
cfg.Services.Replace(typeof(IHttpControllerSelector), typeof(CustomControllerSelector));
// unspecified params in urlhelper links are represented as query params
HttpUtility.ParseQueryString
GetVersionFromQueryString (HttpRequestMessage request)
// versioning with a version header
GetVersionFromHeader (HttpRequestMessage request)
request.Headers.Contains(X-CountingKs-Version)
request.Headers.GetValues(X-CountingKs-Version).FirstOrDefault()
// Versioning with The Accept Header
// Accept: application/json; version=2
request.Headers.Accept.First(mime => mime.MediaType == "application/json").Parameters.Where(p => p.Name == "version")
// own custom mime type
static void CreateMediaTypes (JsonMediaTypeFormatter jsonFormatter)
"application/vnd.countingks.measure.v2+json"
jsonFormatter.SupportedMediaTypes.Add(new MediaTypeHeaderValue(...))
 ```

## Packages

- SDammann.WebApi.Versioning, 2.8.0, Library for API versioning support in Microsoft ASP.NET Web API
- [Microsoft/aspnet-api-versioning](https://github.com/Microsoft/aspnet-api-versioning) a set of libraries which add service API versioning to ASP.NET Web API, OData with ASP.NET Web API, and ASP.NET Core.
  - ASP.NET Core Versioned API Explorer with Swagger [Startup](https://github.com/Microsoft/aspnet-api-versioning/blob/master/samples/aspnetcore/SwaggerSample/Startup.cs)
  - ASP.NET Web API with OData [quick start](https://github.com/Microsoft/aspnet-api-versioning/wiki/API-Documentation#aspnet-web-api-with-odata)

[<](webapi.md) | [<<](../rest.md) | [home](../../README.md)
