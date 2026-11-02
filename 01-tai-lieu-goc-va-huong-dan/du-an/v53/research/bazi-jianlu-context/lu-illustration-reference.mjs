// Private structural projection of the explicitly illustrated 甲 case.
// No assumption about birth-year/day anchor, ordered 兩傍, strength or outcome.
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export function luIllustration({system,sourceStem,relevantBranches,allRelevantBranchesKnown}={}){
 if(system!=='WYG003-jia-lu-illustrated-branch-membership')throw TypeError('Explicit named illustration required');
 if(![...'甲乙丙丁戊己庚辛壬癸'].includes(sourceStem))throw TypeError('Explicit single source stem required');
 if(!Array.isArray(relevantBranches)||relevantBranches.some(x=>!branches.includes(x)))throw TypeError('Explicit source branch array required');
 if(typeof allRelevantBranchesKnown!=='boolean')throw TypeError('Explicit context completeness required');
 const observed=[...new Set(relevantBranches)],known=allRelevantBranchesKnown&&sourceStem==='甲',has=x=>observed.includes(x);
 const matched=known?{mingHe:has('寅')&&has('亥'),anHe:!has('寅')&&has('亥'),xuGong:!has('寅')&&has('丑')&&has('卯'),shiGong:has('寅')&&has('丑')&&has('卯')}:null;
 return{system,sourceStem,observed,illustratedStemSupported:sourceStem==='甲',allRelevantBranchesKnown,
  branchMembershipProjection:matched,sourcePositionalPremiseVerified:null,fullSourcePatternEstablished:null,
  birthPillarAnchor:null,practicalOutcome:null,sourceImages:[13,14]};
}
