# Angular4 Notes

## Links

- Rangle's Angular book [1] One Drive [1] and online handout [2]
- Valerio De Sanctis - ASP.NET & Angular 2 [3] 2016 One Drive [3]
- **angular.io** related: Latest architecture overview [4], live hero list sample [5], official cheatsheet [6]
- Archwizard: github repo [7], demo [8], npm [9], wizard [10] should be ported. `angular2-wizard`: npm [11], demo [12]
- Angular Botstrap `ngx-bootstrap` by _valor-software_
  - Popover [13]
  - TimePicker [14]
- Angular Custom Form Controls with Reactive Forms and NgModel [15]
- Conditionally add styles to an element [16] 2016.01, SO answer [17]
- TS Playground [18]
- Quickstart: Angular2 with TypeScript and Gulp [19]
- angular update guide [20]
- git repos [21] & official blog [22] & resources [23]

## HTTP

- latest angular.io HttpClient [24] guide
- `Angular` 4.3 HttpClient [25] (Accessing **REST** Web Services With Angular)
- Introduction to Angular's HttpClient [26] July, 2017.
- syntaxsuccess.com: Angular 2.0 And Http [27] simple calls, observables, promises, error handling
- cironunes/httpclient-testing github-api.model.ts [28]
- Testing HTTP requests [29]
- angular.io: Httptestingcontroller [30]
- cironunes/httpclient-testing github-api.service.spec.ts [31]
- Unit testing services with HttpClient [32] on Medium
- Angular HttpClient get Example [33] with in memory web api, Nov 2017.

## Test

- Testing Angular 2 code with Jasmine [34], docs [35] and Karma [36].
- Coverage with Istanbul [37]
- End-to-end Angular code using Protractor [38].
  When debugging or first writing test suites, you may find it helpful to try out Protractor commands without starting up the entire test suite. 
  You can do this with the element explorer.Protractor Interactive Mode here [39].
- Tests reports with karma-tfs-reporter [40]
- Test coverage reports with karma-coverage [41]
- **Unit tests** _single run_: `npm test`, _live mode (TDD style)_: `npm run test-watch`
- **End-to-End Tests** (aka. e2e, integration)

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

- `it`, `fit`, `xit` link [42]
- official test guide [43]

## Forms & Validation

- Breeze [44]
- form-validation [45] official
- scotch [46] angular-2-form-validation

## Component Inheritance

- extend & inherit Angular component on SO [47]
- New features in Angular 2.3 [48]
- Component Inheritance in Angular 2 [49] with a focus on ViewContainerRef [50] and TemplateRef [51] with a toggle sample [52]
- angular 2 component inheritance plnkr sample [53]
- plnkr style inheritance sample [54]
- component decorator metadata [55]
- plnkr sample [56] with ComponentMetadata, seems outdated

## Loading Components Dynamically

- Loading Components Dynamically in Angular [57], the graph example
- Dynamic table sample [58] using ElementRef 1 [59], 2 [60], 3 [61] and DynamicComponentLoader [62]
- hackish component decorator [63] from SO [64]
- selectors, resolvers and interceptors
  - UrlResolverInterceptor [65]
  - SO answer UrlResolverInterceptor [66]
  - refactor(core): remove `ViewResolver` and `ViewResolverMock` [67] The methods on `ViewResolverMock` have been merged into `DirectiveResolver`. BREAKING CHANGE: ES5 users can no longer use the `View(…)` function to provide `ViewMetadata`. This mirrors the removal of the `@View` decorator a while ago.
  - Angular 2.0 ViewResolver Class [68]
  - ViewResolver resolves types to ViewMetadata. [69]
  - Dynamic View and Components [70], very nice sample [71]
  - ViewContainerRef [72], Represents a container where one or more Views can be attached.

## Internationalization / Localization

- ngx-translate [73] The internationalization (i18n) library for Angular
  - ngx-translate/core [74] `npm install @ngx-translate/core --save`
  - ngx-translate/http-loader [75] a loader for ngx-translate that loads translations with http calls `npm install @ngx-translate/http-loader --save`
  - Samples: demo plnkr [76], Teradata/covalent commit [77] and repo [78]
