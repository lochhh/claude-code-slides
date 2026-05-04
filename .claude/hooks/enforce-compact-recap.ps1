# Blocks non-Bash tools until compact recap flag is cleared.
$flagPath = Join-Path $PSScriptRoot ".compact-flag"
if (Test-Path $flagPath) {
    Write-Output "BLOCKED: Output state recap first, then run: Remove-Item .claude\hooks\.compact-flag"
    exit 2
}
exit 0
