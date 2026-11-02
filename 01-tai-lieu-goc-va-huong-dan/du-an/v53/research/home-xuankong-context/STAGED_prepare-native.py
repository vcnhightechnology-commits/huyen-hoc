from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
b=Path(__file__).resolve().parent;w=b.parents[1];rows=[]
for p,name,box in [(94,'p94-room-polarity-native.png',[1220,260,2420,1900]),(98,'p98-count-balance-native.png',[1220,240,2420,1880])]:
 src=w/f'v53/research/home-yangzhai-door-water/raw-p{p:03}.jpg';out=b/name;Image.open(src).crop(box).save(out)
 rows.append(dict(sourcePDFPage=p,sourceFile=src.relative_to(w).as_posix(),sourceSHA256=sha256(src.read_bytes()).hexdigest(),file=name,cropBox=box,sha256=sha256(out.read_bytes()).hexdigest(),resampled=False,actuallyViewed=False))
(b/'QA_IMAGES.json').write_text(json.dumps(dict(date='2026-10-28',records=rows),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Prepared2nativecrops')
