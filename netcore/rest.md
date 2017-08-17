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