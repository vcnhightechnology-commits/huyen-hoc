import {readFile,writeFile,mkdir} from 'node:fs/promises';import {resolve} from 'node:path';
import {createHash} from 'node:crypto';import assert from 'node:assert/strict';import vm from 'node:vm';
import {lostObjectCandidates} from '../research/liuyao-b03-book5/lost-object-reference.mjs';
import {catalogue} from '../research/liuyao-foundations/liuyao-reference.mjs';
const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/liuyao-b03-book5'),qa=resolve(root,'qa/liuyao-b03-book5'),
 archive=resolve(root,'../archives/v53-before-liuyao-b03-book5'),sha=(b,a='sha256')=>createHash(a).update(b).digest('hex'),
 read=async p=>JSON.parse(await readFile(p,'utf8')),checks=[];
function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const manual=await read(resolve(base,'MANUAL_READINGS.json')),units=await read(resolve(base,'BOOK5_CURRENT_UNITS.json')),
 clause=await read(resolve(base,'LOST_OBJECT_ROLE_CLAUSES.json')),ops=await read(resolve(base,'OPERATIONAL_CLAUSES.json')),
 pdf=await readFile(resolve(base,manual.sourcePDF)),req=await read(resolve(base,'REQUESTS.json')),
 api=Object.values((await read(resolve(base,'b03-book5-commons-api.json'))).query.pages)[0];
for(const r of req.records){const b=await readFile(resolve(base,r.file));assert.equal(b.length,r.bytes);assert.equal(sha(b),r.sha256);}
test('Retained PDF35113503bytes and two TLS bodies match raw/API SHA1/size/revision;42pages in container',()=>{
 assert.equal(pdf.length,35113503);assert.equal(sha(pdf),manual.sourceSHA256);
 assert.equal(sha(pdf),'cca4c2ce376c54c6ead6463c72e6f25d6e6e544b3d6488d593415afabc6227a6');
 assert.equal(sha(pdf,'sha1'),api.imageinfo[0].sha1);assert.equal(api.imageinfo[0].size,pdf.length);
 assert.equal(api.imageinfo[0].pagecount,42);assert.equal(api.revisions[0].revid,754088953);
 assert.equal(req.records.length,2);assert(req.records.every(r=>r.executed&&r.status===200&&r.tls.authorized));
});
for(const r of [...manual.records,...manual.qaImages])assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
test('42manual page records/40content/2covers/2QA,12first-passmainspans; every clause and source genealogy still open',()=>{
 assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:42},(_,i)=>i+1));
 assert.deepEqual(manual.counts,{manualRecords:42,contentPages:40,coverPages:2,QAOnlyRenders:2});
 assert.deepEqual(manual.directBoundaries.map(r=>r.pdfPage),[2,22,23,41]);
 assert.deepEqual(manual.qaImages.map(r=>r.pdfPage),[17,34]);assert.equal(manual.ocrUsed,false);assert.deepEqual(manual.unviewedPages,[]);
 assert.equal(units.units.length,12);assert(units.units.every(u=>u.relevantSpanFirstPassRead&&!u.entireUnitApplied));
 assert.equal(units.allSourceClausesApplied,false);assert.equal(manual.entireBookApplied,false);
});
test('Explicit non-wealth exceptions and primary moving cautions retained; medical/ritual/crime claims and boat wording not adjudicated',()=>{
 assert.equal(clause.boundedReading,'失脫不可專以財為用神');assert.equal(clause.parentMovingCautionReading,'故忌財動');
 assert.equal(clause.childMovingCautionReading,'故忌父爻動');assert.equal(clause.consumerApplied,false);
 assert.equal(ops.clauses.length,13);assert(ops.clauses.every(c=>!c.consumerApplied&&!c.historicalOutcomesValidated));
 assert.equal(ops.sourceInstructionsAreData,true);assert.equal(ops.allBook5ClausesCompiled,false);
});
const cat=catalogue(),ctx={};ctx.window=ctx;vm.createContext(ctx);vm.runInContext(await readFile(resolve(root,'engine.js'),'utf8'),ctx);
const context=kind=>({sourceContext:'B03-volume11-lost-objects',objectKind:kind});
const roles={cash:'妻財',boat:'父母',vehicle:'父母',garment:'父母',headwear:'父母',document:'父母',memorial:'父母',bird:'子孫',beast:'子孫'};
const najia={'111':['子寅辰','午申戌'],'110':['巳卯丑','亥酉未'],'101':['卯丑亥','酉未巳'],
 '100':['子寅辰','午申戌'],'011':['丑亥酉','未巳卯'],'010':['寅辰午','申戌子'],
 '001':['辰午申','戌子寅'],'000':['未巳卯','丑亥酉']};
