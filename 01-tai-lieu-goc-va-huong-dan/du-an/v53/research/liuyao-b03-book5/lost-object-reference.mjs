import {figureAvailability} from '../liuyao-b03-figures/availability-reference.mjs';
const roles={cash:{kin:'妻財',page:12,sourceObject:'財',caution:null},
 boat:{kin:'父母',page:17,sourceObject:'舟',caution:'妻財'},vehicle:{kin:'父母',page:17,sourceObject:'車',caution:'妻財'},
 garment:{kin:'父母',page:17,sourceObject:'衣',caution:'妻財'},headwear:{kin:'父母',page:17,sourceObject:'帽',caution:'妻財'},
 document:{kin:'父母',page:17,sourceObject:'文章',caution:'妻財'},memorial:{kin:'父母',page:17,sourceObject:'奏疏',caution:'妻財'},
 bird:{kin:'子孫',page:17,sourceObject:'飛禽',caution:'父母'},beast:{kin:'子孫',page:17,sourceObject:'走獸',caution:'父母'}};
export function lostObjectCandidates(values,context,...extra){
 if(extra.length||!context||typeof context!=='object'||Array.isArray(context)||Object.getOwnPropertySymbols(context).length||
  Object.keys(context).some(k=>!['sourceContext','objectKind'].includes(k))||context.sourceContext!=='B03-volume11-lost-objects'||
  typeof context.objectKind!=='string'||!Object.hasOwn(roles,context.objectKind))
  throw TypeError('Explicit B03-volume11-lost-objects and one supported historical object kind required.');
 const role=roles[context.objectKind],availability=figureAvailability(values,role.kin);
 return {schema:'hhc.liuyao.B03.lost-object-candidates.v1',sourceID:'B03-book5',
  sourceContext:context.sourceContext,objectKind:context.objectKind,role:{...role},
  categoryIDsAreEditorialNormalization:true,notEveryLostObjectIsWealth:true,availability,
  sourceCautionMovingLines:role.caution===null?null:availability.chart.lines.filter(l=>l.moving&&l.kin===role.caution)
   .map(l=>({line:l.line,primaryKin:l.kin,branch:l.branch,actualChange:structuredClone(l.changed),
    sourcePDFPage:17,structuralPremiseOnly:true,outcome:null})),
  effectiveUseGodSelection:null,searchLocation:null,suspectIdentity:null,recoveryDate:null,
  recoveryOutcome:null,fullStrengthAdjudication:null,consumerApplied:false,predictedEvent:null};
}
