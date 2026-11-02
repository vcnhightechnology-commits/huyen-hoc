// Private named geographical source tables; no date, room or forecast adapter.
import {readFileSync} from 'node:fs';
const data=JSON.parse(readFileSync(new URL('SOURCE_TABLES.json',import.meta.url),'utf8'));

export function sourceTermDirection({system,sourceTerm}={}) {
 if(system!=='xieji-term-direction')throw new TypeError('Explicit source table required');
 if(sourceTerm===null)return{system,sourceTerm,mountain:null,modelDegrees:null,solarTermInstant:null,practicalOutcome:null};
 const row=data.source24TermRows.find(x=>x.sourceTerm===sourceTerm);
 if(!row)throw new TypeError('Explicit source term spelling required');
 return{system,sourceTerm,mountain:row.sourceMountain,modelDegrees:row.derivedModelCenterDegrees,
  angularModel:'equal24-zi-zero-clockwise-derived',solarTermInstant:null,qimenCycle:null,practicalOutcome:null};
}

export function geographicalNaJia({system,sourceCoordinate}={}) {
 if(system!=='xieji-geographical-najia')throw new TypeError('Explicit geographical system required');
 if(sourceCoordinate===null)return{system,sourceCoordinate,gua:null,lineStemBranches:null,practicalOutcome:null};
 if(typeof sourceCoordinate!=='string'||[...sourceCoordinate].length!==1)throw new TypeError('Explicit single source coordinate required');
 const row=data.geographicalNaJiaRows.find(x=>(x.gua+x.assignedCoordinates).includes(sourceCoordinate));
 if(!row)throw new TypeError('Coordinate not present in source table; no implicit chi/gua alias');
 return{system,sourceCoordinate,gua:row.gua,relatedCoordinates:[...(row.gua+row.assignedCoordinates)],
  sourcePages:[55,56],sourceOriginEstablished:false,lineStemBranches:null,practicalOutcome:null};
}
