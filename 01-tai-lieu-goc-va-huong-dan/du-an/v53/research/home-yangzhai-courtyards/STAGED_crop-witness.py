from pathlib import Path
from hashlib import sha256
import json
from PIL import Image
b=Path(__file__).resolve().parent
specs=[(82,86,(2700,4200,3670,5500),False),(83,86,(840,4200,1670,5500),False),
 (84,87,(1760,760,2540,1870),False),(85,87,(2730,2500,3560,3660),False),
 (86,87,(750,2500,1510,3660),True),(87,87,(1760,4260,2520,5400),True),
 (88,88,(2850,770,3670,1960),True),(89,88,(865,800,1660,1960),True),
 (90,88,(1880,2500,2640,3660),True),(91,88,(2850,4240,3660,5400),False),
 (92,88,(865,4240,1660,5400),True),(93,89,(1680,750,2490,1900),False)]
rows=[]
for c,p,box,rotate in specs:
 src=b/f'gjts-p{p}.png';out=b/f'qa/gjts-case{c}-native.png'
 im=Image.open(src).crop(box)
 if rotate:im=im.transpose(Image.Transpose.ROTATE_180)
 im.save(out)
 rows.append(dict(caseID=f'YZSS-C{c}',sourceDjvuPage=p,sourceFile=src.name,file=out.relative_to(b).as_posix(),cropBox=box,transpose='ROTATE_180' if rotate else None,resampled=False,sha256=sha256(out.read_bytes()).hexdigest(),actuallyViewed=False))
(b/'GJTS_QA_IMAGES.json').write_text(json.dumps({'date':'2026-10-28','derivedNativeCropsNotRawHTTPBodies':True,'records':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote12nativewitnesscrops;notyetviewed')
