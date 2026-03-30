---
title: Polly
layout: default
nav_order: 1
parent: Frameworks and Libraries
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Polly

`Polly` is a .NET resilience and transient-fault-handling library that allows developers to express policies such as **Retry**, **Circuit Breaker**, **Timeout**, **Bulkhead Isolation**, and **Fallback** in a fluent and thread-safe manner [1]. From version 6.0.1, `Polly` targets .NET Standard 1.1 and 2.0+. **PolicyWrap** provides a simple way to combine resilience strategies [2].

Implement HTTP call retries with **exponential backoff** with `IHttpClientFactory` and `Polly` policies [3].

`Polly.Contrib.WaitAndRetry` is an extension library for `Polly` containing helper methods for a variety of _wait-and-retry_ strategies [4].

[1]: https://github.com/App-vNext/Polly
[2]: https://github.com/App-vNext/Polly/wiki/PolicyWrap
[3]: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/implement-http-call-retries-exponential-backoff-polly
[4]: https://github.com/Polly-Contrib/Polly.Contrib.WaitAndRetry

[<](./index.md) | [<<](/index.md)