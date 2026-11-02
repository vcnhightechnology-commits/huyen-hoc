"""Create a bounded deletion plan after verified preservation and package creation."""
from pathlib import Path
from hashlib import sha256
import sqlite3,json
W=Path(__file__).resolve().parent.parent;R=W/'recovery/storage-consolidation'
state=json.loads((R/'COLLECTION_STATE.json').read_text(encoding='utf-8-sig'));assert state['status']=='all-retained-content-sha256-verified'
package=json.loads((R/'LATEST_PACKAGE_MANIFEST.json').read_text(encoding='utf-8-sig'));assert package['status']=='latest-source-package-member-sha256-verified'
z=W/'Huyen_Hoc_Cac_V53_source.zip';assert z.stat().st_size==package['sourceZIPBytes']
c=sqlite3.connect('file:'+(W/'recovery/consolidated-history/INDEX.sqlite').as_posix()+'?mode=ro',uri=True)
deletions=[]
for p in sorted((W/'archives').rglob('*')):
 if not p.is_file():continue
 path=p.relative_to(W).as_posix();size=p.stat().st_size
 if p.suffix=='.zip':
  row=c.execute('SELECT bytes,sha256,status FROM containers WHERE path=?',(path,)).fetchone();assert row and row[0]==size and row[2]=='verified',path
  assert c.execute('SELECT count(*)FROM members m LEFT JOIN content c ON c.sha256=m.sha256 WHERE m.container=? AND c.sha256 IS NULL',(path,)).fetchone()[0]==0
  digest=row[1]
 else:
  row=c.execute('SELECT sha256,bytes FROM files WHERE path=?',(path,)).fetchone();assert row and row[1]==size,path
  digest=sha256(p.read_bytes()).hexdigest();assert digest==row[0],path
 deletions.append({'path':path,'bytes':size,'sha256':digest,'reason':'All unique member/file bytes retained by consolidated-history index.'})
keep={'Huyen_Hoc_Cac_V53_source.zip','Huyen_Hoc_Cac_V53_web.zip'}
for p in sorted(W.glob('Huyen_Hoc_Cac_V*.zip')):
 if p.name in keep:continue
 row=c.execute('SELECT bytes,sha256,status FROM containers WHERE path=?',(p.name,)).fetchone();assert row and row[0]==p.stat().st_size and row[2]=='verified'
 deletions.append({'path':p.name,'bytes':row[0],'sha256':row[1],'reason':'Legacy generated package contents merged into one latest source package.'})
expected={x['file']for x in package['files']}
retired=json.loads((R/'RETIRED_VERSION_PLAN.json').read_text(encoding='utf-8-sig'))
assert retired['status']=='older-version-bytes-preserved-ready-for-removal'
deletions.extend(retired['files'])
assert 'recovery/consolidated-history/INDEX.sqlite'in expected
for digest,path in c.execute('SELECT sha256,path FROM content'):
 assert path in expected,path
 assert (W/path).is_file(),path
c.close()
out={'status':'ready-after-preservation-and-package-verification','root':str(W.resolve()),'files':deletions,'deleteFileCount':len(deletions),'deleteBytes':sum(x['bytes']for x in deletions),'preserveRootFiles':sorted(keep),'retiredFolders':retired['retiredFolders'],'chatHistoryUntouched':True,'gitPruneIsSeparate':True}
(R/'DELETION_PLAN.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'ready':True,'files':len(deletions),'archiveAndOldPackageGiB':out['deleteBytes']/1024**3}))
