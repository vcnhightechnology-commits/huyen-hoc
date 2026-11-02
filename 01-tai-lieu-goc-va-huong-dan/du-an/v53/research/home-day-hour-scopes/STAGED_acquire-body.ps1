param([string]$BodyName,[string]$SourceURL)
$ErrorActionPreference='Stop'
$taskDir=Join-Path (Get-Location) 'tmp/home-day-hour-staging'
if($BodyName -notmatch '^[a-zA-Z0-9_.-]+$'){throw 'Expected plain body filename.'}
$dest=Join-Path $taskDir $BodyName
if(Test-Path -LiteralPath $dest){throw 'Response already retained.'}
$records=@()
try{
 $response=Invoke-WebRequest -Uri $SourceURL -OutFile $dest -PassThru -TimeoutSec 60 -SkipHttpErrorCheck
 $row=@{file=$BodyName;url=$SourceURL;status=[int]$response.StatusCode;headers=$response.Headers;bytes=(Get-Item -LiteralPath $dest).Length;sha256=(Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash.ToLower();standardTLSValidation=$true;downloadedAt=[DateTime]::UtcNow.ToString('o')}
}catch{$row=@{requestedFile=$BodyName;url=$SourceURL;transportFailure=$_.Exception.Message;originalResponseBytesRetained=$false;standardTLSValidation=$true;observedAt=[DateTime]::UtcNow.ToString('o')}}
$records+=$row
$records | ConvertTo-Json -Depth 8 | Set-Content (Join-Path $taskDir ($BodyName+'.request.json')) -Encoding utf8
$row | Select-Object file,status,bytes,transportFailure | ConvertTo-Json
