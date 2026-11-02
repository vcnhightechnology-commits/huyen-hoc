import{readFile,writeFile}from'node:fs/promises';
import{resolve}from'node:path';
import{createHash}from'node:crypto';
import{createRequire}from'node:module';
import assert from'node:assert/strict';
import vm from'node:vm';
import{sourceTermDirection,geographicalNaJia}from'../research/home-direction-tables/direction-reference.mjs';
import{compile}from'../research/liuyao-foundations/liuyao-reference.mjs';

const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/home-direction-tables'),q=resolve(r,'qa/home-direction-tables');
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex');
const d=await read(resolve(b,'SOURCE_TABLES.json')),checks=[];
const check=async(name,fn)=>{await fn();checks.push({name,ok:true});};
const ctx={};ctx.window=ctx;vm.createContext(ctx);
const engine=await readFile(resolve(r,'engine.js')),mountains=await readFile(resolve(r,'mountains.js'));
vm.runInContext(engine.toString(),ctx);vm.runInContext(mountains.toString(),ctx);
const require=createRequire(import.meta.url),{LunarUtil,Solar}=require(resolve(w,'v46/node_modules/lunar-typescript'));
const expectedViet=['Tý','Quý','Sửu','Cấn','Dần','Giáp','Mão','Ất','Thìn','Tốn','Tỵ','Bính','Ngọ','Đinh','Mùi','Khôn','Thân','Canh','Dậu','Tân','Tuất','Càn','Hợi','Nhâm'];
const positions=[],guaGlyphs=[],assignments=[],liuyaoContrasts=[];
let actualHHCMountainCalls=0,actualHHCPureHexCalls=0,actualLunarTermTableExecutions=0;

