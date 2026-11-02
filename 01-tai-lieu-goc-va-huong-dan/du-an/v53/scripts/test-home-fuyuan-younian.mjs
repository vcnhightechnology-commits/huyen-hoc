import {readFile,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';
import vm from 'node:vm';
import {pathToFileURL} from 'node:url';
import assert from 'node:assert/strict';
import {sourceFuyuan,sourceYouNian} from '../research/home-yangzhai-fuyuan/fuyuan-younian-reference.mjs';
const b=resolve(import.meta.dirname,'../research/home-yangzhai-fuyuan'),w=resolve(b,'../../..'),r=resolve(w,'v53');
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex');
const require=createRequire(import.meta.url),lunar=require(resolve(w,'v46/node_modules/lunar-typescript'));
const system='YZSS-Tianyige-fuyuan-dayounian',checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const table=await read(resolve(b,'MANUAL_FUYUAN_TABLE.json')),seq=await read(resolve(b,'MANUAL_YOUNIAN_SEQUENCES.json'));
let annotations=0;
await check('180 manually entered rows /360 cells match independent source counting rule, including40 central remaps',()=>{
 assert.equal(table.rows.length,180);const seen=new Set();
 for(const row of table.rows){const key=row.era+row.ordinal;assert(!seen.has(key));seen.add(key);
  for(const sourceSex of ['male','female']){const x=sourceFuyuan({system,era:row.era,ordinal:row.ordinal,sourceSex});
   assert.equal(x.trigram,row[sourceSex].normalizedTrigram,key+sourceSex);
   assert.equal(x.rawPalaceNumber===5,row[sourceSex].printedCentralAnnotation,key+sourceSex+'central');
   if(x.rawPalaceNumber===5)annotations++;
   assert.equal(x.birthYearBoundary,null);assert.equal(x.modernDateAdapter,null);assert.equal(x.practicalOutcome,null);
  }
 }assert.equal(annotations,40);
});
const matrix=[];
await check('Eight source sequences expand to64 coordinate labels with an explicit compass order and self role',()=>{
 const expectedNames=seq.abbreviations;
 for(const row of seq.rows){assert.equal(row.tokens.length,7);const originIndex=seq.clockwiseOrder.indexOf(row.origin);
  for(let offset=0;offset<8;offset++){const target=seq.clockwiseOrder[(originIndex+offset)%8];
   const expected=offset===0?'伏位':expectedNames[row.tokens[offset-1]],x=sourceYouNian({system,anchorKind:'declared-source-gate',origin:row.origin,target});
   assert.equal(x.relation,expected);assert.equal(x.conditionalClassification,null);assert.equal(x.practicalOutcome,null);
   matrix.push({origin:row.origin,target,relation:expected,star:x.star,elementRelation:x.elementRelation,
    sourcePage:offset===0?59:58,coordinateDerivation:'Declared clockwise expansion of the manually entered compact line'});
  }
 }assert.equal(new Set(matrix.map(x=>x.origin+x.target)).size,64);
});
await check('Birth and declared gate contexts remain explicit; unknown context and missing coordinates stay unresolved',()=>{
 for(const anchorKind of ['birth-fuyuan','declared-source-gate'])for(const row of matrix){const x=sourceYouNian({system,anchorKind,origin:row.origin,target:row.target});assert.equal(x.relation,row.relation);assert.equal(x.anchorKind,anchorKind);}
 for(const args of [{anchorKind:'unknown',origin:'乾',target:'坎'}, {anchorKind:'birth-fuyuan',origin:null,target:'坎'}, {anchorKind:'declared-source-gate',origin:'乾',target:null}])assert.equal(sourceYouNian({system,...args}).relation,null);
 for(const args of [{era:null,ordinal:1,sourceSex:'male'},{era:'upper',ordinal:null,sourceSex:'female'},{era:'lower',ordinal:1,sourceSex:null}])assert.equal(sourceFuyuan({system,...args}).trigram,null);
});
await check('Source-palace element relation has direction, without predicting health, wealth or family outcomes',()=>{
 const x=sourceYouNian({system,anchorKind:'declared-source-gate',origin:'乾',target:'坎'});
 assert.equal(x.star,'文曲');assert.equal(x.starElement,'水');assert.equal(x.palaceElement,'水');assert.equal(x.elementRelation,'same-element');
 const types=new Set(matrix.map(x=>x.elementRelation));assert.equal(types.size,5);
 for(const x of matrix){const actual=sourceYouNian({system,anchorKind:'birth-fuyuan',origin:x.origin,target:x.target});assert.equal(actual.practicalOutcome,null);assert.equal(actual.conditionalClassification,null);}
});
await check('Strict source API rejects implicit periods, Gregorian years, sitting-direction substitution and hidden fields',()=>{
 const a={system,era:'upper',ordinal:1,sourceSex:'male'},c={system,anchorKind:'birth-fuyuan',origin:'乾',target:'坎'};
 for(const args of [{...a,year:1984},{...a,era:'automatic'},{...a,ordinal:0},{...a,ordinal:61},{...a,ordinal:'1'},{...a,sourceSex:'unknown'},{system,ordinal:1,sourceSex:'male'},Object.assign(Object.create(null),a)])assert.throws(()=>sourceFuyuan(args),TypeError);
 for(const args of [{...c,sitting:'乾'},{...c,anchorKind:'house-facing'},{...c,origin:6},{...c,target:'良'},{...c,system:'xieji-da'}])assert.throws(()=>sourceYouNian(args),TypeError);
 const hidden={...a};Object.defineProperty(hidden,'ordinal',{value:1,enumerable:false});assert.throws(()=>sourceFuyuan(hidden),TypeError);
 const symbol={...a};symbol[Symbol('year')]=1984;assert.throws(()=>sourceFuyuan(symbol),TypeError);
});
const bytes=await readFile(resolve(r,'engine.js')),ctx={window:{}};vm.createContext(ctx);vm.runInContext(bytes.toString(),ctx);
const engine=ctx.window.HHC_ENGINE,eraNames={'上元':'upper','中元':'middle','下元':'lower'};
const packageInfo=await read(resolve(w,'v46/node_modules/lunar-typescript/package.json'));assert.equal(packageInfo.version,'1.8.6');
const yearFixtures=[];let actualHHCDirections=0,actualLunarYearObjects=0,actualLunarYearFields=0,labelComparisons=0;
const trigramNumbers={坎:1,坤:2,震:3,巽:4,乾:6,兌:7,艮:8,離:9},directions={乾:'Tây Bắc',坎:'Bắc',艮:'Đông Bắc',震:'Đông',巽:'Đông Nam',離:'Nam',坤:'Tây Nam',兌:'Tây'};
const labels={伏位:'Phục Vị',生氣:'Sinh Khí',天乙:'Thiên Y',延年:'Diên Niên',禍害:'Họa Hại',六煞:'Lục Sát',五鬼:'Ngũ Quỷ',絕命:'Tuyệt Mệnh'};
await check('Actual lunar1.8.6 annual fields select all180 source coordinates;360 actual HHC year-sex executions match source cells',()=>{
 const seen=new Set();
 for(let year=1900;year<2080;year++){
  const ly=lunar.LunarYear.fromYear(year);actualLunarYearObjects++;
  const ganZhi=ly.getGanZhi(),yuan=ly.getYuan();actualLunarYearFields+=2;
  const era=eraNames[yuan],row=table.rows.find(x=>x.era===era&&x.sexagenary===ganZhi);assert(row,year+' '+yuan+ganZhi);
  seen.add(era+row.ordinal);
  for(const gender of ['male','female']){
   const input={year,gender},out=engine.directions(input);actualHHCDirections++;
   const expected=row[gender].normalizedTrigram;assert.equal(out.number,trigramNumbers[expected],year+gender);
   const measured=[];
   for(const cell of matrix.filter(x=>x.origin===expected)){const actual=out.all.find(x=>x.direction===directions[cell.target])?.label;
    assert.equal(actual,labels[cell.relation]);labelComparisons++;measured.push({target:cell.target,sourceRelation:cell.relation,engineLabel:actual});}
   yearFixtures.push({input,lunarAnnualFields:{ganZhi,yuan},sourceCoordinate:{era,ordinal:row.ordinal,sourcePDFPage:row.sourcePDFPage},
    sourceTrigram:expected,HHCNumber:out.number,sourceCentralAnnotation:row[gender].printedCentralAnnotation,labels:measured});
  }
 }assert.equal(seen.size,180);assert.equal(actualHHCDirections,360);assert.equal(labelComparisons,2880);
});
await check('An earlier different-work source reference matches64 normalized relations, without asserting textual independence',async()=>{
 const {youNian}=await import(pathToFileURL(resolve(r,'research/home-you-nian/you-nian-reference.mjs')).href);
 for(const x of matrix){const old=youNian({system:'xieji-da',origin:x.origin,target:x.target});assert.equal(old.relation,seq.comparisonAliases[x.relation]??x.relation);}
});
await check('Consumer bytes remain unchanged and exclude the research APIs',async()=>{
 const html=await readFile(resolve(r,'Huyen_Hoc_Cac.html'));assert.equal(sha(html),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');
 assert.deepEqual(html,await readFile(resolve(w,'Huyen_Hoc_Cac.html')));assert.deepEqual(html,await readFile(resolve(r,'site/index.html')));
 for(const term of ['YZSS-Tianyige-fuyuan-dayounian','sourceFuyuan','home-yangzhai-fuyuan'])assert(!html.toString().includes(term));
});
const out={date:'2026-10-28',checks,summary:{manualSourceRows:180,manualSexSpecificCells:360,centralRemaps:annotations,
 compactSequences:8,derivedCompassCoordinates:64,actualLunarYearObjects,actualLunarAnnualFieldQueries:actualLunarYearFields,
 actualHHCDirectionsExecutions:actualHHCDirections,repeatedDirectionLabelComparisons:labelComparisons,
 priorDifferentWorkRelationComparisons:64},engineSHA256:sha(bytes),lunarVersion:'1.8.6',
 lunarRuntimeSHA256:sha(await readFile(resolve(w,'v46/node_modules/lunar-typescript/dist/index.cjs'))),
 annualBridgeScope:'Software convention comparison of declared annual numbers1900–2079. Lunar annual yuan/sexagenary fields select a source coordinate; this does not prove the source regnal headings, historical Gregorian conversion, or a birth-date boundary.',
 sourceMatrix:matrix,yearFixtures,consumerChanged:false,wholeCatalogueCompleted:false,
 notValidated:['Historical regnal conversion/萬曆五十二年','Tết/LậpXuân or any birth-date boundary','Modern geometry/room placement/relative heights','Complete clauses or empirical source outcomes']};
await writeFile(resolve(r,'qa/home-yangzhai-fuyuan/REFERENCE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,...out.summary}));
