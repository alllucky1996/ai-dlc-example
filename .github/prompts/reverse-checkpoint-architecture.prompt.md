---
name: Checkpoint — Architecture
description: Validate architecture.md artifact quality and completeness.
---

# Checkpoint: architecture.md Validation

## Target File

`aidlc-docs/reverse-engineering/{repo-name}/architecture.md`

---

## Validation Checklist

### Section 1: System Overview
- [ ] Section exists with heading "System Overview"
- [ ] Describes the overall system topology (layers, tiers)
- [ ] Identifies the architectural style (MVC, Layered, Microservice, etc.)
- [ ] Mentions deployment context (web app, API, SPA, etc.)
- [ ] Minimum 3 sentences of meaningful content

### Section 2: Architecture Diagram
- [ ] Section exists with heading "Architecture Diagram" or similar
- [ ] Contains at least ONE valid Mermaid diagram
- [ ] Diagram shows multiple components/layers
- [ ] Relationships between components are shown
- [ ] Mermaid syntax is valid (test: no unclosed `[`, `{`, `(` brackets)
- [ ] Diagram is readable (not more than 15 nodes without subgraphs)

### Section 3: Data Flow
- [ ] Section exists with heading "Data Flow"
- [ ] Describes how data moves through the system
- [ ] Includes at least one concrete example (e.g., "user submits form → controller → service → DB")
- [ ] Mentions key data transformations or processing steps
- [ ] May include a Mermaid `sequenceDiagram` (bonus)

### Section 4: Integration Points
- [ ] Section exists with heading "Integration Points"
- [ ] Lists all external systems the repo integrates with
- [ ] Each integration has: system name, protocol/method, purpose
- [ ] Includes database connections
- [ ] Includes any external APIs consumed or exposed

---

## Mermaid Syntax Quick Validation

Check for these common errors:
```
❌ Unclosed brackets: graph TD\n  A[Node without closing
❌ Invalid characters in node IDs: A[Node with "quotes"]
❌ Missing arrow type: A B (should be A --> B or A --- B)
❌ Subgraph without end: subgraph X\n  A --> B (missing 'end')
```

---

## Scoring

- **18-20 ✅**: PASS
- **14-17 ✅**: PARTIAL — Fix flagged items
- **< 14 ✅**: FAIL — Regenerate

---

## Fix Instructions

### If Architecture Diagram is missing:
```
Ask the agent to:
"Create an Architecture Diagram using Mermaid graph TD showing the layered structure of
{repo-name}. Include: Presentation layer, Business Logic layer, Data Access layer,
and Infrastructure (database, external services). Show dependencies between layers."
```

### If Mermaid syntax is invalid:
```
Ask the agent to:
"Fix the Mermaid syntax in architecture.md. Common issues to check:
- All subgraph blocks must end with 'end'
- Node IDs cannot contain spaces (use underscores or quotes)
- All brackets must be closed
- Arrow syntax: --> for directed, --- for undirected"
```

### If Integration Points are incomplete:
```
Ask the agent to:
"Read appsettings.json, Startup.cs/Program.cs, and package.json in {submodule-path}/
and list ALL external integrations: databases, APIs, message queues, storage services, email."
```

---

## On Pass

Update `aidlc-docs/reverse-engineering-state.md`:
- Set `architecture.md` status = ✅ Validated

Proceed to: `reverse-checkpoint-code-structure.prompt.md`
