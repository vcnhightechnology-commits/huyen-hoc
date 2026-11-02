import{sourceLayerCoordinate as inspect}from'../research/home-yangzhai-shishu/layer-coordinate-reference.mjs';import assert from'node:assert/strict';import{writeFile}from'node:fs/promises';
const checks=[];function check(name,fn){fn();checks.push({name,ok:true});}
const base={system:'YZSS-Tianyige-selected-chuangong',countBasis:'ordered-source-jin',layerIndex:1,firstElement:'水',declaredOrigin:'outer-main-gate',boundary:{hasWall:false,hasDoor:false}};let coordinateContexts=0,boundaryContexts=0;
check('Directsource93waterstartfivepositionspreserved;secondfiveuseexplicit周而復始withnoautomaticstarheightoutcome',()=>{
 const expected=['水','木','火','土','金','水','木','火','土','金'];for(let i=1;i<=10;i++){const out=inspect({...base,layerIndex:i});assert.equal(out.element,expected[i-1]);assert.equal(out.cycleFromDeclaredOtherStartIsEditorialApplicationOfSourceCycle,false);assert.equal(out.localStarName,null);assert.equal(out.houseHeightAdvice,null);assert.equal(out.practicalOutcome,null);coordinateContexts++;}
});
check('Otherdeclaredstartsareeditorialapplicationofsourcecycleandcannotbepresentedasfiveindependentlyprintedstarttables',()=>{
 const generation={木:'火',火:'土',土:'金',金:'水',水:'木'};
 for(const start of['木','火','土','金']){let expected=start;for(let i=1;i<=10;i++){const out=inspect({...base,firstElement:start,layerIndex:i});assert.equal(out.element,expected);assert(out.cycleFromDeclaredOtherStartIsEditorialApplicationOfSourceCycle);expected=generation[expected];coordinateContexts++;}}
});
check('Wallplusdoorrequireslocalorigin;neithermakesouteroriginexplicit;allmixedorunknownboundaryframesstayunadjudicated',()=>{
 for(const wall of[true,false,null])for(const door of[true,false,null])for(const origin of['outer-main-gate','current-enclosure','unknown']){const x=inspect({...base,boundary:{hasWall:wall,hasDoor:door},declaredOrigin:origin}),required=wall===true&&door===true?'current-enclosure':wall===false&&door===false?'outer-main-gate':null;assert.equal(x.sourceBoundaryFrameRequired,required);const expected=required===null||origin==='unknown'?null:origin===required;assert.equal(x.originPremiseMatches,expected);assert.equal(x.element,expected===true?'水':null);boundaryContexts++;}
});
check('Modernverticalstoreysneverstandinsourcelayercount;unknowncountdoesnotbecomefalseorpositive',()=>{
 for(const origin of['outer-main-gate','current-enclosure','unknown']){const x=inspect({...base,countBasis:'modern-vertical-storeys',declaredOrigin:origin});assert.equal(x.countMeaningMatches,false);assert.equal(x.selectedPremisesMatch,false);assert.equal(x.element,null);assert.equal(x.modernBuildingGeometryAdapterEstablished,false);}
 const x=inspect({...base,countBasis:'unknown'});assert.equal(x.selectedPremisesMatch,null);assert.equal(x.element,null);
});
check('Initialelementandlocaldepthmustbeindependentlydeclared;resetdoesnotguessnewfirstelementorcalculatedroomcoordinates',()=>{
 const local={...base,boundary:{hasWall:true,hasDoor:true},declaredOrigin:'current-enclosure'};for(const input of[{...local,firstElement:null},{...local,layerIndex:null}]){const x=inspect(input);assert.equal(x.selectedPremisesMatch,true);assert.equal(x.element,null);assert.equal(x.sourceFirstElementDerivationEstablished,false);assert.equal(x.fullChuangongMethodEstablished,false);}
});
check('Sourceonlybounded1to10andstrictkeysrejectcoercion,extraautomatednorth,flooraliases,symbols,nonenumerablefieldsandinvalidtruthvalues',()=>{
 const extra={...base};Object.defineProperty(extra,'autoNorth',{value:0});for(const x of[null,{},[],extra,{...base,[Symbol('x')]:true},{...base,layerIndex:0},{...base,layerIndex:11},{...base,layerIndex:1.5},{...base,layerIndex:'1'},{...base,firstElement:'Thuỷ'},{...base,countBasis:'floor'},{...base,boundary:{hasWall:true,hasDoor:'true'}},{...base,boundary:{hasWall:true,hasDoor:true,wallThickness:1}},{...base,system:'universal-fengshui'}])assert.throws(()=>inspect(x));
 const a=inspect(base);a.boundary.hasWall=true;assert.equal(inspect(base).boundary.hasWall,false);assert.equal(inspect(base).consumerApplied,false);
});
const out={date:'2026-10-28',checks,summary:{coordinateContexts,boundaryContexts,directWaterStartFirstCycleCells:5,secondCycleCellsFromSourceCycleRule:5,otherDeclaredStartContextsExplicitlyDerived:40,newEngineCalendarOrChartExecutions:0,engineComparisonNotApplicable:'NoHHCastronomy/calendar/duNienorgeometryalgorithmchanged;sourcecoordinatesareprivateboundednewcomponent.',modernRoomOrFloorAdapter:false,sourceOutcomesValidated:false,consumerChanged:false,wholeCatalogueCompleted:false}};
await writeFile(new URL('../qa/home-yangzhai-shishu/LAYER_RESULTS.json',import.meta.url),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out));
