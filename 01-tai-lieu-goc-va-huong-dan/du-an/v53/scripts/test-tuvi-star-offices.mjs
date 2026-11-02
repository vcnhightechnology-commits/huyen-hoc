import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import{createRequire}from'node:module';import vm from'node:vm';import assert from'node:assert/strict';
import{sourceStarProfile,attachDeclaredPlacement}from'../research/tuvi-star-offices/star-office-reference.mjs';
const b=resolve(import.meta.dirname,'../research/tuvi-star-offices'),w=resolve(b,'../../..'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
const table=await read(resolve(b,'SOURCE_TABLES.json')),system=table.system,branches=[...'子丑寅卯辰巳午未申酉戌亥'];
async function check(name,fn){await fn();checks.push({name,ok:true});}
await check('Thirty institutional JPEG derivative bodies match retained SHA/size, normal TLS and manual-reading inventory',async()=>{
 const s=await read(resolve(b,'SOURCE_MANIFEST.json')),r=await read(resolve(b,'FIRST_PASS_READINGS.json'));assert.equal(s.images.length,30);assert.equal(r.records.length,30);
 for(const x of s.images){const d=await readFile(resolve(b,x.file));assert.equal(d.length,x.bytes);assert.equal(sha(d),x.sha256);assert.equal(x.status,200);assert(x.TLSCertificateValidationEnabled&&x.actuallyViewed);assert(r.records.find(z=>z.canvas===x.canvas&&z.sha256===x.sha256&&z.actuallyViewed));}
 assert.equal(s.images.filter(x=>x.responseHeadersRetained).length,29);assert.equal(s.originalJP2BodiesAcquired,0);
});
await check('Fourteen profiles retain fifteen voice claims, compound elements and roles without scalar weights or inferred star placements',()=>{
 assert.equal(table.rows.length,14);assert.equal(table.rows.flatMap(x=>x.elementClaims).length,15);
 for(const star of['Thiên Đồng','Cự Môn'])assert.deepEqual(sourceStarProfile({system,star}).elementClaims[0].elements,['水','金']);
 assert.deepEqual(sourceStarProfile({system,star:'Thất Sát'}).elementClaims[0].elements,['火','金']);
 assert.deepEqual(sourceStarProfile({system,star:'Liêm Trinh'}).elementClaims[0].elements,['木']);
 const tan=sourceStarProfile({system,star:'Tham Lang'});assert.deepEqual(tan.elementClaims[1].roles,{'氣':'木','體':'水'});assert.equal(tan.elementClaims[0].voice,'Q&A answer');assert.equal(tan.elementClaims[1].canvas,23);
 for(const row of table.rows){const p=sourceStarProfile({system,star:row.vietnameseStar});assert.equal(p.elementScore,null);assert.equal(p.elementWeights,null);assert.equal(p.practicalOutcome,null);assert.equal(p.officeIsPlacementConstraint,false);assert.equal(p.fullChapterApplied,false);}
});
await check('Explicit source and exact canonical names are required; null placement does not fabricate a palace',()=>{
 for(const x of[{star:'Tử Vi'},{system,star:'紫微'},{system,star:'Unknown'}])assert.throws(()=>sourceStarProfile(x),TypeError);
 for(const x of[{branch:undefined,palace:null},{branch:'Tý',palace:null},{branch:null,palace:'官祿'},{branch:'子',palace:'官禄'}])assert.throws(()=>attachDeclaredPlacement({system,star:'Thái Dương',...x}),TypeError);
 const p=attachDeclaredPlacement({system,star:'Thái Dương',branch:null,palace:null});assert.equal(p.declaredPlacement.known,false);assert.equal(p.physicalPalaceInferred,false);
});
const req=createRequire(import.meta.url),iztro=req(resolve(w,'v46/node_modules/iztro')),ctx={};ctx.window=ctx;vm.createContext(ctx);const engine=await readFile(resolve(w,'v53/engine.js'));vm.runInContext(engine.toString(),ctx);const E=ctx.HHC_ENGINE;
const vn={'Mệnh':'命宮','Huynh Đệ':'兄弟','Phu Thê':'夫妻','Tử Tức':'子女','Tài Bạch':'財帛','Tật Ách':'疾厄','Thiên Di':'遷移','Nô Bộc':'交友','Quan Lộc':'官祿','Điền Trạch':'田宅','Phúc Đức':'福德','Phụ Mẫu':'父母'},cn={'命宫':'命宮','兄弟':'兄弟','夫妻':'夫妻','子女':'子女','财帛':'財帛','疾厄':'疾厄','迁移':'遷移','仆役':'交友','交友':'交友','官禄':'官祿','田宅':'田宅','福德':'福德','父母':'父母'};
let actualHHCTuviCalls=0,actualIztroNatalCalls=0;const runtime=[];
await check('Twelve real natal contexts attach168 source-star profiles to HHC positions and match168 real iztro major-star branch/palace coordinates',()=>{
 assert.equal(req(resolve(w,'v46/node_modules/iztro/package.json')).version,'2.6.2');
 try{for(let i=0;i<12;i++){
  const input={y:1984+i,m:1,d:15,calendar:'lunar',leap:false,leapPolicy:'same',dayPolicy:'current',tz:8,hour:i===0?0:i*2,minute:0,gender:i%2?'female':'male'};
  const chart=E.tuvi(input);actualHHCTuviCalls++;const solar=`${chart.originalSolar.y}-${String(chart.originalSolar.m).padStart(2,'0')}-${String(chart.originalSolar.d).padStart(2,'0')}`;
  iztro.astro.resetConfig();iztro.astro.config({yearDivide:'normal',horoscopeDivide:'normal',ageDivide:'normal',dayDivide:'current',algorithm:'default'});
  const iz=iztro.astro.bySolar(solar,i,input.gender==='male'?'男':'女',false,'zh-CN');actualIztroNatalCalls++;
  for(const row of table.rows){const star=chart.stars[row.vietnameseStar];assert(star&&Number.isInteger(star.idx));const hp=chart.palaces.find(p=>p.idx===star.idx),ip=iz.palaces.find(p=>p.majorStars.some(s=>s.name===row.iztroName));assert(ip);assert.equal(ip.earthlyBranch,branches[star.idx]);assert(vn[hp.name],hp.name);assert(cn[ip.name],ip.name);assert.equal(vn[hp.name],cn[ip.name]);
   const profile=attachDeclaredPlacement({system,star:row.vietnameseStar,branch:branches[star.idx],palace:vn[hp.name]});assert.equal(profile.officeReplacesPhysicalPlacement,false);assert.equal(profile.practicalOutcome,null);
   runtime.push({input,solar,star:row.vietnameseStar,sourceID:row.id,hhcBranch:branches[star.idx],hhcPalace:hp.name,canonicalPalace:vn[hp.name],iztroBranch:ip.earthlyBranch,iztroPalace:ip.name,sourceOffice:profile.officeClaim.literal,profile});
  }
 }}finally{iztro.astro.resetConfig();}assert.equal(runtime.length,168);
});
await check('Symbolic office labels remain attached when physical placement is elsewhere, with no office-based placement or element score',()=>{
 const selected={'Thái Dương':'官祿','Thiên Đồng':'福德','Thái Âm':'田宅','Thiên Tướng':'官祿','Thiên Lương':'父母','Thiên Cơ':'兄弟'};
 for(const star of Object.keys(selected)){const rows=runtime.filter(x=>x.star===star);assert.equal(rows.length,12);assert(rows.some(x=>x.canonicalPalace!==selected[star]));for(const x of rows){assert.equal(x.profile.declaredPlacement.palace,x.canonicalPalace);assert.equal(x.profile.officeIsPlacementConstraint,false);assert.equal(x.profile.elementScore,null);}}
});
await check('Caller mutation and explicitly partial placement cannot corrupt source profiles or infer a missing palace',()=>{
 const p=sourceStarProfile({system,star:'Tham Lang'});p.elementClaims[1].roles['氣']='火';p.elementClaims.length=0;assert.equal(sourceStarProfile({system,star:'Tham Lang'}).elementClaims.length,2);assert.equal(sourceStarProfile({system,star:'Tham Lang'}).elementClaims[1].roles['氣'],'木');
 const q=attachDeclaredPlacement({system,star:'Thái Dương',branch:'子',palace:null});assert.equal(q.declaredPlacement.branch,'子');assert.equal(q.declaredPlacement.palace,null);assert.equal(q.physicalPalaceInferred,false);
});
await check('Public HTML, clean site, current engine and public modules remain byte-identical to4718-file release',async()=>{
 const previous=await read(resolve(w,'archives/v53-before-tuvi-star-offices/PACKAGE_MANIFEST.json'));
 assert.equal(previous.files.length,4718);for(const file of['Huyen_Hoc_Cac.html','site/index.html','engine.js','app.js','content.js','fortune.js','tuvi-context.js'])assert.equal(sha(await readFile(resolve(w,'v53',file))),previous.files.find(x=>x.file===file).sha256);
 assert.equal(sha(await readFile(resolve(w,'Huyen_Hoc_Cac.html'))),previous.product.sha256);
});
const out={date:'2026-10-28',checks,summary:{sourceProfiles:14,sourceVoiceElementClaims:15,actualHHCTuviCalls,actualIztroNatalCalls,realContexts:12,majorStarBranchPalaceCoordinatesMatched:168,profilesProjected:168},runtime,
 actualEngine:{file:'v53/engine.js',sha256:sha(engine)},iztroVersion:'2.6.2',runtimePackageProof:'v53/research/tuvi-masters/SOURCE_MANIFEST.json',
 sourcePlacementAlgorithmValidated:false,sourceOutcomesValidated:false,wholeChaptersApplied:false,consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(w,'v53/qa/tuvi-star-offices/REFERENCE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
