---
name: sql
description: '**WORKFLOW SKILL** — Create, refactor, optimize, secure, and troubleshoot SQL workloads, especially for IBM i / AS400 modernization, Java/Spring/MyBatis migration, and batch-processing conversion. USE FOR: writing and tuning queries for PostgreSQL, MySQL, SQL Server, Oracle, SQLite, and DB2-style relational migrations; modeling tables and relations; converting IBM i record-oriented logic to set-based SQL; improving performance, security, maintainability, functions, procedures, views, and ETL workflows; adapting CL/RPG batch jobs to modern database patterns; and aligning data access boundaries for Java, Spring Boot, and MyBatis applications. DO NOT USE FOR: application-level business logic outside SQL-centric scope or non-SQL data stores. INVOKES: file system tools for query and migration scripts, terminal for DB CLI commands, database schema analysis, migration reasoning, and query optimization workflows.'
---

# SQL Development Skill

## Overview

This skill provides comprehensive support for SQL and relational database workloads, with special emphasis on migrating legacy IBM i / AS400 systems to modern relational platforms and Java application stacks. It helps generate and refactor queries, design normalized schemas, tune performance, harden security, improve maintainability, and translate CL, RPG, SQLRPGLE, and batch-oriented processing patterns into durable SQL procedures, functions, views, MyBatis mappings, and Spring-friendly data workflows.

## Key Capabilities

### Query Authoring
- Create SELECT, INSERT, UPDATE, DELETE statements with JOINs, aggregation, window functions, subqueries, CTEs
- Build parameterized queries for safety and maintainability
- Implement complex business logic in SQL for reporting and transformations
- Translate record-at-a-time IBM i access patterns into set-based SQL where safe and beneficial

### Schema & Data Modeling
- Design normalized schema (1NF, 2NF, 3NF) and identify denormalization patterns when needed
- Define primary/foreign keys, unique constraints, and check constraints
- Create indexes, materialized views, partitions, and data retention strategies
- Map DDS or DB2 for i physical/logical file structures into portable relational models

### Performance & Tuning
- Analyze execution plans and suggest index changes
- Rewrite queries for set-based processing and reduced row scans
- Optimize joins, filter predicates, and subquery usage
- Adapt batch-heavy workloads to chunking, staging, restartability, and controlled transaction scopes

### Security & Governance
- Replace library-list-driven or implicit access with explicit schemas, roles, grants, and execution boundaries
- Convert embedded dynamic SQL toward parameterized and audited patterns
- Design least-privilege access for tables, views, procedures, and batch service accounts

### IBM i Migration Patterns
- Convert CL/RPG batch orchestration into stored procedures, scheduler jobs, and SQL-driven control tables
- Refactor native file I/O loops, keyed access, and temporary work files into tables, MERGE logic, and staged transformations
- Preserve business rules while separating platform-specific operational behavior from portable SQL logic

### Java / Spring / MyBatis Alignment
- Split migrated logic cleanly across SQL, MyBatis mappers, Spring services, and batch orchestration layers
- Define which legacy RPG rules stay in SQL procedures versus move into Java service logic
- Build mapper-friendly query shapes, DTO projections, and result contracts for maintainable application code
- Support Spring Batch or scheduler-driven execution for migrated nightly and high-volume jobs

### User-Defined Functions
- Design scalar and table-valued user-defined functions for reusable calculation, normalization, and lookup logic
- Evaluate when a UDF improves reuse versus when inline SQL, views, or procedures are safer for performance and observability
- Refactor repeated RPG subroutine calculations into deterministic SQL functions when side effects are not required
- Expose UDF-backed logic safely to MyBatis and Spring code without hiding expensive data-access behavior

### ETL & Data Pipelines
- Generate conversion scripts (CSV/JSON -> relational tables)
- Implement staging tables, upserts (MERGE/ON CONFLICT), and incremental load logic
- Create stored procedures, functions, and triggers for transformation rules
- Design checkpoint, audit, error, and restart tables for nightly or high-volume batch cycles

### Migrations & Versioning
- Create idempotent migration scripts (DDL, DML) for schema changes
- Cope with safe rolling updates and data backfills
- Document and test migration impact
- Identify where IBM i business logic should become SQL procedures, application services, or scheduler-controlled batch units

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

