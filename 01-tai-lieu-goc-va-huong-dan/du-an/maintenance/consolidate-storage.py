"""Preserve unique bytes before deleting generated snapshots. No deletion in collect."""
from pathlib import Path
from hashlib import sha256,sha1
from datetime import datetime,timezone,timedelta
import os,json,sqlite3,zipfile,struct,zlib,sys,time

W=Path(__file__).resolve().parent.parent
R=W/'recovery/storage-consolidation';R.mkdir(exist_ok=True)
H=W/'recovery/consolidated-history';H.mkdir(exist_ok=True)
OBJ=H/'objects';OBJ.mkdir(exist_ok=True)
DB=H/'INDEX.sqlite';C=sqlite3.connect(DB)
C.executescript('''
CREATE TABLE IF NOT EXISTS content(sha256 TEXT PRIMARY KEY,bytes INTEGER NOT NULL,git_sha1 TEXT UNIQUE NOT NULL,path TEXT NOT NULL,kind TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS files(path TEXT PRIMARY KEY,sha256 TEXT NOT NULL,bytes INTEGER NOT NULL,mtime_ns INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS containers(path TEXT PRIMARY KEY,bytes INTEGER NOT NULL,sha256 TEXT NOT NULL,git_sha1 TEXT NOT NULL,entries INTEGER NOT NULL,status TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS members(container TEXT NOT NULL,ordinal INTEGER NOT NULL,name TEXT NOT NULL,sha256 TEXT NOT NULL,bytes INTEGER NOT NULL,crc INTEGER NOT NULL,compressed_sha256 TEXT NOT NULL,PRIMARY KEY(container,ordinal));
CREATE TABLE IF NOT EXISTS representations(method INTEGER NOT NULL,bytes INTEGER NOT NULL,crc INTEGER NOT NULL,compressed_sha256 TEXT NOT NULL,sha256 TEXT NOT NULL,PRIMARY KEY(method,bytes,crc,compressed_sha256));
CREATE TABLE IF NOT EXISTS git_objects(oid TEXT PRIMARY KEY,type TEXT NOT NULL,bytes INTEGER NOT NULL,sha256 TEXT,status TEXT NOT NULL);
''')
BATCH=8*1024*1024
def log(**d):print(json.dumps(d,ensure_ascii=False),flush=True)
def rel(p):return p.relative_to(W).as_posix()
def safe(p):
 p=p.resolve();assert p.is_relative_to(W.resolve())and p!=W.resolve();return p
def content_info(sha):return C.execute('SELECT path,bytes,git_sha1 FROM content WHERE sha256=?',(sha,)).fetchone()
def consume(stream,size,kind,live=None):
 h=sha256();g=sha1(('blob '+str(size)+'\0').encode());n=0
 temp=H/'incoming-content.tmp'
 out=None if live is not None else temp.open('wb')
 try:
  while True:
   b=stream.read(BATCH)
   if not b:break
   h.update(b);g.update(b);n+=len(b)
   if out:out.write(b)
 finally:
  if out:out.close()
 assert n==size,(kind,n,size)
 digest=h.hexdigest();git=g.hexdigest();known=content_info(digest)
 if known:
  assert known[1]==n and known[2]==git
  if temp.exists()and live is None:temp.unlink()
  return digest,git
 if live is None:
  target=OBJ/digest[:2]/digest;target.parent.mkdir(exist_ok=True);os.replace(temp,target);location=rel(target)
 else:location=rel(live)
 C.execute('INSERT INTO content VALUES(?,?,?,?,?)',(digest,n,git,location,kind))
 return digest,git

def index_live():
 n=0;total=0
 stack=[W]
 while stack:
  directory=stack.pop()
  for e in os.scandir(directory):
   p=Path(e.path);relative=p.relative_to(W);parts=relative.parts
   if parts[0]in['.git','archives']:continue
   if p==H or p==R:continue
   if len(parts)==1 and p.suffix=='.zip':continue
   st=e.stat(follow_symlinks=False)
   if getattr(st,'st_file_attributes',0)&0x400:continue
   if e.is_dir(follow_symlinks=False):stack.append(p);continue
   if not e.is_file(follow_symlinks=False):continue
   old=C.execute('SELECT sha256,bytes,mtime_ns FROM files WHERE path=?',(rel(p),)).fetchone()
   if old and old[1:]==(st.st_size,st.st_mtime_ns):continue
   with p.open('rb')as f:digest,git=consume(f,st.st_size,'live',p)
   C.execute('INSERT OR REPLACE INTO files VALUES(?,?,?,?)',(rel(p),digest,st.st_size,st.st_mtime_ns));n+=1;total+=st.st_size
   if n%1000==0:C.commit();log(stage='live-index',files=n,GiB=round(total/1024**3,3))
 C.commit();log(stage='live-index-complete',files=n,GiB=round(total/1024**3,3))

