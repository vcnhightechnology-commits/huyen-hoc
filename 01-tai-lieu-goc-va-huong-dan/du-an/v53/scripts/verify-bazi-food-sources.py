from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,re,sys,ast
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-food-source';q=r/'qa/bazi-food-source'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
sources=read(b/'SOURCE_MANIFEST.json');assert len(sources['sources'])==3
for x in sources['sources']:
    p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
    if x.get('retainedRequestManifest'):
        req=next(y for y in read(w/x['retainedRequestManifest'])['records']if y.get('sha256')==x['sha256'])
        assert req['status']==200 and req['tlsAuthorized']and req['bytes']==x['bytes']
assert sources['scopeNewHTTPRequests']==sources['scopeNewOriginalContainers']==sources['scopeNewIndependentWitnesses']==0
renders=read(b/'LOCAL_RENDERS.json');assert len(renders['records'])==27
for x in renders['records']:
    p=b/x['file'];assert x['actuallyViewed']and p.stat().st_size==x['bytes']and sha(p)==x['sha256']
    image=Image.open(p).convert('RGBA');assert list(image.size)==[x['width'],x['height']]and sha256(image.tobytes()).hexdigest()==x['pixelRGBA_SHA256']
manual=read(b/'MANUAL_READINGS.json');assert len(manual['records'])==31
assert [x['containerPage']for x in manual['records']]==list(range(168,199))
assert sum(x['newSourceReadPosition']for x in manual['records'])==27 and sum(x['boundaryOnly']for x in manual['records'])==1
for x in manual['records']:assert x['actuallyViewed']and sha(w/x['file'])==x['sha256']
crops=[]
for name in ['QA_CROPS.json','EXTRA_CROPS.json']:
    for x in read(q/name)['records']:
        source=b/x['sourceFile'];p=q/x['file'];assert sha(source)==x['sourceSHA256']and sha(p)==x['sha256']
        a=Image.open(source).convert('RGBA').crop(x['box']);im=Image.open(p).convert('RGBA')
        assert x['actuallyViewed']and x['sourcePixelIdentityVerified']and a.size==im.size and a.tobytes()==im.tobytes();crops.append(x)
assert len(crops)==8
extra=read(q/'EXTRA_CROPS.json');assert extra['records'][0]['initialIntendedFocusNotInCrop']and extra['records'][-1]['file']=='daihe-middle-columns.png'
rep=read(q/'DECODE_RESULTS.json');assert len(rep['records'])==2 and rep['containerPages']==226 and not rep['browserUsed']
for x in rep['records']:
    expected=next(y for y in renders['records']if y['page']==x['page']);assert x['nativePixelMatch']and x['pixelRGBA_SHA256']==expected['pixelRGBA_SHA256']
raw=(b/'RETAINED_DIGITAL_SECTION.txt').read_text(encoding='utf-8');digital=(r/'research/four-items/sources/KR3g0042_005.txt').read_text(encoding='utf-8')
start=digital.index('　　論食神(');end=digital.index('　　　論陽刃',start);assert digital[start:end]==raw and len(raw)==6755
contexts=read(b/'CONTEXTS.json');units=read(b/'UNITS.json');assert contexts['contextCount']==len(contexts['records'])==90 and len(units['units'])==11
assert contexts['retainedSectionSHA256']==sha(b/'RETAINED_DIGITAL_SECTION.txt')and contexts['cleanCodepoints']==5307
assert contexts['decodedTextSHA256AfterUniversalNewlines']==sha256(raw.encode()).hexdigest()and contexts['rawUTF8DecodedCodepointsIncludingCRLF']==7050 and contexts['decodedCodepointsAfterUniversalNewlines']==6755
for u in units['units']:
    text=re.sub(r'<pb:KR3g0042_WYG_005-\d+[ab]>','',raw[u['digitalStartCodepoint']:u['digitalEndCodepoint']]);text=''.join(c for c in text if c!='¶'and not c.isspace())
    rows=[x for x in contexts['records']if x['unit']==u['id']];assert ''.join(x['text']for x in rows)==text
    assert rows[0]['startCleanCodepoint']==0 and rows[-1]['endCleanCodepoint']==len(text)
    for x,y in zip(rows,rows[1:]):assert x['endCleanCodepoint']==y['startCleanCodepoint']
    for x in rows:assert x['firstPassRead']and not x['allCharactersImageCollated']and not x['fullConditionalRuleEncoded']and not x['consumerApplied']
    assert u['digitalFirstPassRead']and u['retainedImageSpanActuallyRead']and not u['entireUnitApplied']
