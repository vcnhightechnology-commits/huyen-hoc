import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';import vm from 'node:vm';
import {homeSymbolCoordinates} from '../research/liuyao-b03-book4/home-symbol-reference.mjs';
import {catalogue} from '../research/liuyao-foundations/liuyao-reference.mjs';
const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/liuyao-b03-book4'),
 qa=resolve(root,'qa/liuyao-b03-book4'),archive=resolve(root,'../archives/v53-before-liuyao-b03-book4');
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=b=>createHash('sha256').update(b).digest('hex');
const checks=[];function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const manual=await read(resolve(base,'MANUAL_READINGS.json')),units=await read(resolve(base,'BOOK4_CURRENT_UNITS.json')),
 ops=await read(resolve(base,'OPERATIONAL_CLAUSES.json')),clause=await read(resolve(base,'HOME_SYMBOL_CLAUSES.json')),
 api=Object.values((await read(resolve(base,'b03-book4-commons-api.json'))).query.pages)[0],
 req=await read(resolve(base,'REQUESTS.json')),pdf=await readFile(resolve(base,manual.sourcePDF));
for(const r of req.records){const b=await readFile(resolve(base,r.file));assert.equal(b.length,r.bytes);assert.equal(sha(b),r.sha256);}
test('One retained original PDF and two TLS-verified bodies newly enter release; no new HTTP in this run',()=>{
 assert.equal(pdf.length,57017134);assert.equal(sha(pdf),manual.sourceSHA256);
 assert.equal(sha(pdf),'5f8bb92f28120fa4c2c4d629ae8bad9f785dc02324f15f285085c99ab7ffadaf');
 assert.equal(createHash('sha1').update(pdf).digest('hex'),api.imageinfo[0].sha1);
 assert.equal(api.revisions[0].revid,754088947);assert.equal(api.imageinfo[0].size,pdf.length);assert.equal(api.imageinfo[0].pagecount,67);
 assert.equal(req.records.length,2);assert(req.records.every(r=>r.executed&&r.status===200&&r.tls.authorized));
 assert.equal(manual.counts.newOriginalPDFsToRelease,1);assert.equal(manual.counts.retainedHTTPBodiesNewToRelease,2);assert.equal(manual.counts.newHTTPBodiesThisRun,0);
});
for(const r of [...manual.records,...manual.qaImages])assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
test('All67physical pages viewed;17inherited pending/48new content/2covers and2QA crops counted separately',()=>{
 assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:67},(_,i)=>i+1));
 assert.equal(manual.records.filter(r=>r.inheritedPendingReading).length,17);
 assert.equal(manual.records.filter(r=>r.newLocalRenderThisRun).length,50);
 assert.equal(manual.counts.newContentRendersThisRun,48);assert.equal(manual.counts.contentImagesNewToRelease,65);
 assert.equal(manual.counts.coverImagesNewToRelease,2);assert.equal(manual.qaImages.length,2);
 assert.deepEqual(manual.qaImages.map(r=>r.pdfPage),[40,41]);
 assert.deepEqual(manual.directBoundaries.map(r=>r.pdfPage),[2,21,22,44,45,66]);
 assert.equal(manual.ocrUsed,false);assert.deepEqual(manual.unviewedPages,[]);assert.equal(manual.entireBookApplied,false);
});
test('11main units plus one nested supplement span across volumes8/9/10, no duplicate page or whole-unit application',()=>{
 assert.equal(units.units.length,11);assert(units.units.every(u=>u.relevantSpanFirstPassRead&&!u.entireUnitApplied));
 assert.deepEqual(units.units.filter(u=>u.textualVolume===8).map(u=>u.heading),['種作','蠶桑','六畜','求名','仕宦']);
 assert.deepEqual(units.units.filter(u=>u.textualVolume===9).map(u=>u.heading),['求財','家宅']);
 assert.deepEqual(units.units.filter(u=>u.textualVolume===10).map(u=>u.heading),['墳墓','求師','學館','詞訟']);
 assert.equal(units.subsections.length,1);assert.equal(units.counts.newOrCompletedMainSpans,7);
 assert.equal(units.counts.entireUnitsApplied,0);assert.equal(units.allSourceClausesApplied,false);
});
test('Source gates retain line4brother premise, line4/2combination, explicit moving-or-static and line3卯 exception',()=>{
 assert.equal(ops.clauses.length,17);assert.equal(ops.sourceInstructionsAreData,true);assert.equal(ops.allBook4ClausesCompiled,false);
 assert(ops.clauses.every(c=>!c.consumerApplied&&!c.historicalOutcomesValidated));
 assert.equal(clause.fourthLineDoor.boundedReading,'四爻兄弟方言戶');
 assert.equal(clause.fourthLineDoor.kinPrerequisite,'兄弟');assert.equal(clause.fourthLineDoor.motionRequirement,null);
 assert.deepEqual(clause.fourthLineDoor.primaryLinesCompared,[4,2]);
 assert.equal(clause.thirdLineBedException.line,3);assert.equal(clause.thirdLineBedException.branch,'卯');assert.equal(clause.floorPlanAdapter,false);
});
const cat=catalogue(),ctx={};ctx.window=ctx;vm.createContext(ctx);vm.runInContext(await readFile(resolve(root,'engine.js'),'utf8'),ctx);
const context={sourceContext:'B03-volume9-home-divination'},identities=[];let hhcCalls=0;
test('64actual HHC figure-number calls anchor private source charts without a consumer home-fortune adapter',()=>{
 for(const c of cat){const values=c.bits.map(b=>b?7:8),r=homeSymbolCoordinates(values,context);
  assert.equal(ctx.HHC_ENGINE.hexNumber(values),c.number);hhcCalls++;assert.equal(r.chart.primary.number,c.number);
  assert.equal(r.houseAnchor.line,2);assert.equal(r.occupantAnchor.line,5);identities.push([c.number,values]);
 }assert.equal(hhcCalls,64);
});
// Literal independent NaJia rows, element cycle and six combination pairs.
const najia={'111':['子寅辰','午申戌'],'110':['巳卯丑','亥酉未'],'101':['卯丑亥','酉未巳'],
 '100':['子寅辰','午申戌'],'011':['丑亥酉','未巳卯'],'010':['寅辰午','申戌子'],
 '001':['辰午申','戌子寅'],'000':['未巳卯','丑亥酉']};