const element={子:'水',丑:'土',寅:'木',卯:'木',辰:'土',巳:'火',午:'火',未:'土',申:'金',酉:'金',戌:'土',亥:'水'},
 cycle=['木','火','土','金','水'],kinNames=['兄弟','子孫','妻財','官鬼','父母'];
const kin=(palace,branch)=>kinNames[(cycle.indexOf(element[branch])-cycle.indexOf(palace)+5)%5],
 branches=bits=>[...najia[bits.slice(0,3).join('')][0],...najia[bits.slice(3).join('')][1]];
let hhcCalls=0,staticObjectContexts=0;const identities=[];
test('64actual HHC calls and576private static object contexts preserve9explicit IDs/3source kin groups and all candidates',()=>{
 for(const c of cat){const v=c.bits.map(b=>b?7:8),b=branches(c.bits);assert.equal(ctx.HHC_ENGINE.hexNumber(v),c.number);hhcCalls++;
  for(const [kind,desired]of Object.entries(roles)){
   const r=lostObjectCandidates(v,context(kind));assert.equal(r.role.kin,desired);assert.equal(r.availability.chart.primary.number,c.number);
   assert.deepEqual(r.availability.visibleCandidates.map(l=>l.line),b.flatMap((x,i)=>kin(c.palaceElement,x)===desired?[i+1]:[]));
   assert.deepEqual(r.availability.changedCandidates,[]);assert.equal(r.availability.effectiveUseGodSelection,null);
   assert.equal(r.sourceCautionMovingLines?.length??null,kind==='cash'?null:0);staticObjectContexts++;
  }identities.push([c.number,v]);
 }assert.equal(hhcCalls,64);assert.equal(staticObjectContexts,576);
});
const controls=[];
test('Càn gives wealth2,parents3/6,child1; primary moving wealth2 or parent3 caution by object, changed-only parent never substitutes',()=>{
 const v=Array(6).fill(7),cash=lostObjectCandidates(v,context('cash')),doc=lostObjectCandidates(v,context('document')),bird=lostObjectCandidates(v,context('bird'));
 assert.deepEqual(cash.availability.visibleCandidates.map(l=>l.line),[2]);assert.deepEqual(doc.availability.visibleCandidates.map(l=>l.line),[3,6]);
 assert.deepEqual(bird.availability.visibleCandidates.map(l=>l.line),[1]);
 const a=lostObjectCandidates([7,9,7,7,7,7],context('document')),b=lostObjectCandidates([7,7,9,7,7,7],context('bird')),
 c=lostObjectCandidates([9,7,7,7,7,7],context('bird'));
 assert.deepEqual(a.sourceCautionMovingLines.map(l=>l.line),[2]);assert.deepEqual(b.sourceCautionMovingLines.map(l=>l.line),[3]);
 assert.equal(c.availability.chart.lines[0].changed.kin,'父母');assert.deepEqual(c.sourceCautionMovingLines,[]);
 for(const r of [cash,doc,bird,a,b,c])controls.push({synthetic:true,notAPrintedCoinCast:true,result:r});
});
let contexts=0,cautionContexts=0,cautionFlags=0,hiddenSearchContexts=0,multipleShownContexts=0,movingAnnotations=0;
const digest=createHash('sha256');
test('12288private chart/object-group contexts match independent literal NaJia/kin oracles on primary and changed layers',()=>{
 for(const c of cat)for(let mask=0;mask<64;mask++){
  const v=c.bits.map((bit,i)=>(mask>>i)&1?bit?9:6:bit?7:8),b=branches(c.bits),cb=branches(c.bits.map((bit,i)=>bit^((mask>>i)&1)));
  for(const kind of ['cash','document','bird']){
   const desired=roles[kind],r=lostObjectCandidates(v,context(kind)),a=r.availability,
    expectedPrimary=b.flatMap((x,i)=>kin(c.palaceElement,x)===desired?[i+1]:[]),
    expectedChanged=cb.flatMap((x,i)=>(mask>>i)&1&&kin(c.palaceElement,x)===desired?[i+1]:[]),
    cautionKin=kind==='cash'?null:kind==='document'?'妻財':'父母',
    expectedCautions=cautionKin===null?null:b.flatMap((x,i)=>(mask>>i)&1&&kin(c.palaceElement,x)===cautionKin?[i+1]:[]);
   assert.deepEqual(a.visibleCandidates.map(l=>l.line),expectedPrimary);assert.deepEqual(a.changedCandidates.map(l=>l.line),expectedChanged);
   assert.deepEqual(r.sourceCautionMovingLines?.map(l=>l.line)??null,expectedCautions);
   assert.equal(a.structuralHiddenSearchNeeded,expectedPrimary.length+expectedChanged.length===0);
   for(const l of a.chart.lines){assert.equal(l.kin,kin(c.palaceElement,b[l.line-1]));
    if((mask>>(l.line-1))&1){assert.equal(l.changed.branch,cb[l.line-1]);assert.equal(l.changed.kin,kin(c.palaceElement,cb[l.line-1]));movingAnnotations++;}
    else assert.equal(l.changed,null);
   }
   if(expectedCautions?.length){cautionContexts++;cautionFlags+=expectedCautions.length;}
   if(a.structuralHiddenSearchNeeded)hiddenSearchContexts++;if(expectedPrimary.length+expectedChanged.length>1)multipleShownContexts++;
   for(const key of ['effectiveUseGodSelection','searchLocation','suspectIdentity','recoveryDate','recoveryOutcome','fullStrengthAdjudication','predictedEvent'])assert.equal(r[key],null);
   assert.equal(r.consumerApplied,false);digest.update(JSON.stringify([c.number,mask,kind,expectedPrimary,expectedChanged,expectedCautions])+'\n');contexts++;
  }
 }assert.equal(contexts,12288);assert.equal(movingAnnotations,36864);assert(cautionFlags>cautionContexts&&hiddenSearchContexts>0&&multipleShownContexts>0);
});
test('Missing or unsupported object kind/domain, added gender/strength, sparse or malformed casts reject; no fallback to wealth or input mutation',()=>{
 const v=Array(6).fill(7);for(const bad of [null,{},[],{sourceContext:'B03-volume11-lost-objects'},context('phone'),context('__proto__'),
  {...context('bird'),sourceContext:'lost-person'},{...context('cash'),strength:1},{...context('boat'),suspectGender:'male'},
  {...context('cash'),[Symbol('x')]:1}])assert.throws(()=>lostObjectCandidates(v,bad));
 for(const bad of [Array(6),[7,7,7],[7,7,7,7,7,'9']])assert.throws(()=>lostObjectCandidates(bad,context('cash')));
 assert.throws(()=>lostObjectCandidates(v,context('cash'),null));const copy=v.slice();lostObjectCandidates(v,context('cash'));assert.deepEqual(v,copy);
});
const old=await read(resolve(archive,'PACKAGE_MANIFEST.json')),html=await readFile(resolve(root,'Huyen_Hoc_Cac.html')),
 refs=old.files.filter(f=>/research\/liuyao-[^/]+\/.*reference\.mjs$/.test(f.file));
