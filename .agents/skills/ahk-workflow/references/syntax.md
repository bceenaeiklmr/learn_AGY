# AutoHotkey v2 Key Syntax & Quick Reference

## Core Differences from AHK v1

1. **Expressions Everywhere**:
   - In AHK v2, all parameters are expressions.
   - Strings must be quoted: `Title := "Notepad"`
   - Function calls must use parentheses: `WinActivate("ahk_exe notepad.exe")`

2. **Hotkeys and Hotstrings**:
   ```ahk
   #SingleInstance Force

   ; Win + N launches Notepad
   #n::
   {
       Run("notepad.exe")
   }

   ; Hotstring with auto-replace
   ::btw::by the way
   ```

3. **GUI Creation in v2**:
   ```ahk
   myGui := Gui("+AlwaysOnTop", "Quick Launcher")
   myGui.Add("Text", "w200", "Enter command:")
   cmdEdit := myGui.Add("Edit", "w200 vCommand")
   btnOk := myGui.Add("Button", "default", "Run")
   btnOk.OnEvent("Click", (*) => MsgBox("Executed: " cmdEdit.Value))
   myGui.Show()
   ```

4. **Window Management**:
   ```ahk
   SetTitleMatchMode(2) ; 2 = contains match

   if WinExist("Visual Studio Code") {
       WinActivate()
   } else {
       Run("code")
   }
   ```

5. **Safe Script Template**:
   ```ahk
   #Requires AutoHotkey v2.0+
   #SingleInstance Force

   ; Emergency stop: Ctrl + Esc
   ^Esc::ExitApp()

   ; Reload script: Ctrl + Shift + R
   ^+r::Reload()
   ```
