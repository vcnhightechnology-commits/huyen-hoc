// Private reference for the retained Tianyige-attributed 陽宅十書 witness.
// Inputs are declared source coordinates, not a birth-date or floor-plan adapter.
const SYSTEM='YZSS-Tianyige-fuyuan-dayounian';
const mod=(n,k)=>(n%k+k)%k;
const numbers=Object.freeze({1:'坎',2:'坤',3:'震',4:'巽',6:'乾',7:'兌',8:'艮',9:'離'});
const male=Object.freeze({upper:1,middle:4,lower:7});
const female=Object.freeze({upper:5,middle:2,lower:8});
const order=Object.freeze(['乾','坎','艮','震','巽','離','坤','兌']);
const sequences=Object.freeze({乾:'六天五禍絕延生',坎:'五天生延絕禍六',艮:'六絕禍生延天五',
 震:'延生禍絕五天六',巽:'天五六禍生絕延',離:'六五絕延禍生天',坤:'天延絕生禍五六',兌:'生禍延絕六五天'});
const names=Object.freeze({生:'生氣',天:'天乙',延:'延年',禍:'禍害',六:'六煞',五:'五鬼',絕:'絕命'});
const stars=Object.freeze({生氣:['貪狼','木'],天乙:['巨門','土'],延年:['武曲','金'],禍害:['祿存','土'],
 六煞:['文曲','水'],五鬼:['廉貞','火'],絕命:['破軍','金'],伏位:['輔弼','木']});
const palaceElements=Object.freeze({乾:'金',兌:'金',艮:'土',坤:'土',坎:'水',離:'火',震:'木',巽:'木'});
const cycle='木火土金水';
function strict(input,keys){
 if(input===null||typeof input!=='object'||Object.getPrototypeOf(input)!==Object.prototype||
  Reflect.ownKeys(input).length!==keys.length||keys.some(k=>!Object.hasOwn(input,k))||
  Reflect.ownKeys(input).some(k=>!keys.includes(k)))throw new TypeError('Exact declared source-coordinate fields required');
 for(const k of keys){const d=Object.getOwnPropertyDescriptor(input,k);if(!d.enumerable||!Object.hasOwn(d,'value'))throw new TypeError('Plain enumerable data fields required');}
 if(input.system!==SYSTEM)throw new TypeError('Named source system required');
}
function trigram(x){if(x!==null&&!order.includes(x))throw new TypeError('Canonical trigram or explicit null required');}
export function sourceFuyuan(input){
 strict(input,['system','era','ordinal','sourceSex']);
 const {system,era,ordinal,sourceSex}=input;
 if(era!==null&&!Object.hasOwn(male,era))throw new TypeError('upper/middle/lower or explicit null required');
 if(ordinal!==null&&(!Number.isInteger(ordinal)||ordinal<1||ordinal>60))throw new TypeError('Source year ordinal1–60 or null required');
 if(sourceSex!==null&&!['male','female'].includes(sourceSex))throw new TypeError('Named source counting category or null required');
 const out={system,era,ordinal,sourceSex,rawPalaceNumber:null,centralRemap:null,palaceNumber:null,trigram:null,
  group:null,birthYearBoundary:null,modernDateAdapter:null,practicalOutcome:null};
 if(era===null||ordinal===null||sourceSex===null)return out;
 const raw=mod((sourceSex==='male'?male[era]:female[era])+(sourceSex==='male'?-1:1)*(ordinal-1)-1,9)+1;
 const number=raw===5?(sourceSex==='male'?2:8):raw;
 return {...out,rawPalaceNumber:raw,centralRemap:raw===5?(sourceSex==='male'?'男五寄坤':'女五寄艮'):null,
  palaceNumber:number,trigram:numbers[number],group:['坎','震','巽','離'].includes(numbers[number])?'東四':'西四'};
}
function relation(starElement,palaceElement){
 const a=cycle.indexOf(starElement),b=cycle.indexOf(palaceElement),d=mod(b-a,5);
 return ['same-element','star-generates-palace','star-controls-palace','palace-controls-star','palace-generates-star'][d];
}
export function sourceYouNian(input){
 strict(input,['system','anchorKind','origin','target']);
 const {system,anchorKind,origin,target}=input;
 if(!['birth-fuyuan','declared-source-gate','unknown'].includes(anchorKind))throw new TypeError('Explicit source anchor context required');
 trigram(origin);trigram(target);
 const out={system,anchorKind,origin,target,relation:null,star:null,starElement:null,palaceElement:null,
  elementRelation:null,sourcePDFPage:null,conditionalClassification:null,practicalOutcome:null,
  modernGeometryAdapter:null};
 if(anchorKind==='unknown'||origin===null||target===null)return out;
 const offset=mod(order.indexOf(target)-order.indexOf(origin),8);
 const name=offset===0?'伏位':names[sequences[origin][offset-1]], [star,element]=stars[name];
 return {...out,relation:name,star,starElement:element,palaceElement:palaceElements[target],
  elementRelation:relation(element,palaceElements[target]),sourcePDFPage:offset===0?59:58};
}
