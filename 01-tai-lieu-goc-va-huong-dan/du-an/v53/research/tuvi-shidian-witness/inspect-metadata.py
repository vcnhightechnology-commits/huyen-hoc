from pathlib import Path
from html.parser import HTMLParser
import json
B=Path(__file__).resolve().parent;d=json.loads((B/'public-router-data.json').read_text(encoding='utf-8'));r=d['loaderData']['__session/(lang$)/book/$'];book=r['bookInfo']
print(json.dumps({k:book[k]for k in ['bookName','library','publicationStmt','edition','extra','license','catalog']},ensure_ascii=False,indent=2))
print('volume',json.dumps(r['volume'],ensure_ascii=False)[:2000])
class Parser(HTMLParser):
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='script'and'src'in a:print('SCRIPT',a['src'])
p=Parser();p.feed((B/'chapter-response.html').read_text(encoding='utf-8'))
