---
name: databricks
description: '**WORKFLOW SKILL** — Build, operate, and troubleshoot Databricks data engineering, analytics, and machine learning workflows. USE FOR: Spark jobs and notebooks, Delta Lake tables, Unity Catalog governance, Databricks SQL, workflows/jobs, cluster configuration, dbx or Databricks CLI deployment, and platform security/cost tuning. DO NOT USE FOR: non-Databricks data platforms, generic application coding unrelated to Databricks workloads, or cloud infrastructure outside Databricks context unless directly required for workspace integration. INVOKES: terminal for Databricks CLI and Spark-related commands, file system tools for notebooks and pipeline code, and workflow reasoning for data platform design and optimization.'
---

# Databricks Development Skill

## Overview

This skill provides structured support for Databricks-based data platforms, including notebook development, Spark and Delta Lake engineering, orchestration, governance, and production troubleshooting. It emphasizes scalable data pipelines, secure workspace practices, and reliable deployment patterns across development, staging, and production.

## Key Capabilities

### Data Engineering
- Build batch and streaming pipelines with Apache Spark
- Design Bronze, Silver, and Gold data layers with Delta Lake
- Implement ingestion, transformation, deduplication, and incremental processing
- Optimize partitioning, file sizing, and schema evolution strategies

### Databricks Platform Workflows
- Create and manage notebooks, repos, jobs, and workflows
- Configure job clusters and all-purpose clusters for the right workload type
- Package and deploy code with Databricks CLI, bundles, or CI/CD pipelines
- Integrate secrets, environment variables, and external storage access

### SQL and Analytics
- Author Databricks SQL queries, dashboards, and warehouse workloads
- Create managed and external tables, views, and materialized patterns
- Tune joins, aggregations, and caching for BI and reporting use cases
- Support medallion architecture and semantic-layer aligned datasets

### Governance and Security
- Configure Unity Catalog catalogs, schemas, tables, volumes, and permissions
- Apply least-privilege access with workspace and data-level controls
- Manage service principals, secret scopes, and credential passthrough patterns
- Support auditability, lineage, and environment isolation practices

### Machine Learning and Operations
- Support MLflow experiments, model tracking, and promotion flows
- Operationalize feature engineering and model scoring jobs
- Monitor job reliability, cluster cost, and runtime regressions
- Troubleshoot notebook failures, dependency issues, and runtime incompatibilities

## Usage Examples

### Create a Delta table with incremental load
```python
from pyspark.sql import functions as F

source_df = spark.read.format("json").load("/mnt/raw/orders")

clean_df = (
    source_df
    .withColumn("ingested_at", F.current_timestamp())
    .dropDuplicates(["order_id"])
)

(
    clean_df.write
    .format("delta")
    .mode("append")
    .saveAsTable("main.sales.orders_bronze")
)
```

### Optimize and compact a Delta table
```sql
OPTIMIZE main.sales.orders_silver
ZORDER BY (customer_id, order_date);
```

### Define a Databricks job task in YAML
```yaml
resources:
  jobs:
    orders_pipeline:
      name: orders-pipeline
      tasks:
        - task_key: bronze_to_silver
          notebook_task:
            notebook_path: /Workspace/Shared/pipelines/orders_silver
          new_cluster:
            spark_version: 14.3.x-scala2.12
            node_type_id: Standard_DS3_v2
            num_workers: 2
```

## Common Patterns

### Medallion pipeline flow
- **Bronze**: land raw source data with minimal transformation and ingestion metadata
- **Silver**: standardize types, deduplicate records, enforce quality checks, and model business-ready entities
- **Gold**: publish curated aggregates and dimensional outputs for analytics, BI, and downstream consumers

### Merge into Delta table
```sql
MERGE INTO main.sales.orders_silver AS target
USING staging_orders AS source
ON target.order_id = source.order_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```

### Structured streaming to Delta
```python
(
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .load("/mnt/raw/events")
    .writeStream
    .format("delta")
    .option("checkpointLocation", "/mnt/checkpoints/events_bronze")
    .trigger(availableNow=True)
    .toTable("main.events.events_bronze")
)
```

### Unity Catalog grants
```sql
GRANT USE CATALOG ON CATALOG main TO `data-engineers`;
GRANT USE SCHEMA, CREATE TABLE ON SCHEMA main.sales TO `data-engineers`;
GRANT SELECT ON TABLE main.sales.orders_gold TO `analysts`;
```

## Best Practices

### Engineering
- Prefer modular notebook or package design over monolithic notebooks
- Keep schemas explicit for production pipelines where stability matters
- Use idempotent writes and checkpointing for scheduled and streaming workloads
- Separate transformation logic from environment-specific configuration

### Performance
- Avoid small-file explosions by controlling write frequency and partition strategy
- Use `OPTIMIZE`, `VACUUM`, and statistics maintenance intentionally, not blindly
- Filter early, project only needed columns, and review shuffle-heavy operations
- Match cluster size and runtime type to workload shape instead of overprovisioning

### Governance
- Standardize on Unity Catalog for data access and lineage where available
- Isolate dev, test, and prod with separate catalogs, schemas, or workspaces
- Use service principals and secret management instead of embedded credentials
- Apply naming conventions and tags for ownership, environment, and cost visibility

### Operations
- Prefer jobs over manual notebook runs for repeatable production execution
- Store source in repos and move deployment config into version-controlled files
- Capture job parameters and outputs clearly for observability and reruns
- Monitor failed tasks, long-running stages, and cluster startup delays as separate signals

## Troubleshooting

### Pipeline and Job Failures
- **Task failed with notebook error**: inspect cell output, parameters, and upstream table assumptions
- **Job cluster startup issues**: verify node availability, policies, runtime version, and cloud quotas
- **Dependency/import failures**: check wheel or library installation scope and runtime compatibility

### Data Quality and Schema Issues
- **Schema mismatch on write**: compare incoming schema with Delta table metadata before enabling merge behavior
- **Duplicate rows after reruns**: review keys, watermarking, merge logic, and checkpoint reuse
- **Null or malformed fields**: quarantine bad records and add explicit type casting plus validation rules

### Performance Problems
- **Slow Spark stages**: inspect skew, shuffle volume, partition count, and expensive UDF usage
- **Delta table degradation**: look for too many small files, stale stats, or poor clustering columns
- **Warehouse latency**: review query plans, caching, concurrency, and table design for BI access

### Security and Access Problems
- **Permission denied in Unity Catalog**: verify grants at catalog, schema, and object levels
- **External location access errors**: check storage credentials, IAM roles, and network restrictions
- **Secret resolution failures**: confirm scope name, secret key, and principal permissions

## Integration Points

- **Languages**: Python, SQL, Scala
- **Core services**: Spark, Delta Lake, Databricks SQL, Jobs, Repos, Unity Catalog, MLflow
- **Deployment**: Databricks CLI, Databricks Asset Bundles, Terraform, CI/CD pipelines
- **Storage and cloud**: ADLS, S3, GCS, service principals, IAM roles, external locations
- **Adjacent tools**: Airflow, dbt, Kafka, Power BI, Tableau, Git providers
