from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,sys
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-combination-context';q=r/'qa/liuyao-combination-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
pdf=r/'research/liuyao-foundations/NLC416-12jh005345-45344.pdf';assert pdf.stat().st_size==11089308 and sha(pdf)=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
req=next(x for x in read(r/'research/liuyao-foundations/REQUESTS.json')['records']if x['file']==pdf.name);assert req['status']==200 and req['tls']['authorized']and req['sha256']==sha(pdf)
origin,combination=read(b/'SOURCE_MANIFEST.json'),read(b/'COMBINATION_SOURCE_MANIFEST.json');images=origin['images']+combination['images'];assert[x['pdfPage']for x in images]==list(range(50,55))+list(range(73,80))
for x in images:assert x['actuallyViewed']and not x['newSourcePosition']and sha(w/x['file'])==x['sha256']
assert origin['inheritedPrintedCast']and origin['independentNewPrintedCasts']==0 and len(combination['boundedContextGroups'])==18
crops=[]
for name in['CROP.json','TRIAD_CROP.json','TRIAD_FIXTURE_CROP.json']:
 d=read(q/name);src=w/d['source'];assert sha(src)==d['sourceSHA256'];source=Image.open(src).convert('RGB')
 if name=='CROP.json':coords=[(d['cropFile'],d['cropBox'],d['cropSHA256'],d['actuallyViewed'])]
 else:coords=[(d['file'],d['box'],d['sha256'],d['actuallyViewed'])]
 if'expandedCrop'in d:
  x=d['expandedCrop'];coords.append((x['file'],x['box'],x['sha256'],x['actuallyViewed']))
 for file,box,digest,viewed in coords:
  target=q/file;a=source.crop(box);actual=Image.open(target).convert('RGB');assert viewed and sha(target)==digest and a.size==actual.size and a.tobytes()==actual.tobytes();crops.append(file)
 if'higherResolution'in d:
  x=d['higherResolution'];a=Image.open(q/x['file']).convert('RGB').crop(x['cropBox']);actual=Image.open(q/x['cropFile']).convert('RGB');assert x['cropActuallyViewed']and not x['fullQAActuallyViewed']and sha(q/x['file'])==x['sha256']and sha(q/x['cropFile'])==x['cropSHA256']and a.size==actual.size and a.tobytes()==actual.tobytes();crops.append(x['cropFile'])
  assert d['workingReadingResolved']=='一卦之內有一爻動而合局者一也'and d['semanticFirstModeStillNotAdjudicated']
assert len(crops)==6
rep=read(q/'RENDER_REPRODUCTION.json');a=Image.open(q/rep['file']).convert('RGB');e=Image.open(q/rep['targetFile']).convert('RGB');assert sha(q/rep['file'])==rep['sha256']and sha(q/rep['targetFile'])==rep['targetSHA256']and a.size==e.size and a.tobytes()==e.tobytes()
ids=read(b/'PROMOTION_IDENTITIES.json');assert len(ids['records'])==26 and len(ids['referenceImportRelocations'])==3
for x in ids['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
prefixes=[('liuyao-use-god/use-god-reference.mjs'),('liuyao-day-month/day-month-reference.mjs'),('liuyao-foundations/liuyao-reference.mjs')]
for x in ids['referenceImportRelocations']:
 a=w/x['stagedFile'];p=w/x['promotedFile'];assert sha(a)==x['stagedSHA256']and sha(p)==x['promotedSHA256'];text=a.read_text(encoding='utf-8')
 for name in prefixes:text=text.replace("from'../../v53/research/"+name+"'","from'../"+name+"'")
 assert text==p.read_text(encoding='utf-8')
results=[read(q/n)for n in['RESULTS.json','COMBINATION_RESULTS.json','TRIAD_RESULTS.json']];assert sum(len(x['checks'])for x in results)==16 and all(c['ok']for x in results for c in x['checks'])
failure=read(b/'FAILURE_AUDIT.json');assert failure['priorFailedRunSuccessfulHHCCalls']==4 and failure['reexecutionOfThose4ForCompletedCheckRunNotIndependentEvidence']
f=read(b/'TRIAD_FIXTURE.json');assert f['valuesBottomToTop']==[9,8,9,9,8,9]and len(f['primaryBranchKinBottomToTop'])==6 and len(f['changedBranchKin'])==4
assert results[0]['summary']['actualHHCHexCallsForNewExceptionProjection']==2 and results[1]['summary']['actualHHCHexCallsForNamedFigureProjections']==4 and results[2]['summary']['actualHHCHexCallsForPrinted79']==2
out={'date':'2026-10-28','retainedPDFBytesVerified':11089308,'retainedPDFSHA256':sha(pdf),'retainedHTTP200AndTLSVerified':True,'sourceImagesReviewedAndHashesVerified':12,'nativeAndHighResolutionCropsViewedAndPixelVerified':6,'fullHigherResolutionPageViewedNotClaimed':True,'pixelReproductionsVerified':1,'promotionIdentityHashesVerified':26,'referenceBodiesIdenticalExceptImportPrefixes':3,'passingChecks':16,'successfulHHCCallsInFinalPassingRuns':8,'successfulRepeatedHHCCallsInEarlierFailedSyntheticTestRun':4,'totalSuccessfulHHCCallsIncludingFailedTestRun':12,'repeatCallsNotIndependentNewEvidence':True,'sourceNamedCombinationForms':6,'sourceTriadGroups':4,'sourceTriadModesRecorded':4,'sourceFirstModeLiteral':'一爻動','sourceFirstModeAdjudicated':False,'sourcePrimary79Labels':6,'sourceChanged79Labels':4,'sourceInnerOuterCandidateGroups':2,'source51HoldVs74SupportNotSilentlyUnified':True,'newHTTPRequests':0,'newSourcePositions':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'fullFunctionalHoldClassifier':False,'fullTriadFormationModel':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
if'--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
