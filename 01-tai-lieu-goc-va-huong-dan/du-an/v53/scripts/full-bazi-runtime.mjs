import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createRequire} from 'node:module';
import {resolve} from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const root=resolve(import.meta.dirname,'../..'),out=resolve(root,'v53/research/full-study/bazi');
await mkdir(out,{recursive:true});
const reqTs=createRequire(resolve(root,'v46/package.json'));
const reqJs=createRequire(resolve(root,'v47/bazi/package.json'));
const ts=reqTs('lunar-typescript'),js=reqJs('lunar-javascript');
const source=await readFile(resolve(root,'v53/engine.js'),'utf8');
const fragment=source.slice(source.indexOf('const BAZI_JIE_MIN='),source.indexOf('function tvJDN('));
const c={STEMS:['Giáp','Ất','Bính','Đinh','Mậu','Kỷ','Canh','Tân','Nhâm','Quý'],BRANCHES:['Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất','Hợi']};
vm.createContext(c);vm.runInContext('const mod=(a,n)=>((a%n)+n)%n;'+fragment,c);
const GAN='甲乙丙丁戊己庚辛壬癸',ZHI='子丑寅卯辰巳午未申酉戌亥';
const han=p=>GAN[p.s]+ZHI[p.b];
const mod=(a,n)=>(a%n+n)%n;
const cycle=Array.from({length:60},(_,i)=>GAN[i%10]+ZHI[i%12]);
const offset=y=>({year:y.getStartYear(),month:y.getStartMonth(),day:y.getStartDay(),hour:y.getStartHour()});
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function calcOffsetFromMinuteSpan(minutes){
  const year=Math.floor(minutes/4320);minutes-=year*4320;
  const month=Math.floor(minutes/360);minutes-=month*360;
  const day=Math.floor(minutes/12);minutes-=day*12;
  return {year,month,day,hour:minutes*2};
}
function serialize(lib,input,gender,sect){
  const solar=lib.Solar.fromYmdHms(...input),lunar=solar.getLunar(),eight=lunar.getEightChar();
  const yun=eight.getYun(gender,sect),prev=lunar.getPrevJie(),next=lunar.getNextJie();
  const boundary=yun.isForward()?next:prev;
  const span=yun.isForward()?boundary.getSolar().subtractMinute(solar):solar.subtractMinute(boundary.getSolar());
  return {year:eight.getYear(),month:eight.getMonth(),forward:yun.isForward(),offset:offset(yun),startSolar:yun.getStartSolar().toYmdHms(),boundary:{name:boundary.getName(),solar:boundary.getSolar().toYmdHms()},spanMinutes:span,cycles:yun.getDaYun(10).map(d=>({index:d.getIndex(),ganZhi:d.getGanZhi(),startYear:d.getStartYear(),endYear:d.getEndYear(),startAge:d.getStartAge(),endAge:d.getEndAge()})),monthHidden:eight.getMonthHideGan(),monthGods:eight.getMonthShiShenZhi()};
}
const inputs=[];
for(const y of [1900,1926,1950,1984,1988,2000,2024,2025,2026,2100])for(let m=1;m<=12;m++)inputs.push([y,m,15,12,37,0]);
inputs.push([1988,2,15,23,30,0],[2024,2,4,16,26,0],[2024,2,4,16,28,0],[2025,2,3,22,9,0],[2025,2,3,22,11,0],[2000,2,29,0,0,0],[2026,10,26,0,0,0]);
const rows=[];
for(const input of inputs)for(const gender of [0,1])for(const sect of [1,2]){
  const a=serialize(ts,input,gender,sect),b=serialize(js,input,gender,sect);
  assert.ok(same(a,b),`TypeScript and JavaScript mismatch: ${input}/${gender}/${sect}`);
  const expectedForward=(GAN.indexOf(a.year[0])%2===0)===(gender===1);
  assert.equal(a.forward,expectedForward);
  const monthIndex=cycle.indexOf(a.month);
  for(const d of a.cycles){
    assert.equal(d.ganZhi,d.index===0?'':cycle[mod(monthIndex+(a.forward?d.index:-d.index),60)]);
    if(d.index>0){assert.equal(d.endYear-d.startYear,9);assert.equal(d.startAge,d.startYear-input[0]+1);}
  }
  if(sect===2)assert.ok(same(a.offset,calcOffsetFromMinuteSpan(a.spanMinutes)));
  const hhc=c.baziCalcData(...input.slice(0,5),8,'midnight',false);
  const hhcForward=(hhc.all[0].s%2===0)===(gender===1);
  assert.equal(hhcForward,a.forward);
  assert.equal(han(hhc.all[1]),a.month);
  const term=hhcForward?hhc.after:hhc.start;
  const hhcMinutes=Math.abs(term.ts-hhc.utc)/60000;
  const refBoundaryUtc=Date.UTC(...a.boundary.solar.match(/\d+/g).map(Number).map((v,i)=>i===1?v-1:v))-8*3600000;
  rows.push({input,gender,sect,reference:a,crossLanguageEqual:true,hhc:{forward:hhcForward,month:han(hhc.all[1]),spanMinutes:hhcMinutes,offsetMinuteConvention:calcOffsetFromMinuteSpan(hhcMinutes),boundaryUtc:new Date(term.ts).toISOString(),boundaryDifferenceSeconds:(term.ts-refBoundaryUtc)/1000,spanDifferenceMinutes:hhcMinutes-a.spanMinutes}});
}
const examples=rows.filter(r=>r.input[0]===2026&&[1,10].includes(r.input[1])&&r.sect===2);
const unknown=[];
for(const hour of [0,6,12,18,23])for(const gender of [0,1])unknown.push({hour,gender,...serialize(ts,[2026,10,26,hour,0,0],gender,2)});
const maxTerm=Math.max(...rows.map(x=>Math.abs(x.hhc.boundaryDifferenceSeconds)));
const maxMinute=Math.max(...rows.map(x=>Math.abs(x.hhc.spanDifferenceMinutes)));
const versions={typescript:JSON.parse(await readFile(resolve(root,'v46/node_modules/lunar-typescript/package.json'),'utf8')).version,javascript:JSON.parse(await readFile(resolve(root,'v47/bazi/node_modules/lunar-javascript/package.json'),'utf8')).version};
const result={createdUTC:new Date().toISOString(),runtime:process.version,engines:versions,summary:{birthInputs:inputs.length,cases:rows.length,crossLanguageEqual:rows.length,directionChecks:rows.length,monthChecks:rows.length,cycleGanZhiChecks:rows.length*10,sect2MinuteDecompositionChecks:rows.filter(r=>r.sect===2).length,maximumHhcTermDifferenceSeconds:maxTerm,maximumMinuteSpanDifference:maxMinute,hhcMinuteOffsetsDifferFromReference:rows.filter(r=>r.sect===2&&!same(r.hhc.offsetMinuteConvention,r.reference.offset)).length},conventions:{timezone:'All comparisons use civil UTC+8, matching the library Jie tables. No claim that Solar API has arbitrary timezone support.',sect2MinuteSpan:'Library subtractMinute ignores seconds at both endpoints; HHC Jie table rounds its astronomical timestamp to the nearest minute. One minute in this convention maps to two onset hours.',daYun:'Index0 is pre-first-luck period with empty GanZhi. Indices1..9 form actual 10-year luck cycles. Calendar year/age labels are not exact anniversary boundaries.',unknownBirthHour:'Samples demonstrate variation; must present a range/ask time rather than use fabricated noon. These 5 hour samples are illustrative and are not a full-day extrema proof.'},examples,unknownBirthHourSamples:unknown,rows};
await writeFile(resolve(out,'RUNTIME_COMPARISON.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result.summary,null,2));
console.log(JSON.stringify({examples:examples.map(r=>({input:r.input,gender:r.gender,reference:r.reference,hhc:r.hhc}))},null,2));