await check('Container, five native images and actual lunar runtime retain original audited bytes',async()=>{
 assert.equal(sha(await readFile(resolve(w,d.sourceContainer))),d.sourceSHA256);
 for(const x of d.readings)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 const audit=await read(resolve(r,'research/bazi-late-zi/VERIFICATION.json'));
 for(const x of audit.runtime)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 assert.equal(require(resolve(w,'v46/node_modules/lunar-typescript/package.json')).version,'1.8.6');
});
await check('24 source term directions match source diagram/prose and24 actual HHC model-center calls',()=>{
 assert.equal(d.source24TermRows.length,24);
 for(let i=0;i<24;i++){
  const row=d.source24TermRows[i],x=sourceTermDirection({system:'xieji-term-direction',sourceTerm:row.sourceTerm});
  assert.equal(x.mountain,row.sourceMountain);assert.equal(x.modelDegrees,i*15);assert.equal(x.solarTermInstant,null);assert.equal(x.qimenCycle,null);
  const actual=ctx.HHC_MOUNTAINS.inspect(x.modelDegrees,0);actualHHCMountainCalls++;
  assert.equal(actual.selected.name,expectedViet[i]);
  positions.push({sourceTerm:row.sourceTerm,sourceMountain:row.sourceMountain,actualMountain:actual.selected.name,derivedModelDegrees:x.modelDegrees});
 }
 assert.equal(new Set(positions.map(x=>x.sourceMountain)).size,24);
 assert.deepEqual(d.explicitCoordinateAliases,{'坎':'子','震':'卯','離':'午','兌':'酉'});
});
await check('Five declared spelling aliases align24 labels with one actual lunar term table; no source event-time assertion',()=>{
 const table=Solar.fromYmdHms(2026,6,15,12,0,0).getLunar().getJieQiTable();actualLunarTermTableExecutions++;
 let aliases=0;
 for(let i=0;i<24;i++){
  const sourceTerm=d.source24TermRows[i].sourceTerm,libraryName=d.termNameAliasesForModernLibrary[sourceTerm]??sourceTerm;
  if(libraryName!==sourceTerm)aliases++;
  assert.equal(LunarUtil.JIE_QI[i],libraryName);assert(table[libraryName]);positions[i].libraryName=libraryName;
 }
 assert.equal(aliases,5);
});
await check('24 manually read strokes give8 actual pure-hex identities and24 unique geographical assignments',()=>{
 const pureNumbers={'乾':1,'坤':2,'艮':52,'巽':57,'震':51,'兌':58,'坎':29,'離':30};
 for(const row of d.geographicalNaJiaRows){
  const bits=[...row.manualGlyphTopToBottom].reverse().map(Number),values=[...bits,...bits].map(x=>x?7:8);
  const number=ctx.HHC_ENGINE.hexNumber(values);actualHHCPureHexCalls++;assert.equal(number,pureNumbers[row.gua]);
  guaGlyphs.push({gua:row.gua,manualGlyphTopToBottom:row.manualGlyphTopToBottom,actualPureHexNumber:number});
  for(const sourceCoordinate of row.gua+row.assignedCoordinates){
   const x=geographicalNaJia({system:'xieji-geographical-najia',sourceCoordinate});
   assert.equal(x.gua,row.gua);assert.equal(x.lineStemBranches,null);assert.equal(x.practicalOutcome,null);assignments.push(x);
  }
 }
 assert.equal(guaGlyphs.length,8);assert.equal(assignments.length,24);assert.equal(new Set(assignments.map(x=>x.sourceCoordinate)).size,24);
});
await check('Two actual private Liuyao charts preserve 戊/己 instead of importing geographical 癸/壬',()=>{
 for(const gua of['坎','離']){
  const row=d.geographicalNaJiaRows.find(x=>x.gua===gua),bits=[...row.manualGlyphTopToBottom].reverse().map(Number);
  const out=compile([...bits,...bits].map(x=>x?7:8)),stems=[...new Set(out.lines.map(x=>x.stem))];
  assert.equal(out.primary.number,gua==='坎'?29:30);assert.deepEqual(stems,gua==='坎'?['戊']:['己']);
  const geographicalStem=row.assignedCoordinates[0];assert(!stems.includes(geographicalStem));
  liuyaoContrasts.push({gua,geographicalStem,actualPrivateLiuyaoStems:stems});
 }
 const unknown=d.nextSourceClauses.find(x=>x.id==='D56-02');assert(unknown.text.includes('其法不知所自來'));
 assert.equal(d.historicalCitationIndependentlyVerified,false);
});
await check('Named systems, source spellings and coordinate roles are explicit; unknowns stay null',()=>{
 assert.equal(sourceTermDirection({system:'xieji-term-direction',sourceTerm:null}).mountain,null);
 assert.equal(geographicalNaJia({system:'xieji-geographical-najia',sourceCoordinate:null}).gua,null);
 for(const sourceCoordinate of['戊','己','子','卯','午','酉','坎癸',undefined,24])
  assert.throws(()=>geographicalNaJia({system:'xieji-geographical-najia',sourceCoordinate}),TypeError);
 for(const sourceTerm of['惊蛰','谷雨','立春艮',undefined])
  assert.throws(()=>sourceTermDirection({system:'xieji-term-direction',sourceTerm}),TypeError);
 assert.throws(()=>sourceTermDirection({sourceTerm:'立春'}),TypeError);
 assert.throws(()=>geographicalNaJia({sourceCoordinate:'乾'}),TypeError);
 const input={system:'xieji-geographical-najia',sourceCoordinate:'震'},before=JSON.stringify(input),out=geographicalNaJia(input);
 out.relatedCoordinates[0]='X';assert.equal(geographicalNaJia(input).relatedCoordinates[0],'震');assert.equal(JSON.stringify(input),before);
});
await check('Eight contextual source segments are inventoried and all research remains outside unchanged consumer HTML',async()=>{
 assert.equal(d.nextSourceClauses.length,8);assert.equal(d.diagramReadings.najiaLineGlyphs,24);
 const html=await readFile(resolve(r,'Huyen_Hoc_Cac.html'));
 assert.equal(sha(html),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');
 assert(html.toString().includes(mountains.toString().trim()));
 for(const x of['home-direction-tables','direction-reference','xieji-geographical-najia'])assert(!html.includes(Buffer.from(x)));
});
const summary={termRows:24,termCoordinateLabels:24,najiaCoordinates:24,manualGlyphs:24,contextualProseSegments:8,
 actualHHCMountainCalls,actualHHCPureHexCalls,actualLunarTermTableExecutions,actualPrivateLiuyaoContrasts:liuyaoContrasts.length,
 newHTTPRequests:0,newSourcePages:0,expandedPreviouslyReadPages:5};
const out={date:'2026-10-27',checks,summary,positions,guaGlyphs,assignments,liuyaoContrasts,
 consumerChanged:false,astronomicalInstantsVerifiedBySource:false,physicalCompassAdapterEstablished:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...summary}));
