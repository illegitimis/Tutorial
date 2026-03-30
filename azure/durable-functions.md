---
title: Durable Functions
layout: default
nav_order: 17
parent: Azure
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# Durable Functions

> Azure Durable Functions: orchestrator patterns, DTFx backends, and bindings.

## Resources

- Monitor scenario — Weather Watcher sample [1]
- `DurableFunctionsMonitor`: TaskHubNames [2], setup and run [3], Standalone mode [4]
- Create a long-running serverless workflow with Durable Functions [5]
- SPARK Conference Durable Functions Demo [6]
- `azure-functions-core-tools` — command line tools for Azure Functions [7]
- Work with Azure Functions Core Tools [8]

## DTFx Backends

- `DurableTask.AzureStorage` — default backend, least expensive
- `DurableTask.Netherite` — combines Azure Event Hubs with FASTER [9], 10x throughput over Azure Storage
- `DurableTask.SqlServer` — runs everywhere, multitenant

## Important Orchestrator Limitations

Orchestrator code is _replayed on every rehydration_ to restore all local state (local variables, etc).

- Follows the **Event Sourcing** stateful pattern
- Function calls are never replayed — the outputs are remembered

This requires the orchestrator code to be **deterministic**:

- Rule #1: Never write logic that depends on random numbers, `DateTime.Now`, `Guid.NewGuid()`, etc.
- Rule #2: Never do I/O directly in the orchestrator function
- Rule #3: Do not write infinite loops
- Rule #4: Use the built-in workarounds for rules #1, #2, and #3

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

[1]: https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-monitor?tabs=csharp
[2]: https://github.com/microsoft/DurableFunctionsMonitor/blob/main/durablefunctionsmonitor.dotnetbackend/Functions/TaskHubNames.cs
[3]: https://github.com/microsoft/DurableFunctionsMonitor/blob/main/durablefunctionsmonitor.dotnetbackend/setup-and-run.js
[4]: https://github.com/microsoft/DurableFunctionsMonitor/wiki/How-to-run-DfMon-in-Standalone-mode
[5]: https://docs.microsoft.com/en-us/learn/modules/create-long-running-serverless-workflow-with-durable-functions/
[6]: https://github.com/MaximRouiller/spark-durable-demo/
[7]: https://github.com/Azure/azure-functions-core-tools
[8]: https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash
[9]: https://www.microsoft.com/en-us/research/project/faster/

[<](./index.md) | [<<](/index.md)
