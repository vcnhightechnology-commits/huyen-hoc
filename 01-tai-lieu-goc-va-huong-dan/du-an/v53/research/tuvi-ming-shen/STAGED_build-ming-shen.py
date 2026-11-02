from pathlib import Path
from PIL import Image,ImageChops
import json
b=Path('tmp/tuvi-juan2-staging');read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));write=lambda n,x:(b/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(b/'QA_IMAGES.json')
for x in qa['records']:
 assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox()is None;x['actuallyViewed']=True;x['pixelIdenticalToSourceCrop']=True
write('QA_IMAGES.json',qa)
system='NAJ-4468520-juan3-declared-month-hour-ming-shen'
write('MING_SHEN_READINGS.json',dict(date='2026-10-28',system=system,canvas=73,records=[dict(id='month-anchor',literal='大抵入命俱從寅上起正月順數至本生月上'),dict(id='ming-hour',literal='又自人生月上起子時逆至本生時安命'),dict(id='shen-hour',literal='順至本生時安身'),dict(id='examples',literal='假如正月生子時就在寅宮安命身丑時逆轉丑安命順去卯安身寅時逆轉子安命順至辰安身餘宮倣此'),dict(id='leap-premise',literal='又若閏正月生寅時逆轉子安命順至辰安身'),dict(id='leap-general',literal='凡有閏月俱要依此為例')],selectedClausesActuallyViewed=True,allGlyphsCollated=False,leapFirstMonthHourYinExampleAttested=True,generalLeapMonthMappingForAllMonthsResolved=False,monthSourceRole='birth lunar month ordinal',hourRole='declared hour branch, conversion from clock unimplemented',numericalBranchIndexIsEditorial=True,sourceOutcomeValidated=False))
# Crucial leap example is printed. Preserve it but do not extrapolate an all-month leap policy.
write('FLANKING_LABEL_DISPOSITIONS.json',dict(date='2026-10-28',canvas=61,sourceCountClaim=dict(favourable=6,adverse=3),rows=[dict(id=k,sourceLabel=label,sourceGroup=g,tokenNames=names,sourceSimplePairResolved=pair,geometryImplementedInThisScope=False,fullPatternImplemented=False,reason=reason)for k,label,g,names,pair,reason in [
 ('purple-fu','紫府夾命','夾貴',['紫微','天府'],True,'Explicit two named stars, full contextual conditions remain open.'),
 ('ke-quan-lu','科權祿夾命','夾貴',['科','權','祿'],False,'Three transformation labels in six-type list; distribution/anchor/assignment cannot be inferred by choosing any two.'),
 ('sun-moon','日月夾命','夾貴',['太陽','太陰'],True,'Geometry implemented only in previous named scope; no new runtime counted here.'),
 ('chang-qu','昌曲夾命','夾貴',['文昌','文曲'],True,'Geometry implemented only in previous named scope; no new runtime counted here.'),
 ('kui-yue','魁鉞夾命','夾貴',['天魁','天鉞'],True,'Names editorially expanded from printed abbreviated pair; full conditions open.'),
 ('zuo-you','左右夾命','夾貴',['左輔','右弼'],True,'Names editorially expanded; full conditions open.'),
 ('void-robbery','劫空夾命','夾敗',['地劫','天空'],False,'Printed 劫空 needs same-source identity mapping; do not silently choose current engine Địa Không.'),
 ('fire-bell','火鈴夾命','夾敗',['火星','鈴星'],True,'Full conditions and source adverse outcomes not inferred.'),
 ('yang-tuo','羊陀夾命','夾敗',['擎羊','陀羅'],True,'Source explicitly allows 吉星/廟旺/化忌 qualifications; sourceGroup does not determine result.')]],sourceGroupIsHistoricalLabelNotOutcome=True,wholeSectionApplied=False))
module="""const systemName='NAJ-4468520-juan3-declared-month-hour-ming-shen',branches=[...'子丑寅卯辰巳午未申酉戌亥'];
export function sourceMingShen({system,monthOrdinal,hourBranch,leapMonth}={}){
 if(system!==systemName)throw new TypeError('Named source required');
 if(monthOrdinal!==null&&(!Number.isInteger(monthOrdinal)||monthOrdinal<1||monthOrdinal>12))throw new TypeError('Declared lunar month1..12 or explicit null required');
 if(hourBranch!==null&&!branches.includes(hourBranch))throw new TypeError('Declared canonical hour branch or explicit null required');
 if(![true,false,null].includes(leapMonth))throw new TypeError('Explicit leap flag or null required');
 const known=monthOrdinal!==null&&hourBranch!==null,printedLeapExample=leapMonth===true&&monthOrdinal===1&&hourBranch==='寅';
 const applicable=known&&(leapMonth===false||printedLeapExample),h=known?branches.indexOf(hourBranch):null,monthAnchor=monthOrdinal===null?null:(monthOrdinal+1)%12;
 const ming=applicable?(monthAnchor-h+12)%12:null,shen=applicable?(monthAnchor+h)%12:null;
 return{system,monthOrdinal,hourBranch,leapMonth,sourceMonthAnchor:monthAnchor===null?null:branches[monthAnchor],mingBranch:ming===null?null:branches[ming],shenBranch:shen===null?null:branches[shen],
  resolved:applicable,resolutionBasis:!known?'missing-month-or-hour':leapMonth===null?'leap-status-unknown':leapMonth===true?(printedLeapExample?'printed-leap-month1-hourYin-example':'general-leap-policy-unresolved'):'printed-regular-month-hour-rule',
  sourceGeneralLeapPolicyResolved:false,clockToHourBranchAdapterImplemented:false,calendarConversionImplemented:false,sourceOutcomesValidated:false,practicalOutcome:null};
}
"""
(b/'source-ming-shen.mjs').write_text(module,encoding='utf-8')
print('Source lunar month/hour API preserves explicit leap1-hourYin example; no general leap policy extrapolated. Nine flanking labels retain source scope.')
