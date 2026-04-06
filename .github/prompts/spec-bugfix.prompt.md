# New Bugfix Spec

Start a Kiro bugfix spec workflow for the following bug:

**Bug:** {{Describe the bug — symptoms, error messages, reproduction steps}}

## Instructions

1. Derive a `kebab-case` bugfix name from the description above.
2. Create the directory `.kiro/specs/[bugfix-name]/`.
3. Generate `bugfix.md` (NOT `requirements.md`) with three behavior sections:
   - **Current Behavior (Defect)** — what is broken
   - **Expected Behavior (Correct)** — what should happen after the fix
   - **Unchanged Behavior (Regression Prevention)** — what must NOT change
4. Include the Bug Condition (C) and Postcondition (P).
5. After generating, ask: "Does the bugfix analysis look good? If so, we can move on to the fix design."
