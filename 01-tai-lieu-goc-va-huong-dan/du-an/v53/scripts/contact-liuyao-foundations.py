from pathlib import Path
from PIL import Image,ImageDraw
q=Path(__file__).resolve().parent.parent/'qa/liuyao-foundations/navigation'
for book in ['zengshan','bushi']:
 files=sorted(q.glob(book+'-*.png'))
 for group in range(0,len(files),8):
  canvas=Image.new('RGB',(1120,940),'#eeeeee');draw=ImageDraw.Draw(canvas)
  for j,p in enumerate(files[group:group+8]):
   im=Image.open(p).convert('RGB');im.thumbnail((270,430));x=(j%4)*280;y=(j//4)*470;canvas.paste(im,(x+(280-im.width)//2,y+28));draw.text((x+12,y+6),p.name,fill='black')
  canvas.save(q/f'contact-{book}-{group//8+1}.png')
