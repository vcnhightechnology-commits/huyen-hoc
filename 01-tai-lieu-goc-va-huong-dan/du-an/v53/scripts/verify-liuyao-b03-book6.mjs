import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';
import assert from'node:assert/strict';import vm from'node:vm';
import{supportChainCoordinates}from'../research/liuyao-b03-book6/support-chain-reference.mjs';
import{catalogue}from'../research/liuyao-foundations/liuyao-reference.mjs';
const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/liuyao-b03-book6'),qa=resolve(root,'qa/liuyao-b03-book6'),
 archive=resolve(root,'../archives/v53-before-liuyao-b03-book6'),sha=(b,a='sha256')=>createHash(a).update(b).digest('hex'),
 read=async p=>JSON.parse(await readFile(p,'utf8')),checks=[];
function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const manual=await read(resolve(base,'MANUAL_READINGS.json')),units=await read(resolve(base,'BOOK6_CURRENT_UNITS.json')),
 ops=await read(resolve(base,'OPERATIONAL_CLAUSES.json')),clause=await read(resolve(base,'SUPPORT_CHAIN_CLAUSE.json')),
 fixtures=await read(resolve(base,'PRINTED_FIXTURES.json')),pdf=await readFile(resolve(base,manual.sourcePDF)),req=await read(resolve(base,'REQUESTS.json')),
 api=Object.values((await read(resolve(base,'b03-book6-commons-api.json'))).query.pages)[0];
for(const r of req.records){const b=await readFile(resolve(base,r.file));assert.equal(b.length,r.bytes);assert.equal(sha(b),r.sha256);}
test('PDF55093879bytes/65pages and two retained TLS bodies match API revision754088957/size/SHA1/SHA256',()=>{
 assert.equal(pdf.length,55093879);assert.equal(sha(pdf),manual.sourceSHA256);
 assert.equal(sha(pdf),'1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f');
 assert.equal(sha(pdf,'sha1'),api.imageinfo[0].sha1);assert.equal(api.imageinfo[0].size,pdf.length);
 assert.equal(api.imageinfo[0].pagecount,65);assert.equal(api.revisions[0].revid,754088957);
 assert.equal(req.records.length,2);assert(req.records.every(r=>r.executed&&r.status===200&&r.tls.authorized));
});
for(const r of [...manual.records,...manual.qaImages])assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
test('65pages now viewed with scope,63content/2covers;18available question spans, two direct volume openings and no invented final colophon',()=>{
 assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:65},(_,i)=>i+1));
 assert.equal(manual.counts.contentPages,63);assert.equal(manual.counts.inheritedPendingContentPages,7);
 assert.equal(manual.counts.newContentRendersThisRun,56);assert.equal(manual.counts.newCoverRendersThisRun,1);
 assert.deepEqual(manual.directOpenings.map(r=>r.pdfPage),[2,35]);assert.equal(manual.lastContentImage,64);
 assert.equal(manual.directPrintedFinalColophonEstablished,false);assert.equal(units.units.length,18);
 assert.deepEqual(units.units.map(u=>u.question),Array.from({length:18},(_,i)=>i+1));
 assert(units.units.every(u=>u.availableSourceSpanFirstPassRead&&!u.entireUnitApplied));
 assert(units.units[17].terminalAvailableImageNotProofOfUnabridgedEnding);assert.equal(manual.entireBookApplied,false);
});
test('18bounded clauses distinguish source questions and preserve original-support efficacy/strength/hidden premises as uncompiled',()=>{
 assert.equal(ops.clauses.length,18);assert(ops.clauses.every(c=>!c.consumerApplied&&!c.historicalOutcomesValidated));
 assert.equal(ops.sourceInstructionsAreData,true);assert.equal(ops.allBook6ClausesCompiled,false);
 assert.equal(clause.question,3);assert.deepEqual(clause.pdfPages,[9,10,11]);assert.equal(clause.consumerApplied,false);
 assert(clause.notCompiled.includes('Hidden original support'));
});
const cat=catalogue(),ctx={};ctx.window=ctx;vm.createContext(ctx);const engine=await readFile(resolve(root,'engine.js'));
vm.runInContext(engine.toString('utf8'),ctx);let hhcCalls=0;const identity=[];
const context=line=>({sourceContext:'B03-question3-original-support',useLine:line});
test('64actual HHC identity calls anchor private primary charts and explicit selected-use coordinates',()=>{
 for(const c of cat){const v=c.bits.map(b=>b?7:8),r=supportChainCoordinates(v,context(1));
  assert.equal(ctx.HHC_ENGINE.hexNumber(v),c.number);hhcCalls++;assert.equal(r.chart.primary.number,c.number);
  assert.equal(r.selectedUse.line,1);assert.equal(r.effectiveSupportSelection,null);identity.push([c.number,v]);
 }assert.equal(hhcCalls,64);
});
const printed=[];
test('Two actual printed figures63.4→49 and47.3.5→32 pass four HHC number calls plus selected own-change branches',()=>{
 assert.equal(fixtures.fixtureCount,2);assert.equal(fixtures.engineSHA256,sha(engine));
 for(const f of fixtures.results){
  const main=ctx.HHC_ENGINE.hexNumber(f.values),changed=ctx.HHC_ENGINE.hexNumber(f.values.map(v=>v===6?7:v===9?8:v));hhcCalls+=2;
  const r=supportChainCoordinates(f.values,context(3));assert.equal(main,f.primaryNumber);assert.equal(changed,f.changedNumber);
  assert.deepEqual(r.chart.movingLines,f.movingLines);
  for(const c of f.sourceSelectedChanges){assert.equal(r.chart.lines[c.line-1].branch,c.primaryBranch);assert.equal(r.chart.lines[c.line-1].changed.branch,c.changedBranch);}
  assert.equal(f.sourceOutcomeIndependentlyVerified,false);assert.equal(f.sourceMonthDayConvertedToGregorian,false);
  printed.push({id:f.id,primary:main,changed,movingLines:r.chart.movingLines,ownChanges:f.sourceSelectedChanges,sourceHistoricalOutcomeValidated:false});
 }assert.equal(hhcCalls,68);
});
const najia={'111':['子寅辰','午申戌'],'110':['巳卯丑','亥酉未'],'101':['卯丑亥','酉未巳'],
 '100':['子寅辰','午申戌'],'011':['丑亥酉','未巳卯'],'010':['寅辰午','申戌子'],
 '001':['辰午申','戌子寅'],'000':['未巳卯','丑亥酉']},element={子:'水',丑:'土',寅:'木',卯:'木',辰:'土',巳:'火',午:'火',未:'土',申:'金',酉:'金',戌:'土',亥:'水'},cycle=['木','火','土','金','水'];
