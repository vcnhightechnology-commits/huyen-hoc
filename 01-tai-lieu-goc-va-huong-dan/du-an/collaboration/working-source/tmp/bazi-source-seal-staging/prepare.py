from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not(B/'FREEZE.json').exists()and not(B/'source-seal.mjs').exists()
p=W/'v53/research/bazi-relations/sources/KR3g0042_003.txt';raw=p.read_text(encoding='utf-8');a=raw.index('　　論正印');b=raw.index('<pb:KR3g0042_WYG_003-44b>')
extract=raw[a:b];(B/'RETAINED_EXCERPT.txt').write_text(extract,encoding='utf-8')
write('MANUAL.json',{'sourceID':'TMTH003-reported-five-element-seal','level':'retained-pinned-digital-transcription-only;no-new-facsimile-collation',
 'folios':['003-43b','003-44a'],'rows':[{'sourceClass':'金命','targets':['乙丑']},{'sourceClass':'木','targets':['癸未']},{'sourceClass':'火','targets':['甲戌']},{'sourceClass':'水土','targets':['壬辰','丙辰']}],
 'waterEarthClause':'水土壬辰丙辰是也','waterEarthAssignmentToSeparateElementsAdjudicated':False,
 'sourceAnchorMeaningFullyAdjudicated':False,'notAutomaticallyDayStemElement':True,
 'huagaiExample':'有華蓋印如亥卯未得癸未之類','huagaiThreeBranchJoinChosen':False,
 'C19CrossReference':'Same work contains a distinct正印chapter defining五行之正庫and華蓋印. This is a concrete lexical lead forC19, not proof C19means exactly that entire system.',
 'C19MeaningAdjudicated':False,'natalAdapter':False,'sourceOutcomeValidated':False})
write('EXPECTED.json',{'cases':[{'sourceClass':s,'target':t,'literalTargetMatch':expected}for s,t,expected in [('金命','乙丑',True),('木','癸未',True),('火','甲戌',True),('水土','壬辰',True),('水土','丙辰',True),('金命','丙辰',False),('木',None,None)]],
 'unsupportedSplitClasses':['水','土'],'supportedClassesAreLiteralSourceGroupsNotNormalizedElementIDs':True})
write('SOURCE_IDENTITIES.json',{'files':[ident(p),ident(W/'v53/research/bazi-relations/sources/REVISION.json'),ident(B/'RETAINED_EXCERPT.txt'),
 ident(W/'v53/research/bazi-relations/sources/KR3g0042_001.txt')],
 'newHTTPBodies':0,'newSourceImages':0,'newSourcePositions':0,'newEngineCalls':0,
 'webSearchLeadsNotEvidence':['Search led to a proposedvolume3論正印reference; local pinned transcription supplies the actual evidence. Unfetched thirdpartytranscriptions/PDFhits are not independent witnesses.'],
 'retainedDigitalSourceRepository':'https://github.com/kanripo/KR3g0042','retainedRevision':'7db72e5553de6ee4c45ed3980c6c67f8a6e451bf'})
write('FREEZE.json',{'atUTC':datetime.now(timezone.utc).isoformat(),'referenceAbsent':True,'files':[ident(B/n)for n in ['MANUAL.json','EXPECTED.json','SOURCE_IDENTITIES.json']],
 'newEngineCallsPlanned':0,'sourceOnlyLookupNotEngineComparison':True})
print(json.dumps({'frozenFiles':3,'sourceGroups':4,'waterEarthSplitAdjudicated':False,'newEngineCalls':0}))
