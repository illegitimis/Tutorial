# signalr

- [signalr](http://signalr.net/) Incredibly simple real-time web for ASP .NET
- Hub [protocol](https://github.com/aspnet/AspNetCore/blob/master/src/SignalR/docs/specs/HubProtocol.md) specs
- PS course [Real-time applications using ASP.NET Core, SignalR & Angular](https://chsakell.com/2016/10/10/real-time-applications-using-asp-net-core-signalr-angular/) oct 16 & [demo app](https://github.com/chsakell/aspnet-core-signalr-angular)
- [SignalR-plus-RX-Streaming-Data-Demo-App](http://www.codeproject.com/Articles/851437/SignalR-plus-RX-Streaming-Data-Demo-App)
- `SSE` (server sent events) is a html5 feature. server response content type `text/event-stream`. js must instantiate an `EventSource` object. Easilt polyfilled for older browsers?
- web sockets are a standardized way to use a TCP socket through which messages can be sent full duplex
- lifetime of a web socket: http handshake, data exchange, close. all inside the same TCP socket.
- web socket handshake
  - upgrade request. client sends random string

  ```http
  GET /chat HTTP/1.1
  Host: server.chat.com
  Origin: client.chat.com
  Upgrade: websocket
  Connection: Upgrade
  Sec-WebSocket-Key: dfsddscxvb
  Sec-WebSocket-Protocol: chat, superchat
  Sec-WebSocket-Version: 13
  Sec-WebSocket-Extensions: deflate-stream
  ```

  - 101 fine (switching protocols) response. Sends key back in accept header. Server add constant and hashes and base64 encodes.

  ```http
  HTTP/1.1 101 Switching Protocols
  Upgrade: websocket
  Connection: Upgrade
  Sec-WebSocket-Accept: vcbvcbasdef
  Sec-WebSocket-Protocol: chat
  Sec-WebSockets-Extensions: deflate-stream
  ```


- message is composed out of multiple frames with header bits to determine last frame. text msg converted to binary
- realtime web apps: polling, long polling, sse and signalr. named _transports_, fallback mechanism integrated from most efficient to polling.
- client side signalr libraries?
- uses RPC for communication.
- **hub** server side _class_ that sends/receives messages to/from clients.
- protocol is the serialization format: [msgpack](https://github.com/neuecc/MessagePack-CSharp/#compare-with-protobuf-json-zeroformatter) Compare with protobuf, JSON, ZeroFormatter. `Microsoft.AspNetCore.SignalR.Protocols.[Json|MessagePack|NewtonsoftJson]`. `MessagePackHubProtocol` [src](https://github.com/aspnet/SignalR/blob/master/src/Microsoft.AspNetCore.SignalR.Protocols.MessagePack/Protocol/MessagePackHubProtocol.cs), [proj](https://github.com/aspnet/SignalR/blob/master/src/Microsoft.AspNetCore.SignalR.Protocols.MessagePack/Microsoft.AspNetCore.SignalR.Protocols.MessagePack.csproj), [DI extensions](https://github.com/aspnet/SignalR/blob/master/src/Microsoft.AspNetCore.SignalR.Protocols.Json/JsonProtocolDependencyInjectionExtensions.cs), json hub protocol [impl](https://github.com/aspnet/SignalR/blob/master/src/Microsoft.AspNetCore.SignalR.Protocols.Json/Protocol/JsonHubProtocol.cs)
- configuration [docs](https://github.com/aspnet/AspNetCore.Docs/blob/master/aspnetcore/signalr/configuration.md).
- Under the Covers of ASP.NET Core SignalR [article may 2018](https://msdn.microsoft.com/en-us/magazine/mt846655.aspx)
- The client side of a SignalR app needs a SignalR library `@aspnet/signalr-protocol-msgpack`
- Azure SignalR Service

[<< home](../../README.md) | [< soa](../soa.md)