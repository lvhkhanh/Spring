---
name: kql
description: '**WORKFLOW SKILL** — Write, review, optimize, and explain KQL/Kusto queries for Azure Monitor, Log Analytics, Application Insights, Microsoft Sentinel, and Azure Data Explorer investigations. USE FOR: telemetry analysis, failed request and exception correlation, performance traces, security hunting, dashboard queries, alert logic, and query tuning. DO NOT USE FOR: relational SQL, database schema migration, or non-Kusto analytics unless translating into KQL is the explicit goal. INVOKES: file system tools for query artifacts, terminal or cloud tools only for read-only query validation when credentials and approval are available.'
---

# KQL Investigation Skill

## Overview

This skill supports Kusto Query Language work across Azure Monitor, Log Analytics, Application Insights, Microsoft Sentinel, and Azure Data Explorer. It focuses on safe, time-bounded investigation queries, readable transformations, and clear validation steps.

## Key Capabilities

### Query Authoring
- Build KQL queries with `where`, `project`, `extend`, `summarize`, `join`, `union`, `parse`, `mv-expand`, and time binning.
- Create incident investigation queries for failed requests, exceptions, traces, dependencies, availability tests, and custom events.
- Produce alert-ready queries with stable thresholds, windows, and dimensions.
- Translate observability questions into scoped query plans before writing final KQL.

### Investigation Patterns
- Correlate requests, exceptions, dependencies, and traces by operation or correlation identifiers.
- Compare error rates before and after deployments or configuration changes.
- Detect latency regressions using percentiles and outlier grouping.
- Summarize activity by cloud role, endpoint, result code, user, IP, region, or resource.

### Review and Optimization
- Check table names, timestamp fields, filters, join keys, and cardinality risks.
- Prefer selective time windows and early filtering before joins or unions.
- Replace noisy columns with focused projections.
- Explain performance tradeoffs and suggest safer query shapes.

## Usage Examples

### Failed Request Investigation
```kusto
requests
| where timestamp > ago(24h)
| where success == false
| summarize failures=count(), sampleOperationIds=make_set(operation_Id, 5) by name, resultCode
| order by failures desc
```

### Correlate Exceptions to Requests
```kusto
let failedRequests =
    requests
    | where timestamp > ago(24h)
    | where success == false
    | project operation_Id, requestName=name, resultCode, requestTime=timestamp;
exceptions
| where timestamp > ago(24h)
| join kind=inner failedRequests on operation_Id
| project requestTime, requestName, resultCode, exceptionType=type, problemId, outerMessage
| order by requestTime desc
```

### Latency Trend
```kusto
requests
| where timestamp > ago(7d)
| summarize p50=percentile(duration, 50), p95=percentile(duration, 95), p99=percentile(duration, 99) by bin(timestamp, 1h), name
| order by timestamp asc
```

## Best Practices

- Always start with a time filter such as `timestamp > ago(24h)` or `TimeGenerated > ago(24h)`.
- Confirm whether the workspace uses classic Application Insights tables (`requests`, `exceptions`) or Azure Monitor tables (`AppRequests`, `AppExceptions`).
- Project only the columns needed for investigation or alert output.
- Use `summarize` with `bin()` for trends and `percentile()` for latency analysis.
- Prefer `join kind=innerunique`, `leftouter`, or `inner` intentionally and explain why.
- Avoid broad `union *` unless the user explicitly asks for discovery.
- Treat query execution as read-only; do not change Azure resources or alert rules without explicit approval.

## Troubleshooting

### Empty Results
- Check the time range and timestamp column name.
- Confirm table names and workspace scope.
- Remove restrictive filters one at a time.
- Verify ingestion delay for recent telemetry.

### Slow Queries
- Reduce the time window.
- Filter before `join`, `union`, `parse`, or `mv-expand`.
- Project fewer columns before expensive operations.
- Summarize before joining when exact row-level correlation is not required.

## Integration Points

- **Azure Monitor / Log Analytics**: operational telemetry and resource logs.
- **Application Insights**: application requests, dependencies, traces, exceptions, and custom events.
- **Microsoft Sentinel**: security hunting and detection logic.
- **Azure Data Explorer**: larger Kusto analytics workloads.
