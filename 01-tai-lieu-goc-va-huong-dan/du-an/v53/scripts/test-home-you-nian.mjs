import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import{youNian}from'../research/home-you-nian/you-nian-reference.mjs';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/home-you-nian'),q=resolve(r,'qa/home-you-nian');
const read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const rules=await read(resolve(b,'SOURCE_RELATIONS.json')),stars=await read(resolve(b,'SMALL_DIRECT_STARS.json')),policies=await read(resolve(b,'SOURCE_POLICIES.json'));
await check('Facsimile container and decoder retained identity',async()=>{const d=await read(resolve(b,'RENDERS.json'));assert.equal(sha(await readFile(resolve(w,d.source))),d.sourceSHA256);assert.equal(sha(await readFile(resolve(w,d.decoder))),d.decoderSHA256);assert(d.calibration.nativePixelEqualityWithPriorBrowserPNG);});
let directPairs=0;
await check('Seven directly read transformations cover all nonself pairs in each named system',()=>{
 const seen=new Set();for(const row of rules.rows)for(const pair of row.directUnorderedPairs)for(const [origin,target]of[[...pair],[...pair].reverse()]){
  assert(!seen.has(origin+target));seen.add(origin+target);directPairs++;
  for(const [system,key]of[['xieji-da','big'],['xieji-xiao','small']]){const x=youNian({system,origin,target});assert.equal(x.mask,row.mask);assert.equal(x.relation,row[key]);assert.equal(x.sourcePage,row.diagramPage);assert.equal(x.practicalOutcome,null);}
 }assert.equal(seen.size,56);
 for(const origin of '乾坤震巽坎離艮兌'){assert.equal(youNian({system:'xieji-da',origin,target:origin}).relation,'伏位');assert.equal(youNian({system:'xieji-xiao',origin,target:origin}).relation,'輔弼');}
});
await check('64 directly read small-system star abbreviations match independent relation map',()=>{let n=0;for(const row of stars.readings)for(const cell of row.starsByTarget){assert.equal(youNian({system:'xieji-xiao',origin:row.origin,target:cell.target}).star,stars.abbreviations[cell.printedAbbreviation]);n++;}assert.equal(n,64);});
let policyContexts=0;
await check('Two source contexts retain their different favorable-star sets without a default rating',()=>{for(const origin of '乾坤震巽坎離艮兌')for(const target of '乾坤震巽坎離艮兌'){
 assert.equal(youNian({system:'xieji-xiao',origin,target}).sourceContextRating,null);
 for(const p of policies.policies){const x=youNian({system:'xieji-xiao',origin,target,application:p.id});assert.equal(x.sourceContextRating,p.auspiciousStars.includes(x.star)?'吉':'凶');policyContexts++;}
}assert.equal(policyContexts,128);assert.equal(youNian({system:'xieji-xiao',origin:'乾',target:'巽',application:'geography-from-dragon'}).sourceContextRating,'吉');assert.equal(youNian({system:'xieji-xiao',origin:'乾',target:'巽',application:'date-selection-from-facing'}).sourceContextRating,'凶');});
let literalMatches=0,differences=0,selfRoleOnly=0;
await check('128 private relations distinguish 40 differing labels,16 literal agreements and8 self roles',()=>{for(const origin of '乾坤震巽坎離艮兌')for(const target of '乾坤震巽坎離艮兌'){
 const a=youNian({system:'xieji-da',origin,target}),c=youNian({system:'xieji-xiao',origin,target});
 if(origin===target){assert.notEqual(a.relation,c.relation);selfRoleOnly++;}else if(a.relation===c.relation)literalMatches++;else differences++;
}assert.deepEqual([literalMatches,differences,selfRoleOnly],[16,40,8]);});
await check('Unknown origin/target remain null; named system and inputs validated',()=>{for(const system of ['xieji-da','xieji-xiao']){assert.equal(youNian({system,origin:null,target:'乾'}).relation,null);assert.equal(youNian({system,origin:'乾',target:null}).mask,null);}for(const args of [{origin:'乾',target:'坤'},{system:'xieji-da',origin:7,target:'坤'},{system:'xieji-da',origin:'乾',target:'坤',application:'geography-from-dragon'},{system:'xieji-xiao',origin:'乾',target:'坤',application:'universal'}])assert.throws(()=>youNian(args),TypeError);});
const engineBytes=await readFile(resolve(r,'engine.js')),ctx={window:{}};vm.createContext(ctx);vm.runInContext(engineBytes.toString(),ctx);const engine=ctx.window.HHC_ENGINE;
const old=await read(resolve(r,'research/full-study/home/DAYOUNIAN_ENGINE_CHECK.json')),access=[...new Map(old.results.map(x=>[x.kua,{kua:x.kua,origin:x.sourceTrigram,input:x.engineAccessInput}])).values()];
let actualHHCDirectionsCalls=0;const fixtures=[];
await check('Eight actual HHC executions match all64 conditional palace/direction labels from image-based rules',()=>{
 const labels={'伏位':'Phục Vị','禍害':'Họa Hại','絶命':'Tuyệt Mệnh','天醫':'Thiên Y','生氣':'Sinh Khí','六煞':'Lục Sát','五鬼':'Ngũ Quỷ','延年':'Diên Niên'};
 for(const a of access){const out=engine.directions(a.input);actualHHCDirectionsCalls++;assert.equal(out.number,a.kua);
 for(const f of old.results.filter(x=>x.kua===a.kua)){const expected=youNian({system:'xieji-da',origin:a.origin,target:f.targetTrigram}),actual=out.all.find(x=>x.direction===f.target)?.label;assert.equal(actual,labels[expected.relation]);fixtures.push({origin:a.origin,target:f.targetTrigram,sourcePage:expected.sourcePage,expected:labels[expected.relation],actual,engineAccessInput:a.input});}
 }assert.equal(actualHHCDirectionsCalls,8);assert.equal(fixtures.length,64);
});
await check('Six digital artifacts and three failed HTTP bodies retain byte hashes',async()=>{
 const map=await read(resolve(b,'zhaijing/DIGITAL_UNIT_MAP.json')),cmp=await read(resolve(b,'zhaijing/TRANSMISSION_COMPARISON.json'));
 for(const x of [...map.sources,...cmp.HFLArtifacts]){const data=await readFile(resolve(w,x.file));assert.equal(data.length,x.bytes);assert.equal(sha(data),x.sha256);}
 const log=await read(resolve(b,'zhaijing/REQUESTS.json'));assert.deepEqual(log.records.map(x=>x.status),[403,403,503]);for(const x of log.records){const data=await readFile(resolve(b,'zhaijing',x.file));assert.equal(data.length,x.bytes);assert.equal(sha(data),x.sha256);assert(x.tls.authorized);assert.equal(x.usableAsSource,false);}
});
await check('Consumer remains byte-identical and excludes new private reference',async()=>{
 const data=await readFile(resolve(r,'Huyen_Hoc_Cac.html'));assert.equal(sha(data),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');assert.deepEqual(data,await readFile(resolve(w,'Huyen_Hoc_Cac.html')));assert.deepEqual(data,await readFile(resolve(r,'site/index.html')));for(const x of['you-nian-reference','home-you-nian','geography-from-dragon'])assert(!data.toString().includes(x));
});
await mkdir(q,{recursive:true});const out={date:'2026-10-27',checks,summary:{actualHHCDirectionsCalls,conditionalHHCLabels:64,privateRelations:128,directSmallStarCells:64,directNonselfPairs:directPairs,sourcePolicyContexts:policyContexts,differingLabels:differences,literalMatchingLabels:literalMatches,selfRoleOnly},
 engineSHA256:sha(engineBytes),fixtures,validated:'Conditional relation labels, named-system distinction and source-context guard only.',notValidated:['Year→kua/calendarboundary','Actual dwelling origin/dragon/sitting/facing','Room/stove/bed placement','Source predictive efficacy','Complete110pagevolume/allclauses'],consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
