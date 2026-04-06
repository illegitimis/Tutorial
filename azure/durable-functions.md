---
title: Durable Functions
layout: default
nav_order: 17
parent: Azure
last_modified_date: 2026-04-06 00:00:00 +0000
---

# Durable Functions

> Azure Durable Functions: COAE pattern, application patterns, orchestrator constraints, DTFx backends, bindings, and timer triggers.

## Resources

- Monitor scenario — Weather Watcher sample [1]
- `DurableFunctionsMonitor`: TaskHubNames [2], setup and run [3], Standalone mode [4]
- Create a long-running serverless workflow with Durable Functions [5]
- SPARK Conference Durable Functions Demo [6]
- `azure-functions-core-tools` — command line tools for Azure Functions [7]
- Work with Azure Functions Core Tools [8]
- `Microsoft.Azure.WebJobs.Extensions.DurableTask` NuGet package [23]

## COAE Pattern

Durable Functions are built around four function types:

- **Client** function — entry point that starts orchestrations
- **Orchestrator** function — defines the workflow as code
- **Activity** function — performs a single unit of work
- **Entity** function — manages durable state (Durable Entities)

## Application Patterns

| Pattern | Description |
|---------|-------------|
| **Function Chaining** | a sequence of functions executes in order, output feeds the next |
| **Fan-Out/Fan-In** | multiple functions execute in parallel, then aggregate results |
| **Async HTTP APIs** | coordinates long-running operations with external clients via polling |
| **Monitor** | recurring process that observes and reacts to external state changes |
| **Human Interaction** | pauses workflow waiting for an external event (approval, etc.) |
| **Aggregator** (entity) | aggregates event data over time into a single addressable entity |

## Orchestrations

- Orchestrators can call activity functions, other orchestrators (**sub-orchestrations**), wait for external events, and use HTTP and timers
- Sub-orchestrations support composition and parallel fan-out across child workflows

## Entity Functions

**Durable Entities** provide a state management primitive:

- Addressable by entity ID (entity name + key)
- Support operation-based access (signal and call)
- Entities serialize between operations — one operation at a time per entity
- Two programming models: **function-based** and **class-based**

## DTFx Backends

- `DurableTask.AzureStorage` — default backend, least expensive
- `DurableTask.Netherite` — combines Azure Event Hubs with FASTER [9], 10x throughput over Azure Storage
- `DurableTask.SqlServer` — runs everywhere, multitenant

## Task Hubs

A **task hub** is a logical container for storage resources used by orchestrations and entities:

- Orchestrator and entity instances interact within the same task hub
- Default backend uses Azure Storage queues, tables, and blobs scoped to a single task hub name

## Instance Management

- Query all instances, query with filters, send events to instances
- Terminate, rewind, suspend, and resume instances
- Purge instance history

## Important Orchestrator Limitations

Orchestrator code is _replayed on every rehydration_ to restore all local state (local variables, etc).

- Follows the **Event Sourcing** stateful pattern
- Function calls are never replayed — the outputs are remembered

This requires the orchestrator code to be **deterministic**:

- Rule #1: Never write logic that depends on random numbers, `DateTime.Now`, `Guid.NewGuid()`, etc.
- Rule #2: Never do I/O directly in the orchestrator function
- Rule #3: Do not write infinite loops
- Rule #4: Use the built-in workarounds for rules #1, #2, and #3

### Code Constraints

- No `Thread.Sleep` or `Task.Delay` — use `CreateTimer`
- No `DateTime.Now` or `DateTime.UtcNow` — use `CurrentUtcDateTime`
- No random — pass random values from activity functions
- No environment variables — pass configuration from activity functions

## Versioning

- **Side-by-side** — deploy new version alongside old; route new instances to new code
- **Slot swap** — deploy to staging slot, then swap
- Avoid breaking changes to serialized orchestration state

## Bindings

> **Trigger** / **Non-Trigger** Bindings

- **Orchestration** Trigger Binding: triggers orchestrator functions, polls control-queue, partition-aware, handles return values
- **Activity** Trigger Binding: triggers activity functions, polls work-item queue, stateless, handles return values
- **Orchestrator** Client: output binding, start new orchestrator instances, terminate instances, send event notifications, fetch instance status

## Azure Storage

- Queues: scheduled execution of activity functions
- Table Storage: `<taskhub>History` contains execution history of all activities ran by orchestrator. `<taskhub>Instances` contains all the orchestrator instances ever started.
- Blob Storage: used when Queues/Table Storage hits size limits

