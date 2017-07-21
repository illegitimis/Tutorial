# Angular4 notes

## links

- Latest [architecture overview](https://angular.io/guide/architecture#architecture-overview)
- [live hero list sample](https://angular.io/generated/live-examples/toh-pt6/eplnkr.html)
- [Angular official cheatsheet](https://angular.io/guide/cheatsheet)
- Archwizard: [github repo](https://github.com/madoar/ng2-archwizard-demo), [demo](https://madoar.github.io/ng2-archwizard-demo/), [npm](https://www.npmjs.com/package/ng2-archwizard)
- PrimeNG: [GitRepo](https://github.com/primefaces/primeng-quickstart-webpack), [Get Started](https://www.primefaces.org/primeng/#/setup)
- [Angular CLI wiki](https://github.com/angular/angular-cli/wiki)
- [http](http://www.syntaxsuccess.com/viewarticle/angular-2.0-and-http) simple calls, observables, promises, error handling

## start

```cmd
npm install -g @angular/cli
ng new my-app
cd my-app
npm install
ng serve --open
ng generate component [name]
```

## component inheritance

- [so](https://stackoverflow.com/questions/36475626/how-to-extend-inherit-angular2-component)
- [plnkr sample ???](https://plnkr.co/edit/TPps03QCGQCWbX6oVKXp?p=preview)
- [New features in Angular 2.3](https://medium.com/@gerard.sans/angular-2-new-features-in-angular-2-3-f2e73f16a09e)
- [Component Inheritance in Angular 2](https://scotch.io/tutorials/component-inheritance-in-angular-2)
- [angular 2 component inheritance plnkr sample](https://embed.plnkr.co/hMgaYPVRiXMCiKBdfqHy/)
- [plnkr style inheritance sample](http://plnkr.co/edit/bWa1JmH7NaSaJffLsl0x?p=preview)
- [component decorator metadata](https://medium.com/@amcdnl/inheritance-in-angular2-components-206a167fc259)

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
	
	
[<<](AngularJS.md) | [Home](https://github.com/illegitimis/Tutorial/)
