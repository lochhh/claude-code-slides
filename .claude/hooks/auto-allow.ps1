param()
$json = [System.Console]::In.ReadToEnd()
try { $data = $json | ConvertFrom-Json } catch { exit 0 }

$tool = $data.tool_name

# Read-only Claude tools — always safe
$safeTools = @('Read', 'Glob', 'Grep', 'LS', 'WebSearch', 'WebFetch', 'TodoRead')
if ($safeTools -contains $tool) {
    Write-Output '{"permissionDecision": "allow"}'
    exit 0
}

# Bash — auto-allow known read-only commands with no output redirection
if ($tool -eq 'Bash') {
    $cmd = $data.tool_input.command
    if (-not $cmd) { exit 0 }

    # Reject if command writes to files
    if ($cmd -match '>\s*\S') { exit 0 }

    $safePatterns = @(
        '^ls\b', '^cat\b', '^head\b', '^tail\b', '^wc\b',
        '^echo\b', '^pwd\b', '^which\b', '^file\b', '^stat\b',
        '^du\b', '^df\b', '^grep\b', '^rg\b', '^find\b',
        '^git (status|log|diff|show|branch|remote|describe)\b',
        '^type\b'
    )

    $cmdTrimmed = $cmd.Trim()
    foreach ($p in $safePatterns) {
        if ($cmdTrimmed -match $p) {
            Write-Output '{"permissionDecision": "allow"}'
            exit 0
        }
    }
}
