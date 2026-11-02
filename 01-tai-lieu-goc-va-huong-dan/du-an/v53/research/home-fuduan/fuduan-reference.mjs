/** Internal source arithmetic only. Xieji vol36 describes then criticizes this system.
 * No Gregorian epoch, astronomical mansion, auspiciousness, or ITKC adapter.
 */
export const SOURCE_ID='xieji-ssid12152602-vol36-selected';
export const FRAME_ID='seven-declared-720-step-blocks-28-mansions';
const order=Object.freeze(Array.from('虛危室壁奎婁胃昴畢觜參井鬼柳星張翼軫角亢氐房心尾箕斗牛女'));
const starts=Object.freeze(Array.from('虛奎畢鬼翼氐箕'));
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
function frame(o,keys) {
  return o!==null && typeof o==='object' && !Array.isArray(o)
    && own(o,'sourceID') && o.sourceID===SOURCE_ID
    && own(o,'frameID') && o.frameID===FRAME_ID
    && Object.keys(o).every(k=>keys.includes(k));
}
function integer(n,min,max,name) {
  if (!Number.isInteger(n)||n<min||n>max) throw new RangeError(name);
}
function at(yuan,step) { return order[(order.indexOf(starts[yuan-1])+step)%28]; }
function result(fields) {
  return Object.freeze({status:'cited-and-criticized-source-arithmetic',
    useForRecommendations:false,calendarDate:null,auspiciousness:null,...fields});
}
export function sourceMansionAt(o) {
  if (!frame(o,['sourceID','frameID','yuan','dayOffset','hourIndex'])) return null;
  integer(o.yuan,1,7,'yuan');integer(o.dayOffset,0,59,'dayOffset');integer(o.hourIndex,0,11,'hourIndex');
  return result({yuan:o.yuan,dayOffset:o.dayOffset,hourIndex:o.hourIndex,
    mansion:at(o.yuan,o.dayOffset*12+o.hourIndex)});
}
export function sourceBlockBoundary(o) {
  if (!frame(o,['sourceID','frameID','yuan'])) return null;
  integer(o.yuan,1,7,'yuan');
  const nextYuan=o.yuan%7+1,last=at(o.yuan,719),continuousNext=at(o.yuan,720),declaredNext=starts[nextYuan-1];
  const forwardGap=(order.indexOf(declaredNext)-order.indexOf(continuousNext)+28)%28;
  return result({yuan:o.yuan,nextYuan,last,continuousNext,declaredNext,forwardGap,seamless:forwardGap===0});
}
