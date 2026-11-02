from pathlib import Path
from hashlib import sha256
from collections import Counter
import json,subprocess,shutil
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-exam-intent';q=r/'qa/liuyao-exam-intent'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
src=read(b/'SOURCE_MANIFEST.json');pdf=w/src['sourcePDF']
assert pdf.stat().st_size==src['sourceBytes']==11089308 and sha(pdf)==src['sourceSHA256']=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
request=next(x for x in read(r/'research/liuyao-foundations/REQUESTS.json')['records'] if x['file']==pdf.name)
assert request['status']==200 and request['tls']['authorized'] and request['sha256']==src['sourceSHA256'] and request['bytes']==pdf.stat().st_size
assert [x['pdfPage']for x in src['images']]==list(range(264,301))
for x in src['images']+src['extraQA']:
 p=w/x['file'];assert x['actuallyViewed'] and sha(p)==x['sha256'] and Image.open(p).size==tuple(x['size'])
assert [x['sourcePage']for x in src['extraQA']]==[271,292,296]
assert src['nonRuleLeaves']==[286,287,288] and src['contentPositionsActuallyViewed']==34

ids=read(b/'PROMOTION_IDENTITIES.json')
for x in ids['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes'] and sha(p)==x['sha256']
relocation=ids['referenceImportRelocation'];old=w/relocation['stagedFile'];new=w/relocation['promotedFile']
assert sha(old)==relocation['stagedSHA256'] and sha(new)==relocation['promotedSHA256']
old_text=old.read_text(encoding='utf-8');new_text=new.read_text(encoding='utf-8')
assert old_text.count(relocation['oldImport'])==1 and new_text.count(relocation['newImport'])==1
assert old_text.replace(relocation['oldImport'],relocation['newImport'])==new_text
rel=ids['unitMapEvidenceRelocation'];units_text=(b/'STAGED_UNITS.json').read_text(encoding='utf-8')
assert units_text.count(rel['oldEvidence'])==rel['replacements']==19
assert units_text.replace(rel['oldEvidence'],rel['newEvidence'])==(b/'B02_CURRENT_UNITS.json').read_text(encoding='utf-8')
assert sha(b/'B02_CURRENT_UNITS.json')==rel['promotedSHA256']

renderer=shutil.which('pdftoppm');assert renderer
reproductions=[]
for page,dpi,expected in [(271,144,b/'images/zengshan-271.png'),(296,360,q/'qa360-296.png')]:
 prefix=q/f'redecode-{page}-{dpi}'
 subprocess.run([renderer,'-r',str(dpi),'-f',str(page),'-l',str(page),'-singlefile','-png',str(pdf),str(prefix)],check=True,capture_output=True)
 actual=prefix.with_suffix('.png');a=Image.open(actual).convert('RGB');e=Image.open(expected).convert('RGB')
 assert a.size==e.size and a.tobytes()==e.tobytes()
 reproductions.append({'pdfPage':page,'dpi':dpi,'file':actual.relative_to(w).as_posix(),'sha256':sha(actual),'pixelMatch':True,'notNewSourcePosition':True})

manual=read(b/'MANUAL_READINGS.json');units=read(b/'B02_CURRENT_UNITS.json');old_units=read(r/'research/liuyao-family-study/B02_CURRENT_UNITS.json')
assert len(manual['chapterRanges'])==19 and manual['inheritedOpeningPage']['pdfPage']==263 and manual['inheritedOpeningPage']['notRereadThisScope']
assert sha(w/manual['inheritedOpeningPage']['file'])==next(x['sha256']for x in read(r/'research/liuyao-family-study/MANUAL_READINGS.json')['records'] if x['pdfPage']==263)
assert units['currentCounts']=={'registeredUnits':136,'regularNumberedUnits':130,'supplements':6,'headingOnlyBodyUnits':62,'partialFoundationUnits':7,'otherPartialUnits':1,'firstPassCompleteSpanUnits':66,'wholeUnitsApplied':0}
assert old_units['currentCounts']['firstPassCompleteSpanUnits']==47 and old_units['currentCounts']['headingOnlyBodyUnits']==81
assert len(units['units'])==136 and all(not x['entireUnitApplied']for x in units['units'])
assert [(x['id'],x['printedNumber'])for x in units['units']if x['printedNumber']==55]==[('B02-ch055',55),('B02-ch055-supp-a',55)]
assert next(x for x in units['units']if x['id']=='B02-ch068')['nextPDFPage']==301
assert len(read(b/'BOUNDED_CLAUSES.json')['clauses'])==31 and len(read(b/'SOURCE_CONTEXTS.json')['methods'])==19
result=read(q/'RESULTS.json');assert len(result['checks'])==8 and all(x['ok']for x in result['checks'])
assert result['summary']['actualHHCHexCalls']==2 and result['summary']['listedPetitionIntentsNotEncoded']==5 and result['summary']['explicitMissingScopeCases']==58
fixture=read(b/'PRINTED_FIXTURE.json');assert fixture['sourceSelfLine']==2 and fixture['sourceResponseLine']==5 and not fixture['sourceChangedKinPrinted']
out={'date':'2026-10-28','sourcePDFSHA256':src['sourceSHA256'],'originalRetainedHTTP200AndTLSVerified':True,
 'sourceImageHashesVerified':37,'firstReadContentPositions':34,'nonRuleLeaves':3,'highResolutionQAViewed':3,'pixelReproductions':reproductions,
 'promotionIdentityHashesVerified':len(ids['records']),'referenceBodyIdenticalExceptImportPath':True,'unitMapEvidenceOnlyRelocated':19,
 'firstPassSpansAdded':19,'firstPassSpansCurrent':66,'remainingHeadingOnlyUnits':62,'partialFoundationUnits':7,'otherPartialUnits':1,
 'boundedSourceClauses':31,'namedSourceContexts':19,'listedPetitionIntentsNotEncoded':5,'explicitMissingScopeCases':58,
 'inheritedOpeningPageNotNewRead':263,'chapter68Partial':True,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,
 'wholeImageCharactersCollated':False,'fullConditionalRulesEncoded':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items()if k!='pixelReproductions'},ensure_ascii=False))
