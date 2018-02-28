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
- It's going to look for requests that have the `If-Match` and `If-Not-Match`, and do the right thing, and it's going to look for the responses as they go out to Push them into the Cache, and Push those ETags in for us.
- this ETag is not only weak, but it's going to change every time the server Refreshes, or, more importantly what happens if it hits another load balance server.
- On rebuild, website restarted and therefore all that Cache and Memory was wiped.
- `CacheCow.Server.EntityTagStore.SqlServer` use a non-memory data store, something persistent, like SQL Server, RavenDB, Memcache, one of those different facilities for actually caching these responses.
- ``, `System.Configuration.`


[<](./webapi.md)
|
[<<](../REST.md)
|
[home](../README.md) 


  can't find the stored procedure named GetCache. 
  
  So, CacheCow implies that for the SQL Server version we're going to want to have a store procedure, actually a number of store procedures that are going to handle pushing and pulling into the database. It's using store procedures for speed, but at the end of the day, it's going to expect that it's going to have a couple of tables, as well as the store procedures exist in the database you're pointing at. How do we get them in there? Simply by using the cacheHandler it's not going to prebuild those tables and store procedures for you, much like you might expect from something like Entity Framework. Instead, and in my book a little odd, they've included the script. 
  
  Let's go ahead and Open this up in File Explorer, inside of the NuGet package. So, if we go to look at Packages, CacheCow, SQL Server, and then a folder called Scripts, there's going to be a SQL script. Let's go ahead and Open this in the editor of your choice. I'm going to use Sublime Text. So, I'm going to go ahead and Copy that out so I have it in my Clipboard, and now we're going to want to actually go over to the SQL Server Object Explorer, or you could do this at the command line, or really any way that you're used to dealing with the SQL Server, but this is the way I prefer. And, I'm going to go look for our database, and right in the database itself, I'm going to go ahead and issue a new query. There's our database, and I'm just going to Execute this code that came with CacheCow in order to put it in our database. The problem here is if you're storing it in some other server for actual production, you're going to need to repeat this process. So, part of your deployment strategy is going to be taking this and also executing it on the server. There isn't any real magic trick to make this work. You may want to put it in the initialization for Entity Framework. You may want to put it as part of Deployment Scripts, that's up to you. But, to get this to work, we're going to go ahead and just Execute it. It executed. I'm not going to bother saving it. And now if we come over here, and we Execute it again, we're going to now see that there's an ETag, but this ETag no longer has the weak prefix. Because this is stored in SQL Server, it knows it's more persistent, and so it's going to give you an ETag that's going to live for quite a while. So until this is cleaned up or timed out inside the Cache, and the way CacheCow works, you're ETag is going to be valid for quite a while. We can still go ahead and use that same value for the If-None-Match, and get our 304 because the object hasn't changed, or has not been modified. We're going to get that same behavior, but we're now storing it in a more persistent store. And more notably, when you're dealing with a server farm, or even a server garden, this is a good way to have Cache that's stored in sort of a central place. Now, this may feel a lot like having side effects of things like session state. So even though this Cache system does have some side effects on the server, the benefit of using Cached objects, and being able to test concurrency using that Cache, for me greatly outweigh the bending of the rule for a Stateless Server.