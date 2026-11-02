from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
import json,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(n):return json.loads((B/n).read_text(encoding='utf-8-sig'))
def verify(row):
 p=W/row['file'];assert p.stat().st_size==row['bytes']and sha256(p.read_bytes()).hexdigest()==row['sha256'],row['file']
frozen=read('DIGITAL_WITNESS_FREEZE.json')
for row in frozen['files']+frozen['clientFiles']:verify(row)
for row in read('RETAINED_COMPARISON_IDENTITIES.json')['files']:verify(row)
host=read('HOST_REQUEST.json');assert host['status']==200 and host['bytes']==992096 and not host['TLSVerificationDisabled']
assert sha256((B/'chapter-response.html').read_bytes()).hexdigest()==host['sha256']
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.active=False;self.scripts=[];self.current=''
 def handle_starttag(self,t,a):
  if t=='script':self.active=True;self.current=''
 def handle_data(self,d):
  if self.active:self.current+=d
 def handle_endtag(self,t):
  if t=='script'and self.active:self.scripts.append(self.current);self.active=False
p=Parser();p.feed((B/'chapter-response.html').read_text(encoding='utf-8'));s=next(x for x in p.scripts if x.startswith('window._ROUTER_DATA = '));d=json.JSONDecoder().raw_decode(s.split('=',1)[1].lstrip())[0]
r=d['loaderData']['__session/(lang$)/book/$'];ledger=read('DIGITAL_PASSAGE_LEDGER.json')
assert r['bookInfo']['bookId']==ledger['bookID']=='SDZJ0170';assert r['ssrChapterId']==ledger['chapterID'];assert r['bookInfo']['library']==ledger['metadataClaims']['library']=='日本内阁文库'
assert r['bookInfo']['edition']==ledger['metadataClaims']['edition']=={'edition':'南阳堂刊本','editionDynastyName':'明'}
assert r['bookInfo']['totalPage']==528 and ledger['metadataClaims']['pageCountIsNotReadCount']
for record in ledger['records']:
 q=r['paragraphList'][record['paragraphIndexZeroBased']];assert q['paragraphId']==record['paragraphId']and q['startPageId']==record['startPageId']and q['endPageId']==record['endPageId']
 lines=[x['content']for x in json.loads(q['content'])['lines']if x['content'].strip()];assert lines==record['underlyingLiteralLines']and q['contentEncryptType']==0
 assert not record['sourceImageActuallyViewedOnThisPlatform']and not record['wholeRuleApplied']and not record['independentEditionEstablished']
assert len(ledger['records'])==7
assert ledger['records'][4]['underlyingLiteralLines']==['一命二財三疾厄，四妻五福六官禄。','餘年一泒順流行，十五命宫㸔端的。']
assert '火鈴星'in ledger['records'][6]['underlyingLiteralLines'][0]
assert read('ACQUISITION_SUMMARY.json')['publicOriginalImageBodies']==0
out={'passed':True,'frozenFiles':len(frozen['files']),'publicClientFilesSHA256Matched':len(frozen['clientFiles']),'retainedSourceEngineAndConsumerFilesUnchanged':7,'selectedDigitalParagraphsReproducedFromRawHTML':7,'platformMetadataPagesNotReadCount':528,'newIndependentEditions':0,'newSourceImages':0,'newEngineCalls':0,'ageConventionResolved':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
if '--write-results'in sys.argv:(B/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
