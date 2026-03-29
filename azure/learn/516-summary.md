# Summary

Tailwind Traders needs to ensure that only its workforce can access [1] its growing set of cloud applications, both from any location and from any device.

In building out its plan, Tailwind Traders learns that:

- Authentication (`AuthN`) establishes the user's identity.
- Authorization (`AuthZ`) establishes the level of access that an authenticated user has.
- Single sign-on (`SSO`) enables a user to sign in one time and use that credential to access multiple resources and applications.
- Azure Active Directory (`Azure AD`) is a cloud-based identity and access management service. Azure AD enables an organization to control access to apps and resources based on its business requirements.
- Azure AD Multi-Factor Authentication `MFA` provides additional security for identities by requiring two or more elements to fully authenticate. In general, multifactor authentication can include something the user knows, something the user has, and something the user is.
- `Conditional Access` is a tool that Azure AD uses to allow or deny access to resources based on identity signals such as the user's location.

With these ideas in place, the software development and IT administrator teams can begin to replace their existing authentication systems with ones that use multiple factors and allow access to multiple applications.

## Learn More

Here are more resources to help you go further:

- start free [2]
- Compare Active Directory to Azure Active Directory docs [3]
- Azure Active Directory * [4]
- What is single sign-on (SSO)? docs [5]
- Azure Active Directory Seamless Single Sign-On [6]
- What is Azure AD Connect? docs [7]
- Azure AD Multi-Factor Authentication docs [8]
- Azure AD Conditional Access entrypoint [9]
- Microsoft identity platform and OpenID Connect protocol docs [10]
- Single Sign-On SAML protocol docs [11]

## Misc SSO

- directory sync: only usernames from on prem ad to aad
- password hash sync: securely sync hashes of passwords to the cloud
- in both cases above, auth is in the cloud
- if on prem is needed, adfs required
- pass-through auth needs agent in intra and aad connect, zero mngmt and auto update and no additional infrastructure. public key outbound https
- bridge between on prem and aad. js to get kerberos ticket
- aad connect cfg. choose pass-through and enable sso, disable pass hashes (wizard), disable federation (blade)
- group policy, edit site to zone assignment list

[< 5: Describe identity, governance, privacy, and compliance features](./5-lp-az-900.md)

[1]: https://docs.microsoft.com/en-us/learn/modules/secure-access-azure-identity-services/6-summary
[2]: https://azure.microsoft.com/en-us/free/
[3]: https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-compare-azure-ad-to-ad
[4]: https://azure.microsoft.com/en-us/services/active-directory/#overview
[5]: https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on
[6]: https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-sso
[7]: https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-azure-ad-connect
[8]: https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks
[9]: https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/
[10]: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc
[11]: https://docs.microsoft.com/en-us/azure/active-directory/develop/single-sign-on-saml-protocol
