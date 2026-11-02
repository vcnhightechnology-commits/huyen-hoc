from pathlib import Path
import json,hashlib,re
root=Path(__file__).resolve().parent.parent
out=root/'research/fortune-followup'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
requests=json.loads((out/'REQUESTS.json').read_text(encoding='utf-8'))['records']
for x in requests:
 p=out/x['file'];assert p.stat().st_size==x['bytes'] and sha(p)==x['sha256']
 assert x['tls']['authorized'] and x['status'] in [200,302]
manifest=json.loads((out/'official-manifest.json').read_text(encoding='utf-8'))
canvases=manifest['sequences'][0]['canvases']
viewer=(out/'official-viewer.html').read_text(encoding='utf-8')
items=json.loads(re.search(r'var najContentList = (\[.*?\]);',viewer,re.S)[1])
pages=[]
for n in range(74,81):
 x=next(r for r in requests if r['file']==f'official-{n:03}.jpg')
 assert x['status']==200 and not items[n-1]['restricted']
 pages.append({'sequenceNumber':n,'canvas':canvases[n-1]['@id'],'canvasLabel':canvases[n-1]['label'],'sourceDimensions':[canvases[n-1]['width'],canvases[n-1]['height']],'request':x,'imageDerivative':'Server-rendered IIIF JPEG at 2200 px width, full uncropped spread; not a downloaded original JP2 or a retouched image.'})
stars=[['Liêm Trinh','Phá Quân','Vũ Khúc','Thái Dương'],['Thiên Cơ','Thiên Lương','Tử Vi','Thái Âm'],['Thiên Đồng','Thiên Cơ','Văn Xương','Liêm Trinh'],['Thái Âm','Thiên Đồng','Thiên Cơ','Cự Môn'],['Tham Lang','Thái Âm','Hữu Bật','Thiên Cơ'],['Vũ Khúc','Tham Lang','Thiên Lương','Văn Khúc'],['Thái Dương','Vũ Khúc','Thiên Đồng','Thiên Tướng'],['Cự Môn','Thái Dương','Văn Khúc','Văn Xương'],['Thiên Lương','Tử Vi','Thiên Phủ','Vũ Khúc'],['Phá Quân','Cự Môn','Thái Âm','Tham Lang']]
source={
 'date':'2026-10-26','scope':'Seven complete image spreads acquired; only the explicitly listed passages manually transcribed/compared. Not a whole-book collation.',
 'locationAndTranscriptionPolicy':'Page numbers in this JSON are one-based IIIF sequence ordinals, not physical leaf or PDF page numbers. Chinese running-text readings are normalized working transcriptions (including graphic variants of the earthly-branch Si), not diplomatic character-by-character editions. Decisive Canh/Nham readings are preserved separately; dark or illegible patches are not reconstructed.',
 'institutionalCatalogue':{'url':'https://www.digital.archives.go.jp/file/1078787','file':'official-catalog.html','sha256':sha(out/'official-catalog.html'),'title':'新鋟希夷陳先生紫微斗数全書','referenceCode':'子０６０－０００１','formerHolding':'紅葉山文庫','personsAsCatalogued':['選者:陳搏（宋）','補訂者:潘希尹（明）'],'publicationAsCatalogued':'刊本:明:::','quantity':'2冊','volumes':'７巻','access':'公開','limits':'Official metadata independently confirms these fields; it does not by itself prove historic authorship, a precise publication year, or the Nanyangtang/Baohetang imprint details claimed elsewhere.'},
 'officialImages':{'item':'https://www.digital.archives.go.jp/item/4468520','viewer':'https://www.digital.archives.go.jp/img/4468520','manifest':'official-manifest.json','manifestSHA256':sha(out/'official-manifest.json'),'canvasCount':len(canvases),'publicRestrictionFlag':False,'pages':pages},
 'passages':[
  {'id':'chang-qu','page':75,'region':'right half, below heading 安文昌文曲星訣','reading':'文昌星從戌上起子時如人生子時就在戌宮安之丑時逆至酉宮安之文曲星從辰上起子時若人生子時就在辰宮安之丑時順去巳宮安之餘宮仿此','finding':'Both explanatory columns are legible. They independently support Chang from Xu backwards and Qu from Chen forwards by birth hour. A dark patch above affects an adjacent verse column; no reconstruction of that patch is claimed.'},
  {'id':'zuo-you','page':75,'region':'right final heading and left first columns 安左輔右弼星訣','reading':'左輔從辰上起正月順行如正月生者就辰宮安之二月在巳宮右弼從戌宮逆轉如正月就在戌宮安之二月在酉宮餘依此','finding':'Normal-month direction and starting branches support the current formula. No leap-month extension inferred from this paragraph.'},
  {'id':'four-transformations','pages':[76,77],'region':'76 left lower section 安祿權科忌四星變化訣, continuation 77 right top','heading':'論生年干 挾火而化','rowsByStem':stars,'labelsInOrder':['Hóa Lộc','Hóa Quyền','Hóa Khoa','Hóa Kỵ'],'decisiveReadings':{'Canh':'庚日武同相為首','Nham':'壬梁紫府武宿是'},'finding':'Manual expansion of the forty abbreviated star references. Canh Khoa/Ky differs from the retained digital transcription and selected engine table. Nham Khoa explicitly reads Phu, corroborating Thien Phu in the selected table. This one passage is not evidence that every table or paragraph in the same book agrees.'},
  {'id':'dou-jun','page':79,'region':'right lower half 安斗君訣 即月將星 and continued verse left top','reading':'於流年太歲宮起正月逆至本生月又從本生月起子順數至本生時安斗君','verse':'太歲宮中便起正逆尋生月即留停又從生月宮輪子順到生時鎮斗星','finding':'Supports first-lunar-month anchor by annual branch, birth month and hour. Counting later months forward and applying same/next/split16 are separately declared implementation conventions.'},
  {'id':'major-period','page':80,'region':'right half 安大限訣','reading':'陽男陰女從命前一宮起是父母宮陰男陽女從命後一宮起是兄弟宮','finding':'Adjacent-palace wording is present in the original image, not merely an apparent transcription typo. It differs from the current engine first-decade-at-Menh convention. Do not silently switch the chart or claim the image verifies the current start palace/age.'},
  {'id':'minor-period','page':80,'region':'left top 安小限訣','reading':'不論陰陽男俱順數不論陰陽女俱逆數寅午戌人起辰宮申子辰人起戌宮巳酉丑人起未宮亥卯未人起丑宮','finding':'Confirms four starting branches and gender-based direction. First-age/nominal-age indexing remains the implementation convention tested separately.'}
 ],
 'notVerified':['Other parts of the 129 canvases','All Tứ Hóa tables and internal consistency of this witness','Historic authorship and exact printing date','Full-star prediction validity','A universal leap-month or major-period convention'],
 'transportNote':'Web rendering tool returned 403 for the catalogue during this turn; ordinary authenticated HTTPS subsequently returned 200 for catalogue, viewer, manifest and unrestricted image services, without challenge solving, cookie tricks or access-control bypass.',
 'publicProductPolicy':'Keep evidence/corpus outside site. Current default chart and period indices are unchanged. Consumer period output now retains actual selected leap/day conventions in on-screen, TXT and print content.'
}
(out/'WITNESS_AUDIT.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Verified response hashes and prepared six targeted passage records from seven official image spreads.')
