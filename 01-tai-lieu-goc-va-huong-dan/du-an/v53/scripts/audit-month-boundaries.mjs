import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';
const root=resolve(import.meta.dirname,'..'),out=resolve(root,'research/month-boundaries');await mkdir(out,{recursive:true});const hash=b=>createHash('sha256').update(b).digest('hex'),c={};c.window=c;vm.createContext(c);for(const f of ['engine.js','content.js','fortune.js','fortune-months.js'])vm.runInContext(await readFile(resolve(root,f),'utf8'),c,{filename:f});const E=c.HHC_ENGINE,M=c.HHC_FORTUNE_MONTHS;
const bytes=await readFile(resolve(root,'../v46/data/hko_month_starts.json')),starts=JSON.parse(bytes),stamp=s=>Date.parse(s+'T00:00:00Z'),iso=s=>`${s.y}-${String(s.m).padStart(2,'0')}-${String(s.d).padStart(2,'0')}`,rows=[],years=[],chart=E.tuvi({y:1900,m:1,d:1,hour:8,minute:30,tz:8,gender:'male',leapPolicy:'same',dayPolicy:'current'});
for(let year=1901;year<=2100;year++){
 const got=M.inspect(chart,`${year}-06-01`);years.push({year,overviewYear:got.year,rowCount:got.rows.length});
 for(let i=0;i<starts.length-1;i++){
  const h=starts[i];if(h.y!==year)continue;const expectedFirst=h.date,expectedLast=new Date(stamp(starts[i+1].date)-86400000).toISOString().slice(0,10),r=got.rows.find(r=>r.month===h.m&&r.leap===h.leap),first=r?.first?iso(r.first):null,last=r?.last?iso(r.last):null;
  rows.push({year,month:h.m,leap:h.leap,expectedFirst,expectedLast,actualFirst:first,actualLast:last,present:!!r,available:r?.available??false,reason:r?.reason??null,matches:first===expectedFirst&&last===expectedLast});
 }
}
const differences=rows.filter(r=>!r.matches),unguarded=differences.filter(r=>r.available),missing=rows.filter(r=>!r.present),summary={years:years.length,intervals:rows.length,matching:rows.filter(r=>r.matches).length,differences:differences.length,unguarded:unguarded.length,missing:missing.length};
const result={date:new Date().toISOString(),input:{file:'v46/data/hko_month_starts.json',sha256:hash(bytes),scope:'Previously parsed official original TXT archive; lunar year/leap are derived from ordered month labels, not explicit per-row fields. No new source download or gap filling. UTC+8 only.'},summary,unguarded,missing,differences,years,rows};
const name=process.argv.includes('--after')?'after.json':'before.json';await writeFile(resolve(out,name),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({summary,unguarded,missing},null,2));
