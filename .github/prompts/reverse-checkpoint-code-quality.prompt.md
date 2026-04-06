---
name: Checkpoint — Code Quality Assessment
description: Validate code-quality-assessment.md artifact quality and objectivity.
---

# Checkpoint: code-quality-assessment.md Validation

## Target File

`aidlc-docs/reverse-engineering/{repo-name}/code-quality-assessment.md`

---

## Validation Checklist

### Section 1: Test Coverage
- [ ] Section exists with heading "Test Coverage"
- [ ] States number of test projects found (or "0 — no tests found")
- [ ] Estimates test count or states "unknown"
- [ ] Names testing frameworks used (or states none)
- [ ] Notes coverage tooling if present
- [ ] Risk level is stated if no tests exist

### Section 2: Code Quality Indicators
- [ ] Section exists with heading "Code Quality Indicators"
- [ ] Lists positive quality indicators with specific examples
- [ ] Lists areas needing improvement with specific examples
- [ ] References actual files or patterns (not generic statements)
- [ ] Minimum 3 positive indicators and 3 improvement areas

### Section 3: Technical Debt
- [ ] Section exists with heading "Technical Debt"
- [ ] Lists specific technical debt items
- [ ] Each item has: type, description, severity (High/Medium/Low)
- [ ] Minimum 3 technical debt items identified
- [ ] Items are evidence-based (cite specific files or patterns)

### Section 4: Patterns / Anti-patterns
- [ ] Section exists with heading "Patterns" or "Design Patterns"
- [ ] Lists good patterns observed with where they're used
- [ ] Lists anti-patterns with where they occur
- [ ] Minimum 3 patterns and 2 anti-patterns documented
- [ ] Anti-patterns are described constructively (not just criticism)

---

## Objectivity Check

Verify the assessment is evidence-based:
```
Each claim should be verifiable:
✅ "ExamResultController has 1776 lines — violates Single Responsibility"
✅ "No test projects found in solution"
✅ "appsettings.json contains hardcoded DB password"
❌ "Code quality is poor" (too vague)
❌ "Tests are insufficient" (no evidence)
❌ "Architecture is good" (no specifics)
```

---

## Scoring

- **18-20 ✅**: PASS
- **14-17 ✅**: PARTIAL — Fix flagged items
- **< 14 ✅**: FAIL — Regenerate

---

## Fix Instructions

### If Test Coverage section is vague:
```
Ask the agent to:
"Search {submodule-path}/ for files matching patterns: *Test*.cs, *.spec.ts, *_test.dart,
*Tests/ directories. Count test files and test methods. Report exact numbers."
```

### If Technical Debt items lack evidence:
```
Ask the agent to:
"For each technical debt item in code-quality-assessment.md, add a specific file path
or code example as evidence. Search for TODO/FIXME comments, deprecated API usage,
and files over 500 lines."
```

### If Anti-patterns are missing:
```
Ask the agent to:
"Review the largest files in {submodule-path}/ (by line count) and identify specific
anti-patterns: God Objects (classes with too many responsibilities), Magic Numbers,
hardcoded configuration, missing error handling."
```

---

## On Pass

Update `aidlc-docs/reverse-engineering-state.md`:
- Set `code-quality-assessment.md` status = ✅ Validated

All 9 checkpoints complete → Run: `reverse-ecosystem-integrate.prompt.md`
