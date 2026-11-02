import {readFile,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {sourceQuestionProjection as inspect} from '../research/liuyao-family-study/question-reference.mjs';
import {catalogue} from '../research/liuyao-foundations/liuyao-reference.mjs';

const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/liuyao-family-study'),q=resolve(r,'qa/liuyao-family-study');
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const source=await read(resolve(b,'SOURCE_MANIFEST.json')),contexts=await read(resolve(b,'SOURCE_CONTEXTS.json')),methods=contexts.methods;
const fixture=(await read(resolve(b,'PRINTED_FIXTURES.json'))).fixtures[0],values=fixture.valuesBottomToTop;
const ctx=(system,subject,question,classic=null,examStage=null)=>({system,subject,question,classic,examStage});
const defaultContext=m=>ctx(m.id,m.subjects[0],m.questions[0],m.id==='b02-ch046-classic'?'春秋':null,m.id==='b02-ch048-exam-stage'?'county':null);

await check('Original PDF and33 viewed positions retain exact identities;31 first-read positions and2 expanded positions are not new downloads',async()=>{
 assert.equal(sha(await readFile(resolve(w,source.sourcePDF))),source.sourceSHA256);assert.equal(source.images.length,33);
 assert.equal(source.images.filter(x=>x.newReadPositionThisScope).length,31);assert.equal(source.images.filter(x=>x.expandedPriorRead).length,2);
 for(const x of source.images){assert(x.actuallyViewed);assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);}
 assert.equal(source.newHTTPRequests,0);assert.equal(source.newOriginalContainers,0);assert.equal(source.independentNewWitnesses,0);
});
let hhcCalls=0;const c={};c.window=c;vm.createContext(c);vm.runInContext(await readFile(resolve(r,'engine.js'),'utf8'),c);
await check('Printed 益→觀 executes2 actual HHC calls and matches6 independent kin/branch labels, self/response and 子父→未財',()=>{
 assert.equal(c.HHC_ENGINE.hexNumber(values),42);hhcCalls++;
 assert.equal(c.HHC_ENGINE.hexNumber(values.map(v=>v===9?8:v===6?7:v)),20);hhcCalls++;
 const out=inspect(values,ctx('b02-ch046-classic','self','specified-classic','春秋'));
 assert.deepEqual(out.chart.lines.map(x=>({branch:x.branch,kin:x.kin})),fixture.sourceBaseLabelsBottomToTop);
 assert.equal(out.chart.primary.shi,3);assert.equal(out.chart.primary.ying,6);assert.deepEqual(out.chart.movingLines,[1]);
 assert.equal(out.chart.lines[0].changed.branch,'未');assert.equal(out.chart.lines[0].changed.kin,'妻財');
 assert.equal(out.chronologicalDateAdapter,null);assert.equal(out.examResult,null);
});
await check('10 named contexts distinguish biological targets, dual teacher/books meanings, literary roles and artisan roles without selecting a use-line',()=>{
 assert.equal(methods.length,10);
 const father=inspect(values,ctx('b02-ch041-parent','father','longevity')),mother=inspect(values,ctx('b02-ch041-parent','mother','longevity'));
 assert.deepEqual(father.candidateRoleGroups,mother.candidateRoleGroups);assert.equal(father.symbolicKinIsBiologicalIdentity,false);
 const teacher=inspect(values,ctx('b02-ch047-teacher','self','teacher'));
 assert.deepEqual(teacher.candidateRoleGroups.map(g=>[g.id,g.kin,g.originalLines]),[['teacher','父母',[1]],['books','父母',[1]]]);
 const a=inspect(values,ctx('b02-ch045-literary','self','literary-study')),b=inspect(values,ctx('b02-ch045-artisan','self','artisan-study'));
 assert.deepEqual(a.candidateRoleGroups.map(g=>g.kin),['父母','官鬼']);assert.deepEqual(b.candidateRoleGroups.map(g=>g.kin),['妻財','子孫']);
 assert.equal(a.useLineSelected,null);assert.equal(b.useLineSelected,null);
 const wife=inspect(values,ctx('b02-ch043-spouse','wife','harmony')),husband=inspect(values,ctx('b02-ch043-spouse','husband','harmony'));
 assert.deepEqual(wife.candidateRoleGroups.map(g=>g.kin),['妻財']);assert.equal(husband.candidateRoleGroups,null);assert.equal(husband.unknownReason,'role-not-extracted-for-this-source-context');
});
await check('Question target, topic, chosen classic and historical exam stage must be explicit; ambiguity stays null instead of automatic reinterpretation',()=>{
 for(const m of methods){const a=defaultContext(m);for(const k of['subject','question']){const out=inspect(values,{...a,[k]:null});assert.equal(out.questionScope.complete,false);assert.equal(out.candidateRoleGroups,null);assert(out.questionScope.missing.includes(k));}}
 for(const [name,element]of[['春秋','金'],['毛詩','木'],['書經','水'],['禮記','火'],['易經','土']]){
  const out=inspect(values,ctx('b02-ch046-classic','self','specified-classic',name));assert.equal(out.classicSourceCoordinate.element,element);assert.equal(out.practicalOutcome,null);
 }
 const absent=inspect(values,ctx('b02-ch046-classic','self','specified-classic'));
 assert.equal(absent.candidateRoleGroups,null);assert.equal(absent.classicSourceCoordinate,null);
 const unspecified=inspect(values,ctx('b02-ch048-exam-stage','self','specified-exam-stage'));
 assert.equal(unspecified.historicalExamStage,null);assert.equal(unspecified.questionScope.complete,false);
 for(const stage of['county','prefecture','circuit']){const out=inspect(values,ctx('b02-ch048-exam-stage','self','specified-exam-stage',null,stage));assert.equal(out.historicalExamStage,stage);assert.equal(out.candidateRoleGroups,null);assert.equal(out.examResult,null);}
});
let enumerated=0,roleEntries=0;
await check('5120 bounded figure/motion/source projections retain original/changed candidate identities, unknown premises and null practical outcomes',()=>{
 for(const h of catalogue())for(const mask of[0,1,2,4,8,16,32,63]){
  const v=h.bits.map((bit,i)=>(mask>>i)&1?(bit?9:6):(bit?7:8));
  for(const m of methods){const out=inspect(v,defaultContext(m));assert.equal(out.chart.primary.number,h.number);
   for(const g of out.candidateRoleGroups??[]){assert.deepEqual(g.originalLines,out.chart.lines.filter(x=>x.kin===g.kin).map(x=>x.line));assert.deepEqual(g.changedLines,out.chart.lines.filter(x=>x.changed?.kin===g.kin).map(x=>x.line));roleEntries++;}
   for(const key of['useLineSelected','strength','effectiveActivity','practicalOutcome','lifespan','healthResult','fertilityResult','marriageResult','examResult','chronologicalDateAdapter'])assert.equal(out[key],null);
   assert.equal(out.automaticQuestionInference,false);assert.equal(out.consumerApplied,false);enumerated++;
  }
 }assert.equal(enumerated,5120);
});
await check('Malformed, aliased, free-text or hidden premises are rejected; returned objects and caller inputs cannot mutate source tables',()=>{
 const a=ctx('b02-ch046-classic','self','specified-classic','春秋'),before=values.slice();
 for(const bad of[null,{},[],new Date(),{...a,subject:undefined},{...a,question:'will I pass?'},{...a,classic:'I Ching'},{...a,examStage:'county'},{...a,calendar:'today'},{...a,[Symbol('x')]:true}])assert.throws(()=>inspect(values,bad),TypeError);
 for(const bad of[[],Array(6),[9,8,8,8,7,'7']])assert.throws(()=>inspect(bad,a),TypeError);
 const x=inspect(values,a);x.classicSourceCoordinate.element='假';x.candidateRoleGroups[0].originalLines.push(99);x.sourcePages.length=0;
 const y=inspect(values,a);assert.equal(y.classicSourceCoordinate.element,'金');assert.deepEqual(y.candidateRoleGroups[0].originalLines,[1]);assert(y.sourcePages.length>0);assert.deepEqual(values,before);
});
await check('Eleven further first-pass spans preserve shared boundaries, a partial chapter50 and source-corroborated correction of working TOC40',async()=>{
 const map=await read(resolve(b,'B02_CURRENT_UNITS.json')),manual=await read(resolve(b,'MANUAL_READINGS.json'));
 assert.equal(map.units.length,136);assert.equal(map.units.filter(x=>x.disposition==='heading-only-body-extraction-open').length,81);
 assert.deepEqual(map.currentCounts,{registeredUnits:136,regularNumberedUnits:130,supplements:6,headingOnlyBodyUnits:81,partialFoundationUnits:7,otherPartialUnits:1,firstPassCompleteSpanUnits:47,wholeUnitsApplied:0});
 assert.equal(Object.keys(manual.chapterRanges).length,11);assert.equal(manual.chapter50.wholeFirstPassRead,false);
 const unit=map.units.find(x=>x.id==='B02-ch040');assert.equal(unit.normalizedHeading,'趨避');assert.equal(unit.workingTranscriptionCorrection.old,'超遷');
 assert.deepEqual(unit.workingTranscriptionCorrection.evidencePDFPages,[15,235]);assert.equal(unit.workingTranscriptionCorrection.sourceEmended,false);
 const old=await read(resolve(r,'research/liuyao-life-context/B02_CURRENT_UNITS.json'));assert.equal(old.units.find(x=>x.id==='B02-ch040').normalizedHeading,'超遷');
 assert.equal(map.units.find(x=>x.id==='B02-ch050').disposition,'partial-body-reading-application-open');assert(map.units.every(x=>x.entireUnitApplied===false));
 assert.equal((await read(resolve(b,'BOUNDED_CLAUSES.json'))).clauses.length,35);
});
await check('Released HTML/engine and preceding research reference implementations remain byte-identical to the verified home-diagram package',async()=>{
 const old=await read(resolve(w,'archives/v53-before-liuyao-family-study/PACKAGE_MANIFEST.json'));
 for(const f of['engine.js','app.js','content.js','fortune.js','Huyen_Hoc_Cac.html','site/index.html','research/liuyao-life-context/life-context-reference.mjs','research/home-tomb-diagrams/diagram-reference.mjs'])
  assert.equal(sha(await readFile(resolve(r,f))),old.files.find(x=>x.file===f).sha256);
});
const out={date:'2026-10-28',checks,summary:{actualHHCHexCalls:hhcCalls,printedCastFixtures:1,sourceKinBranchLabels:6,namedSourceContexts:10,sourceClassicCoordinates:5,
 enumeratedPrivateFigureMotionContexts:enumerated,roleEntriesWithinEnumeratedContexts:roleEntries,boundedClauses:35,viewedSourcePositions:33,newSourceReadPositions:31,expandedPriorReadPositions:2,
 newNativeContentRenders:31,newHighResolutionQARenders:2,completeFirstPassChapterSpans:11,workingTOCLabelsCorrected:1,newHTTPRequests:0,newOriginalContainers:0},
 sourceOutcomesValidated:false,clinicalOrFertilityOrMarriageOrExamClassifier:false,consumerChanged:false,wholeChaptersApplied:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
