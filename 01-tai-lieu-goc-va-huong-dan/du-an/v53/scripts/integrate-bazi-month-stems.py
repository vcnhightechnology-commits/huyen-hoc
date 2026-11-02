from pathlib import Path
root=Path(__file__).resolve().parent.parent
path=root/'bazi-cycles.js';s=path.read_text(encoding='utf8')
before="Đây là quan hệ của bản khí tháng với Nhật chủ. ${a.season.revealed.filter(h=>h.pillars.length).map(h=>`${esc(h.name)} lộ ở trụ ${esc(h.pillars.join(', '))}`).join('; ')||'Các tàng can tháng không lộ ở can năm, tháng hoặc giờ đã biết'}."
after="Đây là quan hệ của bản khí tháng với Nhật chủ. Mở phần bên dưới để xem cả các can tàng khác và vị trí can lộ tương ứng."
assert s.count(before)==1;s=s.replace(before,after)
before='<h5>Chuỗi đại vận · ${a.direction';after='${monthStems(a)}<div class="bazi-dayun-block"><h5>Chuỗi đại vận · ${a.direction'
assert s.count(before)==1;s=s.replace(before,after)
before='Các nhãn không dự báo một sự kiện chắc chắn sẽ xảy ra.</p></section>';after='Các nhãn không dự báo một sự kiện chắc chắn sẽ xảy ra.</p></div></section>'
assert s.count(before)==1;s=s.replace(before,after)
path.write_text(s,encoding='utf8')
print('Month stem detail inserted without changing inspection/onset calculations.')
