# Blazor

> `Blazor` [1] is a client-side web UI .NET framework targeted at `WebAssembly` based on HTML and CSS that runs in the browser using open web standards

- install Blazor CLI templates `dotnet new -i Microsoft.AspNetCore.Blazor.Templates`
- in VS install extension `aspnet.blazor`
- When a Blazor app is built and run in a browser:
  - C# code files and Razor files are compiled into .NET assemblies.
  - The assemblies and the .NET runtime are downloaded to the browser.
  - Blazor uses JavaScript to _bootstrap the .NET runtime_ (`blazor.webassembly.js`)
  - and configures the runtime (`mono.wasm`) to _load required assembly references_.
  - Document object model (DOM) manipulation and browser API calls are handled by the Blazor runtime via _JavaScript interoperability_.

## calendar

what | when
---|---
server | netcore30
webassembly | may 2020
pwa & electron | .net 5 preview
native | internal

## links

- Blazor home [1]
- Awesome Blazor [2] community
- tour of heroes demo clone [3]
- workshop [4]

## videos

- Blazor: Modern Web development with .NET and WebAssembly [5], Daniel Roth, sep 2018
- Blazor and Azure Functions for Serverless Websites [6] sep 2019
- Building Full-stack C# Web Apps with Blazor in .NET Core 3.0 [7] sep 2019
- The Future of Blazor on the Client [8] sep 2019

[< netcore](../netcore.md) | [<< home](../../README.md)

[1]: https://blazor.net
[2]: https://aka.ms/awesomeblazor
[3]: https://blazor-demo.github.io/
[4]: https://aka.ms/blazorworkshop
[5]: https://youtu.be/61qmX5eAPwI
[6]: https://youtu.be/noG3rxt38VI
[7]: https://youtu.be/MetcuX1OHD0
[8]: https://youtu.be/qF6ixMjCzHA
