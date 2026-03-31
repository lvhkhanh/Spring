---
name: as400
description: '**WORKFLOW SKILL** — Support IBM i / AS400 development, modernization, and operations. USE FOR: creating and refactoring RPG / COBOL / CL programs, converting legacy data models, integrating with APIs, managing jobs, libraries and spool files. DO NOT USE FOR: non-IBM i platforms, general mainframe z/OS, or unrelated web app code. INVOKES: file system and shell tools for code editing, command execution, and environment analysis.'
---

# AS400 / IBM i Development Skill

## Overview

This skill provides comprehensive AS400/IBM i development support including legacy application maintenance, modernization guidance, job/process management, database access, and API integration. It is optimized for common IBM i use cases and operational tasks.

## Key Capabilities

### Language Support
- RPG IV / ILE RPG
- CL (Control Language)
- COBOL (IBM i variant)
- SQLRPGLE and embedded SQL
- DDS and DDL for database files

### Project Operations
- Create and compile programs/commands (CRTRPGPGM, CRTBNDCL, CRTCLPGM, CRTSQLRPG)
- Manage libraries and object lists (DLTLIB, RCLSTG, WRKOBJ)
- Handle spool files and output queues (WRKSPLF, CPYSPLF, DLTSPLF)
- Schedule jobs with job scheduler (SBMJOB, SBMJOBD, WRKJOBSCDE)

### Database and Data Access
- DB2 for i SQL query formation and optimization
- File-level operations (PF, LF, DSPPFM, CPYTOIMPF, CPYFRMIMPF)
- Data migration and conversion strategies
- LOB, multi-member physical files, arrays, and data structure mapping

### Integration & Modernization
- REST/SOAP services using IBM i integrated web services
- Node.js / Java / Python JNI and data gateway patterns
- Free-form RPG modernization best practices
- API management and microservice integration through IBM API Connect

## Usage Examples

### Compile an RPG program
```
CRTRPGPGM PGM(MYLIB/MYPGM) SRCFILE(MYLIB/QRPGLESRC) SRCMBR(MYPGM)
```

### Fetch data with SQL
```
SELECT CUST_ID, CUST_NAME FROM MYLIB/CUSTOMERS WHERE STATUS = 'A';
```

### Run a batch job on schedule
```
SBMJOB JOB(MYJOB) JOBD(MYLIB/MYJOBD) CMD('CALL PGM(MYLIB/MYPGM)')
```

### Convert fixed-format RPG to free-form
```
- Replace old `C` and `F` specs with free-form `DCL-S` and HRA code.
- Use `RLNVAR` and `EVAL` for clarity.
```

## Common Patterns

### ILE RPG Module and Binding
- Use modules (`CRTRPGMOD`) and service programs (`CRTSRVPGM`) for reusable logic
- Define prototypes and export keywords
- Leverage activation groups with clear termination control

### CL Automation Script
```cl
PGM
 DCL VAR(&MSG) TYPE(*CHAR) LEN(100)
 CHGVAR VAR(&MSG) VALUE('Start processing')
 SBMJOB CMD(CALL PGM(MYLIB/MYPGM))
 ENDPGM
```

### SQL in RPGLE
```rpg
EXEC SQL
  SELECT COUNT(*) INTO :count
  FROM MYLIB/ORDERS
  WHERE ORDER_DATE >= :startDate;
```

### Error handling
- Use monitored programs and `MONMSG` in CL
- Trap and log errors with `QMHSNDPM` or job log analysis
- Validate file access with `CHKOBJ` and `CHKOBJL`

## Best Practices

- Use modular ILE design instead of monolithic programs
- Favor free-form RPG for readability and maintenance
- Keep data definitions in one place (DDL over DDS where possible)
- Keep library list minimal and explicit to avoid unbound references
- Use exception handlers and clear jstart/jterm logic in RPG
- Document dependencies and use source entry descriptions

## Troubleshooting

### Compile errors
- Check `WRKJOB` and spool file behavior after compile (DSPJOBLOG)
- Resolve binding errors by verifying service program exports and prototypes
- Missing objects: ensure library list includes dependent libraries

### Job failures
- Use `WRKJOB` and `DSPJOBLOG` to inspect exact fail action and messages
- Verify `QSYSOPR` messages and spool file output
- Ensure correct user profile authority for library & object operations

### Data access issues
- Validate library file path and member names
- Check data locking with `WRKOBJLCK`
- Confirm field types and lengths for SQL vs DDS alignment

## Integration Points

- **DevOps pipelines**: Git + Rational Team Concert + Jenkins for source control and build automation
- **Query tools**: Run SQL scripts via ACS, Db2 for i, or node-odbc
- **APIs**: Expose RPG business logic via REST services, OData endpoints, or MQ
- **Monitoring**: Use IBM Navigator for i and `WRKACTJOB` for performance metrics
- **Migration**: Refactor legacy RPG/Cobol to modern RPGLE + SQL, or to Node.js/Python service layers