const elem={子:'水',丑:'土',寅:'木',卯:'木',辰:'土',巳:'火',午:'火',未:'土',申:'金',酉:'金',戌:'土',亥:'水'};
const cycle=['木','火','土','金','水'],kinLabels=['兄弟','子孫','妻財','官鬼','父母'];
const kin=(palace,branch)=>kinLabels[(cycle.indexOf(elem[branch])-cycle.indexOf(palace)+5)%5];
const combined=(a,b)=>['子丑','寅亥','卯戌','辰酉','巳申','午未'].some(p=>p.includes(a)&&p.includes(b)&&a!==b);
const branchList=bits=>[...najia[bits.slice(0,3).join('')][0],...najia[bits.slice(3).join('')][1]];
const controls=[];
test('Synthetic positive and negative controls selected by literal source premises include false generic-door and bed exceptions',()=>{
 const rows=cat.map(c=>{const b=branchList(c.bits);return{c,b,k4:kin(c.palaceElement,b[3]),
  combined:combined(b[3],b[1]),bed:kin(c.palaceElement,b[2])==='兄弟'&&b[2]==='卯'};});
 for(const [name,predicate]of [
  ['principal-door-premises',r=>r.k4==='兄弟'&&r.combined],
  ['fourth-brother-without-combination',r=>r.k4==='兄弟'&&!r.combined],
  ['combination-without-brother',r=>r.k4!=='兄弟'&&r.combined],
  ['third-brother-mao-bed',r=>r.bed],
  ['third-mao-without-brother',r=>r.b[2]==='卯'&&!r.bed]]){
  const row=rows.find(predicate);assert(row,name);
  const values=row.c.bits.map(b=>b?7:8),r=homeSymbolCoordinates(values,context);
  assert.equal(r.fourthLineDoor.principalDoorGate==='source-symbol-prerequisites-present',row.k4==='兄弟'&&row.combined);
  assert.equal(r.thirdLineBedException.gate,row.bed);assert.equal(r.fourthLineDoor.actualDoorExistence,null);
  controls.push({synthetic:true,notAPrintedCoinCast:true,name,number:row.c.number,values,result:r});
 }
});
let contexts=0,doorKinContexts=0,principalDoorContexts=0,bedContexts=0,combinationWithoutKinContexts=0,
 changedBrotherWithoutPrimaryKinContexts=0,movingAnnotations=0;
