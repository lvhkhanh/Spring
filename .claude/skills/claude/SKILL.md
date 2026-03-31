---
name: claude
description: '**WORKFLOW SKILL** — Assist with Claude agent/system prompt design, skill development, instruction zoning, and workflow automation. USE FOR: crafting prompt templates; designing skills, agents, roles, and tool chains; validating prompt safety and guidelines; debugging agent behavior. DO NOT USE FOR: non-agent UI design, direct business logic implementation outside prompt/agent pattern context. INVOKES: file system tools for skill files, semantic search for pattern discovery, terminal for repository operations.'
---

# Claude Agent and Skill Development

## Overview

This skill provides structured support for building and refining Claude-style agent skills, including prompt composition, instruction structure, system role definition, and safe behavior controls.

## Key Capabilities

### Skill Definition
- Create skill metadata and YAML frontmatter
- Define skill name, description, and invocation context
- Provide clear `USE FOR` and `DO NOT USE FOR` boundaries
- Add practical examples and usage scenarios

### Prompt Engineering
- Formulate system, user, and assistant messages
- Design instruction templates with placeholders
- Optimize for specificity, clarity, and robustness
- Implement safety and content policy constraints

### Agent Architecture
- Guide action pipelines (semantic search, tools, API calls)
- Map user intents to skill workflows and tools
- Design fallbacks and error handling strategies
- Support orchestration across multi-skill setups

### Validation & Testing
- Review correctness of skill documentation
- Verify edge cases and failure modes in prompts
- Provide test query examples and expected outputs
- Suggest logging and telemetry points

## Usage Examples

### Creating a New Claude Skill
```
Generate a Claude skill for "data ingestion" that includes:
- YAML frontmatter
- clear `OVERVIEW`, `CAPABILITIES`, and `EXAMPLES`
- tooling guidance (HTTP, DB, file systems)
```

### Refining an Existing Skill
```
Review this Claude skill and update:
- descriptions for accuracy
- best practices section for deployment
- troubleshooting scenarios with clear next steps
```

### Debugging Prompt Behavior
```
Analyze this prompt template and identify:
- ambiguous instructions
- potential hallucination triggers
- user intent mismatches
```

## Common Patterns

### Modular Skill Layout
- `name`, `description` frontmatter
- `Overview`, `Key Capabilities`, `Usage Examples`
- `Common Patterns`, `Best Practices`, `Troubleshooting`, `Integration Points`

### Minimal-Mail Flow
- Use short, precise language in instructions
- Avoid open-ended maxima unless needed
- Include explicit success and failure criteria

### Safety Conditions
- Always define forbidden content categories
- Add a fallback policy for unconstrained inputs
- Confirm prompt is aligned with content policy

## Best Practices

- Keep descriptions concise and actionable
- Use consistent terminology and naming conventions
- Provide code snippets for practical implementation
- Include troubleshooting checklists and validation steps
- Update skills with real bug reports and usage feedback
- Avoid over-specification that blocks valid user goals

## Troubleshooting

### Common Issues
- Conflicting instructions inside the same prompt
- Vague requirements leading to unpredictable outputs
- Missing tool invocation info for multi-step workflows
- Lack of guardrail language for policy-sensitive domains

### 5-Step Validation
1. Confirm frontmatter syntax and fields
2. Check constants: skill name, intent, scope
3. Run sample queries through list of examples
4. Validate negative cases (forbidden behaviors)
5. Document outcomes and apply iterative improvements

## Integration Points

- **Toolchains**: agent, semantic search, external tools
- **Repositories**: code, docs, config, policy artifacts
- **Operating environments**: local, cloud, CI/CD
- **Stakeholders**: product, security, developer experience
