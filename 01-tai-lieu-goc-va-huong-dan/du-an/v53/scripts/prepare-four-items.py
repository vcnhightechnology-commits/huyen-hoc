from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent.parent
out=r/'research/four-items'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=json.loads((r.parent/'v49/data/yi_research.json').read_text(encoding='utf-8'))
all_readings={};audit=[]
for p in sorted(out.glob('yi-*.tsv')):
 for row in p.read_text(encoding='utf-8').splitlines():
  n,title,text,tip=row.split('\t');n=int(n);entries=all_readings.setdefault(n,[]);pos=len(entries)+1
  entry={'position':pos,'title':title,'text':text,'tip':tip};entries.append(entry)
  h=source['hexagrams'][n-1];s=r.parent/'v48/evidence/yi'/f'{n:02}.html'
  assert sha(s)==h['source']['sha256']
  audit.append({'number':n,'position':pos,'sourceLine':h['lines'][pos-1]['sourceLine'],'sourceLabel':h['lines'][pos-1]['sourceLineLabel'],'revision':h['source']['revision'],'sourceFile':str(s.relative_to(r.parent)),'sourceSHA256':sha(s),'reading':entry,'editorialReview':'Read individually against the literal image/action of this line. Practical paraphrase, not a full translation or empirically validated prediction; no blanket six-position substitution.'})
assert sorted(all_readings)==list(range(3,65)) and all(len(x)==6 for x in all_readings.values())
assert len(audit)==372 and len({x['reading']['title'] for x in audit})==372
(r/'yi-complete-data.js').write_text('window.HHC_YI_COMPLETE_READINGS='+json.dumps(all_readings,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
(out/'YI_REVIEW.json').write_text(json.dumps({'schema':'hhc.yi.complete-reading-review.v1','date':'2026-10-26','ordinaryLines':384,'newLines':372,'preexistingQianKunLines':12,'records':audit,'limit':'All 384 individual readings are edited from the archived digital text; not a full facsimile collation or independent scholarly endorsement. Alternative interpretations remain possible. Extra Qian/Kun usage texts are kept separate.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
old=json.loads((r/'research/library-audit/NDL_CHART_READINGS.json').read_text(encoding='utf-8'))
new=[
 (9,'離宅 / 九紫宅之圖','10','left',{'Bắc':'延年','Đông Bắc':'禍害','Đông':'生氣','Đông Nam':'天醫','Nam':'伏位','Tây Nam':'六煞','Tây':'五鬼','Tây Bắc':'絶命'}),
 (4,'巽宅 / 四緑宅之圖','13','right',{'Bắc':'生氣','Đông Bắc':'絶命','Đông':'延年','Đông Nam':'伏位','Nam':'天醫','Tây Nam':'五鬼','Tây':'六煞','Tây Bắc':'禍害'}),
 (3,'震宅 / 三碧宅之圖','13','left',{'Bắc':'天醫','Đông Bắc':'六煞','Đông':'伏位','Đông Nam':'延年','Nam':'生氣','Tây Nam':'禍害','Tây':'絶命','Tây Bắc':'五鬼'}),
 (1,'坎宅 / 一白宅之圖','14','left',{'Bắc':'伏位','Đông Bắc':'五鬼','Đông':'天醫','Đông Nam':'生氣','Nam':'延年','Tây Nam':'絶命','Tây':'禍害','Tây Bắc':'六煞'})]
rows=old['readings']+[{'kua':n,'name':name,'file':f'v53/research/library-audit/new-sources/ndl-760737-{page}.jpg','region':side+' chart','directions':dirs} for n,name,page,side,dirs in new]
for x in rows:
 p=r.parent/x['file'] if x['file'].startswith('v53/') else r/'research/library-audit'/x['file'];x['file']=str(p.relative_to(r.parent));x['sha256']=sha(p)
(out/'HOME_64_READINGS.json').write_text(json.dumps({'source':old['source'],'method':old['method'],'date':'2026-10-26','readings':rows,'limit':'Eight diagrams manually read in identifiable Japanese adaptation. Checks labels only, not birth year-to-kua arithmetic, 24 mountains or room fortunes. Earlier 4 charts retained; new 4 read from images 10,13,14. No claim all other book pages reviewed.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Prepared 372 distinct readings and 64 manually read direction labels.')
