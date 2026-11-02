from pathlib import Path
from PIL import Image,ImageDraw
from hashlib import sha256
import json
q=Path(__file__).resolve().parent.parent/'qa/meihua-table-bodies'
regions=[(33,'qian-weather',.245,.30,.18,.52),(33,'qian-geography',.185,.245,.18,.66),(34,'qian-time',.575,.64,.15,.78),(39,'zhen-object',.455,.515,.15,.66),(39,'zhen-food',.235,.29,.15,.68),(42,'xun-house',.585,.64,.15,.76),(46,'li-weather',.19,.255,.15,.76),(46,'li-geography',.135,.195,.15,.81),(47,'li-person',.76,.83,.15,.78),(47,'li-action',.705,.765,.15,.78),(47,'li-office',.18,.245,.15,.78),(49,'gen-animal',.18,.245,.15,.78)]
records=[];tiles=[]
for n,label,x0,x1,y0,y1 in regions:
 im=Image.open(q/f'native-{n}.png');box=tuple(round(v*d)for v,d in zip([x0,y0,x1,y1],[im.width,im.height,im.width,im.height]));crop=im.crop(box);p=q/(label+'.png');crop.save(p)
 records.append({'pdfPage':n,'label':label,'nativePNG':f'native-{n}.png','nativeSHA256':sha256((q/f'native-{n}.png').read_bytes()).hexdigest(),'cropBoxXYXY':list(box),'cropSHA256':sha256(p.read_bytes()).hexdigest()})
 panel=Image.new('RGB',(max(135,crop.width+20),crop.height+44),'white');ImageDraw.Draw(panel).text((5,5),str(n)+' '+label,fill='black');panel.paste(crop,(10,34));tiles.append(panel)
for group,start in [(tiles[:6],1),(tiles[6:],2)]:
 canvas=Image.new('RGB',(sum(t.width for t in group),max(t.height for t in group)),'white');x=0
 for tile in group:canvas.paste(tile,(x,0));x+=tile.width
 canvas.save(q/f'glyph-sheet-{start}.png')
(q/'GLYPH_CROPS.json').write_text(json.dumps({'operation':'Read-onlyPDF300dpiPopplerrender;rectangularPILcrops,noOCR/sharpening/textreplacement.','newSourceHTTP':0,'nativePages':7,'crops':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
