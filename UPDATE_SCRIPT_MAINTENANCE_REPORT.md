## Update Script Maintenance Report

Date: 2026-03-04

- Root cause: script fetched Unicode source over HTTP and workflow had no explicit write permission.
- Fixes made: switched script fetch to HTTPS with timeout/status checks, removed duplicate fetch, updated workflow trigger model, and added `permissions: contents: write`.
- Validation: ran updater locally and confirmed expected output paths (`archive/source.csv`, `data/unicode-characters.csv`).
- Known blockers: none identified in this remediation pass.
