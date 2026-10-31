# AS/400 RPG + DB2 CRUD Sample

This sample demonstrates a minimal CRUD application using:
- RPGLE with embedded SQL
- DB2 table access
- a small CL wrapper for program execution

## Files
- `EMPLOYEE.DDL` — DB2 DDL script to create the `EMPLOYEE` table
- `EMPCRUD.RPGLE` — RPG program with Create, Read, Update, Delete and List operations
- `EMPCRUD.CLP` — CL wrapper to call the RPG program

## Build and run
1. Create or use a library in your AS/400 environment.
2. Execute `EMPLOYEE.DDL` in STRSQL, RUNSQLSTM, or another SQL tool.
3. Compile the RPG program with `CRTSQLRPGI` or `CRTRPGMOD`.
4. Compile the CL program with `CRTCLPGM` if you want a wrapper.
5. Call the program in a 5250 session:
   - `CALL EMPCRUD`
   - or if using CL wrapper: `CALL EMPCRUD`

## Notes
- The sample uses `DSPly` for simple interactive input/output.
- Run in an environment where the current library contains the `EMPLOYEE` table or qualify the table name.
- Adjust the SQL schema if your system requires a specific library name.
