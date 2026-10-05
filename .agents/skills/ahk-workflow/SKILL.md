---
name: ahk-workflow
description: >-
  Use this skill when the user asks to write, debug, test, or refactor AutoHotkey (AHK v2) scripts, desktop shortcuts, hotkeys, or Windows GUI automation.
---

# AutoHotkey v2 Automation Workflow

This skill guides the creation, testing, and validation of AutoHotkey v2 scripts.

## Step-by-Step Procedure

1. **Verify Target Version**:
   - Ensure all output adheres strictly to AutoHotkey v2. If the user provides v1 code, migrate it to v2 syntax using [references/syntax.md](./references/syntax.md).

2. **Template Requirements**:
   - Always include the `#Requires AutoHotkey v2.0+` directive.
   - Always include `#SingleInstance Force`.
   - Always include an emergency kill switch (`^Esc::ExitApp()`).

3. **Syntax Validation**:
   - If AutoHotkey is installed on the user's system, run a syntax verification check without executing:
     ```powershell
     & "AutoHotkey.exe" /validate "path\to\script.ahk"
     ```
   - Check exit code for syntax errors.

4. **Safety & Execution**:
   - Before launching an active keyboard or mouse hook script, alert the user about any key intercepts.
   - Recommend testing in an isolated window context (using `#HotIf WinActive(...)`) rather than global shortcuts.
