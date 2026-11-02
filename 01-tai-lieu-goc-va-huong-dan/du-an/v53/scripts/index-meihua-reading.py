from pathlib import Path
from hashlib import sha256
import json,re

root=Path(__file__).resolve().parent.parent
source=root/'research/meihua'
out=root/'research/meihua-reading'
out.mkdir(exist_ok=True)
sha=lambda b:sha256(b).hexdigest()
implemented={'周易卦數','五行生克','八宮所屬五行','八卦象例','卦以八除','爻以六除','互卦起例','年月日時起例','物數占例','物卦起例（端法後天起卦）','八卦方位圖'}
examples={'觀梅占','牡丹占','鄰夜扣門借物占','老人有憂色占','少年有喜色占','牛哀鳴占'}
words={'字占','一字占至十一字占','今日動靜如何','西林寺牌額占','起卦加數例'}
measures={'丈尺占','尺寸占'}
philosophy={'占法','玩法','心易占卜玄機','占卜論理訣','八卦心易體用訣','三要靈應篇序','觀梅數訣序','風覺鳥占'}
conflicts={'變卦式八則','體用互變之訣','觀物玄妙歌訣','起卦加數例','卦應（與前八卦類象，大同小異，觀者可以互參）'}
notes={
 '聲音占例':'Single-stream wording differs from the separately exemplified two-group method;do not silently map every sound input to one formula.',
 '字占':'Even/odd grouping;the characters and historical count/tone premises must be explicit.',
 '一字占至十一字占':'One-character left/right strokes,2/3-character strokes,4..10historical tone classes,11+character counts differ. No universal modern automatic counting.',
 '丈尺占':'Upperzhang/lowerchi,moving=sum without hour,ignorecun;historical units not automatically metric.',
 '尺寸占':'Upperchi/lowercun,moving=sum plus hour,ignorefen;must not reuse zhang/chi line rule.',
 '今日動靜如何':'Six-character1/4/3and3/1/1 historical tone counts,8upper/5lower,total13,moving1,46→11. No hour in worked example.',
 '西林寺牌額占':'Witness counts西7/林8then10;not modern standard strokes.17gives moving5/41→61;15gives moving3/23→52.',
 '起卦加數例':'Three surname offsets4/6/21are explicit,including田6. Digital text says初爻 after remainder3;printedp95says三為爻. No automatic name counting.',
 '體用互變之訣':'Upper/lower mutual roles follow static/moving half. Printedp109says觀梅恒卦;do not merge that unnamed context with the earlier49plum example.',
 '變卦式八則':'Full-hexagram versus changed-trigram labels and source-internal inconsistencies require separate interpretation;one-line consumer rule is not overwritten.',
 '觀物玄妙歌訣':'Printedp121also has離 heading with earth/mountain attributes;unresolved witness-internal mismatch. Digital凱撒 differs from printed西澤.',
 '疾病占第十六':'Historical medical/medicine/death/ghost claims are recorded for source study,not used as diagnoses or treatment rules.',
 '生產占第六':'Historical birth/sex/maternal risk forecasts are source content,not a validated functional classifier.',
 '天時占第一':'Whole-hexagram weather symbolism expressly does not divide body/use;not a weather forecast service.',
 '八卦萬物屬類':'Eight tables contain neutral symbolic data and conditional social/medical/financial predictions;field-level disposition retained separately.',
 '八卦萬物屬類（並為上卦）':'Object→symbol lists apply only when observer explicitly chooses symbol;not a unique image/text classifier.',
 '十應目論':'Eleven nested headings follow a title of ten responses;retain actual section count rather than renumbering the witness.',
 '占卜十應訣':'Opening list omits方應 but body includes it;count actual named responses and distinguish paragraph headings from unit-level headings.',
 '卦應（與前八卦類象，大同小異，觀者可以互參）':'Mixed traditional/simplified transcription with＄placeholder and wording issues;requires scan collation before structured application.'
}
records=[];tables=[]
for volume in ['一','二','三']:
 path=source/f'volume-{volume}.wiki';text=path.read_text(encoding='utf8')
 heads=list(re.finditer(r'^(={3,4})\s*(.*?)\s*\1\s*$',text,re.M))
 for n,m in enumerate(heads):
  end=heads[n+1].start()if n+1<len(heads)else len(text)
  title=m.group(2).strip();body=text[m.end():end]
  if title in conflicts:kind='unresolved-text-or-witness-premise'
  elif title in implemented:kind='core-data-or-arithmetic-partly-implemented'
  elif title in examples:kind='arithmetic-implemented-narrative-not-validated'
  elif title in words:kind='reproducible-method-open-needs-explicit-input-convention'
  elif title in measures:kind='reproducible-method-open-historical-units'
  elif title in philosophy or title.endswith('序'):kind='historical-philosophical-no-direct-calculation'
  elif re.search(r'占第[一二三四五六七八九十]+$',title):kind='traditional-domain-prognosis-not-validated-for-automation'
  elif title in ['八卦萬物屬類','八卦萬物屬類（並為上卦）','八卦類象','卦應（與前八卦類象，大同小異，觀者可以互參）']:kind='symbolic-correspondences-partly-used-most-fields-research-only'
  else:kind='conditional-symbolic-or-narrative-rule-study-open'
  records.append({'id':f'{volume}-{n+1:03}','volume':volume,'headingLevel':len(m.group(1)),'heading':title,'sourceFile':f'../meihua/{path.name}','sourceFileSHA256':sha(path.read_bytes()),'offsetKind':'PythonUnicode-codepoint-index-in-decoded-UTF8','start':m.start(),'end':end,'sourceSliceSHA256':sha(text[m.start():end].encode()),'bodyCharacters':len(body),'disposition':kind,'readingLevel':'digital-section-survey-not-complete-clause-collation','note':notes.get(title,'Content remains conditional within this named section;not promoted to a complete or validated rule merely by indexing.'),'wholeUnitApplied':False})
  if volume=='一'and title=='八卦萬物屬類':
   sub=list(re.finditer(r"^'''([乾坤震巽坎離艮兌])卦'''",body,re.M))
   for k,t in enumerate(sub):
    part=body[t.end():sub[k+1].start()if k+1<len(sub)else len(body)]
    fields=[]
    for line in part.splitlines():
     if '：'not in line:continue
     key,value=line.split('：',1);key=key.strip();value=value.strip()
     if not key or len(key)>4:continue
     neutral=key in ['方道','五色','數目','五味','動物','靜物','人物','人事','地理','天時','屋舍','姓字','時序']
     fields.append({'field':key,'text':value,'textSHA256':sha(value.encode()),'disposition':'historical-symbolic-data-requires-field-collation'if neutral else 'traditional-domain-or-health-claim-research-only','productApplied':False})
    tables.append({'trigram':t.group(1),'fields':fields,'fieldCount':len(fields),'sourceSectionID':records[-1]['id'],'notAnAutomaticObjectClassifier':True})
result={'schema':'hhc.meihua.digital-unit-dispositions.v1','date':'2026-10-26','sourceScope':'Three pinned digital volumes only;five-volume scan and full clause collation still open. Survey is not whole-work application.','counts':{'sections':len(records),'trigramTables':len(tables),'tableFields':sum(len(t['fields'])for t in tables),'wholeUnitsApplied':0},'records':records}
(out/'DIGITAL_UNIT_DISPOSITIONS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(out/'TRIGRAM_TABLE_FIELDS.json').write_text(json.dumps({'source':'../meihua/volume-一.wiki','tables':tables,'scope':'Extracted indexed fields,not a full witness collation and not all knowledge implemented.'},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
assert len(records)==123 and len(tables)==8
print(json.dumps(result['counts']))
