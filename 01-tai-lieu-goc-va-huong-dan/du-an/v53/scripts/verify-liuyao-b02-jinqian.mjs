import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import assert from'node:assert/strict';import vm from'node:vm';
import{interposedContext}from'../research/liuyao-b02-jinqian/interposed-reference.mjs';
import{catalogue}from'../research/liuyao-foundations/liuyao-reference.mjs';
const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/liuyao-b02-jinqian'),qa=resolve(root,'qa/liuyao-b02-jinqian');
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=b=>createHash('sha256').update(b).digest('hex'),checks=[];
function test(name,fn){fn();checks.push({name,ok:true});console.log('PASS',name);}
const manual=await read(resolve(base,'MANUAL_READINGS.json')),units=await read(resolve(base,'B02_CURRENT_UNITS.json')),
 spans=await read(resolve(base,'CHAPTER_SPANS.json')),fixtures=await read(resolve(base,'PRINTED_FIXTURES.json')),
 req=await read(resolve(base,'witness/REQUESTS.json')),wr=await read(resolve(base,'witness/MANUAL_READINGS.json'));
for(const r of manual.records)assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
assert.equal(sha(await readFile(resolve(base,manual.sourcePDF))),manual.sourceSHA256);
test('50 viewed records;46-page chapter34 firstpass;chapter35partial keeps TOC/body-volume variant',()=>{
 assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:50},(_,i)=>141+i));
 assert.equal(manual.records.filter(r=>r.actuallyViewed).length,50);assert.equal(spans.chapter34.pdfPages.length,46);
 assert.equal(spans.chapter35.fullFirstPass,false);assert.equal(spans.chapter35.tocVolume,4);assert.equal(spans.chapter35.runningTitleVolume,3);
 assert.deepEqual(units.currentCounts,{registeredUnits:136,regularNumberedUnits:130,supplements:6,headingOnlyBodyUnits:96,partialFoundationUnits:7,otherPartialUnits:1,firstPassCompleteSpanUnits:32,wholeUnitsApplied:0});
 assert.equal(units.units.find(u=>u.id==='B02-ch034').tocVolume,3);
 assert.equal(units.units.filter(u=>u.disposition==='heading-only-body-extraction-open').length,96);
});
for(const r of req.records){const b=await readFile(resolve(base,'witness',r.file));assert.equal(b.length,r.bytes);assert.equal(sha(b),r.sha256);}
for(const r of [...wr.records,...wr.qaImages])assert.equal(sha(await readFile(resolve(base,'witness',r.file))),r.sha256);
test('Seven retained HTTP bodies incl403;uncaptured TLS staysnull;four bounded images not53canvases',()=>{
 assert.equal(req.records.length,7);assert.equal(req.records.filter(x=>x.status===200).length,6);assert.equal(req.records.filter(x=>x.status===403).length,1);
 assert.equal(req.records.filter(x=>x.tls.authorized===true).length,5);assert.equal(req.records.filter(x=>x.tls.authorized===null).length,2);
 assert.deepEqual(wr.records.map(r=>r.canvasOrdinal1),[48,50,51,52]);assert.equal(wr.all53CanvasesViewed,false);
 for(const r of wr.records){assert.deepEqual(r.servedImagePixels,[3000,2073]);assert.equal(r.masterResolutionProved,false);}
});
const wc=await read(resolve(base,'witness/WITNESS_COMPARISON.json'));
test('Additionalwitness preserves庚ambiguity andsixLuroots;13.6→49 isnot a new logicalcast',()=>{
 assert.equal(wc.independentTextualGenealogyEstablished,false);
 assert.equal(wc.findings.find(f=>f.id==='salary-still-six').notExplicitInRetainedParagraph.length,4);
 assert(wc.findings.find(f=>f.id==='geng-not-resolved').conclusion.includes('doesnotchoose'));
 assert(wc.findings.find(f=>f.id==='single-motion-case-name').comparison.includes('third distinct'));
});
const ctx={};ctx.window=ctx;vm.createContext(ctx);const engine=await readFile(resolve(root,'engine.js'));vm.runInContext(engine.toString(),ctx);
let hhcCalls=0;const results=[];
test('Two newly transcribed source cases execute four real HHC calls and inspect間爻',()=>{
 for(const f of fixtures.fixtures){const p=ctx.HHC_ENGINE.hexNumber(f.values),c=ctx.HHC_ENGINE.hexNumber(f.values.map(v=>v===6?7:v===9?8:v));hhcCalls+=2;
  assert.equal(p,f.primary);assert.equal(c,f.changed);const r=interposedContext(f.values,{sourceContext:'B02-ch034',question:f.question,bilateralContext:f.roleApplicable});
  assert.equal(r.shi,f.shi);assert.equal(r.ying,f.ying);assert.deepEqual(r.interposedLines.map(l=>l.line),f.interposed);assert.equal(r.roleApplicable,f.roleApplicable);
  if(f.sourceMovingInterposed){const l=r.interposedLines.find(l=>l.line===f.sourceMovingInterposed.line);assert.equal(l.branch,'酉');assert.equal(l.kin,'兄弟');assert.equal(l.moving,true);}
  results.push({id:f.id,primary:p,changed:c,...r});
 }assert.equal(hhcCalls,4);
});
let cases=0;const context={sourceContext:'B02-ch034',question:'trade'};
test('All64palacepositions ×64visible-motionmasks keep exactlytwo between-lines;no wraparound or endpoint',()=>{
 for(const h of catalogue())for(let mask=0;mask<64;mask++){
  const v=h.bits.map((bit,i)=>(mask>>i)&1?(bit?9:6):(bit?7:8)),r=interposedContext(v,context),expected=[];
  for(let n=Math.min(h.shi,h.ying)+1;n<Math.max(h.shi,h.ying);n++)expected.push(n);
  assert.equal(expected.length,2);assert.deepEqual(r.interposedLines.map(x=>x.line),expected);
  assert.deepEqual(r.visibleMovingInterposedLines,expected.filter(n=>(mask>>(n-1))&1));assert.equal(r.obstructionEstablished,null);cases++;
 }assert.equal(cases,4096);
});
test('Seven explicit rolecontexts andthree non-rolecontexts cannot infer real persons ormedicalresults',()=>{
 const v=fixtures.fixtures[1].values;
 const rs={marriage:'媒妁',litigation:'中證',trade:'牙行',loan:'中保',boat_travel:'附載',childbirth:'收生保母',social_exchange:'幫間'};
 for(const[q,label]of Object.entries(rs)){const x=interposedContext(v,{...context,question:q,bilateralContext:true});assert.equal(x.symbolicRole,label);assert.equal(x.predictedOutcome,null);assert.equal(x.consumerApplied,false);
  const no=interposedContext(v,{...context,question:q,bilateralContext:false}),unknown=interposedContext(v,{...context,question:q});
  assert.equal(no.roleApplicable,false);assert.equal(no.symbolicRole,null);assert.equal(unknown.roleApplicable,null);assert.equal(unknown.symbolicRole,null);
 }
 for(const q of ['weather','self','other']){const x=interposedContext(v,{...context,question:q});assert.equal(x.symbolicRole,null);assert.equal(x.roleApplicable,false);assert.equal(x.interposedLines.length,2);}
});
test('Strict context andno silent defaults;input/result mutations donot corrupt future calculations',()=>{
 const v=fixtures.fixtures[1].values.slice(),before=v.slice();
 for(const bad of[undefined,null,{},[],{...context,question:'unknown'},{...context,date:'today'},{...context,bilateralContext:1},{...context,[Symbol('x')]:true}])assert.throws(()=>interposedContext(v,bad));
 for(const bad of[[],Array(6),[7,7,7,7,7,'9']])assert.throws(()=>interposedContext(bad,context));
 assert.throws(()=>interposedContext(v,context,null));const x=interposedContext(v,context);x.interposedLines[0].line=99;
 assert.deepEqual(v,before);assert.deepEqual(interposedContext(v,context).interposedLines.map(l=>l.line),[4,5]);
});
const html=await readFile(resolve(root,'Huyen_Hoc_Cac.html'));
test('Consumerbytes unchanged andprivate references absent',()=>{
 assert.equal(html.length,707411);assert.equal(sha(html),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');
 for(const t of ['liuyao-b02-jinqian','interposed-reference.mjs'])assert(!html.includes(Buffer.from(t)));
});
await mkdir(qa,{recursive:true});
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary:{actualHHCHexCalls:hhcCalls,newPrintedCastFixtures:2,privateMotionContexts:cases,manualRecords:50,chapter34Pages:46,witnessHTTPBodies:7},engineSHA256:sha(engine),htmlSHA256:sha(html),caseDigest:sha(JSON.stringify(results)),wholeCatalogueCompleted:false},null,2)+'\n');
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify(results,null,2)+'\n');