const branches=bits=>[...najia[bits.slice(0,3).join('')][0],...najia[bits.slice(3).join('')][1]],
 delta=(a,b)=>(cycle.indexOf(element[b])-cycle.indexOf(element[a])+5)%5,
 generates=(a,b)=>delta(a,b)===1,controls=(a,b)=>delta(a,b)===2;
let contexts=0,candidateOrigins=0,staticOrigins=0,movingOrigins=0,ownChangeControlCautions=0,changedOnlySupportNotSubstituted=0;
const digest=createHash('sha256'),controlsSeen={static:null,control:null,nonControl:null,changedOnly:null};
test('24576private selected-line/motion contexts match independent primary-generation and own-return-control oracles',()=>{
 for(const c of cat)for(let mask=0;mask<64;mask++)for(let line=0;line<6;line++){
  const v=c.bits.map((bit,i)=>(mask>>i)&1?bit?9:6:bit?7:8),b=branches(c.bits),cb=branches(c.bits.map((bit,i)=>bit^((mask>>i)&1))),
   r=supportChainCoordinates(v,context(line+1)),expected=b.flatMap((x,i)=>i!==line&&generates(x,b[line])?[i+1]:[]);
  assert.deepEqual(r.candidateOrigins.map(o=>o.line),expected);assert.equal(r.selectedUse.branch,b[line]);
  for(const o of r.candidateOrigins){const i=o.line-1,moving=Boolean((mask>>i)&1),risk=moving?controls(cb[i],b[i]):null;
   assert.equal(o.branch,b[i]);assert.equal(o.moving,moving);assert.equal(o.rawOwnChangeControlsOriginal,risk);
   assert.equal(o.primaryToSelectedUse.generates,true);assert.equal(o.effectiveGeneration,null);assert.equal(o.activation,null);
   if(moving){assert.equal(o.actualOwnChange.branch,cb[i]);assert.equal(o.ownReturnRelation.controls,risk);movingOrigins++;
    if(risk){ownChangeControlCautions++;controlsSeen.control??={values:v,useLine:line+1,origin:o};}
    else controlsSeen.nonControl??={values:v,useLine:line+1,origin:o};
   }else{assert.equal(o.actualOwnChange,null);assert.equal(o.ownReturnRelation,null);staticOrigins++;controlsSeen.static??={values:v,useLine:line+1,origin:o};}
   candidateOrigins++;
  }
  for(let i=0;i<6;i++)if(i!==line&&((mask>>i)&1)&&!generates(b[i],b[line])&&generates(cb[i],b[line])){
   assert(!r.candidateOrigins.some(o=>o.line===i+1));changedOnlySupportNotSubstituted++;
   controlsSeen.changedOnly??={values:v,useLine:line+1,excludedOrigin:i+1};
  }
  assert.equal(r.effectiveSupportSelection,null);assert.equal(r.hiddenOriginalSupportSearched,false);
  assert.equal(r.emptyCandidateListProvesNoRescue,false);assert.equal(r.predictedEvent,null);assert.equal(r.consumerApplied,false);
  digest.update(JSON.stringify([c.number,mask,line+1,r.candidateOrigins.map(o=>[o.line,o.moving,o.rawOwnChangeControlsOriginal])])+'\n');contexts++;
 }assert.equal(contexts,24576);assert.equal(movingOrigins,staticOrigins);assert(ownChangeControlCautions>0&&changedOnlySupportNotSubstituted>0);
 assert(Object.values(controlsSeen).every(Boolean));
});
test('Explicit primary selected-line context required, no invented strength/month adapter, sparse casts reject and inputs preserved',()=>{
 const v=Array(6).fill(7);for(const bad of [null,{},[],context(0),context('2'),{...context(1),monthBranch:'寅'},
  {...context(1),strength:'strong'},{...context(1),sourceContext:'health'},{...context(1),[Symbol('x')]:1}])assert.throws(()=>supportChainCoordinates(v,bad));
 for(const bad of [Array(6),[7,7,7],[7,7,7,7,7,'9']])assert.throws(()=>supportChainCoordinates(bad,context(1)));
 assert.throws(()=>supportChainCoordinates(v,context(1),null));const copy=v.slice();supportChainCoordinates(v,context(1));assert.deepEqual(v,copy);
});
const old=await read(resolve(archive,'PACKAGE_MANIFEST.json')),html=await readFile(resolve(root,'Huyen_Hoc_Cac.html')),
 refs=old.files.filter(f=>/research\/liuyao-[^/]+\/.*reference\.mjs$/.test(f.file));