for(const f of refs)assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
test('Consumer707411bytes and12earlier private references unchanged; private lost-object module absent from product',()=>{
 assert.equal(html.length,707411);assert.equal(sha(html),old.product.sha256);assert.equal(refs.length,12);
 for(const token of ['lost-object-reference.mjs','LOST_OBJECT_ROLE_CLAUSES.json','BOOK5_CURRENT_UNITS.json'])assert.equal(html.includes(Buffer.from(token)),false);
});
const issues=await read(resolve(base,'TEXT_ISSUES.json'));
test('Conflicting boat ordinal wording kept open without silent correction, source accusation/medical/ritual wording not consumer rules',()=>{
 assert.equal(issues.issues.length,1);assert.equal(issues.issues[0].correctionApplied,false);
 assert(issues.issues[0].readings.includes('初當船尾')&&issues.issues[0].readings.includes('青龍初是船頭'));
 assert(ops.clauses.some(c=>c.id==='no-suspect-identification')&&ops.clauses.some(c=>c.id==='pox-history')&&ops.clauses.some(c=>c.id==='spirit-claims'));
});
await mkdir(qa,{recursive:true});const summary={actualHHCHexCalls:hhcCalls,staticObjectContexts,privatePrimaryMotionObjectContexts:contexts,
 movingAnnotations,cautionContexts,cautionFlags,hiddenSearchContexts,multipleShownContexts,graphDigest:digest.digest('hex'),
 explicitObjectKinds:9,sourceKinGroups:3,manualRecords:42,contentPages:40,coverPages:2,QAOnlyRenders:2,
 firstPassMainUnits:12,boundedOperationalClauses:13,openTextIssues:1};
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify({date:'2026-10-27',syntheticControls:controls,
 actualHHCIdentityCases:identities,sourcePrintedCoinCastFixtures:0,historicalOutcomesValidated:false},null,2)+'\n');
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary,htmlSHA256:sha(html),consumerChanged:false,wholeBookApplied:false},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...summary}));
