import os
import time

from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    function_tool,
    input_guardrail,
)
from openai import RateLimitError

try:
    import ibm_db_dbi
except ImportError:
    ibm_db_dbi = None


@function_tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together. Use for multiplication operations."""
    return a * b


@function_tool
def divide(a: float, b: float) -> str:
    """Divide the first number by the second. Returns an error if dividing by zero."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return str(a / b)


def get_db2_connection_string() -> str:
    host = os.environ.get("DB2_HOST")
    port = os.environ.get("DB2_PORT", "50000")
    database = os.environ.get("DB2_DATABASE")
    user = os.environ.get("DB2_USER")
    password = os.environ.get("DB2_PASSWORD")

    missing = [
        name
        for name, value in [
            ("DB2_HOST", host),
            ("DB2_DATABASE", database),
            ("DB2_USER", user),
            ("DB2_PASSWORD", password),
        ]
        if not value
    ]
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


@function_tool
def query_db2(sql: str) -> str:
    """Run a SQL query against DB2 and return the first rows as text."""
    if ibm_db_dbi is None:
        return (
            "The ibm_db_dbi package is not installed. "
            "Install it with `pip install ibm_db_dbi` or `pip install ibm_db`."
        )

    conn = None
    cursor = None
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
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if conn is not None:
            try:
                conn.close()
            except Exception:
                pass


@function_tool
def describe_db2_connection() -> str:
    """Describe the current DB2 connection settings without revealing the password."""
    host = os.environ.get("DB2_HOST", "<unset>")
    port = os.environ.get("DB2_PORT", "50000")
    database = os.environ.get("DB2_DATABASE", "<unset>")
    user = os.environ.get("DB2_USER", "<unset>")
    return f"DB2 host={host}, port={port}, database={database}, user={user}"


ALLOWED_TOPIC_TERMS = (
    "ai",
    "artificial intelligence",
    "machine learning",
    "ml",
    "llm",
    "agent",
    "automation",
    "model",
    "neural",
    "robotics",
    "future",
    "brighter",
    "optimism",
    "hope",
    "sustainable",
    "sustainability",
    "education",
    "healthcare",
    "climate",
    "innovation",
    "progress",
    "better world",
)


def input_to_text(input_value: str | list[TResponseInputItem]) -> str:
    if isinstance(input_value, str):
        return input_value
    return " ".join(str(item) for item in input_value)


@input_guardrail(name="ai_and_brighter_future_only", run_in_parallel=False)
def ai_and_brighter_future_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    """Allow only prompts about AI or optimistic brighter-future topics."""
    del ctx, agent
    text = input_to_text(input).lower()
    is_allowed = any(term in text for term in ALLOWED_TOPIC_TERMS)

    return GuardrailFunctionOutput(
        output_info={
            "allowed": is_allowed,
            "policy": "Only AI and brighter-future topics are allowed.",
        },
        tripwire_triggered=not is_allowed,
    )


agent = Agent(
    name="AI brighter future assistant",
    model="gpt-4o",
    instructions=(
        "You are a helpful assistant that only answers questions about AI or optimistic, "
        "brighter-future topics. If a request is outside those topics, politely say you "
        "can only help with AI and brighter-future topics. You can run basic math tools "
        "and DB2 queries only when they support an allowed topic."
    ),
    tools=[multiply, divide, query_db2, describe_db2_connection],
    input_guardrails=[ai_and_brighter_future_guardrail],
)


cobol_to_java_agent = Agent(
    name="COBOL to Java converter",
    model="gpt-4o",
    instructions=(
        "You are a senior modernization engineer specializing in converting COBOL "
        "programs to Java. Convert COBOL code into readable, idiomatic Java while "
        "preserving business behavior. Map COBOL divisions, data declarations, file "
        "handling, conditionals, loops, arithmetic, and paragraphs into clear Java "
        "classes, methods, fields, and control flow. When behavior is ambiguous, keep "
        "the safest equivalent and add a short TODO comment. Return Java code first, "
        "then a concise migration note only when useful."
    ),
)


def is_rate_limit_error(exc: Exception) -> bool:
    message = str(exc).lower()
    status_code = getattr(exc, "status_code", None)
    return isinstance(exc, RateLimitError) or status_code == 429 or "429" in message or "rate limit" in message


def run_with_retry(prompt: str, selected_agent: Agent = agent, max_retries: int = 5):
    backoff = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            return Runner.run_sync(selected_agent, prompt)
        except Exception as exc:
            if not is_rate_limit_error(exc) or attempt == max_retries:
                raise
            print(f"Rate limit hit (429). Retrying in {backoff:.1f}s... (attempt {attempt}/{max_retries})")
            time.sleep(backoff)
            backoff *= 2


def convert_cobol_to_java(cobol_source: str, max_retries: int = 5) -> str:
    result = run_with_retry(
        "Convert this COBOL program to Java:\n\n" + cobol_source,
        selected_agent=cobol_to_java_agent,
        max_retries=max_retries,
    )
    return result.final_output


if __name__ == "__main__":
    try:
        result = run_with_retry(
            "How can AI help build a brighter future for education and healthcare?"
        )
        print(result.final_output)
    except InputGuardrailTripwireTriggered:
        print("I can only help with AI and brighter-future topics.")