for(const f of refs)assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
test('Consumer707411bytes and13earlier references unchanged, original-support research absent from site',()=>{
 assert.equal(refs.length,13);assert.equal(html.length,707411);assert.equal(sha(html),old.product.sha256);
 for(const t of ['support-chain-reference.mjs','SUPPORT_CHAIN_CLAUSE.json','BOOK6_CURRENT_UNITS.json'])assert.equal(html.includes(Buffer.from(t)),false);
});
await mkdir(qa,{recursive:true});const summary={actualHHCHexCalls:hhcCalls,actualHHCIdentityCalls:64,printedFixtureCount:2,
 printedHHCHexCalls:4,privateSelectedLineMotionContexts:contexts,candidateOrigins,staticOrigins,movingOrigins,
 ownChangeControlCautions,changedOnlySupportNotSubstituted,graphDigest:digest.digest('hex'),manualRecords:65,
 contentPages:63,coverPages:2,inheritedPendingContentPages:7,inheritedPendingCoverPages:1,newContentRendersThisRun:56,
 newCoverRendersThisRun:1,QAOnlyRenders:2,firstPassAvailableQuestionSpans:18,boundedOperationalClauses:18};
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify({date:'2026-10-27',printedStructureChecks:printed,
 actualHHCIdentityCases:identity,syntheticControls:controlsSeen,sourceHistoricalOutcomesValidated:false,allPrintedAnnotationsCollated:false},null,2)+'\n');
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary,htmlSHA256:sha(html),consumerChanged:false,wholeBookApplied:false},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...summary}));
