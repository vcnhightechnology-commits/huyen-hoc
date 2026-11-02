from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
s=Path(__file__).resolve().parent;w=s.parent.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
d=read(s/'EXTRA_CROPS.json')
d['records'][0]['initialIntendedFocusNotInCrop']=True
d['records'][0]['actualFocus']='同窠倒食example甲子年見壬子時,not帶合己glyph;misleadingfilenamepreservedinaudit'
p=s/'daihe-middle-columns.png'
d['records'].append({'page':192,'sourceFile':'p192.png','sourceSHA256':sha256((s/'p192.png').read_bytes()).hexdigest(),'file':p.name,'sha256':sha256(p.read_bytes()).hexdigest(),'box':[970,300,1420,2900],'nativeNoResize':True,'actuallyViewed':True,'actualFocus':'帶合己人見辛有丙合;localimageworkingreading己,digitalraw巳'})
for x in d['records']:
    a=Image.open(s/x['sourceFile']).convert('RGBA').crop(x['box']);b=Image.open(s/x['file']).convert('RGBA')
    assert a.size==b.size and a.tobytes()==b.tobytes()
    x.update(actuallyViewed=True,sourcePixelIdentityVerified=True)
write(s/'EXTRA_CROPS.json',d)
coordinate_tables={
 'date':'2026-10-28','basis':'Manually bounded source coordinates. Not a unified full-pattern classifier. No hidden-stem,anchor,calendar,logical-operator or effective-combination premises invented.',
 'fuxing':{'containerPage':191,'explicitAnchor':'year','explicitExamplesOnly':[{'yearStem':'甲','targetPillars':['丙寅','丙子']},{'yearStem':'乙','targetPillars':['丁亥','丁丑']}],'otherEightStemRowsDirectlyPrintedHere':False,'sourceExcludesDayAnchor':True,'fullMethodEncoded':False},
 'tongke':{'containerPages':[191,192],'sourceCountLiteral':'十三位','explicitExample':['甲子','丙子'],'generalModulo60Step12IsAnEditorialInferenceNotDirect60PrintedRows':True,'globalAnchorAssigned':False,'fullMethodEncoded':False},
 'daihe':{'containerPage':192,'rows':[['甲','丙','辛'],['己','辛','丙'],['乙','丁','壬'],['庚','壬','丁'],['丙','戊','癸'],['辛','癸','戊']],'rowRoles':['sourceStemNotAutomaticallyYearOrDay','foodStem','combiningStem'],'localVariant':{'digital':'巳人見辛有丙合','imageWorkingReading':'己人見辛有丙合','crop':'daihe-middle-columns.png','notGlobalReplacement':True},'effectiveCombinationEncoded':False},
 'hongluan':{'containerPages':[195,196],'rows':[['丙','戊戌'],['辛','癸丑'],['壬','甲辰'],['乙','丁未']],'targetPositionsLiteral':'日時','sourceAnchorPositionAssigned':False,'fullMethodEncoded':False},
 'mochi':{'containerPage':196,'firstExamplePillars':['辛巳','壬辰','癸巳','癸亥'],'firstSourcePair':['辛巳',['癸巳','癸亥']],'firstTwoTargetsAndOrNotAdjudicated':True,'furtherRows':[['丙寅','戊寅'],['戊申','庚申'],['己巳','辛亥'],['庚午','壬申'],['甲戌','丙寅'],['壬辰','甲申']],'globalAnchorPositionAssigned':False,'fullMethodEncoded':False},
 'noSourceWealthRankHealthFamilyOrLongevityOutcomeValidated':True,'consumerApplied':False}
write(s/'SOURCE_COORDINATES.json',coordinate_tables)
raw=w/'v53/research/bazi-pattern-witness/CADAL06066041.djvu';digital=w/'v53/research/four-items/sources/KR3g0042_005.txt';decoder=w/'v53/research/bazi-pattern-extension/tooling/djvu.js'
sources=[]
for p,reqp in[(raw,w/'v53/research/bazi-pattern-witness/REQUESTS.json'),(decoder,w/'v53/research/bazi-pattern-extension/tooling/REQUESTS.json')]:
    digest=sha256(p.read_bytes()).hexdigest();rows=read(reqp)['records'];http=next(x for x in rows if x.get('sha256')==digest)
    assert http['status']==200 and http['tlsAuthorized']and http['bytes']==p.stat().st_size
    sources.append({'file':p.relative_to(w).as_posix(),'bytes':p.stat().st_size,'sha256':digest,'retainedRequestManifest':reqp.relative_to(w).as_posix(),'retainedHTTP200AndTLSAuthorized':True,'newHTTPThisScope':False})