### Modernize IBM i batch logic
```
Convert this AS/400 nightly CL + RPG batch flow into SQL tables, procedures, and scheduler-friendly restartable steps while preserving commit behavior and audit logging.
```

### Replace record-level processing
```
This RPG program reads invoices one row at a time with CHAIN/READE and updates totals. Refactor it into set-based SQL with staging tables, error capture, and performance-safe indexes.
```

### Convert RPG/DB2 flow to Spring + MyBatis
```
Take this RPG + DB2 business flow and split it into SQL views/procedures, MyBatis mapper XML, Spring service methods, and a restartable batch job design.
```

### Estimate migration complexity and delivery timing
```
Analyze this RPG/CL/DB2 source and estimate complexity, risks, and timeline for source analysis, unit test case creation, implementation, testing, review, and review-fix cycles.
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

### Restartable batch control pattern
```sql
CREATE TABLE batch_run_control (
  run_id            bigint generated always as identity primary key,
  batch_name        varchar(100) not null,
  business_date     date not null,
  status            varchar(20) not null,
  started_at        timestamp not null,
  completed_at      timestamp,
  last_checkpoint   varchar(100),
  error_message     varchar(2000)
);
```

### Procedure for chunked batch updates
```sql
CREATE PROCEDURE process_open_orders(IN p_business_date date)
LANGUAGE SQL
BEGIN
  INSERT INTO order_stage (order_id, customer_id, amount, business_date)
  SELECT order_id, customer_id, amount, p_business_date
  FROM orders
  WHERE status = 'OPEN'
    AND business_date = p_business_date;

  MERGE INTO customer_balance t
  USING (
    SELECT customer_id, sum(amount) AS total_amount
    FROM order_stage
    WHERE business_date = p_business_date
    GROUP BY customer_id
  ) s
  ON t.customer_id = s.customer_id
  WHEN MATCHED THEN
    UPDATE SET open_amount = t.open_amount + s.total_amount
  WHEN NOT MATCHED THEN
    INSERT (customer_id, open_amount)
    VALUES (s.customer_id, s.total_amount);
END;
```

### Security via view and execute boundary
```sql
CREATE VIEW reporting_active_customers AS
SELECT customer_id, customer_name, status
FROM customers
WHERE status = 'A';

GRANT SELECT ON reporting_active_customers TO reporting_role;
GRANT EXECUTE ON PROCEDURE process_open_orders TO batch_role;
```

### Scalar user-defined function
```sql
CREATE FUNCTION calculate_discount_rate (
  p_customer_tier varchar(10),
  p_order_amount  decimal(15,2)
)
RETURNS decimal(5,4)
BEGIN
  RETURN CASE
    WHEN p_customer_tier = 'GOLD' AND p_order_amount >= 1000 THEN 0.1500
    WHEN p_customer_tier = 'SILVER' AND p_order_amount >= 500 THEN 0.0800
    ELSE 0.0000
  END;
END;
```

### MyBatis mapper for migrated SQL
```xml
<mapper namespace="com.example.batch.OrderBatchMapper">

  <select id="findOpenOrderTotals" resultType="com.example.batch.OpenOrderTotal">
    SELECT customer_id,
           SUM(amount) AS total_amount
    FROM orders
    WHERE status = 'OPEN'
      AND business_date = #{businessDate}
    GROUP BY customer_id
  </select>

  <update id="markBatchCompleted">
    UPDATE batch_run_control
    SET status = 'COMPLETED',
        completed_at = CURRENT_TIMESTAMP
    WHERE run_id = #{runId}
  </update>

</mapper>
```

### Spring service boundary for batch step
```java
@Service
public class OrderBatchService {

    private final OrderBatchMapper orderBatchMapper;

    public OrderBatchService(OrderBatchMapper orderBatchMapper) {
        this.orderBatchMapper = orderBatchMapper;
    }

