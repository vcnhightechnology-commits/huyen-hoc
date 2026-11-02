import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createRequire}from'node:module';import{createHash}from'node:crypto';import{gunzipSync}from'node:zlib';import vm from'node:vm';import assert from'node:assert/strict';
import{childPrintedOrdinal as inspect}from'../research/tuvi-void-child/ordinal-reference.mjs';
const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/tuvi-void-child'),q=resolve(r,'qa/tuvi-void-child'),req=createRequire(import.meta.url),iztro=req(resolve(w,'v46/node_modules/iztro')),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
const source=await read(resolve(b,'SOURCE_ORDINALS.json')),manifest=await read(resolve(b,'CHILD_SOURCE_MANIFEST.json')),system=source.system;
async function check(name,fn){await fn();checks.push({name,ok:true});}
const runtimeIdentity=[];
await check('Retained source and real iztro package identities match; higher-resolution403 body is retained as rate-limit evidence,not as an image',async()=>{
 assert.equal(sha(await readFile(resolve(w,source.sourceFile))),source.sourceSHA256);
 const response=manifest.newHigherResolutionRequest,body=await readFile(resolve(b,response.file));assert.equal(response.status,403);assert.equal(body.length,608);assert.equal(sha(body),response.sha256);assert(response.tls.authorized);assert.equal(response.actuallyViewed,false);
 const old=await read(resolve(r,'research/tuvi-masters/SOURCE_MANIFEST.json')),raw=await readFile(resolve(w,old.runtimeTarball));assert.equal(sha(raw),old.runtimeTarballSHA256);
 for(const x of old.runtime)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 const tar=gunzipSync(raw),target='package/lib/i18n/locales/zh-CN/palace.js';let found=null;
 for(let offset=0;offset+512<=tar.length;){const head=tar.subarray(offset,offset+512),name=head.subarray(0,100).toString().replace(/\0.*$/s,''),size=parseInt(head.subarray(124,136).toString().replace(/\0.*$/s,'').trim()||'0',8);if(!name)break;assert(Number.isFinite(size)&&size>=0);if(name===target){found=tar.subarray(offset+512,offset+512+size);break}offset+=512+Math.ceil(size/512)*512;}
 assert(found);const local=await readFile(resolve(w,'v46/node_modules/iztro/lib/i18n/locales/zh-CN/palace.js'));assert.deepEqual(local,found);runtimeIdentity.push({file:'v46/node_modules/iztro/lib/i18n/locales/zh-CN/palace.js',sha256:sha(local),bytes:local.length,byteIdenticalToRetainedPackage:true});
 assert.equal(req(resolve(w,'v46/node_modules/iztro/package.json')).version,'2.6.2');
});
await check('Six literal printed ordinal/palace labels are complete as a bounded subset; chart aliases are explicit modern normalization and tail/age semantics remain unresolved',()=>{
 assert.deepEqual(source.rows.map(x=>[x.printedOrdinal,x.sourcePalaceLiteral]),[[1,'命'],[2,'財'],[3,'疾厄'],[4,'妻'],[5,'福'],[6,'官祿']]);
 assert.equal(source.rows.length,6);assert.equal(source.numericMarkersAreModernAgeCalendarAdapter,false);assert.equal(source.sourceAgeCountingConventionResolved,false);assert.equal(source.firstMajorPeriodStartResolved,false);
 for(let n=1;n<=6;n++){const x=inspect({system,printedOrdinal:n});assert.equal(x.sourcePalaceLiteral,source.rows[n-1].sourcePalaceLiteral);assert.equal(x.aliasesAreVerbatimFullSourceLabels,false);assert.equal(x.GregorianAgeAdapter,null);assert.equal(x.firstMajorPeriodAge,null);assert.equal(x.firstMajorPeriodPalace,null);}
});
const c={};c.window=c;vm.createContext(c);const engine=await readFile(resolve(r,'engine.js'));assert.equal(sha(engine),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');vm.runInContext(engine.toString(),c);
let hhcCalls=0,iztroCalls=0,lookups=0;const runtime=[],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
await check('12 actual HHC and12 actual iztro natal charts bind72 numeric-palace alias projections to matching physical branches without using current age or changing period starts',()=>{
 try{for(let hourBranch=0;hourBranch<12;hourBranch++){
  const input={y:2024,m:4,d:15,calendar:'lunar',leap:false,leapPolicy:'same',dayPolicy:'current',tz:8,hour:hourBranch*2,minute:0,gender:hourBranch%2?'female':'male'};
  const chart=c.HHC_ENGINE.tuvi(input);hhcCalls++;const solar=`${chart.originalSolar.y}-${String(chart.originalSolar.m).padStart(2,'0')}-${String(chart.originalSolar.d).padStart(2,'0')}`;
  iztro.astro.resetConfig();iztro.astro.config({yearDivide:'normal',horoscopeDivide:'normal',ageDivide:'normal',dayDivide:'current',algorithm:'default'});
  const other=iztro.astro.bySolar(solar,hourBranch,input.gender==='male'?'男':'女',false,'zh-CN');iztroCalls++;
  const projected=[];
  for(let ordinal=1;ordinal<=6;ordinal++){const out=inspect({system,printedOrdinal:ordinal}),a=chart.palaces.filter(x=>x.name===out.modernChartAliasProjection.hhc),z=other.palaces.filter(x=>x.name===out.modernChartAliasProjection.iztro);
   assert.equal(a.length,1);assert.equal(z.length,1);assert.equal(branches[a[0].idx],z[0].earthlyBranch);assert.equal(out.GregorianAgeAdapter,null);assert.equal(out.practicalOutcome,null);lookups++;
   projected.push({printedOrdinal:ordinal,sourceLabel:out.sourcePalaceLiteral,modernHHCHouse:a[0].name,modernIztroHouse:z[0].name,physicalBranch:branches[a[0].idx],sourceAgeMeaningResolved:false});
  }
  runtime.push({input,solar,projections:projected,majorPeriodStartChanged:false});
 }}finally{iztro.astro.resetConfig();}
 assert.equal(hhcCalls,12);assert.equal(iztroCalls,12);assert.equal(lookups,72);
 for(const row of source.rows)assert.equal(new Set(runtime.flatMap(x=>x.projections.filter(p=>p.printedOrdinal===row.printedOrdinal).map(p=>p.physicalBranch))).size,12);
});
await check('Unknown ordinal stays unknown; no extrapolation to7/15 or Gregorian/nominal-age adapter, and returned aliases cannot mutate source',()=>{
 const u=inspect({system,printedOrdinal:null});assert.equal(u.sourceCoordinateKnown,null);assert.equal(u.sourcePalaceLiteral,null);assert.equal(u.modernChartAliasProjection,null);
 for(const x of[null,{},[],{system,printedOrdinal:undefined},{system,printedOrdinal:0},{system,printedOrdinal:7},{system,printedOrdinal:15},{system,printedOrdinal:'1'},{system,printedOrdinal:1,year:2026},{system:'child-age',printedOrdinal:1},{system,printedOrdinal:1,[Symbol('x')]:true}])assert.throws(()=>inspect(x),TypeError);
 const x=inspect({system,printedOrdinal:4});x.modernChartAliasProjection.hhc='fake';assert.equal(inspect({system,printedOrdinal:4}).modernChartAliasProjection.hhc,'Phu Thê');
});
await check('Released engine/HTML/site remain unchanged from the verified Yangren release',async()=>{
 const current=await read(resolve(w,'archives/v53-before-tuvi-void-child/PACKAGE_MANIFEST.json'));assert.equal(current.files.length,3521);assert.equal(sha(await readFile(resolve(w,'Huyen_Hoc_Cac.html'))),current.product.sha256);
 for(const name of['engine.js','Huyen_Hoc_Cac.html','site/index.html','fortune.js'])assert.equal(sha(await readFile(resolve(r,name))),current.files.find(x=>x.file===name).sha256);
});
const out={date:'2026-10-28',status:'staged-six-source-ordinal-alias-projections-verified-age-semantics-and-tail-open',checks,summary:{sourcePrintedOrdinalCoordinates:6,actualHHCTuviCalls:hhcCalls,actualIztroNatalCalls:iztroCalls,actualNatalContexts:12,privateOrdinalPalaceBindings:lookups,expandedPriorSourcePositions:1,newExactNativeCrops:1,newHTTPRequests:1,successfulImageDownloads:0,retained403Bodies:1,newOriginalContainers:0,newSourcePositions:0},runtime,runtimeIdentity,
 sourceAgeCountingConventionResolved:false,firstMajorPeriodStartResolved:false,GregorianAgeAdapterEstablished:false,wholePassageTranscribed:false,practicalOutcomesValidated:false,consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'CHILD_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
