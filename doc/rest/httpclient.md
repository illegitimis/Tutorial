# HttpClient

  - `HttpClient` [msdn](https://msdn.microsoft.com/en-us/library/system.net.http.httpclient(v=vs.110).aspx)
  - [PowerBI Apiary mock tests](https://gist.github.com/illegitimis/de5975b9de77637d6d5f343c37d53273)
  - [`FormUrlEncodedContent`](https://stackoverflow.com/a/7929084) response on SO  
  - [Calling a Web API From a .NET Client (C#)](https://docs.microsoft.com/en-us/aspnet/web-api/overview/advanced/calling-a-web-api-from-a-net-client) 2014
  - [HttpClientExtensions.PostAsJsonAsync](https://msdn.microsoft.com/en-us/library/system.net.http.httpclientextensions.postasjsonasync.aspx)
  - `HttpRuntime.Cache` and [HttpClient.GetAsync: The underlying connection was closed](https://stackoverflow.com/a/30473478/2239678)
  - [System.Net.Http.HttpRequestException Error while copying content to a stream](https://stackoverflow.com/questions/33233780/system-net-http-httprequestexception-error-while-copying-content-to-a-stream) on SO
  - *scalability* with `ServicePointManager` [on SO](https://stackoverflow.com/questions/25195607/httpclient-scalability-problems)
  - `using Microsoft.AspNetCore.TestHost`
      
      ```cs
        // test class inherits from IDisposable
        //private TestServer _server;
        //private HttpClient _client;

        // Arrange
        //var hostBuilder = new WebHostBuilder()
        //   .UseEnvironment("Development")
        //   .UseStartup<esw.Checkout.Api.Startup>()
        //   .CaptureStartupErrors(true);

        //_server = new TestServer(hostBuilder);

        //_client = _server.CreateClient();
        //_client.BaseAddress = new Uri(hostBuilder.GetSetting("ApiBase"), UriKind.Absolute);

        
        #region IDisposable Support

        // To detect redundant calls
        //private bool disposedValue = false;

        //protected virtual void Dispose(bool disposing)
        //{
        //    if (!disposedValue)
        //    {
        //        if (disposing)
        //        {
        //            _client.Dispose();
        //            _server.Dispose();
        //        }

        //        // No unmanaged resources to free => no finalizer
        //        // set large fields to null.
        //        _client = null;
        //        _server = null;

        //        disposedValue = true;
        //    }
        //}


        //// This code added to correctly implement the disposable pattern.
        //public void Dispose()
        //{
        //    Dispose(true);
        //}

        #endregion
      ```
  - `System.Net.Http` issues

    `System.TypeLoadException`: [Inheritance security rules violated by type: 'System.Net.Http.WebRequestHandler'. Derived types must either match the security accessibility of the base type or be less accessible.](https://github.com/dotnet/corefx/issues/11100)
    
    [dependency on a library that uses `System.Net.Http`](https://github.com/dotnet/corefx/issues/11100#issuecomment-276066197)
    
    [direct dependency on types in `System.Net.Http`](https://github.com/dotnet/corefx/issues/11100#issuecomment-275960251)
    
    I had to:
    1. Package Manager Console for ASP.NET Core project over `net462`
```cmd
Update-Package System.Net.Http -Version 4.4.0-beta-24913-02 -Source https://dotnet.myget.org/F/dotnet-core
```
    2. Command line for ASP.NET Core project targetting `netcoreapp2.0`, `netstandard2.0`
```cmd
dotnet remove package System.Net.Http -v 4.3.3
dotnet add package System.Net.Http -v 4.4.0-beta-24913-02
```
    3. For a standard .Net csproj with .NET framework 4.6.2 removed:
```xml
<ItemGroup>
    <Reference Include="System.Net.Http">
      <HintPath>..\..\..\..\Program Files (x86)\Reference Assemblies\Microsoft\Framework\.NETFramework\v4.6.2\System.Net.Http.dll</HintPath>
    </Reference>
  </ItemGroup>
```

[<](call.md) | [<<](../rest.md) | [home](../../README.md)