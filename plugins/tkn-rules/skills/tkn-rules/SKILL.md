---
name: tkn-rules
description: Apply a named TKN-XXXX engineering convention to a requested design, implementation, SQL review, or rule-authoring task. Use when the request cites a TKN identifier; do not apply TKN rules to unrelated work.
---

# TKN Rules

TKN rules are versioned, local engineering conventions. A request that cites one or more `TKN-XXXX` identifiers opts into those rules for that request only.

## Apply a rule

1. Extract every cited TKN identifier from the request.
2. Read its definition from `../../rules/<identifier>.md` before designing, editing, or reviewing.
3. State the rule identifier and the concrete effect in the response or change summary.
4. Apply the rule only within its stated scope. Preserve user requirements and valid product constraints.
5. If a cited identifier has no definition, do not invent it. Ask for the rule text or propose a draft labelled as a proposal.

## SQL rule requests

When a rule applies to SQL, distinguish the target dialect and the SQL fragment from prose, comments, examples for another database, or ORM configuration. Do not rewrite unrelated dialects.

For a change request, update affected code and add or update a focused validation when the repository has an appropriate test location. For a review-only request, report compliant and non-compliant occurrences without making edits.

## Add a rule

Create `rules/TKN-XXXX.md` using the fields in [rule-template.md](../../rules/rule-template.md). A new rule must have a narrow scope, a rationale, concrete compliant/non-compliant examples, explicit exceptions, and a verification method. Avoid rules that merely restate general coding advice.

## Available rules

- `TKN-0001`: avoid optional `AS` in DB2 SQL.
