import assert from'node:assert/strict';import{readFileSync,writeFileSync,existsSync}from'node:fs';
import{createHash}from'node:crypto';import{resolve}from'node:path';
import{SOURCE_ID,PAIR_FRAME,MONTH_FRAME,HIDDEN_FRAME,sourceUnionPair,sourceUnionMonth,sourceHiddenUnion}from'./union-reference.mjs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8'));
const sha=b=>createHash('sha256').update(b).digest('hex');
const freeze=read('./PREIMPLEMENTATION_FREEZE.json');
for(const x of freeze.files){const b=readFileSync(new URL(x.file,import.meta.url));assert.equal(b.length,x.bytes);assert.equal(sha(b),x.sha256);}
const expected=read('./EXPECTED_BEFORE_IMPLEMENTATION.json'),manual=read('./MANUAL_TABLES.json');
let pairFrames=0,listedPairFrames=0,nullInvariants=0;
const checkNull=r=>{for(const key of expected.neverInfer){assert.equal(r[key],null);nullInvariants++;}assert.equal(r.sourceEfficacyValidated,false);assert.ok(Object.isFrozen(r));};
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
for(const from of branches)for(const to of branches){
 const r=sourceUnionPair({sourceID:SOURCE_ID,frameID:PAIR_FRAME,from,to});
 const isListed=expected.sixPairs.some(([a,b])=>(a===from&&b===to)||(b===from&&a===to));
 assert.equal(r.listedCoordinatePair,isListed);if(isListed)listedPairFrames++;
 const directed=expected.orderedPairs.find(x=>x.from===from&&x.to===to);assert.equal(r.directedSourcePhrase,directed?.phrase??null);
 if(directed)assert.equal(r.directedSourceVoice,'天元變化書云');checkNull(r);pairFrames++;
}
assert.equal(pairFrames,144);assert.equal(listedPairFrames,12);
for(const[from,to]of expected.explicitNonpairs)assert.equal(sourceUnionPair({sourceID:SOURCE_ID,frameID:PAIR_FRAME,from,to}).listedCoordinatePair,false);
for(const[sourceMonth,builtBranch,stationBranch]of expected.sourceMonths){const r=sourceUnionMonth({sourceID:SOURCE_ID,frameID:MONTH_FRAME,sourceMonth});assert.equal(r.builtBranch,builtBranch);assert.equal(r.stationBranch,stationBranch);checkNull(r);}
const input=c=>({sourceID:SOURCE_ID,frameID:HIDDEN_FRAME,caseID:c.caseID,anchorKind:manual.hiddenRows.find(r=>r.id===c.caseID).anchorKind,anchor:c.anchor,anchorBasis:'source-declared-birth-anchor',targetSeen:c.targetSeen,partnerSeen:c.partnerSeen});
for(const c of expected.hiddenCases)assert.equal(sourceHiddenUnion(input(c)).declaredCoordinateGate,c.expectedGate,c.id);
let hiddenFrames=0;
for(const row of manual.hiddenRows)for(const targetSeen of[true,false,null])for(const partnerSeen of[true,false,null]){
 const r=sourceHiddenUnion(input({caseID:row.id,anchor:row.anchor,targetSeen,partnerSeen}));
 const gate=targetSeen===true||partnerSeen===false?false:targetSeen===false&&partnerSeen===true?true:null;
 assert.equal(r.declaredCoordinateGate,gate);assert.equal(r.appliedToNatalChart,false);assert.equal(r.anchorPillar,null);assert.equal(r.observationHorizon,null);checkNull(r);hiddenFrames++;
}
let unsupported=0,invalid=0;
const pair={sourceID:SOURCE_ID,frameID:PAIR_FRAME,from:'子',to:'丑'},month={sourceID:SOURCE_ID,frameID:MONTH_FRAME,sourceMonth:1},hidden=input(expected.hiddenCases[0]);
for(const[fn,good]of[[sourceUnionPair,pair],[sourceUnionMonth,month],[sourceHiddenUnion,hidden]]){
 for(const key of Object.keys(good)){const x={...good};delete x[key];assert.equal(fn(x),null);unsupported++;}
 for(const x of[null,[],new Date(),Object.create(good),{...good,sourceID:'other-tradition'},{...good,frameID:'calendar-date'},{...good,chart:['甲子']},{...good,[Symbol()]:true}]){assert.equal(fn(x),null);unsupported++;}
}
for(const anchorBasis of['year','day','unknown']){assert.equal(sourceHiddenUnion({...hidden,anchorBasis}),null);unsupported++;}
assert.equal(sourceHiddenUnion({...hidden,caseID:'hidden-noble'}),null);unsupported++;
for(const [fn,input]of[
 [sourceUnionPair,{...pair,from:'戍'}],[sourceUnionPair,{...pair,to:'A'}],
 [sourceUnionMonth,{...month,sourceMonth:0}],[sourceUnionMonth,{...month,sourceMonth:13}],[sourceUnionMonth,{...month,sourceMonth:1.5}],
 [sourceHiddenUnion,{...hidden,targetSeen:0}],[sourceHiddenUnion,{...hidden,partnerSeen:'true'}],
 [sourceHiddenUnion,{...hidden,anchorKind:'branch'}],[sourceHiddenUnion,{...hidden,anchor:'甲子'}]]){assert.throws(()=>fn(input));invalid++;}
