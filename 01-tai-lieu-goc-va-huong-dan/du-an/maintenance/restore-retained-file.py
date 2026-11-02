"""Restore one logical historical member using the consolidated SHA-256 index."""
from pathlib import Path
from hashlib import sha256
import sqlite3,argparse,shutil,json

W=Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser();p.add_argument('--container');p.add_argument('--member');p.add_argument('--old-path');p.add_argument('--output',required=True);a=p.parse_args()
db=W/'recovery/consolidated-history/INDEX.sqlite';c=sqlite3.connect('file:'+db.as_posix()+'?mode=ro',uri=True)
if a.old_path:
 rows=c.execute('SELECT f.path,c.sha256,c.bytes,c.path FROM files f JOIN content c ON c.sha256=f.sha256 WHERE f.path=?',(a.old_path,)).fetchall()
else:
 if not a.container or not a.member:p.error('Use --container and --member, or --old-path')
 rows=c.execute('SELECT m.name,c.sha256,c.bytes,c.path FROM members m JOIN content c ON c.sha256=m.sha256 WHERE m.container=? AND m.name=?',(a.container,a.member)).fetchall()
assert len(rows)==1,'Missing/ambiguous member; inspect INDEX.sqlite first.'
name,digest,size,location=rows[0];src=W/location;dst=Path(a.output).resolve()
assert dst.is_relative_to(W.resolve())and dst!=W.resolve(),'Restore only inside this workspace.'
assert not dst.exists(),'Refusing to overwrite a file.'
dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
h=sha256()
with dst.open('rb')as f:
 for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
assert dst.stat().st_size==size and h.hexdigest()==digest
print(json.dumps({'restored':str(dst),'originalLogicalName':name,'sha256':digest,'bytes':size},ensure_ascii=False));c.close()
