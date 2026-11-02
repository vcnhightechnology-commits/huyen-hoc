from pathlib import Path
from hashlib import sha256
import json,subprocess,shutil
from PIL import Image
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-closing-context';q=r/'qa/liuyao-closing-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
src=read(b/'SOURCE_MANIFEST.json');pdf=w/src['sourcePDF']
assert pdf.stat().st_size==src['sourceBytes']==11089308 and sha(pdf)==src['sourceSHA256']=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
request=next(x for x in read(r/'research/liuyao-foundations/REQUESTS.json')['records']if x['file']==pdf.name)
assert request['status']==200 and request['tls']['authorized']and request['sha256']==src['sourceSHA256']
assert [x['pdfPage']for x in src['images']]==list(range(325,395))
assert sum(x['firstReadInCurrentTurn']for x in src['images'])==44
assert src['uniqueBodyPositionsPromoted']==65 and src['allNonRuleLeavesPromoted']==[338,391,392,393,394]
assert src['expandedPriorTOCPositions']==[18,19]
for x in src['images']+src['extraQA']:
 p=w/x['file'];assert x['actuallyViewed']and sha(p)==x['sha256']and Image.open(p).size==tuple(x['size'])
assert len(src['extraQA'])==6
for name in['DETAIL_CROP.json','CHART_CROP.json']:
 crop=read(b/name);original=w/crop['source'];target=w/crop['file']
 assert sha(original)==crop['sourceSHA256']and sha(target)==crop['sha256']and crop['actuallyViewed']and crop['pixelMatch']
 image=Image.open(original).convert('RGB');actual=Image.open(target).convert('RGB');assert image.crop(crop['box']).size==actual.size and image.crop(crop['box']).tobytes()==actual.tobytes()
ids=read(b/'PROMOTION_IDENTITIES.json');assert len(ids['records'])==90 and len(ids['referenceImportRelocations'])==2
for x in ids['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
for x in ids['referenceImportRelocations']:
 old=w/x['stagedFile'];new=w/x['promotedFile'];assert sha(old)==x['stagedSHA256']and sha(new)==x['promotedSHA256']
 text=old.read_text(encoding='utf-8');assert text.count(x['oldImport'])==1 and text.replace(x['oldImport'],x['newImport'])==new.read_text(encoding='utf-8')
renderer=shutil.which('pdftoppm');assert renderer
reproductions=[]
for page,dpi,expected in[(360,144,b/'images/zengshan-360.png'),(393,360,q/'qa360-393.png'),(18,240,q/'qa240-018.png')]:
 prefix=q/f'redecode-{page}-{dpi}';subprocess.run([renderer,'-r',str(dpi),'-f',str(page),'-l',str(page),'-singlefile','-png',str(pdf),str(prefix)],check=True,capture_output=True)
 actual=prefix.with_suffix('.png');a=Image.open(actual).convert('RGB');e=Image.open(expected).convert('RGB');assert a.size==e.size and a.tobytes()==e.tobytes()
 reproductions.append({'sourcePage':page,'dpi':dpi,'file':actual.relative_to(w).as_posix(),'sha256':sha(actual),'pixelMatch':True,'notNewSourcePosition':True})
prior=read(q/'PRIOR_STAGED_SOURCE_VERIFICATION.json');assert len(prior['pixelReproductions'])==2 and all(x['pixelMatch']for x in prior['pixelReproductions'])
units=read(b/'B02_CURRENT_UNITS.json');old=read(r/'research/liuyao-commodity-boundary/B02_CURRENT_UNITS.json');first=read(b/'PRIOR_STAGED_UNITS.json')
assert old['currentCounts']['firstPassCompleteSpanUnits']==82 and first['currentCounts']['firstPassCompleteSpanUnits']==102
assert units['currentCounts']=={'registeredUnits':137,'regularNumberedUnits':130,'supplements':7,'headingOnlyBodyUnits':0,'partialFoundationUnits':7,'otherPartialUnits':0,'firstPassCompleteSpanUnits':130,'wholeUnitsApplied':0}
assert len(units['units'])==137 and all(not x['entireUnitApplied']for x in units['units'])
assert len(read(b/'TRAVELER_MANUAL_READINGS.json')['chapterRanges'])==20 and len(read(b/'CLOSING_MANUAL_READINGS.json')['chapterRanges'])==28
assert not next(x for x in units['units']if x['id']=='B02-ch100')['bodyHeadingUnresolvedReading']['resolved']
assert next(x for x in units['units']if x['id']=='B02-ch106')['tocBodyHeadingDifference']['body361']=='蓋造買宅賃宅'
assert next(x for x in units['units']if x['id']=='B02-ch110')['tocBodyHeadingDifference']['toc18']=='歸宅入火'
colophon=read(b/'COLOPHON_AUDIT.json');assert colophon['sourcePDFPage']==393 and colophon['publicationDateLiteral']=='中華民國十四年十一月出版'and colophon['distributionDateLiteral']=='中華民國十四年十一月發行'
assert colophon['calendarConversion']=={'republicYear':14,'commonEraYear':1925,'printedMonth':11,'dayUnstated':True,'monthCalendarNotFurtherInferred':True}
assert not colophon['editionIndependentlyNewWitness']and not colophon['sourceOriginalBytesChanged']
traveler=read(q/'TRAVELER_RESULTS.json');closing=read(q/'CLOSING_RESULTS.json')
assert len(traveler['checks'])==6 and len(closing['checks'])==8 and all(x['ok']for x in traveler['checks']+closing['checks'])
assert traveler['summary']['actualHHCHexCalls']==2 and closing['summary']['actualHHCHexCalls']==2
assert len(read(b/'HOUSE_CONTEXTS.json')['methods'])==13 and len(read(b/'BOUNDED_CLAUSES.json')['clauses'])==17
out={'date':'2026-10-28','sourcePDFSHA256':src['sourceSHA256'],'retainedHTTP200AndTLSVerified':True,'sourceImagesPromotedVerified':70,'priorStagingImagesPromoted':26,'newViewedSourcePositionsThisTurn':44,
 'bodyPositionsPromoted':65,'newBodyPositionsThisTurn':40,'allNonRuleLeavesPromoted':5,'currentTurnNonRuleLeaves':4,'expandedPriorTOCPositions':2,'highResolutionQAViewed':6,'nativeCropsPixelVerified':2,
 'pixelReproductions':reproductions,'inheritedPriorStagingPixelReproductions':2,'promotionIdentityHashesVerified':90,'referenceBodiesIdenticalExceptImportPaths':2,
 'newFirstPassSpansThisTurn':28,'inheritedStagingSpansPromoted':20,'firstPassSpansNewlyPackaged':48,'firstPassSpansCurrent':130,'partialFoundationUnits':7,'headingOnlyUnits':0,'wholeUnitsApplied':0,
 'namedHouseContexts':13,'boundedClosingContextGroups':17,'colophonSourcePDFPage':393,'colophonCommonEraYear':1925,'colophonPrintedMonth':11,
 'retainedTOCBodyTitleDifferencesAdded':2,'chapter100HeadingUnresolved':True,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,
 'sourceEmended':False,'allImageCharactersCollated':False,'fullConditionalRulesEncoded':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items()if k!='pixelReproductions'},ensure_ascii=False))
