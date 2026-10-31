---
name: tkn-rules
description: Apply a named TKN-XXXX engineering convention to a requested design, implementation, SQL review, or rule-authoring task. Use when the request cites a TKN identifier; do not apply TKN rules to unrelated work.
---

# TKN Rules

The canonical TKN rule definitions live in `plugins/tkn-rules/rules/`.

1. Extract each `TKN-XXXX` identifier cited in the request.
2. Read `../../../plugins/tkn-rules/rules/<identifier>.md` before acting.
3. Apply each rule only within its stated scope and report the identifier and effect.
4. Do not invent an undefined rule; request its text or draft it as a proposal from `../../../plugins/tkn-rules/rules/rule-template.md`.

For DB2 SQL, act only on the target SQL fragment. Do not rewrite prose, comments, literals, other SQL dialects, or required syntax.
