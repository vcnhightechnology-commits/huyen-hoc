import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';import assert from 'node:assert/strict';import vm from 'node:vm';
import {xunExitCoordinates} from '../research/liuyao-b03-book3/xun-exit-reference.mjs';
import {catalogue} from '../research/liuyao-foundations/liuyao-reference.mjs';
const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/liuyao-b03-book3'),
 qa=resolve(root,'qa/liuyao-b03-book3'),archive=resolve(root,'../archives/v53-before-liuyao-b03-book3');
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=b=>createHash('sha256').update(b).digest('hex');
const checks=[];function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const manual=await read(resolve(base,'MANUAL_READINGS.json')),units=await read(resolve(base,'BOOK3_CURRENT_UNITS.json')),
 ops=await read(resolve(base,'OPERATIONAL_CLAUSES.json')),clause=await read(resolve(base,'XUN_EXIT_CLAUSE.json'));
const pdf=await readFile(resolve(base,manual.sourcePDF));
test('Already acquired raw67-page PDF reused without HTTP or duplicated original PDF',()=>{
 assert.equal(pdf.length,56939817);assert.equal(sha(pdf),manual.sourceSHA256);
 assert.equal(sha(pdf),'01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61');
 assert.equal(manual.newHTTPBodies,0);assert.equal(manual.newOriginalPDFs,0);
});
for(const r of [...manual.records,...manual.qaImages])assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
test('43new source renders/8expanded records/two QA crops, all67source pages now viewed by recorded scopes',()=>{
 assert.equal(manual.records.length,51);assert.equal(manual.records.filter(r=>r.newLocalRender).length,43);
 assert.equal(manual.records.filter(r=>r.expandedEarlierReading).length,8);assert.equal(manual.qaImages.length,2);
 assert.equal(manual.counts.newContentPages,41);assert.equal(manual.counts.coverPages,2);
 const union=new Set([...manual.inheritedFirstPassPages,...manual.records.map(r=>r.pdfPage)]);
 assert.equal(union.size,67);assert.deepEqual([...union].sort((a,b)=>a-b),Array.from({length:67},(_,i)=>i+1));
 assert.deepEqual(manual.directBoundaries.map(x=>x.pdfPage),[30,31,48,49,66]);
 assert.deepEqual(manual.unviewedPhysicalBookPages,[]);assert.equal(manual.entireBookApplied,false);
});
test('12first-pass relevant section spans across volumes5/6/7; page30completes body, never entire source application',()=>{
 assert.equal(units.units.length,12);assert(units.units.every(u=>u.relevantSpanFirstPassRead&&!u.entireUnitApplied));
 assert.equal(units.counts.newOrCompletedSpanUnits,8);assert.equal(units.counts.previouslyCompleteSpanUnits,4);
 assert.deepEqual(units.units.find(u=>u.heading==='身命').pdfPages,Array.from({length:12},(_,i)=>i+19));
 assert.deepEqual(units.units.filter(u=>u.textualVolume===6).map(u=>u.heading),['婚姻','產育','進人口']);
 assert.deepEqual(units.units.filter(u=>u.textualVolume===7).map(u=>u.heading),['病症','病體','醫藥','鬼神']);
 assert.equal(units.allClausesApplied,false);assert.equal(units.all14TextualVolumesApplied,false);
});
test('20bounded clauses keep medical/ritual assertions historical and distinguish marriage/birth/household/relative domains',()=>{
 assert.equal(ops.clauses.length,20);assert.equal(ops.sourceInstructionsAreData,true);assert.equal(ops.historicalMedicalClaimsNotClinicalAdvice,true);
 for(const id of ['marriage-domain','marriage-subject','birth-subject','household-new-person','health-relative','medical-claims','ritual-taxonomy'])
  assert(ops.clauses.some(c=>c.id===id&&!c.consumerApplied&&!c.historicalOutcomesValidated));
 assert.equal(ops.allBook3ClausesCompiled,false);
 assert(ops.clauses.find(c=>c.id==='marriage-domain').boundedParaphrase.includes('cả nam hỏi nữ và nữ hỏi nam'));
 assert(manual.qaImages.some(r=>r.pdfPage===38));
 assert.equal(clause.boundedReading,'如旬空候出旬之日應事');assert.equal(clause.motionQualifierInThisBoundedSentence,null);
});
const cat=catalogue(),ctx={};ctx.window=ctx;vm.createContext(ctx);vm.runInContext(await readFile(resolve(root,'engine.js'),'utf8'),ctx);
let hhcCalls=0;const identity=[];
test('64actual HHC figure-number calls anchor all catalogue identities; calendar horizons are not product forecasts',()=>{
 for(const c of cat){const values=c.bits.map(b=>b?7:8),r=xunExitCoordinates(values,{sourceContext:'weather-timing-paragraph',useLine:1});
  assert.equal(ctx.HHC_ENGINE.hexNumber(values),c.number);hhcCalls++;assert.equal(r.chart.primary.number,c.number);
  assert.equal(r.rawVoid,null);assert.equal(r.premiseStatus,'unknown-day-coordinate');
  assert.equal(r.firstOutsideCurrentXun,null);assert.equal(r.predictedEvent,null);identity.push([c.number,values]);
 }
 assert.equal(hhcCalls,64);
});
const runtime=await read(resolve(root,'research/bazi-late-zi/VERIFICATION.json'));
for(const r of runtime.runtime)assert.equal(sha(await readFile(resolve(root,'..',r.file))),r.sha256);
const req=createRequire(import.meta.url),L=req(resolve(root,'../v46/node_modules/lunar-typescript'));
assert.equal(req(resolve(root,'../v46/node_modules/lunar-typescript/package.json')).version,'1.8.6');
const oracle=new Map(),referenceRows=[],uniqueDates=new Set();let lunarCalls=0;
function actualNoon(offset){const date=L.Solar.fromYmdHms(2026,1,1,12,0,0).next(offset),ec=date.getLunar().getEightChar();
 ec.setSect(2);lunarCalls++;uniqueDates.add(date.toYmdHms());return{date:date.toYmdHms(),day:ec.getDay(),xun:ec.getDayXun(),voids:ec.getDayXunKong()};}
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const literalNaJia={'111':['子寅辰','午申戌'],'110':['巳卯丑','亥酉未'],'101':['卯丑亥','酉未巳'],
 '100':['子寅辰','午申戌'],'011':['丑亥酉','未巳卯'],'010':['寅辰午','申戌子'],
 '001':['辰午申','戌子寅'],'000':['未巳卯','丑亥酉']};
