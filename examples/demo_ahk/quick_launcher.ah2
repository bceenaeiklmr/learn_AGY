#Requires AutoHotkey v2.0+
#SingleInstance Force

; ==============================================================================
; Quick Launcher - Demo AutoHotkey v2 Script
; Built following Antigravity workspace rules & safety best practices.
; ==============================================================================

; --- Emergency Kill Switch & Quick Reload ---
; Ctrl + Esc: Terminate the script immediately
^Esc::ExitApp()

; Ctrl + Shift + R: Reload the script when editing
^+r::Reload()


; --- Helper GUI Launcher ---
; Win + Space: Open quick launcher windowű
#Space::
{
    static launcherGui := ""

    if (launcherGui != "") {
        launcherGui.Destroy()
    }

    launcherGui := Gui("+AlwaysOnTop -MaximizeBox", "Agy Quick Launcher")
    launcherGui.SetFont("s10", "Segoe UI")

    launcherGui.Add("Text", "w260", "Type an action or shortcut:")
    inputBox := launcherGui.Add("Edit", "w260 vAction")

    btnRun := launcherGui.Add("Button", "w120 default", "Execute")
    btnRun.OnEvent("Click", (*) => HandleAction(inputBox.Value, launcherGui))

    btnCancel := launcherGui.Add("Button", "x+10 w120", "Cancel")
    btnCancel.OnEvent("Click", (*) => launcherGui.Destroy())

    launcherGui.Show()
}


HandleAction(actionText, guiObj)
{
    guiObj.Destroy()
    trimmed := Trim(actionText)

    if (trimmed = "") {
        return
    }

    switch StrLower(trimmed) {
        case "notepad", "note":
            Run("notepad.exe")
        case "calc":
            Run("calc.exe")
        case "cmd", "terminal":
            Run("wt.exe", , "Hide", &err)
        default:
            MsgBox("Action executed: " . trimmed, "Agy Launcher", 64)
    }
}
