---
name: airflow
description: '**WORKFLOW SKILL** — Create, modify, debug, and optimize Apache Airflow DAGs, tasks, and workflows. USE FOR: generating DAGs from requirements; adding/modifying tasks and operators; setting up dependencies and scheduling; debugging DAG issues; optimizing performance; managing connections and variables; creating custom operators/hooks. DO NOT USE FOR: general Python coding; data processing outside Airflow context; infrastructure setup; runtime execution monitoring. INVOKES: file system tools for DAG creation/modification, terminal for testing/validation, semantic search for existing DAG patterns.'
---

# Airflow DAG Development

## Overview

This skill provides comprehensive support for Apache Airflow development, including DAG creation, task management, dependency configuration, and best practices implementation.

## Key Capabilities

### DAG Creation & Management
- Generate complete DAG structures from natural language requirements
- Create tasks with appropriate operators (PythonOperator, BashOperator, etc.)
- Set up proper dependencies and execution order
- Configure scheduling intervals and catchup policies

### Task Development
- Implement Python functions for data processing
- Create bash scripts for system operations
- Set up XCom communication between tasks
- Handle error scenarios and retries

### Best Practices Implementation
- Proper DAG structure and naming conventions
- Default arguments configuration
- Documentation and docstrings
- Logging and monitoring setup

### Debugging & Optimization
- Identify common DAG issues
- Optimize task performance
- Fix dependency problems
- Validate DAG syntax and logic

## Usage Examples

### Creating a Basic ETL DAG
```
Generate an Airflow DAG that:
- Extracts data from a CSV file
- Transforms the data (filtering and aggregation)
- Loads results to a database
- Runs daily at 6 AM
```

### Adding Error Handling
```
Modify this DAG to include:
- Retry logic for failed tasks
- Email notifications on failure
- Proper error logging
```

### Optimizing Performance
```
Review this DAG and suggest improvements for:
- Parallel task execution
- Resource utilization
- Execution time reduction
```

## Common Patterns

### ETL Pipeline Structure
```python
# Extract → Transform → Load pattern
extract_task >> transform_task >> load_task
```

### Branching Logic
```python
# Conditional execution based on data quality
check_quality >> [good_data_task, bad_data_task]
```

### Parallel Processing
```python
# Multiple independent tasks running concurrently
[extract_task1, extract_task2, extract_task3] >> transform_task
```

## Best Practices

- Use descriptive task IDs and DAG names
- Implement proper error handling and retries
- Document DAGs and tasks with docstrings
- Use XCom for data passing between tasks
- Configure appropriate resource limits
- Test DAGs locally before deployment
- Use connection IDs for external systems
- Implement logging for debugging

## Troubleshooting

### Common Issues
- **Import errors**: Check Airflow version compatibility
- **Dependency issues**: Ensure proper task ordering
- **Scheduling problems**: Verify cron expressions
- **Performance bottlenecks**: Review task parallelism

### Validation Steps
1. Check DAG syntax with `python -m py_compile`
2. Test imports and dependencies
3. Validate task connections
4. Review scheduling configuration
5. Test with sample data

## Integration Points

- **Databases**: PostgreSQL, MySQL, BigQuery
- **Cloud Services**: AWS, GCP, Azure
- **Data Processing**: Spark, Pandas, SQL
- **APIs**: REST, GraphQL, SOAP
- **File Systems**: Local, HDFS, S3, GCS