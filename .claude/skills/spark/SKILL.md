---
name: spark
description: '**WORKFLOW SKILL** — Build, optimize, and modernize Apache Spark data workloads with strong emphasis on SQL-first migration from IBM i / AS400, CL, and RPG batch processing. USE FOR: Spark SQL development, PySpark or Scala Spark transformations, batch pipeline design, Delta or parquet table workflows, migration of DB2-style and record-oriented logic into distributed SQL patterns, performance tuning, restartable batch processing, and data reconciliation. DO NOT USE FOR: non-Spark distributed systems, unrelated application-layer coding, or cloud-platform setup that is not directly tied to Spark workloads. INVOKES: terminal for Spark tooling, file system tools for job and SQL assets, and workflow reasoning for data migration, batch modernization, and performance optimization.'
---

# Apache Spark Migration and SQL Skill

## Overview

This skill provides structured support for Apache Spark development with special focus on SQL-centric modernization from IBM i / AS400 environments. It helps translate CL orchestration, RPG record-level processing, and DB2-style batch workloads into Spark SQL, DataFrame, and restartable pipeline patterns that scale cleanly while preserving business rules, reconciliation, and operational safety.

## Key Capabilities

### Spark SQL Development
- Write and optimize Spark SQL for batch transformations, joins, aggregations, window functions, and merge-style processing
- Convert legacy DB2 for i query logic into portable Spark SQL patterns
- Build reusable SQL views, staging layers, and curated output tables
- Support SQL-first approaches before dropping into PySpark or Scala for edge cases

### IBM i / AS400 Migration
- Translate CL job flows into Spark batch stages, control tables, and scheduler-friendly execution steps
- Convert RPG row-by-row processing into set-based Spark transformations where behavior allows
- Map physical files, logical files, work files, and spool-oriented outputs into modern lakehouse or warehouse patterns
- Preserve business sequencing, restart behavior, and reconciliation expectations during migration

### Batch Processing and Restartability
- Design checkpoint, audit, error, and run-control tables for recurring batch execution
- Break nightly or high-volume jobs into deterministic Spark stages with rerun safety
- Support full rerun, partial rerun, and checkpoint restart strategies
- Model reject handling, balancing totals, and downstream handoff controls

### Performance and Scalability
- Tune partitioning, shuffle behavior, file sizing, joins, caching, and skew mitigation
- Decide when to use Spark SQL, DataFrame APIs, broadcast joins, or incremental strategies
- Reduce small-file problems and unnecessary wide transformations
- Compare correctness and performance against legacy batch windows and SLAs

### Data Quality and Reconciliation
- Add schema validation, null handling, conversion rules, and business-rule checks
- Build reconciliation outputs that compare legacy and Spark results
- Track row counts, control totals, rejected records, and exception categories
- Support phased migration with dual-run validation

## Usage Examples

### Convert RPG batch logic to Spark SQL
```
Convert this RPG and CL batch flow into Spark SQL stages with control tables, restart checkpoints, and reconciliation totals.
```

### Tune Spark SQL migration query
```
Optimize this Spark SQL job migrated from DB2 for i. It currently has large shuffles, skewed joins, and slow end-of-day processing.
```

### Design restartable Spark batch
```
Design a restartable Spark batch pattern for nightly invoice processing migrated from AS/400, including audit tables, reject handling, and rerun strategy.
```

### Translate DB2-style logic
```
Rewrite this DB2 for i SQL and record-level RPG logic into Spark SQL and explain which rules should stay in SQL versus PySpark.
```

## Common Patterns

### Batch run-control table
```sql
CREATE TABLE batch_run_control (
  run_id BIGINT,
  batch_name STRING,
  business_date DATE,
  status STRING,
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  last_checkpoint STRING,
  error_message STRING
)
USING delta;
```

### Spark SQL staging and aggregation
```sql
CREATE OR REPLACE TEMP VIEW invoice_stage AS
SELECT
  customer_id,
  invoice_id,
  invoice_date,
  amount,
  current_timestamp() AS processed_at
FROM raw_invoices
WHERE business_date = DATE '2026-04-11';

INSERT INTO invoice_summary
SELECT
  customer_id,
  SUM(amount) AS total_amount,
  COUNT(*) AS invoice_count
FROM invoice_stage
GROUP BY customer_id;
```

