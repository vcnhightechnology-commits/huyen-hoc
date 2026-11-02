from pathlib import Path
from hashlib import sha256
import json,ast,copy,sys
from PIL import Image,ImageChops
r=Path(__file__).resolve().parents[1];w=r.parent;q=r/'qa/pixel-verifier-hardening';rd=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest();plan=rd(q/'CHANGE_PLAN.json');previous=rd(w/'archives/v53-before-tuvi-lower-printed-cases/PACKAGE_MANIFEST.json');count=0
assert len(plan['records'])==2
for x in plan['records']:
 before=q/x['beforeFile'];after=q/x['afterFile'];actual=w/x['file'];assert sha(before)==x['beforeSHA256']and sha(after)==sha(actual)==x['afterSHA256'];assert before.read_bytes().replace(b'.getbbox()',b'.getbbox(alpha_only=False)')==after.read_bytes();assert x['beforeSHA256']==next(y for y in previous['files']if 'v53/'+y['file']==x['file'])['sha256']
 source=after.read_text(encoding='utf-8');compile(source,str(actual),'exec');nodes=[n for n in ast.walk(ast.parse(source))if isinstance(n,ast.Call)and isinstance(n.func,ast.Attribute)and n.func.attr=='getbbox'and isinstance(n.func.value,ast.Call)and isinstance(n.func.value.func,ast.Attribute)and isinstance(n.func.value.func.value,ast.Name)and n.func.value.func.value.id=='ImageChops'and n.func.value.func.attr=='difference'];assert len(nodes)==x['changedImageDifferenceCalls']
 for n in nodes:
  assert not n.args and len(n.keywords)==1 and n.keywords[0].arg=='alpha_only'and n.keywords[0].value.value is False
  e=copy.deepcopy(n);e.func.value=ast.Name(id='difference',ctx=ast.Load());expr=compile(ast.fix_missing_locations(ast.Expression(e)),'exact-source-bbox','eval')
  a=Image.new('RGBA',(2,2),(10,20,30,255));b=a.copy();assert eval(expr,{'difference':ImageChops.difference(a,b)})is None
  b.putpixel((1,1),(11,20,30,255));d=ImageChops.difference(a,b);assert d.getbbox()is None and eval(expr,{'difference':d})is not None
  b=a.copy();b.putpixel((1,1),(10,20,30,254));assert eval(expr,{'difference':ImageChops.difference(a,b)})is not None;count+=1
assert count==3
retained=rd(q/'PREDICATE_RESULTS.json');assert retained['scripts']==2 and retained['predicates']==3 and len(retained['checks'])==3 and all(x['realNativeCropUnmodifiedPass']and x['oneRGBPixelChangeSameAlphaRejected']and x['oneAlphaPixelChangeRejected']for x in retained['checks'])
# Both full source-results JSON files stayed byte-identical to the prior published source package.
for file in ['qa/bazi-food-six-pillars/SOURCE_RESULTS.json','qa/liuyao-b03-triad-clause/SOURCE_RESULTS.json']:assert sha(r/file)==next(x for x in previous['files']if x['file']==file)['sha256']
out=dict(date='2026-10-28',changedScripts=2,explicitAllChannelBBoxPredicates=3,onlyKeywordArgumentsChanged=True,priorScriptsBoundTo5069Manifest=True,tamperRGBSameAlphaRejected=True,tamperAlphaRejected=True,retainedRealNativeCropControlsPassed=3,fullSourceResultsByteUnchanged=2,newEngineCalls=0,sourceImagesChanged=False,consumerChanged=False)
p=q/'RESULTS.json'
if '--no-write'in sys.argv:assert rd(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
