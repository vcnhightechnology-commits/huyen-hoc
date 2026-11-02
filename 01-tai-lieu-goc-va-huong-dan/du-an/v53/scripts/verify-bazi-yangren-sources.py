from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,re

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-yangren-conditions';q=r/'qa/bazi-yangren-conditions'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
s=read(b/'SOURCE_MANIFEST.json');assert sha(w/s['sourceContainer'])==s['sourceSHA256']and(w/s['sourceContainer']).stat().st_size==s['sourceBytes']
assert sha(w/s['retainedDigitalSource'])==s['digitalSHA256']and sha(w/s['decoder'])==s['decoderSHA256']
assert len(s['nativeImages'])==21 and[ x['containerPage']for x in s['nativeImages']]==list(range(198,219))
for x in s['nativeImages']:
 p=w/x['file'];assert sha(p)==x['sha256']and Image.open(p).size==tuple(x['size'])and x['actuallyViewed']
assert sum(x['targetedRereadThisPromotion']for x in s['nativeImages'])==8
renders=read(b/'LOCAL_RENDERS.json');assert len(renders['records'])==13
for x in renders['records']:
 p=b/x['file'];im=Image.open(p).convert('RGBA');assert sha(p)==x['sha256']and sha256(im.tobytes()).hexdigest()==x['pixelRGBA_SHA256']
crops=read(b/'PAIR_DETAIL_CROPS.json')
for x in crops['records']:
 p=w/x['source'];assert sha(p)==x['sourceSHA256'];a=Image.open(p).crop(x['box']);e=Image.open(q/x['file']);assert a.size==e.size and a.tobytes()==e.tobytes()and x['actuallyViewed']and sha(q/x['file'])==x['sha256']
raw=(b/'RETAINED_DIGITAL_SECTION.txt').read_text(encoding='utf-8');digital=(w/s['retainedDigitalSource']).read_text(encoding='utf-8');assert raw==digital[digital.index('論陽刃'):digital.index('論建禄',digital.index('論陽刃'))]
normalized=re.sub(r'\s+','',re.sub(r'<pb:[^>]+>','',raw).replace('¶',''));assert normalized==(b/'NORMALIZED_DIGITAL_BODY.txt').read_text(encoding='utf-8')
contexts=read(b/'CONTEXT_REVIEW.json');assert len(normalized)==3467 and len(normalized.encode('utf-16-le'))//2==3474 and len(contexts['records'])==55
assert ''.join(x['text']for x in contexts['records'])==normalized and all(x['disposition']for x in contexts['records'])
sub=read(b/'SELECTED_SUBCONTEXTS.json');assert len(sub['subcontexts'])==59 and sub['selectedCodepoints']==1180
for x in sub['subcontexts']:assert normalized[x['digitalStartCodepoint']:x['digitalEndCodepoint']]==x['retainedDigitalText']and x['disposition']
matrix=read(b/'PREDICATE_MATRIX.json');assert len(matrix['rules'])==28 and len(matrix['factRegistry'])==61 and len(matrix['coordinateFactKeys'])==6 and not matrix['allConditionalRulesCompiled']
identities=read(b/'PROMOTION_IDENTITIES.json');assert len(identities['records'])==8
for x in identities['records']:assert sha(w/x['file'])==x['sha256'],x['file']
decode=read(q/'DECODE_RESULTS.json');assert len(decode['records'])==2 and all(x['actualNativeDecodePixelMatch']for x in decode['records'])and not decode['browserUsed']
current=read(b/'CURRENT_PATTERN_READING_MATRIX.json');yang=next(x for x in current['records']if x['section']=='論陽刃');assert yang['currentFullFirstPassSpan']['uniquePositions']==21 and not yang['currentFullFirstPassSpan']['fullConditionalClassifier']
out={'date':'2026-10-28','sourceContainerSHA256':s['sourceSHA256'],'sourceImageHashesVerified':21,'inheritedFirstReadPositionsPromoted':13,'inheritedExpandedPriorPositions':8,'currentScopeTargetedRereadPositions':8,
 'nativePNGPixelBuffersVerified':13,'redecodedNativePixelBuffersVerified':2,'inheritedExactNativeCropsVerified':2,'editorialContexts':55,'normalizedSectionCodepointsIncludingHeader':3467,'headerCodepoints':15,'bodyCodepointsExcludingHeader':3452,'normalizedSectionUTF16Units':3474,
 'selectedParentContexts':8,'selectedSubcontexts':59,'selectedCodepoints':1180,'localPredicateAudits':28,'coordinateFacts':6,'declaredOnlyFacts':55,
 'identicalTestedReferenceModules':2,'inheritedQAResultFilesPreserved':3,'promotionIdentityHashesVerified':8,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePositionsThisHeartbeat':0,
 'independentNewWitnesses':0,'sourceEmended':False,'allImageCharactersCollated':False,'fullConditionalClassifier':False,'practicalOutcomesValidated':False,'wholeCatalogueCompleted':False}
(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
