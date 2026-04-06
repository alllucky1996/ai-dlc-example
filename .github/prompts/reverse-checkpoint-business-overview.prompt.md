---
name: Checkpoint — Business Overview
description: Validate business-overview.md artifact quality and completeness.
---

# Checkpoint: business-overview.md Validation

## Target File

`aidlc-docs/reverse-engineering/{repo-name}/business-overview.md`

---

## Validation Checklist

Read the target file and verify each item:

### Section 1: Business Context Diagram
- [ ] Section exists with heading "Business Context Diagram"
- [ ] Contains a Mermaid code block (` ```mermaid `)
- [ ] Mermaid diagram type is `C4Context`, `graph TD`, or `flowchart`
- [ ] Diagram includes at least 2 actors/persons
- [ ] Diagram includes the target system
- [ ] Diagram includes at least 1 external system or relationship
- [ ] Mermaid syntax is valid (no unclosed brackets, valid node names)

### Section 2: Business Description
- [ ] Section exists with heading "Business Description"
- [ ] Describes WHAT the system does (not just technical details)
- [ ] Identifies WHO uses the system (user types)
- [ ] States the business VALUE or purpose
- [ ] Minimum 3 sentences of meaningful content

### Section 3: Business Transactions
- [ ] Section exists with heading "Business Transactions"
- [ ] Contains a table or list of business operations
- [ ] Minimum 5 business transactions listed
- [ ] Each transaction has a name and description
- [ ] Transactions are business-level (not technical CRUD operations)

### Section 4: Business Dictionary
- [ ] Section exists with heading "Business Dictionary"
- [ ] Contains a table or list of domain terms
- [ ] Minimum 8 terms defined
- [ ] Terms are domain-specific (not generic programming terms)
- [ ] Each term has a clear, business-oriented definition

---

## Scoring

Count checked items:
- **18-20 ✅**: PASS — Update state to "Validated"
- **14-17 ✅**: PARTIAL — Fix flagged items, re-run checkpoint
- **< 14 ✅**: FAIL — Regenerate artifact with agent

---

## Fix Instructions

### If Business Context Diagram is missing or invalid:
```
Ask the agent to:
"Read {submodule-path}/ and create a Business Context Diagram using Mermaid C4Context syntax.
Include: the system itself, all user types, and all external systems it integrates with."
```

### If Business Description is too technical:
```
Ask the agent to:
"Rewrite the Business Description section focusing on business value and user needs,
not technical implementation. Answer: What problem does this solve? Who benefits? How?"
```

### If Business Transactions are incomplete:
```
Ask the agent to:
"Review all Controllers and BS (Business Service) classes in {submodule-path}/ and
list all business operations as user-facing transactions (e.g., 'Patient books exam slot')."
```

### If Business Dictionary is missing terms:
```
Ask the agent to:
"Scan all entity names, enum values, and domain-specific variable names in {submodule-path}/
and add them to the Business Dictionary with business-oriented definitions."
```

---

## On Pass

Update `aidlc-docs/reverse-engineering-state.md`:
- Set `business-overview.md` status = ✅ Validated

Proceed to next checkpoint: `reverse-checkpoint-architecture.prompt.md`
