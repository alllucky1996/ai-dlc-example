---
name: Ecosystem Integration
description: Tích hợp artifacts của một repo vào ecosystem-level view. Cập nhật dependency graph, integration registry, và progress dashboard.
---

# Ecosystem Integration

## Intent

Sau khi hoàn thành reverse engineering một repo, prompt này tích hợp kết quả vào ecosystem-level view để xây dựng bức tranh toàn cảnh của hệ thống.

---

## User Input Required

**Repo name** (tên thư mục artifact):
> Ví dụ: `health-support-web`

---

## Step 1: Load Repo Artifacts

Read the following files from `aidlc-docs/reverse-engineering/{repo-name}/`:
- `api-documentation.md` — extract APIs exposed and consumed
- `dependencies.md` — extract external service dependencies
- `technology-stack.md` — extract infrastructure components
- `architecture.md` — extract integration points

---

## Step 2: Extract Integration Data

From the artifacts, extract:

### APIs Exposed (for Backend repos)
```
From api-documentation.md → REST APIs section:
- Endpoint URL pattern
- HTTP method
- Authentication required
- Purpose
```

### APIs Consumed (for Frontend/Mobile repos)
```
From api-documentation.md → APIs Consumed section:
- Base URL
- Endpoint patterns
- Authentication method
```

### Shared Infrastructure
```
From technology-stack.md → Infrastructure section:
- Database name and type
- Cache service
- Message broker
- Storage service
```

### External Integrations
```
From dependencies.md → External Dependencies:
- Third-party APIs
- Authentication providers
- Email/notification services
```

---

## Step 3: Update Ecosystem Architecture

Create or update `aidlc-docs/reverse-engineering/ecosystem/ecosystem-architecture.md`:

### If file does NOT exist — create it:
```markdown
# Ecosystem Architecture

## System Context Diagram

[Generate C4Context Mermaid diagram with all known repos]

## Inter-Repo Dependency Graph

[Generate graph LR with {repo-name} as first node]

## Integration Points Summary

| Repo | Type | APIs Exposed | APIs Consumed | Database | External Services |
|------|------|-------------|---------------|----------|-------------------|
| {repo-name} | Backend/Frontend/Mobile | [count] | [count] | [db-name] | [list] |

## Ecosystem Metrics

- Total repos analyzed: 1
- Total API endpoints mapped: [count]
- Shared infrastructure components: [count]
```

### If file EXISTS — update it:
1. Add `{repo-name}` to the System Context Diagram
2. Add `{repo-name}` node and its connections to the Dependency Graph
3. Add a new row to the Integration Points Summary table
4. Update Ecosystem Metrics counts

---

## Step 4: Update Integration Registry

Update `aidlc-docs/reverse-engineering-coordination/integration-registry.md`:

### API Integrations Table
Add rows for each API endpoint discovered:
```
| {endpoint} | {repo-name} | [consumer repos if known] | {method} | {auth} | Discovered |
```

### Shared Databases Table
Add rows for each database found:
```
| {db-name} | {db-type} | {repo-name} | [other repos if known] | [other repos if known] | - |
```

### Shared Libraries Table
Add rows for significant shared packages:
```
| {package-name} | {version} | {repo-name} | {purpose} | NuGet/npm |
```

---

## Step 5: Update Progress Dashboard

Update `aidlc-docs/reverse-engineering-coordination/progress-dashboard.md`:
- Increment "Repositories Completed" count
- Update "Artifacts Generated" count (+9)
- Update "API integrations discovered" count
- Update "Last Updated" timestamp

---

## Step 6: Update State File

Update `aidlc-docs/reverse-engineering-state.md`:
- Set `{repo-name}` status = `Ecosystem Integrated`
- Set Completed date = today

Also update `aidlc-docs/reverse-engineering-coordination/team-assignments.md`:
- Set Status = `Completed` for this repo
- Set Completed date = today

---

## Completion Message

```
✅ Ecosystem integration complete for [{repo-name}].

Files updated:
- aidlc-docs/reverse-engineering/ecosystem/ecosystem-architecture.md
- aidlc-docs/reverse-engineering-coordination/integration-registry.md
- aidlc-docs/reverse-engineering-coordination/progress-dashboard.md
- aidlc-docs/reverse-engineering-state.md

Summary:
- APIs mapped: [count]
- Infrastructure components: [count]
- Cross-repo connections identified: [count]

Next steps:
- Assign next repo from team-assignments.md
- Run reverse-start.prompt.md for next repo
```