- Angular2 and i18n [79] translating your application by _Michał Dymel on November 3, 2016_
- Official guide to *i18n* [80]
- Making Sense of Angular Internationalization (i18n) [81] Apr 10, 2017
- Deploying an i18n Angular app with angular-cli [82] Apr 17, and Angular Translator *app* [83]

## Angular CLI

- How to use Angular CLI with Visual Studio 2017 [84] Apr17
- Angular CLI wiki [85]
- Angular2 CLI with ASP.NET Core application - tutorial [86] oct16
- Angular CLI With .NET Core [87] Mar17
- .Net Core / Angular CLI - NPM Build Automation (html to cshtml) [88]
- Chrome Debugging with Angular CLI [89] on vscode recipes
- quick start [90]

```cmd
npm install -g @angular/cli angular-cli typescript
ng new my-app
cd my-app
npm install
npm run start:dev /* package.json */
npm run watch -- --define eswenv=dev
webpack-dev-server --port=3000 --open
webpack --watch --progress  --profile
ng serve --open
ng generate component [name]
ng serve
npm run lite
```

## Promise vs Observable

- Angular - Promise vs Observable [91] 8 January 2018
- Taking advantage of Observables in Angular [92] Nov 2016
- Angular2 observables vs. promises [93]
- rangle.io Observables vs Promises [94]
-  behaviorsubject [95] an observer in addition to being an observable, Rx.BehaviorSubject class docs [96]

## Input Debounce

- Debouncing Angular 2 Input Component [97]
- Angular 2 – Creating a search field with debounce time [98]
- book collection [99] on stackblitz & code [100]

## PrimeNG

GitRepo [101], Get Started [102], dropdown showcase [103], & docs [104], theming [105], p-table [106]

## Misc

- Understanding Router State [107]
- `ActivatedRoute` docs [108]
- User Authentication with Angular and ASP.NET Core [109] Mar _17_
- JWT Authentication with ASP.NET Core 2 Web API, Angular 5, .NET Core Identity and Facebook Login [110] Jan _18_
- Token based authentication in ASP.NET Core [111] Oct _17_
- AspNetCore identity cookie settings [112]
- Material & CDK: badge [113], get started [114], bottom sheet [115]
- Angular Material Data Table: A Complete Example [116]: Server Pagination, Filtering, Sorting; course.component.ts [117], schematics [118], grid list [119] samples