const actual=read('./ACTUAL_RUNTIME.json');assert.equal(actual.actualPartnerTableQueries,12);assert.equal(actual.actualLuQueries,1);assert.equal(actual.actualNatalCharts,0);
assert.equal(actual.freezeSHA256,sha(readFileSync(new URL('./PREIMPLEMENTATION_FREEZE.json',import.meta.url))));
assert.equal(actual.scriptSHA256,sha(readFileSync(new URL('./run-actual-once.mjs',import.meta.url))));
for(const x of actual.partners){assert.ok(x.matches);assert.equal(x.actual,expected.actualLunarExpected.orderedPartners[x.branch]);}
assert.equal(actual.lu.actual,'寅');assert.ok(actual.lu.matches);
const w=existsSync(resolve(import.meta.dirname,'../../v53'))?resolve(import.meta.dirname,'../..'):resolve(import.meta.dirname,'../../..');
if(existsSync(resolve(w,actual.libraryFile)))assert.equal(sha(readFileSync(resolve(w,actual.libraryFile))),actual.librarySHA256);
const chapter=read('./CHAPTER_DISPOSITIONS.json'),clean=readFileSync(new URL('./CHAPTER_CLEAN.txt',import.meta.url),'utf8');
assert.equal(sha(Buffer.from(clean)),chapter.cleanSHA256);assert.equal([...clean].length,1087);assert.equal(clean.length,1090);
let end=0;for(const r of chapter.records){assert.equal(r.startCodepoint,end);assert.equal([...clean].slice(r.startCodepoint,r.endCodepointExclusive).join(''),r.literalDigital);assert.equal(r.wholeUnitApplied,false);end=r.endCodepointExclusive;}
assert.equal(end,[...clean].length);assert.equal(chapter.records.length,14);
assert.equal(chapter.wholeChapterApplied,false);assert.equal(manual.outcomesValidated,false);
const output={date:'2026-10-29',passed:true,groups:8,frozenFiles:5,pairFrames,listedOrderedPairFrames:listedPairFrames,sourceMonthQueries:12,sourceDirectionalPhrases:12,expectedHiddenCases:10,hiddenTernaryFrames:hiddenFrames,nullInvariants,unsupportedRequests:unsupported,invalidInputs:invalid,editorialChapterUnits:14,digitalCleanCodepoints:1087,digitalUTF16Units:1090,retainedActualPartnerTableQueries:12,retainedActualLuQueries:1,newEngineCallsDuringTests:0,newNatalCharts:0,wholeChapterApplied:false,consumerChanged:false};
if(process.argv.includes('--write-results'))writeFileSync(new URL('./REFERENCE_RESULTS.json',import.meta.url),JSON.stringify(output,null,2)+'\n');console.log(JSON.stringify(output));
