---
name: data
description: '**WORKFLOW SKILL** — Analyze, transform, validate, move, and govern data across files, databases, pipelines, and reporting workflows. USE FOR: data analysis, cleansing, shaping, ETL/ELT design, dataset validation, schema mapping, reporting preparation, data quality remediation, and delivery of reliable data workflows. DO NOT USE FOR: purely SQL-centric work better handled by the `sql` skill, model training and MLOps better handled by the `ai` skill, or unrelated application logic without meaningful data workflow scope. INVOKES: file system tools for datasets and pipeline artifacts, terminal for data tooling and validation commands, semantic search for data patterns, governance guidance, and transformation strategies.'
---

# Data Engineering and Analytics Skill

## Overview

This skill provides structured support for working with data across analysis, transformation, quality, movement, and operational workflows. It helps turn raw or inconsistent data into reliable datasets, reporting outputs, and pipeline-ready structures while emphasizing traceability, validation, maintainability, and safe handling of data changes.

## Key Capabilities

### Data Analysis and Exploration
- Inspect datasets from CSV, JSON, Excel, APIs, logs, and database exports
- Profile distributions, null rates, duplicates, outliers, and schema drift
- Summarize trends, anomalies, and quality gaps in business-friendly terms
- Compare source and target datasets during migrations or reconciliations

### Data Transformation and Shaping
- Clean, normalize, filter, enrich, aggregate, and reshape data
- Convert between file formats and structures for downstream systems
- Map legacy fields to modern schemas and canonical models
- Support batch and incremental transformation patterns

### Data Quality and Validation
- Define validation rules for completeness, uniqueness, consistency, and timeliness
- Build checks for schema conformance, value ranges, referential integrity, and reconciliation
- Diagnose bad records, malformed files, and broken upstream assumptions
- Add auditability and error-handling patterns to data workflows

### Pipelines and Operational Workflows
- Design ETL/ELT flows for ingestion, staging, transformation, and delivery
- Support restartable and observable batch jobs and scheduled data processes
- Structure intermediate data zones such as raw, staged, curated, and published layers
- Plan checkpointing, retry handling, and failure recovery for data movement

### Governance and Delivery
- Improve naming, lineage, ownership, and documentation for datasets
- Handle sensitive data carefully with masking, minimization, and access boundaries
- Prepare clean outputs for dashboards, APIs, downstream applications, or ML features
- Support handoff artifacts such as mapping documents, validation summaries, and runbooks

## Usage Examples

### Clean and Standardize a Dataset
```
Take this customer export and standardize names, dates, status fields,
and duplicate records so it can be loaded safely into the target system.
```

### Build a Data Validation Workflow
```
Create checks for this nightly feed to catch missing columns, invalid codes,
row count anomalies, duplicate business keys, and stale delivery dates.
```

### Plan a Migration Mapping
```
Map this legacy file layout to a new reporting schema, including field transforms,
defaulting rules, reconciliation strategy, and exception handling.
```

### Prepare Data for Reporting
```
Transform these operational exports into a curated reporting dataset with
monthly aggregates, category cleanup, and clearly defined business metrics.
```

## Common Patterns

### Basic Data Workflow
```text
1. Inspect source structure and quality
2. Define target shape and business rules
3. Transform and normalize the data
4. Validate counts, keys, and critical fields
5. Capture exceptions and reconciliation output
6. Deliver the curated dataset or downstream artifact
```

### Layered Pipeline Pattern
```text
Raw: preserve source input with minimal change
Stage: clean and standardize structure
Curated: apply business rules and join logic
Published: deliver consumer-ready outputs
```

### Data Quality Checklist
```text
- required fields present
- types and formats are valid
- business keys are unique where expected
- reference values are in allowed domains
- counts reconcile across important boundaries
- exceptions are captured instead of silently dropped
```

## Best Practices

- Preserve raw inputs long enough to support traceability and replay
- Make transformation rules explicit rather than burying them in ad hoc scripts
- Validate data at boundaries, not only at the end of the pipeline
- Keep identifiers, dates, currencies, and status codes normalized consistently
- Separate business-rule transformations from technical cleanup when possible
- Document assumptions, mappings, and reconciliation logic
- Minimize exposure of sensitive data and apply masking where appropriate

## Troubleshooting

### Data Looks Inconsistent Across Sources
- Compare definitions, refresh timing, and filtering logic first
- Check whether keys, time zones, codes, or joins changed between systems
- Reconcile row counts and business totals at multiple checkpoints

### Pipeline Fails on Dirty Input
- Add schema and value validation earlier in the flow
- Route bad records to an exception path instead of blocking all processing
- Harden parsers and defaulting rules where business-approved

### Reports Do Not Match Operational Totals
- Verify aggregation grain and de-duplication rules
- Check late-arriving data, soft deletes, and status transitions
- Confirm business definitions are aligned between source and report layers

### Data Processing Is Too Slow
- Reduce repeated parsing and transformation work
- Batch operations where possible and avoid unnecessary row-by-row handling
- Push appropriate work closer to the database or distributed engine when justified

## Integration Points

- **Data sources**: files, relational databases, APIs, logs, object storage, message streams
- **Transformation tools**: Python, pandas, Spark, SQL, dbt, ETL schedulers
- **Storage targets**: warehouses, marts, operational stores, reporting extracts
- **Quality workflows**: validation rules, reconciliation reports, exception queues, runbooks
- **Related skills**: `sql` for deep relational query work, `ai` for ML-oriented pipelines, `plan` for phased data migrations or delivery efforts
