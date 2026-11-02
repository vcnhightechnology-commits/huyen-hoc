from pathlib import Path
from hashlib import sha256
import json,subprocess,shutil
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-family-study';q=r/'qa/liuyao-family-study'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
src=read(b/'SOURCE_MANIFEST.json');pdf=w/src['sourcePDF'];manual=read(b/'MANUAL_READINGS.json')
assert pdf.stat().st_size==src['sourceBytes']==11089308 and sha(pdf)==src['sourceSHA256']
assert [x['pdfPage']for x in src['images']]==[15,*range(232,264)]
for x in src['images']:
 p=w/x['file'];assert sha(p)==x['sha256']and Image.open(p).size==tuple(x['size'])and x['actuallyViewed']
assert sum(x['newReadPositionThisScope']for x in src['images'])==31 and sum(x['expandedPriorRead']for x in src['images'])==2
extra=src['extraQA'][0];assert extra['sourcePage']==259 and extra['actuallyViewed']and sha(w/extra['file'])==extra['sha256']
renderer=shutil.which('pdftoppm');assert renderer
renders=[]
for page,dpi,expected in[(233,144,b/'images/zengshan-233.png'),(259,144,b/'images/zengshan-259.png'),(15,240,q/'toc-015.png'),(259,360,q/'qa360-259.png')]:
 prefix=q/f'redecode-{page}-{dpi}'
 subprocess.run([renderer,'-r',str(dpi),'-f',str(page),'-l',str(page),'-png',str(pdf),str(prefix)],check=True,capture_output=True)
 actual=q/f'{prefix.name}-{page:03}.png';a=Image.open(actual).convert('RGB');e=Image.open(expected).convert('RGB');assert a.size==e.size and a.tobytes()==e.tobytes()
 renders.append({'sourcePage':page,'dpi':dpi,'file':actual.name,'sha256':sha(actual),'pixelMatch':True,'notNewSourcePosition':True})
units=read(b/'B02_CURRENT_UNITS.json');u=next(x for x in units['units']if x['id']=='B02-ch040')
assert u['normalizedHeading']=='趨避'and u['workingTranscriptionCorrection']['evidencePDFPages']==[15,235]
assert len(manual['chapterRanges'])==11 and not manual['chapter50']['wholeFirstPassRead']
out={'date':'2026-10-28','sourcePDFSHA256':src['sourceSHA256'],'sourceImageHashesVerified':33,'newSourceReadPositions':31,'expandedPriorReadPositions':2,
 'newNativeContentRenders':31,'newHighResolutionQARenders':2,'highResolutionQAViewed':True,'pixelReproductions':renders,'completeFirstPassSpans':11,
 'chapter50OpeningOnly':True,'workingTOCLabelsCorrected':1,'correctionEvidencePDFPages':[15,235],'sourceEmended':False,
 'newHTTPRequests':0,'newOriginalContainers':0,'independentNewWitnesses':0,'allSourceImageCharactersCollated':False,'sourceOutcomesValidated':False,'wholeChaptersApplied':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items()if k!='pixelReproductions'},ensure_ascii=False))
