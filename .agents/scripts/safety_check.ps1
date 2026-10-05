# Antigravity PreToolUse Hook: Safety Checker
# Inspects commands passed to run_command and blocks or asks for dangerous actions.

$InputJson = [Console]::In.ReadToEnd() | ConvertFrom-Json

$toolName = $InputJson.toolCall.name
$cmd = $InputJson.toolCall.args.CommandLine

# Check for dangerous patterns (e.g. disk format, recursive deletion of root, etc.)
if ($toolName -eq "run_command" -and $cmd) {
    if ($cmd -match "Format-Volume" -or $cmd -match "rmdir\s+/[sS]" -or $cmd -match "Remove-Item.*-Recurse\s+[C|c]:\\$") {
        $result = @{
            decision = "deny"
            reason   = "Blocked potentially destructive system command."
        }
        $result | ConvertTo-Json -Compress
        exit 0
    }
}

# Allow by default
@{ decision = "allow" } | ConvertTo-Json -Compress
exit 0
