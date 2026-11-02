from pathlib import Path
from hashlib import sha256
import json,re,shutil

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/bazi-lu-labels';q=r/'qa/bazi-lu-labels';s=w/'tmp/bazi-lu-labels-staging'
assert not b.exists()and not q.exists(),'One-shot recording; preserve earlier source packets'
b.mkdir();q.mkdir()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for name in['SOURCE_ROWS.json','SOURCE_MANIFEST.json','RETAINED_DIGITAL_TABLE.txt']:
 shutil.copyfile(s/name,b/name)
table=read(b/'SOURCE_ROWS.json')
for x in table['sharedClaims']:
 x['groupingPolicy']='Editorial nearest preceding enumerated pairs; shared-clause grouping made explicit, not an outcome evaluator. Original has no modern punctuation.'
 if x['id']=='wu-final-two':x['scopeLimit']='At least the final乙巳/丁巳 enumeration; whether the final俱吉 also ranges over earlier items is not established here.'
write(b/'SOURCE_ROWS.json',table)
raw=(r/'research/bazi-jianlu-context/DIGITAL_CROSSREF_LU.txt').read_text(encoding='utf-8')
norm='';locations=[];folio='003-1a'
for piece in re.split(r'(<pb:[^>]+>)',raw):
 if piece.startswith('<pb:'):
  folio=re.search(r'_WYG_(.*?)>',piece).group(1);continue
 for ch in piece:
  if not ch.isspace()and ch!='¶':norm+=ch;locations.append(folio)
start=norm.index('祿爵祿也');body=norm[start:];locations=locations[start:]
anchors=[
 ('definition','祿爵祿也','Named Lu definition and10 branch coordinates; season/element rhetoric not modern strength model.'),
 ('fifty-labelled-pairs','甲祿寅如','50 native labelled pairs extracted;8 shared claims scoped separately, no forecast.'),
 ('generated-lu','有生成祿','Two explicit examples甲/甲寅 and乙/乙卯;之類 not a printed ten-stem table.'),
 ('named-rank-lu','有名位祿','Explicit甲/丙寅 example only; no noble-status prediction.'),
 ('true-lu','有眞祿','Mixed stem/branch examples and source貴格 claim; anchor/type semantics open.'),
 ('advance-retreat-true-lu','有進退眞祿','Eight explicit source-pillar/candidate pairs; premise更帶福神 and怕重見 remain, not universal progression formula.'),
 ('lu-meeting','有祿値㑹合','甲/庚戌 example; complete meeting premise not supplied.'),
 ('food-carries-lu','有食神帶祿','Four explicit stem/pillar examples; source食 relation not silently equated with a fully qualified pattern.'),
 ('food-combines-lu','有食神合祿','Eight explicit examples; source collective主吉 retained historically.'),
 ('lu-head-wealth','有祿頭財','甲/戊寅 and乙/己卯 examples; label絪縟煞/claim no consumer forecast.'),
 ('lu-head-ghost','有祿頭鬼','甲/庚寅 and乙/辛卯 examples; source harm/social claim retained, not a forecast.'),
 ('within-xun-lu','有旬中祿','甲申/庚寅 and戊午/丁巳 illustrations, not a complete xun algorithm.'),
 ('heaven-lu-noble','有天祿貴神','丁→午/丙→酉亥/辛酉辛亥→午 chain example; noble-table convention and遁 premises not compiled.'),
 ('stem-branch-combined-lu','有干支合祿','甲/甲寅己亥 and乙/乙卯庚戌 examples; full conditions/open.'),
 ('mutual-noble-lu','有互換貴祿','庚寅/甲申日時 example; source positional context retained.'),
 ('facing-origin-lu','有朝元祿','寅人/甲日時 and胎 context; do not replace explicit source positions with an inferred day anchor.'),
 ('origin-flanking','有朝元夾合','癸巳 +戊辰/戊午 example flanks巳; ordering/夾 andclaim not determined from set membership alone.'),
 ('lu-hall','有祿入祿堂','Quoted named voices and甲/甲戌、辛/辛卯辛丑、壬/壬寅壬子; source says歲干 for甲, not permission to rewrite every other anchor.'),
 ('build-face-near-combine','古人云','甲寅建/丑向/卯近/亥合 andtwo-of-four source claim;餘准此 is derivation invitation, not ten printed rows.'),
 ('physical-social-claims','夫建祿者','Source physiological/social/personality stereotypes; historical-only, not implemented.'),
 ('lu-storage','又曰庫者','Ten stem→庫 coordinates in four printed groups; privately compiled as named Lu storage only.'),
 ('combination-examples','合者','甲寅/亥明合 andabsent寅/亥暗合; branch-membership projection already private, unknown context staysnull.'),
 ('flanking-examples','拱者','甲/丑卯 with/without寅; existing projection leaves兩傍 positional premise unresolved.'),
 ('not-automatic-good','凡人命帶祿','Source warns not everyLu吉 andquotes other works; whole strength/power model absent.'),
 ('change-and-horse-theory','洞𤣥經曰','Quoted theory andschool rationale; not an empirical/physical claim or full horse algorithm.'),
 ('horse-life-claims','燭神經云','Quoted qualities/health/social claims andsource constraints; historical-only, no forecasts.'),
 ('clash-void-claims','又曰凡命帶祿','Source甲/寅申、乙/卯酉 and甲辰旬空寅卯 examples plusunvalidated socialclaims; modern旬空 not inferred for50labels.'),
 ('closing-limit','大抵命入格','Explicit source remindernot exclusively dependentonLu; blocks unconditional label→outcome.')
]
positions=[body.index(text)for _,text,_ in anchors];assert positions==sorted(positions)and positions[0]==0
units=[]
for i,(name,anchor,disposition)in enumerate(anchors):
 lo=positions[i];hi=positions[i+1]if i+1<len(positions)else len(body);text=body[lo:hi]
 fs=list(dict.fromkeys(locations[lo:hi]));pages=[2*int(re.search(r'003-(\d+)',f).group(1))+(1 if f.endswith('a')else 2)for f in fs]
 units.append({'id':name,'digitalStart':lo,'digitalEndExclusive':hi,'retainedDigitalText':text,'retainedFolios':fs,'nativePages':pages,'disposition':disposition,
  'dispositionStatus':'native-label-table-private'if name=='fifty-labelled-pairs'else'native-ten-storage-coordinates-private'if name=='lu-storage'else'explicit-context-with-uncompiled-premises-or-historical-claim',
  'allImageCharactersCollated':False,'sourceOutcomeValidated':False})
