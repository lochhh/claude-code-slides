param()
$json = [System.Console]::In.ReadToEnd()
try { $data = $json | ConvertFrom-Json } catch { exit 0 }

$filePath = $data.tool_input.file_path
if (-not $filePath) { exit 0 }

$filePath = $filePath -replace '\\', '/'

if ($filePath -match 'README\.md$') {
    Write-Output "README.md was modified. Run /sync-workflows to update any affected workflows/ files."
}

exit 0
