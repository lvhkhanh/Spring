---
name: cl
description: '**WORKFLOW SKILL** — Create, refactor, debug, and optimize IBM i AS/400 CL (Control Language) scripts and batch workflows. USE FOR: CL program development, job scheduling, command flow logic, variable handling, error recovery, and runtime environment management. DO NOT USE FOR: non-IBM i languages or platforms unrelated to CL/OS/400 system programming. INVOKES: file system tools for script creation/modification, terminal for command examples, and knowledge of IBM i CL best practices.'
---

# IBM i CL (Control Language) Skill

## Overview

This skill supports IBM i (AS/400) Control Language (CL) automation: job scripts, command sequences, spool and output processing, job scheduling, and environment configuration. It focuses on practical CL usage, system command handling, variable iteration, error checks, and cross-component interactions with RPGLE, SQL, and file systems.

## Key Capabilities

### Script Generation
- Create CL source (CLP) scripts for job control and scheduled tasks
- Craft command flow (IF/ELSE/DO/ENDDO/DOFOR)
- Handle file transfers (CPYTOSTMF/CPYFRMSTMF, CPYTOIMPF/CPYFRMIMPF) and library operations (DLTLIB, RCLSTG)
- Manage service programs, objects, and libraries (CRTxxx, DLTxxx, ADDLIBLE, RMVLIBLE)

### Job and Scheduler Management
- Build jobs with SBMJOB, SNDPM, and RTVJOBA for runtime context
- Configure job descriptions, output queues, and message queues
- Explain use of WRKJOB, WRKOUTQ, and WRKMSGD for operational status

### Error Handling
- Use MONITOR/ON-ERROR and IF COND(&MSGID *EQ ...) for robust recovery
- Handle return codes via RTNxx and required action messages
- Parse message queues (SNDPGMMSG, RCVMSG) for actionable logging

### Integration
- Invoke RPGLE / SQL procedures from CL via CALL and RUNSQLSTM
- Coordinate data pipelines with DB2 commands (RUNSQL, RUNQRY)
- Use FTP and SFTP command objects for data exchange with external hosts
- Interface with APIs via HTTP or integration services if available

## Usage Examples

### Basic CL Program Template
```
PGM
  DCL VAR(&JOB) TYPE(*CHAR) LEN(10)
  RTVJOBA JOB(&JOB)
  SNDPGMMSG MSGID(CPF9898) MSGF(QCPFMSG) MSGDTA('Start: ' *CAT &JOB)

  /* Business commands */
  CPYTOIMPF FROMFILE(MYLIB/MYFILE) TOSTMF('/tmp/out.csv') MBROPT(*REPLACE) STMFCODPAG(*PCASCII)

  IF COND((&RC *NE 0)) THEN(DO)
    MONMSG MSGID(CPF0000) EXEC(DO)
      SNDMSG MSG('File copy failed for &JOB rc=&RC') TOPGMQ(*EXT)
      ENDPGM
    ENDDO
  ENDIF

  SNDPGMMSG MSGID(CPF9898) MSGF(QCPFMSG) MSGDTA('Complete: ' *CAT &JOB)
ENDPGM
```

### Loop Over Files
```
PGM
  DCL VAR(&FILE) TYPE(*CHAR) LEN(10)
  DCL VAR(&CTR) TYPE(*DEC) LEN(5 0)

  SETLL FILEKEY MYLIB/MYFILE *FILE
  RCVF
  DOU COND(&EOF = '1')
    CHGVAR VAR(&CTR) VALUE(&CTR + 1)
    /* Process each record from the file */
    RCVF
  ENDDO

  SNDPGMMSG MSG('Processed records=' *CAT &CTR) TOPGMQ(*EXT)
ENDPGM
```

### Job Submission with Dependencies
```
PGM
  SBMJOB CMD(CALL PGM(MYLIB/STEP1)) JOB(MYJOB1) JOBQ(QBATCH)
  SBMJOB CMD(CALL PGM(MYLIB/STEP2)) JOB(MYJOB2) JOBQ(QBATCH) JOBD(MYJOBD) JOBPTY(1) INLLIBL(MYLIB) \
    PGMQ(QGPL) RUNPTY(*SAME) SJID(MYJOB1)
ENDPGM
```

## Common Patterns

### Conditional Processing
- `IF COND(condition) THEN(DO) ... ENDDO`
- `MONMSG` with wildcards `*EXCPT`, `*CPF` and query `MSGID(...)`
- `GOTO` for failure paths only when necessary

### System context and JRNL
- `RTVJOBA`, `RTVSYSVAL` and `RTVUSRPRF` for dynamic logic
- Use `CHGVAR` for intermediate state e.g. run counts and status tracking

### Transaction and DB2 control
- `RUNSQLSTM` inside CL to execute stored SQL from source member
- `DLTF` and `CRTDUPOBJ` for temporary objects around batch tasks

## Best Practices

- Keep CL programs small, modular, and business-meaningful
- Prefer CMD objects for reusable task units and API-like invocation
- Use descriptive message texts and message IDs to ease debugging
- Always set `MSGQ(*EXT)` for operational logs in production
- Validate results after each command with `MONMSG MSGID(CPF0000)`
- Use `CALL PGM()` instead of `GOTO` for maintainable flow

## Troubleshooting

### RC handling
- `RC` is set for command errors; check with `IF COND(&RC *NE 0)` or `MONMSG`
- `MONMSG MSGID(CPF0000) EXEC(DO ... ENDDO)` catches all exceptions

### Common CL errors
- `CPF0000` missing data or syntax; fix code or variable length
- `CPF9898` custom messages for status/tracing
- `CPFxxxx` indicates specific command failures

### Messaging and logs
- Use `DSPMSG MSGQ(MYLIB/QSYSOPR)` or `QSYSOPR` for history
- Use job logs `DSPJOBLOG` or `WRKJOB` to inspect step details

## Integration Points

- **RPGLE**: call `CALL PGM(MYLIB/RPGPROGRAM) PARM(...)` from CL
- **DB2/SQL**: `RUNSQL`, `RUNSQLSTM`, `RUNQRY` statements
- **Scheduling**: integrate with `WRKJOBSCDE`, `ADDJOBSCDE`, and batch windows
- **External file exchange**: `FTP`, `SFTP`, `STPDMN` operations where supported
- **Monitoring**: use system operations like `WRKACTJOB`, `WRKOUTQ`, `WRKMBRPDM`