    @Transactional
    public void completeRun(long runId) {
        orderBatchMapper.markBatchCompleted(runId);
    }
}
```

## Best Practices

- Use explicit column names instead of SELECT *
- Prefer joins with clear predicate conditions and avoid Cartesian products
- Keep transactions short and handle deadlock retries
- Use database constraints for data integrity
- Avoid scalar subqueries in SELECT for large result sets; use JOIN or CTE
- Document indexing strategy and date/hot key access patterns
- During IBM i migration, separate business rules from job-control behavior before converting code
- Replace implicit library-list assumptions with fully qualified schema/object references
- Prefer stored procedures for batch step orchestration and functions for deterministic reusable calculations
- Design restartability explicitly with control tables, status columns, checkpoints, and idempotent writes
- Preserve audit columns, source identifiers, and reconciliation outputs for batch validation
- Convert row-by-row loops only after confirming ordering, locking, and side-effect requirements
- Use views or APIs to shield consumers from transitional schema differences during phased migration
- Keep SQL focused on data-intensive work and move orchestration, validation branching, and external integrations into Spring services
- Use MyBatis when migrated SQL must stay explicit and close to the database, especially for complex joins, procedures, and batch DML
- Design mapper methods and DTOs around stable business contracts rather than one-to-one legacy record formats
- Use user-defined functions only for deterministic reusable logic; avoid burying heavy queries or side effects inside them
- Estimate migration step-by-step instead of giving one bulk number for the whole legacy module

## IBM i Migration Guidance

### Performance adaptation
- Review keyed file access patterns (`CHAIN`, `SETLL`, `READE`) and map them to proper indexes, joins, and window logic
- Replace temporary physical files with staging tables only when lifecycle, cleanup, and concurrency are defined
- Avoid giant end-of-day commits; batch by business key ranges or checkpoints where the target platform benefits from smaller units
- Measure before and after with execution plans, row counts, and elapsed-time baselines from representative batch windows

### Security adaptation
- Inventory adopted authority, library-list resolution, and object-level permissions before redesign
- Move shared batch credentials toward dedicated service accounts with least privilege
- Restrict direct table access when business rules belong behind views or procedures
- Log who ran batch, what parameters were used, and which rows were affected when compliance matters

### Maintainability adaptation
- Standardize naming for schemas, procedures, work tables, error tables, and scheduler jobs
- Break monolithic CL or RPG flows into discrete SQL batch steps with clear inputs and outputs
- Keep portable SQL logic out of platform-specific shell, scheduler, or deployment scripts
- Document assumptions around collation, packed decimal conversion, blank values, and date formats from IBM i sources
- Align package and module boundaries so SQL artifacts map predictably to Java domain, mapper, service, and batch packages

### Functions and procedures
- Use scalar functions for reusable derivations with low side effects and predictable inputs
- Use procedures for multi-step batch work, audit logging, error capture, and transaction management
- Avoid hiding heavy DML inside functions where the target platform expects functions to stay mostly query-safe
- Translate subroutine-heavy RPG logic into smaller procedures instead of one oversized migration procedure

### SQL user-defined functions
- Use scalar UDFs for calculations such as status normalization, pricing rules, date derivation, and code translation
- Use table-valued UDFs carefully for reusable row sets when the target platform can optimize them acceptably
- Keep UDFs deterministic, small, well-named, and independently testable
- Do not move orchestration, transaction control, or batch-step state management into UDFs
- Validate whether a repeated RPG subroutine should become a UDF, a procedure, a view, or a Java service helper based on side effects and call frequency

### Java / Spring / MyBatis conversion
- Move screen flow, command orchestration, message handling, and external calls from RPG/CL into Spring services or batch components
- Keep set-based retrieval, aggregation, and bulk updates in SQL, surfaced through MyBatis mappers with explicit XML for complex cases
- Use MyBatis result maps, DTOs, and type handlers to handle packed decimal, date, status-code, and legacy flag conversions cleanly
- Treat stored procedures as batch-step or transaction boundaries when the database can execute them more efficiently than Java loops
- Prefer Spring-managed transactions around mapper calls, while avoiding duplicated commit logic between Java and stored procedures

### Batch processing focus
- Model batch runs, work queues, rejects, and reconciliation totals as first-class tables
- Plan for rerun behavior: full rerun, restart from checkpoint, or compensating correction
- Preserve sequencing requirements when IBM i jobs depended on job queues, message queues, or spool outputs
- Validate migrated batch using parallel-run totals, exception counts, and file-to-table reconciliation

## Complexity and Timing Estimation

### What to analyze first
- Count programs, service programs, copy members, CL scripts, SQL objects, and database files involved in the flow
- Identify external dependencies such as job schedules, spool outputs, data areas, message queues, APIs, and downstream tables
- Classify logic by type: pure calculation, record transformation, orchestration, data access, reporting, or external integration
- Highlight hidden complexity such as dynamic SQL, adopted authority, multi-member files, packed decimals, and restart logic

### Complexity drivers
- **Low complexity**: mostly CRUD SQL, limited branching, few files, minimal batch restart logic, low cross-program coupling
- **Medium complexity**: several joined files, reusable business rules, moderate batch sequencing, some data conversion, and mapper/service split decisions
- **High complexity**: heavy CL orchestration, many RPG call chains, complex state transitions, dense subroutines, external integrations, or strict overnight batch windows

### Estimation workflow
1. Analyze old source and dependencies, then produce an object inventory and rule map.
2. Derive candidate unit test cases from business rules, edge cases, conversions, and batch checkpoints.
3. Design target SQL, Java/Spring/MyBatis boundaries, migration approach, and rollback or rerun behavior.
4. Implement SQL objects, mappers, services, and batch orchestration.
5. Execute unit, integration, data-reconciliation, and batch rerun tests.
6. Review each artifact for correctness, security, performance, and maintainability.
7. Fix review findings, rerun impacted tests, and re-review until the scope is stable.

### Timing by delivery step
- **Analyze old source**: estimate by number of source members, coupling level, and undocumented job behavior
- **Create unit test cases**: estimate by number of business rules, conversions, negative cases, and batch restart points
- **Implement**: estimate separately for SQL objects, MyBatis mappers, Spring services, and batch configuration
- **Test**: include unit tests, integration tests, batch-window simulation, reconciliation, and defect retesting
- **Review**: account for SQL review, Java review, migration architecture review, and security/performance review
- **Fix review findings**: budget explicit time for rework because legacy migrations almost always surface missed edge cases

### Practical sizing approach
- Small flow: 1 to 3 programs or jobs, limited tables, low branching, and few interfaces
- Medium flow: 4 to 10 source members, shared business rules, moderate batch controls, and multiple mapper/service boundaries
- Large flow: 10+ interacting members, complex CL scheduling, many files, strict timing windows, and extensive reconciliation needs
- Add contingency when documentation is weak, test data is incomplete, or production behavior depends on operations knowledge not present in source

### Review and fix expectations at each step
- Analysis review: validate source inventory, assumptions, missing dependencies, and target-scope boundaries
- Test-case review: verify business coverage, negative cases, conversion rules, and batch restart scenarios
- Implementation review: inspect SQL plans, mapper clarity, transaction ownership, naming, and maintainability
- Test review: validate coverage gaps, flaky data setup, reconciliation mismatches, and performance realism
- Fix review: confirm that each defect fix includes regression validation and does not break earlier migrated behavior

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

### IBM i migration issues
- Record-level logic behaves differently after set-based conversion: verify ordering, duplicate handling, and restart behavior
- Packed decimal, zoned decimal, blank dates, or sentinel values may require explicit conversion rules
- CL-controlled batch dependencies can disappear during migration unless scheduler sequence and status tables are rebuilt
- Security regressions often come from granting broad table access instead of recreating controlled execution paths
- Overloading MyBatis mappers with business branching can recreate RPG monoliths in Java; keep orchestration in Spring services
- Transaction boundaries may become inconsistent if both Spring and stored procedures attempt to own commit behavior
- Result mapping bugs often appear when DB2-style naming, nullability, or decimal formats are not normalized for Java DTOs
- Complexity estimates are often wrong when hidden copybook rules, operator procedures, or undocumented rerun steps are discovered late
- Unit test creation is usually underestimated when legacy behavior depends on packed-decimal rounding, status-code conventions, or spool-based outputs

## Integration Points

- ORMs: SQLAlchemy, Hibernate, Django ORM, jOOQ
- Data warehousing: Snowflake, BigQuery, Redshift
- ETL: Airflow, dbt, Talend, Pentaho
- Scripting: psql, mysql, sqlcmd, sqlplus
- Cloud RDBMS: Amazon RDS, Azure SQL Database, Google Cloud SQL
- IBM i modernization: AS400, DB2 for i, SQLRPGLE, CL batch jobs, service programs, job schedulers
- Java modernization: Java, Spring Boot, Spring Batch, MyBatis, JDBC transaction management, mapper XML
