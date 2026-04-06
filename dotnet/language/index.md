---
title: "C# Language"
layout: minimal
nav_order: 3
has_children: true
parent: .NET
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# C# Language

> Core C# language constructs covering type system features, functional patterns, and performance-oriented collections.

## Pages

- [Delegates](./delegates.md) — **multicast delegates** as the foundation for callbacks and notifications
- [Events](./events.md) — event-based notification patterns built on top of delegates
- [Lambdas](./lambdas.md) — lambda expressions, `Expression<T>`, and delegate/expression tree duality
- [Anonymous Types](./anonymous-types.md) — compiler-generated immutable projection types for on-the-fly composition
- [Co/Contra Variance](./co-contra-variance.md) — generic type compatibility rules: covariance and contravariance
- [Collections Performance](./collections-performance.md) — performance comparison of `Dictionary`, `List`, `HashSet`, and other collection types
- [Exceptions](./exceptions.md) — stack trace preservation, `throw` vs `throw ex`, and exception handling patterns
- [Immutable Types](./immutable-types.md) — immutability patterns, `Lookup<K,V>`, and value-type design guidelines
- [Interfaces](./interfaces.md) — `IComparable`, `IEnumerable`, and interface contract patterns
- [Managed C++/CLI](./managed-cpp-cli.md) — C++/CLI syntax as the successor to Managed C++ for .NET interop
- [Rx](./rx.md) — **Reactive Extensions** (Rx.NET): observables, events, and tuple deconstruction

## Notnull Constraint

The **non-null** constraint uses the contextual keyword `notnull`. Triggers a warning if a nullable type is specified for the decorated type parameter.

```cs
public class EntityDictionary<TKey, TValue> :
    System.Collections.Generic.Dictionary<TKey, TValue>
    where TKey : notnull
    where TValue : EntityBase
```

[<](../index.md) | [<<](/index.md)