def zip_fingerprints(p,z):
 ranges=[]
 with p.open('rb')as f:
  for i,info in enumerate(z.infolist()):
   if info.is_dir():continue
   assert not info.flag_bits&1,'Encrypted source archive requires explicit handling'
   f.seek(info.header_offset);header=f.read(30);assert header[:4]==b'PK\x03\x04'
   nl,xl=struct.unpack_from('<HH',header,26);start=info.header_offset+30+nl+xl
   ranges.append([start,start+info.compress_size,i,sha256()])
 ranges.sort();assert all(ranges[i][1]<=ranges[i+1][0]for i in range(len(ranges)-1))
 size=p.stat().st_size;raw=sha256();git=sha1(('blob '+str(size)+'\0').encode());pos=0;idx=0
 with p.open('rb')as f:
  while True:
   b=f.read(BATCH)
   if not b:break
   raw.update(b);git.update(b);end=pos+len(b);view=memoryview(b)
   while idx<len(ranges)and ranges[idx][1]<=pos:idx+=1
   k=idx
   while k<len(ranges)and ranges[k][0]<end:
    lo,hi,ordinal,h=ranges[k]
    if hi>pos:h.update(view[max(lo,pos)-pos:min(hi,end)-pos])
    if hi<=end:k+=1
    else:break
   idx=k;pos=end
 assert pos==size
 return raw.hexdigest(),git.hexdigest(),{ordinal:h.hexdigest()for _,_,ordinal,h in ranges}

def preserve_zip(p,label=None):
 name=label or rel(p);size=p.stat().st_size
 done=C.execute('SELECT bytes,status FROM containers WHERE path=?',(name,)).fetchone()
 if done:
  assert done[0]==size and done[1]=='verified';return
 try:z=zipfile.ZipFile(p)
 except zipfile.BadZipFile:
  with p.open('rb')as f:digest,git=consume(f,size,'unreadable-original-container')
  C.execute('INSERT INTO containers VALUES(?,?,?,?,?,?)',(name,size,digest,git,0,'verified'));C.commit();log(stage='unreadable-container-preserved',file=name);return
 with z:
  rawsha,rawgit,fp=zip_fingerprints(p,z);new=0;reused=0
  for ordinal,info in enumerate(z.infolist()):
   if info.is_dir():continue
   compressed=fp[ordinal]
   known=C.execute('SELECT sha256 FROM representations WHERE method=? AND bytes=? AND crc=? AND compressed_sha256=?',(info.compress_type,info.file_size,info.CRC,compressed)).fetchone()
   if known:digest=known[0];reused+=1
   else:
    with z.open(info)as f:digest,git=consume(f,info.file_size,'historical-member')
    C.execute('INSERT INTO representations VALUES(?,?,?,?,?)',(info.compress_type,info.file_size,info.CRC,compressed,digest));new+=1
   assert content_info(digest)
   C.execute('INSERT OR REPLACE INTO members VALUES(?,?,?,?,?,?,?)',(name,ordinal,info.filename,digest,info.file_size,info.CRC,compressed))
  C.execute('INSERT INTO containers VALUES(?,?,?,?,?,?)',(name,size,rawsha,rawgit,len(z.infolist()),'verified'));C.commit()
  log(stage='container-preserved',file=name,GiB=round(size/1024**3,3),entries=len(z.infolist()),representationsRead=new,identicalCompressedStreamsReused=reused)

def collect_archives():
 index_live()
 roots=[W/'Huyen_Hoc_Cac_V53_source.zip',W/'Huyen_Hoc_Cac_V53_web.zip']
 roots+=sorted(p for p in W.glob('*.zip')if p not in roots)
 roots+=sorted(p for p in(W/'archives').rglob('*.zip'))
 for i,p in enumerate(roots,1):preserve_zip(p);log(stage='archive-progress',done=i,total=len(roots))
 for p in sorted((W/'archives').rglob('*')):
  if not p.is_file()or p.suffix=='.zip':continue
  st=p.stat()
  with p.open('rb')as f:digest,git=consume(f,st.st_size,'historical-archive-file')
  C.execute('INSERT OR REPLACE INTO files VALUES(?,?,?,?)',(rel(p),digest,st.st_size,st.st_mtime_ns))
 C.commit();write_state('archives-preserved');log(stage='archives-preserved',containers=C.execute('SELECT count(*)FROM containers').fetchone()[0],uniqueContents=C.execute('SELECT count(*)FROM content').fetchone()[0])

