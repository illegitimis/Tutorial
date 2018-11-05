**Angular Fundamentals** Pluralsight course wiki page

# Links

+ Pluralsight [Course page](https://app.pluralsight.com/library/courses/angularjs-fundamentals/)
+ [Files](https://github.com/joeeames/AngularFundamentalsFiles) from course creator
+ Built for version 1.0.5 and **updated for 1.4**. [Course on Angular 1.5 components](https://app.pluralsight.com/library/courses/building-components-angular-1-5/table-of-contents) is an update
+ ['Angular 2: First Look' course](https://app.pluralsight.com/library/courses/angular-2-first-look/table-of-contents)

# TOC
1. [Intro](https://github.com/illegitimis/Tutorial/blob/v10/AngularFundamentals.md#intro)
2. [Controllers & Markup](https://github.com/illegitimis/Tutorial/blob/v10/AngularFundamentals.md#controllers--markup)
3. [Creating & Using Angular Services](https://github.com/illegitimis/Tutorial/blob/v10/AngularFundamentals.md#services)

# Intro

## Course Introduction

Client-side JavaScript used to be simple enough that we could get away with very little thought as to the structure of our JavaScript, but as our web applications have become bigger and bigger, we need something to reign in all the resulting complexity. **AngularJS allows us to toss out all that client-side spaghetti code and write simple and elegant MVC-style single-page applications**. In module 1, I'll show you how simple it is to get your project bootstrapped with Angular and how to start working with Angular markup. Then, in module 2 I'll show you how to start _organizing that code into controllers_ and how to use the _built-in directives_ to _control your view_. Then I'll jump in, and in module 3 I'll show you how to _abstract some of the complexity out of your controllers and into services_ to **facilitate** the **single responsibility principle** and make testing easier. After talking about services, I'll show you in module 4 how to use routing to turn your app into a true single-page app, and I'll demonstrate all the built-in power and functionality that comes with Angular routing. And finally, in module 5, I'll talk about one of the most exciting and powerful pieces of AngularJS, directives. I'll demonstrate how you can use AngularJS directives to create your own custom elements, observe changes, and handle events. And last, but certainly not least, I will jump back in and show you how the Angular team has designed AngularJS to allow you to do all this in a fully test-driven way. I'll demonstrate how to test your controllers, services, and directives, and even how to do full end to end UI testing.

## Introduction to Angular

So what is Angular and why would you want to use it? The simplest answer to that question is that Angular is a **JavaScript library**, but it's so much more than that. It's probably more accurate to categorize it as an **MV* framework**. If saying that doesn't tell us everything about it, at least we have some context since we can compare and contrast it to some other popular MV* frameworks, such as **Knockout** or **Backbone**. Although we won't really make any direct comparisons to other MV* frameworks, we will discuss things it has in common with other frameworks, and the things that set it apart from the crowd. Angular isn't just an MV* framework, it's an **opinionated MV* framework**. What is opinionated software? Well, _opinionated software guides you into certain ways of doing things_. Opinionated software has a _vision_. It may limit itself to solving fewer problems, but generally, software with opinions solves those problems with less fuss. That doesn't mean that there isn't more than one way to solve a problem with Angular. For example, take DOM manipulation. _Angular wants you to_ **only** _manipulate your DOM inside of directives_, but with Angular inside of a directive you can use jQuery, Zepto, any other library, or even just raw JavaScript, to manipulate your DOM. That doesn't mean that you can't manipulate the DOM from within any other piece of an Angular application, but Angular definitely has an opinion about whether or not you should, and it gently guides you into doing things a certain way. So why should you use opinionated software? There are many reasons. At first glance it may seem like a lack of freedom is a bad thing, but that's really not true. The guys at 37signals, the company which invented Ruby on Rails, have written [a great article on the benefits of opinionated software](https://gettingreal.37signals.com/ch04_Make_Opinionated_Software.php). In essence, they say, the best software has a vision, the best software takes sides. This is quite true. You will find that using opinionated software will make it faster to do things that fall within the vision of the software. When it comes to Angular, that vision is extremely broad. It is well-suited to building anything from line-of-business applications to video players. In fact, if you are watching this video on your computer, then you are using an Angular application. But first, let's make sure that we understand exactly what an MV* framework is. The M in MV* stands for Model. **The model is where you store the data and state of your application**. The V in MV* stands for View. **The view is where you actually render to the user** the information that you want them to see, and the view is where your receive input from the user. The * in MV* stands for, well, something else. In many common MV* frameworks, the * is either a **controller**, or a **presenter**, or a **ViewModel**, or even something different besides those three. In fact, some frameworks even allow you to choose one of those three, and don't necessarily prescribe which one. Now you may be asking yourself, which one of those does Angular use? Well, **Angular uses a controller**. So some people may call Angular an MVC framework that would definitely be true, but in the web world there are so many frameworks that fall within this categorization, but don't necessarily fit into just MVC, that this term MV* is commonly used. Angular is an _open source library_ built by the folks at _Google_. This gives us the best of both worlds. It is maintained by a team of highly-skilled professionals whose employment is based around building Angular. That means that you won't have to worry about it stagnating because the primary contributors get bored or busy, but because it's open source, it can benefit from the contributions of the entire JavaScript community. In fact, at the time of this recording, Angular has over 100 unique contributors to its GitHub repository. Angular is also comprehensive. What makes Angular comprehensive? Let's take a look at a diagram. Angular **handles the Ajax communication with your server** so that you can _both send and receive_ data from your backend. This data is **stored as plain JavaScript objects**, so you won't have to make any special calls like get and set when you to update your data. Angular handles showing that data on the page, which you can do using **partial templates** or just _modify the HTML DOM that already exists_. Angular also **handles updating the data or model based on user interaction**, so when a user types into a text field, that new value can automatically be copied into your model. You don't have to wait for certain events, you can just tell Angular that a certain textbox owns a certain piece of data, and it will keep them in sync. This feature is called **two-way binding**. And lastly, Angular handles routing, or moving from one view to another. This is the key piece in building single-age applications or SPAs. This way you can completely change your view based on user interaction with your page. Angular will also update the URL in the browser so that the new view can be bookmarked for later. The next important aspect of Angular is its _testability_. Angular was built from the ground up with testing in mind. When the Angular team built the first versions of Angular, testability was a primary consideration. That means that Angular not only **supports isolated unit tests**, but it also **supports integrated end to end tests**. Also, a lot of the built-in objects that Angular provides have special versions that you can use to make your testing easier. In fact, testing is so critical to Angular, that while building the framework the team created a fantastic testing tool which used to be called **Testacular**, and is now called **Karma**. This tool is used by lots of development shops to test their code, and many of them aren't even using Angular. Perhaps the one attribute of Angular that sets it most apart from the rest of MV* frameworks is the fact that it **extends HTML** by _providing its own elements and properties_ called **directives**, that are used to interact with your HTML DOM. Basically, Angular lets you teach your HTML new tricks. Imagine if HTML had been **designed for applications** and not for documents. That is how Angular thinks of HTML and the ability it gives you to teach your HTML new tricks is a result of this thinking. 
`<input id="id1" type="text" focus>`
Here I have a simple input tag, but look at this last property. This is a custom attribute that I might build that tells Angular to make the element have focus when the page loads. What some of you may recognize is that HTML5 already has an attribute like this, it's called `auto-focus`. So HTML5 is already thinking along these lines. The problem is that that property only works in newer browsers. A custom directive like this one can work in a much wider range of browsers through the magic of Angular. Here's another example. This time I'm being a little more ambitious. 
`<multiStateButton id="btn1" />`
This is maybe a toggle button or possibly even a button that cycles through several states, but here I can create some kind of a multiStateButton that works the way I want it to work in my application. In my HTML, all I see is this, but after Angular gets done processing this element, the browser will see the HTML that it needs in order to accomplish what I want. And finally, something even more ambitious. 
`<userTile id="ut1" user="currentUser">`
This is, perhaps, a display widget customized to a particular application that displays users in a specific manner. I just have to pass in a user object using the user property that I created on my custom tag, and Angular knows how to turn this custom HTML element into HTML that my browser can render. Think of how this keeps so much of your view logic where it belongs, in your view. The last important attribute of Angular that we will discuss is how it is forward thinking. Angular is basically supporting the future of what we will see in web technology in the coming years, and as that technology becomes more widespread, our Angular applications will already be built to take advantage of that technology. Let's look at a couple specific technologies that apply here. Remember when I talked about what HTML would be if it had been designed for applications and not for documents? Well that's what web components are. **Web components allow you to make truly encapsulated components and widgets for your page, encapsulating HTML, JavaScript, and CSS**. [You can look at this article for more information about web components](https://www.w3.org/TR/components-intro/). Another up and coming feature that will soon be supported by some browsers is `Object.observe`. This technology lets you watch an object or a property on a JavaScript object for changes and react to those changes. Most MV* frameworks make you stick your data into special structures and call methods whenever you want to read or write to that data. Because Angular doesn't do that, it can support Object.observe when it becomes widely available, and Angular will simply benefit from the performance improvements of having things handled by faster, lower-level code. [You can read more about Object.observe at this URL here](http://wiki.ecmascript.org/doku.php?id=harmony:observe). 

Now one of the last things I want to do is take a quick look at Angular's official site. On the home page there's a lot of introductory text about it. There's this Learn section which has links to videos, and tutorials, and case studies, and a link to the Seed project template, which we will cover later on, but a key piece of the Angular site I want to show you that you're going to use and refer to a lot is under this Develop link, and it's these two links right here, the [Developer Guide](https://docs.angularjs.org/guide) and the [API Reference](https://docs.angularjs.org/api). Let's look at the Developer Guide first. This page has a list of all of the concepts that are part of Angular, so anytime you have any questions about something specific to Angular, you can come in here, look for the concept, say we have a question about modules, come in here, click on Modules, and look at Angular's official documentation on modules. Now let's look at the API Reference. This page has a list of a lot of the very specific pieces of Angular, for example, a list of all the directives that Angular provides is given right here. If we scroll down a little bit we can see a list of all the filters that Angular provides, and a list of all the services that it provides, and a lot of other stuff. So those are two pieces of Angular's official site that you ought to be comfortable with and visit frequently. Let's review with a quiz. _Angular thinks of HTML as if it had been designed to do what? Angular thinks of HTML as if it had been designed to build applications instead of documents. What kinds of tests does Angular support? Angular supports both unit tests and integrated end to end tests. Name one of the ways that Angular is forward thinking. Angular is forward thinking because of its future support for web components and Object.observe._

## Angular Architecture

Let's take a look at some of the architectural choices that Angular has made. First, Angular supports **two-way binding**. This means the user input into form fields is instantly updated in your Angular models. That means that in most cases you don't need to watch for specific events and respond to them, and then manually update your HTML. Instead, Angular will handle that for you. Angular also employs a technique called **dirty checking**. The net result of this is that you don't have to put your data into special structures and call getter and setter methods to read and write to your data. you can simply put your model data into plain old JavaScript objects and Angular will respond whenever your data changes and automatically update your view. Lastly, Angular is **built on dependency injection**. This lets you encapsulate pieces of your application better and also improves testability. You can read more about dependency injection here. 

Now let's take a look at the primary components of Angular and their relationship to each other. With Angular, _everything starts with the controller_. The **controller** is the **central player** in an Angular application. Controllers contain both _logic_ and _state_. Next we have the View. **Views are made up of bindings and directives**. This is how Angular talks to and listens to the user. _Controllers can communicate with views through both one-way and two-way binding_. _Directives_, which are a heavily talked about piece of Angular, are _really just part of the view_. And the last major piece is Services. **Services give you a place to contain the real logic and state of your application**. If you think about what is the essential tasks of your application, this would likely happen in your Services. Complex business logic, important application state, etc., Services are the place to house all that. Also, _Services are the place where you will want to communicate with the server_. Alright, let's review. What is the central component in an Angular application? The _central component_ in an angular application is the **controller**. _Directives_ are a part of which component? **Directives are part of the View**. In which component should you put your complex _business logic_? You should put your **core business logic** in the _Services_.

## Demo: Hello World in Angular

In this section, I'm going to build the simplest possible Hello World application that I can using Angular. If you look at my screen, you can see that I've got a minimal project with one file in it, an html file, and inside of that html file I've got a very small amount of HTML. I'm going to start by adding a script tag to point at the Angular library, and I'm going to point at the Angular library on Google CDN. I'm going to use version 1.4.0, which has been recently released, but you can use the latest stable version of Angular. Now that I've got that script file here, the next thing I need to do is tell Angular that this html page is an Angular application. I'm going to do that by going up to the _html tag_ and **adding an ng-app attribute to the html tag**, and I'm going to set it equal to "app". This is going to be the **name of my application**. Now that I've got that in place, the next step will be to add some HTML will display our Hello World message, so down in the body I'll add an h1 tag and I'm going to do two things to that `h1` tag. First I'll give it a special _attribute_ called `ng-controller`, and I'm going to set that equal to the value of `HelloWorldCtrl`. This will be the name of the controller that I'll create in just a second. And inside of that h1 tag, I'm going to make the **content two curly braces**, which tells Angular to replace this value with something else, and then I'm going to give it the value of `helloMessage`. That will cause Angular to look for a helloMessage variable and put its value inside this h1 tag. Now I've got to write a little bit of custom code and create this controller, which I named HelloWorldCtrl, and then create the helloMessage property. I'll do that by creating a new `script` tag, and inside of that I'm going to call `angular.module`. **This creates a module which is a container for every piece of an Angular application**. The first parameter of this function is the name of the module, which is going to be "app", which matches the name I gave it up in my html tag, and the second parameter is a _list of other modules that this module that I am creating depends on_. In this case, I'm not depending on any other modules, so I'm going to give it an _empty array_. Now that I've created the module, I can call the controller function, which will create a controller, which takes in two parameters. The first is the name of the controller, which is going to be HelloWorldCtrl, which matches the name I gave it in my h1 tag, and the second parameter is a function, I'm going to put this on another line to make it easier to read, and I'm going to have that function receive one parameter called `$scope`. This is a special parameter which we'll talk about more later on. And inside of here I will call $scope and create a new property called helloMessage, which matches the value that I put inside the curly braces on my h1 tag, and I'm going to set it equal to the string Hello World. And now if I open up that file in a browser, we will see the message Hello World.

## The Angular Event Reg Application

In this course, we will be learning about Angular through building a real application. This application is called Angular EventReg. Now we're not talking about some simple Hello World application. This application will have a reasonable amount of features. When we are done, we should have written around 500 lines of JavaScript and 200 lines of HTML, plus tests. Now realize that this is a showcase application and not necessarily a reference application on best practices, especially for things that are external to what Angular itself actually handles, such as CSS, deployment, data access, performance, and other concerns like that. We will be showing quite a few best practices with Angular itself, but as Angular is relatively new, many best practices are yet to be discovered and Angular is evolving all the time. New versions are regularly release, and with each new version new best practices are waiting to be found. One of our goals here is not to just teach you how to use Angular, but how to use Angular in a real-world application. This should give you the confidence you need to go and start your own Angular application from scratch. Now let's look at the major features of EventReg. EventReg is an application for _creating and viewing Angular events or conferences_, and for viewing and voting for the sessions available at these events. So the first major feature of EventReg is the ability to show a list of Angular events. From that list, the user can click on an event to see that event's details including a list of sessions and the details on each session. Also users should be able to create new sessions and events. There will be some validation here so that the necessary information is available on each event. Users who create an event or a session should be able to edit that event or session. Next, any operations that require knowing who the user is should require the user to login. As such, users should be able to freely register a new user account, and should be able to edit their account. Since we want to have a realistic application, we are going to be sending data to and from a server, therefore we will need some kind of server technology in place. You can really use any technology that you want, but in this course we will show you how to build and use both a node server and an ASP.NET MVC server, if you're on Windows. Of course the node server will run on both Windows and Linux. We will be making Ajax calls to the server just like we would in a real application, so it will show us what it's like to run Angular in a more production-like environment. For this application we will be using Twitter Bootstrap to make the styling easier. In addition, we will be using an open source theme for Bootstrap so that we have a slightly more interesting look and feel.

## Angular Version

This course was originally authored using Angular version 1.0.5. Since then, several major versions of Angular have been released. The current version of Angular is now 1.4. We have updated the course to be compatible with this version. In order to make the updates as seamless as possible, we have gone through all the demos and updated them to be compatible, and we've also gone through the entire course and updated it for 1.4. In some cases, those updates involved a complete rerecording of a clip, and in some cases the changes were minor enough that we simply added an explanation that was different, or left the clip alone. So it's possible that you might occasionally see a place where it looks like we're using version 1.2 or 1.0. You can safely ignore this, the course is up to date for 1.4. As newer versions of Angular come out, we will continue to update the course to be compatible with those versions. If you're following along, you should almost always be using the latest stable version of Angular. That might be 1.5 or even 1.6. You should always check the GitHub repo mentioned earlier, which will tell you if anything is out of date, but otherwise you can use the latest stable version of Angular.

## Tools Used

In this course, you will see a lot of work done from the command line. Although we recorded this course using Windows boxes, we are going to be using the Bash Shell for our command line work. For those of you who have only developed on a Windows Box it may seem a little foreign, but even though it may look a bit different from the Windows command prompt, you can follow along using either the standard Windows command prompt or the Bash Shell. None of what we do will be unique to the Bash Shell, and there will be only 1 or 2 places where the commands you use won't be exactly the same. In those cases we will note the difference. Most of our command line work will be running prebuilt scripts. From the Bash Shell we will run scripts that end in the sh extension. **For Windows users, you'll be using batch files**. If you have the downloaded code, you can choose between the .sh and .bat files based on your chosen command shell. If you're wondering how we installed the Bash Shell on Windows, it is installed when you install Git for Windows. The editor you will see us use in this course is Webstorm. Webstorm is a product by JetBrains, the same folks who make IntelliJ and ReSharper. The reason we chose Webstorm is because it is an excellent product. It gives you a lot of the features that you can't get from most text editors, but it's lighter weight than a full IDE like IntelliJ or Visual Studio, and it's integration with the Karma testing tool is second to none. You'll get to see that in the last module. Naturally, any text editor is fine to follow along. Nothing we do will be dependent on Webstorm. The last tool we need to talk about is the web server. As mentioned previously, you can use any web server that you want. In this course, though, we're going to show you how to create and use two different web servers, a Node web server and an ASP.NET MVC web server. You are free to use whichever one suits your purposes best, or if you're very familiar with another technology you're free to create your own. The web server that we're going to use is very simple. The web server itself will be responsible for not only serving up the files that we create, but also we're going to be sending and receiving Ajax to that server. In order to save that data, we're just going to write it to the hard disk, so therefore requests will come from the browser to the web server, which will then persist the data to the hard disk and correspondingly pull the data from the disk and serve it down to the browser when requested. Files relating to the web servers will be available on the GitHub repo for this course.

## Summary

In this module we started by taking a look at JavaScript MV* frameworks, some of the various options there, and how Angular fits into that world. Then we looked at some of the benefits of AngularJS such as it being forward thinking and very testable. After that we took a brief look at the application that we will be building throughout this course, the EventReg application.

---
# Controllers & Markup

Download any Angular version [from here](https://code.angularjs.org/). Current stable release of April 2017 is 1.6.4. Small applications should use a single module.

install from root app node where package.json resides
```sh
npm install
```
individual install, creates a _node_modules_ directory
```sh
npm install express@4.13.0 body-parser@1.13.1
```

**/scripts/web-server.js**
```js
var express = require('express');
var path = require('path');
var app = express();
var rootPath = path.normalize(__dirname+'/../');
app.use (express.static(rootPath+'/app'));
app.listen(8080);
```

from the bash shell, run node, serve a static file
```sh
server.sh
```

**iis**, physical path: $PathToDemo/app, site name: DemoApp, port: 8080. When started, uris `http://localhost:8080/img/profile.jpg` and `http://localhost:8080/img/angularjs-logo.png` should display images.

## Scope

We can't talk about controllers without talking about scope. So let's look at the relationship between controllers and scope. **A controller's primary responsibility is to create a scope object**. A _scope object_ is **how we communicate with the view**, and the scope is able to communicate with a few through a **two-way** _communication_. The **view can bind the properties and results of functions on the scope**, and **events on the view can call methods on a scope**. Data passes in this way _from the controller to the scope_, and _from the scope back and forth to the view_. The _scope is used to **expose** the model to the view_, but the scope is not the model. The model is the _data that is put into the scope_. If we want to modify the model, we can either **use methods that are on the scope to modify the model**, perhaps in response to events fired by the view, or using **two-way bindings** we can modify the model. In this way users through the view can make modifications to the model, or in other words can make modifications to the data. Let's review with a quiz. What is the primary responsibility of the controller? _Controllers primary responsibility is to create the scope_. Is the scope the model? No, the scope is not the model. _The scope merely contains the model_. Can the view bind to functions on the scope? _Yes, you can bind your view to both functions and properties on your scope object_.

## Controllers

**EventDetails.html**
1. Add inside `head` css for bootstrap and app
````htm
<link rel="stylesheet" href="/css/bootstrap.min.css" />
<link rel="stylesheet" href="/css/app.css" />
````
2. Add a `<div class="container">` directly to `body`
3. Add the event controller as `<div ng-controller="EventController">`
4. Add all necessary scripts to the end of body including `<script src="/js/controllers/EventController.js"></script>`
5. Angular ref `<script src="/lib/angular/angular.js"></script>`
6. `img ng-src`, `li ng-repeat="s in main.sessions"`, `ng-click`

**EventController.js** 
1. inside `{{ }}` evaluation. double curly brace
2. `$scope.upVoteSession = function(session) { session.upVoteCount++; };`

## Built-in Directives

According to the Angular documentation, directives are a way to teach HTML new tricks. Essentially **directives get HTML a new functionality**. As Angular parses through your HTML, it will look for directives and then take action based on what it finds. So in the case of **NG click**, whenever it encounters an NG click, it will _register a click handler event on that DOM object_. If you remember, that was an attribute of a tag. There are actually four ways to specify directives with Angular. The first one is actually is the tag itself. For example, the _NG form directive is a tag_, `<ng-form />`. The other way is the way that we've seen before with NG click where the directive is an _attribute of a tag_, `<div ng-form />`. And the third way that we can write directives is _as a class_, `<div class="ng-form" />`. Now not all directives can be written out as tags, attributes and as classes. Often times a particular directive could only be written out in one or two of these forms. The fourth way to write a directive is inside of an _HTML comment_. 

| ![](https://wewstq.by3302.livefilestore.com/y4m7bmJFejQc0caig6ev0xh8WWJPf0WpPm-_HusgmwioYUmkut0vBbphlkBx_RVewAk-WWbMF3Hg_lfrzItTcPuqaZ1bbpu6iYswipH9OrHAITANxNj1Pr0nqcjC6cCSZ6Vm222b2ogBli4tsM32jwVA2Rb-_fXoBFnfxkkEp0XyMSDVUSTLHDH0TvUoXDGV5GXljoptxMpBMYMywWcejhsiw?width=256&height=182&cropmode=none) | ![](https://tsywqq.by3302.livefilestore.com/y4macba6ntHzRbwtfFl5wjshPScN3lHc4ZtJ86Dc8eFe9hBqrQcE11usSn5EHXnF2V3HpWXy_sBkGWo_bds-aFsx73W_B0Q5q6M-fNm04njxGa9bC_NsD5nobXV9rQgeYsEgmdaTQLp7IrD2ypEDxNAuunU81i_Hd2eThlnC-guvV5NImQvH8YvuCtsnkGtN-INTlSDt1n_qN6PEbSYZlOKfg?width=192&height=256&cropmode=none) | ![](https://6ubyoa.by3302.livefilestore.com/y4ml8m3Bu8fysKHIALi-HP9ynsUPPCltGiWFtmR0gPlKi8aLmHnqpbAjIEjXjW_JwVB4qGeFg6iyTya8JIUjGOxUQTh2qiFGStsU5yzP-WrAK5wb9uZ9ej56z66QRNTmDezrH5RQVGGGoZ3tY2RKuBfVyNvCjAaY07rzI7PlwmbBM2e1tJTioShZiqr5zDmY_l1PGNgM1S12cEes2bEGU0CJg?width=157&height=256&cropmode=none) |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Instead of using double curly braces, bind to property name(attribute value) using `ng-bind` attribute, or
`<h2 ng-bind-template="{{event.name}} {{event.date}}"></h2>`

## Event directives
![](https://jnhreg.by3302.livefilestore.com/y4m44yvgmdMGnjp3HrBS9ahlUaNZnyGakBB3WwCNuKM5atooXAhMcY_624KaFLxuDdlpIDuPBa0zAF1gXH_eRpHTreLnpU8xqAQsj9RFwp0VH1IIend2aTggrYqpXQAGYeUomrQFQe7wXB5G5qAuC8R51mFb3W_hb4p1hZM_Y4raw_Qr8Q-MkeIVytwVvUaTP2VhLjfO1MELR6sn0jP2kHVXA?width=161&height=256&cropmode=none)

ng-model required if ng-change present
`<input type="checkbox" ng-change="handleChange()" ng-model="property">`

In the controller, add `$scope.buttonDisabled = true;` and in the view `<button class="btn" ng-disabled="buttonDisabled">Disabled</button>`

## Filters
`{{ expression | filter }}`
built-in: uppercase, lowercase, for instance `<h3>{{event.name | uppercase}}</h3>`
number & currency `<div>{{3.14132453 | number:2}}</div>`
date: `<div>{{jsdate | date:'mediumDate'}}</div>`

````html
<li ng-repeat "session in event.sessions | orderBy:sortorder | limitTo:2 | filter:query">
````

two-way binding
ng-model works with input, select and textarea. `<input type="text" ng-model="object.container.property" />`.
A property that does not exist will be created automatically on the scope.

## Validation
The `required` attribute on a html element bound with `ng-model`. You can validate against a regular expression with `ng-pattern`.


---
# Services

**Creating and Using Angular Services**

- an object that is used to encapsulate some sort of business logic, or just does some sort of work. just a **worker object**
- **often stateless**, although it isn't unusual for a service to _cache data that is accessed frequently_.
- It is **not accessed over the wire**, although it may be used to _perform operations that do go over-the-wire_, such as making AJAX calls
- Just an object that has methods and properties on it that we can **reuse**
- Registering a service with Angular is simple, and, once **registered**, it now becomes part of the Angular world and it can be used like any other Angular service. It can now be easily injected into your controllers and directives and filters and even into other services.
- _$scope param_ in controller is a service! do not use dollar sign for your own services.
- What you pass into the **factory** method is the _name of the service_, and then _a function that returns the object that will become that service_. 

## Built-in
![](https://gonhua.by3302.livefilestore.com/y4mVAD0zWAKIE_dUnvzChzwjJGmZ9YmB6iUPjBDKI5KQKGekWR4rotfGZiQhQhLQa0HrCYMb7G0Wfm-dJjYNnlTZoex9A2pqyyYyMtIs5Z361lOP70M20x19s-rGn1gL5lXHB9lcwy66gSU621CNUlM424fmQURCbzaN3bVdK4lJXDEHW9avMx321T81NQRcAUMYx3ZbTU0--m1onjRyXaMYg?width=256&height=201&cropmode=none)

### $http
good for non-restful calls, **raw**, _regardless of endpoint type_

**EventData.js**
````js
eventsApp.factory('eventData', function($http) {
    return {
        getEvent: function (cb) {
            $http({method:'GET', url:'/data/event/1'}).
               success(function(data, status, headers, config) {
                   cb(data);
               }).
               error(function(data, status, headers, config) {
                   $log.warn (data, status, headers(), config);
               });
        }        
    };
});
````
Controller calls `eventData.getEvent(function(event) {$scope.event=event;});`

**web-server.js** with node server
````js
var events = require('./eventsController');
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.get('/data/event/:id', events.get);
app.post('/data/event/:id', events.save);
````

**eventController.js**
````js
    var fs = require('fs');
     
    module.exports.get = function(req, res) {
        var event = fs.readFileSync('app/data/event/' + req.params.id + '.json', 'utf8');
        res.setHeader('Content-Type', 'application/json');
        res.send(event);
    };
     
    module.exports.save = function(req, res) {
       var event = req.body;
       fs.writeFileSync('app/data/event/' + req.params.id + '.json', JSON.stringify(event));
       res.send(event);
    }
````

### $promise
.\app\js\controllers\EditEventController.js 

````js
'use strict';

eventsApp.controller('EditEventController',
    function EditEventController($scope, eventData) {

        $scope.event = {};

        $scope.saveEvent = function(event, newEventForm) {
            if(newEventForm.$valid) {
                eventData.save(event)
                    .$promise
                    .then(function(response) { console.log('success', response)})
                    .catch(function(response) { console.log('failure', response)});
            }
        };

        $scope.cancelEvent = function() {
          window.location = '/EventDetails.html';
        }

    }
);
````

### $resource
good for **restful** web apis
include reference to `angular-resource.js`.
add to `app.js` the module _.\app\js\services\EventData.js_
````js
eventsApp.factory('eventData', function($resource) {
    var resource = $resource('/data/event/:id', {id:'@id'}, {"getAll": {method: "GET", isArray: true, params: {something: "foo"}}});
    return {
        getEvent: function(eventId) {
            return resource.get({id:eventId});
        },
        save: function(event) {
            event.id = 999;
            return resource.save(event);
        },
        getAllEvents: function() {
            return resource.query();
        }
    };
});
````

_.\app\js\services\userResource.js_
````js
'use strict';

eventsApp.factory('userResource', ['$resource', function ($resource) {
    var service = $resource('/data/user/:userName', {userName:'@userName'}, { });

    service.queryAll = function (callback) {
        return service.query({}, callback)
    };

    return service;
}]);
````

[<<](../JS.md) | [home](../../README.md)