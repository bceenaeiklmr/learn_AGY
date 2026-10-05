# Antigravity PostToolUse Hook: Post-Edit Checker
# Runs after file creation or modification.

$InputJson = [Console]::In.ReadToEnd()

# Expected output contract is an empty JSON object
"{}"
exit 0
