param()
$json = [System.Console]::In.ReadToEnd()
try { $data = $json | ConvertFrom-Json } catch { exit 0 }

$filePath = $data.tool_input.file_path
if (-not $filePath) { exit 0 }

$name = [System.IO.Path]::GetFileName($filePath).ToLower()
$path = $filePath.ToLower() -replace '\\', '/'

$namePatterns = @(
    '^\.env$',
    '^\.env\.',
    '^secrets?\.',
    '^credentials?\.',
    '\.pem$',
    '^id_rsa',
    '^id_ed25519',
    '^id_dsa',
    '^id_ecdsa',
    '\.key$',
    '\.p12$',
    '\.pfx$',
    '\.gpg$',
    'private.?key'
)

$pathPatterns = @(
    '/\.ssh/'
)

$blocked = $false
foreach ($p in $namePatterns) { if ($name -match $p) { $blocked = $true; break } }
foreach ($p in $pathPatterns) { if ($path -match $p) { $blocked = $true; break } }

if ($blocked) {
    Write-Error "BLOCKED: Write to sensitive file '$($data.tool_input.file_path)'. Edit secrets manually outside Claude."
    exit 2
}
