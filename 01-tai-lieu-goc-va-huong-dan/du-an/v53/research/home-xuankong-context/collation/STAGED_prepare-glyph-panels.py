from pathlib import Path
from PIL import Image,ImageDraw
from hashlib import sha256
import json
b=Path(__file__).resolve().parent;w=b.parents[1];s=w/'v53/qa/home-yangzhai-courtyards'
specs=[('C84-6',84,[315,145,450,300]),('C84-2',84,[315,700,450,850]),('C90-6',90,[315,170,450,320]),('C90-1',90,[315,845,450,990]),('C91-4',91,[315,455,450,610]),('C92-5',92,[315,200,450,355]),('C93-2',93,[315,670,450,830])]
rows=[]
for label,c,box in specs:
 src=s/f'gjts-case{c}-native.png';out=b/f'{label}-glyph-native.png';im=Image.open(src).crop(box);im.save(out)
 rows.append(dict(label=label,sourceFile=src.relative_to(w).as_posix(),file=out.name,cropBox=box,sha256=sha256(out.read_bytes()).hexdigest(),resampled=False,actuallyViewed=False))
(b/'QA_IMAGES.json').write_text(json.dumps(dict(date='2026-10-28',records=rows,notNewSourcePositions=True),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote7isolatednativecrops;awaitactualview')
