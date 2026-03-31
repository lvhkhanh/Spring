---
name: rpg
description: '**WORKFLOW SKILL** — Create, refactor, debug, and optimize IBM i (AS/400 iSeries) RPG programs (RPGLE and RPG/400). USE FOR: RPG program development, data structure design, database access, error handling, performance tuning, and integration with CL/SQL and external systems. DO NOT USE FOR: non-IBM i languages or unrelated application platforms. INVOKES: file system tools for RPG source editing, terminal/ssh examples for IBM i commands, and knowledge of RPG compiler/runtime best practices.'
---

# IBM i RPG Skill

## Overview

This skill provides guidance for developing and maintaining RPG applications on IBM i (AS/400, iSeries). It covers modern RPGLE with free-format code, legacy fixed-format RPG/400, database access via embedded SQL and native file I/O, modularization with procedures/Service Programs, and integration points with CL, DB2, and external services.

## Key Capabilities

### RPG Program Structure
- Define programs with `ctl-opt`, `dcl-pr`, `dcl-pi`, procedures, and modules
- Use free-format `dcl-s`, `dcl-ds`, `dcl-f`, `dcl-pr` for readability and maintainability
- Support multiple compile options (`DBGVIEW`, `OPTION(*NODEBUGIO)`, `ACTGRP`) and performance tuning

### Data Access
- Native file access with `dcl-f`, `read`, `chain`, `setll`, and `write`
- Embedded SQL with `exec sql` for select/insert/update/delete and cursors
- Index, commitment control, and record-level locking management

### Error Handling
- Use `%error`, `%found`, `%eof`, `%on-error`, and `MONITOR/ON-ERROR` blocks
- Return messages (`sendpgmmsg`) and status to callers via `*entry` and program statuses
- Trace and diagnostic logs using `debug` and `snmp` / job logs

### Integration
- Call CL programs (`CALL`), run SQL statements (`RUNSQLSTM`) and invoke web services via HTTP APIs
- Exchange data with file transfer (FTP/SFTP), message queues (`QMQRY`, `QMHSNDPM`), and MQ
t
- Use Service Programs / binder language for reusable libraries

## Usage Examples

### Minimal RPGLE Free-Format Program
```
ctl-opt dftactgrp(*no) actgrp(*new) option(*srcstmt: *nodebugio);

dcl-f myfile usage(*input) keyed;

dcl-s recKey char(10);

dcl-ds myData qualified;
  field1 char(20);
  field2 packed(7:2);
end-ds;

exec sql set option commit = *none;

read myfile key %key(myData); // example native file access
if %found(myfile);
  // process record
else;
  // no record
endif;

*inlr = *on;
return;
```

### Embedded SQL Example
```
ctl-opt dftactgrp(*no) actgrp(*new);

dcl-s custno char(10) inz('1000');

dcl-s custName char(50);

exec sql
  select name into :custName
  from customer
  where custno = :custno;

if sqlcode = 0;
  dsply ('Customer:' + %trim(custName));
else;
  dsply ('Customer not found, SQLCODE=' + %char(sqlcode));
endif;

*inlr = *on;
return;
```

### Subprocedure and Service Program
```
ctl-opt dftactgrp(*no) actgrp(*new) option(*srcstmt);

dcl-proc calcTax export;
  dcl-pi *n float(8:0);
    amount float(8:2) value;
    taxRate float(5:2) value;
  end-pi;

  return amount * taxRate;
end-proc;

// main

dcl-s net decimal(15:2);
net = calcTax(100.00: 0.08);
*inlr = *on;
return;
```

## Common Patterns

### Modularization
- Keep programs small and focused, use procedures and service programs for shared logic
- Use `dcl-pr` and `dcl-pi` to define clear interfaces and avoid global variables

### DB2 and Error Control
- Wrap SQL in `exec sql` and check `sqlcode` and `sqlstate`
- Use `MONITOR; ... ON-ERROR; ... ENDMON` for structured error catch

### Conversion and Legacy Support
- Convert fixed-format code to free-format gradually using `/%FREE`.
- Use `RPGLE` for new development and maintain legacy RPG/400 only when unavoidable.

## Best Practices

- Use `option(*srcstmt)` on development builds; use `*nodebugio` in production where appropriate
- Use commitment control and logging strategies for DB changes
- Validate data early with strong data structure typing (`dcl-ds`, `dcl-s`, subfields)
- Scoping rule: prefer local variables and avoid `*PSSR` and global file pointers where possible
- Name service programs and procedures consistently for findability and maintenance

## Troubleshooting

### Common Compiler Issues
- `H` record missing or wrong options: include `ctl-opt` and the correct compile flags
- Type mismatch: ensure `dcl-s` and `dcl-ds` definitions match field lengths/types and no hidden truncation
- `SQLCODE` != 0: log values and use `exec sql set option commit = *none` (or `*chg`) for retries

### Runtime Diagnostics
- Use `DSPJOBLOG`, `STRDBG`, `WRKACTJOB` for job trouble shooting
- Check program dumps (`DSPJOBLOG`) and last commands (`WRKJOB`) when failures occur

## Integration Points

- CL/Batch: call RPG from CL with `CALL` or `SBMJOB`
- DB2: `RUNSQLSTM`, `CALL PGM(GETMSG)`, `CONNECTION` for remote database queries
- Web APIs: call external REST endpoints via HTTP services then map responses to RPG structures
- Workflow: integrate with Control Language and System i output queues for enterprise batch
