// Source-specific coordinate audit, not a whole pattern, rank, health or fortune classifier.
const stems=[...'甲乙丙丁戊己庚辛壬癸'],branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const valid=p=>typeof p==='string'&&[...p].length===2&&stems.includes(p[0])&&branches.includes(p[1])&&stems.indexOf(p[0])%2===branches.indexOf(p[1])%2;
const plain=x=>!!x&&typeof x==='object'&&Object.getPrototypeOf(x)===Object.prototype&&!Object.getOwnPropertySymbols(x).length;
const and=x=>x.includes(false)?false:x.includes(null)?null:true;
export function specialFoodCoordinates(context){
 const keys=['system','pillars','declaredFacts'];
 if(!plain(context)||Object.keys(context).length!==3||keys.some(k=>!Object.hasOwn(context,k))||Object.keys(context).some(k=>!keys.includes(k)))throw TypeError('Explicit named system,pillars and declaredFacts required.');
 if(!['TMTH005-zhuanshi','TMTH005-zhuanyin'].includes(context.system)||!Array.isArray(context.pillars)||context.pillars.length!==4||!Array.from(context.pillars).every(p=>p===null||valid(p))||!plain(context.declaredFacts))throw TypeError('Four explicit canonical pillars or null;plain research facts required.');
 const shi=context.system==='TMTH005-zhuanshi',factKeys=shi?['effectiveMonthGengControlsYearJia','dayStrong','effectiveCombination','effectiveMonthWealthOfficerPriority']:['dayStrong','sealStrong','effectiveHiddenCombination'];
 if(Object.entries(context.declaredFacts).some(([k,v])=>!factKeys.includes(k)||(v!==true&&v!==false&&v!==null)))throw TypeError('Only named boolean/null research premises.');
 const [year,month,day,hour]=context.pillars,targetDayStem=shi?'戊':'癸',dayMatches=day===null?null:day[0]===targetDayStem,hourMatches=hour===null?null:hour==='庚申',base=and([dayMatches,hourMatches]);
 const yearMonth=[['year',year],['month',month]],hits=[];
 if(shi){for(const[position,p]of yearMonth)if(p){if('甲丙'.includes(p[0]))hits.push({position,kind:'stem',symbol:p[0],sourceContainerPage:193});if('卯寅'.includes(p[1]))hits.push({position,kind:'branch',symbol:p[1],sourceContainerPage:193});}}
 else{for(const[position,p]of[['year',year],['month',month],['day',day],['hour',hour]])if(p){if('戊己丙'.includes(p[0]))hits.push({position,kind:'stem',symbol:p[0],sourceContainerPage:197});if('巳午寅'.includes(p[1]))hits.push({position,kind:'branch',symbol:p[1],sourceContainerPage:197});}}
 const counterShape=shi?and([year===null?null:year[0]==='甲',month===null?null:month[0]==='庚',base]):null;
 if(shi&&context.declaredFacts.effectiveMonthGengControlsYearJia===true&&counterShape!==true)throw TypeError('Declared source195counterexample requires actual year甲/month庚and戊day庚申hour shape.');
 return{system:context.system,pillars:context.pillars.slice(),coordinateBasis:'explicit-four-visible-pillar-scope-only;nohidden-stemorcalendarinference',baseDayStem:targetDayStem,sourceHour:'庚申',baseCoordinatesMatch:base,
  sourceLocalRawHits:hits,rawHitPresenceIsNotFinalSourceRejection:true,
  rawHitScannedPositions:shi?['year','month']:['year','month','day','hour'],
  rawHitScanComplete:(shi?[year,month]:context.pillars).every(x=>x!==null),source193YearMonthOnly:shi,
  difficultDayCoordinates:shi?(day===null?null:['戊午','戊寅'].includes(day)):null,
  source195ControlledJiaCounterexampleShape:counterShape,declaredEffectiveMonthGengControlsYearJia:shi?context.declaredFacts.effectiveMonthGengControlsYearJia??null:null,
  sourceProseVsPoemSealConflict:shi?{prose:'愛財星印綬',poem:'要無官印',resolution:null}:null,
  sourceProseAutumnWinterVsCommentaryNotExclusive:shi?{prose:'喜秋冬生',commentary:'不專秋冬生',automaticSeasonGate:null}:null,
  declaredResearchFacts:structuredClone(context.declaredFacts),sourceFullPatternEstablished:null,effectiveControlOrCombination:null,overallStrength:null,sourcePriorityResolved:null,practicalOutcome:null,consumerApplied:false};
}
