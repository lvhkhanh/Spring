---
name: sql
description: '**WORKFLOW SKILL** — Create, refactor, optimize, and troubleshoot SQL queries and database schema design. USE FOR: writing and tuning queries for PostgreSQL, MySQL, SQL Server, Oracle, and SQLite; modeling tables and relations; implementing ETL transformations and migrations; writing stored procedures and views. DO NOT USE FOR: application-level business logic or non-SQL data stores. INVOKES: file system tools for query and migration scripts, terminal for DB CLI commands, database schema analysis, and query optimization reasoning.'
---

# SQL Development Skill

## Overview

This skill provides comprehensive support for SQL and relational database workloads. It helps generate and refactor queries, design normalized schemas, tune performance, and resolve integrity and indexing issues across DBMS platforms.

## Key Capabilities

### Query Authoring
- Create SELECT, INSERT, UPDATE, DELETE statements with JOINs, aggregation, window functions, subqueries, CTEs
- Build parameterized queries for safety and maintainability
- Implement complex business logic in SQL for reporting and transformations

### Schema & Data Modeling
- Design normalized schema (1NF, 2NF, 3NF) and identify denormalization patterns when needed
- Define primary/foreign keys, unique constraints, and check constraints
- Create indexes, materialized views, partitions, and data retention strategies

### Performance & Tuning
- Analyze execution plans and suggest index changes
- Rewrite queries for set-based processing and reduced row scans
- Optimize joins, filter predicates, and subquery usage

### ETL & Data Pipelines
- Generate conversion scripts (CSV/JSON -> relational tables)
- Implement staging tables, upserts (MERGE/ON CONFLICT), and incremental load logic
- Create stored procedures, functions, and triggers for transformation rules

### Migrations & Versioning
- Create idempotent migration scripts (DDL, DML) for schema changes
- Cope with safe rolling updates and data backfills
- Document and test migration impact

## Usage Examples

### Basic reporting query
```
Write a query to get total sales per month for the current year, including product category and region.
```

### Join with window function
```
Create a query returning each employee with their salary rank inside department, along with running department salary total.
```

### Optimize slow query
```
This query performs a full table scan on orders and joins customers with no index on customer_id; refactor and add optimal indexes for PostgreSQL.
```

### Migrate schema
```
Generate a migration that adds `last_login` TIMESTAMP NULL to `users`, populates existing rows with current timestamp and updates constraints safely.
```

## Common Patterns

### CTE and aggregation
```sql
WITH monthly AS (
  SELECT date_trunc('month', order_date) as month,
         sum(amount) as total_amount
  FROM orders
  WHERE order_date >= date_trunc('year', current_date)
  GROUP BY 1
)
SELECT month, total_amount
FROM monthly
ORDER BY month;
```

### Upsert (PostgreSQL)
```sql
INSERT INTO users (id, name, email)
VALUES (:id, :name, :email)
ON CONFLICT (id)
DO UPDATE SET name = EXCLUDED.name,
              email = EXCLUDED.email;
```

### Window function pattern
```sql
SELECT id,
       department,
       salary,
       rank() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
FROM employees;
```

### Soft delete pattern
```sql
UPDATE items
SET deleted_at = now()
WHERE id = :item_id;
```

## Best Practices

- Use explicit column names instead of SELECT *
- Prefer joins with clear predicate conditions and avoid Cartesian products
- Keep transactions short and handle deadlock retries
- Use database constraints for data integrity
- Avoid scalar subqueries in SELECT for large result sets; use JOIN or CTE
- Document indexing strategy and date/hot key access patterns

## Troubleshooting

### Syntax / semantics
- `ERROR: column does not exist`: verify aliases and schema names
- `ambiguous column name`: qualify with table alias
- `conversion failed`: cast values explicitly

### Performance
- `Hash Join` / `Nested Loop` / `Merge Join` analysis: pick index or materials accordingly
- Missing index on filtered columns causes sequential scans
- Use `EXPLAIN ANALYZE` to compare query variants

### Concurrency
- `serialization failure`, `deadlock detected`: apply retry, lock ordering, and lower isolation if safe
- Long-running transactions block DML; detect with monitoring views

## Integration Points

- ORMs: SQLAlchemy, Hibernate, Django ORM, jOOQ
- Data warehousing: Snowflake, BigQuery, Redshift
- ETL: Airflow, dbt, Talend, Pentaho
- Scripting: psql, mysql, sqlcmd, sqlplus
- Cloud RDBMS: Amazon RDS, Azure SQL Database, Google Cloud SQL
