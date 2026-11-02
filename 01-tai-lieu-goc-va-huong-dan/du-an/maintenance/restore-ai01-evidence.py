"""Restore only byte-verified AI01 archive records; refuse differing existing files."""
from pathlib import Path, PurePosixPath
from hashlib import sha256
import argparse, io, json, zipfile

W=Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser(description=__doc__);p.add_argument('archive',type=Path);a=p.parse_args()
m=json.loads((W/'collaboration/imports/ai01-2026-10-31/IMPORT_VERIFICATION.json').read_text(encoding='utf-8'))
assert a.archive.stat().st_size==m['sourceArchiveBytes'] and sha256(a.archive.read_bytes()).hexdigest()==m['sourceArchiveSHA256']
planned=[]
with zipfile.ZipFile(a.archive) as outer:
 for r in m['files']:
  rel=PurePosixPath(r['file']);assert not rel.is_absolute() and '..' not in rel.parts and ':' not in r['file'] and '\\' not in r['file']
  dst=(W/r['file']).resolve();assert dst.is_relative_to(W/'collaboration')
  origin=r['origin']
  if '!' in origin:
   name,member=origin.split('!',1)
   with zipfile.ZipFile(io.BytesIO(outer.read(name))) as nested:data=nested.read(member)
  else:data=outer.read(origin)
  assert len(data)==r['bytes'] and sha256(data).hexdigest()==r['sha256']
  if dst.exists():assert dst.read_bytes()==data,'Existing file differs: '+r['file']
  else:planned.append((dst,data))
for dst,data in planned:
 dst.parent.mkdir(parents=True,exist_ok=True)
 with dst.open('xb') as out:out.write(data)
print(json.dumps({'verifiedRecords':len(m['files']),'restoredMissingFiles':len(planned),'originalZIPHashVerified':True}))
