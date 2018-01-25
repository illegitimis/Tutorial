# Microsoft.AspNetCore Rest

## Attributes

+ Microsoft.AspNetCore.Mvc.ProducesResponseTypeAttribute
```cs
	[ProducesResponseType((int)HttpStatusCode.OK, Type = typeof(List<MessageResponse>))]
	[ProducesResponseType((int)HttpStatusCode.BadRequest, Type = typeof(void))]
	[ProducesResponseType((int) HttpStatusCode.OK, Type = typeof(MessageResponse))]
    [ProducesResponseType((int) HttpStatusCode.BadRequest, Type = typeof(void))]
    [ProducesResponseType((int)HttpStatusCode.NotFound, Type = typeof(void))]
	[ProducesResponseType((int)HttpStatusCode.Created, Type = typeof(Uri))]
	[ProducesResponseType((int)HttpStatusCode.Forbidden, Type = typeof(void))]
    [ProducesResponseType((int)HttpStatusCode.NoContent, Type = typeof(void))]
```

+ Microsoft.AspNetCore.Mvc.FromQueryAttribute
```cs
 public IActionResult Get([FromQuery]MessagesRequest request)
 public IActionResult Get([FromQuery] int id, [FromQuery] MessageRequest request)
```

+ In-memory caching in ASP.NET Core
  - add `microsoft.extensions.caching.memory`
  - [In-memory caching is a service](https://docs.microsoft.com/en-us/aspnet/core/performance/caching/memory) that is referenced from your app using `Dependency Injection`. Call `AddMemoryCache` in `ConfigureServices`
```cs

```


```cs

```

```cs

```



```cs

```


```cs

```


```cs

```


```cs

```

```cs

```