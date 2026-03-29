# OpenID Connect

OpenID Connect [1] is an interoperable authentication protocol based on the OAuth 2.0 family of specifications.
It uses straightforward **REST**/JSON message flows with a design goal of “_making simple things simple and complicated things possible_”. 
It’s uniquely easy for developers to integrate, compared to any preceding Identity protocol. 
**(Identity, Authentication) + OAuth 2.0 = OpenID Connect**

## Specs

An entity has multiple identities. Facebook extends OAuth with 'signed request' does the same thing as OpenID Connect.  

Final OpenID Connect specifications [2] were launched on February 26, 2014.  

The certification program [3] for OpenID Connect was launched on April 22, 2015.  
Google, Microsoft, Ping Identity, ForgeRock, Nomura Research Institute, and PayPal OpenID Connect deployments were the first to self-certify conformance. 

**IDP** = _identity provider_ = offer authentication as a service 

**RP** = _relying party_ = app that outsources its authentication function to an IDP 

**JWT** = _json web token_ = data structures with signatures 

> From <openid.net: Faq [4]>  

OpenID Connect is a _simple identity layer that works over the top of OAuth 2.0_. It uses the same underlying REST protocol, but adds _consistency_ and _additional security_ on top of the OAuth protocol.  

OAuth 2.0 _is_ fundamentally ~an authorisation protocol~, _not an authentication protocol_.

> From <andrewlock.net: An Introduction To Openid Connect In Asp Net Core [5]>  

+ OpenID Connect Basic Client Implementer's Guide 1.0 - draft 37 [6]
+ OpenID Connect Implicit Client Implementer's Guide 1.0 - draft 20 [7]
+ Safe storage of app secrets during development [8]

## Sequence diagram

![open id sequence](https://s6rk0g-ch3302.files.1drv.com/y4mNlGp93qrvJ_Zsh0EZb_q8a5oi5KVzi76opEWIHT_N7coyJXfQCinzEerB7XgEkd7nvesdWUdMkIm95CNm25mULv3en1CVceZ-24JfV-QeJJflUtN6z76Mu5iM_-h4fOTNGhdyabt9jhndBx9CfnN7XXGDC0eztDBZAIRY8GbjX_kUfIba5FOxnQ5ogDEaf4uGxjjKxv5GNWmHdZuSjymEw?width=811&height=801&cropmode=none)
![sequence diagram](https://1drv.ms/i/s!As0cxZAk26SzjMAaEByL2Qz0DLP5LA)
![sequence diagram](https://g7ucqw.by3302.livefilestore.com/y3mf3_zYz2mPPB2h0Qjk7xv94b29SkaoGo__Xj2UJYS7TmwNCTNfqykyIlZi75yqYTSMpHGYGL6rsLEr6_xo20Yu7ERtYNBojf0sTiDcw_KwNMSpCwxPQxEBFMUU-oFbNDl_HwHmGbonXe5NUmdXKm52ge6QZaIKTxmBsN3iBV9Yjg?width=811&height=801&cropmode=none)

[<<](../ASP.md)
|
[home](../../README.md)
|
wiki [9]

[1]: http://openid.net/connect/
[2]: http://openid.net/2014/02/26/the-openid-foundation-launches-the-openid-connect-standard/
[3]: http://openid.net/2015/04/17/openid-connect-certification-program/
[4]: http://openid.net/connect/faq/
[5]: http://andrewlock.net/an-introduction-to-openid-connect-in-asp-net-core/
[6]: http://openid.net/specs/openid-connect-basic-1_0.html
[7]: http://openid.net/specs/openid-connect-implicit-1_0.html
[8]: https://docs.microsoft.com/en-us/aspnet/core/security/app-secrets
[9]: https://github.com/illegitimis/Tutorial/wiki
