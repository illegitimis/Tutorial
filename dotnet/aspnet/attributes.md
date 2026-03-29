# Attributes

## Microsoft.AspNetCore.Authorization.`AuthorizeAttribute`

```cs
[Authorize]
[Authorize(AuthenticationSchemes = "Bearer")]
[Authorize(AuthenticationSchemes = JwtBearerDefaults.AuthenticationScheme, Policy = Function.CanReject)]
```

## Microsoft.AspNetCore.Mvc.`ProducesResponseTypeAttribute`

```cs
using static Microsoft.AspNetCore.Http.StatusCodes;

[ProducesResponseType(Status200OK, Type = typeof(CommandResponse<List<SomeDto>>))]
[ProducesResponseType(Status400BadRequest, Type = typeof(JsonErrorResponse))]
[ProducesResponseType(Status401Unauthorized, Type = typeof(string))]
[ProducesResponseType(Status403Forbidden, Type = typeof(string))]
[ProducesResponseType(Status500InternalServerError, Type = typeof(JsonErrorResponse))]
```

## Microsoft.AspNetCore.Mvc.`FromQueryAttribute`

`FromBody`/`FromQuery`/`FromRoute` specifies how a parameter or property _should be bound_, query params, request body or route-data from the current request.

```cs
public IActionResult Get([FromQuery]MessagesRequest request)
public IActionResult Get([FromQuery] int id, [FromQuery] MessageRequest request)
public async Task<IActionResult> Create([FromBody] BatchRequest batch)

[HttpPost("reject/{id:guid}")]
public async Task<IActionResult> Reject(Guid id, [FromBody] string reason)

// constructor takes a template as parameter
[HttpPut("{facilityId}/{bandwidthChange}")]
// use multiple FromRoute attributes, one for each parameter you are expecting to be bound from the routing data
public void UpdateBandwidthChangeHangup([FromRoute] int facilityId, [FromRoute] int bandwidthChange)
```

[<< home](../../README.md) | [< netcore](../netcore.md)
