import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import assert from'node:assert/strict';
import{mountainElement,zhaijingMonthlyCoordinates}from'../research/home-you-nian/named-table-reference.mjs';
const r=resolve(import.meta.dirname,'..'),b=resolve(r,'research/home-you-nian'),read=async p=>JSON.parse(await readFile(p,'utf8')),checks=[];
function check(name,fn){fn();checks.push({name,ok:true});}
const data=await read(resolve(b,'NAMED_MOUNTAIN_ELEMENTS.json')),map=await read(resolve(b,'zhaijing/DIGITAL_UNIT_MAP.json'));
let coordinates=0;
check('Two explicit source inventories each contain24unique coordinates; 48referenceassignments match',()=>{
 for(const sys of data.systems){const seen=new Set();for(const [element,mountains]of Object.entries(sys.groups))for(const mountain of mountains){assert(!seen.has(mountain));seen.add(mountain);const x=mountainElement({system:sys.id,mountain});assert.equal(x.element,element);assert.equal(x.sourcePage,sys.prosePage);assert.equal(x.practicalOutcome,null);coordinates++;}assert.equal(seen.size,24);}
 assert.equal(coordinates,48);
});
check('Examples prevent universal mountain element substitution',()=>{assert.equal(mountainElement({system:'xieji-regular',mountain:'壬'}).element,'水');assert.equal(mountainElement({system:'xieji-hongfan',mountain:'壬'}).element,'火');assert.equal(mountainElement({system:'xieji-regular',mountain:'辛'}).element,'金');assert.equal(mountainElement({system:'xieji-hongfan',mountain:'辛'}).element,'水');});
check('All12monthly transcription rows match coordinate-only reference and keep calendar premises null',()=>{
 assert.equal(map.monthlyLifeDeathRows.length,12);for(const row of map.monthlyLifeDeathRows){const x=zhaijingMonthlyCoordinates({witness:'WYG-retained-transcription',sourceMonthNumber:row.sourceMonthNumber});assert.deepEqual(x.lifeCoordinates,row.lifeCoordinates);assert.deepEqual(x.deathCoordinates,row.deathCoordinates);assert.equal(x.calendarBoundary,null);assert.equal(x.leapMonthRule,null);assert.equal(x.practicalOutcome,null);assert(x.sourceTier.includes('not facsimile'));}
});
check('Explicit systems/months required; missing stays null and HFL glyph unresolved',()=>{
 assert.equal(mountainElement({system:'xieji-hongfan',mountain:null}).element,null);assert.equal(zhaijingMonthlyCoordinates({witness:'WYG-retained-transcription',sourceMonthNumber:null}).lifeCoordinates,null);
 for(const args of [{mountain:'壬'},{system:'universal',mountain:'壬'},{system:'xieji-regular',mountain:'甲子'},{system:'xieji-regular',mountain:'己'}])assert.throws(()=>mountainElement(args),TypeError);
 for(const sourceMonthNumber of [0,13,1.5,'1',undefined])assert.throws(()=>zhaijingMonthlyCoordinates({witness:'WYG-retained-transcription',sourceMonthNumber}),TypeError);
 assert.throws(()=>zhaijingMonthlyCoordinates({witness:'HFL',sourceMonthNumber:12}),TypeError);
});
const out={date:'2026-10-27',checks,summary:{namedMountainAssignments:coordinates,monthlySourceRows:12,calendarAdapters:0,actualHHCEngineCalls:0},consumerChanged:false,allAtomicClausesApplied:false};
await writeFile(resolve(r,'qa/home-you-nian/NAMED_TABLE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
