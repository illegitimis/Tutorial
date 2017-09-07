# Redux

[Using Redux to Manage State in Angular](https://app.pluralsight.com/library/courses/angular-2-redux-manage-state/table-of-contents)	
[![Pluralsight course page](https://img.shields.io/badge/Pluralsight-course-lightgrey.svg)](https://app.pluralsight.com/library/courses/angular-2-redux-manage-state/table-of-contents)

Redux attempts to make state [mutations predictable](http://redux.js.org) by imposing certain restrictions on how and when updates can happen.
Overkill if application is small. Comes with ts bindings, first class support for Angular.

[diagram](https://db.tt/9CFdKyhJSc)
![diagram](https://photos-5.dropbox.com/t/2/AAD3e2vMl8kW3ZORleK71JACBDMJW-X6SW8ML9wHTZtrdQ/12/693348804/png/32x32/3/1504184400/0/2/2017-08-28%2009_39_34-Using%20Redux%20to%20Manage%20State%20in%20Angular.png/EMeD9dkFGAogBygH/lB0KbF5QI8KprGcfjnwpqcC8bVRyvU0HeyekZt5EyjA?dl=0&size=2048x1536&size_mode=3)



**Core** principles: 
1. single source of truth (for state), one big store 
2. state is read-only, immutable
3. pure functions drive changes 

**links**
- [course repo](https://github.com/hendrikswan/console-redux), a little console app that shows you how to use redux without *React* or *Angular* (used in Pluralsight course). 
- [angular2 cli ts app](https://github.com/hendrikswan/pluralsight-angular-redux)
you may have multiple reducer types updating some root state.
- [redux dev tools](https://github.com/zalmoxisus/redux-devtools-extension) multi browser extension
- [Angular 2 redux bindings](https://github.com/angular-redux/ng-redux)



[<<](../JS.md)
|
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 