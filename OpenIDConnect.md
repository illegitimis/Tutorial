# OpenID Connect

[OpenID Connect](http://openid.net/connect/) is an interoperable authentication protocol based on the OAuth 2.0 family of specifications. It uses straightforward REST/JSON message flows with a design goal of “_making simple things simple and complicated things possible_”. It’s uniquely easy for developers to integrate, compared to any preceding Identity protocol. 

An entity has multiple identities. Facebook extends OAuth with 'signed request' does the same thing as OpenID Connect.  

**(Identity, Authentication) + OAuth 2.0 = OpenID Connect** 

[Final OpenID Connect specifications](http://openid.net/2014/02/26/the-openid-foundation-launches-the-openid-connect-standard/) were launched on February 26, 2014.  

[The certification program](http://openid.net/2015/04/17/openid-connect-certification-program/) for OpenID Connect was launched on April 22, 2015.  Google, Microsoft, Ping Identity, ForgeRock, Nomura Research Institute, and PayPal OpenID Connect deployments were the first to self-certify conformance. 

**IDP** = _identity provider_ = offer authentication as a service 

**RP** = _relying party_ = app that outsources its authentication function to an IDP 

**JWT** = _json web token_ = data structures with signatures 

> From <http://openid.net/connect/faq/>  

OpenID Connect is a _simple identity layer that works over the top of OAuth 2.0_. It uses the same underlying REST protocol, but adds _consistency_ and _additional security_ on top of the OAuth protocol.  

OAuth 2.0 _is_ fundamentally _an authorisation protocol_, _not an authentication protocol_.

> From <http://andrewlock.net/an-introduction-to-openid-connect-in-asp-net-core/>  

![sequence diagram](https://g7ucqw.by3302.livefilestore.com/y3mf3_zYz2mPPB2h0Qjk7xv94b29SkaoGo__Xj2UJYS7TmwNCTNfqykyIlZi75yqYTSMpHGYGL6rsLEr6_xo20Yu7ERtYNBojf0sTiDcw_KwNMSpCwxPQxEBFMUU-oFbNDl_HwHmGbonXe5NUmdXKm52ge6QZaIKTxmBsN3iBV9Yjg?width=811&height=801&cropmode=none)

### OpenID Connect Basic Client Implementer's Guide 1.0 - draft 37 
> From <http://openid.net/specs/openid-connect-basic-1_0.html>  

### OpenID Connect Implicit Client Implementer's Guide 1.0 - draft 20 
> From <http://openid.net/specs/openid-connect-implicit-1_0.html>  

### Safe storage of app secrets during development 
> From <https://docs.microsoft.com/en-us/aspnet/core/security/app-secrets>

