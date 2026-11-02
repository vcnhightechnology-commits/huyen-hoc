"""Historical text/code must survive later edits of current working files."""
from pathlib import Path
from hashlib import sha256
import sqlite3,shutil,json
W=Path(__file__).resolve().parent.parent;H=W/'recovery/consolidated-history';R=W/'recovery/storage-consolidation';c=sqlite3.connect(H/'INDEX.sqlite')
immutable={'.pdf','.djvu','.png','.jpg','.jpeg','.webp','.gif','.woff','.woff2','.ttf','.otf','.exe','.dll','.zip','.sqlite'}
count=0;total=0
for digest,size,git,location,kind in c.execute('SELECT * FROM content').fetchall():
 if location.startswith('recovery/consolidated-history/objects/'):continue
 src=W/location
 if src.suffix.lower()in immutable:continue
 assert src.stat().st_size==size,location
 dst=H/'objects'/digest[:2]/digest;dst.parent.mkdir(exist_ok=True)
 if not dst.exists():shutil.copy2(src,dst)
 assert sha256(dst.read_bytes()).hexdigest()==digest,location
 c.execute('UPDATE content SET path=?,kind=? WHERE sha256=?',(dst.relative_to(W).as_posix(),'sealed-history-'+kind,digest));count+=1;total+=size
 if count%1000==0:c.commit();print(json.dumps({'stage':'seal-mutable-history','files':count}),flush=True)
c.commit();c.close();out={'status':'mutable-history-text-code-sealed-by-sha256','files':count,'bytes':total,'nativeOriginalBinarySourcesKeptAtPinnedLivePaths':True,'purpose':'Later edits to current text/code will not invalidate restoration of old unique source versions.'};(R/'SEALED_MUTABLE_HISTORY.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out),flush=True)
