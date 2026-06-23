DB2 MCP (minimal)
===================

This folder contains a minimal HTTP adapter to access a DB2 database. It is intended to act as a lightweight MCP-style service that other agents/tools can call.

Quick start
-----------

1. Copy environment variables (or create a `.env` file):

```
DB2_HOST=localhost
DB2_PORT=50000
DB2_DATABASE=SAMPLE
DB2_USER=db2inst1
DB2_PASSWORD=Secret123
DB2_MCP_PORT=8080
```

2. Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r mcp/requirements.txt
```

3. Run the server:

```bash
python mcp/db2_mcp.py
```

4. Query the server:

```bash
curl -X POST http://localhost:8080/query -H 'Content-Type: application/json' -d '{"sql": "SELECT * FROM SYSCAT.TABLES FETCH FIRST 5 ROWS ONLY"}'
```

Notes
-----
- This server is intentionally minimal. For production, add authentication, input validation, query timeouts, and connection pooling.
- `ibm_db` requires native DB2 client libraries on some platforms; prefer using the official Docker image for local DB2 testing.
