---
name: db2
description: '**WORKFLOW SKILL** — Design, query, optimize, and operate IBM Db2 databases across application and enterprise workloads. USE FOR: Db2 SQL development, schema design, performance tuning, indexing strategy, backup/recovery planning, and troubleshooting locks/deadlocks. DO NOT USE FOR: non-relational data stores, non-Db2-specific platform operations, or application-only logic unrelated to database behavior. INVOKES: file system tools for SQL/migration scripts, terminal for Db2 CLI and admin commands, semantic search for Db2 optimization patterns.'
---

# IBM Db2 Development and Operations Skill

## Overview

This skill provides structured support for IBM Db2 workflows, including query authoring, schema modeling, performance tuning, operational maintenance, and incident troubleshooting. It emphasizes correctness, scalability, and operational safety across development and production environments.

## Key Capabilities

### SQL Authoring and Refactoring
- Write Db2-compatible SELECT/INSERT/UPDATE/DELETE/MERGE statements
- Build CTEs, window functions, and aggregate queries for analytics use cases
- Refactor legacy SQL for readability and performance
- Create parameterized SQL patterns for safer application integration

### Schema and Data Modeling
- Design normalized schemas with keys, constraints, and referential integrity
- Define indexes, partitioning, and tablespace-aware storage strategies
- Plan datatype choices for precision, performance, and compatibility
- Create migration scripts for additive and backward-safe changes

### Performance and Optimization
- Analyze access plans and recommend index/query improvements
- Reduce scans and sort overhead with predicate and join tuning
- Optimize batch DML and transaction sizing
- Balance read/write workloads with index and locking tradeoffs

### Operations and Reliability
- Define backup, restore, and recovery workflows
- Manage runstats/reorg cycles and statistics quality
- Monitor connection pools, lock waits, and resource utilization
- Support deployment runbooks and rollback planning

### Troubleshooting and Incident Handling
- Diagnose deadlocks, lock contention, and long-running transactions
- Investigate syntax/compatibility issues in Db2 SQL dialect usage
- Resolve performance regressions after schema or data volume changes
- Build regression queries and checks for post-fix validation

## Usage Examples

### Query with CTE and aggregation
```sql
WITH monthly_sales AS (
  SELECT
    DATE(TRUNC(order_date, 'MM')) AS sales_month,
    SUM(total_amount) AS revenue
  FROM orders
  WHERE order_date >= CURRENT DATE - 12 MONTHS
  GROUP BY DATE(TRUNC(order_date, 'MM'))
)
SELECT sales_month, revenue
FROM monthly_sales
ORDER BY sales_month;
```

### Upsert with MERGE
```sql
MERGE INTO customers AS t
USING (VALUES (?, ?, ?)) AS s(customer_id, name, email)
ON t.customer_id = s.customer_id
WHEN MATCHED THEN
  UPDATE SET name = s.name, email = s.email
WHEN NOT MATCHED THEN
  INSERT (customer_id, name, email)
  VALUES (s.customer_id, s.name, s.email);
```

### Basic index creation
```sql
CREATE INDEX idx_orders_customer_date
  ON orders (customer_id, order_date DESC);
```

### Db2 CLI execution example
```bash
db2 connect to SAMPLE user dbuser using '******'
db2 -tvf migrations/2026_04_add_last_login.sql
db2 "RUNSTATS ON TABLE app.users WITH DISTRIBUTION AND DETAILED INDEXES ALL"
```

## Common Patterns

### Safe migration pattern
```text
1. Add nullable column or new table/index
2. Backfill data in controlled batches
3. Deploy application changes using new schema
4. Enforce NOT NULL/constraints after data validation
```

### Lock-aware transaction pattern
```text
- Keep transactions short
- Access objects in consistent order
- Commit in batches for bulk operations
- Retry transient deadlock/timeout failures
```

### Query tuning checklist
```text
- Validate predicate selectivity
- Check join order and join keys
- Review access plan for table scans/sorts
- Confirm relevant indexes and fresh statistics
```

## Best Practices

- Use explicit column lists instead of `SELECT *`
- Keep statistics current with scheduled `RUNSTATS`
- Apply `REORG` strategy for high-churn tables and indexes
- Use bind variables/parameter markers for reusable statements
- Add covering indexes only when read gain justifies write overhead
- Separate DDL migrations from high-risk data backfills
- Validate rollback paths before production schema changes

## Troubleshooting

### Lock wait and deadlock issues
- Inspect lock/transaction views and deadlock logs
- Identify conflicting SQL and reduce transaction scope
- Add targeted indexes to reduce lock duration on scanned rows

### Slow queries after data growth
- Re-run `RUNSTATS` and compare access plans
- Check cardinality shifts and skewed predicates
- Revisit partitioning or archival strategy for hot tables

### Migration failures
- Validate schema dependency ordering and object ownership
- Check privileges, tablespace limits, and transaction log usage
- Re-run in staging with production-like volume before retrying

### Connectivity/authentication problems
- Validate database alias, credentials, and instance availability
- Check SSL/TLS configuration and client catalog entries
- Confirm firewall/network path for Db2 service ports

## Integration Points

- **Db2 tooling**: Db2 CLP, Data Studio, IBM Data Management Console
- **Application layers**: JDBC, ODBC, .NET providers, ORM integrations
- **Automation**: Bash/PowerShell scripts, CI/CD migration pipelines
- **Monitoring**: Prometheus exporters, APM tools, centralized logging
- **Platform contexts**: Linux/UNIX/Windows Db2 deployments and IBM i/Db2 for i interoperability
