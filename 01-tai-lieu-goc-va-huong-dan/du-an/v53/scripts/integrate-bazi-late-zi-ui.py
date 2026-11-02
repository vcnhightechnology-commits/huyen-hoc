"""One-time, exact-match UI edit. A snapshot of the prior app is retained."""
from pathlib import Path
root=Path(__file__).resolve().parent.parent
path=root/'app.js';text=path.read_text(encoding='utf8')
def change(old,new):
    global text
    assert text.count(old)==1,old[:100]
    text=text.replace(old,new)
change("dayPolicy:'current',noTime:false", "dayPolicy:'current',lateZiHour:'day',noTime:false")
anchor='function basicForm()'
helper="""function baziHourOptions(x){return `<div id="bazi-hour-policy" hidden>${selectField('Can giờ Tý muộn (23:00–23:59)','lateZiHour',[['day','Theo ngày đang đọc'],['next','Theo ngày kế tiếp']],x.lateZiHour||'day').replace('<select ', '<select aria-label="Can giờ Tý muộn (23:00–23:59)" ')}<p class="hint" style="margin:-8px 0 16px">Giữ nguyên ngày sinh và Nhật chủ; lựa chọn này chỉ thay cách tính can giờ trong khoảng 23:00–23:59.</p></div>`}
function baziPolicyMeta(x){if(x.noTime||Number(x.hour)!==23)return '';if(x.dayPolicy==='zi')return '<br>Ngày và can giờ Tý muộn cùng theo ngày kế tiếp';return `<br>Can giờ Tý muộn: ${x.lateZiHour==='next'?'theo ngày kế tiếp':'theo ngày đang đọc'}`}
"""
change(anchor,helper+anchor)
change(",x.dayPolicy)}${t==='tuvi'?selectField('Nếu sinh vào tháng nhuận'", ",x.dayPolicy)}${t==='bazi'?baziHourOptions(x):''}${t==='tuvi'?selectField('Nếu sinh vào tháng nhuận'")
change("leapPolicy:raw.leapPolicy||'same'});if(x.noTime)","leapPolicy:raw.leapPolicy||'same'});if(t==='bazi')x.lateZiHour=raw.lateZiHour||'day';if(x.noTime)")
change("}updateYearFields()}","}if($('#bazi-hour-policy'))$('#bazi-hour-policy').hidden=f.elements.noTime.checked||f.elements.hour.value===''||Number(f.elements.hour.value)!==23||f.elements.dayPolicy.value!=='midnight';updateYearFields()}")
change("${x.dayPolicy==='zi'?'Ngày mới từ 23:00':'Ngày mới từ 00:00'}`;const uncertain", "${x.dayPolicy==='zi'?'Ngày mới từ 23:00':'Ngày mới từ 00:00'}${baziPolicyMeta(x)}`;const uncertain")
path.write_text(text,encoding='utf8')
print('Integrated explicit late-Zi hour selection and result metadata.')
