from pathlib import Path
import sqlite3,json
W=Path(__file__).resolve().parent.parent;R=W/'recovery/storage-consolidation'
s=json.loads((R/'COLLECTION_STATE.json').read_text(encoding='utf-8-sig'));assert s['status']=='all-retained-content-sha256-verified'
c=sqlite3.connect('file:'+(W/'recovery/consolidated-history/INDEX.sqlite').as_posix()+'?mode=ro',uri=True)
oids=[]
for d in(W/'.git/objects').iterdir():
 if not d.is_dir()or len(d.name)!=2:continue
 for p in d.iterdir():
  if p.is_file()and len(p.name)==38:oids.append(d.name+p.name)
missing=[oid for oid in oids if not c.execute('SELECT 1 FROM git_objects WHERE oid=?',(oid,)).fetchone()]
assert not missing,('New objects require collection before pruning',missing[:5])
assert c.execute('SELECT count(*)FROM git_objects WHERE status NOT IN (?,?,?,?)',('content-retained','container-members-consolidated','unique-content-retained','metadata-retained')).fetchone()[0]==0
c.close();out={'status':'all-current-loose-git-objects-preserved-before-prune','looseObjectCount':len(oids),'missingObjects':0,'chatHistoryUntouched':True};(R/'GIT_PRUNE_READY.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
