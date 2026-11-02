$ErrorActionPreference='Stop'
$taskDir=Join-Path (Get-Location) 'tmp/home-day-hour-staging'
foreach($job in @(@{kind='day';node='itkc-day-image-node-pwsh.json';last=253},@{kind='hour';node='itkc-hour-image-node.json';last=256})){
 $node=Get-Content -LiteralPath (Join-Path $taskDir $job.node) -Raw | ConvertFrom-Json
 while($true){
  $path=[string]$node.imginfo.imgPath
  if($path -notmatch '^/data/imagedb/BOOK/ITKC_BT/ITKC_BT_1508A/ITKC_BT_1508A_V002_(24[7-9]|25[0-3]|25[5-6])\.JPG$'){throw 'Outside observed day/hour image range.'}
  $num=[int]$Matches[1];$name=Split-Path -Leaf $path
  if($num -ne 247){& (Join-Path $taskDir 'acquire-body.ps1') -BodyName $name -SourceURL ('https://db.itkc.or.kr'+$path)}
  if($num -eq $job.last){break}
  $idx=[string]$node.imginfo.imgNext;$name='itkc-'+$job.kind+'-image-index-'+$idx+'.json';$dest=Join-Path $taskDir $name
  if(Test-Path -LiteralPath $dest){throw 'Navigation already retained.'}
  $url='https://db.itkc.or.kr/imgviewer/imgnavi';$body=@{seojiId='ITKC_GO_1508A';imgIdx=$idx}
  $response=Invoke-WebRequest -Uri $url -Method Post -Body $body -OutFile $dest -PassThru -TimeoutSec 60 -SkipHttpErrorCheck
  $row=@{file=$name;url=$url;method='POST';readOnlyImageNavigation=$true;requestBody=$body;status=[int]$response.StatusCode;headers=$response.Headers;bytes=(Get-Item -LiteralPath $dest).Length;sha256=(Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash.ToLower();standardTLSValidation=$true;downloadedAt=[DateTime]::UtcNow.ToString('o')}
  $row | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath (Join-Path $taskDir ($name+'.request.json')) -Encoding utf8
  if([int]$response.StatusCode -ne 200){throw 'Retained non200 navigation; stop without retry.'}
  $node=Get-Content -LiteralPath $dest -Raw | ConvertFrom-Json
 }
}
