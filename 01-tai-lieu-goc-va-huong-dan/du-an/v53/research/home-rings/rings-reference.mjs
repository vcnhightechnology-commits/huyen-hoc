// Private source-coordinate reference. The numerical angular model is explicit;
// it does not calibrate a physical compass or infer an architectural outcome.
const names = Object.freeze([... '子癸丑艮寅甲卯乙辰巽巳丙午丁未坤申庚酉辛戌乾亥壬']);
const offsets = Object.freeze({regular: 0, middle: -7.5, seam: 7.5});
const uses = Object.freeze({regular: '定向', middle: '格龍', seam: '消砂納水'});
const rows = Object.freeze([
  Object.freeze({element:'水',pairs:Object.freeze(['坤申','壬子','乙辰']),branches:'申子辰'}),
  Object.freeze({element:'木',pairs:Object.freeze(['乾亥','甲卯','丁未']),branches:'亥卯未'}),
  Object.freeze({element:'火',pairs:Object.freeze(['艮寅','丙午','辛戌']),branches:'寅午戌'}),
  Object.freeze({element:'金',pairs:Object.freeze(['巽巳','庚酉','癸丑']),branches:'巳酉丑'})
]);
const norm = n => (n % 360 + 360) % 360;
const distance = (a,b) => Math.abs(norm(a-b+180)-180);
const knownRing = ring => {
  if (!Object.hasOwn(offsets,ring)) throw new TypeError('Explicit regular, middle or seam ring required');
};
const knownMountain = mountain => {
  if (mountain !== null && !names.includes(mountain)) throw new TypeError('Explicit known single mountain or null required');
};

export function pairedElement({system,ring,mountain}={}) {
  if (system !== 'xieji-double-mountain') throw new TypeError('Explicit named paired-mountain system required');
  knownRing(ring);
  if (ring === 'regular') throw new TypeError('Paired element lookup needs middle or seam coordinates');
  knownMountain(mountain);
  if (mountain === null) return {system,ring,mountain,pair:null,element:null,sourceUse:uses[ring],practicalOutcome:null};
  const row=rows.find(r=>r.pairs.some(p=>p.includes(mountain)));
  return {system,ring,mountain,pair:row.pairs.find(p=>p.includes(mountain)),element:row.element,
    triadBranches:row.branches,sourceUse:uses[ring],sourcePages:[14,15],practicalOutcome:null};
}

export function namedCenter({system,angularModel,ring,mountain}={}) {
  if (system !== 'xieji-three-needles' || angularModel !== 'equal24-zi-zero-clockwise')
    throw new TypeError('Named system and explicit derived angular model required');
  knownRing(ring); knownMountain(mountain);
  return {system,angularModel,ring,mountain,
    regularModelDegrees:mountain===null?null:norm(names.indexOf(mountain)*15+offsets[ring]),
    offsetDegrees:offsets[ring],sourceOffsetHalfPositions:offsets[ring]/7.5,
    sourceUse:uses[ring],physicalNorthCalibration:null,practicalOutcome:null};
}

export function ringCoordinates({system,angularModel,endpointPolicy,ring,regularModelDegrees,uncertaintyDegrees}={}) {
  if (system !== 'xieji-three-needles' || angularModel !== 'equal24-zi-zero-clockwise' || endpointPolicy !== 'both-at-touch')
    throw new TypeError('Explicit named system, derived model and endpoint convention required');
  knownRing(ring);
  if (!Number.isFinite(uncertaintyDegrees) || uncertaintyDegrees<0 || uncertaintyDegrees>180)
    throw new TypeError('Explicit angular uncertainty from0 through180 required');
  if (regularModelDegrees!==null && (!Number.isFinite(regularModelDegrees) || regularModelDegrees<0 || regularModelDegrees>360))
    throw new TypeError('Regular model coordinate from0 through360 or null required');
  const point=regularModelDegrees===null?null:norm(regularModelDegrees);
  const possible=point===null?[]:names.flatMap((mountain,index)=>{
    const center=norm(index*15+offsets[ring]);
    if (distance(center,point)>uncertaintyDegrees+7.5+1e-10) return [];
    const element=ring==='regular'?null:pairedElement({system:'xieji-double-mountain',ring,mountain});
    return [{mountain,regularModelCenterDegrees:center,pair:element?.pair??null,element:element?.element??null}];
  });
  const pairs=[...new Set(possible.map(x=>x.pair).filter(x=>x!==null))];
  const elements=[...new Set(possible.map(x=>x.element).filter(x=>x!==null))];
  return {system,angularModel,endpointPolicy,ring,regularModelDegrees:point,uncertaintyDegrees,
    possible,mountain:possible.length===1?possible[0].mountain:null,possiblePairs:pairs,possibleElements:elements,
    pair:pairs.length===1?pairs[0]:null,element:elements.length===1?elements[0]:null,
    sourceUse:uses[ring],physicalNorthCalibration:null,practicalOutcome:null};
}
