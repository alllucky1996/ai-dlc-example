---
name: Checkpoint — Component Inventory
description: Validate component-inventory.md artifact quality and completeness.
---

# Checkpoint: component-inventory.md Validation

## Target File

`aidlc-docs/reverse-engineering/{repo-name}/component-inventory.md`

---

## Validation Checklist

### Section 1: Package Categorization
- [ ] Section exists with packages organized into categories
- [ ] Categories are meaningful (e.g., Core, Infrastructure, Testing, UI, Utility)
- [ ] Each package has: name, version, purpose description
- [ ] Minimum 10 packages documented (or all packages if fewer than 10)
- [ ] No packages listed without a purpose description

### Section 2: Total Count
- [ ] Total package count is stated explicitly
- [ ] Count matches the number of packages listed
- [ ] Cross-check: count matches entries in `package.json` / `.csproj` / `pubspec.yaml`

### Section 3: Purpose Clarity
- [ ] Each package has a one-line purpose description
- [ ] Descriptions are specific (not just "utility library")
- [ ] Critical packages have more detailed descriptions
- [ ] Deprecated or unused packages are flagged

### Section 4: Internal Projects (if applicable)
- [ ] Internal project references are listed separately
- [ ] Each internal project has a purpose description
- [ ] Dependency direction is noted (which project depends on which)

---

## Completeness Check

```
For .NET repos:
- Read all .csproj files and count <PackageReference> entries
- Verify documented count matches actual count

For Node.js repos:
- Read package.json dependencies + devDependencies
- Verify all significant packages are documented

For Flutter repos:
- Read pubspec.yaml dependencies
- Verify all packages are documented
```

---

## Scoring

- **14-16 ✅**: PASS
- **10-13 ✅**: PARTIAL — Fix flagged items
- **< 10 ✅**: FAIL — Regenerate

---

## Fix Instructions

### If packages are missing:
```
Ask the agent to:
"Read all dependency files in {submodule-path}/ (.csproj, package.json, pubspec.yaml)
and create a complete inventory of ALL packages with their versions and purposes."
```

### If purpose descriptions are too generic:
```
Ask the agent to:
"For each package in component-inventory.md, provide a specific description of HOW
it is used in {repo-name}, not just what the package does in general."
```

### If categorization is missing:
```
Ask the agent to:
"Organize the packages in component-inventory.md into logical categories:
Core Framework, Database/ORM, Authentication, Logging, Testing, UI/Frontend, Utilities."
```

---

## On Pass

Update `aidlc-docs/reverse-engineering-state.md`:
- Set `component-inventory.md` status = ✅ Validated

Proceed to: `reverse-checkpoint-technology-stack.prompt.md`
