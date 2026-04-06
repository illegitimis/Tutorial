---
title: Gantt Charts
layout: default
nav_order: 3
parent: Mermaid
grand_parent: DevOps
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# Mermaid Gantt Charts

[Gantt chart syntax][1]

> Bar Chart

```mermaid
gantt
    title Git Issues - days since last update
    dateFormat X
    axisFormat %s
    section Issue19062
    71   : 0, 71
    section Issue19401
    36   : 0, 36
    section Issue193
    34   : 0, 34
    section Issue7441
    9    : 0, 9
    section Issue1300
    5    : 0, 5
```

> Comments need to be on their own line and must be prefaced with %%

```mermaid
gantt
    title A Gantt Diagram
    %% this is a comment
    dateFormat  YYYY-MM-DD
    section Section
    A task: a1, 2014-01-01, 30d
    Another task: after a1, 20d
    section Another
    Task in sec: 2014-01-12, 12d
    another task: 24d
```

> Compact display optimizes screen real estate

```mermaid
---
displayMode: compact
---
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD

    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :a2, 2014-01-20, 25d
    Another one      :a3, 2014-02-10, 20d
```

## Date Formats

type | format | def
--- | --- | ---
date | %c | date and time, as "%a %b %e %H:%M:%S %Y"
month | %B | full month name
month | %b | abbreviated month name
month | %m | month as a decimal number [01,12]
week | %U | week number of the year (Sunday as the first day of the week) as a decimal number [00,53]
week | %W | week number of the year (Monday as the first day of the week) as a decimal number [00,53]
weekday | %w | weekday as a decimal number [0(Sunday),6]
weekday | %A | full weekday name
day of month | %d | zero-padded day of the month as a decimal number [01,31]
day of month | %e | space-padded day of the month as a decimal number [ 1,31]; equivalent to %_d

## Trial Activity Report

```mermaid
%% ---
%% displayMode: compact
%% ---
gantt
    title Trial activity report
    %% dateFormat  YYYY-MM-DD-HH
    dateFormat  YYYY-MM-DD
    %% axisFormat %m-%b-%H
    %% axisFormat %B-%W-%d-%w
    %% axisFormat %A-%e
    %% axisFormat %Y-%m-%d
    axisFormat %b-%d-%a
    tickInterval 1day
    %% todayMarker off
    excludes weekends

    section PBI1
    task 01 2h : t1, 2023-06-05, 6h
    PR task 01: pr1, after t1, 2h
    Cloudtest 01: done, ci1, after pr1, 0h
    section PBI2
    task 02: active, t2, 2023-06-06, 15h
    PR task 02: pr2, 2023-06-07, 12h
    task 03: t3, 2023-06-08, 8h    
    task 04: t4, after t3, 8h
    section PBI3
    task 03: t3, 2023-06-09, 23h
    PR task 03: milestone, pr3, after t3, 1h
    task 04: t4, 2023-06-12, 10h
    pr 04: pr04, after t4, 8h    
    ci 04: crit, ci04, after pr04, 2h    
    section PBI4
    Initial milestone: milestone, m1, 2023-06-13, 3d
    task qwe : done, tqwe, 2023-06-13, 1d
    task asd : done, tasd, after tqwe, 12h
    task zxc : active, tzxc, after tasd, 18h
    Final milestone : milestone, m2, after tzxc, 1h
```

## Time Tracking

```mermaid
---
displayMode: compact
---
gantt
    title Time Tracking
    dateFormat X
    axisFormat %s
    tickInterval 1
    section Issue19062
    code: 0, 2
    pr: 3, 4
    so: 5,8 
    section Issue19401
    code   : 0, 8
    pr   : 0, 8
    section Issue193
    code   : 0, 3
    pr: 4,8
    section Issue7441
    cloud : 0, 8
    test : 0, 8
    section Issue1300
    5    : 0, 5
```

## User Journey

```mermaid
journey
    title My working day
    actor code
    actor cloudtest

    section Task 01
      Code: 5: code
      CloudTest: 3: cloudtest
    section Task 02
      Code: 5: code
      CloudTest: 5: cloudtest
```

[<](./index.md) | [<<](/index.md)

[1]: https://mermaid.js.org/syntax/gantt.html
