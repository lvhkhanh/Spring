"""Simple DB2 MCP-like HTTP server.

Provides a minimal HTTP API to run read-only queries against a local/remote DB2 instance.
This is intended as a lightweight MCP-style adapter you can run locally or in a container.

Endpoints:
- POST /query  -> {"sql": "SELECT ..."}
- GET  /info   -> connection info (no password)

Environment variables:
- DB2_HOST
- DB2_PORT (default 50000)
- DB2_DATABASE
- DB2_USER
- DB2_PASSWORD

Install requirements in the project: `pip install -r mcp/requirements.txt`
Run: `python mcp/db2_mcp.py`
"""

from flask import Flask, request, jsonify
import os
import traceback

try:
    import ibm_db_dbi
except Exception:
    ibm_db_dbi = None

app = Flask(__name__)


def get_db2_dsn():
    host = os.environ.get("DB2_HOST")
    port = os.environ.get("DB2_PORT", "50000")
    database = os.environ.get("DB2_DATABASE")
    user = os.environ.get("DB2_USER")
    password = os.environ.get("DB2_PASSWORD")

    missing = [name for name, value in [("DB2_HOST", host), ("DB2_DATABASE", database), ("DB2_USER", user), ("DB2_PASSWORD", password)] if not value]
    if missing:
        raise RuntimeError(f"Missing DB2 environment variables: {', '.join(missing)}")

    dsn = (
        f"DATABASE={database};"
        f"HOSTNAME={host};"
        f"PORT={port};"
        "PROTOCOL=TCPIP;"
        f"UID={user};"
        f"PWD={password};"
    )
    return dsn


def connect_db2():
    if ibm_db_dbi is None:
        raise RuntimeError("ibm_db_dbi (or ibm_db) is not installed. Install with `pip install ibm_db ibm_db_dbi`.")
    dsn = get_db2_dsn()
    # ibm_db_dbi.connect accepts either (dsn, '', '') or (database, user, password) depending on installation
    return ibm_db_dbi.connect(dsn, "", "")


@app.route("/info", methods=["GET"])
def info():
    host = os.environ.get("DB2_HOST", "<unset>")
    port = os.environ.get("DB2_PORT", "50000")
    database = os.environ.get("DB2_DATABASE", "<unset>")
    user = os.environ.get("DB2_USER", "<unset>")
    return jsonify({"host": host, "port": port, "database": database, "user": user})


@app.route("/query", methods=["POST"])
def query():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON with key 'sql'"}), 400
    payload = request.get_json()
    sql = payload.get("sql")
    if not sql:
        return jsonify({"error": "Missing 'sql' field"}), 400

    try:
        conn = connect_db2()
        cur = conn.cursor()
        cur.execute(sql)
        cols = [d[0] for d in cur.description] if cur.description else []
        rows = cur.fetchmany(50)
        result = {"columns": cols, "rows": [list(r) for r in rows]}
        cur.close()
        conn.close()
        return jsonify(result)
    except Exception as exc:
        tb = traceback.format_exc()
        return jsonify({"error": str(exc), "trace": tb}), 500


if __name__ == "__main__":
    port = int(os.environ.get("DB2_MCP_PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
