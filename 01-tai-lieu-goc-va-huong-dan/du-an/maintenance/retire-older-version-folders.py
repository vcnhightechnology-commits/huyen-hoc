"""Move unique older working-copy bytes into the content-addressed history, before removal."""
from pathlib import Path
from hashlib import sha256
import sqlite3,json,shutil
W=Path(__file__).resolve().parent.parent;R=W/'recovery/storage-consolidation';H=W/'recovery/consolidated-history';retired={'v47','v48','v49','v50','v51','v52'}
c=sqlite3.connect(H/'INDEX.sqlite');moved=0;aliased=0;deletions=[]
for digest,size,git,location,kind in c.execute('SELECT * FROM content').fetchall():
 if Path(location).parts[0]not in retired:continue
 src=W/location;assert src.stat().st_size==size and sha256(src.read_bytes()).hexdigest()==digest
 alternatives=c.execute('SELECT path FROM files WHERE sha256=?',(digest,)).fetchall();replacement=None
 for (name,)in alternatives:
  if Path(name).parts[0]in retired or Path(name).parts[0]=='archives':continue
  p=W/name
  if p.is_file()and p.stat().st_size==size and sha256(p.read_bytes()).hexdigest()==digest:replacement=name;break
 if replacement is None:
  dst=H/'objects'/digest[:2]/digest;dst.parent.mkdir(exist_ok=True)
  if not dst.exists():shutil.copy2(src,dst)
  assert sha256(dst.read_bytes()).hexdigest()==digest;replacement=dst.relative_to(W).as_posix();moved+=1
 else:aliased+=1
 c.execute('UPDATE content SET path=? WHERE sha256=?',(replacement,digest))
for folder in sorted(retired):
 for p in sorted((W/folder).rglob('*')):
  if not p.is_file():continue
  name=p.relative_to(W).as_posix();row=c.execute('SELECT sha256,bytes FROM files WHERE path=?',(name,)).fetchone();assert row and row[1]==p.stat().st_size,name
  assert sha256(p.read_bytes()).hexdigest()==row[0],name
  deletions.append({'path':name,'bytes':row[1],'sha256':row[0],'reason':'Retired version unique bytes consolidated by SHA; active latest version is v53.'})
c.commit();c.close()
out={'status':'older-version-bytes-preserved-ready-for-removal','retiredFolders':sorted(retired),'files':deletions,'bytes':sum(x['bytes']for x in deletions),'uniqueContentRelocated':moved,'contentAliasedToRetainedWorkingFiles':aliased,'keptV46DependencyTree':True,'filesDeleted':0}
(R/'RETIRED_VERSION_PLAN.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items()if k!='files'}))
