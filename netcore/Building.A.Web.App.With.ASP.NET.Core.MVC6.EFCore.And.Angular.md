# Building a Web App with ASP.NET Core, MVC 6, EF Core, and Angular

(todo) fix image links 

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
<img src="https://6ebaoa.by3302.livefilestore.com/y4mbc7XYRW0pYXbS3mKlUUxgKzbwpv2ScJAedJRPNIDB_IjwfywPhKGrjmfv4svxNEdn6oG37YzlTiKc3aaKmPuGVc7KtknIbzn-CQDGURHuEuGSy23Q9CT77VUQKAe_R7oAIM9urZd1P8TrMSQVYkfl1qofISrKPFxFoKQkALrjWZQp3LDDG84QroEdHTfY7dU9LzEG1Yhb--Rse9HGNF4yA?width=660&height=386&cropmode=none" alt="1" />
    </td>
  </tr>
  <tr>
    <td>
<img src="https://fpnjua.by3302.livefilestore.com/y4mKi3tB9cR_VhT8u70fc1Cr2spxqhXd7zArPnLkGCARCukVWCttPYQJcKCbTvZOyvOVHo3FGK4iifINb5NOay7oV45QBW7jwnws01ZTwAONknw-3xhp5RZljBiAZLKZwkfH29L_L87puRdQOyr-gHKxqeInRE-vbfSch5BXHsdvhrtEw0ZrFUkBC_1Vh-yJ99iV5AaXfa30sH8wjVVrBcclA?width=256&height=197&cropmode=none" alt="2" />	
    </td>
    <td>
<img src="https://slclww.by3302.livefilestore.com/y4mXUoEFTWhhF27mk3OFfnr-4AFwcK5YgjxUr79sn6h_b5Prp3cOP4jUesPgOBg56xDLpLlwL8YnGEvjTvxIZU4-1AqSmio_MM12R4Lm8e0WN8Bopmz40FB-zFnp2Ujgtg4VAfAj_urT_AGev7IZcD5qG8GAJcG_NX8hcycVcFk0f5QqKCP5_IIDHomSv95QeuZvgP0cKwV4h52pZNL5xM3yg?width=256&height=231&cropmode=none" alt="3" /> 	
	</td>
  </tr>
</table>

## ASP.NET Core

<table>
  <tr>
    <td colspan="2">
	<img src="https://g7ubqw.by3302.livefilestore.com/y4m_mJShBdpgbvSHZCazYWNvU1Pk-1Ih2raSXLpKK83Rjuytxpn94XQwe4H0m3miWLt-wDu6jyRNDQqlf_dsnFO28KWpkSH-qyfPtRCbIpnFBxrfqkjE_nBA6KAmxTtahY-i2klVIBMQGB0dhD0aGiuSKRjogJNxEocms-Ydm2gn7Kyt1onamn84ZveKUFLXzfh1XovN2CcOrMxEIv4fS4kpg?width=660&height=355&cropmode=none" alt="principles" />    
    </td>	
    <td colspan="2">
	<img src="https://hiqp5q.by3302.livefilestore.com/y4myUpNQ2rfkSjM65Ti8a2v2i4oDX5u7kX7JgJ2Nq-NTyYf_yVx9ZNdD7Iir4szxfoLeUhFz9b4t1QH-vP_xmeUwZXgx4GL8odsRYNT8zK9yRzmKFUNdryQ2u_g_yjD1br9mGeQfZ5RTiFs_NdRFxUAtiz58V18HEBP5X-eT4fr-SbqD_W8TUVgb5olZRM-aV7LdxlD95YLFbZbeogUnyDWbg?width=660&height=454&cropmode=none" alt="three frameworks" />      
    </td>
  </tr>
  
  <tr>
    <td colspan="2">
<img alt="completely composed" src="https://jxhueg.by3302.livefilestore.com/y4mATGvX7RSE_spEElHWWgo6j0ID4e-BGQsVquy2rw83OebFlBte5DkHEwePuikc75q3P5-xjqNXZjZ7I0SghO1Sy5mroSpY19vh1VXs5n8rC1RlLnA-yjIXhpW-5ce2Vv-zNePTI5ukjZh-50MjQNH7cZRN2ssr4aql5FKoADyRLu6r1M6GxNSABckIQNZ_KXBrE4nBAH2xabLLJKQn8DS7w?width=660&height=263&cropmode=none" />
    </td>
    <td colspan="2">
