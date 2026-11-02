import assert from'node:assert/strict';import{readFileSync,writeFileSync,existsSync}from'node:fs';import{resolve}from'node:path';import{createHash}from'node:crypto';
import{SOURCE_ID,FRAME_ID,sourceTriadPremises}from'./triad-reference.mjs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8')),sha=b=>createHash('sha256').update(b).digest('hex');
for(const x of read('./PREIMPLEMENTATION_FREEZE.json').files){const b=readFileSync(new URL(x.file,import.meta.url));assert.equal(b.length,x.bytes);assert.equal(sha(b),x.sha256);}
const expected=read('./EXPECTED_BEFORE_IMPLEMENTATION.json'),manual=read('./MANUAL_TABLES.json');
const base={sourceID:SOURCE_ID,frameID:FRAME_ID,anchorBasis:'source-declared-birth-stem'};
const input=c=>({...base,groupID:c.groupID,slots:c.slots,anchorStem:c.anchorStem});
let nullInvariants=0;
const check=r=>{for(const key of expected.neverInfer){assert.equal(r[key],null);nullInvariants++;}assert.equal(r.anchorPillar,null);assert.equal(r.appliedToNatalChart,false);assert.equal(r.sourceEfficacyValidated,false);assert.ok(Object.isFrozen(r));assert.ok(Object.isFrozen(r.requiredBranches));};
for(const c of expected.cases){const r=sourceTriadPremises(input(c));assert.equal(r.sourceCompletenessPremise,c.expectedComplete,c.id);assert.equal(r.missingThreeBranchExclusion,c.expectedMissingExclusion,c.id);if('expectedThreeLu'in c)assert.equal(r.sourceThreeLuCoordinateGate,c.expectedThreeLu,c.id);if('expectedSourceRole'in c)assert.equal(r.sourceRoleLabel,c.expectedSourceRole,c.id);check(r);}
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];let exhaustiveFrames=0;const completeCounts=Object.fromEntries(manual.groups.map(g=>[g.id,0]));
for(const a of branches)for(const b of branches)for(const c of branches)for(const d of branches){
 const slots=[a,b,c,d];
 for(const group of manual.groups){const r=sourceTriadPremises({...base,groupID:group.id,slots,anchorStem:'丙'});assert.notEqual(r.sourceCompletenessPremise,null);if(r.sourceCompletenessPremise)completeCounts[group.id]++;check(r);exhaustiveFrames++;}
}
assert.equal(exhaustiveFrames,expected.exhaustiveKnownBranchFrameCount*5);
for(const g of manual.groups)assert.equal(completeCounts[g.id],g.threeBranchGroup?expected.analyticCompleteCoordinateFramesPerThreeBranchGroup:expected.analyticCompleteCoordinateFramesEarth,g.id);
let partialFrames=0;
for(const group of manual.groups)for(let missing=0;missing<=group.branches.length;missing++){
 const known=group.branches.slice(0,group.branches.length-missing),outside=branches.find(b=>!group.branches.includes(b));
 for(let unknown=0;unknown<=4-known.length;unknown++){
  const slots=[...known,...Array(unknown).fill(null),...Array(4-known.length-unknown).fill(outside)];
  const r=sourceTriadPremises({...base,groupID:group.id,slots,anchorStem:'丁'});
  assert.equal(r.sourceCompletenessPremise,missing===0?true:missing>unknown?false:null);check(r);partialFrames++;
 }
}
for(const group of manual.groups){const slots=[...group.branches];while(slots.length<4)slots.push(group.branches[0]);for(const anchorStem of['丙','丁'])assert.equal(sourceTriadPremises({...base,groupID:group.id,slots,anchorStem}).sourceRoleLabel,group.sourceRoleForBingDing);}
let unsupported=0,invalid=0;const good=input(expected.cases[0]);
for(const key of Object.keys(good)){const x={...good};delete x[key];assert.equal(sourceTriadPremises(x),null);unsupported++;}
for(const x of[null,[],new Date(),Object.create(good),{...good,sourceID:'B02'},{...good,frameID:'lunar-calendar'},{...good,anchorBasis:'day'},
 {...good,anchorBasis:'year'},{...good,groupID:'half-triad'},{...good,calendarDate:'2026-10-29'},{...good,beneficPresent:true},{...good,[Symbol()]:true}]){assert.equal(sourceTriadPremises(x),null);unsupported++;}
