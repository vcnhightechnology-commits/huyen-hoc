from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
b=Path(__file__).resolve().parent;w=b.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ctx=read(b/'RETAINED_CONTEXT.json');assert sha256((w/ctx['file']).read_bytes()).hexdigest()==ctx['sha256']
partition=read(b/'CLAUSE_PARTITION.json');assert len(partition['records'])==10 and ''.join(x['digitalText']for x in partition['records'])==ctx['context']['text']and len(ctx['context']['text'])==213
for x in partition['records']:
 a,z=x['localCodepointOffsets'];assert ctx['context']['text'][a:z]==x['digitalText']
 assert x['globalCleanCodepointOffsets']==[ctx['context']['startCleanCodepoint']+a,ctx['context']['startCleanCodepoint']+z]
qa=read(b/'QA_IMAGES.json');assert len(qa['records'])==4
for x in qa['records']:
 src=w/x['sourceFile'];p=b/x['file'];assert x['actuallyViewed']and not x['resampled']and sha256(p.read_bytes()).hexdigest()==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None
res=read(b/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])and res['ternaryContexts']==162
assert len(res['relationRecords'])==8 and len({(x['editorialRecipientStem'],x['owlActorStem'])for x in res['relationRecords']})==7
save('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',sourceParentContext='FOOD-00-C15',contextCodepoints=213,digitalPartitionUnits=10,selectedExceptionRecords=8,
 directNativeReviewPositions=[175,176],nativeCropsViewedPixelMatched=4,newSourcePositions=0,newHTTPRequests=0,newContainers=0,
 sourceTextLayers=dict(originalCorpusRetainedUnchanged=True,manualNativeSelectedReadingsNotWholeGlyphCollation=True,canonicalStemRoleReadingsExplicit=True),
 unresolved=dict(namedPillarDayOrOtherAnchor=True,effectiveCombinationOrSupport=True,luClause土Versus壬=True,guiClauseFinalBranchGlyph=True,jiXinVersusXinDingPriority=True),
 disposition='Bounded research premise audit; all true research premises are explicit declarations, not validated birth-chart facts.',
 noBlanketOwlRule=True,noRelationRemapping=True,sourceFullClausesApplied=False,sourceOutcomesValidated=False,consumerApplied=False,
 testExecutionAudit=dict(finalCompleteChecks=5,finalHHCTenGodQueries=8,uniqueRecipientOwlPairs=7,finalLunarHiddenTableQueries=4,finalLunarCombinationTableQueries=4,
 firstFailedRun=read(b/'TEST_FAILURE_AUDIT.json'),allRunsHHCTenGodQueries=16,allRunsLunarHiddenTableQueries=8,allRunsLunarCombinationTableQueries=8,doNotTreatRerunAsIndependentEvidence=True)))
summary='ThựcThần C15:chiađúng213codepoint thành10đơnvị/8mệnhđềngoạilệ;giữ8phạmvicâu/4trụđượcnêu/cácvaiđảo己不倒食辛và庚不倒食壬. Ảnh175–176/crop4đãxemkhớppixel,土祿在亥khácbảnsố壬禄在亥vàchữcuốicâu癸貴chưachốt.5kiểmcuối/162ngữcảnhbagiátrị;8truyvấnhàmThậpthầnHHCthật(7cặpkhácnhau)/4bảngtàngcan+4bảnghợpcanlunar. Đúngcặp/tàngcankhôngtựxáclậphợphóa;khunglá sốkhôngđượcnhậngiảlàvaiđãchứngminh. Lỗisốkiểmkỳvọng135sửa162,auditgiữlầnnàygọi8+4+4trướcchạylạikhôngcộngthànhchứngcứmới. C15lànhómthứ10chọnmộtphần,còn80/90vàmọimệnhđềphụ;0HTTP/vịtrínguồnmới/webđổi,toànkhoactive.'
nexts=['C15cònphầnluậnchungvàsáuTân/hợp-hóa/đờivịtrụ,haiđiểmchữvàưu tiên己不倒食辛với辛有丁chưaxáclập.Khôngtựkếthừakhungnhậtcanhoặcđảotoànbộquan hệThậpThần.',
 'Mười ngữcảnhmớichọntừngmệnhđề,80nhómkhácvàmọitiềnđềphụchưaáp.Phầntưsự2bảng32/26/380v360,mùavụ夏水因,khí lực/toàncách vẫn mở;khônglặpkiểmđãđạt.',
 'Tiếpphầnđộclậpcótiềnđềđủ:ThựcThầncácvận/hợptàng,hoặcNhàở/Tửvi/Dịch.Nhàở69ô64khớp5mờ/交門換象初爻,童限火鈴CanhNhâm/khởihạn,B02/B03/MaiHoacònmở.Nghiêncứu/QAngoàisite;UIKiếnLộcchờbrowserQAkhảdụng,khôngvượtsetting/khôngxuấtbản.']
state=read(b/'WORK_STATE.json');state.update(status='C15eight-source-exception-premise-audits-verified-full-method-open',sourceDirectory='v53/research/bazi-food-owl-exceptions',latestReport='v53/BAZI_FOOD_OWL_EXCEPTIONS_REPORT.md',completedStep=summary,next=nexts,
 noExceptionEngineImplemented=False,fullNatalExceptionClassifierImplemented=False,passingFinalRuntimeChecks=5,sourceContextCodepoints=213,contextUnits=10,selectedExceptionRecords=8,
 ternaryContexts=162,actualHHCTenGodQueries=8,uniqueRecipientOwlPairs=7,actualLunarHiddenStemTableQueries=4,actualLunarCombinationTableQueries=4,newCalendarChartCalls=0,
 selectedParentContextsAcrossFoodScopes=10,otherParentContextsNotSelected=80,allSelectedParentsSubsidiaryClausesApplied=False,sourceBirthChartAnchorEstablished=False,consumerChanged=False,wholeCatalogueCompleted=False)
state.pop('passedRuntimeChecks',None)
save('WORK_STATE.json',state)
print('VerifiedC15partition/eightexceptions/5finalchecks/162ternarycontexts;fullconditionsopen')