## Actors/Monitor Pattern

> **Eternal Orchestrations**

```cs
public static async Task Run(DurableOrchestrationContext ctx)
{
    int counterState = ctx.GetInput<int>();

    string operation = await ctx.WaitForExternalEvent<string>("operation");

    if (operation == "incr")
    {
        counterState++;
    }
    else if (operation == "decr")
    {
        counterState--;
    }

    ctx.ContinueAsNew(counterState);
}
```

```cs
public static async Task Run(DurableOrchestrationContext ctx)
{
    var jobInfo = ctx.GetInput<JobInfo>();

    while (ctx.CurrentUtcDateTime < jobInfo.ExpiryTime)
    {
        string status = await ctx.CallActivityAsync<string>("GetStatus", jobInfo);
        if (status == "Completed")
        {
            await ctx.CallActivityAsync<string>("SendAlert", jobInfo);
            break;
        }

        DateTime nextCheck = ctx.CurrentUtcDateTime.AddSeconds(30);
        await ctx.CreateTimer(nextCheck, CancellationToken.None);
    }
}
```

## Official Documentation

- What are Durable Functions? [10] — application patterns (chaining, fan-out/fan-in, async HTTP, monitor, human interaction, aggregator)
- Durable Functions types and features [11]
- Durable orchestrations [12] — orchestration identity, reliability, history
- Sub-orchestrations [13]
- Entity functions [14] — entity ID, operations, access, and coordination
- Developer's guide to durable entities in .NET [15] — definition, requirements, dependency injection, function-based syntax
- Bindings for Durable Functions [16] — orchestration, activity, entity triggers and `host.json`
- Task hubs [17]
- Manage instances [18] — start, query, terminate, send events, rewind, purge
- Timers [19] — custom timeout and delay on `IDurableOrchestrationContext`
- Orchestrator function code constraints [20]
- Durable Functions versions overview [21]
- Implement Durable Functions [22] — MS Learn module
- `Microsoft.Azure.WebJobs.Extensions.DurableTask` [23]
- Guide for running C# Azure Functions in an isolated process [24]

## Timer Triggers

- Timer trigger for Azure Functions [25]
- Dynamically set schedule in Azure Function [26]
- Create a function in the Azure portal that runs on a schedule [27]
- Azure Functions — Timer Triggers — Configurable Scheduled Expressions [28]

[1]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-monitor?tabs=csharp
[2]: https://github.com/microsoft/DurableFunctionsMonitor/blob/main/durablefunctionsmonitor.dotnetbackend/Functions/TaskHubNames.cs
[3]: https://github.com/microsoft/DurableFunctionsMonitor/blob/main/durablefunctionsmonitor.dotnetbackend/setup-and-run.js
[4]: https://github.com/microsoft/DurableFunctionsMonitor/wiki/How-to-run-DfMon-in-Standalone-mode
[5]: https://docs.microsoft.com/en-us/learn/modules/create-long-running-serverless-workflow-with-durable-functions/
[6]: https://github.com/MaximRouiller/spark-durable-demo/
[7]: https://github.com/Azure/azure-functions-core-tools
[8]: https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash
[9]: https://www.microsoft.com/en-us/research/project/faster/
[10]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=csharp#application-patterns
[11]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-types-features-overview
[12]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-orchestrations?tabs=csharp
[13]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-sub-orchestrations?tabs=csharp
[14]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-entities?tabs=csharp
[15]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-dotnet-entities
[16]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-bindings?tabs=csharp%2C2x-durable-functions
[17]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-task-hubs
[18]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-instance-management?tabs=csharp
[19]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-timers?tabs=csharp
[20]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-code-constraints?tabs=csharp
[21]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-versions
[22]: https://docs.microsoft.com/en-us/learn/modules/implement-durable-functions/
[23]: https://www.nuget.org/packages/Microsoft.Azure.WebJobs.Extensions.DurableTask
[24]: https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide
[25]: https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=in-process&pivots=programming-language-csharp
[26]: https://stackoverflow.com/questions/45564848/dynamically-set-schedule-in-azure-function
[27]: https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-scheduled-function
[28]: https://praveenkumarsreeram.com/2020/08/06/azure-functions-timer-triggers-configurable-scheduled-expressions/

[<](./index.md) | [<<](/index.md)
