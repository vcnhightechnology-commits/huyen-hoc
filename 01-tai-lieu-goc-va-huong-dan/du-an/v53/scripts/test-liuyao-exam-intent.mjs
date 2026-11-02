import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{sourceIntentProjection as inspect}from'../research/liuyao-exam-intent/intent-reference.mjs';
const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/liuyao-exam-intent'),q=resolve(r,'qa/liuyao-exam-intent'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const data=await read(resolve(b,'SOURCE_CONTEXTS.json')),fixture=await read(resolve(b,'PRINTED_FIXTURE.json')),values=fixture.valuesBottomToTop;
const scope=(system,subject,question,intent,rank=null)=>({system,subject,question,intent,rank});
const defaultScope=m=>scope(m.id,m.subjects[0],m.questions[0],m.intents[0],m.requiresNamedRank?'一品':null);
const roles=out=>out.candidateRoleGroups?.map(x=>x.kin)??null;
await check('Retained PDF,37 actual inspected positions and3 high-resolution QA images preserve exact recorded hashes and non-rule leaf distinctions',async()=>{
 const src=await read(resolve(b,'LOCAL_RENDERS.json')),qa=await read(resolve(b,'QA_RENDERS.json'));
 assert.equal(sha(await readFile(resolve(w,src.sourcePDF))),src.sourceSHA256);assert.equal(src.records.length,37);assert.equal(src.contentPositionsActuallyViewed,34);assert.deepEqual(src.nonRuleLeaves,[286,287,288]);
 for(const x of[...src.records,...qa.records]){assert(x.actuallyViewed);assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);}
 assert.equal(qa.records.length,3);assert.equal(src.newHTTPRequests,0);assert.equal(src.newOriginalContainers,0);
});
let hhcCalls=0;const c={};c.window=c;vm.createContext(c);const code=await readFile(resolve(r,'engine.js'));assert.equal(sha(code),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');vm.runInContext(code.toString(),c);
await check('Printed 臨→師 executes2 actual HHC figure calls and independently matches6 source kin/branch labels,Self2/Response5 and first-line巳→寅',()=>{
 assert.equal(c.HHC_ENGINE.hexNumber(values),19);hhcCalls++;
 const changed=values.map(v=>v===9?8:v===6?7:v);assert.equal(c.HHC_ENGINE.hexNumber(changed),7);hhcCalls++;
 const out=inspect(values,scope('b02-ch055-literary','self','provincial-metropolitan-examination','examination'));
 assert.equal(out.chart.primary.number,fixture.primaryNumber);assert.equal(out.chart.changed.number,fixture.changedNumber);
 assert.deepEqual(out.chart.lines.map(x=>({branch:x.branch,kin:x.kin})),fixture.sourceBaseLabelsBottomToTop);
 assert.equal(out.chart.primary.shi,2);assert.equal(out.chart.primary.ying,5);assert.deepEqual(out.chart.movingLines,[1]);
 assert.equal(out.chart.lines[0].changed.branch,fixture.sourceFirstChangedBranch);assert.equal(out.chart.lines[0].changed.kin,'官鬼');
 assert.equal(fixture.sourceChangedKinPrinted,false);assert.equal(out.examResult,null);assert.equal(out.sourceBodySymbolEqualsSelf,null);
});
await check('School/stipend/court/military/recruitment contexts distinguish intended role and local priority without adopting blanket presence rules',()=>{
 const by=id=>{const m=data.methods.find(x=>x.id===id);return inspect(values,defaultScope(m));};
 assert.deepEqual(roles(by('b02-ch051-stipend')),['妻財']);assert.deepEqual(roles(by('b02-ch053-results')),['父母']);
 assert.deepEqual(roles(by('b02-ch054-court')),['官鬼','父母']);assert.deepEqual(by('b02-ch054-court').candidateRoleGroups.map(x=>x.sourceLocalPriority),['primary','secondary']);
 assert.deepEqual(roles(by('b02-ch055-literary')),['父母','官鬼']);
 assert.deepEqual(roles(by('b02-ch058-status-finance')),['妻財','官鬼']);
 assert.deepEqual(roles(by('b02-ch059-military')),['官鬼','父母']);assert.equal(by('b02-ch059-military').candidateRoleGroups[0].sourceLocalPriority,'primary');
 const recruiter=by('b02-ch060-recruiter');assert.equal(recruiter.candidateRoleGroups[0].id,'recruiter');assert.match(recruiter.candidateRoleGroups[0].purpose,/not querent own rank/);
 assert.equal(by('b02-ch056-location').sourceGeographyAdapter,null);
});
await check('Practitioner asking own status differs from explicit other practitioner;five listed petition motives remain unencoded instead of silently inheriting status rules',()=>{
 const own=inspect(values,scope('b02-ch065-practitioner','self','practitioner','own-status'));
 const other=inspect(values,scope('b02-ch065-practitioner','other-practitioner','practitioner','professional-service'));
 assert.deepEqual(roles(own),['官鬼']);assert.deepEqual(roles(other),['子孫']);assert.equal(own.occupationInferred,false);
 assert.throws(()=>inspect(values,scope('b02-ch065-practitioner','self','practitioner','professional-service')),TypeError);
 const seek=inspect(values,scope('b02-ch062-petition','self','petition','seek-status'));assert.deepEqual(roles(seek),['官鬼']);
 for(const intent of['public-interest','redress','protect-existing-rank','financial-interest','subordinate-liability']){
  const out=inspect(values,scope('b02-ch062-petition','self','petition',intent));assert(out.questionScope.complete);assert.equal(out.candidateRoleGroups,null);assert.equal(out.unknownReason,'listed-source-intent-not-yet-encoded');
 }
 const father=inspect(values,scope('b02-ch067-father','father','father-status','status'));assert.deepEqual(roles(father),['父母','官鬼']);assert.equal(father.symbolicKinIsBiologicalIdentity,false);
 for(const intent of['initial-concern','existing-defect']){const out=inspect(values,scope('b02-ch064-project','self','public-project',intent));assert.equal(out.intent,intent);assert.equal(out.engineeringSafety,null);}
});
let explicitMissingCases=0;
await check('Every named context requires explicit subject/question/intent;named ranks require explicit source question and never yield actual rank or a numeric element adapter',()=>{
 assert.equal(data.methods.length,19);
 for(const m of data.methods){const good=defaultScope(m);for(const k of['subject','question','intent']){const out=inspect(values,{...good,[k]:null});assert.equal(out.questionScope.complete,false);assert.equal(out.candidateRoleGroups,null);assert(out.questionScope.missing.includes(k));explicitMissingCases++;}}
 const m=data.methods.find(x=>x.requiresNamedRank),good=defaultScope(m),unknown=inspect(values,{...good,rank:null});assert(!unknown.questionScope.complete);assert.equal(unknown.sourceNamedRankQuestion,null);explicitMissingCases++;
 for(const rank of['公侯','將相','一品','八座']){const out=inspect(values,{...good,rank});assert.equal(out.sourceNamedRankQuestion,rank);assert.equal(out.actualRank,null);}
 assert.equal(explicitMissingCases,58);
});
await check('Malformed/aliased/implicit premises are rejected;source roles project original and changed coordinates separately without mutating caller or adding strength/outcome guesses',()=>{
 const good=scope('b02-ch055-literary','self','provincial-metropolitan-examination','examination'),before=values.slice();
 for(const bad of[null,{},[],{...good,subject:undefined},{...good,intent:'will I pass?'},{...good,rank:'manager'},{...good,question:'modern-admission'},{...good,strength:true},{...good,[Symbol('x')]:1}])assert.throws(()=>inspect(values,bad),TypeError);
 for(const bad of[[],Array(6),[9,7,8,8,8,'8']])assert.throws(()=>inspect(bad,good),TypeError);
 const out=inspect(values,good);assert.deepEqual(out.candidateRoleGroups.map(x=>[x.kin,x.originalLines,x.changedLines]),[['父母',[1],[]],['官鬼',[2],[1]]]);
 for(const m of data.methods){const x=inspect(values,defaultScope(m));for(const k of['sourceGeographyAdapter','sourceBodySymbolEqualsSelf','sourceStrength','effectiveActivity','useLineSelected','practicalOutcome','examResult','officeResult','actualRank','financialResult','healthResult','lifespan','legalResult','engineeringSafety','chronologicalDateAdapter'])assert.equal(x[k],null);assert.equal(x.automaticIntentInference,false);assert.equal(x.consumerApplied,false);}
 out.candidateRoleGroups[0].originalLines.push(99);out.sourcePages.length=0;const next=inspect(values,good);assert.deepEqual(next.candidateRoleGroups[0].originalLines,[1]);assert(next.sourcePages.length);assert.deepEqual(values,before);
});
await check('19 further chapter spans preserve repeated55 and volume4/5 boundary;chapter68 and all conditional application stay open',async()=>{
 const map=await read(resolve(b,'B02_CURRENT_UNITS.json')),manual=await read(resolve(b,'MANUAL_READINGS.json')),clauses=await read(resolve(b,'BOUNDED_CLAUSES.json'));
 assert.equal(map.units.length,136);assert.deepEqual(map.currentCounts,{registeredUnits:136,regularNumberedUnits:130,supplements:6,headingOnlyBodyUnits:62,partialFoundationUnits:7,otherPartialUnits:1,firstPassCompleteSpanUnits:66,wholeUnitsApplied:0});
 assert.equal(manual.chapterRanges.length,19);assert.deepEqual(manual.chapter68.pagesRead,[299,300]);assert.equal(manual.chapter68.wholeFirstPassRead,false);
 assert.deepEqual(map.units.filter(x=>x.printedNumber===55).map(x=>x.normalizedHeading),['鄉試會試','陞選候補']);assert.deepEqual(manual.nonRuleLeaves,[286,287,288]);
 assert.equal(map.units.find(x=>x.id==='B02-ch062').bodyPDFPages[0],289);assert.equal(map.units.find(x=>x.id==='B02-ch068').nextPDFPage,301);
 assert.equal(clauses.clauses.length,31);assert(clauses.clauses.every(x=>!x.fullConditionalRuleEncoded&&!x.outcomeValidated));assert(map.units.every(x=>!x.entireUnitApplied));
 const old=await read(resolve(r,'research/liuyao-family-study/B02_CURRENT_UNITS.json'));assert.equal(old.currentCounts.firstPassCompleteSpanUnits,47);assert.equal(old.units.find(x=>x.id==='B02-ch050').disposition,'partial-body-reading-application-open');
});
await check('Released3549-file research package and consumer engine/HTML retain byte-identical intended behavior;source-only staging is absent from site',async()=>{
 const current=await read(resolve(w,'archives/v53-before-liuyao-exam-intent/PACKAGE_MANIFEST.json'));assert.equal(current.files.length,3549);
 for(const f of['engine.js','app.js','content.js','Huyen_Hoc_Cac.html','site/index.html'])assert.equal(sha(await readFile(resolve(r,f))),current.files.find(x=>x.file===f).sha256);
 assert.equal(sha(await readFile(resolve(w,'Huyen_Hoc_Cac.html'))),current.product.sha256);
});
const result={date:'2026-10-28',status:'staged-bounded-question-intent-reference-and19further-first-pass-spans-verified',checks,
 summary:{actualHHCHexCalls:hhcCalls,printedCastFixtures:1,sourceKinBranchLabels:6,sourceChangedBranchLabels:1,namedSourceContexts:data.methods.length,listedPetitionIntentsNotEncoded:5,explicitMissingScopeCases:explicitMissingCases,
 newViewedSourcePositions:37,contentPositions:34,nonRuleLeaves:3,firstPassSpansAdded:19,boundedSourceClauses:31,highResolutionQAViewed:3,newHTTPRequests:0,newOriginalContainers:0},
 fixtureProjection:inspect(values,scope('b02-ch055-literary','self','provincial-metropolitan-examination','examination')),
 fullConditionalRulesEncoded:false,sourceOutcomesValidated:false,wholeCatalogueCompleted:false,consumerChanged:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...result.summary}));