for(const patch of[{slots:['申','子','辰']},{slots:['申','子','辰','午','午']},{slots:['申','子','申',undefined]},{slots:['申','子','戍','辰']},{slots:[,'子','辰','午']},{slots:'申子辰午'},{anchorStem:'丙子'},{anchorStem:null}]){assert.throws(()=>sourceTriadPremises({...good,...patch}));invalid++;}
const actual=read('./ACTUAL_RUNTIME.json');assert.equal(actual.actualHHCTenGodCalls,20);assert.equal(actual.actualLuTableQueries,2);assert.equal(actual.actualNatalCharts,0);assert(actual.tenGod.every(x=>x.matches)&&actual.lu.every(x=>x.matches));
assert.equal(actual.freezeSHA256,sha(readFileSync(new URL('./PREIMPLEMENTATION_FREEZE.json',import.meta.url))));assert.equal(actual.scriptSHA256,sha(readFileSync(new URL('./run-actual-once.mjs',import.meta.url))));
const w=existsSync(resolve(import.meta.dirname,'../../v53'))?resolve(import.meta.dirname,'../..'):resolve(import.meta.dirname,'../../..');
for(const x of actual.engineFiles)if(existsSync(resolve(w,x.file)))assert.equal(sha(readFileSync(resolve(w,x.file))),x.sha256);
if(existsSync(resolve(w,actual.libraryFile)))assert.equal(sha(readFileSync(resolve(w,actual.libraryFile))),actual.librarySHA256);
const earth=actual.tenGod.filter(x=>x.targetElement==='土');assert.equal(earth.filter(x=>x.actual==='Thực Thần').length,2);assert.equal(earth.filter(x=>x.actual==='Thương Quan').length,2);
const chapter=read('./CHAPTER_DISPOSITIONS.json'),clean=readFileSync(new URL('./CHAPTER_CLEAN.txt',import.meta.url),'utf8');assert.equal([...clean].length,807);assert.equal(clean.length,807);assert.equal(sha(Buffer.from(clean)),chapter.cleanSHA256);let end=0;for(const x of chapter.records){assert.equal(x.startCodepoint,end);assert.equal([...clean].slice(x.startCodepoint,x.endCodepointExclusive).join(''),x.literalDigital);assert.equal(x.wholeUnitApplied,false);end=x.endCodepointExclusive;}assert.equal(end,807);assert.equal(chapter.records.length,22);assert.ok(clean.includes('故申子申為水局'));assert.equal(chapter.wholeChapterApplied,false);
const output={date:'2026-10-29',passed:true,groups:8,frozenFiles:5,expectedCases:12,exhaustiveKnownSlotFrames:12**4,exhaustiveGroupQueries:exhaustiveFrames,analyticCompleteCounts:completeCounts,partialUnknownFrames:partialFrames,nullInvariants,unsupportedRequests:unsupported,invalidInputs:invalid,editorialChapterUnits:22,digitalCleanCodepoints:807,retainedActualHHCTenGodCalls:20,retainedActualLuTableQueries:2,newEngineCallsDuringTests:0,actualNatalCharts:0,wholeChapterApplied:false,consumerChanged:false};
if(process.argv.includes('--write-results'))writeFileSync(new URL('./REFERENCE_RESULTS.json',import.meta.url),JSON.stringify(output,null,2)+'\n');console.log(JSON.stringify(output));
