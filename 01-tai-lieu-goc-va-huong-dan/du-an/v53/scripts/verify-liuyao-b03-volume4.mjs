import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {triadCoordinates} from '../research/liuyao-b03-volume4/triad-reference.mjs';
import {catalogue} from '../research/liuyao-foundations/liuyao-reference.mjs';
const root=resolve(import.meta.dirname,'..'), base=resolve(root,'research/liuyao-b03-volume4'),
  qa=resolve(root,'qa/liuyao-b03-volume4'), archive=resolve(root,'../archives/v53-before-liuyao-b03-volume4');
const read=async p=>JSON.parse(await readFile(p,'utf8')), sha=b=>createHash('sha256').update(b).digest('hex');
const checks=[];
function test(name,fn){fn(); checks.push({name,ok:true}); console.log('PASS',name);}
const manual=await read(resolve(base,'MANUAL_READINGS.json')), tables=await read(resolve(base,'TRIAD_TABLES.json')),
 clauses=await read(resolve(base,'OPERATIONAL_CLAUSES.json')), audit=await read(resolve(base,'SOURCE_AUDIT.json'));
const pdf=await readFile(resolve(base,manual.sourcePDF));
test('Reuse exact acquired 49-page PDF, with no new HTTP or original-PDF counts',()=>{
 assert.equal(pdf.length,41224832); assert.equal(sha(pdf),manual.sourceSHA256);
 assert.equal(manual.sourceSHA256,'c1e1027331d43769733c6011b4fe99e90928e9fde013fce563c8e9bad81c04bf');
 assert.equal(manual.newHTTPBodies,0);assert.equal(manual.newOriginalPDFs,0);assert.equal(audit.newHTTPBodies,0);
});
for(const r of manual.records)assert.equal(sha(await readFile(resolve(base,r.image))),r.sha256);
test('All 19 volume-four content pages plus final cover read; 17 new renders, three expanded readings',()=>{
 assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:20},(_,i)=>30+i));
 assert.equal(manual.counts.newLocalRenders,17);assert.equal(manual.counts.expandedEarlierBoundedPages,3);
 assert.equal(manual.records.filter(r=>r.newLocalRender).length,17);
 assert.equal(manual.opening.literalTitle,'卜筮正宗卷之四');assert.equal(manual.ending.literalReading,'卜筮正宗卷之四終');
 assert.equal(manual.ending.pdfPage,48);assert.equal(manual.records.at(-1).scope,'cover-only');
 assert.deepEqual(manual.physicalBook2PageCoverage.unreadPages,[]);assert.equal(manual.wholePhysicalBookApplied,false);
});
test('Thirty bounded clauses preserve question, strength, timing and spirit qualifications',()=>{
 assert.equal(clauses.clauses.length,30);assert.equal(clauses.allVolume4ClausesCompiled,false);
 for(const id of ['self-void','functional-void','day-parity','moving-bound','spirits-not-verdict','ritual-not-instruction'])
  assert(clauses.clauses.some(c=>c.id===id&&!c.consumerApplied&&!c.historicalOutcomesValidated));
 assert.equal(clauses.sourceInstructionsAreData,true);
});
const expected=[['water-trine','三合','申子辰'],['fire-trine','三合','寅午戌'],['metal-trine','三合','巳酉丑'],
 ['wood-trine','三合','亥卯未'],['tiger-snake-monkey','三刑','寅巳申'],['ox-dog-goat','三刑','丑戌未']];
