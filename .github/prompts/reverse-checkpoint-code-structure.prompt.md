---
name: Checkpoint — Code Structure
description: Validate code-structure.md artifact quality and completeness.
---

# Checkpoint: code-structure.md Validation

## Target File

`aidlc-docs/reverse-engineering/{repo-name}/code-structure.md`

---

## Validation Checklist

### Section 1: Build System
- [ ] Section exists with heading "Build System"
- [ ] Identifies the build tool (dotnet CLI, Maven, Gradle, npm/yarn, etc.)
- [ ] Lists the main project/solution file
- [ ] Mentions SDK or runtime version
- [ ] Notes any CI/CD pipeline files found

### Section 2: Key Classes/Components Diagram
- [ ] Section exists with a diagram
- [ ] Contains a valid Mermaid diagram (`classDiagram`, `graph TD`, or `flowchart`)
- [ ] Shows at least 5 key classes/components
- [ ] Shows relationships between classes (inheritance, composition, dependency)
- [ ] Mermaid syntax is valid

### Section 3: Files Inventory
- [ ] Section exists with heading "Files Inventory" or "Project Structure"
- [ ] Lists all top-level directories with their purpose
- [ ] Minimum 5 directories documented
- [ ] Each directory has a clear purpose description
- [ ] Includes both source and config directories

### Section 4: Design Patterns
- [ ] Section exists with heading "Design Patterns"
- [ ] Lists at least 3 design patterns identified
- [ ] Each pattern has: name, where it's used, brief description
- [ ] Patterns are specific to this codebase (not generic)
- [ ] Includes both good patterns and any anti-patterns noted

---

## Completeness Check

Cross-reference with actual directory structure:
```
Ask the agent to:
"List all top-level directories in {submodule-path}/ and verify each one is documented
in the Files Inventory section of code-structure.md. Add any missing directories."
```

---

## Scoring

- **18-20 ✅**: PASS
- **14-17 ✅**: PARTIAL — Fix flagged items
- **< 14 ✅**: FAIL — Regenerate

---

## Fix Instructions

### If Key Classes Diagram is missing or too sparse:
```
Ask the agent to:
"Create a Mermaid classDiagram showing the key classes in {repo-name}.
Include: the main Controller/Handler classes, Service/BS classes, Repository classes,
and key Entity/Model classes. Show inheritance and dependency relationships."
```

### If Files Inventory is incomplete:
```
Ask the agent to:
"List every directory in {submodule-path}/ recursively to depth 2 and document
each directory's purpose in the Files Inventory section."
```

### If Design Patterns section is generic:
```
Ask the agent to:
"Review the actual code in {submodule-path}/ and identify specific design patterns
with concrete examples. For each pattern, cite the specific class or file where it's used."
```

---

## On Pass

Update `aidlc-docs/reverse-engineering-state.md`:
- Set `code-structure.md` status = ✅ Validated

Proceed to: `reverse-checkpoint-api-documentation.prompt.md`
