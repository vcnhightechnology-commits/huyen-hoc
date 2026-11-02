import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import{createRequire}from'node:module';import vm from'node:vm';import assert from'node:assert/strict';
import{masterLabel}from'../research/tuvi-masters/master-reference.mjs';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/tuvi-masters'),q=resolve(r,'qa/tuvi-masters'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const source=await read(resolve(b,'SOURCE_MANIFEST.json')),table=await read(resolve(b,'SOURCE_TABLES.json')),system=table.system,branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const req=createRequire(import.meta.url),iztro=req(resolve(w,'v46/node_modules/iztro')),c={};c.window=c;vm.createContext(c);vm.runInContext(await readFile(resolve(r,'engine.js'),'utf8'),c);const E=c.HHC_ENGINE;
await check('Retained institutional JPEGs and pinned real iztro package/runtime have their recorded bytes',async()=>{
 for(const x of source.images)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 assert.equal(sha(await readFile(resolve(w,source.runtimeTarball))),source.runtimeTarballSHA256);
 for(const x of source.runtime){const data=await readFile(resolve(w,x.file));assert.equal(data.length,x.bytes);assert.equal(sha(data),x.sha256);assert(x.byteIdenticalToRetainedPackage);}
 assert.equal(req(resolve(w,'v46/node_modules/iztro/package.json')).version,'2.6.2');
});
await check('All24 source coordinates preserve twelve Ming labels, ten resolved Body labels and two literal unresolved compounds',()=>{
 assert.equal(table.rows.length,24);
 for(const kind of['ming-master','body-master'])for(const sourceBranch of branches){
  const row=table.rows.find(x=>x.kind===kind&&x.branch===sourceBranch),out=masterLabel({system,kind,sourceBranch});assert(row);assert.equal(out.sourceNameLiteral,row.sourceNameLiteral);assert.equal(out.practicalOutcome,null);assert.equal(out.starStrength,null);
 }
 assert.equal(table.rows.filter(x=>x.kind==='body-master'&&!x.sourceSingleStarResolved).length,2);
 for(const sourceBranch of['子','午']){
  const out=masterLabel({system,kind:'body-master',sourceBranch});assert.equal(out.sourceNameLiteral,'火鈴星');assert.equal(out.sourceStarName,null);assert.equal(out.sourceSingleStarResolved,false);assert.deepEqual(out.editorialParseCandidates,['火星','铃星']);assert.equal(out.bodyBirthYearAnchorExplicitlyAttested,false);
 }
});
let actualHHCTuviCalls=0,actualIztroDefaultNatalCalls=0,actualIztroZhongzhouNatalCalls=0;const runtime=[];
await check('144 actual HHC charts and288 actual iztro charts preserve source-palace versus alternate-year Ming anchors',()=>{
 try{
  for(let yearIndex=0;yearIndex<12;yearIndex++)for(let hourBranch=0;hourBranch<12;hourBranch++){
   const input={y:1984+yearIndex,m:1,d:15,calendar:'lunar',leap:false,leapPolicy:'same',dayPolicy:'current',tz:8,hour:hourBranch===0?0:hourBranch*2,minute:0,gender:hourBranch%2?'female':'male'};
   const chart=E.tuvi(input);actualHHCTuviCalls++;
   const solar=`${chart.originalSolar.y}-${String(chart.originalSolar.m).padStart(2,'0')}-${String(chart.originalSolar.d).padStart(2,'0')}`,gender=input.gender==='male'?'男':'女';
   const config={yearDivide:'normal',horoscopeDivide:'normal',ageDivide:'normal',dayDivide:'current'};
   iztro.astro.resetConfig();iztro.astro.config({...config,algorithm:'default'});
   const def=iztro.astro.bySolar(solar,hourBranch,gender,false,'zh-CN');actualIztroDefaultNatalCalls++;
   const sourceMing=masterLabel({system,kind:'ming-master',sourceBranch:branches[chart.menh]});
   assert.equal(def.earthlyBranchOfSoulPalace,branches[chart.menh]);assert.equal(def.soul,sourceMing.sourceStarName);
   const placed=chart.stars[sourceMing.vietnameseStar];assert(placed&&Number.isInteger(placed.idx));
   const modernBodyContext=masterLabel({system,kind:'body-master',sourceBranch:branches[chart.branch]});
   if(modernBodyContext.sourceSingleStarResolved)assert.equal(def.body,modernBodyContext.sourceStarName);
   else{assert.equal(modernBodyContext.sourceStarName,null);assert(modernBodyContext.editorialParseCandidates.includes(def.body));}
   iztro.astro.resetConfig();iztro.astro.config({...config,algorithm:'zhongzhou'});
   const alt=iztro.astro.bySolar(solar,hourBranch,gender,false,'zh-CN');actualIztroZhongzhouNatalCalls++;
   const alternateYearAnchor=masterLabel({system,kind:'ming-master',sourceBranch:branches[chart.branch]});
   assert.equal(alt.soul,alternateYearAnchor.sourceStarName);assert.equal(alt.body,def.body);
   runtime.push({input,solar,palaceBranch:branches[chart.menh],birthYearBranch:branches[chart.branch],sourceMing:sourceMing.sourceStarName,hhcMasterStarPhysicalBranch:branches[placed.idx],
    iztroDefaultMing:def.soul,iztroZhongzhouMing:alt.soul,mingNamesDiffer:def.soul!==alt.soul,sourceBodyLiteral:modernBodyContext.sourceNameLiteral,
    sourceBodyResolved:modernBodyContext.sourceSingleStarResolved,iztroBody:def.body,bodyBirthYearIsComparedModernConvention:true});
  }
 }finally{iztro.astro.resetConfig();}
 assert.equal(runtime.length,144);
});
await check('Observed anchor contrasts retain122 different names and22 equal names without treating the alternate algorithm as an error',()=>{
 assert.equal(runtime.filter(x=>x.mingNamesDiffer).length,122);assert.equal(runtime.filter(x=>!x.mingNamesDiffer).length,22);
 assert.equal(new Set(runtime.map(x=>x.palaceBranch)).size,12);assert.equal(new Set(runtime.map(x=>x.birthYearBranch)).size,12);
 assert.equal(new Set(runtime.map(x=>x.sourceMing)).size,7);
});
await check('Body comparisons retain120 direct name matches and24 source-undetermined compound cases',()=>{
 const direct=runtime.filter(x=>x.sourceBodyResolved),unknown=runtime.filter(x=>!x.sourceBodyResolved);assert.equal(direct.length,120);assert.equal(unknown.length,24);
 assert(unknown.every(x=>['子','午'].includes(x.birthYearBranch)&&x.sourceBodyLiteral==='火鈴星'&&x.iztroBody==='火星'));
 assert.equal(table.bodyBirthYearAnchorExplicitlyAttested,false);
});
await check('Unknown branch stays unknown; invalid or missing source fields are rejected and the table cannot be mutated by callers',()=>{
 for(const kind of['ming-master','body-master']){const x=masterLabel({system,kind,sourceBranch:null});assert.equal(x.sourceCoordinateKnown,null);assert.equal(x.sourceStarName,null);assert.equal(x.sourceBranchAdapterInferred,false);}
 for(const x of[{kind:'ming-master',sourceBranch:'子'},{system,kind:'unknown',sourceBranch:'子'},{system,kind:'ming-master',sourceBranch:'Tý'},{system,kind:'ming-master',sourceBranch:undefined}])assert.throws(()=>masterLabel(x),TypeError);
 const x=masterLabel({system,kind:'body-master',sourceBranch:'子'});x.editorialParseCandidates.length=0;assert.equal(masterLabel({system,kind:'body-master',sourceBranch:'子'}).editorialParseCandidates.length,2);
});
await check('Current public source, HTML and engine remain identical to the previous verified release',async()=>{
 const previous=await read(resolve(w,'archives/v53-before-tuvi-masters/PACKAGE_MANIFEST.json'));
 for(const file of['Huyen_Hoc_Cac.html','site/index.html','engine.js','app.js','content.js','fortune.js','tuvi-context.js'])assert.equal(sha(await readFile(resolve(r,file))),previous.files.find(x=>x.file===file).sha256);
 assert.equal(sha(await readFile(resolve(w,'Huyen_Hoc_Cac.html'))),previous.product.sha256);
});
const out={date:'2026-10-27',checks,summary:{sourceMingCoordinates:12,sourceBodyCoordinates:12,sourceBodySingleStarCoordinates:10,sourceBodyUnresolvedCoordinates:2,
 actualHHCTuviCalls,actualIztroDefaultNatalCalls,actualIztroZhongzhouNatalCalls,actualRuntimeContexts:144,mingAnchorNameContrasts:122,mingAnchorNameEqual:22,bodyDirectNameMatches:120,bodySourceUndeterminedContexts:24,
 expandedPreviouslyReadPages:2,nativeQACrops:2,newHTTPRequests:0,newOriginalContainers:0,newSourcePages:0},runtime,
 consumerChanged:false,bodyBirthYearAnchorExplicitlyAttested:false,bodyCompoundResolved:false,majorPeriodStartResolved:false,wholeBookApplied:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