test('Source-specific complete-member gate has four trines and two three-member punishments',()=>{
 assert.deepEqual(tables.groups.map(g=>[g.id,g.kind,g.members.join('')]),expected);
 assert.equal(tables.pdfPage,39);assert.equal(tables.effectiveFormationEstablished,false);
 assert.equal(tables.normalization.atLeastTwoIsOperationalInterpretationNotAnAdditionalLiteralQuote,true);
 assert.deepEqual(tables.otherSourceExamplesNotCompiledHere,['子卯相刑','辰午酉亥自刑']);
});
const controls=[];
test('Complete branches alone do not satisfy motion; one moving member differs from two',()=>{
 for(const [values,gate] of [ [[7,7,7,7,7,7],'moving-premise-not-present'],
  [[9,7,7,7,7,7],'moving-premise-not-present'], [[9,7,9,7,7,7],'structural-prerequisites-present'] ]){
  const r=triadCoordinates(values), water=r.groups.find(g=>g.id==='water-trine');
  assert.equal(water.completePrimaryMembership,true);assert.equal(water.preliminaryGate,gate);
  assert.equal(water.effectiveFormation,null);assert.equal(water.auspicious,null);
  assert.equal(r.groups.find(g=>g.id==='tiger-snake-monkey').preliminaryGate,'incomplete-members');
  controls.push({syntheticNotPrintedCast:true,values,water});
 }
 const q=triadCoordinates([9,9,9,9,9,9]);
 assert.equal(q.groups.filter(g=>g.preliminaryGate==='structural-prerequisites-present').length,2);
 assert.equal(q.groups.find(g=>g.id==='water-trine').witnesses[0].movingCount,3);
});
const ctx={};ctx.window=ctx;vm.createContext(ctx);vm.runInContext(await readFile(resolve(root,'engine.js'),'utf8'),ctx);
const cat=catalogue();let actualHHC=0;
// Separate literal Na-Jia coordinate oracle, not the new gate implementation.
const oracleNaJia={'111':['子寅辰','午申戌'],'110':['巳卯丑','亥酉未'],'101':['卯丑亥','酉未巳'],
 '100':['子寅辰','午申戌'],'011':['丑亥酉','未巳卯'],'010':['寅辰午','申戌子'],
 '001':['辰午申','戌子寅'],'000':['未巳卯','丑亥酉']};
test('Execute 64 actual HHC figure identities; compare primary branch coordinates with independent literal arrays',()=>{
 for(const c of cat){const values=c.bits.map(b=>b?7:8), r=triadCoordinates(values);
  assert.equal(ctx.HHC_ENGINE.hexNumber(values),c.number);actualHHC++;
  assert.equal(r.chart.primary.number,c.number);
  const branches=[...oracleNaJia[c.bits.slice(0,3).join('')][0],...oracleNaJia[c.bits.slice(3).join('')][1]];
  assert.deepEqual(r.chart.lines.map(l=>l.branch),branches);
 }
 assert.equal(actualHHC,64);
});
// Independent combination-of-positions oracle: choose triples out of six, instead of member Cartesian products.
const triples=[];for(let a=0;a<4;a++)for(let b=a+1;b<5;b++)for(let c=b+1;c<6;c++)triples.push([a,b,c]);
const digest=createHash('sha256');let pairs=0, completeGroups=0, qualifyingGroups=0, witnesses=0,
 duplicateMemberCharts=0, discardedRepeatedBranchTriples=0;
