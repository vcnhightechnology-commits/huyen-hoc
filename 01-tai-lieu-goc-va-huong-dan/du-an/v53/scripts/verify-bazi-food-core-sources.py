from pathlib import Path
from hashlib import sha256
import json,sys,runpy,contextlib,io
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-food-core';q=r/'qa/bazi-food-core'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
args=sys.argv[:]
try:
    sys.argv=['verify-bazi-food-sources.py','--no-write']
    with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(r/'scripts/verify-bazi-food-sources.py'))
finally:sys.argv=args
source=read(b/'SOURCE_MANIFEST.json');assert sha(w/source['sourceContextFile'])==source['sourceContextSHA256']
corpus=read(w/source['sourceCorpus']);parents={x['id']:x for x in corpus['records']};matrix=read(b/'SELECTED_PREDICATES.json')
assert len(matrix['clauses'])==12 and len(matrix['rules'])==11 and len(matrix['declaredResearchFactRegistry'])==21 and matrix['coordinateFacts']==['dayIsYang','dayIsYin']
assert len(set(x['parent']for x in matrix['clauses']))==8 and sum(len(x['text'])for x in matrix['clauses'])==135 and source['otherUnselectedParentContexts']==82
for x in matrix['clauses']:
    p=parents[x['parent']];assert p['text'][x['offsetWithinParent']:x['offsetWithinParent']+len(x['text'])]==x['text']and x['digitalFolios']==p['digitalFolios']and not x['sourceOutcomeValidated']
facts=set(matrix['declaredResearchFactRegistry'])|set(matrix['coordinateFacts']);clauseIDs={x['id']for x in matrix['clauses']}
for x in matrix['rules']:assert set(x['all'])<=facts and set(x['sourceClauseIDs'])<=clauseIDs and not x['fullSourceConditionSetEstablished']
assert matrix['sourceManyFewNotComplements']and matrix['visibleCountDoesNotAdjudicateQuantityOrPurity']and not matrix['fullPatternCompiler']
for x in source['actualModules']:assert sha(w/x['file'])==x['sha256']
ids=read(b/'PROMOTION_IDENTITIES.json');assert len(ids['records'])==8
for x in ids['records']:
    p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256']
for x in ids['testPathRelocations']:
    t=(w/x['staged']).read_text(encoding='utf-8');t=t.replace("from'./core-reference.mjs'","from'../research/bazi-food-core/core-reference.mjs'").replace("s=new URL('./',import.meta.url)","s=new URL('../qa/bazi-food-core/',import.meta.url)").replace("new URL('TEN_RELATION_RESULTS.json',import.meta.url)","new URL('../qa/bazi-food-core/TEN_RELATION_RESULTS.json',import.meta.url)").replace('archives/v53-before-bazi-food-source/','archives/v53-before-bazi-food-core/')
    assert t==(w/x['promoted']).read_text(encoding='utf-8')
a,z=read(q/'RESULTS.json'),read(q/'TEN_RELATION_RESULTS.json');assert len(a['checks'])+len(z['checks'])==8 and all(x['ok']for d in[a,z]for x in d['checks'])
assert a['summary']['ternaryCases']==78 and a['summary']['actualHHCBaziCalls']==2 and a['summary']['actualHHCFoodRelationInspections']==2 and a['summary']['actualLunarRelationTableQueries']==8
assert z['summary']['actualHHCTenGodFunctionQueries']==10 and z['summary']['actualLunarRelationTableQueries']==10 and z['summary']['newHHCBaziCharts']==0
assert [x['actualHHCFoodVisiblePositions']for x in a['records']]==[[1,3],[]]
for x in a['records']:assert x['actualHHCFoodVisiblePositions']==x['actualLunarFoodVisiblePositions']and x['sourceManyFewNotDetermined']and not x['independentNewSourceExample']
for x in z['records']:assert x['actualHHCTenGod']=='Thực Thần'and x['actualLunarTenGod']=='食神'and not x['realCalendarDateValidated']
out={'date':'2026-10-28','sourceContextSHA256Verified':source['sourceContextSHA256'],'inheritedSourceScopeVerificationPassedWithoutRerunningEngines':True,'inheritedSourcePassingChecksNotNew':6,'parentContextsSelectedNotFullyEncoded':8,'selectedClauses':12,'selectedCodepoints':135,'localPredicateRules':11,'declaredResearchFactsNotAutomaticStrengthFacts':21,'derivedDayPolarityFacts':2,'passingChecks':8,'ternaryCases':78,'actualHHCBaziCallsForNewProjectionOfOldExamples':2,'actualHHCFoodRelationInspections':2,'actualHHCTenGodFunctionQueries':10,'actualLunarRelationTableQueries':18,'newLunarCalendarChartsOrSearches':0,'newIndependentPrintedExamples':0,'promotionIdentityHashesVerified':8,'moduleByteIdenticalToStaging':True,'testScriptBodiesIdenticalExceptPaths':2,'manyFewPurityAndStrengthNotInferredFromVisibleCount':True,'fixedTenGodRelationsNeverRemappedByRepeatPatternLabel':True,'sourceConservativeInterpretationBoundaryDeclared':True,'unselectedParentContexts':82,'subsidiaryClausesOfSelectedParentsStillOpen':True,'sourceFourFolioImageGapStillOpen':True,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePositions':0,'newIndependentWitnesses':0,'fullPatternCompiler':False,'fullStrengthMethod':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
if '--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
