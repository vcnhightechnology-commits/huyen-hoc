import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import{createRequire}from'node:module';import vm from'node:vm';import assert from'node:assert/strict';
import{bladeCoordinate}from'../research/bazi-jianlu-context/blade-reference.mjs';
import{luIllustration}from'../research/bazi-jianlu-context/lu-illustration-reference.mjs';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/bazi-jianlu-context'),q=resolve(r,'qa/bazi-jianlu-context'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const old=await read(resolve(w,'archives/v53-before-bazi-jianlu-context/PACKAGE_MANIFEST.json')),sourceRows=(await read(resolve(r,'research/bazi-jianlu-coordinates/SOURCE_ROWS.json'))).rows,fixtures=(await read(resolve(r,'research/bazi-jianlu-coordinates/PROBE_RESULTS.json'))).fixtures;
const source=await read(resolve(b,'SOURCE_MANIFEST.json')),blade=await read(resolve(b,'BLADE_TABLES.json')),contexts=await read(resolve(b,'JIANLU_CONTEXTS.json'));
await check('Original source identities, actual lunar dependency and unchanged engine/relations bytes',async()=>{
 assert.equal(sha(await readFile(resolve(w,source.sourceContainer))),source.sourceSHA256);
 for(const x of[...source.retainedDigital,...source.nativeImages])assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 const audit=await read(resolve(r,'research/bazi-late-zi/VERIFICATION.json'));for(const x of audit.runtime)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 for(const file of['engine.js','bazi-relations.js','app.js','content.js'])assert.equal(sha(await readFile(resolve(r,file))),old.files.find(x=>x.file===file).sha256);
});
const req=createRequire(import.meta.url),L=req(resolve(w,'v46/node_modules/lunar-typescript')),c={};c.window=c;vm.createContext(c);
for(const file of['engine.js','bazi-relations.js'])vm.runInContext(await readFile(resolve(r,file),'utf8'),c);
for(const file of['bazi-month-context.js','bazi-cycles.js'])vm.runInContext(await readFile(resolve(b,'consumer-candidate',file),'utf8'),c);
const E=c.HHC_ENGINE,M=c.HHC_BAZI_MONTH_CONTEXT,han='甲乙丙丁戊己庚辛壬癸',vn={'比肩':'Tỷ Kiên','劫财':'Kiếp Tài','食神':'Thực Thần','伤官':'Thương Quan','偏财':'Thiên Tài','正财':'Chính Tài','七杀':'Thất Sát','正官':'Chính Quan','偏印':'Thiên Ấn','正印':'Chính Ấn'};
const runtime=[];let hhcCalls=0,lunarCalls=0,syntheticMonthContexts=0,bladeContexts=0;
await check('Ten actual charts match all four pillars, actual 临官 month status and year/hour relation locations',()=>{
 for(const f of fixtures){
  const chart=E.bazi(f.input);hhcCalls++;const ec=L.Solar.fromYmdHms(f.input.y,f.input.m,f.input.d,f.input.hour,f.input.minute,0).getLunar().getEightChar();ec.setSect(2);lunarCalls++;
  const actualPillars=Array.from(chart.pillars,p=>p.han);assert.deepEqual(actualPillars,[ec.getYear(),ec.getMonth(),ec.getDay(),ec.getTime()]);assert.equal(ec.getMonthDiShi(),'临官');
  const out=M.inspect(chart);assert(out.matched&&out.known);assert.equal(out.dayStem,E.stems[han.indexOf(f.source.dayStem)]);
  for(const [key,index]of[['year',0],['hour',3]]){
   assert.equal(out[key].stem,E.stems[chart.all[index].s]);assert.equal(out[key].relation,vn[L.LunarUtil.SHI_SHEN[f.source.dayStem+han[chart.all[index].s]]]);
  }
  assert.equal(out.patternEstablished,null);assert.equal(out.usefulGodSelected,null);
  runtime.push({input:f.input,actualPillars,actualMonthStage:ec.getMonthDiShi(),consumer:JSON.parse(JSON.stringify(out))});
 }
 assert.equal(runtime.length,10);
});
await check('120 explicit day/month contexts use source month coordinates rather than peer counts or day branch',()=>{
 const chart=E.bazi(fixtures[0].input);hhcCalls++;
 for(const row of sourceRows)for(let month=0;month<12;month++){
  const clone=JSON.parse(JSON.stringify(chart));clone.dayP.s=han.indexOf(row.dayStem);clone.all[2].s=clone.dayP.s;clone.all[1].b=month;
  assert.equal(M.inspect(clone).matched,E.branches[month]==={'子':'Tý','丑':'Sửu','寅':'Dần','卯':'Mão','辰':'Thìn','巳':'Tỵ','午':'Ngọ','未':'Mùi','申':'Thân','酉':'Dậu','戌':'Tuất','亥':'Hợi'}[row.monthBranch]);syntheticMonthContexts++;
 }
 assert.equal(syntheticMonthContexts,120);
});
await check('Unknown birth hour keeps a known month reading without inventing an hour; ambiguous or unmatched charts have no new reading',()=>{
 const noTime={...fixtures[0].input,noTime:true};delete noTime.hour;delete noTime.minute;const unknown=E.bazi(noTime);hhcCalls++;
 const out=M.inspect(unknown);assert(out.matched);assert.equal(out.hour,null);assert.equal(out.completeChart,false);assert(M.render(unknown).includes('Chưa có giờ sinh để xác định.'));
 const uncertain={...unknown,uncertainPillars:[false,true,false,false]};assert.equal(M.inspect(uncertain).matched,null);assert.equal(M.render(uncertain),'');
 const different=E.bazi({...fixtures[0].input,d:22});hhcCalls++;assert.equal(M.inspect(different).matched,false);assert.equal(M.render(different),'');
 assert.throws(()=>M.inspect({}));
});
await check('Candidate rendering recomputes from canonical chart and does not infer useful god or outcomes',()=>{
 const chart=E.bazi(fixtures[0].input);hhcCalls++;const before=JSON.stringify(chart);const out=M.inspect(chart);out.year.stem='invented';assert.notEqual(M.inspect(chart).year.stem,'invented');assert.equal(JSON.stringify(chart),before);
 const html=M.render(chart);assert(html.includes('result-expand-export'));assert(html.includes('Kiến Lộc'));assert(!html.includes(' open'));assert(!/CADAL|KR3g|SHA-256|SOURCE_MANIFEST|夭折|主貧賤/.test(html));
});
await check('Two named blade tables preserve eight direct versus five direct coordinates and explicit unknown/excluded states over240 contexts',()=>{
 const branches='子丑寅卯辰巳午未申酉戌亥';
 for(const table of blade.tables)for(const stem of han)for(const candidateBranch of branches){
  const out=bladeCoordinate({system:table.system,stem,candidateBranch}),row=table.rows.find(x=>x.stem===stem),excluded=table.explicitlyExcludedStems.includes(stem);
  assert.equal(out.sourceBranch,row?.branch??null);assert.equal(out.coordinateMatched,row?row.branch===candidateBranch:excluded?false:null);
  assert.equal(out.coordinateStatus,row?'directly-stated':excluded?'explicitly-excluded':'not-stated-in-this-table');assert.equal(out.practicalOutcome,null);bladeContexts++;
 }
 assert.equal(bladeContexts,240);
 const named=(system,stem)=>bladeCoordinate({system,stem,candidateBranch:null});
 assert.equal(named(blade.tables[0].system,'戊').sourceScopeAllowsCoordinate,null);
 assert.equal(named(blade.tables[1].system,'己').sourceScopeAllowsCoordinate,false);
 assert.equal(named(blade.tables[0].system,'乙').sourceBranch,'辰');assert.equal(named(blade.tables[1].system,'乙').sourceBranch,null);
 for(const context of[{stem:'甲',candidateBranch:'卯'},{system:blade.tables[0].system,stem:'甲乙',candidateBranch:'卯'},{system:blade.tables[0].system,stem:'甲',candidateBranch:undefined}])assert.throws(()=>bladeCoordinate(context),TypeError);
});
await check('The explicit 甲 Lu illustration preserves four overlapping membership projections and unknown positional semantics',()=>{
 const system='WYG003-jia-lu-illustrated-branch-membership',sourceStem='甲',named=[...'寅亥丑卯'];
 const masks={mingHe:[3,7,11,15],anHe:[2,6,10,14],xuGong:[12,14],shiGong:[13,15]};
 for(let mask=0;mask<16;mask++){
  const relevantBranches=named.filter((x,i)=>mask&(1<<i)),out=luIllustration({system,sourceStem,relevantBranches,allRelevantBranchesKnown:true});
  for(const [key,expected]of Object.entries(masks))assert.equal(out.branchMembershipProjection[key],expected.includes(mask));
  assert.equal(out.sourcePositionalPremiseVerified,null);assert.equal(out.fullSourcePatternEstablished,null);assert.equal(out.practicalOutcome,null);
 }
 for(const extra of[{sourceStem:'甲',allRelevantBranchesKnown:false},{sourceStem:'乙',allRelevantBranchesKnown:true}]){
  assert.equal(luIllustration({system,relevantBranches:[...'寅亥丑卯'],...extra}).branchMembershipProjection,null);
 }
 assert.throws(()=>luIllustration({system,sourceStem,relevantBranches:[],allRelevantBranchesKnown:undefined}),TypeError);
 const incomplete=luIllustration({system,sourceStem,relevantBranches:[...'亥丑卯'],allRelevantBranchesKnown:false});assert.equal(incomplete.branchMembershipProjection,null);
});
await check('All44 source contexts cover1223 retained digital characters; exceptions, voices and incomplete strength premises remain explicit',async()=>{
 assert.equal(contexts.units.length,44);const joined=contexts.units.map(x=>x.retainedDigitalText).join('');assert.equal(joined.length,1223);
 for(let i=0;i<44;i++){const x=contexts.units[i];assert.equal(x.digitalEndExclusive-x.digitalStart,x.retainedDigitalText.length);if(i)assert.equal(contexts.units[i-1].digitalEndExclusive,x.digitalStart);assert(x.sourceImages.length);assert(x.dispositionStatus);}
 assert.equal(contexts.allSourceImageCharactersCollated,false);assert.equal(contexts.wholeSectionApplied,false);
 assert(contexts.units.find(x=>x.id==='wu-fire-seal-exception').retainedDigitalText.includes('雖無財官主吉'));
 const cross=await read(resolve(b,'CROSSREF_READINGS.json'));assert(cross.duplicateByteIdentical);assert(cross.sourceWarnings.some(x=>x.includes('&KR0339;')));
 const txt=await readFile(resolve(b,'DIGITAL_CROSSREF_BLADE.txt'),'utf8');assert(txt.includes('子平以甲丙戊庚壬五陽干有刃'));assert(txt.includes('其義見後論陽刃格中'));
});
await check('Printed four-pillar example remains a feasibility fixture and all existing cycle calculation code is unchanged',async()=>{
 const p=await read(resolve(b,'SOURCE_EXAMPLE_PROBE.json'));assert.deepEqual(p.actualPillars,['丙戌','丁酉','辛酉','乙未']);assert.equal(p.sourceClaimedOutcomeValidated,false);assert.equal(p.GregorianBirthDateAttributedToHistoricalPerson,false);
 const previous=await readFile(resolve(w,'archives/v53-before-bazi-jianlu-context/bazi-cycles.js'),'utf8'),candidate=await readFile(resolve(b,'consumer-candidate/bazi-cycles.js'),'utf8');assert.equal(previous.split('function render')[0],candidate.split('function render')[0]);
 const html=await readFile(resolve(b,'consumer-candidate/Huyen_Hoc_Cac.html'),'utf8');assert(html.includes((await readFile(resolve(b,'consumer-candidate/bazi-month-context.js'),'utf8')).trim()));
 const current=await readFile(resolve(r,'Huyen_Hoc_Cac.html'));assert.equal(sha(current),old.product.sha256);assert(!current.includes(Buffer.from('bazi-month-context')));
});
const out={date:'2026-10-27',checks,summary:{actualHHCBaziCalls:hhcCalls,actualLunarCalls:lunarCalls,actualRuntimeFixtures:10,syntheticMonthContexts,privateBladeContexts:bladeContexts,privateLuIllustrationMasks:16,directBladeRows:13,sourceContextUnits:44,retainedDigitalBodyCharacters:1223,expandedPreviouslyReadPages:10,newSourcePages:27,newConditionalContentPages:24,newHTTPRequests:2,newOriginalContainers:1},runtime,
 consumerChanged:false,candidateChanged:true,visualQAComplete:false,fullPatternClassifier:false,strengthMethodValidated:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
