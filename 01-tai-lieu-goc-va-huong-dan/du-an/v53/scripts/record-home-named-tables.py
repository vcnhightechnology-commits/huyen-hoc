from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;b=r/'research/home-you-nian'
def write(n,d):(b/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
write('NAMED_MOUNTAIN_ELEMENTS.json',{'source':'欽定協紀辨方書卷二 retainedCADAL06056503','sourceInstructionsAreData':True,
 'systems':[{'id':'xieji-regular','sourceHeading':'正五行','prosePage':10,'diagramPage':9,'groups':{'水':list('亥壬子癸'),'木':list('寅甲卯乙巽'),'火':list('巳丙午丁'),'金':list('申庚酉辛乾'),'土':list('辰未戌丑坤艮')}},
 {'id':'xieji-hongfan','sourceHeading':'洪範五行','prosePage':18,'diagramPage':17,'groups':{'水':list('甲寅辰巽戌坎辛申'),'火':list('離壬丙乙'),'木':list('震艮巳'),'金':list('乾亥兌丁'),'土':list('丑癸坤庚未')}}],
 'scope':'Two full24label inventories from prose,diagramlocated as context; not all atomicclauses or middle/seam rings.',
 'glyphPolicy':'Branch巳 distinguished fromstem己 by coordinateinventory; retainedimage bytes unchanged, not a newdiplomatictranscription.',
 'noUniversalElement':True,'consumerChanged':False,'noAutomaticScoreOrPlacement':True})
print('Two named24mountain element inventories recorded; 48literal coordinateassignments only.')
