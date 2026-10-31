---
name: legacy-flowchart
description: '**WORKFLOW SKILL** — Create flowchart and control-flow visualizations from legacy RPG/COBOL source code. USE FOR: extracting program structure, decisions, loops, file I/O, and business process flows from RPG, COBOL, CL, and DB2 artifacts into diagrams and structured flowcharts. DO NOT USE FOR: generic UML modeling unrelated to legacy code or runtime debugger output. INVOKES: file system tools for source inspection, terminal examples for legacy language parsing, and diagram generation guidance.'
---

# Legacy System Flowchart Skill

## Overview

This skill supports drawing flowcharts from legacy IBM i / mainframe source code, especially RPG, COBOL, CL, and DB2-related artifacts. It emphasizes recovering control flow, decision points, I/O operations, and business process steps from legacy program text.

## Key Capabilities

### Legacy Source Analysis
- Parse RPG fixed-format and free-format programs to identify entry points, procedures, loops, conditionals, file access, and subroutine calls.
- Analyze COBOL `IDENTIFICATION`, `ENVIRONMENT`, `DATA`, and `PROCEDURE` divisions to recover program flow.
- Recognize CL job wrappers, call chains, and DB2 interactions that show the operational flow around RPG/COBOL programs.

### Flowchart Mapping
- Map legacy constructs to flowchart shapes: Start/End, Process, Decision, Input/Output, Subroutine/Call, and Database Access.
- Extract business workflow from batch jobs, screen/report logic, and DB2 file operations.
- Label nodes with meaningful legacy terms such as `READ`, `PERFORM`, `EXEC SQL`, `CHAIN`, `CALLP`, `DISPLAY`, and `WRITE`.

### Diagram Output
- Generate Mermaid flowchart syntax for text-based diagramming.
- Create PlantUML or Graphviz DOT descriptions when requested.
- Produce structured JSON/YAML representations of nodes and transitions for further tooling.

## Usage Examples

### Draw an RPG control-flow chart
- Analyze `apps/RPG/EMPCRUD.rpgle` and identify the main entry, CRUD branches, input validation, database access, and termination logic.
- Output a Mermaid diagram with nodes for `READ`, `INSERT`, `UPDATE`, `DELETE`, and SQL operations.
- Highlight decision splits, loop boundaries, and error handling flow.

### Diagram COBOL program workflow
- Analyze `apps/COBOL/hello.cob` or `apps/COBOL/FPANALYSIS.cob`.
- Extract `PERFORM`, `IF`, `EVALUATE`, `READ`, `WRITE`, and `DISPLAY` control flow.
- Provide an abstracted business flow diagram that is easy to follow for modernization planning.

### Example Prompt
```text
You are a legacy modernization analyst.
Analyze the following RPG or COBOL source and produce a flowchart of the program's control flow.
Return the diagram in Mermaid syntax and include a structured JSON flow model with node ids, labels, types, and transitions.

Source:
<legacy_source>
...
</legacy_source>

Requirements:
- Identify Start and End nodes.
- Map processes, decisions, inputs/outputs, and DB2/file operations.
- Preserve legacy labels such as `READ`, `PERFORM`, `EXEC SQL`, `CALLP`, and `WRITE`.
- Show branches explicitly with `-- yes -->` / `-- no -->` or equivalent.
- Provide a short summary of the extracted business flow.
```

## Best Practices

- Start with high-level flow and major decision points before refining details.
- Use source comments, paragraph names, and program titles to infer business intent.
- Keep diagrams stakeholder-appropriate: high-level for product owners, detailed for developers.
- Preserve legacy language terms in flow labels when the source is still under analysis.
- Use a structured intermediate representation before generating final diagram markup.

## Output Formats

- Mermaid flowchart syntax (`graph TD`, `subgraph`, `-->`, `-- yes -->`, `-- no -->`)
- PlantUML activity diagrams
- Graphviz DOT
- Structured JSON or YAML describing nodes and transitions

## Limitations

- This skill does not compile or execute legacy code.
- It relies on static source analysis and may not capture runtime dispatch or data-dependent branch behavior.
- Best used as a documentation and modernization aid, not a formal verification tool.
