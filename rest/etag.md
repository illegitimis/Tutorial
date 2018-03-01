# ETag

- ETag on [w3](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14\.19)
- server initial response: `ETag: "01234567890abcdef"`
- client later request : `If-None-Match: "01234567890abcdef"`
- server later response : `304 Not Modified`
- 304 is returned without the body of the message, and that's the message back to the client saying, you already have the most recent copy of this object obviously because you gave me the ETag, so I'm not going to bother sending it back to you. 
- Size of the response, as it comes back across the wire, is much smaller. makes the server work less.
- They're a unique key for a particular version of a resource.
- They're returned in the header and often used for calls later back to the server, also in the header.
- This ETag is just, again, a magic number, and is going to include a prefix of W/ if it is a weak ETag.
- The difference between a weak and a strong ETag is how persistent that number is. 
- **strong ETag** is going to exist for days or weeks at a time, _won't include this W/_. 
- **weak** does include the W/, only useful for a shorter amount of time. 
- as the client has retrieved this ETag, they can use it on subsequent requests. 
- Usually with GET and DELETE, you're going to use the `If-None-Match` header value. 
- Ask the server, hey, if you have a newer version of this GET, return it to me, otherwise, return a 304 to tell me I have most current. 
- For PUT and PATCH, this is different. Here we're going to use `If-Match`. So, we're going to say, make this modification only if the ETag matches this If-Match clause. And, if this match fails, it's going to return a **412, or precondition failed**. 
- standard web Cache Headers, put together usually by IIS to define whether an object is static or not, `Cache-Control: no-cache`, `Pragma: no-cache`
- `CacheCow.Server` a project started from a WebApiContrib project
```cs
// the CacheCow system is going to use an in-memory source for our caching
var cs = ConfigurationManager.ConnectionStrings["DefaultConnection"]....;
var cacheHandler = new CachingHandler(new CacheCow.Server.EntityTagStore.XYZEntityTagStore(cs));
cacheHandler.AddLastModifiedHeader = true;
config.MessageHandlers.Add (cacheHandler);
```
- It's going to look for requests that have the `If-Match` and `If-None-Match`, and do the right thing, and it's going to look for the responses as they go out to Push them into the Cache, and Push those ETags in for us. 
- this ETag is not only weak, but it's going to change every time the server Refreshes, or, more importantly what happens if it hits another load balance server (`W/`).
- On rebuild, website restarted and therefore all that Cache and Memory was wiped.
- `CacheCow.Server.EntityTagStore.SqlServer` use a non-memory data store, something persistent, like SQL Server, RavenDB, Memcache.
  can't find the stored procedure named `GetCache`. Deploy script included in package.
- [CacheCow](https://github.com/aliostad/CacheCow/wiki) is a library for implementing HTTP caching on both client and server in ASP.NET Web API. It uses _message handlers on both client and server_ to intercept request and response and apply caching logic and rules.
+ [KevinDockx/HttpCacheHeaders](https://github.com/KevinDockx/HttpCacheHeaders) **ASP.NET Core middleware** that adds `HttpCache` headers to responses (`Cache-Control`, `Expires`, `ETag`, `Last-Modified`), and implements cache expiration & validation models 
+ [Implement HTTP Cache (ETag) in ASP.NET Core Web API](https://stackoverflow.com/questions/35458737/implement-http-cache-etag-in-asp-net-core-web-api/35555544#35555544) on SO
+ And more notably, when you're dealing with a server farm, or even a server garden, this is a good way to have Cache that's stored in sort of a central place. Now, this may feel a lot like having side effects of things like session state. So even though _this Cache system does have some side effects on the server_, the benefit of using Cached objects, and being able to test concurrency using that Cache, for me greatly _outweigh the bending of the rule for a Stateless Server_.


[<](./webapi.md)
|
[<<](../REST.md)
|
[home](../README.md) 