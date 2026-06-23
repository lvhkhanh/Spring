---
name: langchain-langgraph
description: '**WORKFLOW SKILL** - Build, refactor, debug, test, and productionize LLM applications with LangChain and LangGraph. USE FOR: LangChain agents, model/tool integrations, RAG pipelines, structured output, middleware, streaming, LangGraph state machines, durable agent workflows, persistence, checkpoints, memory, human-in-the-loop interrupts, multi-agent orchestration, LangSmith tracing/evaluation, and Python or TypeScript agent applications. DO NOT USE FOR: generic AI/ML model training, unrelated chatbot UI work, or non-agent application code with no LangChain/LangGraph surface. INVOKES: file system tools for code/config changes, terminal for package/test commands, official LangChain/LangGraph docs when current APIs or migration details matter.'
---

# LangChain / LangGraph Development Skill

## Overview

This skill supports agentic application development with LangChain and LangGraph. Use LangChain for composable agent harnesses, model/tool abstractions, middleware, structured output, retrieval, and provider portability. Use LangGraph when the workflow needs explicit state, branching, cycles, persistence, interrupts, streaming, long-running execution, or deterministic orchestration around agent behavior.

Prefer official LangChain documentation when API details matter because LangChain and LangGraph change frequently:
- Python LangChain: `https://docs.langchain.com/oss/python/langchain/overview`
- Python LangGraph: `https://docs.langchain.com/oss/python/langgraph/overview`
- TypeScript LangChain: `https://docs.langchain.com/oss/javascript/langchain/overview`
- TypeScript LangGraph: `https://docs.langchain.com/oss/javascript/langgraph/overview`

## Framework Choice

### Choose LangChain
- Create a standard tool-calling agent with `create_agent`
- Integrate chat models, embeddings, tools, prompts, retrievers, and middleware
- Need structured output, guardrails, short-term memory, streaming, or provider switching
- Want a high-level agent loop without manually defining graph state and edges

### Choose LangGraph
- Need explicit workflow control with nodes, edges, conditional routing, loops, or subgraphs
- Need persistence, checkpointers, resumability, time travel, or fault tolerance
- Need human-in-the-loop review through interrupts and state updates
- Need long-running, stateful, multi-step, or multi-agent orchestration
- Need deterministic steps mixed with LLM/tool calls

### Use Both
- Build model/tool primitives with LangChain and orchestrate them with LangGraph
- Start with LangChain for simple agents, then move to LangGraph when state, branching, or recovery becomes central
- Use LangSmith for traces, evaluation, debugging, and deployment observability across both

## Development Workflow

1. Identify runtime and language: Python or TypeScript.
2. Inspect existing package versions and imports before adding dependencies.
3. Define the agent contract: input shape, output shape, tools, side effects, memory needs, and error behavior.
4. Choose the smallest abstraction that fits: `create_agent` for simple agents, `StateGraph` for controlled workflows.
5. Keep prompts, tools, state schemas, graph nodes, and persistence boundaries separate.
6. Add tracing, targeted tests, and at least one smoke invocation before considering the workflow complete.

## Project Setup

### Python
```bash
pip install -U langchain langgraph
```

Add provider packages only when used, for example:
```bash
pip install -U "langchain[openai]"
```

### TypeScript
```bash
npm install langchain @langchain/langgraph
```

Add provider packages only when used.

### Environment
- Keep provider keys in `.env`, secret managers, or deployment config; never hard-code them.
- Use `LANGSMITH_TRACING=true` and a LangSmith API key when debugging or evaluating agent behavior.
- Pin or lock dependency versions for production systems.

## LangChain Patterns

### Agent Harness
Use `create_agent` for a compact, configurable tool-calling loop.

```python
from langchain.agents import create_agent

def get_order_status(order_id: str) -> str:
    """Return the shipping status for an order."""
    return "in_transit"

agent = create_agent(
    model="openai:gpt-4.1",
    tools=[get_order_status],
    system_prompt="You help customers check order status.",
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Where is order A123?"}]
})
```

### Tool Design
- Give each tool one responsibility and a descriptive docstring.
- Validate inputs before external calls.
- Return structured data when downstream code needs to branch on it.
- Make side effects explicit in names and descriptions.
- Wrap flaky external calls with timeout, retry, and clear error behavior.

### Structured Output
- Use schema-backed structured output when the application consumes fields programmatically.
- Validate model output before persistence or downstream side effects.
- Include tests for malformed, missing, or unexpected fields.

### RAG
- Separate ingestion, indexing, retrieval, reranking, answer generation, and citation formatting.
- Store document IDs and metadata with chunks.
- Test retrieval quality independently from generation quality.
- Prefer small, inspectable retrieval chains before adding agentic routing.

