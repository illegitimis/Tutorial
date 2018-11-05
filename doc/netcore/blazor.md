# Blazor

- [Blazor](https://blazor.net) is a client-side web UI .NET framework targeted at WebAssembly based on HTML and CSS that runs in the browser using open web standards
- install the .NET Core SDK [from here](https://dot.net), .NET runtime used for Blazor supports .NET Standard 2.0
- install Blazor CLI templates `dotnet new -i Microsoft.AspNetCore.Blazor.Templates`
- in VS install extension `aspnet.blazor`
- [Blazor: Modern Web development with .NET and WebAssembly](https://www.youtube.com/watch?time_continue=92&v=61qmX5eAPwI) - Daniel Roth
- When a Blazor app is built and run in a browser:
  - C# code files and Razor files are compiled into .NET assemblies.
  - The assemblies and the .NET runtime are downloaded to the browser.
  - Blazor uses JavaScript to _bootstrap the .NET runtime_ (`blazor.webassembly.js`) and configures the runtime (`mono.wasm`) to _load required assembly references_.
  - Document object model (DOM) manipulation and browser API calls are handled by the Blazor runtime via _JavaScript interoperability_.
- tour of heroes [demo clone](https://blazor-demo.github.io/)

[<<](../netcore.md) | [home](../../README.md)