---
name: Checkpoint — Dependencies
description: Validate dependencies.md artifact quality and completeness.
---

# Checkpoint: dependencies.md Validation

## Target File

`aidlc-docs/reverse-engineering/{repo-name}/dependencies.md`

---

## Validation Checklist

### Section 1: Internal Dependencies Diagram
- [ ] Section exists with heading "Internal Dependencies"
- [ ] Contains a valid Mermaid diagram (`graph LR`, `graph TD`, or `flowchart`)
- [ ] Shows all internal project-to-project references
- [ ] Arrow direction is correct (dependent → dependency)
- [ ] Mermaid syntax is valid
- [ ] Minimum 2 nodes in diagram (or states "Single project — no internal dependencies")

### Section 2: External Dependencies
- [ ] Section exists with heading "External Dependencies"
- [ ] Lists all external services (databases, APIs, storage, email, etc.)
- [ ] Each dependency has: name, type, purpose
- [ ] Distinguishes between runtime dependencies and build-time dependencies
- [ ] Minimum 3 external dependencies (or all if fewer)

### Section 3: Dependency Types
- [ ] Dependency types are specified (direct vs. transitive, runtime vs. dev)
- [ ] Critical dependencies are highlighted
- [ ] Optional vs. required dependencies noted where relevant

### Section 4: Reasons for Dependencies
- [ ] Each significant dependency has a reason for inclusion
- [ ] Reasons are specific to this project (not generic)
- [ ] Any redundant or questionable dependencies are flagged

---

## Completeness Check

```
For .NET repos:
- Read all .csproj files for <ProjectReference> (internal) and <PackageReference> (external)
- Verify internal dependency diagram matches actual project references

For Node.js repos:
- Check package.json imports in key files to verify dependency usage
- Verify all significant packages are in the external dependencies list

Cross-check with component-inventory.md:
- All packages in component-inventory.md should appear in dependencies.md
```

---

## Scoring

- **16-18 ✅**: PASS
- **12-15 ✅**: PARTIAL — Fix flagged items
- **< 12 ✅**: FAIL — Regenerate

---

## Fix Instructions

### If Internal Dependencies Diagram is missing:
```
Ask the agent to:
"Read all .csproj files in {submodule-path}/ and create a Mermaid graph LR diagram
showing project-to-project references. Each node = one project, arrows = dependencies."
```

### If External Dependencies are incomplete:
```
Ask the agent to:
"List all external services referenced in configuration files, connection strings,
and API client code in {submodule-path}/. Include: databases, external APIs,
storage services, email providers, authentication services."
```

### If reasons are missing:
```
Ask the agent to:
"For each external dependency in dependencies.md, add a 'Reason' column explaining
WHY this dependency is needed in {repo-name} specifically."
```

---

## On Pass

Update `aidlc-docs/reverse-engineering-state.md`:
- Set `dependencies.md` status = ✅ Validated

Proceed to: `reverse-checkpoint-code-quality.prompt.md`