### Merge-style upsert
```sql
MERGE INTO customer_balance AS target
USING (
  SELECT customer_id, SUM(amount) AS total_amount
  FROM invoice_stage
  GROUP BY customer_id
) AS source
ON target.customer_id = source.customer_id
WHEN MATCHED THEN
  UPDATE SET target.open_amount = target.open_amount + source.total_amount
WHEN NOT MATCHED THEN
  INSERT (customer_id, open_amount)
  VALUES (source.customer_id, source.total_amount);
```

### Spark DataFrame fallback for edge rules
```python
from pyspark.sql import functions as F

result_df = (
    source_df
    .withColumn("normalized_status", F.when(F.col("status") == "A", F.lit("ACTIVE")).otherwise(F.lit("INACTIVE")))
    .groupBy("customer_id")
    .agg(F.sum("amount").alias("total_amount"))
)
```

## Best Practices

- Start with Spark SQL for migrated batch logic because it is easier to review, test, and compare with legacy SQL behavior
- Convert record-at-a-time RPG loops to set-based transformations only after validating ordering, side effects, and restart semantics
- Keep orchestration outside the transformation body by using control tables, scheduler metadata, and explicit batch states
- Use deterministic staging layers for each major conversion step
- Measure row counts and balancing totals after every critical stage during migration
- Partition by business-relevant keys and dates, not by habit
- Avoid overusing Python UDFs when built-in Spark SQL functions can do the work more efficiently
- Preserve legacy meaning first, then optimize once reconciliation is stable

## IBM i Migration Guidance

### From CL to Spark orchestration
- Replace CL command flow with scheduler-driven Spark stages and run-control metadata
- Convert message-driven or spool-based checkpoints into tables, logs, and structured status outputs
- Keep job dependencies explicit so batch order remains visible and testable

### From RPG to Spark transformations
- Translate `CHAIN`, `SETLL`, `READE`, and update loops into joins, windows, filters, and grouped aggregations
- Separate pure calculation rules from side-effecting job-control logic before migration
- Use Spark SQL for reusable business transformations and DataFrame APIs only where SQL becomes awkward or opaque

### From DB2 for i to Spark SQL
- Normalize DB2 for i data types, blank values, and packed-decimal conventions early
- Replace temporary physical files with staging tables that have clear lifecycle and ownership
- Rebuild UDF, procedure, and view logic in forms Spark can execute and monitor cleanly
- Validate ordering-sensitive logic carefully because distributed execution may expose hidden assumptions

### Batch migration focus
- Model batch scope, input cutoff, reject output, reconciliation totals, and rerun policy as first-class artifacts
- Budget time for dual-run validation against legacy outputs
- Keep control totals, counts, and exception summaries at every major stage
- Treat restartability and auditability as required design features, not cleanup work after implementation

## Troubleshooting

### Performance issues
- **Large shuffle stages**: review join strategy, partition count, skew, and wide dependencies
- **Too many small files**: reduce write frequency, tune partitions, and compact outputs intentionally
- **Broadcast join not triggered**: inspect table size assumptions and join hints
- **Slow SQL after migration**: compare execution plan against legacy intent and check for unnecessary repartitions

### Data correctness issues
- **Mismatched totals**: compare stage-by-stage row counts and balancing totals with legacy runs
- **Duplicate rows after rerun**: revisit merge keys, checkpoint logic, and idempotent write design
- **Packed decimal or blank-value problems**: add explicit conversion and normalization rules
- **Ordering-dependent behavior changed**: identify hidden procedural assumptions from RPG or CL flow

### Operational issues
- **Rerun failed midway**: inspect control-table status, checkpoint design, and partial-write handling
- **Job dependency gaps**: rebuild explicit upstream/downstream sequencing rather than relying on manual operator knowledge
- **Schema drift**: pin schemas where production behavior must remain stable and quarantine bad records when needed

## Integration Points

- **Languages**: Spark SQL, PySpark, Scala
- **Storage formats**: Delta Lake, parquet, ORC
- **Scheduling**: Airflow, Databricks Jobs, enterprise schedulers, cron-driven wrappers
- **Migration context**: AS400, IBM i, DB2 for i, CL, RPG, SQLRPGLE
- **Adjacent platforms**: Databricks, Hadoop-compatible Spark clusters, lakehouse and warehouse ecosystems
