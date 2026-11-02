from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
b=Path(__file__).resolve().parent;w=b.parents[1];src=w/'v53/research/home-yangzhai-final-spans/selection/raw-p135.jpg'
box=[1240,220,1400,1950];out=b/'p135-gouchen-column-native.png';Image.open(src).crop(box).save(out)
(b/'QA_IMAGES.json').write_text(json.dumps(dict(date='2026-10-28',sourceFile=src.relative_to(w).as_posix(),sourceSHA256=sha256(src.read_bytes()).hexdigest(),file=out.name,cropBox=box,sha256=sha256(out.read_bytes()).hexdigest(),resampled=False,actuallyViewed=False),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(out.name)
