---
name: Reverse Engineering Start
description: Khởi động reverse engineering cho một submodule. Tự động detect repo type và load agent phù hợp.
---

# Reverse Engineering — Start

## Intent

Bắt đầu reverse engineering cho một Git submodule. Prompt này sẽ:
1. Detect loại repo (Backend / Frontend / Mobile)
2. Load agent chuyên biệt tương ứng
3. Tạo thư mục artifact
4. Khởi tạo state tracking

---

## User Input Required

**Submodule path** (tên thư mục tại workspace root):
> Ví dụ: `health-support-web`, `mobile-app`, `admin-frontend`

**Output language** (optional, default: English):
- `en` — English
- `vi` — Tiếng Việt
- `ja` — 日本語

---

## Step 1: Detect Repo Type

Read the following files from `{submodule-path}/` to determine repo type:

```
Priority order:
1. Check for .csproj or .sln files → Backend .NET
2. Check for build.gradle + AndroidManifest.xml → Android Native
3. Check for Podfile + Info.plist (no package.json) → iOS Native
4. Check for pubspec.yaml → Flutter Mobile
5. Check package.json:
   - Has "react-native" or "expo" → React Native Mobile
   - Has "react", "@angular/core", or "vue" → Frontend Web
   - Has "electron" → Desktop (treat as Frontend)
6. If none of the above → Ask user to specify type manually
```

**Detection result**: Log detected type to `aidlc-docs/reverse-engineering-state.md`

---

## Step 2: Load Appropriate Agent

Based on detected type:

| Detected Type | Agent to Load |
|---|---|
| Backend .NET | `@reverse-backend` |
| Frontend Web (React/Angular/Vue) | `@reverse-frontend` |
| Mobile (React Native / Flutter / Android / iOS) | `@reverse-mobile` |
| Unknown | Ask user: "Could not auto-detect repo type. Please specify: Backend / Frontend / Mobile" |

---

## Step 3: Create Artifact Directory

Create the directory structure:
```
aidlc-docs/
└── reverse-engineering/
    └── {repo-name}/          ← Create this directory
        (9 artifact files will be generated here)
```

Where `{repo-name}` = the submodule folder name (e.g., `health-support-web`).

**⚠️ NEVER create files inside the submodule directory itself.**

---

## Step 4: Initialize State Tracking

Update `aidlc-docs/reverse-engineering-state.md`:
- Find the row for `{submodule-path}` in the Execution Phase Progress table
- Set **Status** = `In Progress`
- Set **Started** = today's date (ISO format: YYYY-MM-DD)
- Set **Artifacts** = `0/9`

If the submodule is not yet in the table, add a new row:
```
| {submodule-path} | {repo-name} | {detected-type} | - | In Progress | 0/9 | {today} | - |
```

Also update `aidlc-docs/reverse-engineering-coordination/team-assignments.md` if it exists:
- Set Status = `In Progress` for this submodule

---

## Step 5: Invoke Agent

Hand off to the selected agent with this context:

```
Target repo: {submodule-path}
Repo name: {repo-name}
Artifact directory: aidlc-docs/reverse-engineering/{repo-name}/
Output language: {selected-language}
State file: aidlc-docs/reverse-engineering-state.md

Please generate all 9 artifacts for this repository.
```

---

## Notes

- If `aidlc-docs/reverse-engineering/{repo-name}/` already contains artifacts, ask user:
  "Artifacts already exist for `{repo-name}`. Do you want to: (A) Overwrite all, (B) Regenerate missing only, (C) Cancel?"
- Always read `.gitmodules` to validate the submodule path exists before proceeding
- Log all actions to `aidlc-docs/reverse-engineering-state.md`
