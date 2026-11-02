from pathlib import Path
from html.parser import HTMLParser
import json,hashlib,re
root=Path(__file__).resolve().parent.parent
out=root/'research/yi-lines';out.mkdir(parents=True,exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
class Node:
 def __init__(self,tag='',attrs=None):self.tag=tag;self.attrs=dict(attrs or []);self.children=[]
 def all(self,tag=None):
  for c in self.children:
   if isinstance(c,Node):
    if tag is None or c.tag==tag:yield c
    yield from c.all(tag)
 def text(self):
  if any(s in self.attrs.get('class','').split() for s in ['variant-tooltip','reference']):return ''
  return ''.join(c if isinstance(c,str) else c.text() for c in self.children)
class DOM(HTMLParser):
 def __init__(self):super().__init__();self.root=Node();self.stack=[self.root]
 def handle_starttag(self,tag,attrs):
  n=Node(tag,attrs);self.stack[-1].children.append(n)
  if tag not in ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']:self.stack.append(n)
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,0,-1):
   if self.stack[i].tag==tag:self.stack=self.stack[:i];break
 def handle_data(self,text):self.stack[-1].children.append(text)
def han(s):return re.sub(r'[^\u3400-\u9fff\U00020000-\U0002fa1f]','',s)
old=json.loads((root.parent/'v49/data/yi_research.json').read_text(encoding='utf-8'))
records=[]
for n in [1,2]:
 prior=old['hexagrams'][n-1];path=root.parent/'v48/evidence/yi'/f'{n:02}.html';b=path.read_bytes();assert sha(b)==prior['source']['sha256']
 p=DOM();p.feed(b.decode('utf-8'));area=next(x for x in p.root.all() if 'mw-parser-output' in x.attrs.get('class','').split());ol=next(area.all('ol'));lis=[x for x in ol.children if isinstance(x,Node) and x.tag=='li'];assert len(lis)==7
 for i,l in enumerate(lis[:6]):
  text=l.text().strip();label=prior['lines'][i]['sourceLineLabel'];assert text.startswith(label+'：') or text.startswith(label+':'),text
  source=text[len(label)+1:].strip();assert han(source)==han(prior['lines'][i]['sourceLine'])
  records.append({'number':n,'position':i+1,'label':label,'sourceText':source,'sourceFile':str(path.relative_to(root.parent)),'sha256':sha(b),'revision':prior['source']['revision'],'review':'Authored practical paraphrase checked against this source text motif; no full literal translation, divination guarantee or independent philological certification.'})
 extra=lis[6].text().strip();label='用九' if n==1 else '用六';assert extra.startswith(label+'：')
 records.append({'number':n,'position':'all-moving-supplement','label':label,'sourceText':extra[len(label)+1:],'sourceFile':str(path.relative_to(root.parent)),'sha256':sha(b),'revision':prior['source']['revision'],'review':'Supplementary reading when all six lines of Qian/Kun move. Not encoded as a universal precedence rule for changing lines.'})
audit={'schema':'hhc.yi-moving-line-reading.source-audit.v1','date':'2026-10-25','scope':{'hexagrams':[1,2],'ordinaryLines':12,'supplementaryLines':2,'remainingOrdinaryLinesWithoutSpecificReading':372},'sourceType':'Two already archived Wikisource digital witnesses. Original bytes rechecked and direct LI text parsed independently from saved HTML; no duplicate downloads or scanned historical edition claim.','records':records,'editorialLimits':['Practical Vietnamese paraphrase, not literal translation or quotations of a modern copyrighted translation.','Kun line 2 is not taken as permission to stop learning; Kun line 5 does not prescribe yellow clothing for luck.','Qian/Kun all-moving supplements coexist with the six individual readings; no school is declared universally binding.','Other hexagrams retain clearly labeled position-based prompts.','No source text, URLs, revisions or corpus are shipped in the consumer interface.']}
(out/'SOURCE_AUDIT.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('14 source units located and compared with archived byte hashes.')
