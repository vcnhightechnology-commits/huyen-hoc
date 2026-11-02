"""A source-ambiguity ledger only; no engine batch or full返哺classifier."""
from pathlib import Path
from hashlib import sha256
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
assert not(B/'SOURCE_DIRECTION_REVIEW.json').exists()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
c=next(r for r in read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']if r['id']=='FOOD-00-C22')
files=['v53/research/four-items/sources/KR3g0042_005.txt','v53/research/bazi-relations/sources/KR3g0042_005.txt']
assert (W/files[0]).read_bytes()==(W/files[1]).read_bytes()
role_order=['year','month','day','hour'];adjacent=[[role_order[i],role_order[i-1]]for i in range(1,4)]
all_later_earlier=[[role_order[i],role_order[j]]for i in range(1,4)for j in range(i)]
review={'date':'2026-10-30','status':'source-role-and-quantifier-ambiguity-reviewed;no-reference-implemented',
 'parent':c,'sourceVoice':'理愚歌 plus following gloss','selectedGlossLiteral':'返哺者年月日時皆自下食上見天乙官印吉煞主貴',
 'sourceIdentities':[ident(W/'v53/research/bazi-food-source/CONTEXTS.json'),*[ident(W/f)for f in files]],
 'retainedFullSourceImagesReexamined':[ident(W/f'v53/research/bazi-food-source/p{n}.png')for n in [178,179]],
 'quotedTextDoesNotPrintAnExplicitFourPillarExample':True,
 'directionHypotheses':[{'id':'lower-as-relation-root','meaning':'下食上 read as lower/later pillar taking upper/earlier pillar as food','sourceAdjudicated':False},
 {'id':'upper-as-relation-root','meaning':'Editorial counter-reading of return-feeding presentation; not a source correction','sourceAdjudicated':False}],
 'edgeScopeHypotheses':[{'id':'adjacent','laterEarlierRolePairs':adjacent,'sourceAdjudicated':False},
 {'id':'all-later-earlier','laterEarlierRolePairs':all_later_earlier,'sourceAdjudicated':False}],
 'selectedDirection':None,'selectedEdgeScope':None,'sourceYearOrDayRootDefault':None,
 'otherOpenPremises':['子建/建官 meanings and whether quoted lines/gloss share the same operational scope','天乙/官印/吉煞 precise list sense and anchor/frame','strength/effectiveness and full source outcome'],
 'retainedSearch':{'scope':'UTF8txt within v53/research and two retained source trees; no claim the full scans/corpus were read again',
 'matchesInDistinctFullTextWitnesses':1,'twoFullTextPathsAreByteDuplicates':True,
 'thirdTextHit':'v53/research/bazi-food-source/RETAINED_DIGITAL_SECTION.txt',
 'thirdHitIsSameSectionExtractionNotIndependentWitness':True,'independentWitnessFound':False},
 'currentParentMatrix':ident(W/'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json'),
 'currentMatrixCountsUnchanged':[49,41,0],'C22SelectedModuleLinkAdded':False,
 'newEngineCalls':0,'newHTTPBodies':0,'newSourcePositions':0,'consumerChanged':False,'wholeContextApplied':False,'wholeCatalogueCompleted':False,
 'next':'Keep both direction and edge-scope axes explicit if a future comparison is made. Seek a defined explanatory witness or directly printed example before choosing a classifier; switch to independent C35 source conditions meanwhile. Do not use synthetic engine agreement to resolve the original grammar.'}
assert review['selectedGlossLiteral']in c['text']
(B/'SOURCE_DIRECTION_REVIEW.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'parent':'FOOD-00-C22','directionAdjudicated':False,'edgeScopeAdjudicated':False,'newEngineCalls':0,'newIndependentWitnesses':0}))