<img alt="open web" src="https://wowvtq.by3302.livefilestore.com/y4mC721cet5sjCqyDjvmKxO8uftfts1OCdiWE3T-YutvZQrJstXRNLfBiHCC-VXQM7T7nMyRdHRNN5u8XSCywxu3DNuEFeX144hAgBbe-KjJzcr24Z5XtXPfzqLzUX43N59Wc3k2cIpPfIyy4R4xm60gVSUkYaptP9ESyPJ6WGjoh6oaYLRFQwjgsFDeLb2ctxZSaMfXHrNqHea-p4KlQo1Gg?width=660&height=352&cropmode=none" width="660" height="352" />
    </td>
  </tr>
  
  <tr>
    <td colspan="4">   
<img ALT="OVERVIEW" src="https://6ebxoa.by3302.livefilestore.com/y4mTaHDPP9TjX288dohTvJZ9Q0hmYeCUqHIuEtIYRWLdSp9cPABwamWnh9GTLc7m58-NRUIg3zagEUE4mKSo-FFxGY7Qa5GA-weHumJ9FZLL0_YcacZKHNLBcg-0oDO-3B3jdtGvm0hsnZBWpIa9ks_gpXrUeSMITjJ5E0bR2Z4pqR-6PLa-xKOpqhd4KwntTd0CnPAWbUUbE3cpx9RUZOJDw?width=1024&height=442&cropmode=none" width="1024" height="442" />
    </td>    
  </tr>
  
  <tr>
    <td colspan="3">	
<img alt="new project" src="https://slciww.by3302.livefilestore.com/y4myljA9gw9YGeNKME513PQSHyNCBYmI8P1C40bvOyHUFslxC5tW1CYtAi32aUA-xc6GPSa4IoYMUl0-lWD_UjbWZ6PxazYn-rTxHK7CGLbWIwTwmqBz4mcz78rWx4q58oMSZcPPFFPorVAb9eCnBeMuqDMen-3Q3RBijfHJquN9_HSqTaULdA0gdFnOQJnxmng1Nw3HQt2hPRxaNlyErj__Q?width=512&height=128&cropmode=none" width="512" height="128" />
    </td>
	<td colspan="1" >
<img alt="CLR" src="https://fpngua.by3302.livefilestore.com/y4mhRs7yoqpBlW7yhLAj0d2aj9qNugs4BwYcFLrIkC8YIWKCCroi96_Y-73CZqdw7fwZs_n8MjEIvmYN-6v0oocWuoGqrtNBL9BlZhJMlb9jNdBb_wnPpI_q8UgsU7qgcVagoeW71jvKRuk3qdU5Ms0FnuzvdEgnpkz3kcy9rWaH0sFkaUKu3J-hCgPsGiffH4oWjfTbVDi-Xwpijhfzs5RaQ?width=256&height=96&cropmode=none" width="256" height="96" />
    </td>    
  </tr>
  
  <tr>    
    <td rowspan="2">
<img alt="sln explorer" src="https://uz5nia.by3302.livefilestore.com/y4mIa4uXH2tM0bF3Fc2VCbqOOajnLfQg14Dqca8tFvJjwout4RbMDZJ3X-DYPpOBSWXamsgcpJKQtXwWXT7gXj-DZ43gvIFSedzPC85-Y6c2OFE5tt_3bR0T4e4mJ9gy_jQJXsxlv5NhOKyK15ycfvkW-cgMQ0vNKiFkCs7gwUO_sO5m2nxbtgq228jxG391Kd8oh2xHaMVffrdpSH7ZCj7Yg?width=113&height=256&cropmode=none" width="113" height="256" />
    </td>  
    <td rowspan="2" colspan="3">
<img alt="program" src="https://vbp1kg.by3302.livefilestore.com/y4m2oMGxnV09Bzk_iyjuSYpBSDbulZYXgYleKo_DnCby9wWdFdarriGc6JohaqcvapoWp0Z4dDFPTM7Sj4L8eBGv6e7izW4BBp4PpnxI3-7kqM5is2Alj2fWYLVLNHDlZUmIqK54NAhhCGsFOP-6BA0YRMu94On13WINtUCpT-iJMiS933auXvRIdV39E116jQvJMcdLPE-JPtbrx5vjS0geQ?width=660&height=391&cropmode=none" width="660" height="391" />
    </td>
  </tr>
  
  <tr></tr>
  
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

new  


### new  project  options

web fwk | os fwk | title
--- | --- | ---
ASP.NET | .NET Framework 4.5-4.7| ASP.NET WebForms, MVC, WebAPI, classic
ASP.NET Core | .NET Core | ASP.NET Core web app **multiplatform**
ASP.NET Core | .NET Framework | ASP.NET Core web app for **Windows**

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


[<<](../netcore.md)
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 
