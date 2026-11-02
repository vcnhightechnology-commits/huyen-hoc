from pathlib import Path
from hashlib import sha256
import json,subprocess,shutil
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-life-context';q=r/'qa/liuyao-life-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
src=read(b/'SOURCE_MANIFEST.json');source=w/src['sourcePDF'];manual=read(b/'MANUAL_READINGS.json')
assert source.stat().st_size==src['sourceBytes']==11089308 and sha(source)==src['sourceSHA256']
assert len(src['images'])==20 and [x['pdfPage']for x in src['images']]==list(range(213,233))
for x in src['images']:
 p=w/x['file'];assert sha(p)==x['sha256']and Image.open(p).size==tuple(x['size'])and x['actuallyViewed']
assert sum(x['newlyRenderedThisStage']for x in src['images'])==12 and sum(x['previouslyRenderedButUnread']for x in src['images'])==7
renderer=shutil.which('pdftoppm');assert renderer
expected144=w/next(x for x in src['images']if x['pdfPage']==215)['file'];expected360=q/'qa360-215.png'
reproductions=[]
for dpi,expected in[(144,expected144),(360,expected360)]:
 subprocess.run([renderer,'-r',str(dpi),'-f','215','-l','215','-png',str(source),str(q/f'redecode-{dpi}')],check=True,capture_output=True)
 actual=q/f'redecode-{dpi}-215.png';a=Image.open(actual).convert('RGB');e=Image.open(expected).convert('RGB');assert a.size==e.size and a.tobytes()==e.tobytes()
 reproductions.append({'file':actual.name,'sourcePage':215,'dpi':dpi,'sha256':sha(actual),'pixelMatch':True,'notNewSourcePosition':True})
contexts=read(b/'SOURCE_CONTEXTS.json');assert len(contexts['methods'])==2 and len(contexts['separateQuestionSource']['focusCategories'])==7
fixture=read(b/'PRINTED_FIXTURES.json')['fixtures'][0];assert fixture['sourcePDFPage']==215 and fixture['sourceProse']=='獨嫌酉金福神破而化絕'and not fixture['sourceOutcomeValidated']
assert len(read(b/'BOUNDED_CLAUSES.json')['clauses'])==20 and not read(b/'BOUNDED_CLAUSES.json')['allSubsidiaryClausesEnumerated']
units=read(b/'B02_CURRENT_UNITS.json');assert units['currentCounts']['wholeUnitsApplied']==0 and len(units['units'])==136
assert len([x for x in units['units']if x['disposition']=='heading-only-body-extraction-open'])==92
out={'date':'2026-10-27','sourcePDFSHA256':src['sourceSHA256'],'sourceImageHashesVerified':20,'stagedPositionsPromoted':20,'firstReadPositionsNewToRelease':19,'alreadyIntegratedPositionExpanded':1,
 'sourceReadingCountsBasis':'Firstpasspositions inheritedfromtmp staging;thisheartbeat reread targeted213/214/215/229. Not19newdownloadsornewreadingsclaimedforthisheartbeat.',
 'inheritedNewlyRenderedPositions':12,'inheritedRetainedRendersRead':7,'newHighResolutionQARenders':1,'highResolutionQAViewed':True,'highResolutionQASHA256':sha(expected360),
 'pixelReproductions':reproductions,'completeFirstPassSpans':3,'chapter39OpeningOnly':True,'newHTTPRequests':0,'newOriginalContainers':0,
 'allSourceImageCharactersCollated':False,'sourceOutcomesValidated':False,'wholeChaptersApplied':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items()if k!='pixelReproductions'},ensure_ascii=False))