## LangGraph Patterns

### StateGraph Skeleton
Use `StateGraph` when the workflow benefits from explicit state transitions.

```python
from langgraph.graph import StateGraph, MessagesState, START, END

def call_model(state: MessagesState):
    return {"messages": [{"role": "assistant", "content": "hello"}]}

graph = StateGraph(MessagesState)
graph.add_node("call_model", call_model)
graph.add_edge(START, "call_model")
graph.add_edge("call_model", END)

app = graph.compile()
app.invoke({"messages": [{"role": "user", "content": "hi"}]})
```

### State Design
- Make state explicit and typed.
- Keep persistent state minimal: messages, task status, decisions, artifacts, and resumable checkpoints.
- Store large documents, files, or binary payloads outside graph state and reference them by ID/path.
- Treat state fields as a public contract between nodes.

### Nodes and Edges
- Keep nodes small and named after the action they perform.
- Put deterministic validation and routing in normal code, not in prompts.
- Use conditional edges for routing decisions that must be inspectable.
- Use subgraphs when a workflow has a reusable lifecycle or nested responsibility.

### Persistence and Checkpoints
- Add a checkpointer when users expect conversation continuity, pause/resume, retries, or long-running execution.
- Use stable thread/session IDs.
- Confirm which fields are persisted and which are transient.
- Test restart behavior by invoking, interrupting or failing, and resuming from checkpoint.

### Human-in-the-Loop
- Use interrupts before irreversible side effects, high-cost operations, sensitive data access, or external writes.
- Show enough state for a human to approve, edit, or reject the next step.
- Resume with explicit human decisions rather than relying on hidden prompt context.

### Streaming
- Stream events when the UI or operator needs progress, tokens, tool calls, or state transitions.
- Keep stream payloads stable and documented for frontend consumers.
- Avoid leaking secrets, raw credentials, or excessive internal state through stream events.

## Testing

### Unit Tests
- Test tools as plain functions.
- Test graph nodes with representative state dictionaries.
- Test routing functions independently.
- Mock LLM/provider calls unless the test is explicitly an integration smoke test.

### Integration Tests
- Invoke the full agent or graph with realistic inputs.
- Verify final output, important intermediate state, tool calls, and error paths.
- Include tests for empty retrieval results, tool failures, invalid structured output, and retries.

### Observability Tests
- Enable LangSmith tracing for non-trivial debugging sessions.
- Check that traces show useful node names, tool names, input/output shapes, and failure reasons.
- Add evaluation datasets for workflows where answer quality matters.

## Production Checklist

- Define model, provider, timeout, retry, and fallback policy.
- Separate prompts/config from business logic where practical.
- Add structured logging around graph starts, node failures, tool calls, and external writes.
- Enforce rate limits and cost controls for model and tool calls.
- Guard sensitive operations with authorization and human approval where needed.
- Add persistence and replay tests for long-running workflows.
- Document deployment environment variables and secret requirements.
- Pin dependencies and record migration notes when upgrading LangChain or LangGraph.

## Troubleshooting

### Import or API Breakage
- Check installed versions and official docs for the exact language/runtime.
- Search for renamed packages, provider split-outs, or migration guide notes.
- Update imports consistently across code, tests, and docs.

### Agent Loops or Bad Tool Calls
- Inspect tool descriptions and schemas.
- Add guardrails or middleware for tool selection.
- Limit tool scope and require explicit arguments.
- Trace the run to find where the loop starts.

### Graph State Bugs
- Print or trace state at node boundaries.
- Verify each node returns only intended state updates.
- Check reducers/merge behavior for list-like fields such as messages.
- Add tests for branching and resume paths.

### Persistence Bugs
- Confirm thread/session IDs are stable.
- Verify checkpointer configuration is used by the compiled graph.
- Reproduce with the smallest graph that persists and resumes one state field.

### RAG Quality Problems
- Inspect retrieved chunks before changing prompts.
- Tune chunking, metadata filters, embeddings, and reranking separately.
- Add retrieval evaluation cases with expected source documents.

## Integration Points

- **Model providers**: OpenAI, Anthropic, Google, Azure, AWS Bedrock, OpenRouter, Ollama, and local model backends
- **Vector stores**: Chroma, FAISS, Milvus, Pinecone, Weaviate, Redis, PostgreSQL/pgvector
- **APIs and tools**: REST, GraphQL, SQL databases, MCP servers, internal service clients
- **Apps**: FastAPI, Flask, Django, Express, Next.js, background workers, CLIs
- **Observability**: LangSmith traces, evaluations, datasets, Studio, and deployment monitoring
