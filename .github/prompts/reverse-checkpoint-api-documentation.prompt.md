---
name: Checkpoint — API Documentation
description: Validate api-documentation.md artifact quality and completeness.
---

# Checkpoint: api-documentation.md Validation

## Target File

`aidlc-docs/reverse-engineering/{repo-name}/api-documentation.md`

---

## Validation Checklist

### Section 1: REST APIs (if applicable)
- [ ] Section exists (or explicitly states "No REST APIs — internal service only")
- [ ] Contains a table with columns: Method | Route/URL | Description
- [ ] Minimum 5 endpoints documented (if repo has controllers/routes)
- [ ] HTTP methods are specified (GET, POST, PUT, DELETE, PATCH)
- [ ] Routes are accurate (cross-check with actual controller files)
- [ ] Authentication requirements noted per endpoint or globally

### Section 2: Internal APIs / Service Interfaces
- [ ] Section exists with heading "Internal APIs" or "Service Interfaces"
- [ ] Lists key service interfaces or internal contracts
- [ ] Each interface has a name and purpose description
- [ ] Minimum 5 interfaces documented

### Section 3: Data Models
- [ ] Section exists with heading "Data Models" or "Request/Response Models"
- [ ] Documents at least 3 key request/response models
- [ ] Each model shows field names and types
- [ ] Includes both input (request) and output (response) models

### Section 4: Request/Response Formats
- [ ] Section exists
- [ ] Documents content types (JSON, XML, multipart, etc.)
- [ ] Notes authentication mechanism (Cookie, JWT, API Key)
- [ ] Documents error response format
- [ ] Notes any special headers required

---

## Accuracy Check

Verify API documentation against actual code:
```
For Backend repos:
- Count controllers in {submodule-path}/Controllers/ directory
- Verify documented endpoint count is reasonable (at least 50% coverage)
- Check that route prefixes match controller names

For Frontend/Mobile repos:
- Check API client files for actual endpoint URLs
- Verify base URL is documented
```

---

## Scoring

- **18-20 ✅**: PASS
- **14-17 ✅**: PARTIAL — Fix flagged items
- **< 14 ✅**: FAIL — Regenerate

---

## Fix Instructions

### If REST API table is incomplete:
```
Ask the agent to:
"Read all Controller files in {submodule-path}/Controllers/ and list every public
action method with its HTTP method, route, and purpose. Create a complete API table."
```

### If Data Models are missing:
```
Ask the agent to:
"Read the Models/ and ViewModels/ directories in {submodule-path}/ and document
the key request/response DTOs. Include field names, types, and validation rules."
```

### If authentication is not documented:
```
Ask the agent to:
"Read Startup.cs/Program.cs and the Filters/ directory in {submodule-path}/ to
document the authentication and authorization mechanism used for API endpoints."
```

---

## On Pass

Update `aidlc-docs/reverse-engineering-state.md`:
- Set `api-documentation.md` status = ✅ Validated

Proceed to: `reverse-checkpoint-component-inventory.prompt.md`
