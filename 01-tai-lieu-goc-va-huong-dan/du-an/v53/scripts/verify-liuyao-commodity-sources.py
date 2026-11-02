from pathlib import Path
from hashlib import sha256
import json,subprocess,shutil
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-commodity-boundary';q=r/'qa/liuyao-commodity-boundary'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
src=read(b/'SOURCE_MANIFEST.json');pdf=w/src['sourcePDF']
assert pdf.stat().st_size==src['sourceBytes']==11089308 and sha(pdf)==src['sourceSHA256']=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
request=next(x for x in read(r/'research/liuyao-foundations/REQUESTS.json')['records']if x['file']==pdf.name)
assert request['status']==200 and request['tls']['authorized'] and request['sha256']==src['sourceSHA256']
assert [x['pdfPage']for x in src['images']]==list(range(301,325))
for x in src['images']+src['extraQA']:
 p=w/x['file'];assert x['actuallyViewed']and sha(p)==x['sha256']and Image.open(p).size==tuple(x['size'])
assert src['expandedPriorTOCPositions']==[17]and len(src['extraQA'])==3
ids=read(b/'PROMOTION_IDENTITIES.json');assert len(ids['records'])==33
for x in ids['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
rel=ids['referenceImportRelocation'];old=w/rel['stagedFile'];new=w/rel['promotedFile']
assert sha(old)==rel['stagedSHA256']and sha(new)==rel['promotedSHA256']
old_text=old.read_text(encoding='utf-8');assert old_text.count(rel['oldImport'])==1
assert old_text.replace(rel['oldImport'],rel['newImport'])==new.read_text(encoding='utf-8')
renderer=shutil.which('pdftoppm');assert renderer
reproductions=[]
for page,dpi,expected in[(313,144,b/'images/zengshan-313.png'),(17,240,q/'toc-017-240.png')]:
 prefix=q/f'redecode-{page}-{dpi}'
 subprocess.run([renderer,'-r',str(dpi),'-f',str(page),'-l',str(page),'-singlefile','-png',str(pdf),str(prefix)],check=True,capture_output=True)
 actual=prefix.with_suffix('.png');a=Image.open(actual).convert('RGB');e=Image.open(expected).convert('RGB');assert a.size==e.size and a.tobytes()==e.tobytes()
 reproductions.append({'sourcePage':page,'dpi':dpi,'file':actual.relative_to(w).as_posix(),'sha256':sha(actual),'pixelMatch':True,'notNewSourcePosition':True})
units=read(b/'B02_CURRENT_UNITS.json');old_units=read(r/'research/liuyao-exam-intent/B02_CURRENT_UNITS.json');audit=read(b/'NUMBERING_AUDIT.json');manual=read(b/'MANUAL_READINGS.json');reference=read(b/'COMMODITY_BOUNDARY.json')
assert len(old_units['units'])==136 and len(units['units'])==137
assert units['currentCounts']=={'registeredUnits':137,'regularNumberedUnits':130,'supplements':7,'headingOnlyBodyUnits':47,'partialFoundationUnits':7,'otherPartialUnits':1,'firstPassCompleteSpanUnits':82,'wholeUnitsApplied':0}
assert next(x for x in old_units['units']if x['id']=='B02-ch082')['normalizedHeading']=='行險求財'
assert [(x['id'],x['normalizedHeading'])for x in units['units']if x['printedNumber']==81]==[('B02-ch081','請會搖會'),('B02-ch081-supp-a','行險求財')]
assert next(x for x in units['units']if x['id']=='B02-ch082')['normalizedHeading']=='婚姻'
assert next(x for x in units['units']if x['id']=='B02-ch075')['normalizedHeading']=='往何方買賣'
assert next(x for x in units['units']if x['id']=='B02-ch073')['tocBodyHeadingDifference']=={'toc':'買貨賣貨','body':'囤貨賣貨','sourcePositions':[17,308],'notSilentlyUnified':True}
assert audit['historicalMapsRetained']and all(not x['sourceEmended']for x in audit['corrections'])
assert len(manual['chapterRanges'])==16 and not manual['chapter83']['wholeFirstPassRead']and manual['chapter83']['nextPDFPage']==325
assert reference['authorCritique']['automaticCommodityInferenceRejected']and reference['翠毛NotSilentlyNormalizedToModernJadeLabel翡翠']
result=read(q/'RESULTS.json');assert len(result['checks'])==5 and all(x['ok']for x in result['checks'])
assert result['summary']['actualHHCHexCalls']==1 and result['summary']['sourceKinBranchLabels']==6
out={'date':'2026-10-28','sourcePDFSHA256':src['sourceSHA256'],'retainedHTTP200AndTLSVerified':True,'sourceImageHashesVerified':24,'expandedPriorTOCPositions':1,'highResolutionQARendersViewed':3,
 'pixelReproductions':reproductions,'promotionIdentityHashesVerified':33,'referenceBodyIdenticalExceptImportPath':True,
 'workingRegisteredUnitsBefore':136,'workingRegisteredUnitsAfter':137,'regularNumberedUnits':130,'supplements':7,'firstPassSpansAdded':16,'firstPassSpansCurrent':82,'remainingHeadingOnlyUnits':47,'partialFoundationUnits':7,'otherPartialUnits':1,
 'sourceTOCNumberingDispositionsCorrected':1,'workingTitleTranscriptionCorrections':1,'tocBodyTitleDifferencesRetained':1,
 'commodityInferenceRejectedByNamedAuthor':True,'chapter83Partial':True,'sourceEmended':False,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,
 'allImageCharactersCollated':False,'fullConditionalRulesEncoded':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items()if k!='pixelReproductions'},ensure_ascii=False))
