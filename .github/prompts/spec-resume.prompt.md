# Resume Spec Workflow

Resume work on an existing spec:

**Feature directory:** `.kiro/specs/{{feature-name}}/`

## Instructions

1. Read all existing spec files in the feature directory.
2. Determine the spec type and current phase:
   **Feature specs** (contains `requirements.md`):
   - If only `requirements.md` exists → offer to proceed to design (with user approval).
   - If `requirements.md` + `design.md` exist → offer to proceed to tasks (with user approval).
   - If all three files exist → show next unchecked task and offer to execute it.
   **Bugfix specs** (contains `bugfix.md`):
   - If only `bugfix.md` exists → offer to proceed to fix design (with user approval).
   - If `bugfix.md` + `design.md` exist → offer to proceed to tasks (with user approval).
   - If all three files exist → show next unchecked task and offer to execute it.
3. Present a status summary and ask the user what they'd like to do.
