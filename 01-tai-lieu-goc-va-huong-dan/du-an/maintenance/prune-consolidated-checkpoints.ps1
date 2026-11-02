$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$taskGitRoot = [IO.Path]::GetFullPath((Join-Path $taskRoot '.git'))
if ([IO.Path]::GetDirectoryName($taskGitRoot) -ne $taskRoot -or [IO.Path]::GetFileName($taskGitRoot) -ne '.git') { throw 'Git target outside intended project' }
$taskReady = Get-Content -LiteralPath (Join-Path $taskRoot 'recovery/storage-consolidation/GIT_PRUNE_READY.json') -Raw | ConvertFrom-Json
if ($taskReady.status -ne 'all-current-loose-git-objects-preserved-before-prune' -or $taskReady.missingObjects -ne 0) { throw 'Git preservation certificate missing' }
$taskPackage = Get-Content -LiteralPath (Join-Path $taskRoot 'recovery/storage-consolidation/LATEST_PACKAGE_MANIFEST.json') -Raw | ConvertFrom-Json
if ($taskPackage.status -ne 'latest-source-package-member-sha256-verified') { throw 'Consolidated package not verified' }
& git -c "safe.directory=$taskRoot" --no-optional-locks rev-parse --verify --quiet HEAD
if ($LASTEXITCODE -eq 0) { throw 'Repository now has normal commits; reassess before deleting any history' }
$taskRefs = @(& git -c "safe.directory=$taskRoot" --no-optional-locks for-each-ref --format='%(refname) %(objectname)')
if ($LASTEXITCODE -ne 0) { throw 'Could not enumerate refs' }
foreach ($taskRef in $taskRefs) {
    $taskRefParts = $taskRef.Split(' ')
    if ($taskRefParts.Count -ne 2 -or -not $taskRefParts[0].StartsWith('refs/codex/turn-diffs/checkpoints/')) { throw "Unexpected user ref: $taskRef" }
    $taskObjectType = & git -c "safe.directory=$taskRoot" --no-optional-locks cat-file -t $taskRefParts[1]
    if ($LASTEXITCODE -ne 0 -or $taskObjectType -ne 'tree') { throw "Unexpected ref target: $taskRef" }
}
$taskActiveGit = @(Get-CimInstance Win32_Process -Filter "Name = 'git.exe'")
if ($taskActiveGit.Count -gt 0) { throw 'Git processes are active; verify their project directories and stop project writers before pruning' }
foreach ($taskRef in $taskRefs) {
    $taskRefParts = $taskRef.Split(' ')
    & git -c "safe.directory=$taskRoot" update-ref -d $taskRefParts[0] $taskRefParts[1]
    if ($LASTEXITCODE -ne 0) { throw "Failed to remove preserved checkpoint ref: $taskRef" }
}
# Every source blob or archived-container payload has been consolidated first.
# No normal user commit/branch existed. Prune only this repository's now-unreachable objects.
& git -c "safe.directory=$taskRoot" -c core.hooksPath=NUL prune --expire=now
if ($LASTEXITCODE -ne 0) { throw 'Git prune did not complete' }
$taskAfter = @(& git -c "safe.directory=$taskRoot" --no-optional-locks count-objects -v 2>&1)
[PSCustomObject]@{ status='preserved-checkpoint-objects-pruned'; removedCheckpointRefs=$taskRefs.Count; after=$taskAfter; chatHistoryUntouched=$true; normalUserCommitsRemoved=0 } | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $taskRoot 'recovery/storage-consolidation/PRUNED_GIT_CHECKPOINTS.json') -Encoding utf8
$taskAfter
