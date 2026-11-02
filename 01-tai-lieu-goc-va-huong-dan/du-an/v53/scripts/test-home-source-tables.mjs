import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import{createRequire}from'node:module';import assert from'node:assert/strict';import vm from'node:vm';
import{tombMovement,sourceOvercoming}from'../research/home-source-tables/tomb-reference.mjs';
import{eightPalace}from'../research/home-source-tables/eight-palace-reference.mjs';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/home-source-tables'),q=resolve(r,'qa/home-source-tables'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex'),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
const data=await read(resolve(b,'TOMB_MOVEMENT_ROWS.json')),rules=await read(resolve(b,'OVERCOMING_RULE.json')),fig=await read(resolve(b,'MANUAL_FIGURES.json')),names=await read(resolve(b,'FIGURE_NAMES.json'));
const require=createRequire(import.meta.url),runtimeAudit=await read(resolve(r,'research/bazi-late-zi/VERIFICATION.json'));
await check('Original container, old native pages and actual lunar runtime retain audited bytes',async()=>{
 assert.equal(sha(await readFile(resolve(w,data.sourceContainer))),data.sourceSHA256);
 const manual=await read(resolve(b,'MANUAL_READINGS.json'));for(const x of manual.readings)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 for(const x of runtimeAudit.runtime)assert.equal(sha(await readFile(resolve(w,x.file))),x.sha256);
 assert.equal(JSON.parse(await readFile(resolve(w,'v46/node_modules/lunar-typescript/package.json'),'utf8')).version,'1.8.6');
});
const{Solar}=require(resolve(w,'v46/node_modules/lunar-typescript')),stems='甲乙丙丁戊己庚辛壬癸',branches='子丑寅卯辰巳午未申酉戌亥',system='xieji-tomb-movement',phases=['before-current-winter-solstice','after-current-winter-solstice-in-source-chou-period'];
let actualLunarCharts=0;const cache=new Map();function actualNaYin(pillar){if(cache.has(pillar))return cache.get(pillar);const i=Array.from({length:60},(_,i)=>i).find(i=>stems[i%10]+branches[i%12]===pillar);assert.notEqual(i,undefined);const year=1984+i,ec=Solar.fromYmdHms(year,7,1,12,0,0).getLunar().getEightChar();actualLunarCharts++;assert.equal(ec.getYear(),pillar);const result={pillar,fixture:{year,month:7,day:1,hour:12},actualPillar:ec.getYear(),actualNaYin:ec.getYearNaYin()};cache.set(pillar,result);return result;}
await check('20 printed base rows and5 explicit solstice exceptions match derived fiveZi pillar and actual NaYin',()=>{
 for(const g of data.rows)for(const x of g.yearGroupRows){const actual=tombMovement({system,mountain:g.mountains[0],sourceYearStem:[...x.yearStems][0],sourcePeriod:phases[0]});assert.equal(actual.pillar,x.derivedPillar);assert.equal(actual.movementElement,x.sourceMovementElement);assert.equal(actual.sourceAvoidElement,x.sourceAvoidElement);assert.equal(actualNaYin(x.derivedPillar).actualNaYin.at(-1),x.sourceMovementElement);}
 for(const x of data.afterSolsticeRows){const actual=tombMovement({system,mountain:'乾',sourceYearStem:[...x.sourceYearStems][0],sourcePeriod:phases[1]});assert.equal(actual.pillar,x.pillar);assert.equal(actual.movementElement,x.movementElement);assert.equal(actual.sourceAvoidElement,x.avoidElement);assert.equal(actualNaYin(x.pillar).actualNaYin.at(-1),x.movementElement);}
 assert.equal(actualLunarCharts,20);
});
let contexts=0,changes=0;
await check('All480 explicit mountain/yearstem/phase contexts match independent printedrows;40metalrows change',()=>{
 const all=[];for(const g of data.rows)for(const mountain of g.mountains){all.push(mountain);for(const sourceYearStem of stems){const pair=[];for(const sourcePeriod of phases){const i=(stems.indexOf(sourceYearStem)%5+(g.id==='metal'&&sourcePeriod===phases[1]?1:0))%5,expected=g.yearGroupRows[i],actual=tombMovement({system,mountain,sourceYearStem,sourcePeriod});assert.equal(actual.pillar,expected.derivedPillar);assert.equal(actual.movementElement,expected.sourceMovementElement);assert.equal(actual.sourceAvoidElement,expected.sourceAvoidElement);assert.equal(actual.calendarAdapter,null);assert.equal(actual.practicalOutcome,null);pair.push(actual);contexts++;}if(pair[0].pillar!==pair[1].pillar)changes++;}}
 assert.equal(new Set(all).size,24);assert.equal(contexts,480);assert.equal(changes,40);
});
await check('Unknown metal phase retains alternatives; source origin and named system are never inferred',()=>{
 const x=tombMovement({system,mountain:'乾',sourceYearStem:'甲',sourcePeriod:null});assert.equal(x.pillar,null);assert.deepEqual(x.sourceAlternatives.map(x=>x.pillar),['乙丑','丁丑']);
 for(const args of [{mountain:'乾',sourceYearStem:'甲',sourcePeriod:null},{system,mountain:'己',sourceYearStem:'甲',sourcePeriod:null},{system,mountain:'乾',sourceYearStem:2026,sourcePeriod:null},{system,mountain:'乾',sourceYearStem:'甲',sourcePeriod:'after-Lichun'}])assert.throws(()=>tombMovement(args),TypeError);
 assert.equal(tombMovement({system,mountain:null,sourceYearStem:'甲',sourcePeriod:null}).pillar,null);
});
let printedExamplePillars=0,exampleComparisons=0;const examples=[];
await check('All8 printed examplegroups match source overcoming relation with actual candidate NaYin',()=>{
 for(const ex of rules.printedExamples)for(const candidate of ex.candidatePillars){printedExamplePillars++;const ec=actualNaYin(candidate),element=ec.actualNaYin.at(-1),sourcePeriod=ex.context==='year-after-solstice-source-chou'?phases[1]:phases[0],actual=[];
  for(const g of data.rows)for(const mountain of g.mountains){const x=sourceOvercoming({system,mountain,sourceYearStem:ex.yearPillar[0],sourcePeriod,candidateNaYinElement:element,constructionContext:'new-dwelling',coordinateKind:ex.context.startsWith('month')?'month':'year'});if(x.sourceRuleApplies)actual.push(mountain);exampleComparisons++;assert.equal(x.practicalOutcome,null);}
  const expected=ex.expectedMountainGroup===null?[]:data.rows.find(x=>x.id===ex.expectedMountainGroup).mountains;assert.deepEqual(actual.slice().sort(),expected.slice().sort());examples.push({sourceYearPillar:ex.yearPillar,candidatePillar:candidate,actualNaYin:ec.actualNaYin,sourcePeriod,expectedMountains:expected,actualMountains:actual});
 }
 assert.equal(printedExamplePillars,13);assert.equal(exampleComparisons,312);
});
await check('Construction applicability and missing premises stay separate from arithmetic for all4 coordinate kinds',()=>{
 const base={system,mountain:'甲',sourceYearStem:'甲',sourcePeriod:phases[0],candidateNaYinElement:'金'};
 for(const coordinateKind of ['year','month','day','hour'])for(const constructionContext of['new-dwelling','new-grave','repair-foundation-unchanged','burial-existing-grave',null]){
 const x=sourceOvercoming({...base,coordinateKind,constructionContext});assert(x.elementOvercomesMovement);assert.equal(x.sourceRuleApplies,constructionContext===null?null:['new-dwelling','new-grave'].includes(constructionContext));assert.equal(x.practicalOutcome,null);}
 assert.equal(sourceOvercoming({...base,coordinateKind:'year',constructionContext:'new-dwelling',candidateNaYinElement:null}).sourceRuleApplies,null);
 for(const override of[{constructionContext:'renovation'},{candidateNaYinElement:'gold'},{coordinateKind:'gregorian-year'}])assert.throws(()=>sourceOvercoming({...base,coordinateKind:'year',constructionContext:'new-dwelling',...override}),TypeError);
});
const ctx={};ctx.window=ctx;vm.createContext(ctx);const engineBytes=await readFile(resolve(r,'engine.js'));vm.runInContext(engineBytes.toString(),ctx);const trig={'乾':'111','坎':'010','艮':'100','震':'001','巽':'110','離':'101','坤':'000','兌':'011'},sym={'天':'乾','水':'坎','山':'艮','雷':'震','風':'巽','火':'離','地':'坤','澤':'兌'},stageMask=[0,1,3,7,6,4,5,2],figureResults=[];
await check('384 manually read strokes match64 source names,64 actual hexNumber executions and source stage relations',()=>{
 assert.equal(fig.manualGlyphs,384);assert.equal(fig.ambiguousPixelSamples,65);assert.equal(fig.nonambiguousPixelConflictsWithManual.length,0);
 for(const x of fig.records){assert(x.directVisualQA);const printed=names.rows.find(n=>n.palace===x.palace).printedNameLabelsTopToBottom[x.stage],pure=printed.includes('為'),upper=pure?x.palace:sym[printed[0]],lower=pure?x.palace:sym[printed[1]];assert.equal(x.manualTopToBottom.join(''),trig[upper]+trig[lower]);
 const number=ctx.HHC_ENGINE.hexNumber(x.manualTopToBottom.slice().reverse().map(v=>v?7:8)),mask=parseInt(trig[upper],2)^parseInt(trig[lower],2);assert.equal(mask,stageMask[x.stage]);figureResults.push({palace:x.palace,stage:x.stage,printedName:printed,manualTopToBottom:x.manualTopToBottom.join(''),upper,lower,actualHexNumber:number,relationMask:mask});}
 assert.equal(figureResults.length,64);assert.equal(new Set(figureResults.map(x=>x.actualHexNumber)).size,64);
});
await check('All64 glyphs resolve to exact sourcepalace/stage; inputorientation and missing values are explicit',()=>{
 for(const x of fig.records){const bits=x.manualTopToBottom.slice().reverse(),before=JSON.stringify(bits),out=eightPalace({system:'xieji-eight-palace-figures',linesBottomToTop:bits});assert.equal(out.palace,x.palace);assert.equal(out.stage,x.stage);assert.equal(out.sourcePage,x.page);assert.equal(out.practicalOutcome,null);assert.equal(JSON.stringify(bits),before);}
 assert.equal(eightPalace({system:'xieji-eight-palace-figures',linesBottomToTop:null}).palace,null);
 for(const args of[{linesBottomToTop:[1,1,1,1,1,1]},{system:'universal',linesBottomToTop:null},{system:'xieji-eight-palace-figures',linesBottomToTop:[1,1,1,1,1,7]}])assert.throws(()=>eightPalace(args),TypeError);
});
await check('Earlier spelling differences preserved without altering source, model or userwebsite',async()=>{
 const p=await read(resolve(b,'PRIOR_NAME_PROBE.json'));assert.equal(p.literalNameMatches,62);assert.equal(p.predeclaredAliasMatches,1);assert.deepEqual(p.differences.map(x=>[x.rawName,x.actualName,x.actualNumber]),[['恒','恆',32]]);
 const html=await readFile(resolve(r,'Huyen_Hoc_Cac.html'));assert.equal(sha(html),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');for(const t of ['home-source-tables','tomb-reference','sourceOvercoming'])assert(!html.toString().includes(t));
});
const out={date:'2026-10-27',checks,summary:{actualLunarCharts,actualHHCHexNumberCalls:64,printedBaseRows:20,printedSolsticeRows:5,privateTombContexts:contexts,metalAfterSolsticeChanges:changes,printedExampleGroups:8,printedExamplePillars,printedExampleMountainComparisons:exampleComparisons,manualFigureGlyphs:384,manualFigureNames:64,ambiguousPixelSamplesManuallyResolved:65,newSourcePages:0,expandedPreviouslyReadPages:13,newHTTPRequests:0},runtimeFixtures:[...cache.values()],sourceExamples:examples,sourceFigures:figureResults,engineSHA256:sha(engineBytes),calendarAdapter:null,consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
