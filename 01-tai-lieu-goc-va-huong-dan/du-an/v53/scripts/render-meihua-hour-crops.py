from pathlib import Path
from PIL import Image
import numpy as np
from hashlib import sha256
import json
q=Path(__file__).resolve().parent.parent/'qa/meihua-hour-table';records=[]
for n in range(207,213):
 im=Image.open(q/f'native-{n}.png')
 a=np.array(im.convert('L'));projection=(a[round(im.height*.13):round(im.height*.20)]<100).sum(axis=0)
 xs=np.flatnonzero((projection>5)&(np.arange(im.width)>im.width*.1)&(np.arange(im.width)<im.width*(.435 if n==207 else .84)));runs=[]
 for x in xs:
  if runs and x-runs[-1][-1]<=14:runs[-1].append(int(x))
  else:runs.append([int(x)])
 runs=runs[:4]if n==207 else runs[-8:]if n==212 else runs
 assert len(runs)==(4 if n==207 else 8 if n==212 else 12)
 groups=[list(reversed(runs))[i:i+4]for i in range(0,len(runs),4)];names=['rows-1-4']if n==207 else ['right','left']if n==212 else ['right','middle','left']
 boxes=[(name,(min(g[0]for g in group)-25,round(im.height*.13),max(g[-1]for g in group)+60,round(im.height*.70)))for name,group in zip(names,groups)]
 if n==207:boxes.append(('premise',(round(im.width*.41),round(im.height*.13),round(im.width*.59),round(im.height*.70))))
 if n==210:boxes.append(('gui-mao-noon-glyph',(270,940,435,1120)))
 if n==211:boxes.append(('ding-wei-zi-glyph',(970,470,1170,660)))
 for label,box in boxes:
  name=f'p{n}-{label}.png';im.crop(box).save(q/name)
  records.append({'pdfPage':n,'nativeFile':f'native-{n}.png','nativeSHA256':sha256((q/f'native-{n}.png').read_bytes()).hexdigest(),'headerPixelRuns':[[g[0],g[-1]]for g in runs],'crop':name,'cropBoxXYXY':box,'cropSHA256':sha256((q/name).read_bytes()).hexdigest()})
  if label.endswith('-glyph'):
   crop=im.crop(box);zoom=label+'-4x.png';crop.resize((crop.width*4,crop.height*4),Image.Resampling.NEAREST).save(q/zoom)
   records.append({'pdfPage':n,'nativeFile':f'native-{n}.png','nativeSHA256':sha256((q/f'native-{n}.png').read_bytes()).hexdigest(),'crop':zoom,'cropBoxXYXY':box,'scale':4,'resampling':'nearest-no-new-detail','cropSHA256':sha256((q/zoom).read_bytes()).hexdigest()})
(q/'CROPS.json').write_text(json.dumps({'operation':'BundledPoppler300dpi read-only render and rectangular PIL crops;no OCR/text replacement.','nativePages':6,'records':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
