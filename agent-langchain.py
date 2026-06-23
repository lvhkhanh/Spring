import os
import time
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.tools import tool

try:
    import ibm_db_dbi
except ImportError:
    ibm_db_dbi = None

# 1. Initialize the model
model = init_chat_model("openai:gpt-4o")

# 2. Define your tools
@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together. Use for multiplication operations."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divide the first number by the second. Returns error if dividing by zero."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def get_db2_connection_string() -> str:
    host = os.environ.get("DB2_HOST")
    port = os.environ.get("DB2_PORT", "50000")
    database = os.environ.get("DB2_DATABASE")
    user = os.environ.get("DB2_USER")
    password = os.environ.get("DB2_PASSWORD")

    missing = [name for name, value in [
        ("DB2_HOST", host),
        ("DB2_DATABASE", database),
        ("DB2_USER", user),
        ("DB2_PASSWORD", password),
    ] if not value]
    if missing:
        raise RuntimeError(
            f"Missing DB2 connection environment variables: {', '.join(missing)}"
        )

    return (
        f"DATABASE={database};"
        f"HOSTNAME={host};"
        f"PORT={port};"
        "PROTOCOL=TCPIP;"
        f"UID={user};"
        f"PWD={password};"
    )

@tool
def query_db2(sql: str) -> str:
    """Run a SQL query against DB2 and return the first rows as text."""
    if ibm_db_dbi is None:
        return (
            "The ibm_db_dbi package is not installed. "
            "Install it with `pip install ibm_db_dbi` or `pip install ibm_db`."
        )

    try:
        dsn = get_db2_connection_string()
        conn = ibm_db_dbi.connect(dsn, "", "")
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchmany(10)
        columns = [desc[0] for desc in cursor.description] if cursor.description else []

        if not rows:
            return "Query executed successfully, but no rows were returned."

        output_rows = ["\t".join(columns)]
        for row in rows:
            output_rows.append("\t".join(str(item) for item in row))

        return "\n".join(output_rows)
    except Exception as exc:
        return f"DB2 query failed: {exc}"
    finally:
        try:
            cursor.close()
            conn.close()
        except Exception:
            pass

@tool
def describe_db2_connection() -> str:
    """Describe the current DB2 connection settings without revealing the password."""
    host = os.environ.get("DB2_HOST", "<unset>")
    port = os.environ.get("DB2_PORT", "50000")
    database = os.environ.get("DB2_DATABASE", "<unset>")
    user = os.environ.get("DB2_USER", "<unset>")
    return f"DB2 host={host}, port={port}, database={database}, user={user}"

# 3. Create the LangChain Agent — that's it!
agent = create_agent(model, [multiply, divide, query_db2, describe_db2_connection])


def is_rate_limit_error(exc: Exception) -> bool:
    message = str(exc).lower()
    status_code = getattr(exc, "status_code", None)
    return status_code == 429 or "429" in message or "rate limit" in message


def invoke_with_retry(agent, messages, max_retries: int = 5):
    backoff = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            return agent.invoke({"messages": messages})
        except Exception as exc:
            if not is_rate_limit_error(exc) or attempt == max_retries:
                raise
            print(f"Rate limit hit (429). Retrying in {backoff:.1f}s... (attempt {attempt}/{max_retries})")
            time.sleep(backoff)
            backoff *= 2

# 4. Run it with retry support
result = invoke_with_retry(
    agent,
    [
        (
            "user",
            "Run this DB2 query and return the first 10 rows: SELECT * FROM MYSCHEMA.MYTABLE FETCH FIRST 10 ROWS ONLY"
        )
    ]
)

print(result)
