param([string]$ListFile = 'TARGETED_REQUESTS.json', [string]$AuditFile = 'TARGETED_REQUEST_AUDIT.json')
$ErrorActionPreference = 'Stop'
$taskRoot = [System.IO.Path]::GetFullPath($PSScriptRoot)
$taskListPath = Join-Path $taskRoot $ListFile
$taskAuditPath = Join-Path $taskRoot $AuditFile
if (Test-Path -LiteralPath $taskAuditPath) { throw 'Existing request audit must not be overwritten.' }
$taskList = Get-Content -LiteralPath $taskListPath -Raw -Encoding utf8 | ConvertFrom-Json
$taskResults = @()
foreach ($taskRequest in $taskList) {
    $taskDestination = [System.IO.Path]::GetFullPath((Join-Path $taskRoot $taskRequest.file))
    if (-not $taskDestination.StartsWith($taskRoot + [System.IO.Path]::DirectorySeparatorChar)) { throw 'Target outside research staging.' }
    if (Test-Path -LiteralPath $taskDestination) { throw 'Existing response must not be overwritten.' }
    try {
        $taskResponse = Invoke-WebRequest -Uri $taskRequest.url -OutFile $taskDestination -PassThru -TimeoutSec 40 -MaximumRedirection 3
        $taskHeaders = @{}
        foreach ($taskKey in $taskResponse.Headers.Keys) { $taskHeaders[$taskKey] = [string]::Join(', ', $taskResponse.Headers[$taskKey]) }
        $taskResults += [ordered]@{url=$taskRequest.url; file=$taskRequest.file; kind=$taskRequest.kind; status=[int]$taskResponse.StatusCode; headers=$taskHeaders; bytes=(Get-Item -LiteralPath $taskDestination).Length; sha256=(Get-FileHash -LiteralPath $taskDestination -Algorithm SHA256).Hash.ToLowerInvariant(); acquiredUTC=[DateTime]::UtcNow.ToString('o'); TLSVerificationDisabled=$false}
    } catch {
        $taskResults += [ordered]@{url=$taskRequest.url;file=$taskRequest.file;kind=$taskRequest.kind;status='request-failed';error=$_.Exception.Message;acquiredUTC=[DateTime]::UtcNow.ToString('o');TLSVerificationDisabled=$false;retryPlanned=$false}
    }
}
ConvertTo-Json -InputObject @($taskResults) -Depth 8 | Set-Content -LiteralPath $taskAuditPath -Encoding utf8
foreach ($taskRecord in $taskResults) { [pscustomobject]$taskRecord | Select-Object file,status,bytes,sha256,error | ConvertTo-Json -Compress }
