# Angular4 notes

## links

- [Rangle's Angular book](https://1drv.ms/b/s!AnIyfO51kH7NlVvjZo4Mwh9jlDvW)
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!AnIyfO51kH7NlVvjZo4Mwh9jlDvW)
- 2016 [Valerio De Sanctis - ASP.NET & Angular 2](https://1drv.ms/b/s!AnIyfO51kH7NlUSD7yLGPHr79BD7)
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!AnIyfO51kH7NlUSD7yLGPHr79BD7)
- Latest [architecture overview](https://angular.io/guide/architecture#architecture-overview)
- [live hero list sample](https://angular.io/generated/live-examples/toh-pt6/eplnkr.html)
- [Angular official cheatsheet](https://angular.io/guide/cheatsheet)
- Archwizard: [github repo](https://github.com/madoar/ng2-archwizard-demo), [demo](https://madoar.github.io/ng2-archwizard-demo/), [npm](https://www.npmjs.com/package/ng2-archwizard)
- PrimeNG: [GitRepo](https://github.com/primefaces/primeng-quickstart-webpack), [Get Started](https://www.primefaces.org/primeng/#/setup)
- [http](http://www.syntaxsuccess.com/viewarticle/angular-2.0-and-http) simple calls, observables, promises, error handling
- [Chrome Debugging with Angular CLI](https://github.com/Microsoft/vscode-recipes/tree/master/Angular-CLI) on vscode recipes
- Angular Botstrap `ngx-bootstrap` by _valor-software_
  + [Popover](https://valor-software.com/ngx-bootstrap/#/popover)
  + [TimePicker](https://valor-software.com/ngx-bootstrap/#/timepicker)
- [Angular Custom Form Controls with Reactive Forms and NgModel](https://coryrylan.com/blog/angular-custom-form-controls-with-reactive-forms-and-ngmodel)  
- [Conditionally add styles to an element](https://juristr.com/blog/2016/01/learning-ng2-dynamic-styles/) 2016.01, [SO answer](https://stackoverflow.com/a/45816521/2239678)
- [TS Playground](http://www.typescriptlang.org/play/index.html) 


## start

```cmd
npm install -g @angular/cli
ng new my-app
cd my-app
npm install
npm run start:dev /* package.json */
npm run watch -- --define eswenv=dev
webpack-dev-server --port=3000 --open
webpack --watch --progress  --profile
ng serve --open
ng generate component [name]
```
## http

- latest angular.io [HttpClient](https://angular.io/guide/http) guide
- [Angular 4.3 HttpClient](https://medium.com/codingthesmartway-com-blog/angular-4-3-httpclient-accessing-rest-web-services-with-angular-2305b8fd654b) (Accessing REST Web Services With Angular)
- [Introduction to Angular's HttpClient](https://alligator.io/angular/httpclient-intro/) July, 2017.

## component inheritance

- extend & inherit Angular component on [SO](https://stackoverflow.com/questions/36475626/how-to-extend-inherit-angular2-component)
- [New features in Angular 2.3](https://medium.com/@gerard.sans/angular-2-new-features-in-angular-2-3-f2e73f16a09e)
- [Component Inheritance in Angular 2](https://scotch.io/tutorials/component-inheritance-in-angular-2) 
with a focus on [ViewContainerRef](https://v2.angular.io/docs/ts/latest/api/core/index/ViewContainerRef-class.html)
and [TemplateRef](https://v2.angular.io/docs/ts/latest/api/core/index/TemplateRef-class.html)
with a [toggle sample](https://plnkr.co/edit/tSLIxUSTaqEfJK5NAD2D?p=preview)
- [angular 2 component inheritance plnkr sample](https://embed.plnkr.co/hMgaYPVRiXMCiKBdfqHy/)
- [plnkr style inheritance sample](http://plnkr.co/edit/bWa1JmH7NaSaJffLsl0x?p=preview)
- [component decorator metadata](https://medium.com/@amcdnl/inheritance-in-angular2-components-206a167fc259)
- [plnkr sample](https://plnkr.co/edit/TPps03QCGQCWbX6oVKXp?p=preview) with ComponentMetadata, seems outdated

## loading components dynamically

- [Loading Components Dynamically in Angular](http://www.syntaxsuccess.com/viewarticle/loading-components-dynamically-in-angular-2.0), the graph example
- [Dynamic table sample](http://plnkr.co/edit/dqfPCW3MBa9hM23EW3cS?p=preview) using ElementRef [1](https://angular.io/api/core/ElementRef), [2](https://v2.angular.io/docs/ts/latest/api/core/index/ElementRef-class.html), [3](https://angular-2-training-book.rangle.io/handout/advanced-components/elementref.html) and [DynamicComponentLoader](https://www.dartdocs.org/documentation/angular2/2.0.0-beta.9/angular2/DynamicComponentLoader-class.html)
- [hackish component decorator](https://stackoverflow.com/a/34067211) from [SO](https://stackoverflow.com/questions/36531486/dynamic-styleurls-in-angular-2)
- selectors, resolvers and interceptors 
	* [UrlResolverInterceptor](https://github.com/A-Hsien/UrlResolverInterceptor)
	* [SO answer UrlResolverInterceptor](https://stackoverflow.com/a/39588422)
	* [refactor(core): remove `ViewResolver` and `ViewResolverMock`](https://github.com/angular/angular/commit/0988cc8) The methods on `ViewResolverMock` have been merged into `DirectiveResolver`. BREAKING CHANGE: ES5 users can no longer use the `View(…)` function to provide `ViewMetadata`. This mirrors the removal of the `@View` decorator a while ago.
	* [Angular 2.0 ViewResolver Class](https://stackoverflow.com/a/36467207)
	* [ViewResolver resolves types to ViewMetadata.](https://www.dartdocs.org/documentation/angular2/2.0.0-beta.9/angular2/ViewResolver-class.html)
	* [Dynamic View and Components](https://medium.com/nerdlog/angular-2-dynamic-view-and-components-330205fa6896), very nice [sample](http://plnkr.co/edit/wh4VJG?p=preview)
	* [ViewContainerRef](https://angular.io/api/core/ViewContainerRef), Represents a container where one or more Views can be attached.
	
## test

* Testing Angular 2 code with [Jasmine](http://jasmine.github.io/) and [Karma](http://karma-runner.github.io/).
* Coverage with [Istanbul](https://github.com/gotwarlost/istanbul)
* End-to-end Angular code using [Protractor](https://angular.github.io/protractor/). 
  When debugging or first writing test suites, you may find it helpful to try out Protractor commands without starting up the entire test suite. 
  You can do this with the element explorer.[Protractor Interactive Mode here](https://github.com/angular/protractor/blob/master/docs/debugging.md#testing-out-protractor-interactively).
* Tests reports with [karma-tfs-reporter](https://github.com/sgbj/karma-tfs-reporter)
* Test coverage reports with [karma-coverage](https://github.com/karma-runner/karma-coverage)
* **Unit tests** _single run_: `npm test`, _live mode (TDD style)_: `npm run test-watch`	
* **End-to-End Tests** (aka. e2e, integration) 
```sh
#single run, in a tab, if not already running!
npm start
#in a new tab:
npm run webdriver-start
#in another new tab: 
npm run e2e
#interactive mode: 
npm run e2e-live
```
* `it`, `fit`, `xit` [link](https://codecraft.tv/courses/angular/unit-testing/jasmine-and-karma/#_disabled_and_focused_tests)	

## internationalization / localization
+ [ngx-translate](http://www.ngx-translate.com/) The internationalization (i18n) library for Angular
  - [ngx-translate/core](https://github.com/ngx-translate/core) 
  <br>`npm install @ngx-translate/core --save`
  - [ngx-translate/http-loader](https://github.com/ngx-translate/http-loader/tree/4f95eb6184a3b2316691a6364e742cbe32e72189),
  <br> a loader for ngx-translate that loads translations with http calls
  <br> `npm install @ngx-translate/http-loader --save`
  - [How to translate your Angular app](How to translate your Angular app with ngx-translate ) with ngx-translate, tutorial 
  - Samples: [demo plnkr](https://embed.plnkr.co/pYo6bFPRRxVPgRR8toDt/), Teradata/covalent [commit](https://github.com/Teradata/covalent/commit/776331bb5bc4098a4264a36e1275b3c83727e61a) and [repo](https://github.com/Teradata/covalent/search?utf8=%E2%9C%93&q=DEMO_ONE.SELECT)

+ [Angular2 and i18n](https://devblog.dymel.pl/2016/11/03/angular2-and-i18n-translate-your-app/) - translating your application by _Michał Dymel on November 3, 2016_ 
+ [Official guide to *i18n*](https://angular.io/guide/i18n) 	
+ [Making Sense of Angular Internationalization (i18n)](https://medium.com/@t_tsonev/making-sense-of-angular-internationalization-i18n-e7b26fb9c587) Apr 10, 2017
+ [Deploying an i18n Angular app with angular-cli](https://medium.com/@feloy/deploying-an-i18n-angular-app-with-angular-cli-fc788f17e358) Apr 17, and [Angular Translator *app*](http://angular-translator.elol.fr/en/)
 

## Angular CLI
- [How to use Angular CLI with Visual Studio 2017](http://candordeveloper.com/2017/04/12/how-to-use-angular-cli-with-visual-studio-2017/) Apr17
- [Angular CLI wiki](https://github.com/angular/angular-cli/wiki)
- [Angular2 CLI with ASP.NET Core application - tutorial](https://devblog.dymel.pl/2016/10/25/angular2-cli-with-aspnet-core-application-tutorial/) oct16
- [Angular CLI With .NET Core](https://dustinewers.com/angular-cli-with-net-core/) Mar17
- [.Net Core / Angular CLI - NPM Build Automation (html to cshtml)](https://stackoverflow.com/a/43662823/2239678)

[<<](../JS.md)
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 

