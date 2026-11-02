import {readFile,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import {pairedElement,namedCenter,ringCoordinates} from '../research/home-rings/rings-reference.mjs';
import {mountainElement} from '../research/home-you-nian/named-table-reference.mjs';

const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/home-rings'),q=resolve(r,'qa/home-rings');
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex');
const diagrams=await read(resolve(b,'DIAGRAM_LABELS.json')),rows=await read(resolve(b,'PAIRED_ELEMENT_ROWS.json'));
const model=await read(resolve(b,'ANGULAR_MODEL.json')),checks=[];
const check=async(name,fn)=>{await fn();checks.push({name,ok:true});};
const normal=x=>(x%360+360)%360;
const canonical=[...'子癸丑艮寅甲卯乙辰巽巳丙午丁未坤申庚酉辛戌乾亥壬'];
const viet=['Tý','Quý','Sửu','Cấn','Dần','Giáp','Mão','Ất','Thìn','Tốn','Tỵ','Bính','Ngọ','Đinh','Mùi','Khôn','Thân','Canh','Dậu','Tân','Tuất','Càn','Hợi','Nhâm'];
const base={system:'xieji-three-needles',angularModel:'equal24-zi-zero-clockwise',endpointPolicy:'both-at-touch'};
const elementSystem='xieji-double-mountain',rings=['regular','middle','seam'];
const halfPositions={regular:0,middle:-1,seam:1};
const expectedUses={regular:'定向',middle:'格龍',seam:'消砂納水'};
let actualHHCMountainCalls=0,namedAssignments=0,centerContexts=0,boundaryContexts=0,flankContexts=0,uncertaintyContexts=0;
const ctx={};ctx.window=ctx;vm.createContext(ctx);
const mountainBytes=await readFile(resolve(r,'mountains.js'));
vm.runInContext(mountainBytes.toString(),ctx);
function actual(angle){actualHHCMountainCalls++;return ctx.HHC_MOUNTAINS.inspect(normal(angle),0);}
const coordinateEvidence=[];

await check('Retained container, six native pages and current embedded mountain engine retain audited bytes',async()=>{
 const source=await read(resolve(b,'MANUAL_READINGS.json'));
 assert.equal(sha(await readFile(resolve(w,source.sourceContainer))),source.sourceSHA256);
 for(const p of source.readings)assert.equal(sha(await readFile(resolve(w,p.file))),p.sha256);
 const old=await read(resolve(w,'archives/v53-before-home-rings/PACKAGE_MANIFEST.json'));
 assert.equal(sha(mountainBytes),old.files.find(x=>x.file==='mountains.js').sha256);
 assert((await readFile(resolve(r,'Huyen_Hoc_Cac.html'),'utf8')).includes(mountainBytes.toString().trim()));
});

await check('96 literal diagram labels and24 arcs have no missing label or silently shifted pair',()=>{
 assert.equal(diagrams.directLabels,96);assert.equal(diagrams.directPairArcs,24);
 for(const d of diagrams.diagrams){
  assert.deepEqual(d.outerFromZi,canonical);assert.deepEqual(d.innerFromZi,canonical);
  assert.equal(d.sourceOffsetHalfPositions,halfPositions[d.ring]);
  const expectedPairs=rows.rows.flatMap(x=>x.pairs).sort();
  assert.deepEqual(d.innerPairArcs.slice().sort(),expectedPairs);
  assert.deepEqual(d.ziBetweenRegularLabels,d.ring==='middle'?['壬','子']:['子','癸']);
 }
});

await check('48 named ring assignments preserve all4 triads,12 pairs,24 mountains and separate uses',()=>{
 for(const ring of ['middle','seam'])for(const row of rows.rows)for(const pair of row.pairs)for(const mountain of pair){
  const out=pairedElement({system:elementSystem,ring,mountain});
  assert.equal(out.pair,pair);assert.equal(out.element,row.element);
  assert.equal(out.triadBranches,row.branchesInSourceLifeProsperityTombOrder);
  assert.equal(out.sourceUse,expectedUses[ring]);assert.equal(out.practicalOutcome,null);namedAssignments++;
 }
 assert.equal(namedAssignments,48);
 assert.equal(new Set(rows.rows.flatMap(x=>[...x.sourceMountains])).size,24);
 assert(!rows.rows.some(x=>x.element==='土'));
});

const comparisons=[];
await check('Same glyph differs from regular16/24 and Hongfan17/24; no universal table or implicit alias',()=>{
 const aliases={'子':'坎','卯':'震','午':'離','酉':'兌'};
 for(const mountain of canonical){
  const paired=pairedElement({system:elementSystem,ring:'middle',mountain});
  const regular=mountainElement({system:'xieji-regular',mountain});
  const hongfan=mountainElement({system:'xieji-hongfan',mountain:aliases[mountain]??mountain});
  comparisons.push({mountain,paired:paired.element,regular:regular.element,hongfan:hongfan.element,hongfanExplicitAlias:aliases[mountain]??null});
 }
 assert.equal(comparisons.filter(x=>x.paired!==x.regular).length,16);
 assert.equal(comparisons.filter(x=>x.paired!==x.hongfan).length,17);
 assert.throws(()=>pairedElement({system:elementSystem,ring:'middle',mountain:'坎'}),TypeError);
});

await check('72 source-label centers use explicit half-position geometry and actual consumer engine coordinates',()=>{
 for(const ring of rings)for(let i=0;i<24;i++){
  const mountain=canonical[i],center=normal((i+halfPositions[ring]/2)*15);
  const out=namedCenter({...base,ring,mountain});assert.equal(out.regularModelDegrees,center);
  assert.equal(out.sourceOffsetHalfPositions,halfPositions[ring]);assert.equal(out.sourceUse,expectedUses[ring]);
  const point=ringCoordinates({...base,ring,regularModelDegrees:center,uncertaintyDegrees:0});
  assert.equal(point.mountain,mountain);assert.equal(point.possible.length,1);
  const normalizedActual=actual(center-halfPositions[ring]*7.5);
  assert.equal(normalizedActual.selected.name,viet[i]);
  coordinateEvidence.push({ring,mountain,regularModelDegrees:center,actualEngineName:normalizedActual.selected.name});centerContexts++;
 }
 assert.equal(centerContexts,72);
});

await check('72 exact boundaries keep both touching labels;144 flanks retain the correct side',()=>{
 for(const ring of rings)for(let i=0;i<24;i++){
  const next=(i+1)%24,boundary=normal((i+halfPositions[ring]/2+.5)*15);
  const out=ringCoordinates({...base,ring,regularModelDegrees:boundary,uncertaintyDegrees:0});
  assert.equal(out.mountain,null);assert.deepEqual(out.possible.map(x=>x.mountain).sort(),[canonical[i],canonical[next]].sort());
  // Existing user engine intentionally uses clockwise half-open endpoints.
  // The private source reference explicitly retains both at a touch instead.
  assert.equal(actual(boundary-halfPositions[ring]*7.5).selected.name,viet[next]);boundaryContexts++;
  for(const [delta,index]of[[-.001,i],[.001,next]]){
   const angle=normal(boundary+delta),side=ringCoordinates({...base,ring,regularModelDegrees:angle,uncertaintyDegrees:0});
   assert.equal(side.mountain,canonical[index]);assert.equal(actual(angle-halfPositions[ring]*7.5).selected.name,viet[index]);flankContexts++;
  }
 }
 assert.equal(boundaryContexts,72);assert.equal(flankContexts,144);
});

await check('72 uncertainty intervals retain three adjacent labels; full circle and zero wrap keep all possibilities',()=>{
 for(const ring of rings){
  for(let i=0;i<24;i++){
   const center=normal((i+halfPositions[ring]/2)*15),out=ringCoordinates({...base,ring,regularModelDegrees:center,uncertaintyDegrees:8});
   assert.deepEqual(out.possible.map(x=>x.mountain).sort(),[canonical[(i+23)%24],canonical[i],canonical[(i+1)%24]].sort());
   assert.equal(out.mountain,null);uncertaintyContexts++;
  }
  const all=ringCoordinates({...base,ring,regularModelDegrees:0,uncertaintyDegrees:180});
  assert.equal(all.possible.length,24);assert.equal(all.mountain,null);
  assert.equal(all.possibleElements.length,ring==='regular'?0:4);assert.equal(all.element,null);
  assert.deepEqual(ringCoordinates({...base,ring,regularModelDegrees:360,uncertaintyDegrees:0}),ringCoordinates({...base,ring,regularModelDegrees:0,uncertaintyDegrees:0}));
 }
 assert.equal(uncertaintyContexts,72);
});

await check('Same physical model angle is not the same named ring coordinate; uncertain labels do not force an element',()=>{
 const at=(ring,angle)=>ringCoordinates({...base,ring,regularModelDegrees:angle,uncertaintyDegrees:0});
 assert.equal(at('middle',10).mountain,'癸');assert.equal(at('middle',10).element,'金');
 assert.equal(at('seam',10).mountain,'子');assert.equal(at('seam',10).element,'水');
 assert.deepEqual(at('middle',0).possibleElements.slice().sort(),['水','金'].sort());assert.equal(at('middle',0).element,null);
 assert.equal(at('seam',0).mountain,null);assert.equal(at('seam',0).pair,'壬子');assert.equal(at('seam',0).element,'水');
 assert.equal(at('middle',15).pair,'癸丑');assert.equal(at('middle',15).element,'金');
 for(const ring of rings)assert.equal(at(ring,10).physicalNorthCalibration,null);
});

await check('Missing coordinates stay unknown; named system, ring, model, endpoint and uncertainty are mandatory',()=>{
 for(const ring of rings){
  const out=ringCoordinates({...base,ring,regularModelDegrees:null,uncertaintyDegrees:0});
  assert.equal(out.mountain,null);assert.deepEqual(out.possible,[]);assert.equal(out.element,null);assert.equal(out.practicalOutcome,null);
  assert.equal(namedCenter({...base,ring,mountain:null}).regularModelDegrees,null);
 }
 assert.equal(pairedElement({system:elementSystem,ring:'seam',mountain:null}).element,null);
 const valid={...base,ring:'middle',regularModelDegrees:0,uncertaintyDegrees:0},before=JSON.stringify(valid);
 ringCoordinates(valid);assert.equal(JSON.stringify(valid),before);
 for(const override of[{system:undefined},{angularModel:'true-north'},{endpointPolicy:undefined},{ring:'universal'},{regularModelDegrees:NaN},{regularModelDegrees:361},{regularModelDegrees:''},{uncertaintyDegrees:undefined},{uncertaintyDegrees:-1},{uncertaintyDegrees:181}])
  assert.throws(()=>ringCoordinates({...valid,...override}),TypeError);
 assert.throws(()=>pairedElement({system:elementSystem,ring:'regular',mountain:'子'}),TypeError);
 assert.throws(()=>pairedElement({system:elementSystem,ring:'middle'}),TypeError);
 assert.throws(()=>namedCenter({...base,ring:'seam',mountain:'甲子'}),TypeError);
});

await check('All15 printed prose segments are inventoried; degree model and private source content stay off the user site',async()=>{
 const clauses=await read(resolve(b,'SOURCE_CLAUSES.json'));assert.equal(clauses.passages.length,15);
 assert.equal(model.derivedHalfStepDegrees,7.5);assert.equal(model.physicalNorthCalibration,null);
 const html=await readFile(resolve(r,'Huyen_Hoc_Cac.html'));
 assert.equal(sha(html),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');
 assert(!html.includes(Buffer.from('rings-reference')));assert(!html.includes(Buffer.from('home-rings')));
 assert.equal(actualHHCMountainCalls,288);
});

const out={date:'2026-10-27',checks,summary:{directDiagramLabels:96,directPairArcs:24,enumeratedProseSegments:15,namedRingAssignments:namedAssignments,
 actualHHCMountainCalls,centerContexts,boundaryContexts,flankContexts,uncertaintyContexts,
 pairedVersusRegularDifferences:16,pairedVersusHongfanDifferences:17,newHTTPRequests:0,newSourcePages:0,expandedPreviouslyReadPages:6},
 coordinateEvidence,tableComparisons:comparisons,mountainEngineSHA256:sha(mountainBytes),
 consumerChanged:false,physicalCompassAdapterEstablished:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...out.summary}));
