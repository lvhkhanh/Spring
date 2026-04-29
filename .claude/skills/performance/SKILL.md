---
name: performance
description: '**WORKFLOW SKILL** — Analyze, optimize, and validate software and system performance across application, database, frontend, backend, and infrastructure layers. USE FOR: profiling slow paths, diagnosing bottlenecks, improving latency and throughput, reducing resource usage, tuning queries and runtime behavior, and planning safe performance experiments. DO NOT USE FOR: speculative micro-optimizations without measurement, hiding functional defects behind caching or retries, or sacrificing correctness, security, or maintainability for negligible speed gains. INVOKES: file system tools for code and config review, terminal tools for profiling and benchmark workflows, semantic search for stack-specific optimization patterns and measurement guidance.'
---

# Performance Engineering Skill

## Overview

This skill provides structured support for understanding and improving performance across applications, services, databases, user interfaces, and runtime environments. It focuses on measuring real behavior, identifying the dominant bottleneck, applying proportionate optimizations, and validating that changes improve latency, throughput, efficiency, or scalability without causing regressions.

## Key Capabilities

### Performance Investigation
- Reproduce slow behavior with clear scope and representative inputs
- Separate perceived slowness from measured latency, throughput, or resource issues
- Identify whether the primary bottleneck is CPU, memory, I/O, network, locking, rendering, or query behavior
- Prioritize the highest-impact bottleneck instead of optimizing noise

### Profiling and Measurement
- Use logs, traces, metrics, profilers, and benchmarks to gather evidence
- Compare baseline and post-change performance with consistent measurement conditions
- Evaluate p50, p95, p99 latency, throughput, error rate, and resource consumption
- Distinguish steady-state inefficiency from spikes, warmup effects, and contention

### Optimization Across Layers
- Improve backend code paths, batching, concurrency, and data access patterns
- Tune SQL queries, indexes, caching, and data-shaping strategies
- Improve frontend rendering, bundle weight, loading behavior, and interaction responsiveness
- Review infrastructure settings such as connection pools, thread limits, memory sizing, and caching layers

### Scalability and Capacity Planning
- Identify how performance changes under higher load, concurrency, or dataset growth
- Evaluate tradeoffs between latency, throughput, consistency, and cost
- Plan experiments for load testing, stress testing, and capacity validation
- Surface risks such as lock contention, queue buildup, hot partitions, and thundering herd effects

### Safe Validation and Regression Protection
- Confirm that optimizations preserve correctness and user-visible behavior
- Validate that performance gains are meaningful rather than statistical noise
- Add monitoring, benchmarks, or regression checks for critical hot paths
- Document assumptions, constraints, and remaining bottlenecks after changes

## Usage Examples

### Diagnose a Slow API
```
Analyze why this API endpoint is slow under load.
Use logs, query behavior, and code-path analysis to find the primary bottleneck,
then propose the smallest effective optimization and validation plan.
```

### Improve Database Performance
```
Review this query and surrounding access pattern for performance issues.
Suggest indexing, query rewrites, batching, or caching only where the data supports it.
```

### Optimize Frontend Responsiveness
```
Investigate why this page feels slow to render and interact with.
Look at bundle size, render churn, network waterfalls, and expensive component work.
```

### Plan a Load Test
```
Create a performance validation plan for a service expected to handle
5x current traffic, including metrics, bottleneck hypotheses, and rollback signals.
```

## Common Patterns

### Measurement-First Optimization Flow
```text
1. Reproduce the issue with representative conditions
2. Capture baseline metrics and traces
3. Find the dominant bottleneck
4. Apply the smallest meaningful optimization
5. Re-measure under the same conditions
6. Validate correctness and monitor for regressions
```

### Bottleneck Classification Pattern
```text
Check whether the slowdown is primarily caused by:
- CPU-bound computation
- memory pressure or GC behavior
- disk or network I/O
- database scans, joins, or lock contention
- frontend rendering or bundle overhead
- queueing, thread pool, or connection pool saturation
```

### Safe Optimization Pattern
```text
Prefer optimizations that:
- reduce repeated work
- improve data locality or batching
- remove unnecessary blocking
- narrow expensive queries or renders
- preserve clarity and correctness
```

## Best Practices

- Measure before and after every meaningful optimization
- Focus on the dominant bottleneck, not the most visible line of code
- Use representative traffic, data shapes, and environments when possible
- Prefer clear improvements over clever micro-optimizations
- Treat caching as one tool, not the default answer
- Validate both latency and resource cost when making tradeoffs
- Leave behind observability or regression protection for critical hot paths

## Troubleshooting

### Optimization Did Not Improve Real Performance
- Re-check whether the original bottleneck was identified correctly
- Confirm the benchmark or workload matches real usage
- Look for downstream bottlenecks exposed after the first fix

### Performance Is Fine Locally but Bad in Production
- Compare data size, concurrency, network distance, and infrastructure limits
- Check connection pools, autoscaling behavior, and noisy-neighbor effects
- Review production-only integrations, retries, and observability overhead

### Query or Endpoint Gets Slower Over Time
- Check dataset growth, stale indexes, fragmentation, and skewed data distribution
- Review cache hit rate, queue buildup, and lock contention trends
- Look for memory leaks, excessive retries, or compounding background work

### System Is Fast but Costs Too Much
- Evaluate unnecessary over-provisioning, over-caching, and hot-path inefficiency
- Balance throughput targets against memory, CPU, and storage costs
- Right-size infrastructure only after confirming utilization patterns

## Integration Points

- **Application layers**: backend services, APIs, batch jobs, frontend rendering
- **Data systems**: SQL, caches, message queues, search indexes, object stores
- **Runtime and infra**: containers, JVM/Node/Python/.NET runtimes, connection pools, load balancers
- **Observability**: metrics, traces, logs, profilers, synthetic and load tests
- **Related skills**: `sql` for database-heavy tuning, `react` for frontend-specific optimization, `plan` for phased performance work