assert ''.join(x['retainedDigitalText']for x in units)==body
write(b/'LU_SECTION_CONTEXTS.json',{'date':'2026-10-27','sourceInstructionsAreData':True,'retainedDigitalSource':'v53/research/bazi-jianlu-context/DIGITAL_CROSSREF_LU.txt',
 'retainedDigitalBodyCharacters':len(body),'digitalOffsetUnit':'Unicode code points, not UTF-16 code units;𤣥 is one code point/two UTF-16 units.','contextUnits':len(units),'units':units,'completeRetainedDigitalBodyPartition':True,
 'nativeRangeFirstReadPreviously':'v53/research/bazi-jianlu-context/FACSIMILE_CROSSREF_READINGS.json','newWholeRangeReadingClaim':False,
 'allSourceImageCharactersCollated':False,'wholeSectionApplied':False,'wholeWorkApplied':False})
storage={'date':'2026-10-27','system':'WYG003-lu-storage-coordinates','sourceImages':[13],'sourceFolio':'003-6a',
 'sourceGroups':[{'stems':['甲','乙'],'branch':'未'},{'stems':['丙','丁'],'branch':'戌'},{'stems':['戊','己','壬','癸'],'branch':'辰'},{'stems':['庚','辛'],'branch':'丑'}],
 'sourceReading':'庫者祿之聚如甲乙在未丙丁在戌戊己壬癸在辰庚辛在丑','notOrdinaryElementTombAlgorithm':True,
 'sourceConditionalExample':'如甲乙亥多而得未','sourceManyThresholdEstablished':False,'outcomeValidated':False}
write(b/'LU_STORAGE_TABLE.json',storage)
m=read(b/'SOURCE_MANIFEST.json');renders=read(r/'research/bazi-jianlu-context/volume3/RENDERS.json')
x=next(x for x in renders['records']if x['page']==13)
m['additionalRetainedNativeContextPage']={'page':13,'file':'v53/research/bazi-jianlu-context/volume3/'+x['file'],'sha256':x['sha256'],'scope':'Targeted ten-stem storage paragraph;alreadyread page.'}
m['expandedPreviouslyReadPages']=6
write(b/'SOURCE_MANIFEST.json',m)
print(json.dumps({'nativeTableRows':50,'sharedSourceClaims':8,'sectionContexts':len(units),'digitalBodyCharacters':len(body),'storageCoordinates':10,'expandedReadPages':6,'newSourcePages':0},ensure_ascii=False))
