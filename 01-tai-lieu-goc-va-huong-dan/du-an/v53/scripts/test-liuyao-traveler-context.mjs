import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{explicitTravelerContext as inspect}from'../research/liuyao-closing-context/traveler-context.mjs';
const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/liuyao-closing-context'),q=resolve(r,'qa/liuyao-closing-context'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const source=await read(resolve(b,'TRAVELER_CONTEXT.json')),fixture=source.fixture,values=fixture.valuesBottomToTop,ctx=(subject,question)=>({system:source.system,subject,question});
await check('26 inspected source positions/2QA images/2nativecrops retain identities and distinguish1non-ruleleaf;no newHTTP/PDF',async()=>{
 const local=await read(resolve(b,'TRAVELER_RENDERS.json')),qa=await read(resolve(b,'TRAVELER_QA_RENDERS.json'));
 assert.equal(sha(await readFile(resolve(w,local.sourcePDF))),local.sourceSHA256);assert.equal(local.records.length,26);assert.equal(local.contentPositionsActuallyViewed,25);assert.deepEqual(local.nonRuleLeaves,[338]);
 for(const x of[...local.records,...qa.records]){assert(x.actuallyViewed);assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);}
 for(const name of['DETAIL_CROP.json','CHART_CROP.json']){const x=await read(resolve(b,name));assert(x.actuallyViewed);assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);assert.equal(sha(await readFile(resolve(w,x.source))),x.sourceSHA256);}
 assert.equal(local.newHTTPRequests,0);assert.equal(local.newOriginalContainers,0);
});
let hhcCalls=0;
await check('Printed旅→艮 executes2realHHCcalls andmatches6workingkin/branchlabels,Self1/Response4,changed酉財→戌子 while explicitSi-normalization staysdeclared',async()=>{
 const c={};c.window=c;vm.createContext(c);const code=await readFile(resolve(r,'engine.js'));assert.equal(sha(code),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');vm.runInContext(code.toString(),c);
 assert.equal(c.HHC_ENGINE.hexNumber(values),56);hhcCalls++;assert.equal(c.HHC_ENGINE.hexNumber(values.map(v=>v===9?8:v===6?7:v)),52);hhcCalls++;
 const out=inspect(values,ctx('mother','return-date'));assert.equal(out.chart.primary.number,56);assert.equal(out.chart.changed.number,52);assert.deepEqual(out.chart.movingLines,[4]);
 assert.deepEqual(out.chart.lines.map(x=>({branch:x.branch,kin:x.kin})),fixture.sourceBaseWorkingLabelsBottomToTop);assert.equal(out.chart.primary.shi,1);assert.equal(out.chart.primary.ying,4);
 assert.deepEqual({line:out.chart.lines[3].changed.line,branch:out.chart.lines[3].changed.branch,kin:out.chart.lines[3].changed.kin},fixture.sourceChangedLine);
 assert.equal(fixture.sourceGraphicSiNormalizedExplicitly,true);assert.equal(fixture.hiddenRoleReadIsNotAutomaticallyChosenUseLine,true);
});
await check('Source有病isstructuralvocabulary at334,notautomaticactualpersonillness;return-dateandtravelercondition remainexplicitdifferentqueries',()=>{
 for(const question of source.questionLabels){const out=inspect(values,ctx('mother',question));assert.equal(out.question,question);assert(out.sourceQuestionWasNotSilentlyChanged);assert.equal(out.sourceStructuralVocabulary.literal,'用神墓絕空破受傷謂之有病');assert(out.sourceStructuralVocabulary.notAutomaticallyActualPersonIllness);assert(out.sourceStructuralVocabulary.notAClinicalDefinition);
  for(const key of['structuralAffliction','actualPersonIllness','healthResult','lifespan','actualTravelSafety','returnDate','currentLocation','chronologicalDateAdapter','practicalOutcome'])assert.equal(out[key],null);
 }
});
await check('Explicitmother/ father role absentfromsurface staysunselected;unrelatedResponse isnotbiologicalmother oridentifiedtraveler andmissingquestion/subject staysunknown',()=>{
 for(const subject of['mother','father']){const out=inspect(values,ctx(subject,'return-date'));assert.deepEqual(out.candidateRoleProjection.originalLines,[]);assert.equal(out.candidateRoleProjection.kin,'父母');assert.equal(out.candidateRoleProjection.hiddenRoleAutomaticallySelected,false);assert.equal(out.useLineSelected,null);}
 const unrelated=inspect(values,ctx('unrelated-traveler','traveler-condition'));assert.equal(unrelated.candidateRoleProjection.line,4);assert.equal(unrelated.candidateRoleProjection.physicalResponseBranch,'酉');assert.equal(unrelated.candidateRoleProjection.notAnIdentifiedRealPerson,true);
 const husband=inspect(values,ctx('husband','return-date'));assert.equal(husband.candidateRoleProjection.kin,'官鬼');assert.equal(husband.biologicalIdentityInferred,false);
 for(const context of[ctx(null,'return-date'),ctx('mother',null),ctx(null,null)]){const out=inspect(values,context);assert(!out.questionScopeComplete);assert.equal(out.candidateRoleProjection,null);}
});
await check('20furtherfirst-passspans yield102readspans/27headingonly whilemedical/legal/supernatural/sexoutcomes andchapter103stayunestablished',async()=>{
 const units=await read(resolve(b,'PRIOR_STAGED_UNITS.json')),manual=await read(resolve(b,'TRAVELER_MANUAL_READINGS.json'));
 assert.deepEqual(units.currentCounts,{registeredUnits:137,regularNumberedUnits:130,supplements:7,headingOnlyBodyUnits:27,partialFoundationUnits:7,otherPartialUnits:1,firstPassCompleteSpanUnits:102,wholeUnitsApplied:0});
 assert.equal(manual.chapterRanges.length,20);assert.deepEqual(manual.nonRuleLeaves,[338]);assert.equal(manual.chapter103.nextPDFPage,351);assert(!manual.chapter103.wholeFirstPassRead);
 assert(units.units.every(x=>!x.entireUnitApplied));assert(!units.units.find(x=>x.id==='B02-ch100').bodyHeadingUnresolvedReading.resolved);
 const old=await read(resolve(r,'research/liuyao-commodity-boundary/B02_CURRENT_UNITS.json'));assert.equal(old.currentCounts.firstPassCompleteSpanUnits,82);assert.equal(old.units.find(x=>x.id==='B02-ch083').nextPDFPage,325);
});
await check('Strictinputs rejecthiddenpremises/clinicalquestion/silent aliases;returnedliteral/coordinates cannotmutatesource andconsumerreleaseunchanged',async()=>{
 const good=ctx('mother','return-date');for(const bad of[null,{},[],{...good,subject:undefined},{...good,question:'is she sick?'},{...good,subject:'me'},{...good,diagnosis:true},{...good,[Symbol('x')]:true}])assert.throws(()=>inspect(values,bad),TypeError);
 for(const bad of[[],Array(6),[8,8,7,9,8,'7']])assert.throws(()=>inspect(bad,good),TypeError);
 const out=inspect(values,good);out.sourceStructuralVocabulary.literal='fake';out.candidateRoleProjection.originalLines.push(99);const next=inspect(values,good);assert.equal(next.sourceStructuralVocabulary.term,'有病');assert.deepEqual(next.candidateRoleProjection.originalLines,[]);assert.equal(next.consumerApplied,false);
 const m=await read(resolve(w,'archives/v53-before-liuyao-closing-context/PACKAGE_MANIFEST.json'));assert.equal(m.files.length,3663);for(const f of['engine.js','Huyen_Hoc_Cac.html','site/index.html'])assert.equal(sha(await readFile(resolve(r,f))),m.files.find(x=>x.file===f).sha256);
});
const result={date:'2026-10-28',status:'staged-traveler-question-and-structural-vocabulary-boundary-verified',checks,
 summary:{newViewedSourcePositions:26,contentPositions:25,nonRuleLeaves:1,highResolutionQAViewed:2,nativeCropsViewed:2,firstPassSpansAdded:20,stagedCurrentFirstPassSpans:102,stagedCurrentHeadingOnlyUnits:27,actualHHCHexCalls:hhcCalls,printedCastFixtures:1,workingSourceKinBranchLabels:6,explicitSiNormalizations:1,sourceChangedKinBranchLabels:1,namedQuestions:2,explicitSubjects:4,newHTTPRequests:0,newOriginalContainers:0},
 fixtureProjection:inspect(values,ctx('mother','return-date')),wholeChaptersApplied:false,sourceOutcomesValidated:false,consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'TRAVELER_RESULTS.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...result.summary}));
