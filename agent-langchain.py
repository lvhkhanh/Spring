import time
from openai import RateLimitError
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.tools import tool

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

# 3. Create the LangChain Agent — that's it!
agent = create_agent(model, [multiply, divide])


def invoke_with_retry(agent, messages, max_retries: int = 5):
    backoff = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            return agent.invoke({"messages": messages})
        except RateLimitError:
            if attempt == max_retries:
                raise
            print(f"Rate limit hit (429). Retrying in {backoff:.1f}s... (attempt {attempt}/{max_retries})")
            time.sleep(backoff)
            backoff *= 2

# 4. Run it with retry support
result = invoke_with_retry(
    agent,
    [("user", "What is 15 multiplied by 8, then divided by 3?")]
)

print(result)
