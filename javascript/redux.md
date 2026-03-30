---
title: Redux
layout: default
nav_order: 5
parent: JavaScript
last_modified_date: 2026-03-29 21:15:03 +00:00
---

# Redux

Using Redux to Manage State in Angular [1]
Pluralsight course page [1]

Redux attempts to make state mutations predictable [2] by imposing certain restrictions on how and when updates can happen.
Overkill if application is small. Comes with ts bindings, first class support for `Angular`.

diagram [3]
![diagram](https://photos-5.dropbox.com/t/2/AAD3e2vMl8kW3ZORleK71JACBDMJW-X6SW8ML9wHTZtrdQ/12/693348804/png/32x32/3/1504184400/0/2/2017-08-28%2009_39_34-Using%20Redux%20to%20Manage%20State%20in%20Angular.png/EMeD9dkFGAogBygH/lB0KbF5QI8KprGcfjnwpqcC8bVRyvU0HeyekZt5EyjA?dl=0&size=2048x1536&size_mode=3)

## Core Principles

1. single source of truth (for state), one big store
2. state is read-only, immutable
3. pure functions drive changes

## Links

- course repo [4], a little console app that shows you how to use redux without *React* or *Angular* (used in Pluralsight course).
- angular2 cli ts app [5]. you may have multiple reducer types updating some root state.
- redux dev tools [6] multi browser extension
- Angular 2 redux bindings [7]

[1]: https://app.pluralsight.com/library/courses/angular-2-redux-manage-state/table-of-contents
[2]: http://redux.js.org
[3]: https://db.tt/9CFdKyhJSc
[4]: https://github.com/hendrikswan/console-redux
[5]: https://github.com/hendrikswan/pluralsight-angular-redux
[6]: https://github.com/zalmoxisus/redux-devtools-extension
[7]: https://github.com/angular-redux/ng-redux

[<](./index.md) | [<<](/index.md)
