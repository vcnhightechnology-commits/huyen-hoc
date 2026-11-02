$ErrorActionPreference = 'Stop'
$taskFolder = $PSScriptRoot
$taskURL = 'https://www.shidianguji.com/zh/book/SDZJ0170/chapter/1jvzooy7dkbhh'
$taskBody = Join-Path $taskFolder 'chapter-response.html'
$taskAudit = Join-Path $taskFolder 'HOST_REQUEST.json'
if ((Test-Path -LiteralPath $taskBody) -or (Test-Path -LiteralPath $taskAudit)) { throw 'Existing source attempt must not be overwritten.' }
try {
    $taskResponse = Invoke-WebRequest -Uri $taskURL -OutFile $taskBody -PassThru -TimeoutSec 40 -MaximumRedirection 3
    $taskHeaders = @{}
    foreach ($taskKey in $taskResponse.Headers.Keys) { $taskHeaders[$taskKey] = [string]::Join(', ', $taskResponse.Headers[$taskKey]) }
    $taskResult = [ordered]@{url=$taskURL; status=[int]$taskResponse.StatusCode; bytes=(Get-Item -LiteralPath $taskBody).Length; sha256=(Get-FileHash -LiteralPath $taskBody -Algorithm SHA256).Hash.ToLowerInvariant(); headers=$taskHeaders; TLSVerificationDisabled=$false; sourceFacsimileAcquired=$false; independentEditionEstablished=$false; acquiredUTC=[DateTime]::UtcNow.ToString('o')}
} catch {
    $taskResult = [ordered]@{url=$taskURL; status='host-request-failed'; error=$_.Exception.Message; TLSVerificationDisabled=$false; acquiredUTC=[DateTime]::UtcNow.ToString('o'); retryPlanned=$false}
}
$taskResult | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $taskAudit -Encoding utf8
$taskResult | Select-Object url,status,bytes,sha256,error | ConvertTo-Json -Compress
