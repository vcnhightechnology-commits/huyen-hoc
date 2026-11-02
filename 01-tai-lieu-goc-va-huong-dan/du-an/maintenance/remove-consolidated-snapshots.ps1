$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$taskPlanPath = Join-Path $taskRoot 'recovery/storage-consolidation/DELETION_PLAN.json'
$taskPlan = Get-Content -LiteralPath $taskPlanPath -Raw | ConvertFrom-Json
if ($taskPlan.status -ne 'ready-after-preservation-and-package-verification' -or $taskPlan.root.TrimEnd('\') -ne $taskRoot.TrimEnd('\')) { throw 'Invalid verified deletion plan' }
$taskArchiveRoot = [IO.Path]::GetFullPath((Join-Path $taskRoot 'archives'))
$taskRemoved = @()
foreach ($taskFile in $taskPlan.files) {
    $taskTarget = [IO.Path]::GetFullPath((Join-Path $taskRoot $taskFile.path))
    $taskIsArchive = $taskTarget.StartsWith($taskArchiveRoot + '\', [StringComparison]::OrdinalIgnoreCase)
    $taskIsLegacyRootZIP = ([IO.Path]::GetDirectoryName($taskTarget) -eq $taskRoot -and [IO.Path]::GetFileName($taskTarget) -like 'Huyen_Hoc_Cac_V*.zip' -and [IO.Path]::GetFileName($taskTarget) -notin $taskPlan.preserveRootFiles)
    $taskIsRetiredVersion = $false
    foreach ($taskVersion in $taskPlan.retiredFolders) {
        if ($taskVersion -notin @('v47','v48','v49','v50','v51','v52')) { throw 'Invalid retired version folder' }
        $taskVersionRoot = [IO.Path]::GetFullPath((Join-Path $taskRoot $taskVersion))
        if ($taskTarget.StartsWith($taskVersionRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { $taskIsRetiredVersion = $true }
    }
    if (-not ($taskIsArchive -or $taskIsLegacyRootZIP -or $taskIsRetiredVersion)) { throw "Outside bounded cleanup targets: $taskTarget" }
    if (-not (Test-Path -LiteralPath $taskTarget)) {
        # Resume the same verified plan safely after an interrupted cleanup.
        $taskRemoved += [PSCustomObject]@{ path = $taskFile.path; bytes = $taskFile.bytes; alreadyAbsent = $true }
        continue
    }
    $taskItem = Get-Item -LiteralPath $taskTarget -Force
    if ($taskItem.PSIsContainer -or $taskItem.Length -ne $taskFile.bytes -or ($taskItem.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw "File changed or reparse point: $taskTarget" }
    # Preservation collection already computed every source container SHA and every retained member SHA.
    Remove-Item -LiteralPath $taskTarget -Force
    $taskRemoved += [PSCustomObject]@{ path = $taskFile.path; bytes = $taskFile.bytes }
}
# Only remove empty directories, with every resolved target verified inside archives.
if (Test-Path -LiteralPath $taskArchiveRoot) {
    $taskDirs = @(Get-ChildItem -LiteralPath $taskArchiveRoot -Directory -Recurse -Force | Sort-Object { $_.FullName.Length } -Descending)
    foreach ($taskDir in $taskDirs) {
        $taskResolvedDir = [IO.Path]::GetFullPath($taskDir.FullName)
        if (-not $taskResolvedDir.StartsWith($taskArchiveRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Directory outside archives' }
        if (@(Get-ChildItem -LiteralPath $taskResolvedDir -Force).Count -eq 0) { Remove-Item -LiteralPath $taskResolvedDir -Force }
    }
    if (@(Get-ChildItem -LiteralPath $taskArchiveRoot -Force).Count -eq 0) { Remove-Item -LiteralPath $taskArchiveRoot -Force }
}
foreach ($taskVersion in $taskPlan.retiredFolders) {
    $taskVersionRoot = [IO.Path]::GetFullPath((Join-Path $taskRoot $taskVersion))
    if ([IO.Path]::GetDirectoryName($taskVersionRoot) -ne $taskRoot -or [IO.Path]::GetFileName($taskVersionRoot) -notin @('v47','v48','v49','v50','v51','v52')) { throw 'Version root outside authorized workspace' }
    if (-not (Test-Path -LiteralPath $taskVersionRoot)) { continue }
    $taskVersionDirs = @(Get-ChildItem -LiteralPath $taskVersionRoot -Directory -Recurse -Force | Sort-Object { $_.FullName.Length } -Descending)
    foreach ($taskDir in $taskVersionDirs) {
        $taskResolvedDir = [IO.Path]::GetFullPath($taskDir.FullName)
        if (-not $taskResolvedDir.StartsWith($taskVersionRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Directory outside retired version' }
        if (@(Get-ChildItem -LiteralPath $taskResolvedDir -Force).Count -eq 0) { Remove-Item -LiteralPath $taskResolvedDir -Force }
    }
    if (@(Get-ChildItem -LiteralPath $taskVersionRoot -Force).Count -eq 0) { Remove-Item -LiteralPath $taskVersionRoot -Force }
}
[PSCustomObject]@{ status = 'consolidated-snapshots-removed'; count = $taskRemoved.Count; files = $taskRemoved; chatHistoryUntouched = $true } | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $taskRoot 'recovery/storage-consolidation/REMOVED_SNAPSHOTS.json') -Encoding utf8
Write-Output "Removed $($taskRemoved.Count) consolidated snapshot/package files."
