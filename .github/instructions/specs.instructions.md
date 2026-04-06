---
applyTo: ".kiro/specs/**/*.md"
---

# Spec File Conventions

When working on files under `.kiro/specs/`:

## Common Conventions (All Spec Types)
- Maintain consistent terminology across all spec files within the same feature/bugfix directory.
- Design documents MUST include valid Mermaid diagrams where applicable.
- Task checkboxes use `- [ ]` (incomplete) and `- [x]` (complete) — standard GFM.
- Task hierarchy uses maximum two levels: `1`, `1.1`, `1.2`, `2`, `2.1`.
- Never delete or overwrite spec content without explicit user instruction.
- When updating one spec file, check if dependent files need corresponding updates.

## Feature Spec Conventions (requirements.md + design.md + tasks.md)
- Use requirement identifiers (R1, R1.1, R2, etc.) consistently for traceability.
- Acceptance criteria MUST use EARS notation: WHEN/THEN, WHILE, IF/THEN, WHERE.

## Bugfix Spec Conventions (bugfix.md + design.md + tasks.md)
- The first artifact is `bugfix.md`, NOT `requirements.md`.
- `bugfix.md` has three mandatory behavior sections:
  - **Current Behavior (Defect):** `WHEN ... THEN the system [broken behavior]`
  - **Expected Behavior (Correct):** `WHEN ... THEN the system SHALL [correct behavior]`
  - **Unchanged Behavior (Regression Prevention):** `WHEN ... THEN the system SHALL CONTINUE TO [preserved behavior]`
- Use section-numbered identifiers: 1.x = defect, 2.x = expected fix, 3.x = unchanged.
- `bugfix.md` is a pure requirements document — no formal specs, no code, no implementation details.
- Bug Condition (C), Postcondition (P), and formal pseudocode belong in `design.md`.
- `design.md` must include: root cause hypothesis with actual code, correctness properties, current vs proposed code, and test strategy with pseudocode.
- `tasks.md` must follow test-before-fix order:
  1. Bug condition tests (run against UNFIXED code — must FAIL)
  2. Preservation tests (run against UNFIXED code — must PASS)
  3. Apply fix
  4. Re-run ALL tests (must all PASS, no test modifications)
- Tasks use inline descriptions with bold Property references and italic `_Requirements: x.x_` traceability.
