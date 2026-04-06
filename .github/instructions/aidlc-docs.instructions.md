---
applyTo: "aidlc-docs/**/*.md,.aidlc-rule-details/**/*.md"
---

# AI-DLC Document Conventions

When working on files under `aidlc-docs/` or reading `.aidlc-rule-details/`:

- `aidlc-docs/aidlc-state.md` is the single source of truth for workflow progress. Always read it before taking action.
- `aidlc-docs/audit.md` is append-only. Never delete or modify existing entries.
- Questions for the user are written in dedicated markdown files under `aidlc-docs/`, not in chat.
- All questions must be multiple-choice with an "Other (please describe)" option.
- Mark completed steps with checkboxes `[x]` in plan documents.
- Mermaid diagrams are used for workflow visualization, architecture, and sequence flows.
- Stage-level rule files in `.aidlc-rule-details/` are read-only reference material — never modify them.
- The `extensions/` folder contains opt-in rule sets (e.g., security baseline). Present opt-in prompts during Inception.
