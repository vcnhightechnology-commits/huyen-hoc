// Private source reference. No calendar, room-placement or predictive adapter.
const bits=Object.freeze({'坤':0,'震':1,'坎':2,'兌':3,'艮':4,'離':5,'巽':6,'乾':7});
const big=Object.freeze(['伏位','禍害','絶命','天醫','生氣','六煞','五鬼','延年']);
const small=Object.freeze(['輔弼','五鬼','絶命','福德','生氣','遊魂','天醫','絶體']);
const star=Object.freeze(['輔弼','廉貞','破軍','武曲','貪狼','文曲','巨門','祿存']);
const pages=Object.freeze([90,97,103,99,91,101,95,105]);
const named=Object.freeze(['不變','下一爻變','中一爻變','下二爻變','上一爻變','上下二爻變','上二爻變','三爻俱變']);
const favorable=Object.freeze({'geography-from-dragon':Object.freeze(['貪狼','巨門','武曲','廉貞']),
 'date-selection-from-facing':Object.freeze(['貪狼','巨門','武曲','文曲'])});
function validateTrigram(x){if(x!==null&&!(typeof x==='string'&&Object.hasOwn(bits,x)))throw new TypeError('Known trigram or explicit null required');}
export function youNian({system,origin,target,application=null}={}){
 if(!['xieji-da','xieji-xiao'].includes(system))throw new TypeError('Explicit named system required');
 validateTrigram(origin);validateTrigram(target);
 if(application!==null&&(!Object.hasOwn(favorable,application)||system!=='xieji-xiao'))throw new TypeError('Named application belongs to 小遊年 only');
 if(origin===null||target===null)return {system,origin,target,mask:null,relation:null,star:null,sourceContextRating:null,practicalOutcome:null};
 const mask=bits[origin]^bits[target],isSmall=system==='xieji-xiao';
 return {system,origin,target,mask,namedChangedLines:named[mask],relation:(isSmall?small:big)[mask],
  star:isSmall?star[mask]:null,sourcePage:mask===0?(isSmall?83:90):pages[mask],
  application,sourceContextRating:application===null?null:(favorable[application].includes(star[mask])?'吉':'凶'),
  ratingScope:application===null?null:'Quoted classification in this explicitly named source use; not a universal score or outcome.',
  practicalOutcome:null};
}