function representative(branch){for(const c of cat){const bb=[...literalNaJia[c.bits.slice(0,3).join('')][0],...literalNaJia[c.bits.slice(3).join('')][1]],i=bb.indexOf(branch);
 if(i>=0)return{values:c.bits.map(b=>b?7:8),useLine:i+1};}throw Error('Missing branch');}
test('Pinned actual lunar runtime executes60anchors and120boundary endpoints, current/next xun tested with last-inside controls',()=>{
 for(let i=0;i<60;i++){
  const anchor=actualNoon(i),rep=representative([...anchor.voids][0]);
  const r=xunExitCoordinates(rep.values,{sourceContext:'weather-timing-paragraph',useLine:rep.useLine,dayGanZhi:anchor.day});
  const offset=r.firstOutsideCurrentXun.offsetDays,last=actualNoon(i+offset-1),after=actualNoon(i+offset);
  assert.equal(r.day.xunHead,anchor.xun);assert.equal(r.day.voidBranches.join(''),anchor.voids);
  assert.equal(last.xun,anchor.xun);assert.notEqual(after.xun,anchor.xun);
  assert.equal(r.firstOutsideCurrentXun.dayGanZhi,after.day);assert.equal(r.firstOutsideCurrentXun.xunHead,after.xun);
  assert.equal(r.firstOutsideCurrentXun.voidBranches.join(''),after.voids);assert.equal(r.firstOutsideCurrentXun.subjectStillRawVoid,false);
  assert(after.day.startsWith('甲'));oracle.set(anchor.day,{...anchor,offset,last,after});referenceRows.push({anchor,offset,last,after});
 }
 assert.equal(oracle.size,60);assert.equal(lunarCalls,180);assert.equal(new Set(referenceRows.map(r=>r.anchor.xun)).size,6);
});
const controls=[];
test('Raw branch 寅 on 甲辰 gives10days and on 癸丑 gives1day; actual movement/changed丑 do not replace primary branch',()=>{
 const common={sourceContext:'weather-timing-paragraph',useLine:2};
 const a=xunExitCoordinates([7,7,7,7,7,7],{...common,dayGanZhi:'甲辰'});
 const b=xunExitCoordinates([7,9,7,7,7,7],{...common,dayGanZhi:'甲辰'});
 const c=xunExitCoordinates([7,9,7,7,7,7],{...common,dayGanZhi:'癸丑'});
 assert.equal(a.subjectBranch,'寅');assert.equal(b.chart.lines[1].changed.branch,'丑');
 assert.equal(a.rawVoid,true);assert.equal(b.rawVoid,true);assert.equal(a.firstOutsideCurrentXun.offsetDays,10);
 assert.deepEqual(a.firstOutsideCurrentXun,b.firstOutsideCurrentXun);
 assert.equal(c.firstOutsideCurrentXun.offsetDays,1);assert.equal(c.firstOutsideCurrentXun.dayGanZhi,'甲寅');
 for(const r of [a,b,c]){assert.equal(r.functionalVoid,null);assert.equal(r.gregorianDate,null);assert.equal(r.allSourceExceptionsChecked,false);controls.push(r);}
});
let contexts=0,voidContexts=0;const exitHistogram={},digest=createHash('sha256');
test('46080selected primary-line/motion/day contexts match independent literal NaJia and actual lunar xun oracles',()=>{
 for(const [day,data]of oracle){for(const c of cat){
  const bb=[...literalNaJia[c.bits.slice(0,3).join('')][0],...literalNaJia[c.bits.slice(3).join('')][1]];
  for(let line=0;line<6;line++)for(const moving of [false,true]){
   const values=c.bits.map((b,i)=>moving&&i===line?b?9:6:b?7:8);
   const r=xunExitCoordinates(values,{sourceContext:'weather-timing-paragraph',useLine:line+1,dayGanZhi:day}),isVoid=data.voids.includes(bb[line]);
   assert.equal(r.subjectBranch,bb[line]);assert.equal(r.rawVoid,isVoid);assert.equal(r.subjectMotion,moving?'moving':'static');
   if(isVoid){assert.equal(r.firstOutsideCurrentXun.offsetDays,data.offset);assert.equal(r.firstOutsideCurrentXun.dayGanZhi,data.after.day);
    assert.equal(r.currentXunWindow.endOffset0,data.offset-1);voidContexts++;exitHistogram[data.offset]=(exitHistogram[data.offset]??0)+1;
   }else{assert.equal(r.firstOutsideCurrentXun,null);assert.equal(r.currentXunWindow,null);assert.equal(r.premiseStatus,'not-in-raw-void');}
   if(!moving)assert(r.chart.lines.every(l=>l.changed===null));
   assert.equal(r.subjectLayer,'primary-selected-line');assert.equal(r.changedBranchSubstituted,false);
   assert.equal(r.functionalVoid,null);assert.equal(r.predictedEvent,null);assert.equal(r.meteorologicalForecast,null);
   digest.update(JSON.stringify([day,c.number,line+1,moving,bb[line],isVoid,r.firstOutsideCurrentXun?.offsetDays??null])+'\n');contexts++;
  }
 }}assert.equal(contexts,46080);assert.equal(voidContexts,7680);assert.deepEqual(Object.values(exitHistogram),Array(10).fill(768));
});
test('Missing day stays unknown; unsupported domain, invalid day, extra strength/month context or malformed cast rejects',()=>{
 const v=[7,7,7,7,7,7],common={sourceContext:'weather-timing-paragraph',useLine:2};
 for(const bad of [{...common,dayGanZhi:'甲丑'},{...common,sourceContext:'marriage'},
  {...common,useLine:'2'},{...common,useLine:7},{...common,dayGanZhi:'甲辰日'},
  {...common,strength:'strong'},{...common,monthBranch:'寅'}])assert.throws(()=>xunExitCoordinates(v,bad));
 for(const bad of [[7,7,7,7,7],Array(6),[7,7,7,7,7,'9']])assert.throws(()=>xunExitCoordinates(bad,common));
 assert.throws(()=>xunExitCoordinates(v,common,null));assert.throws(()=>xunExitCoordinates(v,{...common,[Symbol('x')]:1}));
 const copy=v.slice(),r=xunExitCoordinates(v,{...common,dayGanZhi:null});assert.deepEqual(v,copy);
 assert.equal(r.rawVoid,null);assert.equal(r.day,null);assert.equal(r.firstOutsideCurrentXun,null);
 const no=xunExitCoordinates(v,{...common,useLine:1,dayGanZhi:'甲子'});assert.equal(no.rawVoid,false);assert.equal(no.firstOutsideCurrentXun,null);
});
const old=await read(resolve(archive,'PACKAGE_MANIFEST.json')),html=await readFile(resolve(root,'Huyen_Hoc_Cac.html'));
for(const f of old.files.filter(f=>!f.file.includes('/')&&/\.(js|css)$/.test(f.file)||/research\/liuyao-[^/]+\/.*reference\.mjs$/.test(f.file)))
 assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
