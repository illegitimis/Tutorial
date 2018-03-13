# Angular 2

+ [ECMAScript6 features comparison](http://es6-features.org)
+ [Wizards wizard](https://github.com/danielfigueiredo/wizards-wizard) A wizard to build a wizard. Demo application for integrating _forms_ and _redux_, as showcased @ ng-conf 2017 during FormControl Freaks: Redux Edition.

## diff es6 vs es5 unicorn

![diff es6 vs es5 unicorn](https://s1cjww.by3302.livefilestore.com/y4mitsFDvsIUrGgDny8CaTRzDnRkZ7xHKjLwQuUMssOFqkFy0NXYCZgNfv_epaMCiUaRUcVbS_VW6gK07CrV72zXTOYJIhfUPu07vehw8xRoW3yXZT80w_WpPVuiq5leIVYKa5FCYNJNVgMV7RV94HeeQJYVMevn0FdJBAki9b_Fwm_hzyRt5uFBGoZsoAIoLOsOv-cRfi_U8U43C1LrjT04Q?width=635&height=397&cropmode=none)

directive change, ng2 eliminates _scope_, _restrict_, _link_, module has a **component method** instead
![my-narwhal](https://up5oia.by3302.livefilestore.com/y4msRTsm9lXTA6Y2Rvik59s982Q1wMFSsvzFPUzipbN0Yc1eyeeX_A6Bx8OiJESh5qOgC9Me9M0-csOLKszNjWP8ESaAoo2kwjLn0a1kBiXyPs3HY2A8HvyDPRS02F41MmeWeXCSIvcxEmSu99_hU9gGWBGLZ8utjS2HxdaeqwwUY5NqqO_ve_rd4YNGmHu_F062T4puuhKQVmQxCyVBB7fPQ?width=743&height=490&cropmode=none)

typescript is a __superscript__ of ES6.

|  |  |
|---|---|
`component` | **encapsulates** the _template_, _data_ and _behavior_ of a view. components can be _nested_, in a tree like structure, and reusable. is a ts class. _completely decoupled from the DOM_, binding used instead. facilitates unit testing.
`router` | responsible for _navigation_
`directive` | _modify DOM elements_ so as to modify their behavior
`service` | ![component->service->rest api](https://vrp2kg.by3302.livefilestore.com/y4mQ-0_q17WRRu-5rqmW6VYBivyi6UVJ785Xfwi9vOckCpm2UmqOsurWS0hTIaCEIgmnHEvlwywLwNFvN-xbNPzEQkcQnxVIyJAtJHVeJyB2vRQ6-cAeffijFaDuKCdRbQnHscBMV4q6wtrl1D2KykKFdUlllrh_AiBn8Gfy9KJV6jgASKY3hQ-hKHw2fznDlju0OlIO9DrHES16dG1AhRQNw?width=660&height=251&cropmode=none)

[<<](../JS.md) | [home](../README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki)