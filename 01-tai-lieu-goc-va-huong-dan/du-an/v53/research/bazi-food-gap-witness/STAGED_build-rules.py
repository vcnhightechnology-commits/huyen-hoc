from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
w=Path.cwd();b=w/'tmp/bazi-food-gap-witness-staging'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda name,x:(b/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
source=w/'v53/research/bazi-food-source/CONTEXTS.json';allctx=read(source)
contexts=[x for x in allctx['records']if x['unit']in ['FOOD-01','FOOD-02']]
assert len(contexts)==17
write('SELECTED_CONTEXTS.json',dict(date='2026-10-28',source=source.relative_to(w).as_posix(),sha256=sha(source),records=contexts,allImageCharactersCollated=False))
sets=[dict(id='feitian-four-prose',parent='FOOD-01-C02',days=['庚子','壬子','辛亥','癸亥'],kind='four-day-prose',
    additionalConditionsNotAutomaticallyEvaluated=['十月十一月','冬水純陰','柱無財官','effective-repeated-branch-clash','effective-attraction-and-no-restraint']),
 dict(id='daochong-two-prose',parent='FOOD-02-C02',days=['丙午','丁巳'],kind='two-day-prose',
    additionalConditionsNotAutomaticallyEvaluated=['夏月純陽','多有力','effective-clash-and-binding','priority-over-officer-kill-alternative']),
 dict(id='daochong-six-quoted',parent='FOOD-02-C05',days=['丙午','丙寅','丙戌','丁巳','丁未','丁卯'],kind='another-quoted-six-day-voice',
    additionalConditionsNotAutomaticallyEvaluated=['陽倒衝陰正衝','三合寅午戌全或三丙字','喜印生助忌煞混雜'])]
cases=[]
def add(id,day,branch,target,officer,attract,restrain,parent,**extra):
 cases.append(dict(id=id,day=day,repeatedBranch=branch,virtualTargetBranch=target,sourceOfficerStem=officer,
    printedAttractionBranchPool=attract,printedRestraintBranchPool=restrain,parentContext=parent,
    canonicalStemRoleReadingsEditorial=True,sourceVirtualTargetIsNotActualPillar=True,**extra))
add('fei-gengzi','庚子','子','午','丁',['未','寅','戌'],['丑'],'FOOD-01-C04',
    attractionScope='case-specific',visibleStemMentions=['丁','丙','戊'],stemMentionScope='sourcecase4-not-universal-category-ban')
add('fei-renzi','壬子','子','午','己',['未','寅','戌'],['丑'],'FOOD-01-C05',
    attractionScope='editorial-coordinate-reference-from喜忌同庚子;notallconditionsinherited',visibleStemMentions=['丁'],stemMentionScope='laterC07specific丁wealthmention;notallwealthtokens')
for id,day,officer,focus in [('fei-xinhai','辛亥','丙','丙'),('fei-guihai','癸亥','戊','戊')]:
 add(id,day,'亥','巳',officer,['申','酉','丑'],['寅'],'FOOD-01-C06',
    attractionScope='joint辛癸sourceparagraph',visibleStemMentions=['丙','戊'],
    stemMentionScope='jointC06mentions;C07focuskeptseparate',laterFocusedStem=focus,laterFocusedBranch='巳',severityPriorityAutomaticallyResolved=False)
for id,day,branch,target,officer,restrain in [('dao-bingwu','丙午','午','子','癸',['未']),('dao-dingsi','丁巳','巳','亥','壬',['申','辰'])]:
 add(id,day,branch,target,officer,['丑','寅','申','辰','卯','未'],restrain,'FOOD-02-C02',
    attractionScope='unassigned-collective-pool;notpartitionedintocase-specificbindingrules',
    visibleStemMentions=['壬','癸'],stemMentionScope='joint亥壬子癸clause;notfinalpatternrejection',
    separateC04OfficerKillAlternativePriorityUnresolved=True)
assert len(cases)==6
write('DAY_AND_COORDINATE_TABLES.json',dict(date='2026-10-28',systemPrefix='TMTH005-',daySets=sets,mechanismCases=cases,
    finalDaoComment=dict(parent='FOOD-02-C07',days=['丙午','丁巳'],sourcePreference='此二日倒衝為正',
       notAutomaticallyDeletingSixDayQuote=True),
    finalFeiComment=dict(parent='FOOD-01-C10',label='傷官',positive=['庚子','辛亥'],negative=['壬子','癸亥'],
       notAnAlternativeTwoDayEligibilityList=True),
    allConditionsApplied=False,sourceOutcomeValidated=False))
notes={
 'FOOD-01-C01':('heading','飛天祿馬 heading.'),
 'FOOD-01-C02':('partial-day-membership','Four days only. 冬水純陰 and 十/十一月 are source conditions, not automatically equated with a calendar policy.'),
 'FOOD-01-C03':('partial-coordinate-scope','Other year/month/hour branch repetition and binding/restraint references; 多/併衝/合住 not proved by visible count.'),
 'FOOD-01-C04':('partial-specific-mechanism','庚子→午中丁, 未寅戌 attraction, 丑 restraint, visible 丁丙午戊 raw coordinates. No actual invisible午pillar created.'),
 'FOOD-01-C05':('partial-officer-coordinate','壬子→午中己. 喜忌同 does not silently copy every literal 庚token into 壬 case.'),
 'FOOD-01-C06':('partial-joint-coordinate','辛亥/癸亥→巳中丙/戊; joint attraction/mentions retained with later narrower focus.'),
 'FOOD-01-C07':('parallel-conditional-voice','庚water-too-strong, 庚丑alternative, 壬丁wealth, 辛/癸focused忌 and 餘忌稍輕 retained; no automatic severity/strength adjudication.'),
 'FOOD-01-C08':('unimplemented-effectiveness-outcome','Both effective clash and binding/earlier忌 remain necessary source claims; do not predict calamity or rank.'),
 'FOOD-01-C09':('verse-separate-voice','Full poem context retained, including lines in recovered94a. Verse flags/fortunes are not automatically overriding prose.'),
 'FOOD-01-C10':('explicit-label-constraint','Final comment distinguishes two傷官labels from two nonlabels, not reducing four-day eligibility to two.'),
 'FOOD-02-C01':('heading','倒衝祿 heading.'),
 'FOOD-02-C02':('partial-two-day-and-pools','Two days and explicit officer/virtual target mappings. Six collective attraction tokens remain unassigned; 丁申辰 restraints stay literal, even 辰 not standard六合.'),
 'FOOD-02-C03':('parallel-conditional-voice','不論合祿/只嫌羈絆 and 月/時 wording remain distinct from prior 合住 condition. No universal time exclusion or branch-count threshold invented.'),
 'FOOD-02-C04':('unimplemented-priority-and-counterexample','官煞合格/合煞 alternative explicitly blocks blanket以日刃/填實 verdict. 丁巳辛亥time and source month-strength exception remain source premises, not actual calendar/rank proof.'),
 'FOOD-02-C05':('partial-six-day-separate-voice','Six-day membership kept separately from two-day text, with visible 寅午戌 inventory and 丙count only; not importing all earlier two-day conditions.'),
 'FOOD-02-C06':('verse-separate-voice','All verses retained. 刑衝/無水/合神/填實 severity and prediction statements not converted into factual outcomes.'),
 'FOOD-02-C07':('explicit-final-editor-preference','Final editor prefers 丙午丁巳; six-day voice remains in evidence, not silently erased.')
}
assert set(notes)=={x['id']for x in contexts}
write('CLAUSE_DISPOSITIONS.json',dict(date='2026-10-28',records=[dict(parent=x['id'],digitalCodepoints=len(x['text']),disposition=notes[x['id']][0],note=notes[x['id']][1],wholeContextApplied=False)for x in contexts],wholeSourceUnitsApplied=0))
mapping=[]
for x in read(b/'LOCAL_RENDERS.json')['records']:
 n=x['page'];mapping.append(dict(page=n,file=x['file'],folioNumber=93+(n-187)//2,side='a'if n%2 else'b',
    sideSuffixIsSequenceInference=True,printedFolioNumberDirectlyRead=n%2==1,actuallyViewed=True))
write('FOLIO_MAPPING.json',dict(date='2026-10-28',records=mapping,
    recoveredGapFaces=[dict(folio=f'005-{94+i//2}'+('a'if i%2==0 else'b'),newContainerPage=189+i)for i in range(4)],
    comparedOldBoundaryPositions=[dict(oldPage=188,newPage=188,folio='005-93b'),dict(oldPage=189,newPage=193,folio='005-96a')],
    comparisonKind='Directly viewed text/layout anchors, not a pixel-identity or independently printed edition assertion.',
    earlierContainerStillUnchanged=True,missingFacesNowAvailableInDifferentRepositoryContainer=True,
    original226ContainerGloballySearchedOrRepaired=False))
qa=read(b/'QA_IMAGES.json')
for x in qa['records']:
 assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox()is None
 x['actuallyViewed']=True
write('QA_IMAGES.json',qa)
write('DISCOVERY.json',dict(date='2026-10-28',newRepositoryDescription='https://commons.wikimedia.org/wiki/File:CADAL06056481_三命通會·卷五.djvu',
    githubReadmeOnly='https://github.com/kanripo/KR3g0042',
    institutionalCatalogueLead=dict(url='https://rbook.ncl.edu.tw/NCLSearch/Search/SearchDetail?HasImage=&SourceID=1&item=a8776bf009664f7a8de67d697186e322fDcyODE20.HwkhFZvyoK_b_gt8uDb5Xa7Nh9LYxzj5HEj4uWEtX6g_&page=2&sourceWhereString=&whereString=IChEYXRlX0NyZWF0ZWQgbGlrZSAnJTE1NzglJyBvciBEb2N1bWVudF9ZZWFyIGxpa2UgJyUxNTc4JScgKSA1.IuMldaBSQarjxhBn_BeTs0yAImbyvOSAYg5y7FFSAGw_',
       institution='Taiwan National Central Library',catalogueNumber='06590',catalogueEditionClaim='明萬曆六年1578刊本/十二卷/十二冊',
       inspectedByWebTool=True,exactHTTPBodyRetained=False,imagesAccessed=False,
       metadataIsNotOurWYGImageWitness=True,verificationWidgetPresentNotBypassed=True),
    otherToolProbes=[dict(url='https://ctext.org/library.pl?if=gb&res=6109',result='403Forbidden;notretriedorworkaroundaccessed'),
      dict(url='https://upload.wikimedia.org/wikipedia/commons/d/d6/CADAL06056481_三命通會·卷五.djvu',result='WebtoolunsupportedDjVutype;authorizednormalTLSdownloadofpublicoriginalsucceeded,norestrictionbypassed')],
    retainedNewHTTPBodies=3,toolProbeResultsAreNotRawHTTPByteEvidence=True))
print(json.dumps(dict(contexts=len(contexts),codepoints=sum(len(x['text'])for x in contexts),daySets=3,mechanismCases=6,recoveredFaces=4,crops=6)))
