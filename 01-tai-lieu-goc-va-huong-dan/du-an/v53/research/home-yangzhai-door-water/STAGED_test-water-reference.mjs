import {readFile,writeFile} from 'node:fs/promises';import {resolve} from 'node:path';
import {createHash} from 'node:crypto';import vm from 'node:vm';import assert from 'node:assert/strict';
import {sourceMountainPolarity,sourceWaterTable} from './source-water-reference.mjs';
const b=import.meta.dirname,w=resolve(b,'../..'),r=resolve(w,'v53'),system='YZSS-Tianyige-water-mountain-table';
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const table=await read(resolve(b,'MANUAL_WATER_TABLE.json')),polar=await read(resolve(b,'MANUAL_SOURCE_POLARITY.json'));
await check('24 source mountain rows retain46 main literal target entries and16 separate marginal entries',()=>{
 assert.equal(table.rows.length,24);assert.equal(new Set(table.rows.map(x=>x.mountain)).size,24);
 assert.equal(table.rows.reduce((n,x)=>n+x.mainText.targets.length,0),46);
 assert.equal(table.rows.filter(x=>x.marginalText!==null).length,8);
 assert.equal(table.rows.reduce((n,x)=>n+(x.marginalText?.targets.length??0),0),16);
 for(const x of table.rows){assert([109,110].includes(x.sourcePDFPage));assert.equal(x.courtyardMeaningEncoded,false);}
});
await check('Source-specific12/12 polarity covers24 mountains with four declared cardinal aliases',()=>{
 assert.equal(polar.yangMarks.length,12);assert.equal(polar.yinMarks.length,12);
 assert.equal(new Set([...polar.yangMarks,...polar.yinMarks]).size,24);
 const out=table.rows.map(x=>sourceMountainPolarity({system,mountain:x.mountain}));
 assert.equal(out.filter(x=>x.polarity==='陽').length,12);assert.equal(out.filter(x=>x.polarity==='陰').length,12);
 for(const [mark,expected]of Object.entries({子:'坎',午:'離',卯:'震',酉:'兌'}))assert.equal(out.find(x=>x.mountain===mark).sourceMark,expected);
 assert.equal(sourceMountainPolarity({system,mountain:null}).polarity,null);
 for(const x of out){assert.equal(x.universalPolarity,null);assert.equal(x.practicalOutcome,null);}
});
let flowContexts=0;
await check('72 mountain/flow contexts prevent reversing outflow instructions into incoming-water guidance',()=>{
 for(const row of table.rows)for(const flow of ['outflow','inflow','unknown']){
  const out=sourceWaterTable({system,mountain:row.mountain,anchorBasis:'mountain-dragon',flow,targetMark:null});flowContexts++;
  if(flow==='outflow'){assert.deepEqual(out.mainText,row.mainText);assert.deepEqual(out.marginalText,row.marginalText);assert(out.sourceFrameEstablished);}
  else{assert.equal(out.mainText,null);assert.equal(out.marginalText,null);assert(!out.sourceFrameEstablished);}
  assert.equal(out.mainTextContainsTarget,null);assert.equal(out.sourceClassification,null);assert.equal(out.practicalOutcome,null);assert.equal(out.engineeringAdvice,null);
 }assert.equal(flowContexts,72);
});
let alternateAnchorContexts=0;
await check('72 alternate-anchor contexts do not substitute birth-gua or gate-facing for source mountain-dragon frame',()=>{
 for(const row of table.rows)for(const anchorBasis of ['birth-fuyuan','gate-facing','unknown']){
  const out=sourceWaterTable({system,mountain:row.mountain,anchorBasis,flow:'outflow',targetMark:'甲'});alternateAnchorContexts++;
  assert.equal(out.mainText,null);assert.equal(out.mainTextContainsTarget,null);assert.equal(out.sourceClassification,null);
 }assert.equal(alternateAnchorContexts,72);
});
await check('Native-crop difficult rows keep main/marginal stars separate and absent targets are not bad outcomes',()=>{
 const get=(mountain,targetMark)=>sourceWaterTable({system,mountain,anchorBasis:'mountain-dragon',flow:'outflow',targetMark});
 const yin=get('寅','甲');assert.equal(yin.mainText.star,'廉貞');assert.deepEqual(yin.mainText.targets,['壬','癸']);assert.equal(yin.mainTextContainsTarget,false);assert.equal(yin.marginalText.star,'六煞');assert.equal(yin.marginalTextContainsTarget,true);
 for(const mountain of ['巽','巳']){const x=get(mountain,'丙');assert.equal(x.mainText.star,'六煞');assert.equal(x.marginalText.star,'巨門');assert.equal(x.mainTextContainsTarget,false);assert.equal(x.marginalTextContainsTarget,true);assert.equal(x.sourceClassification,null);}
 assert.deepEqual(get('午','乾').mainText,{targets:['乾'],star:'破軍'});
 assert.equal(get('壬','庚').marginalTextContainsTarget,null);assert.equal(get('壬','庚').practicalOutcome,null);
 const out=get('寅','甲');out.mainText.targets.push('甲');assert.equal(get('寅','甲').mainTextContainsTarget,false);
});
await check('Strict API rejects degree/year/implicit context and keeps unknown mountain unresolved',()=>{
 const a={system,mountain:'壬',anchorBasis:'mountain-dragon',flow:'outflow',targetMark:'甲'};
 assert.equal(sourceWaterTable({...a,mountain:null}).mainText,null);
 for(const x of [{...a,degrees:350},{...a,year:2026},{...a,anchorBasis:'sitting'},{...a,flow:'auto'},
  {...a,mountain:'坎'},{...a,targetMark:'東'},{system,mountain:'壬',flow:'outflow',targetMark:'甲'},
  Object.assign(Object.create(null),a)])assert.throws(()=>sourceWaterTable(x),TypeError);
 const hidden={...a};Object.defineProperty(hidden,'flow',{value:'outflow',enumerable:false});assert.throws(()=>sourceWaterTable(hidden),TypeError);
});
const room=await read(resolve(b,'MANUAL_ROOM_PAIR_ANCHORS.json')),old=await read(resolve(r,'research/full-study/home/DAYOUNIAN_ENGINE_CHECK.json'));
const bytes=await readFile(resolve(r,'engine.js')),ctx={window:{}};vm.createContext(ctx);vm.runInContext(bytes.toString(),ctx);
const access=new Map(old.results.map(x=>[x.sourceTrigram,x.engineAccessInput]));
const directions={乾:'Tây Bắc',坎:'Bắc',艮:'Đông Bắc',震:'Đông',巽:'Đông Nam',離:'Nam',坤:'Tây Nam',兌:'Tây'};
let actualHHCDirections=0;const roomFixtures=[];
await check('Eight actual HHC direction calls match source95 four printed opposite room pairs in both declared orders',()=>{
 for(const row of room.rows)for(const [origin,target]of [row.rooms,[...row.rooms].reverse()]){
  const input=access.get(origin),out=ctx.window.HHC_ENGINE.directions(input);actualHHCDirections++;
  const actual=out.all.find(x=>x.direction===directions[target])?.label;assert.equal(actual,'Diên Niên');
  roomFixtures.push({origin,target,sourcePDFPage:95,printedRelation:row.printedRelation,engineInput:input,actual,
   scope:'Conditional relation projection; source room identity is explicitly declared, not a modern plan or birth-date validation.'});
 }assert.equal(actualHHCDirections,8);
});
await check('Consumer HTML remains byte identical and excludes all new private lookups',async()=>{
 const html=await readFile(resolve(r,'Huyen_Hoc_Cac.html'));assert.equal(sha(html),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');
 assert.deepEqual(html,await readFile(resolve(w,'Huyen_Hoc_Cac.html')));assert.deepEqual(html,await readFile(resolve(r,'site/index.html')));
 for(const s of ['sourceWaterTable','home-yangzhai-door-water','YZSS-Tianyige-water-mountain-table'])assert(!html.toString().includes(s));
});
const result={date:'2026-10-28',checks,summary:{manualMainRows:24,mainTargetEntries:46,marginalRows:8,marginalTargetEntries:16,
 sourcePolarityMarks:24,flowContexts,alternateAnchorContexts,printedOppositeRoomPairs:4,projectedRoomContexts:8,
 actualHHCDirectionsExecutions:actualHHCDirections,newCalendarExecutions:0},engineSHA256:sha(bytes),roomFixtures,
 scope:'Literal outflow table with explicit source frame/flow and main/marginal distinction; source-specific polarity. Actual-engine comparison only for four source95 room pairs in both orders. Not comparing drainage star labels to an assumed modern palace origin.',
 notValidated:['Complete first-draw exchange','Modern directions/north/plan/degree conversion','Door ruler units/face/dimensions','Annual/monthly/daily door date conditions','Hydraulic engineering or source efficacy'],consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(b,'REFERENCE_RESULTS.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...result.summary}));
