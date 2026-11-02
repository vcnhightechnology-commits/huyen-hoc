import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{explicitHouseContext as inspect}from'../research/liuyao-closing-context/house-context.mjs';
const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/liuyao-closing-context'),q=resolve(r,'qa/liuyao-closing-context'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const methods=(await read(resolve(b,'HOUSE_CONTEXTS.json'))).methods,fixture=await read(resolve(b,'PRINTED_FIXTURE.json')),values=fixture.valuesBottomToTop;
const scope=(system,subject,question)=>({system,subject,question}),defaultScope=m=>scope(m.id,m.subjects[0],m.questions[0]);
await check('44newlyviewed positions and4QA images preserve retainedPDF/image identities;2priorTOC rereads and4publisher leaves are notnewrulepages',async()=>{
 const local=await read(resolve(b,'CLOSING_RENDERS.json')),qa=await read(resolve(b,'CLOSING_QA_RENDERS.json'));
 assert.equal(sha(await readFile(resolve(w,local.sourcePDF))),local.sourceSHA256);assert.equal(local.records.length,44);assert.equal(local.contentPositionsActuallyViewed,40);assert.deepEqual(local.nonRuleLeaves,[391,392,393,394]);assert.equal(local.lastBodyPDFPage,390);
 for(const x of[...local.records,...qa.records]){assert(x.actuallyViewed);assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);}
 assert.deepEqual(qa.records.filter(x=>x.expandedPriorTOCRead).map(x=>x.sourcePage),[18,19]);assert.equal(local.newHTTPRequests,0);assert.equal(local.newOriginalContainers,0);
});
let hhcCalls=0;
await check('Printed乾→小畜 executes2actualHHCcalls andmatches6independentkin/branchlabels,Self6/Response3,and午官→未父;parentsymbols present refute the quoted blanketabsence premise locally',async()=>{
 const c={};c.window=c;vm.createContext(c);const code=await readFile(resolve(r,'engine.js'));assert.equal(sha(code),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');vm.runInContext(code.toString(),c);
 assert.equal(c.HHC_ENGINE.hexNumber(values),1);hhcCalls++;assert.equal(c.HHC_ENGINE.hexNumber(values.map(v=>v===9?8:v===6?7:v)),9);hhcCalls++;
 const out=inspect(values,scope('b02-ch105-whole-house-critique','whole-household','undifferentiated-household-fortunes'));
 assert.equal(out.chart.primary.number,1);assert.equal(out.chart.changed.number,9);assert.deepEqual(out.chart.movingLines,[4]);assert.deepEqual(out.chart.lines.map(x=>({branch:x.branch,kin:x.kin})),fixture.sourceBaseLabelsBottomToTop);
 assert.equal(out.chart.primary.shi,6);assert.equal(out.chart.primary.ying,3);assert.deepEqual({line:out.chart.lines[3].changed.line,branch:out.chart.lines[3].changed.branch,kin:out.chart.lines[3].changed.kin},fixture.sourceChangedLine);
 assert.deepEqual(out.chart.lines.filter(x=>x.kin==='父母').map(x=>x.line),[3,6]);assert.equal(out.candidateRoleProjections,null);assert(out.sourceRejectsUndifferentiatedQuestion);assert.equal(out.unknownReason,'source-rejects-undifferentiated-household-query');
});
await check('Buildingrole Father doesnotbecomebiologicalparent;individualmoving/cohabitationqueriesrequireexplicitrelationship andunrelatedResponse stayssymbolic',()=>{
 const house=inspect(values,scope('b02-ch106-house','self','rent-house'));assert.deepEqual(house.candidateRoleProjections.map(x=>[x.kin,x.originalLines,x.changedLines]),[['父母',[3,6],[4]]]);assert(house.sourceRoleIsNotBiologicalIdentity);
 const father=inspect(values,scope('b02-ch111-moving-relative','father','specified-relative-at-move')),child=inspect(values,scope('b02-ch111-moving-relative','child','specified-relative-at-move'));
 assert.equal(father.candidateRoleProjections[0].kin,'父母');assert.equal(child.candidateRoleProjections[0].kin,'子孫');assert.equal(father.familyOutcome,null);assert.equal(child.healthResult,null);
 const unrelated=inspect(values,scope('b02-ch114-cohabitation','unrelated-cohabitant','specified-cohabitant'));assert.deepEqual(unrelated.candidateRoleProjections.map(x=>[x.structuralRole,x.line]),[['世',6],['應',3]]);
 assert(unrelated.candidateRoleProjections.every(x=>x.notActualPersonOrMeasuredGeometry));
 const related=inspect(values,scope('b02-ch114-cohabitation','mother','specified-cohabitant'));assert.equal(related.candidateRoleProjections[0].kin,'父母');assert.equal(related.useLineSelected,null);
});
await check('Landform,acquisitionwhen/where,practitionerandrelativeheight areseparatenamedcoordinates without actualterrain,ownership,dateor excavationdepth',()=>{
 const form=inspect(values,scope('b02-ch120-landform','specified-land','landform-only'));assert.deepEqual(form.sourceSymbolicLandform,{sourceSiteLine:6,sourceOppositeLine:3,sourceMiddleTwoLines:[4,5],actualMeasuredTerrain:null});
 const when=inspect(values,scope('b02-ch121-acquisition-when','self','land-acquisition-time')),where=inspect(values,scope('b02-ch122-acquisition-where','self','land-acquisition-place'));
 assert.equal(when.candidateRoleProjections[0].structuralRole,'世');assert.equal(where.candidateRoleProjections[0].kin,'父母');assert.equal(when.acquisitionDate,null);assert.equal(where.realLocation,null);
 const practitioner=inspect(values,scope('b02-ch123-geomancer','specified-practitioner','practitioner-context'));assert.equal(practitioner.candidateRoleProjections[0].structuralRole,'應');assert.equal(practitioner.practitionerQuality,null);
 const point=inspect(values,scope('b02-ch124-point','specified-land','source-relative-height-band'));assert.deepEqual(point.sourceRelativeHeightBand,{sourceLines:[5,6],label:'上'});assert(point.sourceHeightIsNotElevationOrDepth);assert.equal(point.diggingDepth,null);assert.equal(point.actualElevation,null);
 const grave=inspect(values,scope('b02-ch126-old-grave','self','declared-child-concern'));assert.equal(grave.candidateRoleProjections[0].kin,'子孫');assert.equal(grave.familyOutcome,null);
});
let missingCases=0;
await check('All13sourcecontexts preserve explicitmissingquestions andreturnnull forunencodedoldhouseconcern,universaldoorline,clinical/legal/physicaloutcomes',()=>{
 assert.equal(methods.length,13);
 for(const m of methods){const good=defaultScope(m);for(const k of['subject','question']){const out=inspect(values,{...good,[k]:null});assert(!out.questionScopeComplete);assert.equal(out.candidateRoleProjections,null);missingCases++;}
  const out=inspect(values,good);for(const k of['useLineSelected','strength','effectiveActivity','actualHouseOrRoomPlan','universalDoorLine','compassBearing','realLocation','actualElevation','diggingDepth','landOwnership','acquisitionDate','practitionerQuality','constructionSafety','healthResult','lifespan','familyOutcome','financialResult','chronologicalDateAdapter','practicalOutcome'])assert.equal(out[k],null);assert.equal(out.consumerApplied,false);
 }
 const oldhouse=inspect(values,scope('b02-ch113-old-house','self','named-concern-only'));assert.equal(oldhouse.candidateRoleProjections,null);assert.equal(oldhouse.unknownReason,'named-concern-not-yet-encoded');assert.equal(missingCases,26);
});
await check('393datedcolophon directlyprintsRepublic14month11publication/distribution;394endleafand1925preface remain separate,notanewindependentwitness',async()=>{
 const audit=await read(resolve(b,'COLOPHON_AUDIT.json'));assert.equal(audit.sourcePDFPage,393);assert.equal(audit.publicationDateLiteral,'中華民國十四年十一月出版');assert.equal(audit.distributionDateLiteral,'中華民國十四年十一月發行');
 assert.deepEqual(audit.calendarConversion,{republicYear:14,commonEraYear:1925,printedMonth:11,dayUnstated:true,monthCalendarNotFurtherInferred:true});assert.equal(audit.proofreaderNameLiteral,'秦慎安');assert.equal(audit.editionIndependentlyNewWitness,false);assert.equal(audit.sourceOriginalBytesChanged,false);
 const original=await read(resolve(r,'research/liuyao-foundations/SOURCE_AUDIT.json'));assert(original.bibliography.find(x=>x.work==='增刪卜易').endleaf.pdfPage===394);
});
await check('Closing28spans plus20priorstagedspansyield130firstpass/7partialfoundations/0whole;TOC-bodytitles retainedwithoutclaimall137unitsfullyapplied',async()=>{
 const map=await read(resolve(b,'B02_CURRENT_UNITS.json')),manual=await read(resolve(b,'CLOSING_MANUAL_READINGS.json'));assert.equal(map.units.length,137);
 assert.deepEqual(map.currentCounts,{registeredUnits:137,regularNumberedUnits:130,supplements:7,headingOnlyBodyUnits:0,partialFoundationUnits:7,otherPartialUnits:0,firstPassCompleteSpanUnits:130,wholeUnitsApplied:0});assert.equal(manual.chapterRanges.length,28);assert.equal(manual.lastBodyPDFPage,390);
 const difference=n=>map.units.find(x=>x.id===n).tocBodyHeadingDifference;
 assert.deepEqual(difference('B02-ch106'),{toc18:'蓋造買宅賣宅',body361:'蓋造買宅賃宅',evidencePages:[18,361],notSilentlyUnified:true,sourceEmended:false});
 assert.equal(difference('B02-ch110').toc18,'歸宅入火');assert.equal(difference('B02-ch110').body364,'新宅入火');assert(map.units.every(x=>!x.entireUnitApplied));
 assert(!map.units.find(x=>x.id==='B02-ch100').bodyHeadingUnresolvedReading.resolved);
 const old=await read(resolve(r,'research/liuyao-commodity-boundary/B02_CURRENT_UNITS.json'));assert.equal(old.currentCounts.firstPassCompleteSpanUnits,82);assert.equal(old.currentCounts.headingOnlyBodyUnits,47);
});
await check('Strictcontexts rejectautomaticbroadquestions/aliases/hiddenpremises;returnedsource data cannotmutate tables andreleased3663consumerbytesstayunchanged',async()=>{
 const good=scope('b02-ch106-house','self','rent-house');for(const bad of[null,{},[],{...good,subject:undefined},{...good,question:'willmyfamilybehappy?'},{...good,subject:'mother'},{...good,latitude:10},{...good,[Symbol('x')]:true}])assert.throws(()=>inspect(values,bad),TypeError);
 for(const bad of[[],Array(6),[7,7,7,9,7,'7']])assert.throws(()=>inspect(bad,good),TypeError);
 const out=inspect(values,good);out.candidateRoleProjections[0].originalLines.push(99);out.sourcePages.length=0;const next=inspect(values,good);assert.deepEqual(next.candidateRoleProjections[0].originalLines,[3,6]);assert(next.sourcePages.length>0);
 const m=await read(resolve(w,'archives/v53-before-liuyao-closing-context/PACKAGE_MANIFEST.json'));assert.equal(m.files.length,3663);for(const f of['engine.js','app.js','content.js','Huyen_Hoc_Cac.html','site/index.html'])assert.equal(sha(await readFile(resolve(r,f))),m.files.find(x=>x.file===f).sha256);
});
const result={date:'2026-10-28',status:'staged-closing-source-span-and-explicit-house-question-contexts-verified',checks,
 summary:{newViewedSourcePositions:44,newBodyPositions:40,nonRuleLeaves:4,expandedPriorTOCPositions:2,highResolutionQAViewed:4,newFirstPassSpans:28,inheritedPriorStagingSpans:20,currentFirstPassSpans:130,partialFoundationUnits:7,wholeUnitsApplied:0,
 actualHHCHexCalls:hhcCalls,printedCastFixtures:1,sourceKinBranchLabels:6,sourceChangedKinBranchLabels:1,namedHouseContexts:13,explicitMissingScopeCases:missingCases,colophonSourcePDFPage:393,colophonRepublicYear:14,colophonCommonEraYear:1925,colophonPrintedMonth:11,newHTTPRequests:0,newOriginalContainers:0},
 fixtureProjection:inspect(values,scope('b02-ch105-whole-house-critique','whole-household','undifferentiated-household-fortunes')),
 allConditionalRulesEncoded:false,sourceOutcomesValidated:false,consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'CLOSING_RESULTS.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...result.summary}));
