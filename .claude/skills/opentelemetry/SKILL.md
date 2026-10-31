---
name: opentelemetry
description: '**WORKFLOW SKILL** — Design, instrument, and troubleshoot OpenTelemetry observability solutions. USE FOR: tracing, metrics, logging, exporters, SDK configuration, collector pipelines, and observability best practices for distributed systems. DO NOT USE FOR: non-observability telemetry frameworks or proprietary APM-only vendor lock-in. INVOKES: architecture guidance, configuration examples, SDK usage, and debugging workflows.'
---

# OpenTelemetry Skill

## Overview

This skill supports OpenTelemetry adoption, instrumentation, and operational usage across services, applications, and infrastructure. It helps users choose the right signals, configure SDKs and collectors, wire exporters, and understand tradeoffs between tracing, metrics, and logs.

## Key Capabilities

### Observability Architecture
- Explain OpenTelemetry core concepts: trace, span, context propagation, metrics, and logs.
- Describe the OpenTelemetry Collector architecture and pipeline model.
- Compare OTLP, Jaeger, Prometheus, Zipkin, and vendor-specific exporters.
- Help design telemetry for microservices, serverless, and legacy systems.

### Instrumentation
- Show how to instrument applications in Java, Python, Go, Node.js, .NET, and other SDKs.
- Configure automatic and manual tracing, metrics collection, and semantic conventions.
- Use context propagation headers for distributed transactions.
- Identify useful spans and attributes for service-level telemetry.

### Collector and Exporters
- Build OpenTelemetry Collector pipelines with receivers, processors, exporters, and extensions.
- Configure sampling, batching, resource detection, and retry policies.
- Map telemetry data to observability backends and vendor tools.
- Advise on scaling collectors and securing telemetry transport.

### Metrics and Logs
- Use OpenTelemetry metrics instruments: counters, histograms, gauges, and observers.
- Advise on metric naming, units, and aggregation choices.
- Integrate logs with trace context and correlate logs with spans.
- Explain semantic conventions for log fields and resource attributes.

### Troubleshooting and Best Practices
- Diagnose missing traces, broken context propagation, and exporter failures.
- Explain how to debug collector configuration and verify OTLP traffic.
- Recommend safe sampling rates and performance-conscious instrumentation.
- Help avoid high-cardinality labels, unbounded metrics, and excessive span creation.

## Usage Examples

### Instrument a Java service
- Add the OpenTelemetry Java SDK dependency.
- Configure the OTLP exporter and service resource attributes.
- Create spans around HTTP requests, database calls, and background jobs.
- Propagate context through async callbacks and thread pools.

### Configure a collector pipeline
- Use `receivers:
    otlp:
      protocols:
        grpc: {}
        http: {}`
- Add processors for batching, memory_limiter, and attributes.
- Export to `jaeger`, `prometheus`, or a cloud provider backend.

### Create metrics in Python
- Use `Counter`, `Histogram`, or `ObservableGauge`.
- Record measurements with useful units and labels.
- Export metrics with OTLP or Prometheus endpoint.

### Correlate logs with traces
- Inject trace context into application logs.
- Use structured logging or OpenTelemetry log instrumentation.
- Query traces and logs together in the observability backend.

## Common Patterns

### OpenTelemetry Collector YAML

```yaml
receivers:
  otlp:
    protocols:
      grpc: {}
      http: {}
processors:
  batch:
  memory_limiter:
    limit_mib: 400
    spike_limit_mib: 100
    check_interval: 5s
exporters:
  otlp:
    endpoint: "otel-collector:4317"
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [otlp]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
```

### Java property configuration

```properties
otel.resource.attributes=service.name=orders-service,service.version=1.2.0
otel.traces.exporter=otlp
otel.metrics.exporter=otlp
otel.exporter.otlp.endpoint=http://otel-collector:4317
```

### Python OTLP setup

```python
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(TracerProvider())
span_processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317"))
trace.get_tracer_provider().add_span_processor(span_processor)
```

## Best Practices

- Instrument only meaningful operations and avoid span explosion.
- Use semantic conventions consistently to make traces searchable.
- Correlate traces, logs, and metrics where possible.
- Prefer the Collector for centralized processing and export control.
- Capture resource metadata such as service name, deployment environment, and host ID.
- Monitor the overhead and adjust sampling or batching when needed.

## Troubleshooting

- If no telemetry appears, verify endpoint reachability and collector logs.
- If traces are incomplete, check context propagation and parent/child span relationships.
- If metrics are missing, ensure the correct exporter and instrument registration.
- If logging integration fails, validate log context injection and exporter configuration.

## When to Use This Skill

- Designing an OpenTelemetry strategy for service monitoring and distributed tracing.
- Writing or reviewing instrumentation and collector configurations.
- Debugging telemetry ingestion, exporter failures, or missing observability data.
- Advising on observability tradeoffs and safe telemetry practices.