sources.append({'file':digital.relative_to(w).as_posix(),'bytes':digital.stat().st_size,'sha256':sha256(digital.read_bytes()).hexdigest(),'kind':'retained-pinned-digital-transcription;notindependentimagewitness'})
write(s/'SOURCE_MANIFEST.json',{'date':'2026-10-28','sources':sources,'retainedSectionCodepointsIncludingMarkup':6755,'retainedSectionSHA256':sha256((s/'RETAINED_DIGITAL_SECTION.txt').read_bytes()).hexdigest(),'scopeNewHTTPRequests':0,'scopeNewOriginalContainers':0,'scopeNewIndependentWitnesses':0,'sourceContainerPositions':226,'firstPassRetainedPositionsViewed':31,'newFirstReadPositions':27,'boundaryOnlyNewPosition':168,'foodSectionPositionsAvailableAndReviewed':30,'priorReadPositionsExpanded':[169,170,171,198],'newNativePNGDerivatives':27,'newSourceDownloads':0,'manualContextGroups':90,'contextCleanCodepoints':5307,'imageContinuityGapFolios':['005-94a','005-94b','005-95a','005-95b'],'gapMissingAnywhereInContainerEstablished':False,'digitalAndImageSameWYGFamilyNotIndependent':True,'imageGlyphsNotGloballyNormalized':True,'allImageCharactersCollated':False,'wholeWorkApplied':False})
d=read(s/'WORK_STATE.json');d['status']='retained-span-and90contexts-firstpass-read-two-private-coordinate-systems-verified-full-conditions-active'
d.pop('attachedSubsectionsNotYetAllImageRead',None)
d['allAvailableAttachedSubsectionPositionsFirstPassRead']=[184,198]
d['notes']=[n for n in d['notes']if not n.startswith('Readremaining187')]
d.update(currentFunctionalComponent='special-food-reference.mjs',manualContextGroups=90,contextCleanCodepoints=5307,passingChecks=6,actualHHCBaziCalls=2,actualLunarForwardCharts=2,actualLunarBoundedSearchCharts=57,nativeCropsViewedAndPixelVerified=8,nativePixelReproductions=2,sourceCoordinates='SOURCE_COORDINATES.json',privateCoordinateSystems=['TMTH005-zhuanshi','TMTH005-zhuanyin'],sourceExamplesHistoricalBirthDatesValidated=False)
d['notes']+=['SixchecksrerunonlyafterfixingrawscancompletenesstothetwoactualyearmonthpositionsandrenamingwrongPDFfieldtoContainerPage;prior6resultpreserved.0enginecallsrerunbytests;do notcount12checks.','Oneinitialcropmis-targeted同窠ratherthan帶合己;recordedandretained,correctedcropactuallyviewed.8totalcropsincludeit.','90contextscover5307cleanretaineddigitalcodepointswithnoomissionsafterexplicitPB/paragraph/whitespaceremoval.Paragraphsmaycontainmultipleclauses;not90completeatomicrules.']
d['next']=['Complete selectedsource-specific strength/virtual-combination/prioritypremises andcounterexamples;two coordinate systems do not establishwholepatterns.','Extract subsidiaryclausesof90contexts,includingmultiplequotedpoemvoices.5other source-coordinatecollections retained but not fullfunctions.','Resolveexactimage94a–95bgap byavailableparallelwitnessorwholecontainerlocator;do notretakeoldbytesorinfermissingimagesfromtext.','Other9majorBazi-patternsections fullconditionalrulesremainactive;do notcallthis wholevolumeexhausted.','ContinueTuvi/Home/Yiindependentopenbrancheswhenonewitnessrouteblocked;consumer candidate remains private whilebrowserQAunavailable.']
write(s/'WORK_STATE.json',d)
write(s/'EXECUTION_AUDIT.json',{'date':'2026-10-28','passingChecksCurrent':6,'priorPassingChecksSupersededNotAdditional':6,'reasonForRerun':'ActualprivateAPIchange:yearmonthscopecompletenessandDjVuContainerPagefieldfix. Addedunknown-day/hourandunknown-scoped-positionassertions.','engineReexecutionsFromTestRerun':0,'actualCompletedEngineProbe':{'HHC':2,'lunarForward':2,'lunarBoundedSearch':57},'historicalBirthDateAttribution':False,'consumerDefectFound':False,'initialCropTargetMissedAndCorrected':True,'nativeCropFilesViewed':8,'browserUsed':False,'wholeCatalogueComplete':False})
print(json.dumps({'sourceFiles':len(sources),'contexts':90,'cleanCodepoints':5307,'passingChecks':6,'HHCCalls':2,'lunarForward':2,'lunarBoundedSearch':57,'cropsViewed':8,'reproductions':2}))
