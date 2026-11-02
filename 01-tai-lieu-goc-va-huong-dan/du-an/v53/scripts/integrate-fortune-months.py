from pathlib import Path
root=Path(__file__).resolve().parent.parent
p=root/'index.html';s=p.read_text(encoding='utf-8');needle='<script src="fortune.js"></script>'
if '<script src="fortune-months.js"></script>' not in s:s=s.replace(needle,needle+'\n<script src="fortune-months.js"></script>',1)
p.write_text(s,encoding='utf-8')
p=root/'scripts/build.mjs';s=p.read_text(encoding='utf-8').replace("'fortune.js','bearing-guide.js'","'fortune.js','fortune-months.js','bearing-guide.js'");p.write_text(s,encoding='utf-8')
p=root/'fortune.js';s=p.read_text(encoding='utf-8')
s=s.replace('result.innerHTML=resultHTML(chart,r);','result.innerHTML=resultHTML(chart,r)+(window.HHC_FORTUNE_MONTHS?.render(chart,r)||\'\');',1)
needle="form.addEventListener('submit',e=>{e.preventDefault();show()});"
replacement="result.addEventListener('click',e=>{const button=e.target.closest('[data-forecast-date]');if(!button||button.disabled||!result.contains(button))return;const value=button.dataset.forecastDate;form.elements.forecastDate.value=value;show();const months=result.querySelector('.fortune-months');if(months)months.open=true;result.querySelector(`[data-forecast-date=\"${value}\"]`)?.focus({preventScroll:true})});"+needle
if "result.addEventListener('click'" not in s:s=s.replace(needle,replacement,1)
p.write_text(s,encoding='utf-8')
p=root/'app.js';s=p.read_text(encoding='utf-8')
needle="function download(){if(!state.result)return;const text="
replacement="function download(){if(!state.result)return;const monthDetails=[...document.querySelectorAll('.result-body .fortune-months')].map(el=>({el,open:el.open}));monthDetails.forEach(x=>x.el.open=true);const text="
if needle in s:s=s.replace(needle,replacement,1).replace("const url=URL.createObjectURL(new Blob(['\\ufeff',text]","monthDetails.forEach(x=>x.el.open=x.open);const url=URL.createObjectURL(new Blob(['\\ufeff',text]",1)
needle="function download(){"
if 'printMonthState' not in s:
 s=s.replace(needle,"let printMonthState=[];window.addEventListener('beforeprint',()=>{printMonthState=[...document.querySelectorAll('.result-body .fortune-months')].map(el=>({el,open:el.open}));printMonthState.forEach(x=>x.el.open=true)});window.addEventListener('afterprint',()=>{printMonthState.forEach(x=>x.el.open=x.open);printMonthState=[]});\n"+needle,1)
p.write_text(s,encoding='utf-8')
print('Integrated lunar-month overview, navigation and complete month-list TXT/print handling.')
