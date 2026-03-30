---
title: Auth0
layout: default
nav_order: 11
parent: ASP.NET
grand_parent: .NET
last_modified_date: 2026-03-31 00:00:00 +00:00
---

# Auth0

`Auth0` quick start [1]: SPA, web app, mobile, APIs

Login: through your app via a page you host (**Embedded**) or `Auth0` hosts (**Universal**) \
**Universal Login** [2]: redirect, MFA, social, dynamic, no app changes \
**Embedded Login** [3]: not recommended; log directly to your app, transmit credentials to `Auth0` server \
**Single Sign-On** [4] \
**Sessions**: locally maintained | authorization server with SSO | IdP if social \
A central domain performs authentication and then shares the session with other domains \
SSO is only possible with native platforms (like iOS or Android) if the application uses **Universal Login**

| Acronym | Flavor | Provider | Direction |
|:---:|:---:|:---:|:---:|
| **SP** [5] | Service-Provider-initiated | `Auth0` | inbound |
| **IP** [6] | Identity-Provider-initiated | a third-party Identity Provider | outbound |
| **Native to Web** [7] | Native to Web | | |

## Glossary

| Term | Description |
|---|---|
| ASN | Authorized Services Network |
| B2B | business to business |
| CIBA | **Client-Initiated Backchannel Authentication** |
| _IdP_ | _Identity Provider_. Service that stores and manages digital identities. `Auth0` supports trusted social, enterprise, and legal identity providers. |
| FGA | fine-grained authorization |
| JWT | **JSON Web Token** |
| LDAP | **Lightweight Directory Access Protocol** |
| M2M | Machine-to-Machine |
| MFA | **Multi-factor Authentication** |
| **OAuth 2.0** | _Authorization_ framework that defines authorization protocols and workflows, roles, authorization [8] requests and responses, and token handling |
| **OIDC** | **OpenID Connect** _authentication_; extends **OAuth 2.0** with protocols to verify user identity |
| PKCE | **Proof Key for Code Exchange** |
| RBAC | **Role-Based Access Control** |

[1]: https://auth0.com/docs/quickstarts
[2]: https://auth0.com/docs/authenticate/login/auth0-universal-login#configure-universal-login
[3]: https://auth0.com/docs/authenticate/login/embedded-login
[4]: https://auth0.com/docs/authenticate/single-sign-on
[5]: https://auth0.com/docs/authenticate/single-sign-on/inbound-single-sign-on
[6]: https://auth0.com/docs/authenticate/single-sign-on/outbound-single-sign-on
[7]: https://auth0.com/docs/authenticate/single-sign-on/native-to-web
[8]: https://auth0.com/docs/get-started/identity-fundamentals/authentication-and-authorization

[<](./index.md) | [<<](/index.md)