[1]: https://1drv.ms/b/s!AnIyfO51kH7NlVvjZo4Mwh9jlDvW
[2]: https://angular-2-training-book.rangle.io/
[3]: https://1drv.ms/b/s!AnIyfO51kH7NlUSD7yLGPHr79BD7
[4]: https://angular.io/guide/architecture#architecture-overview
[5]: https://angular.io/generated/live-examples/toh-pt6/eplnkr.html
[6]: https://angular.io/guide/cheatsheet
[7]: https://github.com/madoar/ng2-archwizard-demo
[8]: https://madoar.github.io/ng2-archwizard-demo/
[9]: https://www.npmjs.com/package/ng2-archwizard
[10]: https://github.com/angular-wizard/angular-wizard
[11]: https://www.npmjs.com/package/angular2-wizard
[12]: https://maiyaporn.github.io/angular2-wizard-demo/
[13]: https://valor-software.com/ngx-bootstrap/#/popover
[14]: https://valor-software.com/ngx-bootstrap/#/timepicker
[15]: https://coryrylan.com/blog/angular-custom-form-controls-with-reactive-forms-and-ngmodel
[16]: https://juristr.com/blog/2016/01/learning-ng2-dynamic-styles/
[17]: https://stackoverflow.com/a/45816521/2239678
[18]: http://www.typescriptlang.org/play/index.html
[19]: http://blog.codeleak.pl/2016/03/quickstart-angular2-with-typescript-and.html
[20]: https://update.angular.io/
[21]: https://github.com/angular
[22]: https://blog.angular.io/
[23]: https://angular.io/resources
[24]: https://angular.io/guide/http
[25]: https://medium.com/codingthesmartway-com-blog/angular-4-3-httpclient-accessing-rest-web-services-with-angular-2305b8fd654b
[26]: https://alligator.io/angular/httpclient-intro/
[27]: http://www.syntaxsuccess.com/viewarticle/angular-2.0-and-http
[28]: https://github.com/cironunes/httpclient-testing/blob/master/src/app/shared/github-api.model.ts
[29]: https://angular.io/guide/http#testing-http-requests
[30]: https://angular.io/api/common/http/testing/HttpTestingController
[31]: https://github.com/cironunes/httpclient-testing/blob/master/src/app/shared/github-api.service.spec.ts
[32]: https://medium.com/netscape/testing-with-the-angular-httpclient-api-648203820712
[33]: https://www.concretepage.com/angular-2/angular-httpclient-get-example
[34]: http://jasmine.github.io/
[35]: https://jasmine.github.io/tutorials/your_first_suite
[36]: http://karma-runner.github.io/
[37]: https://github.com/gotwarlost/istanbul
[38]: https://angular.github.io/protractor/
[39]: https://github.com/angular/protractor/blob/master/docs/debugging.md#testing-out-protractor-interactively
[40]: https://github.com/sgbj/karma-tfs-reporter
[41]: https://github.com/karma-runner/karma-coverage
[42]: https://codecraft.tv/courses/angular/unit-testing/jasmine-and-karma/#_disabled_and_focused_tests
[43]: https://angular.io/guide/testing
[44]: http://breeze.github.io/doc-js/breeze-angular.html
[45]: https://angular.io/guide/form-validation
[46]: https://scotch.io/tutorials/angular-2-form-validation
[47]: https://stackoverflow.com/questions/36475626/how-to-extend-inherit-angular2-component
[48]: https://medium.com/@gerard.sans/angular-2-new-features-in-angular-2-3-f2e73f16a09e
[49]: https://scotch.io/tutorials/component-inheritance-in-angular-2
[50]: https://v2.angular.io/docs/ts/latest/api/core/index/ViewContainerRef-class.html
[51]: https://v2.angular.io/docs/ts/latest/api/core/index/TemplateRef-class.html
[52]: https://plnkr.co/edit/tSLIxUSTaqEfJK5NAD2D?p=preview
[53]: https://embed.plnkr.co/hMgaYPVRiXMCiKBdfqHy/
[54]: http://plnkr.co/edit/bWa1JmH7NaSaJffLsl0x?p=preview
[55]: https://medium.com/@amcdnl/inheritance-in-angular2-components-206a167fc259
[56]: https://plnkr.co/edit/TPps03QCGQCWbX6oVKXp?p=preview
[57]: http://www.syntaxsuccess.com/viewarticle/loading-components-dynamically-in-angular-2.0
[58]: http://plnkr.co/edit/dqfPCW3MBa9hM23EW3cS?p=preview
[59]: https://angular.io/api/core/ElementRef
[60]: https://v2.angular.io/docs/ts/latest/api/core/index/ElementRef-class.html
[61]: https://angular-2-training-book.rangle.io/handout/advanced-components/elementref.html
[62]: https://www.dartdocs.org/documentation/angular2/2.0.0-beta.9/angular2/DynamicComponentLoader-class.html
[63]: https://stackoverflow.com/a/34067211
[64]: https://stackoverflow.com/questions/36531486/dynamic-styleurls-in-angular-2
[65]: https://github.com/A-Hsien/UrlResolverInterceptor
[66]: https://stackoverflow.com/a/39588422
[67]: https://github.com/angular/angular/commit/0988cc8
[68]: https://stackoverflow.com/a/36467207
[69]: https://www.dartdocs.org/documentation/angular2/2.0.0-beta.9/angular2/ViewResolver-class.html
[70]: https://medium.com/nerdlog/angular-2-dynamic-view-and-components-330205fa6896
[71]: http://plnkr.co/edit/wh4VJG?p=preview
[72]: https://angular.io/api/core/ViewContainerRef
[73]: http://www.ngx-translate.com/
[74]: https://github.com/ngx-translate/core
[75]: https://github.com/ngx-translate/http-loader/tree/4f95eb6184a3b2316691a6364e742cbe32e72189
[76]: https://embed.plnkr.co/pYo6bFPRRxVPgRR8toDt/
[77]: https://github.com/Teradata/covalent/commit/776331bb5bc4098a4264a36e1275b3c83727e61a
[78]: https://github.com/Teradata/covalent/search?utf8=%E2%9C%93&q=DEMO_ONE.SELECT
[79]: https://devblog.dymel.pl/2016/11/03/angular2-and-i18n-translate-your-app/
[80]: https://angular.io/guide/i18n
[81]: https://medium.com/@t_tsonev/making-sense-of-angular-internationalization-i18n-e7b26fb9c587
[82]: https://medium.com/@feloy/deploying-an-i18n-angular-app-with-angular-cli-fc788f17e358
[83]: http://angular-translator.elol.fr/en/
[84]: http://candordeveloper.com/2017/04/12/how-to-use-angular-cli-with-visual-studio-2017/
[85]: https://github.com/angular/angular-cli/wiki
[86]: https://devblog.dymel.pl/2016/10/25/angular2-cli-with-aspnet-core-application-tutorial/
[87]: https://dustinewers.com/angular-cli-with-net-core/
[88]: https://stackoverflow.com/a/43662823/2239678
[89]: https://github.com/Microsoft/vscode-recipes/tree/master/Angular-CLI
[90]: https://angular.io/guide/quickstart
[91]: https://fullstack-developer.academy/angular-promise-vs-observable/
[92]: https://blog.thoughtram.io/angular/2016/01/06/taking-advantage-of-observables-in-angular2.html
[93]: https://stackoverflow.com/questions/39081715/angular2-observables-vs-promises
[94]: https://angular-2-training-book.rangle.io/handout/observables/observables_vs_promises.html
[95]: https://stackoverflow.com/a/40231605/2239678
[96]: https://github.com/Reactive-Extensions/RxJS/blob/master/doc/api/subjects/behaviorsubject.md
[97]: https://manuel-rauber.com/2015/12/31/debouncing-angular-2-input-component/
[98]: http://www.talkinghightech.com/en/angular-2-creating-search-field-debounce-time/
[99]: https://stackblitz.com/github/ngrx/platform/
[100]: https://github.com/ngrx/platform/blob/master/example-app/app/books/effects/book.ts
[101]: https://github.com/primefaces/primeng-quickstart-webpack
[102]: https://www.primefaces.org/primeng/#/setup
[103]: https://www.primefaces.org/showcase/ui/ajax/dropdown.xhtml
[104]: https://www.primefaces.org/primeng/#/dropdown
[105]: https://www.primefaces.org/primeng/#/theming
[106]: https://www.primefaces.org/primeng/#/table
[107]: https://vsavkin.com/angular-router-understanding-router-state-7b5b95a12eab
[108]: https://angular.io/api/router/ActivatedRoute
[109]: https://fullstackmark.com/post/10/user-authentication-with-angular-and-asp-net-core
[110]: https://fullstackmark.com/post/13/jwt-authentication-with-aspnet-core-2-web-api-angular-5-net-core-identity-and-facebook-login
[111]: https://dotnetthoughts.net/token-based-authentication-in-aspnet-core/
[112]: https://docs.microsoft.com/en-us/aspnet/core/security/authentication/identity-configuration?tabs=aspnetcore2x#cookie-settings
[113]: https://material.angular.io/components/badge/examples
[114]: https://material.angular.io/guide/getting-started
[115]: https://material.angular.io/components/bottom-sheet/overview
[116]: https://blog.angular-university.io/angular-material-data-table/
[117]: https://github.com/angular-university/angular-material-course/blob/2-data-table-finished/src/app/course/course.component.ts
[118]: https://material.angular.io/guide/schematics
[119]: https://material.angular.io/components/grid-list/examples
[120]: https://github.com/illegitimis/Tutorial/wiki


[<<](./index.md) | [home](../../README.md)
