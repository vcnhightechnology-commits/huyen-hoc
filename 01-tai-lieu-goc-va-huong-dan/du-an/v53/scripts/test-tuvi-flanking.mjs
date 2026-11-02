import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import{createRequire}from'node:module';import vm from'node:vm';import assert from'node:assert/strict';
import{inspectSourceFlanking}from'../research/tuvi-flanking/source-flanking.mjs';
const b=resolve(import.meta.dirname,'../research/tuvi-flanking'),w=resolve(b,'../../..'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
const table=await read(resolve(b,'SOURCE_GEOMETRY.json')),system=table.system,branches=table.branchOrder;
async function check(name,fn){await fn();checks.push({name,ok:true});}
const query=(kind,a,x,y)=>{const pair=table.pairs.find(p=>p.kind===kind);return inspectSourceFlanking({system,kind,anchorRole:'命宮',anchorBranch:a,placements:{[pair.stars[0]]:x,[pair.stars[1]]:y}});};
await check('Eighteen newly read institution JPEGs preserve200/TLS/header/SHA; juan2 first-pass boundary is39',async()=>{
 const s=await read(resolve(b,'WINDOWS_TRUST_REQUESTS.json')),m=await read(resolve(b,'FIRST_PASS_READINGS.json'));assert.equal(s.records.length,18);assert.equal(m.juan1EndCanvas,38);assert.equal(m.juan2StartsCanvas,39);
 for(const x of s.records){const d=await readFile(resolve(b,x.file));assert.equal(d.length,x.bytes);assert.equal(sha(d),x.sha256);assert.equal(x.status,200);assert(x.TLSCertificateValidationEnabled&&x.responseHeadersRetained&&x.actuallyViewed);assert(m.records.find(z=>z.canvas===x.canvas&&z.sha256===x.sha256&&z.actuallyViewed));}
});
await check('Selected source clauses keep geometry, exclusions and historical outcome as separate evidence layers',async()=>{
 const m=await read(resolve(b,'MANUAL_READINGS.json'));assert.equal(m.records.length,4);assert(m.records.find(x=>x.id==='solar-lunar-flank').literal.includes('前後二宮夾命不逢空劫羊殺'));assert(m.records.find(x=>x.id==='chang-qu-flank').literal.includes('亦如之'));assert.equal(m.sourceExclusionScopeResolved,false);assert.equal(m.sourceOutcomeValidated,false);assert.equal(table.pairs.length,2);
});
let exhaustiveKnown=0,exhaustiveTrue=0;
await check('All3456 declared known geometries preserve two distinct neighbours, unordered pairing, wraparound and reject same/opposite/non-neighbour substitutions',()=>{
 for(const pair of table.pairs)for(let a=0;a<12;a++){let trueForAnchor=0;
  for(let x=0;x<12;x++)for(let y=0;y<12;y++){const q=query(pair.kind,branches[a],branches[x],branches[y]);exhaustiveKnown++;assert.equal(q.geometryMatched,query(pair.kind,branches[a],branches[y],branches[x]).geometryMatched);assert.equal(q.fullSourceConditionsMatched,null);if(q.geometryMatched){trueForAnchor++;exhaustiveTrue++;assert.deepEqual(q.placements.map(z=>z.offsetFromMing).sort((a,b)=>a-b),[1,11]);}}
  assert.equal(trueForAnchor,2);
 }
 assert.equal(exhaustiveKnown,3456);assert.equal(exhaustiveTrue,48);assert.equal(query('sun-moon','子','亥','丑').geometryMatched,true);assert.equal(query('sun-moon','子','丑','丑').geometryMatched,false);assert.equal(query('sun-moon','子','辰','申').geometryMatched,false);assert.equal(query('sun-moon','子','子','午').geometryMatched,false);
});
await check('Null input stays indeterminate unless a known non-neighbour disproves geometry; unsupported source/anchor/name/branch are rejected',()=>{
 for(const pair of table.pairs){assert.equal(query(pair.kind,null,'亥','丑').geometryMatched,null);assert.equal(query(pair.kind,'子',null,'丑').geometryMatched,null);assert.equal(query(pair.kind,'子',null,'辰').geometryMatched,false);assert.equal(query(pair.kind,'子',null,null).geometryMatched,null);}
 const base={system,kind:'sun-moon',anchorRole:'命宮',anchorBranch:'子',placements:{'Thái Dương':'亥','Thái Âm':'丑'}};
 for(const x of[{system:undefined},{kind:'arbitrary-pair'},{anchorRole:'身宮'},{anchorBranch:undefined},{anchorBranch:'Tý'},{placements:{'Thái Dương':'亥'}},{placements:{'太阳':'亥','太阴':'丑'}}])assert.throws(()=>inspectSourceFlanking({...base,...x}),TypeError);
});
const req=createRequire(import.meta.url),iztro=req(resolve(w,'v46/node_modules/iztro')),ctx={};ctx.window=ctx;vm.createContext(ctx);const engine=await readFile(resolve(w,'v53/engine.js'));vm.runInContext(engine.toString(),ctx);const E=ctx.HHC_ENGINE;
let actualHHCTuviCalls=0,actualIztroNatalCalls=0,matchedStarBranchCoordinates=0;const runtime=[];
await check('144 real HHC and144 real iztro charts produce576 matching star branch coordinates and288 matching flanking contexts',()=>{
 assert.equal(req(resolve(w,'v46/node_modules/iztro/package.json')).version,'2.6.2');
 try{for(let month=1;month<=12;month++)for(let hr=0;hr<12;hr++){
  const input={y:1984,m:month,d:15,calendar:'lunar',leap:false,leapPolicy:'same',dayPolicy:'current',tz:8,hour:hr===0?0:hr*2,minute:0,gender:hr%2?'female':'male'};
  const chart=E.tuvi(input);actualHHCTuviCalls++;const solar=`${chart.originalSolar.y}-${String(chart.originalSolar.m).padStart(2,'0')}-${String(chart.originalSolar.d).padStart(2,'0')}`;
  iztro.astro.resetConfig();iztro.astro.config({yearDivide:'normal',horoscopeDivide:'normal',ageDivide:'normal',dayDivide:'current',algorithm:'default'});
  const iz=iztro.astro.bySolar(solar,hr,input.gender==='male'?'男':'女',false,'zh-CN');actualIztroNatalCalls++;assert.equal(iz.earthlyBranchOfSoulPalace,branches[chart.menh]);
  for(const pair of table.pairs){const hh=pair.stars.map(name=>branches[chart.stars[name].idx]),ii=pair.iztroNames.map(name=>{const p=iz.palaces.find(p=>[...p.majorStars,...p.minorStars,...p.adjectiveStars].some(x=>x.name===name));assert(p,name);return p.earthlyBranch;});assert.deepEqual(hh,ii);matchedStarBranchCoordinates+=2;
   const result=query(pair.kind,branches[chart.menh],...hh),reference=query(pair.kind,iz.earthlyBranchOfSoulPalace,...ii);assert.deepEqual(result,reference);
   runtime.push({input,solar,kind:pair.kind,hhcMingBranch:branches[chart.menh],iztroMingBranch:iz.earthlyBranchOfSoulPalace,hhcStarBranches:hh,iztroStarBranches:ii,result});
  }
 }}finally{iztro.astro.resetConfig();}assert.equal(runtime.length,288);assert.equal(matchedStarBranchCoordinates,576);assert(runtime.some(x=>x.result.geometryMatched));assert(runtime.some(x=>!x.result.geometryMatched));
});
await check('Positive geometry never becomes source pattern validation, outcome, wealth/health/character score or inferred obstruction/strength',()=>{
 for(const x of runtime){const y=x.result;assert.equal(y.fullSourceConditionsMatched,null);assert.equal(y.practicalOutcome,null);assert.equal(y.sourceExclusionScopeResolved,false);assert.equal(y.starStrengthResolved,false);assert.equal(y.sourceOutcomeValidated,false);assert(y.geometryIsNotWholePattern);}
 const x=query('sun-moon','子','亥','丑');x.unimplementedSourceConditions.length=0;x.pair.stars.length=0;assert.equal(query('sun-moon','子','亥','丑').pair.stars.length,2);assert.equal(query('sun-moon','子','亥','丑').unimplementedSourceConditions.length,4);
});
await check('Public engine/HTML/site and modules remain identical to the preserved4718-file baseline',async()=>{
 const previous=await read(resolve(w,'archives/v53-before-tuvi-star-offices/PACKAGE_MANIFEST.json'));for(const file of['Huyen_Hoc_Cac.html','site/index.html','engine.js','app.js','content.js','fortune.js','tuvi-context.js'])assert.equal(sha(await readFile(resolve(w,'v53',file))),previous.files.find(x=>x.file===file).sha256);assert.equal(sha(await readFile(resolve(w,'Huyen_Hoc_Cac.html'))),previous.product.sha256);
});
const positiveByKind=Object.fromEntries(table.pairs.map(p=>[p.kind,runtime.filter(x=>x.kind===p.kind&&x.result.geometryMatched).length]));
const out={date:'2026-10-28',checks,summary:{newJPEGBodySHA256Checks:18,selectedSourceReadings:4,exhaustiveKnownGeometries:exhaustiveKnown,exhaustiveGeometryMatches:exhaustiveTrue,actualHHCTuviCalls,actualIztroNatalCalls,realChartsPerEngine:144,matchedStarBranchCoordinates,realFlankingContexts:288,positiveByKind},runtime,actualEngine:{file:'v53/engine.js',sha256:sha(engine)},iztroVersion:'2.6.2',newHistoricalCaseClaims:0,fullSourcePatternsApplied:false,sourceOutcomesValidated:false,consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(w,'v53/qa/tuvi-flanking/REFERENCE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
