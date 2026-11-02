"""Retain unique small mutable files before edits, without snapshotting full packages."""
from pathlib import Path
from hashlib import sha256,sha1
from datetime import datetime,timezone
import sqlite3,sys,os
W=Path(__file__).resolve().parent.parent;H=W/'recovery/consolidated-history';C=sqlite3.connect(H/'INDEX.sqlite')
C.execute('CREATE TABLE IF NOT EXISTS revisions(path TEXT NOT NULL,sha256 TEXT NOT NULL,recorded_utc TEXT NOT NULL,PRIMARY KEY(path,sha256))')
count=0
for name in sys.argv[1:]:
 p=(W/name).resolve();assert p.is_relative_to(W.resolve()) and p!=W.resolve() and not p.is_relative_to((W/'.git').resolve())
 assert not p.is_relative_to(H.resolve()),'Never recursively snapshot the consolidated index or object store.'
 assert p.is_file() and p.stat().st_size<32*1024*1024,'Use explicit evidence workflow for large binary sources.'
 b=p.read_bytes();d=sha256(b).hexdigest();g=sha1(('blob '+str(len(b))+'\0').encode()+b).hexdigest();location=H/'objects'/d[:2]/d;location.parent.mkdir(exist_ok=True)
 if not location.exists():
  temp=location.with_suffix('.pending');temp.write_bytes(b);assert sha256(temp.read_bytes()).hexdigest()==d;os.replace(temp,location)
 assert sha256(location.read_bytes()).hexdigest()==d
 known=C.execute('SELECT bytes,git_sha1 FROM content WHERE sha256=?',(d,)).fetchone()
 if known:assert known==(len(b),g);C.execute('UPDATE content SET path=? WHERE sha256=?',(location.relative_to(W).as_posix(),d))
 else:C.execute('INSERT INTO content VALUES(?,?,?,?,?)',(d,len(b),g,location.relative_to(W).as_posix(),'selected-mutable-revision'))
 C.execute('INSERT OR IGNORE INTO revisions VALUES(?,?,?)',(p.relative_to(W).as_posix(),d,datetime.now(timezone.utc).isoformat()));count+=1
C.commit();C.close();print(f'Preserved {count} selected prior files by SHA-256; no full ZIP copy.')
