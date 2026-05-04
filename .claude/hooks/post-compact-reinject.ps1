# Fires on SessionStart(compact). Reinjects context-essentials and enforces recap.
$flagPath = Join-Path $PSScriptRoot ".compact-flag"
"1" | Set-Content $flagPath

$essentials = Get-Content (Join-Path $PSScriptRoot "..\context-essentials.md") -Raw

Write-Output @"
COMPACTION DETECTED. You MUST do the following before anything else:

1. Output a state recap covering: current phase, what is done, what is next.
2. Then run: Remove-Item .claude\hooks\.compact-flag (via Bash) to unblock tool use.

--- REINJECTED CONTEXT ---
$essentials
--- END REINJECTED CONTEXT ---
"@
exit 0
