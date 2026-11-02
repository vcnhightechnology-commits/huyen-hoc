from pathlib import Path
from hashlib import sha256
import json
b=Path(__file__).resolve().parent
source=json.loads((b/'RETAINED_CONTEXT.json').read_text(encoding='utf-8'))['context'];txt=source['text']
specs=[
 ('intro','又曰食神忌梟亦有不畏者',None,None,None,[],None),
 ('jihai','如己亥不畏丁倒食','己','丁','己亥',['sourceAnchorRoleAccepted','effectiveStatedCombination','luClauseMeaningResolved'],'丁壬'),
 ('bingwu','丙午不畏甲倒食','丙','甲','丙午',['sourceAnchorRoleAccepted','effectiveStatedCombination','sourceLuSupportEstablished'],'甲己'),
 ('yisi','乙巳不畏癸倒食','乙','癸','乙巳',['sourceAnchorRoleAccepted','effectiveStatedCombination','sourceFireIdentityEstablished'],'戊癸'),
 ('guisi','癸巳不畏辛倒食','癸','辛','癸巳',['sourceAnchorRoleAccepted','effectiveStatedCombination','sourceGuiSupportEstablished'],'丙辛'),
 ('geng-wu','庚為衆陽之首','庚','戊',None,['sourceAnchorRoleAccepted','sourceYangReturnPremiseEstablished'],None),
 ('ji-xin','巳不倒食辛','辛','己',None,['sourceAnchorRoleAccepted','sourceYinOriginPremiseEstablished'],None),
 ('geng-ren','庚不倒食壬','壬','庚',None,['sourceAnchorRoleAccepted','sourceYangOriginPremiseEstablished'],None),
 ('xin-ding','辛有丁不畏巳倒食','辛','己',None,['sourceAnchorRoleAccepted','sourceDingPresent','effectiveDingSupportEstablished'],None),
 ('six-xin-followup','故六辛人切要丁',None,None,None,[],None)]
starts=[txt.index(s[1])for s in specs];assert starts==sorted(starts)
rows=[]
native={
 'jihai':dict(selectedNativeReading='如己亥不畏丁倒食丁與壬合化木而土祿在亥',readingIssue='土 on native versus壬digital; preserve both, no emendation.'),
 'bingwu':dict(selectedNativeReading='丙午不畏甲倒食甲與己合化土而己祿在午',readingIssue='Canonical己for stem-role glyph, digital巳retained separately; not a whole-character collation.'),
 'yisi':dict(selectedNativeReading='乙巳不畏癸倒食戊癸化火乙巳亦火',readingIssue='Selected clause read, no calendar or effective transformation proved.'),
 'guisi':dict(selectedNativeReading='癸巳不畏辛倒食丙辛化水癸貴在□',readingIssue='Final支glyph己/巳left unresolved in this bounded record; not repaired from conventional貴人table.'),
 'geng-wu':dict(selectedNativeReading='庚為衆陽之首不畏戊倒食戊陽氣歸源之數見戊作喜神論',readingIssue='Historical argument, no measurable definition of陽氣歸源established.'),
 'ji-xin':dict(selectedNativeReading='己不倒食辛陰氣初發散之源',readingIssue='Canonical己in actor role; recipient辛is an explicit editorial role interpretation, not a documented birth-date adapter.'),
 'geng-ren':dict(selectedNativeReading='庚不倒食壬陽氣初發散之源',readingIssue='Recipient壬is an explicit editorial role interpretation; preserve reverse grammar.'),
 'xin-ding':dict(selectedNativeReading='辛有丁不畏己倒食為丁養育辛金也况有丁處便有己土陰陽干涉得清福之助',readingIssue='Canonical己stem-role reading; mere丁presence does not establish support or化. No priority overji-xinclauseadjudicated.')}
for i,(id,marker,recipient,owl,pillar,premises,pair)in enumerate(specs):
 start=starts[i];end=starts[i+1]if i+1<len(starts)else len(txt)
 row=dict(id=id,parentContext='FOOD-00-C15',localCodepointOffsets=[start,end],globalCleanCodepointOffsets=[source['startCleanCodepoint']+start,source['startCleanCodepoint']+end],digitalText=txt[start:end],
  sourceContainerPages=[175,176]if id in ['xin-ding','six-xin-followup']else[175],sourceRecipientStemModel=recipient,sourceOwlStemModel=owl,namedPillarToken=pillar,
  sourceStatedCombinationPair=list(pair)if pair else None,requiredResearchPremises=premises,sourceAnchorRoleAutomaticallyEstablished=False,
  disposition='historical-rationale-still-unimplemented'if recipient is None else'named-textual-premise-audit-only',consumerApplied=False,wholeClauseApplied=False)
 row.update(native.get(id,{}));rows.append(row)
assert ''.join(x['digitalText']for x in rows)==txt
obj=dict(date='2026-10-28',system='TMTH005-C15-owl-exception-premises',sourceContext='FOOD-00-C15',sourceContextCodepoints=len(txt),contextUnitCount=len(rows),exceptionRecords=8,
 exactDigitalPartition=True,allImageCharactersCollated=False,sourceRoleModelIsEditorial=True,sourceRhetoricDoesNotChangeFixedTenGodRelation=True,
 jiXinVersusXinDingPriorityResolved=False,records=rows,sourceOutcomesValidated=False,fullFoodPatternEstablished=False)
(b/'CLAUSE_PARTITION.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PartitionedC15exact213codepoints/10units/8exceptionrecords;rolesandmechanismsremainexplicitpremises')
