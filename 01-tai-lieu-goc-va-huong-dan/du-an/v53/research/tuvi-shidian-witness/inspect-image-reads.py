from pathlib import Path
import re
B=Path(__file__).resolve().parent
for name in ['7691.d2ca499c.js','8920.c8dfe8e9.js']:
 p=B/('client-'+name);s=p.read_text(encoding='utf-8');print('FILE',name)
 for needle in ['62783:function','91462:function','/api/','getPageList','get_page','page_list','getPageInfo','pageDetail','picUrl','pageIds']:
  hits=list(re.finditer(re.escape(needle),s))
  if hits:print(needle,len(hits));print('\n'.join(s[max(0,m.start()-90):m.end()+260]for m in hits[:5]))
