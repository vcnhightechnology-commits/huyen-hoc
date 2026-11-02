import assert from'node:assert/strict';import{readFileSync,writeFileSync,existsSync}from'node:fs';import{resolve}from'node:path';import{createHash}from'node:crypto';
import{SOURCE_ID,FRAME_ID,sourceStarCoordinate}from'./star-reference.mjs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8')),sha=b=>createHash('sha256').update(b).digest('hex');
for(const x of read('./PREIMPLEMENTATION_FREEZE.json').files){const raw=readFileSync(new URL(x.file,import.meta.url));assert.equal(raw.length,x.bytes);assert.equal(sha(raw),x.sha256);}
const expected=read('./EXPECTED_BEFORE_IMPLEMENTATION.json');
const base={sourceID:SOURCE_ID,frameID:FRAME_ID,anchorBasis:'source-declared-anchor-branch'};
let invariants=0;
const check=r=>{for(const key of expected.neverInfer){assert.equal(r[key],null);invariants++;}assert.equal(r.naYinSourcePillar,null);assert.equal(r.anchorPillar,null);assert.equal(r.appliedToNatalChart,false);assert.equal(r.sourceEfficacyValidated,false);assert.equal(r.remainingSourceConditionsOpen,true);assert.equal(r.requiresFullTriadFormed,null);assert.equal(r.fullTriadFormationEvaluated,false);assert.ok(Object.isFrozen(r));};
for(const c of expected.selectedCases){const{id,expectedCoordinate,expectedQualifiedGate,...input}=c;const r=sourceStarCoordinate({...base,...input});assert.equal(r.rawCoordinateMatches,expectedCoordinate,id);if('expectedQualifiedGate'in c)assert.equal(r.sourceSelectedCoordinateGate,expectedQualifiedGate,id);check(r);}
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];let frames=0,rawPositive=0,qualifiedXianchi=0,unknownXianchi=0;
for(const row of expected.sourceRows)for(const sourceAnchorBranch of branches)for(const targetBranch of branches)for(const variant of[{star:'general'},{star:'canopy'},...[true,false,null].map(naYinGroupMatch=>({star:'xianchi',naYinGroupMatch}))]){
 const r=sourceStarCoordinate({...base,groupID:row.groupID,sourceAnchorBranch,targetBranch,...variant});
 const coordinate=row.branches.includes(sourceAnchorBranch)&&targetBranch===row[variant.star];
 assert.equal(r.rawCoordinateMatches,coordinate);if(coordinate)rawPositive++;
 const gate=variant.star==='xianchi'?(coordinate?variant.naYinGroupMatch:false):coordinate;
 assert.equal(r.sourceSelectedCoordinateGate,gate);
 if(variant.star==='xianchi'&&gate===true)qualifiedXianchi++;
 if(variant.star==='xianchi'&&gate===null)unknownXianchi++;
 check(r);frames++;
}
assert.equal(frames,2880);assert.equal(rawPositive,60);assert.equal(qualifiedXianchi,12);assert.equal(unknownXianchi,12);
const good={...base,groupID:'fire',star:'xianchi',sourceAnchorBranch:'寅',targetBranch:'卯',naYinGroupMatch:true};
const unknownCases=[
 [{...good,sourceAnchorBranch:null},null,null],
 [{...good,targetBranch:null},null,null],
 [{...good,sourceAnchorBranch:null,targetBranch:'子'},false,false],
 [{...good,sourceAnchorBranch:'子',targetBranch:null},false,false],
 [{...good,sourceAnchorBranch:null,naYinGroupMatch:false},null,false],
 [{...good,sourceAnchorBranch:null,targetBranch:null,naYinGroupMatch:null},null,null]];
for(const[input,coordinate,gate]of unknownCases){const r=sourceStarCoordinate(input);assert.equal(r.rawCoordinateMatches,coordinate);assert.equal(r.sourceSelectedCoordinateGate,gate);check(r);}
let unsupported=0,invalid=0;
for(const key of Object.keys(good)){const x={...good};delete x[key];assert.equal(sourceStarCoordinate(x),null);unsupported++;}
for(const x of[null,[],new Date(),Object.create(good),{...good,sourceID:'modern-shensha'},{...good,frameID:'calendar'},{...good,anchorBasis:'year'},
 {...good,anchorBasis:'day'},{...good,groupID:'four-earth'},{...good,star:'fortune'},{...good,naYinPillar:'year'},{...good,calendarDate:'2026-10-29'},
 {...good,star:'general'},{...good,[Symbol()]:true}]){assert.equal(sourceStarCoordinate(x),null);unsupported++;}
for(const patch of[{sourceAnchorBranch:'戍'},{targetBranch:'卯日'},{targetBranch:1},{naYinGroupMatch:1},{naYinGroupMatch:'true'}]){assert.throws(()=>sourceStarCoordinate({...good,...patch}));invalid++;}
const actual=read('./ACTUAL_RUNTIME.json');assert.equal(actual.actualNaYinTableQueries,2);assert.equal(actual.actualStemElementTableQueries,2);assert(actual.cases.every(x=>x.matches));
assert.equal(actual.cases[0].actualStemElement,actual.cases[1].actualStemElement);assert.notEqual(actual.cases[0].actualNaYin.slice(-1),actual.cases[1].actualNaYin.slice(-1));assert.equal(actual.sourceGoldMeaningAdjudicated,false);assert.equal(actual.actualNatalCharts,0);
assert.equal(actual.freezeSHA256,sha(readFileSync(new URL('./PREIMPLEMENTATION_FREEZE.json',import.meta.url))));assert.equal(actual.scriptSHA256,sha(readFileSync(new URL('./run-actual-once.mjs',import.meta.url))));
const w=existsSync(resolve(import.meta.dirname,'../../v53'))?resolve(import.meta.dirname,'../..'):resolve(import.meta.dirname,'../../..');if(existsSync(resolve(w,actual.libraryFile)))assert.equal(sha(readFileSync(resolve(w,actual.libraryFile))),actual.librarySHA256);
const chapter=read('./CHAPTER_DISPOSITIONS.json'),clean=readFileSync(new URL('./CHAPTERS_CLEAN.txt',import.meta.url),'utf8');assert.equal([...clean].length,899);assert.equal(clean.length,902);assert.equal(sha(Buffer.from(clean)),chapter.cleanSHA256);let end=0;
for(const x of chapter.records){assert.equal(x.startCodepoint,end);assert.equal([...clean].slice(x.startCodepoint,x.endCodepointExclusive).join(''),x.literalDigital);assert.equal(x.wholeUnitApplied,false);end=x.endCodepointExclusive;}assert.equal(end,899);assert.equal(chapter.records.length,38);assert.equal(chapter.wholeChaptersApplied,false);
const out={date:'2026-10-29',passed:true,groups:8,frozenFiles:5,expectedCases:6,coordinateFrames:frames,rawPositiveCoordinateFrames:rawPositive,qualifiedXianchiFrames:qualifiedXianchi,unqualifiedXianchiUnknownFrames:unknownXianchi,unknownCoordinateCases:unknownCases.length,nullInvariants:invariants,unsupportedRequests:unsupported,invalidInputs:invalid,editorialUnits:38,digitalCodepoints:899,digitalUTF16Units:902,retainedActualNaYinQueries:2,retainedActualStemElementQueries:2,newEngineCallsDuringTests:0,actualNatalCharts:0,sourceGoldMeaningAdjudicated:false,wholeChaptersApplied:false,consumerChanged:false};
if(process.argv.includes('--write-results'))writeFileSync(new URL('./REFERENCE_RESULTS.json',import.meta.url),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
