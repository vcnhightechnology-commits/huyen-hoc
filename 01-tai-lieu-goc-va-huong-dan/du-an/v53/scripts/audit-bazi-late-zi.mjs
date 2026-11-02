import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const root=resolve(import.meta.dirname,'..'), workspace=resolve(root,'..'), out=resolve(root,'research/bazi-late-zi');
await mkdir(out,{recursive:true});
const req=createRequire(import.meta.url), L=req(resolve(workspace,'v46/node_modules/lunar-typescript'));
const sha=b=>createHash('sha256').update(b).digest('hex'), checks=[];
const test=(name,ok)=>{checks.push({name,ok});assert.ok(ok,name);console.log('PASS',name)};
const old=JSON.parse(await readFile(resolve(workspace,'archives/v53-before-bazi-relation-locations/PACKAGE_MANIFEST.json'),'utf8'));
const retainedAudit=JSON.parse(await readFile(resolve(root,'research/full-study/bazi/SOURCE_MANIFEST.json'),'utf8'));
const sources=[];
for(const [file,evidence] of [
 ['research/four-items/sources/KR3g0042_002.txt','Pinned digital WYG transcription, no new image collation'],
 ['research/full-study/bazi/sources/6tail-lunar-bazi.html','Retained official software documentation, software convention only'],
 ['research/full-study/bazi/sources/EightCharTest.ts','Retained upstream test source pinned in the earlier source manifest']
]){
 const b=await readFile(resolve(root,file)), before=old.files.find(f=>f.file===file);assert.ok(before,file);assert.equal(sha(b),before.sha256);
 sources.push({file,bytes:b.length,sha256:sha(b),evidence,reusedWithoutDownload:true});
}
test('Three reused source files retain their pre-scope bytes',sources.length===3);
const text=await readFile(resolve(root,sources[0].file),'utf8');
const page=(mark)=>{const a=text.indexOf(`<pb:KR3g0042_WYG_${mark}>`);assert.ok(a>=0);return text.slice(a,text.indexOf('<pb:',a+1)).replace(/¶|\s/g,'')};
test('Exact WYG page43b distinguishes the two halves of Zi around midnight',page('002-43b').includes('若子時則上半時在夜半前屬昨日下半時在夜半後屬今日'));
test('WYG57b/58a contains the five day-stem groups used to start Zi hour',page('002-57b').includes('甲巳還加甲乙庚丙作初丙辛從戊起')&&page('002-58a').includes('丁壬庚子居戊癸何方發壬子是直途'));
const doc=await readFile(resolve(root,sources[1].file),'utf8');
test('Official documentation explicitly assigns late-Zi time pillar to tomorrow for both sects',doc.includes('两种流派都认为晚子时时柱算明天'));
const upstream=await readFile(resolve(root,sources[2].file),'utf8');
test('Retained upstream tests explicitly show different day pillars but the same WuZi hour',upstream.includes("eightChar.getDay(), '庚子'")&&upstream.includes("eightChar.getDay(), '辛丑'")&&upstream.includes("eightChar.getTime(), '戊子'"));
const runtimeFiles=['v46/node_modules/lunar-typescript/package.json','v46/node_modules/lunar-typescript/dist/index.cjs'],runtime=[];
for(const file of runtimeFiles){const b=await readFile(resolve(workspace,file)),previous=retainedAudit.local.find(f=>f.file===file);assert.ok(previous,file);assert.equal(sha(b),previous.sha256);runtime.push({file,bytes:b.length,sha256:sha(b)})}
const runtimeText=await readFile(resolve(workspace,runtimeFiles[1]),'utf8');
test('Actual runtime identity and its time-stem dependence on dayGanIndexExact are verified',JSON.parse(await readFile(resolve(workspace,runtimeFiles[0]),'utf8')).version==='1.8.6'&&runtimeText.includes('o.timeGanIndex = (o.dayGanIndexExact % 5 * 2 + timeZhiIndex) % 10;'));
const c={};c.window=c;vm.createContext(c);const engine=await readFile(resolve(root,'engine.js'));vm.runInContext(engine.toString(),c);assert.equal(sha(engine),old.files.find(f=>f.file==='engine.js').sha256);
const dates=Array.from({length:60},(_,i)=>new Date(Date.UTC(2018,7,9+i)));dates.push(new Date(Date.UTC(2019,11,31)),new Date(Date.UTC(2020,1,29)));
const times=[[0,0],[0,59],[1,0],[22,59],...Array.from({length:60},(_,m)=>[23,m])], rows=[], dayStems=new Set(),variants={midnight:{matches:0,differences:0},zi:{matches:0,differences:0}};
for(const d of dates)for(const[hour,minute]of times){
 const input={y:d.getUTCFullYear(),m:d.getUTCMonth()+1,d:d.getUTCDate(),hour,minute,tz:8,gender:'male',noTime:false},e=L.Solar.fromYmdHms(input.y,input.m,input.d,hour,minute,0).getLunar().getEightChar();
 for(const[policy,sect]of [['midnight',2],['zi',1]]){
  e.setSect(sect);const actual=c.HHC_ENGINE.bazi({...input,dayPolicy:policy}).pillars.map(p=>p.han),reference=['Year','Month','Day','Time'].map(k=>e['get'+k]());
  assert.equal(JSON.stringify(actual.slice(0,3)),JSON.stringify(reference.slice(0,3)));const match=actual[3]===reference[3];assert.equal(match,!(hour===23&&policy==='midnight'));
  if(!match){const stems='甲乙丙丁戊己庚辛壬癸',a=stems.indexOf(actual[3][0]),b=stems.indexOf(reference[3][0]);assert.equal((b-a+10)%10,2);assert.equal(actual[3][1],'子');assert.equal(reference[3][1],'子');dayStems.add(actual[2][0])}
  variants[policy][match?'matches':'differences']++;rows.push({input:{...input,dayPolicy:policy},sect,hhc:actual,reference,match});
 }
}
test('All7936 real chart comparisons agree on year/month/day and differ only at23h under midnight policy',rows.length===7936&&variants.midnight.differences===3720&&variants.zi.differences===0);
test('Every minute23:00–23:59 is covered across all ten day stems, with fixed plus-two reference time-stem offset',dayStems.size===10&&rows.filter(r=>!r.match).length===3720);
const sample=L.Solar.fromYmdHms(1988,2,15,23,30,0).getLunar().getEightChar(),upstreamActual=[];
for(const sect of [2,1]){sample.setSect(sect);upstreamActual.push({sect,day:sample.getDay(),time:sample.getTime()})}
test('Actual installed runtime reproduces both retained upstream late-Zi test expectations',upstreamActual[0].day==='庚子'&&upstreamActual[1].day==='辛丑'&&upstreamActual.every(x=>x.time==='戊子'));
const result={schema:'hhc.bazi.late-zi.audit.v1',date:'2026-10-26',checks,scope:{dates:dates.length,timesPerDate:times.length,realSolarConstructions:dates.length*times.length,realChartComparisons:rows.length,timezone:8,policies:['midnight','zi'],lateZiMinutesPerDate:60,dayStemCoverage:dayStems.size},variants,upstreamActual,sources,runtime,engineSHA256:sha(engine),newDownloads:0,rows,conclusion:'Documented software-policy difference, not a forced match or calendar-independent proof. WYG day-half and ordinary hour-stem clauses do not directly settle a late-Zi hour-stem exception. No product calculation changed.'};
await writeFile(resolve(out,'VERIFICATION.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,scope:result.scope,variants}));
