import{readFile,writeFile,mkdir}from'node:fs/promises';
import{resolve}from'node:path';
import{createRequire}from'node:module';
import{createHash}from'node:crypto';
import vm from'node:vm';
import assert from'node:assert/strict';
const root=resolve(import.meta.dirname,'..'),out=resolve(root,'qa/four-items'),c={};c.window=c;vm.createContext(c);
for(const f of ['engine.js','content.js','fortune.js'])vm.runInContext(await readFile(resolve(root,f),'utf8'),c,{filename:f});
const E=c.HHC_ENGINE,F=c.HHC_FORTUNE,req=createRequire(resolve(root,'../v46/package.json')),iztro=req('iztro'),mod=(n,k)=>(n%k+k)%k,cn=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥'];
const checks=[],check=(name,ok)=>{checks.push({name,ok});assert.ok(ok,name);console.log('PASS',name)},iso=s=>`${s.y}-${String(s.m).padStart(2,'0')}-${String(s.d).padStart(2,'0')}`,nativeMonth=l=>l.m+(l.leap&&l.d>=16?1:0),chosenMonth=(l,p)=>l.m+(l.leap&&(p==='next'||p==='split16'&&l.d>=16)?1:0);
iztro.astro.resetConfig();iztro.astro.config({yearDivide:'normal',horoscopeDivide:'normal',ageDivide:'normal',dayDivide:'current',algorithm:'default'});
const rows=[];
for(const gender of ['male','female'])for(const day of [15,16,29])for(const policy of ['same','next','split16']){
 const birth={y:2004,m:2,d:day,calendar:'lunar',leap:true,hour:8,minute:30,tz:8,gender,dayPolicy:'current',leapPolicy:policy},chart=E.tuvi(birth),ext=iztro.astro.bySolar(iso(chart.originalSolar),4,gender==='male'?'男':'女',true,'zh-CN');
 for(const target of [{y:2025,m:6,d:14,leap:true},{y:2025,m:6,d:15,leap:true},{y:2025,m:6,d:16,leap:true},{y:2026,m:1,d:1,leap:false}]){
  const date=iso(E.lunarToSolar(target.d,target.m,target.y,target.leap,8)),a=F.inspect(chart,date),x=ext.horoscope(date,0),raw=cn.indexOf(ext.palaces[x.monthly.index].earthlyBranch),birthAdjustment=nativeMonth(chart.lunar)-chosenMonth(chart.lunar,policy),targetAdjustment=chosenMonth(target,policy)-nativeMonth(target),expected=mod(raw+birthAdjustment+targetAdjustment,12);
  rows.push({birth,target,date,policy,rawMonth:raw,birthAdjustment,targetAdjustment,expected,actual:a.monthly.idx,age:a.age,engineAge:x.age.nominalAge,ok:a.monthly.idx===expected&&a.age===x.age.nominalAge});
 }
}
check('72 actual iztro calls cover leap birth days 15/16/29, target days 14/15/16, both genders and all three explicit policies',rows.length===72&&rows.every(x=>x.ok));
check('All 24 split16 cases agree directly, with zero policy adjustment',rows.filter(x=>x.policy==='split16').length===24&&rows.filter(x=>x.policy==='split16').every(x=>x.rawMonth===x.actual&&x.birthAdjustment===0&&x.targetAdjustment===0));
check('All three policies wrap a leap twelfth month to a valid 1–12 month without changing its lunar year',F.effective({m:12,d:16,leap:true},'same')===12&&F.effective({m:12,d:16,leap:true},'next')===1&&F.effective({m:12,d:16,leap:true},'split16')===1);
const minorRows=[];
for(let y=1990;y<=2001;y++)for(const gender of ['male','female']){
 const b={y,m:5,d:20,hour:8,minute:30,tz:8,gender,leapPolicy:'same',dayPolicy:'current'},chart=E.tuvi(b),a=F.inspect(chart,'2040-06-01'),ext=iztro.astro.bySolar(`${y}-5-20`,4,gender==='male'?'男':'女',false,'zh-CN'),x=ext.horoscope('2040-6-1',0),expected=cn.indexOf(ext.palaces[x.age.index].earthlyBranch);
 minorRows.push({birth:b,birthBranch:chart.branch,age:a.age,expected,actual:a.minor.idx,ok:a.minor.idx===expected});
}
check('24 actual iztro calls independently confirm minor-period direction for all 12 birth branches and both genders',minorRows.length===24&&minorRows.every(x=>x.ok));
const names={'廉贞':'Liêm Trinh','破军':'Phá Quân','武曲':'Vũ Khúc','太阳':'Thái Dương','天机':'Thiên Cơ','天梁':'Thiên Lương','紫微':'Tử Vi','太阴':'Thái Âm','天同':'Thiên Đồng','文昌':'Văn Xương','巨门':'Cự Môn','贪狼':'Tham Lang','右弼':'Hữu Bật','文曲':'Văn Khúc','左辅':'Tả Phù','天府':'Thiên Phủ'};
const chart=E.tuvi({y:1990,m:5,d:20,hour:8,minute:30,tz:8,gender:'male',leapPolicy:'same',dayPolicy:'current'}),ext=iztro.astro.bySolar('1990-5-20',4,'男',false,'zh-CN'),hua=[];
for(let y=2020;y<=2029;y++){
 const a=F.inspect(chart,`${y}-06-01`),x=ext.horoscope(`${y}-6-1`,0),expected=x.yearly.mutagen.map(s=>names[s]);assert.ok(expected.every(Boolean),'All actual external star names explicitly translated');
 const got=a.transformations.map(t=>t.name),differences=got.flatMap((n,i)=>n===expected[i]?[]:[{position:i,hhc:n,iztro:expected[i]}]);
 hua.push({year:y,yearName:a.yearName,actual:got,iztro:expected,differences});
}
check('Annual four-transformations comparison records exactly the known Nham Khoa variant instead of forcing agreement',hua.filter(x=>x.differences.length).length===1&&hua.find(x=>x.differences.length).year===2022&&hua.find(x=>x.differences.length).differences.length===1&&hua.find(x=>x.differences.length).differences[0].hhc==='Thiên Phủ'&&hua.find(x=>x.differences.length).differences[0].iztro==='Tả Phù');
const source=await readFile(resolve(root,'../v47/tuvi/sources/quanshu-juan2.html'),'utf8');
check('Retained source explicitly attests Nham Thien Phu and the four minor-period starting branches',source.includes('壬梁紫府武宿是')&&source.includes('寅午戌人起辰宮，申子辰人自戌宮，巳酉醜人起未宮，亥卯未人起丑宮'));
const rolled=E.tuvi({y:1991,m:2,d:14,hour:23,minute:30,tz:8,gender:'male',dayPolicy:'calendar-next',leapPolicy:'same'}),midnight=E.tuvi({y:1991,m:2,d:15,hour:0,minute:0,tz:8,gender:'male',dayPolicy:'current',leapPolicy:'same'}),a=F.inspect(rolled,'2026-02-17'),b=F.inspect(midnight,'2026-02-17');
check('Late-Ty next-day selection propagates its effective lunar birth year/month/hour into all period indices',JSON.stringify([a.age,a.decade?.idx,a.yearly.idx,a.monthly.idx,a.minor.idx])===JSON.stringify([b.age,b.decade?.idx,b.yearly.idx,b.monthly.idx,b.minor.idx]));
await mkdir(out,{recursive:true});await writeFile(resolve(out,'fortune-policy-tests.json'),JSON.stringify({date:new Date().toISOString(),checks,actualIztroCalls:rows.length+minorRows.length+hua.length,leapPolicyRows:rows,minorRows,annualTransformations:hua,source:{file:'v47/tuvi/sources/quanshu-juan2.html',sha256:createHash('sha256').update(Buffer.from(source)).digest('hex')},scope:'Policy-normalized index comparison. Split16 compares raw output; same/next corrections are logged. Nham Khoa is an explicit retained textual variant. No claim of predictive validity or complete facsimile collation.'},null,2)+'\n');
console.log(`${checks.length}/${checks.length} policy checks passed`);
