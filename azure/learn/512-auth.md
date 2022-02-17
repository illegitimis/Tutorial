## Compare authentication and authorization

Recall that Tailwind Traders must ensure that only employees can sign in and access its business applications.

Tailwind Traders also needs to ensure that employees can access only authorized applications. For example, all employees can access inventory and pricing software, but only store managers can access payroll and certain accounting software.

Two fundamental concepts that you need to understand when talking about identity and access are authentication (AuthN) and authorization (AuthZ).

Authentication and authorization both support everything else that happens.
They occur sequentially in the identity and access process.

Let's take a brief look at each.

## What is authentication?

Authentication is the process of _establishing the identity_ of a person or service that wants to access a resource. It involves the act of _challenging a party for legitimate credentials_ and provides the basis for creating a security principal for identity and access control. It establishes whether the user is _who they say they are_.

## What is authorization?

Authentication establishes the user's identity, but authorization is the process of establishing what _level of access_ an authenticated person or service has. It specifies what data they're allowed to access and what they can do with it.

## How are authentication and authorization related?

Here's a diagram that shows the relationship between authentication and authorization:

![alt](https://docs.microsoft.com/en-us/learn/azure-fundamentals/secure-access-azure-identity-services/media/2-id-card-access.png)

A diagram that shows an identification card and the various kinds of resources the user can access.
The identification card represents the user's credentials.

The identification card represents credentials that the user has to prove their identity (you'll learn more about the types of credentials later in this module.) Once authenticated, authorization defines what kinds of applications, resources, and data that user can access.

[< 5: Describe identity, governance, privacy, and compliance features](./5-lp-az-900.md)