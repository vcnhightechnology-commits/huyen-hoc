from pathlib import Path
from hashlib import sha256
import json,sys,subprocess
from PIL import Image,ImageChops
from pypdf import PdfReader
v=Path(__file__).resolve().parent.parent;w=v.parent;r=v/'research/home-fuduan';q=v/'qa/home-fuduan'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
no_write='--no-write'in sys.argv
def identity(p,x):
 b=p.read_bytes();assert len(b)==x['bytes']and sha256(b).hexdigest()==x['sha256'],str(p)
def mapped(s):
 return r/Path(s).name if s.startswith('tmp/home-fuduan-staging/')else w/s
promotion=read(r/'PROMOTION_IDENTITIES.json')
for x in promotion['files']:identity(r/x['file'],x)
requests=read(r/'REQUESTS.json')
assert len(requests)==3
for x in requests:assert x['status']==200 and x['standardTLSValidation']is True;identity(r/x['file'],x)
frozen=read(r/'PREIMPLEMENTATION_FREEZE.json');assert frozen['referenceImplementationExists']is False
for x in frozen['files']:identity(r/x['file'],x)
claims=read(r/'SOURCE_CLAIMS.json')
pdf=PdfReader(r/'SSID-12152602-vol33-36.pdf');assert len(pdf.pages)==107
raw=read(r/'RAW_DCT_IMAGES.json')['records']
for x in raw:
 p=mapped(x['rawDCT']['file']);identity(p,x['rawDCT'])
 obj=pdf.pages[x['pdfPage']-1]['/Resources']['/XObject']['/Im0'].get_object()
 assert str(obj['/Filter'])=='/DCTDecode'and obj._data==p.read_bytes()
 assert x['viewed']and x['priorExtractedImage']['finalEvidenceExcluded']
crops=0;excluded=0
for name in ['NATIVE_CROPS.json','XIEJI_NATIVE_CROPS.json']:
 for x in read(r/name)['records']:
  identity(mapped(x['source']['file']),x['source']);identity(mapped(x['crop']['file']),x['crop'])
  if not x['accepted']:excluded+=1;continue
  assert x['viewed']
  im=Image.open(mapped(x['source']['file'])).convert('RGB')
  cropped=Image.open(mapped(x['crop']['file'])).convert('RGB')
  assert ImageChops.difference(im.crop(x['boxXYXY']),cropped).getbbox()is None
  crops+=1
assert crops==5 and excluded==2
reading=read(r/'READING_AUDIT.json');assert len(reading['records'])==11 and not reading['all107PagesRead']
for x in reading['records']:identity(mapped(x['identity']['file']),x['identity']);assert x['actuallyViewedFullImage']
table=claims['table'];assert sum(len(x['values'])for x in table['columnsRightToLeft'])==84
assert table['printedRowHeading']=='日'and table['rowSemanticAdapter']is None and table['fortuneAnnotationsNotTranscribed']
assert not claims['sourceCalendarEpochResolved']and not claims['sourceOutcomesValidated']and not claims['sameMeaningAsITKCChenKeGanEstablished']
assert not claims['bibliography']['samePhysicalEditionAsWikisourceEstablished']
assert 'oldid=627179' in (r/'wikisource-vol36.html').read_text(encoding='utf-8')
proc=subprocess.run(['node',str(r/'test-fuduan-reference.mjs')],capture_output=True,text=True,encoding='utf-8',check=True)
tests=json.loads(proc.stdout);assert tests==read(q/'REFERENCE_RESULTS.json')==read(r/'REFERENCE_RESULTS.json')
out={'date':'2026-10-29','passed':True,'promotedFilesVerified':len(promotion['files']),'HTTP200TLSBodies':3,'PDFPages':107,'positionsActuallyViewed':11,'unreadPositions':96,'rawDCTStreamsMatched':3,'acceptedNativeCropsRGBMatched':crops,'excludedTrialCrops':excluded,'excludedReencodedJPEGs':3,'preimplementationFrozenFilesUnchanged':len(frozen['files']),'sourceMansionCells':84,'sourceProseExamples':7,'sourceQuotedBoundaryCounterexamples':1,'additionalDerivedBoundaryExpectations':6,'referenceTests':tests,'newCalendarEngineCalls':0,'newChartEngineCalls':0,'consumerRuleIntroduced':False,'wholeWorkApplied':False}
if no_write:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
