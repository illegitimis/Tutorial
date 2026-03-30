---
title: Foreground vs Background Threads
layout: default
nav_order: 1
parent: Parallelism
grand_parent: .NET
last_modified_date: 2026-03-29 21:39:07 +00:00
---

# Foreground vs Background Threads

_Thread pool threads are  background threads._

Concerning exception behavior, no difference exists between background and foreground threads: **Unhandled exceptions in either of them terminate the entire process**.

The only altered behavior of a background thread is that _it won’t keep the process from being terminated after all foreground threads have quit_.
In other words, **a foreground thread can keep a process alive until it exits**, whereas a background thread can’t.

[<](./index.md) | [<<](/index.md)