const perGroup=Object.fromEntries(expected.map(([id])=>[id,{complete:0,qualifying:0,witnesses:0}]));
test('All 4096 figure/motion contexts match an independent 20-position-triple oracle; changed branches cannot fill gaps',()=>{
 for(const c of cat){
  const branches=[...oracleNaJia[c.bits.slice(0,3).join('')][0],...oracleNaJia[c.bits.slice(3).join('')][1]];
  if(new Set(branches).size<6)duplicateMemberCharts++;
  for(let mask=0;mask<64;mask++){
   const values=c.bits.map((b,i)=>mask>>i&1?b?9:6:b?7:8),r=triadCoordinates(values), compact=[];
   for(let gi=0;gi<expected.length;gi++){
    const [id,,members]=expected[gi],target=[...members].sort().join('');
    const matches=triples.filter(t=>t.map(i=>branches[i]).sort().join('')===target);
    const qualifying=matches.filter(t=>t.filter(i=>mask>>i&1).length>=2);
    const g=r.groups[gi], want=matches.length?qualifying.length?'structural-prerequisites-present':'moving-premise-not-present':'incomplete-members';
    assert.equal(g.id,id);assert.equal(g.witnesses.length,matches.length);assert.equal(g.qualifyingWitnesses,qualifying.length);
    assert.equal(g.preliminaryGate,want);assert.equal(g.completePrimaryMembership,matches.length>0);
    assert.deepEqual(g.witnesses.map(w=>w.lines.slice().sort((a,b)=>a-b).join(',')).sort(),
     matches.map(t=>t.map(i=>i+1).join(',')).sort());
    assert.equal(g.effectiveFormation,null);assert.equal(g.transformedElement,null);
    if(matches.length){completeGroups++;perGroup[id].complete++;}
    if(qualifying.length){qualifyingGroups++;perGroup[id].qualifying++;}
    witnesses+=matches.length;perGroup[id].witnesses+=matches.length;
    compact.push([id,want,matches.length,qualifying.length]);
   }
   for(const t of triples)if(new Set(t.map(i=>branches[i])).size<3)discardedRepeatedBranchTriples++;
   for(const l of r.chart.lines)if(!l.moving)assert.equal(l.changed,null);
   assert.equal(r.changedOrCalendarBranchesUsedToCompleteGroups,false);assert.equal(r.predictedEvent,null);
   assert.equal(r.fullStrengthModel,null);assert.equal(r.sourceQualifiedFormation,null);
   digest.update(JSON.stringify([c.number,mask,compact])+'\n');pairs++;
  }
 }
 assert.equal(pairs,4096);assert(duplicateMemberCharts>0);assert(discardedRepeatedBranchTriples>0);
 // The primary six Na-Jia branches cannot contain either full three-member punishment.
 // This is a finite catalogue derivation, not a claim that the source has no such formations.
 assert.equal(perGroup['tiger-snake-monkey'].complete,0);
 assert.equal(perGroup['ox-dog-goat'].complete,0);
 assert.equal(completeGroups,2048);assert.equal(qualifyingGroups,1120);assert.equal(witnesses,2816);
});
test('Strict input boundary rejects unsupported calendars/strengths, sparse arrays, text values and incomplete casts',()=>{
 for(const values of [[7,7,7,7,7],[7,7,7,7,7,'9'],Array(6)])assert.throws(()=>triadCoordinates(values));
 assert.throws(()=>triadCoordinates([7,7,7,7,7,7],{dayBranch:'子'}));
 assert.throws(()=>triadCoordinates([7,7,7,7,7,7],null));
 const values=[9,7,9,7,7,7],before=values.slice(),r=triadCoordinates(values);
 r.groups[0].members[0]='x';assert.deepEqual(values,before);
 assert.equal(triadCoordinates(values).groups[0].members[0],'申');
});
const old=await read(resolve(archive,'PACKAGE_MANIFEST.json')),html=await readFile(resolve(root,'Huyen_Hoc_Cac.html'));
for(const f of old.files.filter(f=>!f.file.includes('/')&&/\.(js|css)$/.test(f.file)||/research\/liuyao-[^/]+\/.*reference\.mjs$/.test(f.file)))
 assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
test('Consumer and eight earlier private references preserved, with no source ledger in product',()=>{
 assert.equal(html.length,707411);assert.equal(sha(html),old.product.sha256);
 for(const s of ['triad-reference.mjs','TRIAD_TABLES.json','OPERATIONAL_CLAUSES.json'])assert.equal(html.includes(Buffer.from(s)),false);
});
await mkdir(qa,{recursive:true});
const summary={actualHHCHexCalls:actualHHC,privateFigureMotionContexts:pairs,groupsPerContext:6,
 completeGroups,qualifyingGroups,witnesses,duplicateMemberCharts,discardedRepeatedBranchTriples,
 perGroup,graphDigest:digest.digest('hex'),operationalClauses:clauses.clauses.length};
await writeFile(resolve(qa,'SOURCE_CASE_RESULTS.json'),JSON.stringify({date:'2026-10-27',controls,
 sourceExamplesAreBranchGroupsNotPrintedCoinCasts:true,historicalOutcomesValidated:false},null,2)+'\n');
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({date:'2026-10-27',checks,summary,
 htmlSHA256:sha(html),consumerChanged:false,wholeBookApplied:false},null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...summary}));
