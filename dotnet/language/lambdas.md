---
title: Lambdas
layout: default
nav_order: 9
parent: "C# Language"
grand_parent: .NET
last_modified_date: 2026-03-29 21:15:03 +00:00
---

# Lambdas

- Provide delegates, `Expression<T>` **where T is not a delegate type**
- `Expression<T>` where T is a delegate type.
- ability to produce an object model for an expression: `Expression<Func<int, bool>> greaterThanZero = value => value > 0;`
- Beneath the hood

```cs
ParameterExpression valueParam = Expression.Parameter(typeof(int), "value");
ConstantExpression constantZero = Expression.Constant(0);
BinaryExpression comparison = Expression.GreaterThan(valueParam, constantZero);
Expression<Func<int, bool>> greaterThanZero = Expression.Lambda<Func<int, bool>>(comparison, valueParam);  
```

[<](./index.md) | [<<](/index.md)