const digest=createHash('sha256');
test('4096private primary/motion-mask charts match independent kin/branch/combination gates and preserve moving annotations',()=>{
 for(const c of cat){const b=branchList(c.bits),k=b.map(x=>kin(c.palaceElement,x));
  for(let mask=0;mask<64;mask++){
   const v=c.bits.map((bit,i)=>(mask>>i)&1?bit?9:6:bit?7:8),r=homeSymbolCoordinates(v,context),cb=branchList(r.chart.changed.bits);
   const doorKin=k[3]==='兄弟',door=doorKin&&combined(b[3],b[1]),bed=k[2]==='兄弟'&&b[2]==='卯';
   assert.equal(r.houseAnchor.branch,b[1]);assert.equal(r.occupantAnchor.branch,b[4]);
   assert.equal(r.houseAnchor.kin,k[1]);assert.equal(r.occupantAnchor.kin,k[4]);
   assert.equal(r.fourthLineDoor.kinPremisePresent,doorKin);assert.equal(r.fourthLineDoor.principalDoorCombinationToHouse,combined(b[3],b[1]));
   assert.equal(r.fourthLineDoor.principalDoorGate==='source-symbol-prerequisites-present',door);
   assert.equal(r.thirdLineBedException.gate,bed);assert.equal(r.thirdLineBedException.sourceSymbol,bed?'床榻':null);
   assert.deepEqual(r.innerOuter.innerLines,[1,2,3]);assert.deepEqual(r.innerOuter.outerLines,[4,5,6]);
   assert.equal(r.chart.primary.shi,c.shi);assert.equal(r.chart.primary.ying,c.ying);
   for(let i=0;i<6;i++){assert.equal(r.chart.lines[i].branch,b[i]);assert.equal(r.chart.lines[i].kin,k[i]);
    const changed=r.chart.lines[i].changed,moving=Boolean((mask>>i)&1);assert.equal(r.chart.lines[i].moving,moving);
    if(moving){assert.equal(changed.branch,cb[i]);assert.equal(changed.kin,kin(c.palaceElement,cb[i]));movingAnnotations++;}
    else assert.equal(changed,null);
   }
   if(doorKin)doorKinContexts++;if(door)principalDoorContexts++;if(bed)bedContexts++;
   if(!doorKin&&combined(b[3],b[1]))combinationWithoutKinContexts++;
   if(!doorKin&&r.chart.lines[3].changed?.kin==='兄弟')changedBrotherWithoutPrimaryKinContexts++;
   for(const key of ['compassBearings','roomRecommendations','physicalFloorPlan','sourceOutcomeAdjudication','predictedEvent'])assert.equal(r[key],null);
   assert.equal(r.ordinalIsNotBuildingStorey,true);assert.equal(r.consumerApplied,false);
   assert.equal(r.thirdLineBedException.genericThirdLineDoorAssigned,false);
   digest.update(JSON.stringify([c.number,mask,b,k,doorKin,door,bed])+'\n');contexts++;
  }
 }assert.equal(contexts,4096);assert.equal(movingAnnotations,12288);assert(doorKinContexts>principalDoorContexts&&principalDoorContexts>0&&bedContexts>0);
 assert(combinationWithoutKinContexts>0&&changedBrotherWithoutPrimaryKinContexts>0);
});
test('Explicit bounded context required; bearings, room plans, strength extras, sparse and malformed casts reject without input mutation',()=>{
 const v=[7,7,7,7,7,7];
 for(const bad of [undefined,null,[],{},'home',{sourceContext:'home'},
  {...context,bearing:90},{...context,rooms:[]},{...context,strength:'strong'},
  {...context,[Symbol('x')]:1}])assert.throws(()=>homeSymbolCoordinates(v,bad));
 for(const bad of [Array(6),[7,7,7],[7,7,7,7,7,'9'],[7,7,7,7,7,10]])assert.throws(()=>homeSymbolCoordinates(bad,context));
 assert.throws(()=>homeSymbolCoordinates(v,context,null));const copy=v.slice();homeSymbolCoordinates(v,context);assert.deepEqual(v,copy);
});
const old=await read(resolve(archive,'PACKAGE_MANIFEST.json')),html=await readFile(resolve(root,'Huyen_Hoc_Cac.html'));
const earlierReferences=old.files.filter(f=>/research\/liuyao-[^/]+\/.*reference\.mjs$/.test(f.file));
for(const f of old.files.filter(f=>!f.file.includes('/')&&/\.(js|css)$/.test(f.file)||earlierReferences.includes(f)))
 assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
test('Consumer707411bytes and11earlier private references unchanged; research and home symbolic rules absent from site',()=>{
 assert.equal(earlierReferences.length,11);assert.equal(html.length,707411);assert.equal(sha(html),old.product.sha256);
 for(const token of ['home-symbol-reference.mjs','HOME_SYMBOL_CLAUSES.json','BOOK4_CURRENT_UNITS.json'])assert.equal(html.includes(Buffer.from(token)),false);
});
await mkdir(qa,{recursive:true});const summary={actualHHCHexCalls:hhcCalls,privatePrimaryMotionContexts:contexts,movingAnnotations,
 doorKinContexts,principalDoorContexts,bedContexts,combinationWithoutKinContexts,changedBrotherWithoutPrimaryKinContexts,
 graphDigest:digest.digest('hex'),manualRecords:67,contentImagesNewToRelease:65,coverImagesNewToRelease:2,
 inheritedPendingContentImages:17,newContentRendersThisRun:48,newCoverRendersThisRun:2,QAOnlyRenders:2,
 firstPassMainUnits:11,firstPassNestedSubsections:1,newOrCompletedMainSpans:7,boundedOperationalClauses:17};
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify({date:'2026-10-27',syntheticControls:controls,
 actualHHCIdentityCases:identities,historicalOutcomesValidated:false,sourcePrintedCoinCastFixtures:0},null,2)+'\n');
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary,
 htmlSHA256:sha(html),consumerChanged:false,wholeBookApplied:false},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...summary}));
