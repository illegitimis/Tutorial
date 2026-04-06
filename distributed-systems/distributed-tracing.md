---
title: Distributed Tracing
layout: default
nav_order: 10
parent: Distributed Systems
last_modified_date: 2026-04-06 00:00:00 +00:00
---

# Distributed Tracing

**Distributed tracing** activity IDs [1] \
**Trace Context** W3C specification [2] \
`opentelemetry-dotnet` getting started [3] \
Extending the `OpenTelemetry` .NET SDK [4] \
Collect a distributed trace [5] \
`System.Diagnostics.DiagnosticSource` [6]

## OpenTelemetry

.NET observability with `OpenTelemetry` [7] \
Creating metrics [8] \
Collect metrics [9] \
**OpenTelemetry** Protocol Exporter [10] \
HTTP Configuration Settings [11] \
Making Azure the Best Place to Observe Your Apps with `OpenTelemetry` [12]

## Logging

Logging in C# and .NET [13]

## Monitoring

`Prometheus` query examples [14] \
`Grafana` Docker image [15]

## Jaeger

Export to `Jaeger` [16] — learn how to export traces to Jaeger with `OpenTelemetry` .NET \
**OTLP** Exporter Configuration [17] \
`JaegerGettingStarted` [18] — getting started OTLP with Jaeger \
How to Setup and Run Jaeger with `Docker` and `Docker Compose` [19] \
Frontend UI [20]

## Samples

Example: use `OpenTelemetry` with `Prometheus`, `Grafana`, and `Jaeger` [21] \
`Codebreaker.ServiceDefaults` Extensions [22] \
Duration, metric, trace gist [23] \
API metric demo [24] \
Docker Compose — `Prometheus` / `Grafana` / `PostgreSQL` / pgadmin / node API [25] \
Failover monitoring [26]

## Local Endpoints

```txt
http://localhost:5059/metrics
http://localhost:16686/trace/875932bd700b850983c16e9235b56462
http://localhost:9090/targets
```

[<](./index.md) | [<<](/index.md)

[1]: https://learn.microsoft.com/en-us/dotnet/core/diagnostics/distributed-tracing-concepts#activity-ids
[2]: https://www.w3.org/TR/trace-context/
[3]: https://github.com/open-telemetry/opentelemetry-dotnet#getting-started
[4]: https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/docs/logs/extending-the-sdk/README.md#processor
[5]: https://learn.microsoft.com/en-us/dotnet/core/diagnostics/distributed-tracing-collection-walkthroughs#collect-traces-using-custom-logic
[6]: https://www.nuget.org/packages/System.Diagnostics.DiagnosticSource/
[7]: https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-with-otel
[8]: https://learn.microsoft.com/en-us/dotnet/core/diagnostics/metrics-instrumentation
[9]: https://learn.microsoft.com/en-us/dotnet/core/diagnostics/metrics-collection
[10]: https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md
[11]: https://github.com/open-telemetry/opentelemetry-collector/blob/main/config/confighttp/README.md
[12]: https://techcommunity.microsoft.com/blog/azureobservabilityblog/making-azure-the-best-place-to-observe-your-apps-with-opentelemetry/3995896
[13]: https://learn.microsoft.com/en-us/dotnet/core/extensions/logging/overview?tabs=command-line
[14]: https://prometheus.io/docs/prometheus/latest/querying/examples/
[15]: https://hub.docker.com/r/grafana/grafana/tags
[16]: https://opentelemetry.io/docs/languages/dotnet/traces/jaeger/
[17]: https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#otel_exporter_otlp_endpoint
[18]: https://github.com/benkemt/JaegerGettingStarted/tree/master
[19]: https://citizix.com/how-to-setup-and-run-jaeger-with-docker-and-docker-compose/
[20]: https://www.jaegertracing.io/docs/2.14/deployment/frontend-ui/
[21]: https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-prgrja-example
[22]: https://github.com/PacktPublishing/Pragmatic-Microservices-with-CSharp-and-Azure/blob/main/ch11/Codebreaker.ServiceDefaults/Extensions.cs
[23]: https://gist.github.com/JerryNixon/2314602cdfc77d2d3d13bb6a4b33bc82#file-metric-cs
[24]: https://github.com/axzxs2001/Asp.NetCoreExperiment/blob/master/Asp.NetCoreExperiment/DOTNET8/APIMetricDemo/Program.cs
[25]: https://github.com/JawherKl/node-api-postgres/blob/main/docker-compose.yml
[26]: https://github.com/muslumozturk61/fail-over-monitoring/blob/main/FailoverSample/Program.cs
