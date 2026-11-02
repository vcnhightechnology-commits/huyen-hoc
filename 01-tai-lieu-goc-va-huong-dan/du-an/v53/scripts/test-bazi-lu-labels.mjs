import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import{createRequire}from'node:module';import assert from'node:assert/strict';
import{luLabel,luStorage}from'../research/bazi-lu-labels/lu-label-reference.mjs';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/bazi-lu-labels'),q=resolve(r,'qa/bazi-lu-labels'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const table=await read(resolve(b,'SOURCE_ROWS.json')),storage=await read(resolve(b,'LU_STORAGE_TABLE.json')),contexts=await read(resolve(b,'LU_SECTION_CONTEXTS.json')),manifest=await read(resolve(b,'SOURCE_MANIFEST.json'));
const require=createRequire(import.meta.url),L=require(resolve(w,'v46/node_modules/lunar-typescript')),stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
let actualLunarJiaZiLookups=0,privateLabelContexts=0,privateStorageContexts=0;
await check('Pinned source container, source image and runtime bytes match retained audits',async()=>{
 assert.equal(sha(await readFile(resolve(w,manifest.sourceContainer))),manifest.sourceSHA256);
 for(const x of[...manifest.nativePages,manifest.additionalRetainedNativeContextPage])assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 const audit=await read(resolve(r,'research/bazi-late-zi/VERIFICATION.json'));for(const x of audit.runtime)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
});
await check('Fifty direct pairs form ten distinct five-pillar source groups, all valid in the actual sixty-pillar lunar runtime',()=>{
 assert.equal(table.rows.length,50);assert.equal(new Set(table.rows.map(x=>x.id)).size,50);
 const valid=L.LunarUtil.JIA_ZI;assert.equal(valid.length,60);
 for(let i=0;i<60;i++){assert.equal(L.LunarUtil.getJiaZiIndex(valid[i]),i);actualLunarJiaZiLookups++;}
 for(const stem of stems){
  const group=table.rows.filter(x=>x.sourceStem===stem);assert.equal(group.length,5);assert.equal(new Set(group.map(x=>x.candidatePillar)).size,5);
  for(const x of group){assert(valid.includes(x.candidatePillar));assert.equal(x.candidatePillar[1],x.sourceLuBranch);assert(x.sourceLabels.length);assert(x.sourcePages.length);}
 }
});
await check('Six hundred explicit stem/pillar queries return fifty printed pairs without completing absent labels or inferring an outcome',()=>{
 let matched=0;
 for(const sourceStem of stems)for(const candidatePillar of L.LunarUtil.JIA_ZI){
  const row=table.rows.find(x=>x.sourceStem===sourceStem&&x.candidatePillar===candidatePillar),out=luLabel({system:table.system,sourceStem,candidatePillar});
  assert.equal(out.exactPairDocumented,!!row);assert.deepEqual(out.sourceLabels,row?row.sourceLabels:null);
  for(const key of['sourceStemAnchorField','modernTenGod','patternEstablished','strengthEstablished','practicalOutcome'])assert.equal(out[key],null);
  if(row)matched++;privateLabelContexts++;
 }
 assert.equal(privateLabelContexts,600);assert.equal(matched,50);
});
await check('Eight shared source clauses retain explicit group boundaries; unsupplied local assessments stay empty',()=>{
 assert.equal(table.sharedClaims.length,8);
 for(const claim of table.sharedClaims)for(const candidatePillar of claim.pillars){
  const out=luLabel({system:table.system,sourceStem:claim.stem,candidatePillar});assert(out.sharedSourceClaims.some(x=>x.id===claim.id&&x.clause===claim.clause));
 }
 for(const [sourceStem,candidatePillar]of[['丙','辛巳'],['乙','己卯'],['戊','辛巳'],['己','丙午']]){
  const out=luLabel({system:table.system,sourceStem,candidatePillar});assert.equal(out.rowSpecificSourceClause,'');assert.deepEqual(out.sharedSourceClaims,[]);
 }
 const xin=luLabel({system:table.system,sourceStem:'辛',candidatePillar:'丁酉'});assert(xin.rowSpecificSourceClause.includes('丁木受氣辛水沐浴'));assert.equal(xin.practicalOutcome,null);
 const wu=table.sharedClaims.find(x=>x.id==='wu-final-two');assert(wu.scopeLimit.includes('not established'));
});
await check('Source-specific labels with the same candidate remain distinct across explicitly supplied stems',()=>{
 const a=luLabel({system:table.system,sourceStem:'丙',candidatePillar:'癸巳'}),b=luLabel({system:table.system,sourceStem:'戊',candidatePillar:'癸巳'});
 assert.deepEqual(a.sourceLabels,['伏貴神祿']);assert.deepEqual(b.sourceLabels,['貴神祿']);assert.notEqual(a.rowSpecificSourceClause,b.rowSpecificSourceClause);
 assert.equal(luLabel({system:table.system,sourceStem:'甲',candidatePillar:'壬寅'}).rowSpecificSourceClause,'帶截路空亡必為僧道');
 assert.equal(luLabel({system:table.system,sourceStem:'乙',candidatePillar:'壬寅'}).exactPairDocumented,false);
});
await check('Ten direct Lu storage coordinates remain a named system over120 contexts and do not satisfy the unquantified source example',()=>{
 assert.equal(storage.sourceGroups.flatMap(x=>x.stems).length,10);
 for(const sourceStem of stems)for(const candidateBranch of branches){
  const sourceBranch=storage.sourceGroups.find(x=>x.stems.includes(sourceStem)).branch,out=luStorage({system:storage.system,sourceStem,candidateBranch});
  assert.equal(out.coordinateMatched,sourceBranch===candidateBranch);assert.equal(out.sourceBranch,sourceBranch);assert.equal(out.sourceConditionalExampleSatisfied,null);assert.equal(out.ordinaryElementTombAlgorithm,false);assert.equal(out.practicalOutcome,null);privateStorageContexts++;
 }
 assert.equal(privateStorageContexts,120);
 assert.equal(luStorage({system:storage.system,sourceStem:'壬',candidateBranch:'辰'}).sourceBranch,'辰');
});
await check('Unknown inputs preserve null, impossible pillars are rejected, and returned data cannot mutate retained tables',()=>{
 const out=luLabel({system:table.system,sourceStem:'甲',candidatePillar:null});assert.equal(out.exactPairDocumented,null);assert.equal(out.sourceLabels,null);
 assert.equal(luStorage({system:storage.system,sourceStem:'甲',candidateBranch:null}).coordinateMatched,null);
 for(const input of[{system:table.system,sourceStem:'甲',candidatePillar:'甲丑'},{system:table.system,sourceStem:'甲',candidatePillar:undefined},{system:table.system,sourceStem:'甲乙',candidatePillar:'甲寅'},{sourceStem:'甲',candidatePillar:'甲寅'}])assert.throws(()=>luLabel(input),TypeError);
 assert.throws(()=>luStorage({system:storage.system,sourceStem:'甲'}),TypeError);
 const copy=luLabel({system:table.system,sourceStem:'甲',candidatePillar:'丙寅'});copy.sourceLabels[0]='invented';copy.sharedSourceClaims[0].pillars.length=0;
 const again=luLabel({system:table.system,sourceStem:'甲',candidatePillar:'丙寅'});assert.equal(again.sourceLabels[0],'福星祿');assert.equal(again.sharedSourceClaims[0].pillars.length,2);
});
await check('Twenty-eight contiguous digital contexts have explicit dispositions; historical claims and unresolved source semantics remain open',()=>{
 assert.equal(contexts.units.length,28);assert.equal([...contexts.units.map(x=>x.retainedDigitalText).join('')].length,2217);
 for(let i=0;i<28;i++){
  const x=contexts.units[i];assert.equal(x.digitalEndExclusive-x.digitalStart,[...x.retainedDigitalText].length);assert(x.nativePages.length&&x.disposition);
  if(i)assert.equal(contexts.units[i-1].digitalEndExclusive,x.digitalStart);
 }
 assert.equal(contexts.wholeSectionApplied,false);assert.equal(contexts.allSourceImageCharactersCollated,false);
 assert(contexts.units.find(x=>x.id==='fifty-labelled-pairs').retainedDigitalText.includes('甲土尅丙水為財'));
 assert(contexts.units.find(x=>x.id==='clash-void-claims').retainedDigitalText.includes('&KR0339;'));
 assert(contexts.units.find(x=>x.id==='closing-limit').retainedDigitalText.includes('亦不専在祿上'));
});
await check('Current public product and engine remain identical to the prior fully verified release',async()=>{
 const previous=await read(resolve(w,'archives/v53-before-bazi-lu-labels/PACKAGE_MANIFEST.json'));
 for(const file of['Huyen_Hoc_Cac.html','site/index.html','engine.js','bazi-relations.js','bazi-cycles.js','index.html'])assert.equal(sha(await readFile(resolve(r,file))),previous.files.find(x=>x.file===file).sha256);
 assert.equal(sha(await readFile(resolve(w,'Huyen_Hoc_Cac.html'))),previous.product.sha256);
});
const out={date:'2026-10-27',checks,summary:{sourceStemGroups:10,sourceLabelRows:50,sharedSourceClaims:8,privateLabelContexts,luStorageCoordinates:10,privateStorageContexts,sourceContextUnits:28,retainedDigitalBodyCharacters:2217,actualLunarJiaZiLookups,actualNatalChartCalls:0,expandedPreviouslyReadPages:6,newSourcePages:0,newHTTPRequests:0,newOriginalContainers:0},consumerChanged:false,modernTenGodEquivalenceEstablished:false,allSourceImageCharactersCollated:false,wholeLuSectionApplied:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
