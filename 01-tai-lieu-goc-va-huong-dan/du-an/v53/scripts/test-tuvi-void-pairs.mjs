import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createRequire}from'node:module';import{createHash}from'node:crypto';import{gunzipSync}from'node:zlib';import vm from'node:vm';import assert from'node:assert/strict';
import{sourceYearVoid as inspect}from'../research/tuvi-void-child/void-reference.mjs';
const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/tuvi-void-child'),q=resolve(r,'qa/tuvi-void-child'),req=createRequire(import.meta.url),iztro=req(resolve(w,'v46/node_modules/iztro')),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const tables=await read(resolve(b,'SOURCE_TABLES.json')),manifest=await read(resolve(b,'VOID_SOURCE_MANIFEST.json')),stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'],sixty=Array.from({length:60},(_,i)=>stems[i%10]+branches[i%12]);
const ctx=(system,sourceYearPillar,candidateBranch=null,orthographyPolicy='contextual-branch')=>({system,scope:'birth-year',sourceYearPillar,candidateBranch,orthographyPolicy}),jielu=tables.systems[0].system,xun=tables.systems[1].system;
const runtimeIdentity=[];
await check('Retained source image/manifest, engine and actual iztro2.6.2 code agree with recorded bytes and the preserved npm tarball',async()=>{
 assert.equal(sha(await readFile(resolve(w,manifest.retainedImage))),manifest.retainedImageSHA256);assert.equal(sha(await readFile(resolve(w,manifest.retainedManifest))),manifest.retainedManifestSHA256);
 const old=await read(resolve(r,'research/tuvi-masters/SOURCE_MANIFEST.json')),tgz=await readFile(resolve(w,old.runtimeTarball));assert.equal(sha(tgz),old.runtimeTarballSHA256);
 for(const x of old.runtime)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 const targets=['lib/star/location.js','lib/star/adjectiveStar.js','lib/i18n/locales/zh-CN/star.js','lib/data/constants.js','lib/utils/index.js'];
 const tar=gunzipSync(tgz),entries=new Map();
 for(let offset=0;offset+512<=tar.length;){const h=tar.subarray(offset,offset+512),name=h.subarray(0,100).toString().replace(/\0.*$/s,''),size=parseInt(h.subarray(124,136).toString().replace(/\0.*$/s,'').trim()||'0',8);if(!name)break;assert(Number.isFinite(size)&&size>=0);if(targets.some(x=>'package/'+x===name))entries.set(name,tar.subarray(offset+512,offset+512+size));offset+=512+Math.ceil(size/512)*512;}
 for(const file of targets){const local=await readFile(resolve(w,'v46/node_modules/iztro',file)),archived=entries.get('package/'+file);assert(archived);assert.deepEqual(local,archived);runtimeIdentity.push({file:'v46/node_modules/iztro/'+file,bytes:local.length,sha256:sha(local),byteIdenticalToRetainedTarball:true});}
 assert.equal(req(resolve(w,'v46/node_modules/iztro/package.json')).version,'2.6.2');
});
await check('Five stem groups and six decadeheads retain22 working branch coordinates under explicitly declared birth-year scope and Si orthography',()=>{
 assert.deepEqual(tables.systems[0].rows.map(x=>[x.sourceStemGroup,x.canonicalWorkingBranches.join('')]),[['甲己','申酉'],['乙庚','午未'],['丙辛','辰巳'],['丁壬','寅卯'],['戊癸','子丑']]);
 assert.deepEqual(tables.systems[1].rows.map(x=>[x.sourceCycleHead,x.canonicalWorkingBranches.join('')]),[['甲子','戌亥'],['甲戌','申酉'],['甲申','午未'],['甲午','辰巳'],['甲辰','寅卯'],['甲寅','子丑']]);
 assert.equal(tables.canonicalWorkingBranchCoordinates,22);assert.equal(tables.siNormalizationOccurrences,2);assert(tables.sourceScopeExplicitlyBirthYear);assert(!tables.singleSoftwareStarSelectorAttestedInSource);
});
let queries=0,unresolvedQueries=0,unknownSiMemberships=0;
await check('1440 source-year/branch queries cover both tables and264 unresolved-Si queries preserve unknown rather than silently normalizing',()=>{
 for(let i=0;i<60;i++)for(const system of[jielu,xun])for(const branch of branches){
  const out=inspect(ctx(system,sixty[i],branch));assert.equal(out.selectedBranches.length,2);assert.equal(out.branchMembership,out.selectedBranches.includes(branch));assert.equal(out.sourceYearBoundaryAdapter,null);assert.equal(out.practicalOutcome,null);queries++;
  if(out.contextualSiNormalization){const unknown=inspect(ctx(system,sixty[i],branch,'leave-unresolved'));assert.deepEqual(unknown.selectedBranches,['辰',null]);assert.equal(unknown.branchMembership,branch==='辰'?true:null);unresolvedQueries++;if(unknown.branchMembership===null)unknownSiMemberships++;}
 }
 assert.equal(queries,1440);assert.equal(unresolvedQueries,264);assert.equal(unknownSiMemberships,242);
});
const c={};c.window=c;vm.createContext(c);const code=await readFile(resolve(r,'engine.js'));assert.equal(sha(code),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');vm.runInContext(code.toString(),c);
function starBranches(chart,name){return chart.palaces.flatMap(p=>[...(p.majorStars??[]),...(p.minorStars??[]),...(p.adjectiveStars??[])].filter(s=>s.name===name).map(()=>p.earthlyBranch));}
let hhcCalls=0,defaultCalls=0,zhongzhouCalls=0;const runtime=[];
await check('60 actual HHC natal charts and120 actual iztro natal calls compare full pairs against default two-star and Zhongzhou single-star representations',()=>{
 try{for(let i=0;i<60;i++){
  const input={y:1924+i,m:1,d:15,calendar:'lunar',leap:false,leapPolicy:'same',dayPolicy:'current',tz:8,hour:12,minute:0,gender:i%2?'female':'male'};
  const chart=c.HHC_ENGINE.tuvi(input);hhcCalls++;const sourceYear=stems[chart.stem]+branches[chart.branch];assert.equal(sourceYear,sixty[i]);
  const cut=inspect(ctx(jielu,sourceYear)).selectedBranches,empty=inspect(ctx(xun,sourceYear)).selectedBranches;
  assert.deepEqual(Array.from(chart.triet,n=>branches[n]),cut);assert.deepEqual(Array.from(chart.tuan,n=>branches[n]),empty);
  const solar=`${chart.originalSolar.y}-${String(chart.originalSolar.m).padStart(2,'0')}-${String(chart.originalSolar.d).padStart(2,'0')}`,gender=input.gender==='male'?'男':'女';
  iztro.astro.resetConfig();iztro.astro.config({algorithm:'default',yearDivide:'normal',horoscopeDivide:'normal',ageDivide:'normal',dayDivide:'current'});
  const def=iztro.astro.bySolar(solar,6,gender,false,'zh-CN');defaultCalls++;const d={jielu:starBranches(def,'截路'),kongwang:starBranches(def,'空亡'),xunkong:starBranches(def,'旬空'),jiekong:starBranches(def,'截空')};
  assert.deepEqual(d.jielu,[cut[0]]);assert.deepEqual(d.kongwang,[cut[1]]);assert.deepEqual(d.xunkong,[empty[i%2]]);assert.deepEqual(d.jiekong,[]);
  iztro.astro.resetConfig();iztro.astro.config({algorithm:'zhongzhou',yearDivide:'normal',horoscopeDivide:'normal',ageDivide:'normal',dayDivide:'current'});
  const zz=iztro.astro.bySolar(solar,6,gender,false,'zh-CN');zhongzhouCalls++;const z={jielu:starBranches(zz,'截路'),kongwang:starBranches(zz,'空亡'),xunkong:starBranches(zz,'旬空'),jiekong:starBranches(zz,'截空')};
  assert.deepEqual(z.jielu,[]);assert.deepEqual(z.kongwang,[]);assert.deepEqual(z.jiekong,[cut[i%2]]);assert.deepEqual(z.xunkong,d.xunkong);
  runtime.push({input,solar,sourceYear,fixtureYearBoundaryPolicy:'normal-lunar-year-selection;not proven a universal classical calendar adapter',sourceJieluPair:cut,sourceXunzhongPair:empty,hhcTrietPair:Array.from(chart.triet,n=>branches[n]),hhcTuanPair:Array.from(chart.tuan,n=>branches[n]),iztroDefault:d,iztroZhongzhou:z,sourceSingleStarParitySelectorAttested:false});
 }}finally{iztro.astro.resetConfig();}
 assert.equal(hhcCalls,60);assert.equal(defaultCalls,60);assert.equal(zhongzhouCalls,60);assert.equal(runtime.length,60);
});
await check('Pair-versus-star differences are representation conventions, not source confirmation of a parity selector or performance/outcome difference',()=>{
 assert.equal(runtime.filter(x=>x.iztroDefault.xunkong[0]===x.sourceXunzhongPair[0]).length,30);
 assert.equal(runtime.filter(x=>x.iztroDefault.xunkong[0]===x.sourceXunzhongPair[1]).length,30);
 assert.equal(runtime.filter(x=>x.iztroZhongzhou.jiekong[0]===x.sourceJieluPair[0]).length,30);
 assert.equal(runtime.filter(x=>x.iztroZhongzhou.jiekong[0]===x.sourceJieluPair[1]).length,30);
 assert(runtime.every(x=>!x.sourceSingleStarParitySelectorAttested));
});
await check('Unknown year/branch stays unknown, source day/month substitution and silent aliases are rejected, returned pairs do not mutate source',()=>{
 for(const system of[jielu,xun]){const u=inspect(ctx(system,null,'子'));assert.equal(u.selectedBranches,null);assert.equal(u.branchMembership,null);assert.equal(inspect(ctx(system,'甲子')).branchMembership,null);}
 const base=ctx(jielu,'甲子','申');
 for(const bad of[null,{},[],{...base,sourceYearPillar:undefined},{...base,sourceYearPillar:'甲丑'},{...base,candidateBranch:'己'},{...base,candidateBranch:'Tý'},{...base,scope:'day'},{...base,orthographyPolicy:undefined},{...base,year:1924},{...base,[Symbol('x')]:true}])assert.throws(()=>inspect(bad),TypeError);
 const out=inspect(base);out.selectedBranches.push('fake');out.canonicalWorkingBranches.length=0;assert.deepEqual(inspect(base).selectedBranches,['申','酉']);assert.equal(inspect(base).practicalOutcome,null);
});
await check('Released HTML, engine and first-major-period convention remain byte-identical to the verified3521-file package',async()=>{
 const m=await read(resolve(w,'archives/v53-before-tuvi-void-child/PACKAGE_MANIFEST.json'));assert.equal(m.files.length,3521);
 for(const name of['engine.js','fortune.js','fortune-months.js','Huyen_Hoc_Cac.html','site/index.html'])assert.equal(sha(await readFile(resolve(r,name))),m.files.find(x=>x.file===name).sha256);
 assert.equal(sha(await readFile(resolve(w,'Huyen_Hoc_Cac.html'))),m.product.sha256);
});
const out={date:'2026-10-28',status:'staged-two-birthyear-void-pair-tables-and-runtime-representation-contrasts-verified',checks,summary:{sourceJieluStemGroups:5,sourceXunzhongCycleGroups:6,canonicalWorkingBranchCoordinates:22,explicitSiNormalizationOccurrences:2,
 privateSourceYearBranchQueries:queries,unresolvedSiQueries:unresolvedQueries,unresolvedSiMemberships:unknownSiMemberships,actualHHCTuviCalls:hhcCalls,actualIztroDefaultNatalCalls:defaultCalls,actualIztroZhongzhouNatalCalls:zhongzhouCalls,actualNatalContexts:60,
 expandedPriorReadSourcePositions:1,nativeQACrops:1,newHTTPRequests:0,newOriginalContainers:0,newSourcePositions:0},runtimeIdentity,runtime,
 originalJP2Acquired:false,sourceSingleStarParitySelectorAttested:false,sourceYearBoundaryAdapterEstablished:false,practicalOutcomesValidated:false,consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'VOID_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