assert sum(len(x['text'])for x in contexts['records'])==5307
gap=read(b/'CONTINUITY_AUDIT.json');assert gap['lastBeforeGap']['containerPage']==188 and gap['firstAfterGap']['containerPage']==189 and gap['firstAfterGap']['printedFolioNumeral']=='九十六'
assert gap['correspondingDigitalFoliosNotBetweenTheseRetainedImages']==['005-94a','005-94b','005-95a','005-95b']and not gap['missingAnywhereInEntireContainerEstablished']and gap['noSilentInterpolation']
assert {u['heading']for u in units['units']if u['sourceImageContinuityGap']}=={'飛天禄馬','倒衝禄'}
tables=read(b/'SOURCE_COORDINATES.json');assert tables['fuxing']['explicitAnchor']=='year'and tables['fuxing']['sourceExcludesDayAnchor']and len(tables['daihe']['rows'])==6 and len(tables['hongluan']['rows'])==4 and len(tables['mochi']['furtherRows'])==6
assert tables['daihe']['localVariant']['digital'].startswith('巳')and tables['daihe']['localVariant']['imageWorkingReading'].startswith('己')and tables['mochi']['firstTwoTargetsAndOrNotAdjudicated']
probe=read(q/'SOURCE_EXAMPLES_PROBE.json');tests=read(q/'SPECIAL_FOOD_RESULTS.json');assert len(tests['checks'])==6 and all(x['ok']for x in tests['checks'])
assert probe['actualLunarSearchCharts']==57 and probe['actualLunarForwardCharts']==probe['actualHHCBaziCalls']==2
assert probe['engineSHA256']==sha(r/'engine.js')=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6'
expected=[['甲戌','庚午','戊辰','庚申'],['丁酉','甲辰','癸酉','庚申']]
for x,p in zip(probe['records'],expected):assert x['actualHHCPillars']==x['actualLunarPillars']==x['expectedSourcePillars']==p and not x['historicalBirthDateAttributed']and not x['sourceOutcomeValidated']
assert read(w/'v46/node_modules/lunar-typescript/package.json')['version']=='1.8.6'
audit=read(q/'EXECUTION_AUDIT.json');assert audit['priorPassingChecksSupersededNotAdditional']==6 and audit['engineReexecutionsFromTestRerun']==0
ids=read(b/'PROMOTION_IDENTITIES.json');assert len(ids['records'])==58
for x in ids['records']:
    p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
assert sha(b/'special-food-reference.mjs')==next(x['sha256']for x in ids['records']if x['file']=='v53/research/bazi-food-source/special-food-reference.mjs')
staged=read(b/'STAGED_MANUAL_READINGS.json')
for x in staged['records']:x['file']=x['file'].replace('tmp/bazi-food-source-staging/','v53/research/bazi-food-source/')
assert staged==manual
for p in [Path(__file__),r/'scripts/record-bazi-food-source.py']:
    ast.parse(p.read_text(encoding='utf-8'))
out={'date':'2026-10-28','retainedOriginalContainersSHA256AndTLSVerified':1,'retainedDecoderSHA256AndTLSVerified':1,'retainedDigitalSourceSHA256Verified':1,'sourceContainerPositions':226,'sourcePositionsFirstPassReviewed':31,'foodSectionAvailablePositionsReviewed':30,'newFirstReadPositions':27,'newFirstReadBoundaryOnlyPositions':1,'priorReadPositionsExpanded':4,'newNativePNGDerivativesPixelVerified':27,'sourceCropsViewedAndPixelVerified':8,'initialMisTargetedCropRetainedAndCorrected':True,'nativeDecoderReproductionsVerified':2,'digitalUnitsFirstPassRead':11,'editorialContexts':90,'cleanDigitalCodepointsAssignedExactlyOnce':5307,'allImageCharactersCollated':False,'continuityGapFoliosUnfilled':4,'missingAnywhereInEntireContainerEstablished':False,'promotionIdentityHashesVerified':58,'referenceModuleByteIdenticalToStaging':True,'passingChecks':6,'prior6ChecksSupersededNotAdditional':True,'actualHHCBaziCalls':2,'actualLunarForwardCharts':2,'actualLunarBoundedSearchCharts':57,'testRerunEngineExecutions':0,'printedExampleChartsModernFeasibilityNotHistoricalAttribution':True,'fullConditionalCompiler':False,'fullStrengthOrEffectiveVirtualCombinationMethod':False,'sourceOutcomesValidated':False,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'consumerChanged':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
