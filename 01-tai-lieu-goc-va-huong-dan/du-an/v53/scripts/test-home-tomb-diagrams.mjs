import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import{createRequire}from'node:module';import assert from'node:assert/strict';
import{diagramYear,diagramMonth}from'../research/home-tomb-diagrams/diagram-reference.mjs';
import{tombMovement,sourceOvercoming}from'../research/home-source-tables/tomb-reference.mjs';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/home-tomb-diagrams'),q=resolve(r,'qa/home-tomb-diagrams'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const table=await read(resolve(b,'DIAGRAM_TABLES.json')),source=await read(resolve(b,'SOURCE_MANIFEST.json')),stems=[...'甲乙丙丁戊己庚辛壬癸'],system='xieji41-49-ordinary-diagram',sourcePeriod='before-current-winter-solstice';
const req=createRequire(import.meta.url),L=req(resolve(w,'v46/node_modules/lunar-typescript')),runtimeYears=[],runtimeMonths=[];let lunarYears=0,lunarMonths=0;
await check('Two retained diagram source images, three prose images and actual pinned lunar runtime bytes match their identities',async()=>{
 assert.equal(sha(await readFile(resolve(w,source.sourceContainer))),source.sourceSHA256);
 for(const x of source.nativeDiagramPages)assert.equal(sha(await readFile(resolve(w,x.source))),x.sourceSHA256);
 for(const x of source.additionalProsePages)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 const audit=await read(resolve(r,'research/bazi-late-zi/VERIFICATION.json'));for(const x of audit.runtime)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
});
await check('20 movement cells and24 mountain labels independently read from diagram41 agree with the prior prose table',()=>{
 assert.equal(table.rows.length,20);assert.equal(table.groups.flatMap(x=>x.mountains).length,24);assert.equal(new Set(table.groups.flatMap(x=>x.mountains)).size,24);
 for(const row of table.rows){const g=table.groups.find(x=>x.id===row.mountainGroup),old=tombMovement({system:'xieji-tomb-movement',mountain:g.mountains[0],sourceYearStem:row.sourceYearStems[0],sourcePeriod});assert.equal(row.sourceMovementElement41,old.movementElement);}
});
await check('60 actual lunar EightChar year-pillar executions compare all50 listed year coordinates without turning omitted years into safety claims',()=>{
 for(let year=1984;year<2044;year++){
  const e=L.Solar.fromYmdHms(year,6,15,12,0,0).getLunar().getEightChar();e.setSect(2);lunarYears++;
  const pillar=e.getYear(),element=[...e.getYearNaYin()].at(-1);let printedGroups=0;
  for(const g of table.groups){
   const observed=diagramYear({system,mountain:g.mountains[0],sourceYearPillar:pillar,sourcePeriod});
   const derived=sourceOvercoming({system:'xieji-tomb-movement',mountain:g.mountains[0],sourceYearStem:pillar[0],sourcePeriod,candidateNaYinElement:element,constructionContext:'new-dwelling',coordinateKind:'year'});
   assert.equal(observed.listedInOrdinaryDiagram,derived.elementOvercomesMovement);if(observed.listedInOrdinaryDiagram)printedGroups++;
  }
  runtimeYears.push({GregorianRuntimeFixture:year,pillar,nayin:e.getYearNaYin(),nayinElement:element,printedGroups,sourceDateAdapterValidated:false});
 }
 assert.equal(new Set(runtimeYears.map(x=>x.pillar)).size,60);assert.equal(runtimeYears.reduce((n,x)=>n+x.printedGroups,0),50);
});
const unresolved=[];
await check('60 actual lunar EightChar month-pillar executions compare19 resolved printed month sets;one reading remains unfilled',()=>{
 for(let group=0;group<5;group++)for(let month=1;month<=12;month++){
  const year=1984+group+(month===12?1:0),solarMonth=(month%12)+1;
  const e=L.Solar.fromYmdHms(year,solarMonth,20,12,0,0).getLunar().getEightChar();e.setSect(2);lunarMonths++;
  assert.equal(e.getYear()[0],stems[group]);assert.equal(e.getMonth()[1],[...'寅卯辰巳午未申酉戌亥子丑'][month-1]);
  runtimeMonths.push({sourceYearStem:stems[group],sourceMonthOrdinal:month,modernFixture:[year,solarMonth,20],pillar:e.getMonth(),nayinElement:[...e.getMonthNaYin()].at(-1),calendarBoundaryAttestedByDiagram:false,solsticePhaseFromDateNotApplied:true});
 }
 for(const row of table.rows){
  const g=table.groups.find(x=>x.id===row.mountainGroup),actual=runtimeMonths.filter(x=>row.sourceYearStems.includes(x.sourceYearStem));
  const expected=actual.filter(x=>sourceOvercoming({system:'xieji-tomb-movement',mountain:g.mountains[0],sourceYearStem:x.sourceYearStem,sourcePeriod,candidateNaYinElement:x.nayinElement,constructionContext:'new-dwelling',coordinateKind:'month'}).elementOvercomesMovement).map(x=>x.sourceMonthOrdinal);
  if(row.monthReadingResolved)assert.deepEqual(row.sourceMonthOrdinals49,expected,row.id);
  else{assert.deepEqual(expected,[11,12]);unresolved.push({row:row.id,sourceReadingAlternatives:row.monthReadingAlternatives,derivedExpectedMonthOrdinals:expected,sourceRestoredFromRuntime:false});}
 }
 assert.equal(unresolved.length,1);
});
let yearContexts=0,monthContexts=0;
await check('1440 year and2880 month coordinate queries preserve table membership and a three-valued source reading rather than filling ambiguity',()=>{
 for(const g of table.groups)for(const mountain of g.mountains){
  for(const y of runtimeYears){const out=diagramYear({system,mountain,sourceYearPillar:y.pillar,sourcePeriod});assert.equal(out.practicalOutcome,null);assert.equal(out.calendarAdapter,null);yearContexts++;}
  for(const sourceYearStem of stems)for(let candidateMonthOrdinal=1;candidateMonthOrdinal<=12;candidateMonthOrdinal++){
   const out=diagramMonth({system,mountain,sourceYearStem,sourcePeriod,candidateMonthOrdinal});assert.equal(out.practicalOutcome,null);assert.equal(out.dateBound,false);monthContexts++;
  }
 }
 assert.equal(yearContexts,1440);assert.equal(monthContexts,2880);
 const query=n=>diagramMonth({system,mountain:'甲',sourceYearStem:'丙',sourcePeriod,candidateMonthOrdinal:n});
 assert.equal(query(11).listedAcrossReadingAlternatives,null);assert.equal(query(12).listedAcrossReadingAlternatives,true);assert.equal(query(1).listedAcrossReadingAlternatives,false);assert.equal(query(12).sourceMonthSetResolved,false);
});
await check('After-solstice metal exception stays in prior prose and is not overwritten by an ordinary diagram; unknown phase stays unknown',()=>{
 const pillar='壬申',after='after-current-winter-solstice-in-source-chou-period';
 const old=sourceOvercoming({system:'xieji-tomb-movement',mountain:'乾',sourceYearStem:'壬',sourcePeriod:after,candidateNaYinElement:'金',constructionContext:'new-dwelling',coordinateKind:'year'});assert.equal(old.elementOvercomesMovement,true);
 const ordinary=diagramYear({system,mountain:'乾',sourceYearPillar:pillar,sourcePeriod:after});assert.equal(ordinary.ordinaryDiagramPeriodApplicable,false);assert.equal(ordinary.listedInOrdinaryDiagram,false);assert.equal(ordinary.sourceConditionMatch,null);
 assert.equal(diagramYear({system,mountain:'乾',sourceYearPillar:pillar,sourcePeriod:null}).ordinaryDiagramPeriodApplicable,null);
});
await check('Strict coordinates, explicit nulls and returned copies avoid silent aliases, date adapters and mutation',()=>{
 const base={system,mountain:'甲',sourceYearStem:'甲',sourcePeriod,candidateMonthOrdinal:7};
 assert.equal(diagramYear({system,mountain:null,sourceYearPillar:'甲子',sourcePeriod}).listedInOrdinaryDiagram,null);
 assert.equal(diagramMonth({...base,candidateMonthOrdinal:null}).listedAcrossReadingAlternatives,null);
 for(const bad of[{...base,system:undefined},{...base,mountain:'子'},{...base,sourceYearStem:'甲乙'},{...base,sourcePeriod:undefined},{...base,candidateMonthOrdinal:13}])assert.throws(()=>diagramMonth(bad),TypeError);
 assert.throws(()=>diagramYear({system,mountain:'甲',sourceYearPillar:'甲丑',sourcePeriod}),TypeError);
 const a=diagramMonth(base);a.sourceMonthAlternatives[0].length=0;assert.deepEqual(diagramMonth(base).sourceMonthAlternatives,[[7,8]]);
});
await check('Released HTML, engine and all preceding reference implementations are byte-identical to the archived verified package',async()=>{
 const old=await read(resolve(w,'archives/v53-before-home-tomb-diagrams/PACKAGE_MANIFEST.json'));
 for(const f of['engine.js','Huyen_Hoc_Cac.html','site/index.html','research/home-source-tables/tomb-reference.mjs','research/liuyao-life-context/life-context-reference.mjs'])assert.equal(sha(await readFile(resolve(r,f))),old.files.find(x=>x.file===f).sha256);
});
const out={date:'2026-10-28',checks,summary:{movementCells:20,mountainLabels:24,sourceYearEntries:50,resolvedMonthSets:19,unresolvedMonthSets:1,actualLunarYearCharts:lunarYears,actualLunarMonthCharts:lunarMonths,privateYearContexts:yearContexts,privateMonthContexts:monthContexts,
 expandedPreviouslyReadPages:5,newHTTPRequests:0,newOriginalContainers:0,newSourcePages:0},runtimeYears,runtimeMonths,unresolved,
 consumerChanged:false,calendarAdapterEstablished:false,sourceAmbiguityRestored:false,practicalOutcomesValidated:false,wholeUnitsApplied:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
