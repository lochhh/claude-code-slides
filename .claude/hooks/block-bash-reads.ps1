# Blocks bash cat/head/tail — use Read tool instead.
if ($env:CC_TOOL_INPUT -match '"command"\s*:\s*"[^"]*\b(cat|head|tail)\b') {
    Write-Output "BLOCKED: Use the Read tool instead of bash cat/head/tail."
    exit 2
}
exit 0
