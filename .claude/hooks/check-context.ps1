param()
$json = [System.Console]::In.ReadToEnd()
try { $data = $json | ConvertFrom-Json } catch { exit 0 }

$transcript = $data.transcript_path
if (-not $transcript -or -not (Test-Path $transcript)) { exit 0 }

$kb = [math]::Round((Get-Item $transcript).Length / 1KB)

# ~480KB ≈ 60% of 200k-token context (4 bytes/token + JSONL overhead)
if ($kb -gt 480) {
    Write-Error "BLOCKED: Context >60% (transcript ${kb}KB). Run /compact before continuing."
    exit 2
}
