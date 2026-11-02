from pathlib import Path
import re
B=Path(__file__).resolve().parent
for p in sorted(B.glob('client-*.js')):
 s=p.read_text(encoding='utf-8');print('FILE',p.name)
 for needle in ['62783:function','91462:function','/api/','getPage','get_page','page_list','getBook','pageList','startPageId']:
  hits=list(re.finditer(re.escape(needle),s));print(needle,len(hits))
  for m in hits[:8]:print(s[max(0,m.start()-130):m.end()+210])
