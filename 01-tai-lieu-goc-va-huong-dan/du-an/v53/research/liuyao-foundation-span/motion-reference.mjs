// Private dimensional boundary: a three-line printed diagram is not a six-line chart.
import{compile}from'../liuyao-foundations/liuyao-reference.mjs';
const names={'111':'乾','110':'兌','101':'離','100':'震','011':'巽','010':'坎','001':'艮','000':'坤'};
export function readMotion(values,scope){
 if(!scope||typeof scope!=='object'||Array.isArray(scope)||Object.getPrototypeOf(scope)!==Object.prototype||Object.getOwnPropertySymbols(scope).length||Object.keys(scope).length!==1||!Object.hasOwn(scope,'width')||![3,6].includes(scope.width))throw TypeError('Explicit diagram width3or6 is required.');
 if(!Array.isArray(values)||values.length!==scope.width||!Array.from(values).every(x=>[6,7,8,9].includes(x)))throw TypeError('Explicit numeric6/7/8/9 for every line, bottom-to-top.');
 const original=values.map(x=>x%2),changed=values.map(x=>x===6?1:x===9?0:x%2);
 if(scope.width===3)return{width:3,orientation:'bottom-to-top',original:{bits:original,trigram:names[original.join('')]},changed:{bits:changed,trigram:names[changed.join('')]},movingLines:values.flatMap((x,i)=>x===6||x===9?[i+1]:[]),sixLineChart:null,hexagramNumber:null,companionTrigram:null,consumerApplied:false,practicalOutcome:null};
 return{width:6,orientation:'bottom-to-top',sixLineChart:compile(values),consumerApplied:false,practicalOutcome:null};
}
