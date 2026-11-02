$ErrorActionPreference='Stop'
$stage=Join-Path (Get-Location) 'tmp/tuvi-lower-contiguous-staging'
$selection=Get-Content -LiteralPath (Join-Path $stage 'SELECTION_EXTENSION.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$records=@()
foreach($item in $selection.records){
 $destination=Join-Path $stage $item.file
 if(Test-Path -LiteralPath $destination){throw "Refuse duplicate acquisition: $($item.canvas)"}
 try{
  $response=Invoke-WebRequest -Uri $item.url -OutFile $destination -PassThru -TimeoutSec 45
  $records+=@{canvas=$item.canvas;url=$item.url;file=$item.file;status=[int]$response.StatusCode;bytes=(Get-Item -LiteralPath $destination).Length;sha256=(Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash.ToLowerInvariant();TLSCertificateValidationEnabled=$true;headers=$response.Headers}
 }catch{
  $records+=@{canvas=$item.canvas;url=$item.url;file=$item.file;status='failed';error=$_.Exception.Message;TLSCertificateValidationEnabled=$true}
 }
 ConvertTo-Json -InputObject @($records) -Depth 12 | Set-Content -LiteralPath (Join-Path $stage 'REQUESTS_EXTENSION.json') -Encoding UTF8
 Write-Output "canvas=$($item.canvas) status=$($records[-1].status)"
 if($records[-1].status -ne 200){break}
}
