# Building a Web App with ASP.NET Core, MVC 6, EF Core, and Angular

## TOC
- [Intro](https://github.com/illegitimis/Tutorial/blob/v10/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#intro)
- [ASP.NET Core](https://github.com/illegitimis/Tutorial/blob/v10/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#aspnet-core)
- [HTML and CSS Basics](https://github.com/illegitimis/Tutorial/blob/v10/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#html-and-css-basics)
- [JavaScript](https://github.com/illegitimis/Tutorial/blob/v10/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#javascript)
- [MVC 6](https://github.com/illegitimis/Tutorial/blob/v10/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#mvc-6)
- [Bootstrap](https://github.com/illegitimis/Tutorial/blob/v10/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#bootstrap)
- [EF Core](https://github.com/illegitimis/Tutorial/blob/v10/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#ef-core)
- [Creating the API](https://github.com/illegitimis/Tutorial/blob/v10/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#creating-the-api)
- [AngularJS](https://github.com/illegitimis/Tutorial/blob/v10/Building.A.Web.App.With.ASP.NET.Core.MVC6.EFCore.And.Angular.md#angularjs)

## Intro

<table>
  <tr>
    <td colspan="2">
      <img src="https://6ebaoa.by3302.livefilestore.com/y3mbc7XYRW0pYXbS3mKlUUxgGO2s121EBJwx7KzgUeOv4oOPTD7SBEP6Rmmrv07ZPm-sflblPse3dvuTVOBYhE7lwEfEw01JDxCVEhS2pftkhReBkQBxmclM4r-1zcLBnYM6Prn5gJjWwwvmPNUSJoE9casyiSNFDJE4nMw3gw_y20?width=490&height=287&cropmode=none" alt="1" />
    </td>
  </tr>
  <tr>
    <td>
    <img src="https://fpnjua.by3302.livefilestore.com/y3mKi3tB9cR_VhT8u70fc1Cry9u3ZDNZa9I6x78R5ThTSfRd-9s-z1o79XWkGSoKoUP80yJ0VS-_UHdXoM9S3pubHfn-t2rVH55oR8lGwsQQrqPX8vBuWNifOnamF-b8mRUYxwg60ZeHPL-8YZFdoZr5uDnhngJiZ49mQl7-ILHsVY?width=364&height=280&cropmode=none" alt="2" />
    </td>
    <td>
    <img src="https://slclww.by3302.livefilestore.com/y3mXUoEFTWhhF27mk3OFfnr-w9BgW9ydGhphPz6V8XBoRaMsoDuKQla8MsPF69g2YKCN47OIJfkflRfO92KDT8WvudrTsafe1sIo_JUmV1Q5XpwRajxrPpaCrahuqxSiweZbbEkLEFYcJCwFKKhFA5BFvoIZkrFbaFHZoinEi2cdnU?width=314&height=282&cropmode=none" alt="3" />
    </td>
  </tr>
</table>

## ASP.NET Core

<table>
  <tr>
    <td colspan="2">
      <img src="https://g7ubqw.by3302.livefilestore.com/y3m_mJShBdpgbvSHZCazYWNveR_CVTkhyolPusSYOB1bA034XA54sIVPQJqp0I1XqPAR5SfCUV0OvF0LKx_Fsobj-7B0O3_hMMQd4JQQnlyMG3yoEz0tqj6HmCdXEUQe33GIclMGLIAEwf0HIrWPCxetIH-Wczrv1vCj38tArNMcLs?width=669&height=360&cropmode=none" alt="1" />
    </td>
    <td colspan="2">
      <img src="https://hiqp5q.by3302.livefilestore.com/y3myUpNQ2rfkSjM65Ti8a2v2gj-3qe76eDHaO_BTCyvgCUki89f6QWubGQbnZWuz2gTfYERg4mNCmVLjURMWv6HEerg8yDaTrnZzgvK_e6FeVa5otRbkMSaQ-ilMMoT5_Vdqu8ZYRUEBaSNvmZtunBUeR5FK36Ea01x88L3rOjV9kM?width=539&height=371&cropmode=none" alt="2" />
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <img src="https://jxhueg.by3302.livefilestore.com/y3mATGvX7RSE_spEElHWWgo6rnGH_kT5OQeTcGNPUaWBVIFMXCFkYVwgvGV3n5XdU-Fe25AYQO10Np-n955BFfOgHezXuhfbeOsy-fu1i6eUDceksm4SK3qFLrZd763oIC8R4JfcDVGv26aLyz6zZGzspwVpl93EeIq8oIkurEshwQ?width=661&height=264&cropmode=none" alt="3" />
    </td>
    <td colspan="2">
      <img src="https://wowvtq.by3302.livefilestore.com/y3mC721cet5sjCqyDjvmKxO8rDzsjQJnLOT4HVg1LT-Dj8OvLuoxU5aHVWyKxvZ6f2liPwEXZE40Bkd83N8RHJ6qpqaqdcMi4NWvnZolnBZIn29VkFIjaJqD17ATVxIKj4H6h7Hea-MX8A6CLUm1zqyeUQVLr4WG55KdzCsrNVTJAk?width=639&height=341&cropmode=none" alt="4" />
    </td>
  </tr>
  <tr>
    <td colspan="4">
      <img src="https://tcyvqq.by3302.livefilestore.com/y3mgVk7kAGI6FjFxLqcN279AR83dnKYEw2_5JZdkj82iqiUBW-1b8TqUKc8WR8gfdSA_RTghc8Mag-o8CMKSjMxWOwTqio5bfx_gvlL7ENAujfj4u3HHmDAqh5yNi1AezgIPR6wlJXhVbZntyznNzS7yYdRBTld7cWmFog7UgbYxjo?width=637&height=377&cropmode=none" alt="5" />
    </td>    
  </tr>
  <tr>
    <td colspan="4">
      <img src="https://6ebxoa.by3302.livefilestore.com/y3mTaHDPP9TjX288dohTvJZ9adf09kMOEN9mypVfJrNQotnZH2sNBPSZmtt92ZbsJaMMweeev37lwaAwMNr5OkQAr8EsSTYo7bL5O_qMX0Mv-1tzB76qAWivWkF9zPFqThHtTT1VazudsWn-fgddZQPL2Tq-jDvZ_ksN5ZdkA4B92Y?width=960&height=414&cropmode=none" alt="6" />
    </td>
  </tr>
  <tr>
    <td colspan="3" >
      <img src="https://fpngua.by3302.livefilestore.com/y3mhRs7yoqpBlW7yhLAj0d2apCmXBi54zSgylhiwfOXzRTZCyZwN57ERvKmXyeKPnTKS6jt-zLjpw87xe_G8NkVtUUSeL05ENbB8ZS-KOpo6U02ZWuRjnO6g92_8LYyTTZ2PYHcYnoQHCCiMnNNv2xnDLk0ZCQTlbyvRwL6wIo2jhs?width=440&height=414&cropmode=none" alt="7" />
    </td>    
    <td rowspan="2">
      <img src="https://uz5nia.by3302.livefilestore.com/y3mIa4uXH2tM0bF3Fc2VCbqOMEIy1XT8StM0aZZxIcGIvXr3DIZ0h2c33UQx8j-Q7kQ6M4jn6wuboyXhlNoaW_qj4lCLpAQ20OUfzHBBsWdbHOdLL9qpSEm55tJdnm6LA7hY-iUzKK4Toh-fDO1HcIeMHrHAk9Cd8I5FeFDutPtNF8?width=161&height=365&cropmode=none" alt="9" />
    </td>
  </tr>
  <tr>
    <td colspan="3">
      <img src="https://slciww.by3302.livefilestore.com/y3myljA9gw9YGeNKME513PQSH4anG9tfSEOWd1qFyNo4bjiD74S_pfAPjCwFrSA5CPLl_Ue17bcyBc9F19aa5qMJb3XBSkM5tokkP7nIbVMmTkWleVqAOEkB8Tpth0KfcpX8ncPVdcVksiRdwXVSJfMVd9CLE38vsPiE56aC_h4u4s?width=440&height=109&cropmode=none" alt="8" />
    </td>
  </tr>
</table>

For yeoman, node and npm must be installed, nodejs.org. The command line VS code hello world app has .xproj extension for the project.

```cmd
 code . 
 node -- version 
 npm -- version 
 npm install yo -g
 yo
 cls
 npm install generator-* (aspnet) -g
 yo aspnet
```

new project options
- 452 -> web -> asp.net core web app (.net core) 
- 452 -> web -> asp.net web app (.net fwk) 
- 452 -> .net core -> asp.net core web app (.net core)

## HTML and CSS Basics

![](https://uz5qia.by3302.livefilestore.com/y3mUV4VSA2B8vDntS_hAwdc4g-UFT5LFic4KkwfGip83DYtdzxHrvRk30etvQU8buYkOIS7oI3V3-etYp_01181vqBYGTHYL4KYXboOpFFqikFHwaSw3KTdy7zEDRHSLtbLA2m35YT2eiGQiFRbQQASzJMRGAuMnYOt5Wk7dpVQ-KM?width=408&height=172&cropmode=none)

Start Without Debugging - *ctrl + f5*. create new file - *shift + f2*. Content below named middleware. 

```cs
    public void Configure (IApplicationBuilder app) {
        app.Run ( async (ctx) => { await ctx.Response.WriteAsync ("some html"); }); 
    } 
```

Move static html to **www root** folder, similar to the way that Node and Ruby and Rails and even JSP Pages handles it. In ASP.NET Core, _every feature_ of the web server is **optional**. 
This piece of middleware is called `app.UseDefaultFiles()`. This will add some standard default files so that when looking in a directory, and that includes the root folder of your project, that it's going to automatically look for an index.html. 
Package `Microsoft.AspNetCore.StaticFiles` must be added.

![](https://vbp4kg.by3302.livefilestore.com/y3mLO9GLQ-A5sRP0_dnJbYC69_euaHpfqZUQHJCfM2GyY1z3dXsEOD7D6sWuL_-PxWodBvILgLPIeTKUh3H6dSI4XgdovvQkxJj6xsWf4A72xbkkrK7uNrPzw1dwfk1yE_L0_FrExXGKc_QHu154iI9zmXLfcildPn1LLHO7dpDWCY?width=937&height=234&cropmode=none)

[Web Essentials 2013](http://vswebessentials.com/) has a Surround with tag... feature (**Alt+Shift+W**) that is more fluid than the built-in Surround with.

overriding input buttons, default is text `input[type=submit] {width: auto;}`

overriding input tags `input[type=text], input[type=password], textarea {width: 150px;}`

by default a label is inline, this will move to the row below `label {display: block;}`

images inside sidebar div `#sidebar img {max-width: 50px;}`, 
instead provide a class for the small images `.headshot {max-width: 50px;}`

active list items under menu are bold `.menu li {list-style-type: none;} .menu li.active {font-weight: bold;}`

**the box model**

![](https://g7xpqg.by3302.livefilestore.com/y3mOEee-RY1i694_H7jb3vb-ErefywwjesKLjsz7w5TpwIA5bMJDNhhNsYXqA3IryvNaJ40UT73Wl8fEkVukICowLAIpx2W8tvg8qjA_yYnxN2aAbsS5e-B2SLax8E-MOjSqQarjrafF9nfj2NYgkTskCdTYnQcPUE3fmwZIi92Jag?width=612&height=347&cropmode=none)

create a sidebar and a wrapper div over main and footer
```css
    #sidebar {margin: 0; position: fixed; overflow: hidden; height:100%; width: 200px; left:0;}
    #wrapper {margin: 0 0 0 200px;}
    #footer {bottom: 0; width: 100%;}
```

## JavaScript

- The client side language for web apps
- object oriented
- prototypical inheritance instead of classes
- dynamically typed
- just in time compiled without an intermediate format, like MSIL or Bytecode
- older browsers have an interpreter instead of JIT
- place scripts before the end of the body tag, executes as html is parsed

events / anonymous function / callback 
```js
    var main = document.getElementById("main");
    main.onmouseenter = function () { main.style.backgroundcolor = "#ddd"; };
    main.onmouseleave = function () { main.style.backgroundcolor = ""; main.style = "background: #eee"; };
```

**global scope**, as files are loaded they may overwrite variables, avoid name collisions. 
Either use very specific names, or use function private scope. 
The function name though may be leaking other function names, **immediately executing nameless function**.  `(function(){})();`

**Bower** is for js what NuGet is for cs, client side package management. 
Add _Bower configuration file_, dependencies download to a lib folder in wwroot. .bowerrc is the config options for bower. 

JQuery handles the cross-browser compatibility issues.
`<script type="text/javascript" src="lib/jquery/dist/jquery.min.js"></script>`
```js
    $('#username').text("was innerHtml or InnerHTML");
    $(#main).on("mouseenter", function() {main.style = ""} );
    var menuItems = $("ul.menu li a");
    menuItems.on("click", function(){ alert($(this).text()); });
```

div, sidebar toggle visibility button, wrapped set of DOM elements
```js
    var hscn = "hide-sidebar";
    $("#sidebar-toggle").on("click", function () {
        var sw = $("#sidebar,#wrapper");        
        sw.toggleClass(hscn);
        if (sw.hasClass(hscn)) {
            $(this).text("show sidebar");
        } else {
            $(this).text("hide sidebar");            
        }
    });
```    

On the css side `#sidebar.hide-sidebar {left: -250px;}` downside is tracking const values, 
and `#wrapper.hide-sidebar {margin-left: 0;}`. Can add a `transition: left ease .25s;` and `transition: margin-left ease .25s;`. 
Also add vendor specifics. 

## MVC 6

![](https://hiqm5q.by3302.livefilestore.com/y3m_AmgE7r9P2-ICcLcwrLCE1D9YaGaACjIAVAh81hdYMCPHoXqr1XMvGh__NdOIkPbRww5qAjVq9vZKpfDL_yTQ6UEulOJdo5e9463y0MCbZUhVxikCxttrcKlx_rPyrox5ghZvdS8op0g04d1NtDeyd00nO0d2r3oCzR9Ojeys4E?width=437&height=138&cropmode=none)

Add package `_Microsoft.AspNet.Mvc.ViewFeatures_` for resolving the `Controller` class. That's just a subset of MVC, so better edit `project.json` to add a dependency for `Microsoft.AspNetCore.Mvc`, then add a using namespace. `public IActionResult Index() {return View(); }`. Add a cshtml view for the index `@{ ViewBag.Title = ""}`. In Startup.cs, enable MVC6. 
```cs
    public void Configure (IApplicationBuilder app)  { 
        app.UseStaticFiles(); 
        app.UseMvc(cfg=>{ 
            cfg.MapRoute(name: "Default", template: "{controller}/{action}/{id?}"), 
                defaults: new {controller="App", action="Index"} ); 
        });
    }
    public void ConfigureServices (IServiceCollection services)  { 
        services.AddMvc(); 
    }
```
Add a _MVC View layout page_ as Views\Shared\_Layout.cshtml. The sidebar, header and footer from index will be moved to the shared layout. Then link the layout to the Razor index view as `@{Layout="Layout.cshtml"}`. Add _MVC View Start Page_ as ViewStart.cshtml in the actual views folder. This will isolate the layout include boilerplate. Obviously, paths to css and js will have to be revised as to site root as **~**. Also use `@RenderBody()` in the layout.


Add `app.UseDeveloperExceptionPage()` in Startup.Configure, diagnostics include stack trace, want to hide that from end users, keep it for staging and test servers, instead of `#if DEBUG`, add the `IHostingEnvironment` parameter and check `env.IsProduction()` or `env.IsEnvironment("Development")`. Project properties has environment variables defined, like `ASPNETCORE_ENVIRONMENT`. 

Use **tag helpers** to modify hrefs for main menu, from `<a href="/app/about">About</a>` to something like `<a asp-controller="App" asp-action="About">About</a>`, will generate hrefs programatically while rendering on the server. To enable tag helpers, add a dependency to `Microsoft.AspNet.Mvc.TagHelpers`. Wire it up in _layout.cshtml as `@inject IHostingEnvironment env` or add a _MVC View Imports Page_. `@addTagHelper "*, Microsoft.AspNet.Mvc.TagHelpers"` this will inject tag helpers into all the views needed. Also include common namespaces like `@using ProjectNS.Models`. 

View models. ![](https://jxhreg.by3302.livefilestore.com/y3m_ly-zrpRO_F8uUtQD9BzvOYZi5bddu_KW1cAVLVh1a6-AkKS6s22JQhh3_yYycFDOuf8v0dBps4fjAhtHkz-9OreUSfBSco6IfXBV50-p6l2sAzk3FRBXFAIQBbwmeqZBaNxxjyYpEkaJpo8gX_046d1Wkb8BYOqgzhJdTiYGUM?width=483&height=285&cropmode=none)

Validation attributes. `[Required]`, [[`StringLength`](https://msdn.microsoft.com/en-us/library/system.componentmodel.dataannotations.stringlengthattribute(v=vs.110).aspx)`(MinimumLength=10,MaximumLength=4096)]`. Also add `jquery-validation: "~1.15.0"` and `jquery-validation-unobtrusive: "~3.2.6"` to `bower.json`. Add `@RenderSection("scripts", false)` in the layout. In the contacts page define the scripts section, and use it like `<span asp-validation-for="Name" />` and `<span asp-validation-summary="ModelOnly"></span>`.
```htm
    @section scripts {
        <script src="~/lib/jquery-validation/dist/jquery.validate.min.js"></script>
        <script src="~/lib/jquery-validation-unobtrusive/dist/jquery.validate.unobtrusive.min.js"></script>
    }
```

_Posts_. `<form method="post">`. Add `[HttpPost]` with a `ContactViewModel` parameter, model binding is automatic through the controller. Services/IMailService.cs. Implement a mock debug object for the service interface. `Debug.WriteLine($"Send mail to {to} from {from} with subject {subject} and body {body}");`. 

Use _dependency injection_ for service implementation. Add _constructor_ to `AppController`. Call the service on the post action. Activation in Startup `ConfigureServices`: `services.AddTransient<IMailService, DebugMailService>();` or `services.AddScoped<IMailService, MockMailService>();`. **Transient** creates on the fly and caches it. **Scoped** creates one for each set of requests. Add a `IHostingEnvironment` parameter to the `Startup` constructor. 
`var builder = new ConfigurationBuilder().SetBasePath(_env.ContentRootPath).AddJsonFile("config.json").AddEnvironmentVariables(); _config = builder.Build();` returns an `IConfigurationRoute`, a sort of name value bag, like `_config[MailSettings:ToAddress]`. `services.AddSingleton(_config);`. State of the data passed into the view, `ModelState.IsValid`, `ModelState.AddModelError("Email","Message")`, 'ModelState.Clear()' upon successful post. 

## Bootstrap

+ open source fwk for web apps
+ composed of CSS and LESS, LESS is a language for writing program-like facilities in CSS
+ includes JavaScript components to help you do some common features like carousels, styling of buttons
+ modular and skinnable which means you can use the components you want out of Bootstrap, as well as being able to change the way that Bootstrap looks and feels
+ help you solve the 80% of common design metaphors you're going to see in your web applications. So a bar for navigation through the website, breadcrumbs, panels, thumbnail images

VS add Bootstrap dependency in `bower.json`. Link `bootstrap.min.css` stylesheet site wide and the minified js also. Also `"font-awesome": "~4.4.0"`. Toggle arrow left `<i class="glyphicon glyphicon-chevron-left"></i>`. Refactor to `<i class="fa fa-angle-left"></i>`. Change impl in `site.js` for the auto function hide/show.

_Bootswatch_ is a list of templates that modify look and feel over Bootstrap. Another bower call, `"bootswatch": "3.3.5+2"`, Bootswatch v2 over the Bootstrap release. `<link rel="stylesheet" href="~/lib/bootswatch/spacelab/bootstrap.min.css" />`.
Navbar: Move `menu` class to `nav` in the sidebar section. `<nav class="navbar navbar-inverse">` over `<button id="sidebarToggle">`. If bar contains a list, style as `<ul class="nav navbar-nav navbar-left">`. 

Default font icon buttons. ![](https://wowstq.by3302.livefilestore.com/y3moDvLNKlEe1vihz_sPW3VS78Ex94xXfKa3BKPt1V1GtbQ82juUxmwZoiVwUWrWEv4JwvtcZy6s2iKR6aZiu02aPN8h1tDuJ1qW7RRarOUKYXa8xTF3GGJU18SEY870_ypftX2EP23cnkpvkRhFmRpQs9X3MFr-D8ZkCHXMOutnU4?width=428&height=317&cropmode=none)

Bootstrap grid system is a world of 12 columns. The label and input group is a form-group and decorate the active ctrl with form-control. ![](https://tcywqq.by3302.livefilestore.com/y3miWlkRKVk5Sq5zubKHWUHsHMnJJlTPD9_SDBno3T1hLj2B16MEuS800Rly16Yv-gzDIcLdH_nJygj0KaYRpDEntmh7KVs3DcvHNn5VU7PUy8lsnCnyXWCqMjbs-jsEYgOKRTosTce_Qtjy8Qoz7-JzQfaDcOjSx5azs1BH8-jrj0?width=660&height=122&cropmode=none)

Bootstrap 4. alpha phase in sep 2015. modest change compared to 2 to 3 transition. Card replaces Panels and Thumbnails.

## EF Core

+ build data access without the requirement on relational databases?
+ EF6 will work if you need maturity, work in progress
+ use migrations to build the db for you
+ seeding not built-in, but easily doable
+ repository pattern for testable data access

_Models_ folder has dtos, in comparison with the _ViewModels_ folder. Code first, auto implemented property only classes. Use `ICollection` instead of read-only `IEnumerable` objects. Access to the db, derive from `EFCore.DbContext`. For entities, use `DbSet<TEntity>`. Add `services.AddDbContext<CustomContext>();` in `ConfigureServices`. Additional parameter for controller constructor is the db context. database provider must be configured, override `DbContext.OnConfiguring` by calling `base` and `optionsBuilder.UseSqlServer(_config["CS:CONN"]);`.


![](https://6ebyoa.by3302.livefilestore.com/y3mY_5i27ejOmhEw0k_zx0tO0qeVwEtY2n_H-IeHtt3H-_Mbxi2JfVHG9AZ5Cl8f9I9QuwR9SypC-9crnv3HQ7z1uvRGFzy6WkJG6mz7ZFPu2uoLuzBU8JiG6ecUoxMs-FRrfnMQQVdVwVmlMScg4_o-GHaBrpBOk6Sslu2MCV0YMU?width=594&height=450&cropmode=none)

_alt+space_ opens up a console window. `dotnet ef migrations add InitialDatabase`. A new folder appears, `Migrations`. Or `dotnet database ef update` to create the schema. To add sample data, add a `ContextSeedData` db ctx wrapper, with `async Task Ensure() { if(!_ctx.Trips.Any())  {CrUd();}  }`. `services.AddTransient<ContextSeedData>();`, have to explictly call in Configure, `param.EnsureSeedData().Wait()`. 

[Demo repo](http://github.com/shawnwildermuth/BuildingWebASPNETCore).

Repository. `services.AddScoped<WorldRepository, IWorldRepository>();`. Every time a custom context instance is used as a parameter, replace with the repository interface. `services.AddLogging()` and `ILoggerFactory.AddDebug(LogLevel.Information)`. In the controller constructor add `MS.Extentions.ILogger<TController>`.

## Creating the API

_return json_ in a controller 
```cs
    [HttpGet("api/trips")]
    public JsonResult Get() { return Json (new Trip() { Name = "Some trip" }); }
```
get _errors_ too 
```cs
    [HttpGet("api/trips")]
    public IActionResult Get() { 
        // return BadRequest ("404");
        // return Ok (new Trip() { Name = "Some trip" }); 
        //return Ok (_repo.GetAllTrips());
        return Ok(Mapper.Map<IEnumerable<TripViewModel>>(results));
    }
 ```
 
Rest Client: [postman](http://getpostman.com).

Move from Pascal to Camel casing
```cs
    services.AddMvc()
        .AddJsonOptions (config => config.SerializerSettings.ContractResolver = new CamelCasePropertyNamesContractResolver());
```
_post with object model bind_, one can add default class route for controller `[Route("api/trips")]` at class level.  
```cs
    [HttpPost("api/trips")]
    // public IActionResult Post ([FromBody] Trip t) { 
    public IActionResult Post ([FromBody] TripViewModel tvm) { 
        var t = Mapper.Map<Trip>(tvm);
        if (ModelState.IsValid) return Created ($"api/trips/{t.Name}", t);
        return BadRequest (t.Name);
    }
```
Add validation attributes to the model data classes / view model classes, `[Required]`, `[StringLength]`. 

**AutoMapper**. Add package to `project.json`. Initialize this in _Configure_, and use it like above.
```cs
    Mapper.Initialize (config => config.CreateMap<TripViewModel, Trip>() );
```
try-ok-catch-log-badrequest. use a `ILogger<TController>`. 

## AngularJS
+ supplies services usable throughout your project
+ add anjular 1.5.7 to bower.json 
+ include in a cshtml view `@section Scripts {<script src="~/lib/angular/angular.min.js"></script>}`
+ NG app attribute `data-ng-*` and `ng-*`, e.g. `<div class="row" ng-app="app-trips" />`
+ evaluate expressions `<div> {{ 1+2 }} </div>`
+ code written in app-controller.js ![](https://hiqk5q.by3302.livefilestore.com/y4mdGJ1ZYH7959oBhZahhETy8vaYGgO6a3Iag_5otBbSB_K7HKnoF2t7XIx9A3SffDyU_ie-IK3jG-cLmCG8IuwYF5p0D7ftsczznGbIQ_JgbD8WKU6WSZYTXuq3AFiFYU23zhgpZ8SzlZk0YBhzyC9bvl33HgcFQZhi3HOdGgLVd4vWLtHcNUvQ6egPYe84VBbe0FVnW5PbRo_4jcxPmpvwA?width=487&height=378&cropmode=none) , use it like `<div ng-controller="tripsController as vm">{{vm.name}}</div>`.
+ table ->` tr ng-repeat="t in vm.trips"` -> `td {{t.created | date:'yyyy-MM-dd'}}`
