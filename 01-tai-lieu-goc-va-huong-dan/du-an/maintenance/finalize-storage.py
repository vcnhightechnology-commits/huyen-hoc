"""Record measured completion only after verified cleanup and preservation."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone, timedelta
import json, os, shutil, subprocess, sys

W=Path(__file__).resolve().parent.parent
R=W/'recovery/storage-consolidation'
def read(name):return json.loads((R/name).read_text(encoding='utf-8-sig'))
assert read('REMOVED_SNAPSHOTS.json')['status']=='consolidated-snapshots-removed'
assert read('PRUNED_GIT_CHECKPOINTS.json')['status']=='preserved-checkpoint-objects-pruned'
assert read('CURRENT_VERIFICATION.json')['status']=='current-product-and-retained-history-verified'
assert read('COLLECTION_STATE.json')['status']=='all-retained-content-sha256-verified'
plan=read('DELETION_PLAN.json')
assert all(not (W/x['path']).exists() for x in plan['files'])
assert not (W/'archives').exists()
assert {p.name for p in W.glob('*.zip')}=={'Huyen_Hoc_Cac_V53_source.zip','Huyen_Hoc_Cac_V53_web.zip'}
restore=W/'tmp/storage-final-restore-test.json'
assert not restore.exists()
subprocess.run([sys.executable,str(W/'maintenance/restore-retained-file.py'),
 '--container','archives/v53-before-bazi-branch-union/Huyen_Hoc_Cac_V53_source.zip',
 '--member','v53/research/full-study/WORK_STATE.json','--output',str(restore)],check=True)
assert sha256(restore.read_bytes()).hexdigest()=='f361caefcfdc27864ba27c2dc059a35ade7585003bd41f134852bff7971c0f14'
restore.unlink()
sizes={};count=0
for root,dirs,files in os.walk(W):
 for name in files:
  p=Path(root)/name;rel=p.relative_to(W);key=rel.parts[0] if len(rel.parts)>1 else '[root files]'
  sizes[key]=sizes.get(key,0)+p.stat().st_size;count+=1
before=json.loads((W/'recovery/storage-audit-2026-10-29/LATEST_SIZE_RECHECK.json').read_text(encoding='utf-8-sig'))
total=sum(sizes.values());package=W/'Huyen_Hoc_Cac_V53_source.zip';digest=sha256()
with package.open('rb') as f:
 for b in iter(lambda:f.read(8*1024*1024),b''):digest.update(b)
out={'status':'complete','completedAt':datetime.now(timezone(timedelta(hours=7))).isoformat(),
 'beforeLogicalBytes':before['projectLogicalBytes'],'afterLogicalBytes':total,
 'netLogicalBytesReduced':before['projectLogicalBytes']-total,'afterFileCount':count,
 'topLevelBytes':sizes,'diskFreeBytes':shutil.disk_usage(W).free,
 'latestSourceZIPBytes':package.stat().st_size,'latestSourceZIPSHA256':digest.hexdigest(),
 'rootReleasePackages':['Huyen_Hoc_Cac_V53_source.zip','Huyen_Hoc_Cac_V53_web.zip'],
 'oldSnapshotFilesRemoved':len(plan['files']),'historicalRestoreAfterDeletionPassed':True,
 'chatHistoryUntouched':True,'uniqueSourceEvidencePreserved':True,
 'historyIndex':'recovery/consolidated-history/INDEX.sqlite',
 'verification':'recovery/storage-consolidation/CURRENT_VERIFICATION.json',
 'keptV46Reason':'Live engine dependencies referenced by current research tools.',
 'measurementNote':'Logical file sizes; before audit precedes consolidation, after precedes this small completion record.'}
(R/'COMPLETION_RESULT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
gate=read('MAINTENANCE.json');gate.update(status='complete',completedAt=out['completedAt'],researchBlockedUntilMaintenanceComplete=False,completionResult='recovery/storage-consolidation/COMPLETION_RESULT.json')
(R/'MAINTENANCE.json').write_text(json.dumps(gate,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False),flush=True)
