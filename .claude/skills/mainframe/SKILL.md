---
name: mainframe
description: '**WORKFLOW SKILL** — Analyze, document, test, and modernize IBM mainframe workloads. USE FOR: COBOL, JCL, PROC, copybooks, CICS, IMS, VSAM, DB2 z/OS, batch schedules, file dependencies, control cards, reports, mainframe-to-Java/Spring migration briefs, and characterization test planning. DO NOT USE FOR: IBM i / AS400-specific RPG or CL work unless mainframe concepts are explicitly involved, generic cloud migration without mainframe artifacts, or production changes without human approval. INVOKES: file system tools for source artifacts, terminal tools for read-only inventory, and conversion/test generation workflows.'
---

# Mainframe Modernization Skill

## Overview

This skill supports IBM mainframe understanding and modernization work. It treats existing mainframe behavior as the source of truth and emphasizes inventory, dependency mapping, characterization tests, and human review before code conversion.

## Key Capabilities

### Program Analysis
- Explain COBOL divisions, paragraphs, sections, copybooks, working storage, linkage, file I/O, and embedded SQL.
- Identify business rules, validations, calculations, abnormal paths, and report output.
- Map CALL chains, copybook dependencies, file descriptors, and database access.
- Separate online transaction behavior from batch processing behavior.

### JCL and Batch Flow
- Analyze JOB, EXEC, DD, PROC, INCLUDE, SORT, IDCAMS, IEBGENER, DFSORT, and utility steps.
- Identify datasets, GDGs, control cards, restart points, condition codes, and step dependencies.
- Produce batch flow diagrams and migration briefs for scheduler-friendly modernization.
- Preserve operational behavior such as ordering, restartability, audit records, and report generation.

### CICS, IMS, VSAM, and DB2
- Identify CICS transaction boundaries, COMMAREA/channel-container usage, maps, and pseudo-conversational flows.
- Analyze IMS program interactions when PCBs, segments, or message processing are present.
- Map VSAM KSDS/ESDS/RRDS access patterns and keyed file behavior.
- Document DB2 z/OS table access, cursors, commits, rollbacks, and SQLCODE handling.

### Modernization Planning
- Create inventory-first migration briefs before code generation.
- Recommend decomposition into Java/Kotlin/Spring services, batch jobs, repositories, DTOs, and APIs.
- Identify what should remain procedural, become SQL, move into services, or become orchestration.
- Produce characterization tests from known inputs, outputs, reports, files, SQL results, and return codes.

## Usage Examples

### COBOL Program Brief
```text
Analyze this COBOL program and produce:
- inputs, outputs, datasets, tables, and reports
- business rules and side effects
- copybooks and missing dependencies
- modernization risks
- characterization tests before Java conversion
```

### JCL Job Inventory
```text
Review this JCL job and summarize each step, DD statement, dataset dependency,
utility usage, condition code behavior, restart point, and migration candidate.
```

### CICS Transaction Mapping
```text
Map this CICS transaction into a web/API flow while preserving COMMAREA state,
screen validation, DB2 access, error handling, and transaction boundaries.
```

## Common Workflow

1. Inventory artifacts: COBOL, JCL, PROCs, copybooks, maps, control cards, DB2 SQL, VSAM definitions, and reports.
2. Identify runtime context: batch, CICS, IMS, scheduler, dataset naming, regions, and environment variables.
3. Map inputs, outputs, side effects, restart behavior, and operational controls.
4. Extract business rules and uncertainty separately.
5. Create characterization tests from real examples.
6. Draft the modernization plan and target architecture.
7. Generate candidate code only after behavior and assumptions are reviewed.

## Best Practices

- Treat mainframe artifacts as authoritative until tests prove otherwise.
- Do not flatten batch jobs into services without preserving restartability and audit behavior.
- Keep copybook field names, offsets, signs, scales, and redefines visible in migration notes.
- Flag missing control cards, scheduler parameters, copybooks, maps, or dataset samples.
- Preserve SQLCODE, file status, return code, and abend handling semantics.
- Gate production writes, destructive dataset actions, and DB2 changes behind explicit human approval.

## Troubleshooting

### Missing Context
- Ask for copybooks, JCL, control cards, dataset samples, DB2 DDL, mapsets, or scheduler definitions.
- Mark assumptions clearly instead of silently inventing runtime behavior.

### Ambiguous Data Access
- Distinguish VSAM keyed access, sequential files, temporary work datasets, and DB2 cursor patterns.
- Check whether commits are program-controlled, job-step controlled, or transaction-managed.

### Modernization Risk
- Look for hidden side effects in reports, audit files, return codes, restart datasets, and exception paths.
- Identify batch windows, volume assumptions, sort order requirements, and parallelization constraints.

## Integration Points

- **COBOL**: source programs, copybooks, embedded SQL, reports.
- **JCL**: jobs, PROCs, DDs, utilities, scheduler parameters.
- **CICS / IMS**: transactions, screens, COMMAREA, PCBs, message flows.
- **VSAM / DB2 z/OS**: file access, SQL, commits, error codes.
- **Modern Targets**: Java, Kotlin, Spring Boot, Spring Batch, SQL procedures, APIs, and ETL pipelines.
