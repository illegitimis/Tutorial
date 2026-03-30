---
title: "WebApi Upload & Download Files"
layout: default
nav_order: 13
parent: Web Services
last_modified_date: 2026-03-29 21:39:07 +00:00
---

# WebApi Upload & Download Files

- ASP.NET Web API file download service with resume support [1] _18 October 2012_ on ASP.NET Web API, ASP.NET, file download, HEAD verb, memory mapped files, Range, resume, Accept-Ranges
- More about REST: File upload download service with ASP.NET Web API and Windows Phone background file transfer [2] _ms blogs, 2012_ Custom Media-Type Formatter Sample, `BackgroundTransferRequest`, `PartialContent`, `BeginGetRequestStream`
- Download file from an ASP.NET Web API method using AngularJS [3] on SO, 2014
- download a file using web api in ASP.NET MVC 4 and jquery [4] on SO, 2012
- Android – Upload files to ASP.NET Web API service [5] `MultipartFormDataContent`, `IsMimeMultipartContent`
- Recent ASP.NET Web API Updates [6] _2012_, `PushStreamContent`, HTTP Chunked Encoding, `BufferedMediaTypeFormatter`
- Return file from ASP.NET 5 Web API [7] with a `System.Web.Mvc.FileResult`
  - `FileContentResult` [8] Sends the contents of a binary file to the response
  - `FileStreamResult` [9], Sends binary content to the response by using a Stream instance.
  - `FilePathResult` [10], Sends the contents of a file to the response.
  - PhysicalFileResult [11] `public class PhysicalFileResult : Microsoft.AspNetCore.Mvc.FileResult`. A `FileResult` on execution will write a file from disk to the response using mechanisms provided by the host.
  - `Microsoft.AspNetCore.Mvc.VirtualFileResult`. A `FileResult` that on execution writes the file specified using a virtual path to the response [12] using mechanisms provided by the host. IHostingEnvironment.WebRootFileProvider [13]
- Sample [14] uploading an XDocument using `PushStreamContent` and `HttpClient`. Description [15]
- HTTP Range Request Sample
  - Detailed Description [16]
  - Source Code [17]
- ASP.NET Core 2.0 MVC File Upload with MS SQL SERVER FileTable [18], _2015_ · by damienbod · in .NET, ASP.NET Core, ASPNET5, dotnet, Entity Framework, MVC, SQL, Web
- Web API File Upload, Single or Multiple files [19], _2014_ · by damienbod · in .NET, MVC, TopHeaderMenu, Web
- ASP.NETCore: Create a Web API application [20] _Nov 2016_

[1]: http://piotrwalat.net/file-download-service-with-resume-support-using-asp-net-web-api/
[2]: https://blogs.msdn.microsoft.com/codefx/2012/02/23/more-about-rest-file-upload-download-service-with-asp-net-web-api-and-windows-phone-background-file-transfer/
[3]: https://stackoverflow.com/questions/24080018/download-file-from-an-asp-net-web-api-method-using-angularjs
[4]: https://stackoverflow.com/questions/12975886/how-to-download-a-file-using-web-api-in-asp-net-mvc-4-and-jquery
[5]: http://hintdesk.com/android-upload-files-to-asp-net-web-api-service/
[6]: https://blogs.msdn.microsoft.com/henrikn/2012/04/23/recent-asp-net-web-api-updates-april-24/
[7]: https://stackoverflow.com/questions/34856983/return-file-from-asp-net-5-web-api
[8]: https://msdn.microsoft.com/en-us/library/system.web.mvc.filecontentresult(v=vs.118).aspx
[9]: https://msdn.microsoft.com/en-us/library/system.web.mvc.filestreamresult(v=vs.118).aspx
[10]: https://msdn.microsoft.com/en-us/library/system.web.mvc.filepathresult(v=vs.118).aspx
[11]: https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.physicalfileresult?view=aspnetcore-2.0
[12]: https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.virtualfileresult?view=aspnetcore-2.0
[13]: https://stackoverflow.com/a/35663207/2239678
[14]: http://aspnet.codeplex.com/sourcecontrol/latest#Samples/WebApi/UploadXDocumentSample/ReadMe.txt
[15]: https://blogs.msdn.microsoft.com/henrikn/2012/02/16/push-and-pull-streams-using-httpclient/
[16]: https://blogs.msdn.microsoft.com/webdev/2012/11/23/asp-net-web-api-and-http-byte-range-support/
[17]: http://aspnet.codeplex.com/sourcecontrol/latest#Samples/WebApi/HttpRangeRequestSample/ReadMe.txt
[18]: https://damienbod.com/2015/12/05/asp-net-5-mvc-6-file-upload-with-ms-sql-server-filetable/
[19]: https://damienbod.com/2014/03/28/web-api-file-upload-single-or-multiple-files/
[20]: https://social.technet.microsoft.com/wiki/contents/articles/36340.asp-netcore-create-a-web-api-application.aspx

[<](./index.md) | [<<](/index.md)
