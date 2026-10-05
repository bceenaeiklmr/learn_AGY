# Workspace Rules: Python & AutoHotkey Development

These rules apply to all files and workflows in this workspace.

---

## 1. General Principles
- **Surgical edits**: Only touch lines directly related to the user's objective. Do not reformat unrelated code.
- **Explain trade-offs**: If a requested change introduces complexity, suggest the simpler approach first.
- **Verify before declaring done**: Always test or run syntax verification before concluding a task.

---

## 2. Python Standards
- **Runtime**: Python 3.10+ compatible code.
- **Typing**: Use standard type hints (`typing` or built-in generics like `list[str]`, `dict[str, Any]`, `tuple`, `Optional`).
- **Formatting & Style**: PEP 8 compliant, 4-space indentation, descriptive function and variable names.
- **Testing**: Use `pytest` for all unit testing. Prefer writing unit tests in `test_<module>.py`.
- **Environment**: Check for virtual environment (`.venv` or `venv`) before installing dependencies or executing scripts.

---

## 3. AutoHotkey (AHK) Standards
- **Version**: Strictly **AutoHotkey v2** syntax (`.ahk` or `.ah2`). Never output AHK v1 code.
  - Variables must not use `%var%` syntax for assignment (use `var := value`).
  - Function calls require parentheses (e.g. `MsgBox("Hello")`, not `MsgBox, Hello`).
  - Commands are functions in v2 (e.g. `SendInput("{Enter}")`).
- **Safety & Reload**:
  - Always provide a safe emergency escape hotkey in automation scripts (e.g. `^Esc::ExitApp()`).
  - Use `#SingleInstance Force` at the top of executable scripts to prevent duplicate tray instances.
- **Reliability**:
  - Use `SetTitleMatchMode(2)` for partial window title matching where appropriate.
  - Avoid arbitrary `Sleep` where event-driven waits (like `WinWaitActive`) are possible.
