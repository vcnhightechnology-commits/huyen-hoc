from pathlib import Path
from html.parser import HTMLParser
import json,re
B=Path(__file__).resolve().parent
class Page(HTMLParser):
 def __init__(self):super().__init__();self.scripts=[];self.current=None;self.parts=[]
 def handle_starttag(self,tag,attrs):
  if tag=='script':self.current={'attrs':dict(attrs),'text':''}
 def handle_data(self,data):
  if self.current is not None:self.current['text']+=data
  else:self.parts.append(data)
 def handle_endtag(self,tag):
  if tag=='script'and self.current is not None:self.scripts.append(self.current);self.current=None
p=Page();p.feed((B/'chapter-response.html').read_text(encoding='utf-8'))
print(json.dumps({'scripts':[{**r['attrs'],'chars':len(r['text']),'starts':r['text'][:80]}for r in p.scripts if len(r['text'])>1000]},ensure_ascii=False))
text='\n'.join(p.parts);(B/'chapter-visible-extracted.txt').write_text(text,encoding='utf-8')
for needle in ['底本','版本','SDZJ0170','安童限','安大限','安身主']:
 for value in [text,*[r['text']for r in p.scripts if'SDZJ0170'in r['text']]]:
  positions=[m.start()for m in re.finditer(re.escape(needle),value)]
  print(needle,len(positions),[value[max(0,i-100):i+240]for i in positions[-3:]])
for i,r in enumerate(p.scripts):
 if r['attrs'].get('type')=='application/json':
  try:d=json.loads(r['text'])
  except ValueError:continue
  (B/f'embedded-json-{i}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
