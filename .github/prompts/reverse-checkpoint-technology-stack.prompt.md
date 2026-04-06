---
name: Checkpoint — Technology Stack
description: Validate technology-stack.md artifact quality and completeness.
---

# Checkpoint: technology-stack.md Validation

## Target File

`aidlc-docs/reverse-engineering/{repo-name}/technology-stack.md`

---

## Validation Checklist

### Section 1: Languages
- [ ] Section exists with heading "Languages"
- [ ] Lists all programming languages used
- [ ] Each language has a version specified (e.g., "C# 9.0", "TypeScript 4.9", "Dart 3.0")
- [ ] Scope of use is described (e.g., "backend", "frontend", "scripts")
- [ ] Minimum 1 language documented

### Section 2: Frameworks
- [ ] Section exists with heading "Frameworks"
- [ ] Lists all major frameworks
- [ ] Each framework has a version (e.g., "ASP.NET Core 5.0.1", "React 18.2.0")
- [ ] Purpose/scope is described for each framework
- [ ] Minimum 2 frameworks documented

### Section 3: Infrastructure
- [ ] Section exists with heading "Infrastructure"
- [ ] Lists all infrastructure services (database, cache, storage, message broker)
- [ ] Each service has: name, version/details, purpose
- [ ] Connection details noted (host, port) — without sensitive credentials
- [ ] Minimum 1 infrastructure service documented

### Section 4: Build Tools
- [ ] Section exists with heading "Build Tools"
- [ ] Lists build tool(s) with versions
- [ ] CI/CD pipeline tool mentioned (if found)
- [ ] Package manager noted (npm, yarn, NuGet, pub, etc.)

### Section 5: Testing Tools
- [ ] Section exists with heading "Testing Tools"
- [ ] Lists testing frameworks if found (xUnit, Jest, pytest, etc.)
- [ ] If NO tests found, explicitly states: "No test projects found"
- [ ] Coverage tools noted if present

---

## Version Accuracy Check

```
Verify versions against source files:
- .NET version: check global.json or .csproj TargetFramework
- npm packages: check package.json version fields
- NuGet packages: check .csproj PackageReference Version attributes
- Flutter: check pubspec.yaml sdk constraint
```

---

## Scoring

- **20-22 ✅**: PASS
- **15-19 ✅**: PARTIAL — Fix flagged items
- **< 15 ✅**: FAIL — Regenerate

---

## Fix Instructions

### If versions are missing:
```
Ask the agent to:
"Read global.json, .csproj files, package.json, or pubspec.yaml in {submodule-path}/
and add exact version numbers for all languages and frameworks in technology-stack.md."
```

### If Infrastructure section is incomplete:
```
Ask the agent to:
"Read appsettings.json, docker-compose.yml, and configuration files in {submodule-path}/
to identify all infrastructure services (databases, caches, queues, storage) and document them."
```

### If Testing Tools says nothing:
```
Ask the agent to:
"Search {submodule-path}/ for test projects, test files (*Test*.cs, *.spec.ts, *_test.dart),
and testing configuration files. Document what was found or explicitly state no tests exist."
```

---

## On Pass

Update `aidlc-docs/reverse-engineering-state.md`:
- Set `technology-stack.md` status = ✅ Validated

Proceed to: `reverse-checkpoint-dependencies.prompt.md`
