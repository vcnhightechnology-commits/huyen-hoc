from pathlib import Path
import json
s=Path(__file__).resolve().parent;w=s.parent.parent
corpus=json.loads((w/'v53/research/bazi-food-source/CONTEXTS.json').read_text(encoding='utf-8'))
rows={x['id']:x for x in corpus['records']}
clauses=[
 ('balanced','FOOD-00-C04','此格要日主食神俱生旺無衝破'),
 ('declining','FOOD-00-C06','怕母子俱衰絶兩皆無成'),
 ('many','FOOD-00-C09','食神多者宜行印運'),
 ('few','FOOD-00-C09','食少者不宜是梟神奪食'),
 ('weak-owl','FOOD-00-C10','忌身衰梟旺'),
 ('wealth-many','FOOD-00-C11','柱中雖喜見財亦不宜多多則不清'),
 ('repeat-label','FOOD-00-C12','食神重見變為傷官'),
 ('restricted-void','FOOD-00-C12','若食神逢尅又遇空亡則不貴'),
 ('kill-wealth-chain','FOOD-00-C03','凡命遇財煞之地食神旺相煞被食制不敢為禍財被食生充裕不竭'),
 ('yang-hidden-officer','FOOD-00-C08','陽日食神暗合官星'),
 ('yin-hidden-seal','FOOD-00-C08','隂日食神暗合正印'),
 ('nonmanifest-pure','FOOD-00-C08','官印不要明顯但得食神純粹')]
fact_notes={
 'dayStrong':'source日主生旺;not automatically a phase,month label or visible-stem count',
 'foodStrong':'source食神生旺;not automatically from food presence',
 'effectiveClashOrDamageAbsent':'source無衝破;absence must be established,not supplied by missing input',
 'dayDecliningOrExtinct':'source母衰絶;frame/effectiveness requires separate interpretation',
 'foodDecliningOrExtinct':'source子衰絶;not simply zero visible food stems',
 'sourceFoodMany':'source多 within explicit same research quantity frame;no rawcount threshold',
 'sourceFoodFew':'source少 within same research quantity frame;not logical complement of多',
 'sealLuckEffective':'行印運 within relevant source context;not merely natal seal presence',
 'dayWeak':'source身衰;not derived as complement ofdayStrong',
 'owlStrong':'source梟旺;not simply a偏印stem present',
 'sourceWealthTooMany':'source財不宜多;no automatic numeric boundary',
 'repeatedFoodPatternCriterion':'source重見變為傷官 localpattern criterion;does not remap fixedTenGod relation',
 'foodEffectivelyRestricted':'source食神逢尅;not nominal control pair presence',
 'foodEffectivelyVoid':'source遇空亡 with own effectiveness prerequisites',
 'sourceWealthKillContext':'source命遇財煞之地;actual relative force/position not invented',
 'foodEffectiveRestraintOfKill':'source煞被食制;requires effective interaction',
 'foodEffectiveGenerationOfWealth':'source財被食生;requires effective interaction',
 'foodEffectiveHiddenOfficerCombination':'source陽日暗合官星;not nominalstem pair',
 'foodEffectiveHiddenSealCombination':'source陰日暗合正印;not nominalstem pair',
 'sourceOfficerSealNonmanifestCriterion':'source官印不要明顯;not inferred from visible stems alone',
 'foodPure':'source食神純粹;not raw count==1'}
rules=[
 ('balanced-core',['balanced'],['dayStrong','foodStrong','effectiveClashOrDamageAbsent'],'required-source-premises'),
 ('both-declining',['declining'],['dayDecliningOrExtinct','foodDecliningOrExtinct'],'source-negative-context'),
 ('many-food-seal-luck',['many'],['sourceFoodMany','sealLuckEffective'],'source-local-宜'),
 ('few-food-seal-luck',['few'],['sourceFoodFew','sealLuckEffective'],'source-local-不宜'),
 ('weak-day-strong-owl',['weak-owl'],['dayWeak','owlStrong'],'source-local-忌'),
 ('too-many-wealth',['wealth-many'],['sourceWealthTooMany'],'source-local-不清'),
 ('repeat-pattern-label',['repeat-label'],['repeatedFoodPatternCriterion'],'contextual-label-only-傷官'),
 ('food-restricted-and-void',['restricted-void'],['foodEffectivelyRestricted','foodEffectivelyVoid'],'source-negative-context'),
 ('wealth-kill-effective-chain',['kill-wealth-chain'],['sourceWealthKillContext','foodStrong','foodEffectiveRestraintOfKill','foodEffectiveGenerationOfWealth'],'source-positive-context'),
 ('yang-hidden-officer',['yang-hidden-officer','nonmanifest-pure'],['dayIsYang','foodEffectiveHiddenOfficerCombination','sourceOfficerSealNonmanifestCriterion','foodPure'],'source-positive-context'),
 ('yin-hidden-seal',['yin-hidden-seal','nonmanifest-pure'],['dayIsYin','foodEffectiveHiddenSealCombination','sourceOfficerSealNonmanifestCriterion','foodPure'],'source-positive-context')]
out={'date':'2026-10-28','system':'TMTH005-food-core-selected','source':'v53/research/bazi-food-source/CONTEXTS.json','clauseCount':len(clauses),'clauses':[],'coordinateFacts':['dayIsYang','dayIsYin'],'declaredResearchFactRegistry':fact_notes,'rules':[],'sourceManyFewNotComplements':True,'visibleCountDoesNotAdjudicateQuantityOrPurity':True,'outcomesValidated':False,'fullPatternCompiler':False}
for id,parent,text in clauses:
 p=rows[parent];i=p['text'].index(text);out['clauses'].append({'id':id,'parent':parent,'offsetWithinParent':i,'text':text,'digitalFolios':p['digitalFolios'],'allCharactersImageCollated':False,'sourceOutcomeValidated':False})
for id,ids,terms,stance in rules:out['rules'].append({'id':id,'sourceClauseIDs':ids,'all':terms,'sourceLocalStance':stance,'fullSourceConditionSetEstablished':False})
out['selectedCodepoints']=sum(len(x['text'])for x in out['clauses'])
(s/'SELECTED_PREDICATES.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'clauses':len(clauses),'parentContexts':len(set(x[1]for x in clauses)),'rules':len(rules),'declaredResearchFacts':len(fact_notes),'selectedCodepoints':out['selectedCodepoints']}))
