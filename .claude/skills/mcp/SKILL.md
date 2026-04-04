---
name: mcp
description: '**WORKFLOW SKILL** — Design, configure, integrate, and troubleshoot Model Context Protocol (MCP) servers, tools, and workflows. USE FOR: defining MCP server capabilities, wiring tool interfaces, configuring transports, debugging client-server interactions, shaping resource exposure, and improving agent tooling flows. DO NOT USE FOR: unrelated application business logic, generic API design without MCP context, or non-tooling-only tasks with no protocol integration. INVOKES: file system tools for config and server code changes, terminal for local server execution and diagnostics, and semantic search for protocol-specific patterns and integration points.'
---

# MCP Development Skill

## Overview

This skill supports work on Model Context Protocol (MCP) integrations, including server design, tool exposure, transport configuration, resource modeling, and debugging agent-to-tool interactions. It is for building or refining MCP-based workflows that let assistants access structured tools, resources, and capabilities safely and predictably.

## Key Capabilities

### MCP Server Design
- Create or refine MCP servers that expose tools, resources, and prompts
- Define capability boundaries and clear server responsibilities
- Structure handlers for tool calls, resource reads, and template-based access
- Keep protocol-facing code consistent and easy to extend

### Tool & Resource Integration
- Add tool definitions with clear inputs, outputs, and failure behavior
- Expose static or dynamic resources in a predictable format
- Design resource templates for parameterized access patterns
- Map backend logic cleanly to MCP interfaces without leaking unnecessary internals

### Transport & Configuration
- Configure local or remote MCP transports appropriately
- Wire client/server settings, URLs, authentication hooks, and environment variables
- Organize config files and startup commands for reliable local development
- Support integration with agent platforms, IDEs, and automation workflows

### Debugging & Diagnostics
- Investigate server startup failures, transport issues, and malformed responses
- Diagnose missing tools, empty resources, or schema mismatches
- Trace request/response flow between client and MCP server
- Improve logging, error messages, and validation around protocol boundaries

### Workflow & Safety Design
- Keep tools focused and composable
- Design resource access with least privilege in mind
- Separate read-only and side-effecting operations clearly
- Add graceful fallbacks when external systems fail or data is unavailable

## Usage Examples

### Create an MCP server
```text
Create an MCP server that exposes tools for listing Jira tickets and reading ticket details.
Define the tools, resource structure, and local configuration needed to run it.
```

### Add a new MCP tool
```text
Add a tool to this MCP server for searching customer records by email.
Follow the existing schema and error handling pattern.
```

### Debug an MCP integration
```text
The client connects to the MCP server but the expected tools are missing.
Find the issue in the server registration or capability configuration.
```

### Improve resource modeling
```text
Refactor this MCP server so large datasets are exposed through resource templates instead of one huge static resource.
```

## Common Patterns

### Focused Tool Design
```text
Prefer tools that:
- do one thing clearly
- validate inputs early
- return predictable structured outputs
- separate success and error states explicitly
```

### Resource Exposure Strategy
```text
Use:
- static resources for stable reference material
- resource templates for parameterized lookups
- tools for actions, mutations, or expensive dynamic operations
```

### Safe Capability Boundaries
```text
1. Define what the server should expose
2. Keep side effects explicit
3. Avoid over-broad file or network access
4. Return useful diagnostics without leaking secrets
```

### MCP Debug Loop
```text
1. Verify server startup and transport
2. Confirm capability registration
3. Inspect schemas and handler wiring
4. Reproduce with the smallest failing request
5. Tighten validation and logging
```

## Best Practices

- Keep each MCP tool narrowly scoped and well named
- Prefer structured outputs over free-form text when clients need to compose results
- Make input schemas strict enough to prevent ambiguous calls
- Treat resource URIs and template parameters as API surface that should stay stable
- Separate read operations from write operations where possible
- Add targeted logging around protocol entry points and external integrations
- Validate data before returning it to the client
- Keep authentication, secrets, and side effects outside user-visible payloads

## Troubleshooting

### Server starts but no tools appear
- Check capability registration and startup order
- Confirm the transport is connected to the intended server instance
- Verify tool definitions are exported and reachable by the server bootstrap code

### Tools appear but calls fail
- Compare declared input schema with the actual handler expectations
- Check argument parsing, serialization, and backend dependency wiring
- Return clearer structured errors for invalid input and upstream failures

### Resource reads return empty or stale data
- Validate the URI mapping and template parameter handling
- Check caching assumptions and refresh behavior
- Confirm the backing data source is reachable and populated

### Transport or connection problems
- Verify local command, URL, port, or environment settings
- Inspect logs for handshake or protocol version mismatches
- Start with a minimal local configuration before adding auth or remote routing

### Over-broad or unsafe exposure
- Remove tools that combine unrelated responsibilities
- Restrict resources to the minimum useful surface
- Split mutating operations from read-only discovery workflows

## Integration Points

- **Agent clients**: Claude, Codex, IDE-integrated assistants, custom agent hosts
- **Transports**: stdio, streamable HTTP, local process execution, remote server endpoints
- **Server runtimes**: Node.js, Python, TypeScript, Go, Rust
- **Backends**: REST APIs, databases, file systems, ticketing systems, internal services
- **Validation**: JSON schemas, typed interfaces, contract tests
- **Diagnostics**: structured logging, startup checks, request tracing, local smoke tests
