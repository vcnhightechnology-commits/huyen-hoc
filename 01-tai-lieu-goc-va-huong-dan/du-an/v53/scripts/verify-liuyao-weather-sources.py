from pathlib import Path
from hashlib import sha256
import json,subprocess,shutil
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-weather';q=r/'qa/liuyao-weather'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
src=read(b/'SOURCE_MANIFEST.json');manual=read(b/'MANUAL_READINGS.json');source=w/src['sourcePDF']
assert source.stat().st_size==11089308 and sha(source)==src['sourceSHA256']=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
assert len(manual['records'])==30 and [x['pdfPage']for x in manual['records']]==list(range(191,221))
assert [x['pdfPage']for x in manual['records']if x['actuallyViewed']]==list(range(191,214))
for x in manual['records']:assert sha(b/x['file'])==x['sha256']and Image.open(b/x['file']).size==tuple(x['size'])
for x in src['expandedPriorPages']:assert sha(w/x['file'])==x['sha256']
high=manual['highResolutionQA'];assert sha(b/high['file'])==high['sha256']and high['actuallyViewed']
renderer=shutil.which('pdftoppm');assert renderer
reproductions=[]
for dpi,expected in[(144,b/'images/zengshan-191.png'),(360,b/high['file'])]:
 prefix=q/f'redecode-{dpi}';subprocess.run([renderer,'-r',str(dpi),'-f','191','-l','191','-png',str(source),str(prefix)],check=True,capture_output=True)
 actual=q/f'redecode-{dpi}-191.png'
 a=Image.open(actual).convert('RGB');e=Image.open(expected).convert('RGB');assert a.size==e.size and a.tobytes()==e.tobytes()
 reproductions.append({'sourcePage':191,'dpi':dpi,'file':actual.relative_to(q).as_posix(),'sha256':sha(actual),'pixelRGB_SHA256':sha256(a.tobytes()).hexdigest(),'pixelMatch':True,'notNewSourcePosition':True})
roles=read(b/'QUESTION_ROLES.json')['methods'];assert len(roles)==2 and sum(len(x['selectors'])for x in roles)==5
assert roles[0]['sourcePages']==[191]and roles[1]['sourcePages']==[201]
assert next(x for x in roles[0]['selectors']if x['question']=='clear')['desiredKin']==['子孫']
assert next(x for x in roles[1]['selectors']if x['question']=='clear')['desiredKin']==['子孫','妻財']
units=read(b/'B02_CURRENT_UNITS.json');assert units['currentCounts']['wholeUnitsApplied']==0 and len(units['units'])==136
assert len([x for x in units['units']if x['disposition']=='heading-only-body-extraction-open'])==95
out={'date':'2026-10-27','sourcePDFBytes':11089308,'sourcePDFSHA256':src['sourceSHA256'],'newHTTPRequests':0,'newOriginalContainers':0,
 'promotedRenderedPositions':30,'promotedViewedPositions':23,'newWeatherContentPositionsRead':21,'newParatextPositionsRead':1,'newNextChapterOpeningPositionsRead':1,
 'expandedPriorBodyPositions':3,'renderedNotReadPositions':7,'sourceImageHashesVerified':34,'reproductions':reproductions,
 'namedRoleVoices':2,'namedSelectors':5,'allSourceImageCharactersCollated':False,'wholeChapterApplied':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items()if k!='reproductions'},ensure_ascii=False))
