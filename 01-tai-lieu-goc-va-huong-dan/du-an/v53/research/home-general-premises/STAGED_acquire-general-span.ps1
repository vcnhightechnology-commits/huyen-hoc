param([int]$NextCount=9)
$ErrorActionPreference='Stop'
$taskDir=Join-Path (Get-Location) 'tmp/home-calendar-premises-staging'
$node=Get-Content (Join-Path $taskDir 'itkc-general-image-node.json') -Raw | ConvertFrom-Json
for($step=0;$step -le $NextCount;$step++){
 $path=[string]$node.imginfo.imgPath
 if($path -notmatch '^/data/imagedb/BOOK/ITKC_BT/ITKC_BT_1508A/ITKC_BT_1508A_V002_(25[7-9]|26[0-6])\.JPG$'){throw 'Unexpected observed general-theory span path.'}
 $name=Split-Path -Leaf $path
 & (Join-Path $taskDir 'acquire-body.ps1') -BodyName $name -SourceURL ('https://db.itkc.or.kr'+$path)
 if($step -eq $NextCount){break}
 $idx=[int]$node.imginfo.imgNext
 $name='itkc-general-image-index-'+$idx+'.json'
 $dest=Join-Path $taskDir $name
 if(Test-Path -LiteralPath $dest){throw 'Already retained navigation body.'}
 $url='https://db.itkc.or.kr/imgviewer/imgnavi';$body=@{seojiId='ITKC_GO_1508A';imgIdx=[string]$idx}
 $response=Invoke-WebRequest -Uri $url -Method Post -Body $body -OutFile $dest -PassThru -TimeoutSec 60 -SkipHttpErrorCheck
 $records=@(Get-Content (Join-Path $taskDir 'REQUESTS.json') -Raw | ConvertFrom-Json)
 $records+=@{file=$name;url=$url;method='POST';readOnlyImageNavigation=$true;requestBody=$body;status=[int]$response.StatusCode;headers=$response.Headers;bytes=(Get-Item -LiteralPath $dest).Length;sha256=(Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash.ToLower();standardTLSValidation=$true;downloadedAt=[DateTime]::UtcNow.ToString('o')}
 $records | ConvertTo-Json -Depth 8 | Set-Content (Join-Path $taskDir 'REQUESTS.json') -Encoding utf8
 $node=Get-Content -LiteralPath $dest -Raw | ConvertFrom-Json
}
