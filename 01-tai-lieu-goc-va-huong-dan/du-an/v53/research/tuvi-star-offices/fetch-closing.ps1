$ErrorActionPreference = 'Stop'
$tuviBase = Join-Path (Get-Location) 'tmp/tuvi-full-volume-staging'
$tuviManifest = Get-Content -LiteralPath 'v53/research/fortune-followup/official-manifest.json' -Raw | ConvertFrom-Json
$tuviRecords = [System.Collections.Generic.List[object]]::new()
foreach($tuviN in 25..30) {
 $tuviURL=$tuviManifest.sequences[0].canvases[$tuviN-1].images[0].resource.'@id'.Replace('/full/max/','/full/2200,/')
 $tuviFile='canvas-{0:d3}-native-trust.jpg' -f $tuviN
 $tuviPath=Join-Path $tuviBase $tuviFile
 if(Test-Path -LiteralPath $tuviPath){throw 'Refusing to overwrite retained body'}
 try {
  $tuviResponse=Invoke-WebRequest -Uri $tuviURL -OutFile $tuviPath -PassThru -TimeoutSec 50
  $tuviHeaders=[ordered]@{}
  foreach($tuviKey in $tuviResponse.Headers.Keys){$tuviHeaders[$tuviKey]=[string]::Join(', ', $tuviResponse.Headers[$tuviKey])}
  $tuviRecords.Add([ordered]@{canvas=$tuviN;requestedURL=$tuviURL;file=$tuviFile;status=[int]$tuviResponse.StatusCode;bytes=(Get-Item -LiteralPath $tuviPath).Length;sha256=(Get-FileHash -LiteralPath $tuviPath -Algorithm SHA256).Hash.ToLower();TLSCertificateValidationEnabled=$true;responseHeadersRetained=$true;responseHeaders=$tuviHeaders;kind='Institution-served JPEG derivative, not original JP2';actuallyViewed=$false})
 } catch { $tuviRecords.Add([ordered]@{canvas=$tuviN;requestedURL=$tuviURL;error=$_.Exception.Message;TLSCertificateValidationEnabled=$true;bodySuccessEstablished=$false}) }
 [ordered]@{date='2026-10-28';transport='PowerShell Invoke-WebRequest with normal Windows certificate validation; no TLS bypass';records=$tuviRecords} | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $tuviBase 'WINDOWS_TRUST_REQUESTS_25_30.json') -Encoding utf8
}
$tuviRecords | ForEach-Object { [pscustomobject]$_ } | Select-Object canvas,status,bytes | ConvertTo-Json
