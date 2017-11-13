# Web API

# Unvisited Queue / upload & download files
+ [ASP.NET Web API file download service with resume support](http://piotrwalat.net/file-download-service-with-resume-support-using-asp-net-web-api/)
   
   _18 October 2012_ on ASP.NET Web API, ASP.NET, file download, HEAD verb, memory mapped files, Range, resume, Accept-Ranges 
+ [More about REST: File upload download service with ASP.NET Web API and Windows Phone background file transfer](https://blogs.msdn.microsoft.com/codefx/2012/02/23/more-about-rest-file-upload-download-service-with-asp-net-web-api-and-windows-phone-background-file-transfer/)
  
  _ms blogs, 2012_ Custom Media-Type Formatter Sample, `BackgroundTransferRequest`, `PartialContent`, `BeginGetRequestStream`
+ [Download file from an ASP.NET Web API method using AngularJS](https://stackoverflow.com/questions/24080018/download-file-from-an-asp-net-web-api-method-using-angularjs) on SO, 2014
+ [download a file using web api in ASP.NET MVC 4 and jquery](https://stackoverflow.com/questions/12975886/how-to-download-a-file-using-web-api-in-asp-net-mvc-4-and-jquery) on SO, 2012

+ [Android – Upload files to ASP.NET Web API service](http://hintdesk.com/android-upload-files-to-asp-net-web-api-service/)
  
  `MultipartFormDataContent`, `IsMimeMultipartContent`
+ [Recent ASP.NET Web API Updates](https://blogs.msdn.microsoft.com/henrikn/2012/04/23/recent-asp-net-web-api-updates-april-24/)

  _2012_, `PushStreamContent`, HTTP Chunked Encoding, `BufferedMediaTypeFormatter`
+ [Return file from ASP.NET 5 Web API](https://stackoverflow.com/questions/34856983/return-file-from-asp-net-5-web-api) with a ` System.Web.Mvc.FileResult`
  - [`FileContentResult`](https://msdn.microsoft.com/en-us/library/system.web.mvc.filecontentresult(v=vs.118).aspx) Sends the contents of a binary file to the response
  - [`FileStreamResult`](https://msdn.microsoft.com/en-us/library/system.web.mvc.filestreamresult(v=vs.118).aspx), Sends binary content to the response by using a Stream instance.
  - [`FilePathResult`](https://msdn.microsoft.com/en-us/library/system.web.mvc.filepathresult(v=vs.118).aspx), Sends the contents of a file to the response.
  - [PhysicalFileResult](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.physicalfileresult?view=aspnetcore-2.0)

    `public class PhysicalFileResult : Microsoft.AspNetCore.Mvc.FileResult`
    
    A FileResult on execution will write a file from disk to the response using mechanisms provided by the host.
  - `Microsoft.AspNetCore.Mvc.VirtualFileResult` 
  
    A FileResult that on execution writes the file specified [using a virtual path to the response](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.virtualfileresult?view=aspnetcore-2.0) using mechanisms provided by the host.

    [`IHostingEnvironment.WebRootFileProvider`](https://stackoverflow.com/a/35663207/2239678)
+  [Sample](http://aspnet.codeplex.com/sourcecontrol/latest#Samples/WebApi/UploadXDocumentSample/ReadMe.txt) uploading an XDocument using `PushStreamContent` and `HttpClient`. [Description](https://blogs.msdn.microsoft.com/henrikn/2012/02/16/push-and-pull-streams-using-httpclient/)
+ HTTP Range Request Sample | [Detailed Description](https://blogs.msdn.microsoft.com/webdev/2012/11/23/asp-net-web-api-and-http-byte-range-support/) | [Source Code](http://aspnet.codeplex.com/sourcecontrol/latest#Samples/WebApi/HttpRangeRequestSample/ReadMe.txt) 
+ [ASP.NET Core 2.0 MVC File Upload with MS SQL SERVER FileTable](https://damienbod.com/2015/12/05/asp-net-5-mvc-6-file-upload-with-ms-sql-server-filetable/)

  _2015_ · by damienbod · in .NET, ASP.NET Core, ASPNET5, dotnet, Entity Framework, MVC, SQL, Web
+ [Web API File Upload, Single or Multiple files](https://damienbod.com/2014/03/28/web-api-file-upload-single-or-multiple-files/)

  _2014_ · by damienbod · in .NET, MVC, TopHeaderMenu, Web
+ [ASP.NETCore: Create a Web API application](https://social.technet.microsoft.com/wiki/contents/articles/36340.asp-netcore-create-a-web-api-application.aspx) _Nov 2016_