# TKN Rules integration

The canonical rule definitions are in `rules/`; the Codex skill consumes them automatically when a request cites a `TKN-XXXX` identifier.

## Codex

From a clone of this repository, register the repository marketplace and install the plugin:

```bash
codex plugin marketplace add /absolute/path/to/Batch/.agents/plugins
codex plugin add tkn-rules@batch
```

For another agent host, provide the host with `skills/tkn-rules/SKILL.md` and the `rules/` directory, preserving their relative paths. The host should load a rule only when the request explicitly cites its identifier. This avoids making a local convention a global instruction.

## Claude Code

This repository includes a bridge at `.claude/skills/tkn-rules/` that points to the canonical rule files. After cloning, Claude Code can use requests such as `Apply TKN-0001 to this DB2 query.`