test('Consumer707411bytes and10earlier private references unchanged; prior timing module preserved',()=>{
 assert.equal(html.length,707411);assert.equal(sha(html),old.product.sha256);
 for(const x of ['xun-exit-reference.mjs','BOOK3_CURRENT_UNITS.json','XUN_EXIT_CLAUSE.json'])assert.equal(html.includes(Buffer.from(x)),false);
});
await mkdir(qa,{recursive:true});const summary={actualHHCHexCalls:hhcCalls,actualLunarCalls:lunarCalls,
 distinctLunarNoonDates:uniqueDates.size,referenceAnchorDays:oracle.size,privateSelectedLineContexts:contexts,
 rawVoidContexts:voidContexts,exitHistogram,graphDigest:digest.digest('hex'),newSourceRenders:43,
 expandedEarlierPages:8,QAOnlyRenders:2,firstPassSectionSpans:12,newOrCompletedSectionSpans:8,boundedOperationalClauses:20};
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify({date:'2026-10-27',syntheticControls:controls,
 referenceRows,actualHHCIdentityCases:identity,referenceTimeConvention:'Explicit noon input to lunar-typescript, not an ancient source timezone assertion.',
 historicalOutcomesValidated:false},null,2)+'\n');
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary,
 htmlSHA256:sha(html),consumerChanged:false,wholeBookApplied:false},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...summary}));
