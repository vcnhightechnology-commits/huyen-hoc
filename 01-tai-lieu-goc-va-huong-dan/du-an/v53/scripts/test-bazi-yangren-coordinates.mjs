import {readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createRequire}from'node:module';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{sourceBladeCoordinates as inspect}from'../research/bazi-yangren-conditions/coordinate-reference.mjs';
const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/bazi-yangren-conditions'),q=resolve(r,'qa/bazi-yangren-conditions'),req=createRequire(import.meta.url),L=req(resolve(w,'v46/node_modules/lunar-typescript')),sha=x=>createHash('sha256').update(x).digest('hex');
const read=async p=>JSON.parse(await readFile(p,'utf8')),source=await read(resolve(b,'SOURCE_COORDINATES.json')),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const code=await readFile(resolve(r,'engine.js'));assert.equal(sha(code),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');
const audit=await read(resolve(r,'research/bazi-late-zi/VERIFICATION.json'));for(const x of audit.runtime)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
const c={};c.window=c;vm.createContext(c);vm.runInContext(code.toString(),c);const E=c.HHC_ENGINE;
const branches='子丑寅卯辰巳午未申酉戌亥',stems='甲乙丙丁戊己庚辛壬癸',sixty=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
let lunarSearchCalls=0,lunarForwardCalls=0,hhcCalls=0;const runtime=[],dates=new Map();
await check('Source daysets have3/3/4 distinct literal coordinates and negative examples contain8 separate day/hour pairs',()=>{
 assert.deepEqual(source.tables.map(x=>x.days),[['戊午','丙午','壬子'],['癸丑','丁未','己未'],['丙子','丁丑','戊子','己丑']]);
 assert.equal(source.negativeDayHourPairs.length,8);assert.equal(new Set(source.negativeDayHourPairs.map(x=>x.day+':'+x.hour)).size,8);
 for(const t of source.tables)for(const p of t.days)assert(sixty.includes(p));for(const x of source.negativeDayHourPairs){assert(sixty.includes(x.day));assert(sixty.includes(x.hour));}
});
await check('A bounded60day real lunar search locates8 explicit day/hour fixtures;8 actual HHC and8 lunar forward charts match all pillars and source pair coordinates',()=>{
 const start=L.Solar.fromYmdHms(2000,1,1,12,0,0);
 for(let i=0;i<60;i++){const d=start.next(i),ec=d.getLunar().getEightChar();ec.setSect(2);lunarSearchCalls++;dates.set(ec.getDay(),d);}
 assert.equal(dates.size,60);
 for(const x of source.negativeDayHourPairs){const d=dates.get(x.day),input={y:d.getYear(),m:d.getMonth(),d:d.getDay(),hour:branches.indexOf(x.hour[1])*2,minute:0,tz:8,gender:'male',dayPolicy:'midnight',lateZiHour:'day'};
  const ec=L.Solar.fromYmdHms(input.y,input.m,input.d,input.hour,0,0).getLunar().getEightChar();ec.setSect(2);lunarForwardCalls++;
  const chart=E.bazi(input);hhcCalls++;const pillars=Array.from(chart.pillars,p=>p.han),expected=[ec.getYear(),ec.getMonth(),ec.getDay(),ec.getTime()];assert.deepEqual(pillars,expected);
  assert.equal(pillars[2],x.day);assert.equal(pillars[3],x.hour);
  const out=inspect({system:source.negativeDayHourSystem,candidateDay:pillars[2],candidateHour:pillars[3]});assert.equal(out.sourceLocalNegativeExampleMatches,true);assert.equal(out.fullBladePatternEstablished,null);
  runtime.push({sourcePair:{day:x.day,hour:x.hour},modernFeasibilityFixture:input,actualHHCPillars:pillars,actualLunarPillars:expected,sourceOriginalYearMonthKnown:false,GregorianBirthDateAttributedToHistoricalPerson:false,sourceOutcomeValidated:false});
 }
 assert.equal(hhcCalls,8);assert.equal(lunarForwardCalls,8);
});
let lookups=0;
await check('180 sixtycycle/dayset queries and16 localnegative comparisons keep membership separate from blanketblade classification',()=>{
 for(const t of source.tables)for(const day of sixty){const x=inspect({system:t.system,candidateDay:day,candidateHour:null});assert.equal(x.listedCoordinateMatches,t.days.includes(day));assert.equal(x.fullBladePatternEstablished,null);assert.equal(x.practicalOutcome,null);lookups++;}
 for(const x of source.negativeDayHourPairs){const a=inspect({system:source.negativeDayHourSystem,candidateDay:x.day,candidateHour:x.hour});assert.equal(a.listedCoordinateMatches,true);
  const hour=sixty[(sixty.indexOf(x.hour)+2)%60],different=inspect({system:source.negativeDayHourSystem,candidateDay:x.day,candidateHour:hour});assert.equal(different.listedCoordinateMatches,false);assert.equal(different.fullBladePatternEstablished,null);lookups+=2;}
 assert.equal(lookups,196);
});
await check('Unknown inputs do not become negative evidence, invalid/aliased coordinates are rejected and returned data cannot mutate source',()=>{
 for(const pair of[{candidateDay:null,candidateHour:'丁卯'},{candidateDay:'甲申',candidateHour:null},{candidateDay:null,candidateHour:null}])assert.equal(inspect({system:source.negativeDayHourSystem,...pair}).listedCoordinateMatches,null);
 const base={system:source.negativeDayHourSystem,candidateDay:'甲申',candidateHour:'丁卯'};
 for(const x of[null,{},[],{...base,candidateDay:undefined},{...base,candidateDay:'甲丑'},{...base,system:'yangren'},{...base,dayPolicy:'midnight'},{...base,[Symbol('x')]:true}])assert.throws(()=>inspect(x),TypeError);
 assert.throws(()=>inspect({system:source.tables[0].system,candidateDay:'戊午',candidateHour:'甲子'}),TypeError);
 const out=inspect(base);out.matchedSourceRows[0].sourcePages.push(999);assert.deepEqual(inspect(base).matchedSourceRows[0].sourcePages,[204]);assert.deepEqual(base,{system:source.negativeDayHourSystem,candidateDay:'甲申',candidateHour:'丁卯'});
});
await check('Fullcontext, source-strength, hiddenstemglyph and historicaloutcome premises remain explicitly incomplete',async()=>{
 const full=await read(resolve(b,'CONTEXT_REVIEW.json'));assert.equal(full.records.length,55);assert.equal(full.normalizedSectionCodepointsIncludingHeader,3467);assert.equal(full.bodyCodepointsExcludingHeader,3452);
 assert.equal(full.records.map(x=>x.text).join(''),await readFile(resolve(b,'NORMALIZED_DIGITAL_BODY.txt'),'utf8'));assert(full.records.every(x=>x.disposition&&x.editorialContextReviewed));
 assert.equal(full.allLogicalConditionsExtracted,false);assert.equal(source.allConditionsCompiled,false);assert.equal(source.sourceOutcomesValidated,false);
});
const out={date:'2026-10-28',status:'staging-coordinate-projection-verified-full-conditional-compiler-open',checks,actualLunarSearchEightCharCalls:lunarSearchCalls,actualLunarForwardEightCharCalls:lunarForwardCalls,actualHHCBaziCalls:hhcCalls,sourceDayHourExamples:8,sourceDaySetEntries:10,privateCoordinateLookups:lookups,runtime,fullBladePatternClassifier:false,strengthMethodValidated:false,sourceChronologyEstablished:false,historicalOutcomesValidated:false,consumerChanged:false};
await writeFile(resolve(q,'COORDINATE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,actualLunarSearchEightCharCalls:lunarSearchCalls,actualLunarForwardEightCharCalls:lunarForwardCalls,actualHHCBaziCalls:hhcCalls,sourceDayHourExamples:8,sourceDaySetEntries:10,privateCoordinateLookups:lookups,fullBladePatternClassifier:false}));
