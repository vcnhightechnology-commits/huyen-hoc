"""Private C35 source work created after the three-layer release inventory."""
from pathlib import Path
from hashlib import sha256
from PIL import Image
import re,json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not(B/'PREIMPLEMENTATION_FREEZE.json').exists()and not(B/'song-reference.mjs').exists()
c=next(r for r in read(W/'v53/research/bazi-food-source/CONTEXTS.json')['records']if r['id']=='FOOD-00-C35')
assert len(c['text'])==411 and c['text'].startswith('古歌云')
parts=re.split(r'\((又|义)/\)',c['text'][3:]);poems=parts[::2];markers=parts[1::2]
assert len(poems)==12 and [len(s)for s in poems]==[28]*11+[56]
offset=3;rows=[]
notes=[
 'Control煞/effectivewealth and吞㗖terms; source historical rank/family outcomes not compiled.',
 '祿/衝尅/空亡/官煞/死絶/偏印/合處 retain whole context; do not infer a calendar outcome or resolve line-scope from absent punctuation.',
 '食退/食馬/食貴/食祿 meanings and list join remain open.',
 '印綬notpreferred,財官praised and身旺/梟/比conditions; not merged with next verse.',
 'Selected declared-premise reference:食神生旺, source-listed水木土金luck and whole官煞無來混雜condition; no automatic prohibition of火.',
 '先/後/近 roles/direction/proximity not converted to year/day/hour or numerical distance.',
 '合起/七煞歲時/干頭旺 requires full premises; not automatically effective natal combination.',
 'Explicit甲→丙 reused as fixedrelation only; effective財production and偏印effect stay unknown.',
 '他强旺本干 subject/pronoun binding not adjudicated; no automatic day-master substitution.',
 '食神生旺/無刑尅/身旺/財地 remain distinct necessary source premises.',
 '無損/庻母/偏財救護 retain source metaphors and effective rescue; no lifespan/health prediction.',
 '月上/天厨/梟/衝/生財化鬼 require full scope; no automatic monthly calendar adapter or medical/career output.'
]
for i,s in enumerate(poems):
 marker=None if i==0 else '('+markers[i-1]+'/)'
 if marker:offset+=len(marker)
 rows.append({'id':f'V{i+1:02}','digitalMarkerBefore':marker,'startWithinParentCodepoints':offset,
 'endWithinParentCodepoints':offset+len(s),'text':s,'editorialSevenCharacterLines':[s[j:j+7]for j in range(0,len(s),7)],
 'lineBreaksAreEditorialNotClaimedPrintedLineBreaks':True,'readingNote':notes[i],'wholeVerseApplied':False,'sourceOutcomeValidated':False})
 offset+=len(s)
assert offset==411 and sum(len(r['text'])for r in rows)==364
write('VERSE_PARTITION.json',{'parent':c,'prefixLiteral':'古歌云','rows':rows,'poems':12,'editorialLines':52,
 'poemTextCodepoints':364,'prefixCodepoints':3,'separatorCodepoints':44,'parentCodepoints':411,
 'exactReconstructionRequired':True,'ancientSongSequenceDoesNotEstablishOneAuthorOrUnifiedRule':True,
 'allSourceCharactersDiplomaticallyCollated':False,'wholeContextApplied':False})
write('SELECTED_V05_PREMISES.json',{'sourceID':'TMTH005-FOOD-C35-ancient-song-V05','verseID':'V05','sourceText':poems[4],
 'foodStrengthLiteral':'食神生旺','preferredLuckLiteral':'惟行水木土金佳','preferredLuckElements':['水','木','土','金'],
 'noMixtureLiteral':'官煞更無來混雜','wholeMixtureConditionMustBeDeclared':True,
 'noMixtureIsNotAutomaticallyAbsenceOfEveryOfficialOrSha':True,'verse4OfficialClause': '惟見財官福更隆',
 'noSourcePriorityBetweenVersesChosen':True,'fireUnlistedDoesNotProveBadOutcome':True,
 'C31NotImported':True,'C13NotOverwritten':True,'sourceOutcomeValidated':False,'consumerApplied':False})
write('EXPECTED_CASES.json',{'frameID':'single-verse-declared-premises','cases':[
 {'id':'unknown','element':None,'food':None,'mixtureAbsent':None,'listed':None,'premises':None},
 *[{'id':'listed-'+s,'element':s,'food':True,'mixtureAbsent':True,'listed':True,'premises':True}for s in ['水','木','土','金']],
 {'id':'fire-unlisted','element':'火','food':True,'mixtureAbsent':True,'listed':False,'premises':False},
 {'id':'food-unknown','element':'木','food':None,'mixtureAbsent':True,'listed':True,'premises':None},
 {'id':'mixture-unknown','element':'土','food':True,'mixtureAbsent':None,'listed':True,'premises':None},
 {'id':'food-not-strong','element':None,'food':False,'mixtureAbsent':None,'listed':None,'premises':False},
 {'id':'mixture-present','element':'水','food':True,'mixtureAbsent':False,'listed':True,'premises':False}],
 'fireAdverseOutcomeAlwaysUnknown':True,'neitherListedNorPremiseMatchValidatesFortune':True})
p=W/'v53/research/bazi-food-source/p182.png';box=[530,290,1150,2870];Image.open(p).convert('RGB').crop(box).save(B/'V04-V05-native.png')
write('CROP_CANDIDATE.json',{'source':ident(p),'crop':ident(B/'V04-V05-native.png'),'boxXYXY':box,'actuallyViewed':False})
pair=next(r for r in read(W/'v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json')['records']if r['declaredCoordinatePair']==['甲子','丙子'])
write('REUSE_IDENTITIES.json',{'files':[ident(W/p)for p in ['v53/research/bazi-food-source/CONTEXTS.json','v53/qa/bazi-food-core/TEN_RELATION_RESULTS.json',
 'v53/research/bazi-food-quantity/CURRENT_CONTEXT_COVERAGE.json']],
 'retainedFullImagesActuallyViewed':[ident(W/f'v53/research/bazi-food-source/p{n}.png')for n in [182,183,184]],
 'V08RetainedActualFoodPair':pair,'V08DoesNotValidateWealthProduction':True,
 'referenceIsTextListAndDeclaredPremiseCompositionNotCalendarOrEngineQuery':True,'newEngineCalls':0,'currentMatrixCountsRemain':[49,41,0]})
print(json.dumps({'poems':12,'editorialLines':52,'parentCodepoints':411,'manualCases':10,'newEngineCalls':0,'createdAfterPackageInventory':True,'cropAwaitView':True}))