class GitStream:
 def __init__(self,p):self.f=p.open('rb');self.z=zlib.decompressobj();self.buf=b'';self.eof=False
 def read(self,n):
  while len(self.buf)<n and not self.eof:
   b=self.f.read(1024*1024)
   if not b:self.buf+=self.z.flush();self.eof=True;break
   self.buf+=self.z.decompress(b)
  out=self.buf[:n];self.buf=self.buf[n:];return out
 def header(self):
  value=b''
  while not value.endswith(b'\0'):value+=self.read(1)
  return value[:-1].decode().split(' ')
 def close(self):self.f.close()

def collect_git():
 folder=W/'.git/objects';n=0;represented=0;extracted=0
 for directory in sorted(folder.iterdir()):
  if not directory.is_dir()or len(directory.name)!=2:continue
  for p in sorted(directory.iterdir()):
   if len(p.name)!=38:continue
   oid=directory.name+p.name
   if C.execute('SELECT 1 FROM git_objects WHERE oid=?',(oid,)).fetchone():continue
   # OID is the cryptographic Git hash over type/size/content.
   known=C.execute('SELECT sha256,bytes FROM content WHERE git_sha1=?',(oid,)).fetchone()
   container=C.execute('SELECT sha256,bytes FROM containers WHERE git_sha1=?',(oid,)).fetchone()
   if known or container:
    value=known or container;C.execute('INSERT INTO git_objects VALUES(?,?,?,?,?)',(oid,'blob',value[1],value[0],'content-retained'if known else'container-members-consolidated'));represented+=1;n+=1;continue
   stream=GitStream(p)
   try:
    typ,amount=stream.header();size=int(amount)
    if typ=='blob':
     digest,actual=consume(stream,size,'git-only-blob');assert actual==oid
     location=W/content_info(digest)[0]
     if size>1024*1024 and location.is_file()and zipfile.is_zipfile(location):
      preserve_zip(location,'git-object:'+oid)
     C.execute('INSERT INTO git_objects VALUES(?,?,?,?,?)',(oid,typ,size,digest,'unique-content-retained'));extracted+=1
    else:
     b=stream.read(size);assert len(b)==size
     actual=sha1((typ+' '+str(size)+'\0').encode()+b).hexdigest();assert actual==oid
     digest=sha256(b).hexdigest();dst=OBJ/digest[:2]/digest;dst.parent.mkdir(exist_ok=True)
     if not dst.exists():dst.write_bytes(b)
     C.execute('INSERT OR IGNORE INTO content VALUES(?,?,?,?,?)',(digest,size,oid,rel(dst),'git-'+typ))
     C.execute('INSERT INTO git_objects VALUES(?,?,?,?,?)',(oid,typ,size,digest,'metadata-retained'));extracted+=1
   finally:stream.close()
   n+=1
   if n%1000==0:C.commit();log(stage='git-content',objects=n,alreadyPreserved=represented,unique=extracted)
 C.commit();write_state('git-content-preserved');log(stage='git-content-preserved',objects=C.execute('SELECT count(*)FROM git_objects').fetchone()[0])

def verify():
 # Every historical entry resolves to retained byte content, and each content is hashed.
 missing=C.execute('SELECT count(*)FROM members m LEFT JOIN content c ON c.sha256=m.sha256 WHERE c.sha256 IS NULL').fetchone()[0];assert missing==0
 count=0;total=0
 for digest,size,git,path,kind in C.execute('SELECT * FROM content'):
  p=W/path;assert p.is_file()and p.stat().st_size==size,(path,size)
  h=sha256()
  with p.open('rb')as f:
   for b in iter(lambda:f.read(BATCH),b''):h.update(b)
  assert h.hexdigest()==digest,path;count+=1;total+=size
 C.commit();write_state('all-retained-content-sha256-verified');log(stage='verification-complete',uniqueContent=count,GiB=round(total/1024**3,3))

def write_state(status):
 result={'status':status,'updatedAt':datetime.now(timezone(timedelta(hours=7))).isoformat(),'retainedContentObjects':C.execute('SELECT count(*)FROM content').fetchone()[0],'originalContainers':C.execute('SELECT count(*)FROM containers').fetchone()[0],'historicalMemberOccurrences':C.execute('SELECT count(*)FROM members').fetchone()[0],'gitObjectsPreserved':C.execute('SELECT count(*)FROM git_objects').fetchone()[0],'collectionNeverDeletesArchives':True,'chatHistoryUntouched':True}
 (R/'COLLECTION_STATE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
 mode=sys.argv[1]if len(sys.argv)>1 else'archives'
 if mode=='archives':collect_archives()
 elif mode=='git':collect_git()
 elif mode=='verify':verify()
 else:raise ValueError(mode)
 C.close()
