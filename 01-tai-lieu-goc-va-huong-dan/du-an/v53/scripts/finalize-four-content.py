from pathlib import Path

root=Path(__file__).resolve().parent.parent
p=root/'app.js'
s=p.read_text(encoding='utf-8')
needle="${metric('Cục',r.cucName)}</div>${heading('GÓC NHÌN TỔNG QUAN')}"
replacement="${metric('Cục',r.cucName)}</div><button type=\"button\" id=\"fortune-jump\" class=\"outline-button fortune-jump\">Xem vận hạn theo ngày ↓</button>${heading('GÓC NHÌN TỔNG QUAN')}"
if needle in s:s=s.replace(needle,replacement,1)
needle="if(t==='tuvi')window.HHC_FORTUNE.mount({chart:r,input:x,container:$('.result-body'),onChange:value=>{if(value)x.forecastDate=value;else delete x.forecastDate}});"
replacement="if(t==='tuvi'){window.HHC_FORTUNE.mount({chart:r,input:x,container:$('.result-body'),onChange:value=>{if(value)x.forecastDate=value;else delete x.forecastDate}});$('#fortune-jump').onclick=()=>{$('.fortune-section').scrollIntoView({block:'start',behavior:'smooth'});$('.fortune-form input').focus({preventScroll:true})}}"
if needle in s:s=s.replace(needle,replacement,1)
p.write_text(s,encoding='utf-8')
p=root/'index.html';s=p.read_text(encoding='utf-8').replace('Tử vi theo 12 chủ đề','12 chủ đề & vận hạn');p.write_text(s,encoding='utf-8')
p=root/'scripts/verify.mjs';s=p.read_text(encoding='utf-8').replace("p.locator('.reading-card').count()===2","p.locator('.result-body > .reading-grid > .reading-card').count()===2");p.write_text(s,encoding='utf-8')
p=root/'scripts/verify-four-browser.mjs';s=p.read_text(encoding='utf-8');needle="test('No reference date or period is fabricated before a user chooses it'";replacement="await p.locator('#fortune-jump').click();test('A shortcut at the top of the result focuses the period date field',await p.locator('[name=forecastDate]').evaluate(e=>document.activeElement===e));test('No reference date or period is fabricated before a user chooses it'";s=s.replace(needle,replacement,1);p.write_text(s,encoding='utf-8')
p=root/'four-items.css';s=p.read_text(encoding='utf-8');s+='\n.fortune-jump{margin-top:16px;min-height:44px}.fortune-section{scroll-margin-top:24px}@media print{.fortune-jump{display:none!important}}\n' if '.fortune-jump{' not in s else '';p.write_text(s,encoding='utf-8')
print('Added accessible period shortcut and scoped the existing natal-reading assertion.')
