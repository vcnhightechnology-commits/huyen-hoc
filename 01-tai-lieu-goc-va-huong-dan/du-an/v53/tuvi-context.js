(()=>{'use strict';
const mod=(x,n)=>(x%n+n)%n,esc=v=>String(v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
// Rows start at Dan, as in the archived table selected for this reading.
const table={
'Tử Vi':['wang','wang','de','wang','miao','miao','wang','wang','de','wang','ping','miao'],
'Thiên Cơ':['de','wang','li','ping','miao','xian','de','wang','li','ping','miao','xian'],
'Thái Dương':['wang','miao','wang','wang','wang','de','de','ping','bu','xian','xian','bu'],
'Vũ Khúc':['de','li','miao','ping','wang','miao','de','li','miao','ping','wang','miao'],
'Thiên Đồng':['li','ping','ping','miao','xian','bu','wang','ping','ping','miao','wang','bu'],
'Liêm Trinh':['miao','ping','li','xian','ping','li','miao','ping','li','xian','ping','li'],
'Thiên Phủ':['miao','de','miao','de','wang','miao','de','wang','miao','de','miao','miao'],
'Thái Âm':['wang','xian','xian','xian','bu','bu','li','wang','wang','miao','miao','miao'],
'Tham Lang':['ping','li','miao','xian','wang','miao','ping','li','miao','xian','wang','miao'],
'Cự Môn':['miao','miao','xian','wang','wang','bu','miao','miao','xian','wang','wang','bu'],
'Thiên Tướng':['miao','xian','de','de','miao','de','miao','xian','de','de','miao','miao'],
'Thiên Lương':['miao','miao','miao','xian','miao','wang','xian','de','miao','xian','miao','wang'],
'Thất Sát':['miao','wang','miao','ping','wang','miao','miao','wang','miao','ping','wang','miao'],
'Phá Quân':['de','xian','wang','ping','miao','wang','de','xian','wang','ping','miao','wang']};
const labels={miao:'Miếu',wang:'Vượng',de:'Đắc địa',li:'Lợi',ping:'Bình hòa',bu:'Bất đắc địa',xian:'Hãm'};
const pairs=[
['Tử Vi','Thiên Phủ','Tầm nhìn và gìn giữ nguồn lực','Kết nối việc định hướng với khả năng duy trì nền tảng. Hãy phân biệt điều cần quyết định với điều cần giao cho người khác chăm sóc.'],
['Tử Vi','Tham Lang','Định hướng và trải nghiệm','Giữ một mục tiêu chính khi có nhiều điều hấp dẫn. Trải nghiệm mới hữu ích hơn khi bạn biết giới hạn thời gian và nguồn lực.'],
['Tử Vi','Thiên Tướng','Dẫn dắt và phối hợp','Làm rõ vai trò của người quyết định và người điều phối; một thỏa thuận tốt giúp trách nhiệm không dồn vào một người.'],
['Tử Vi','Thất Sát','Định hướng và quyết đoán','Trước một bước mạnh, xác định mục tiêu, giới hạn và người có thể phản biện. Quyết đoán cần đi cùng trách nhiệm về hệ quả.'],
['Tử Vi','Phá Quân','Định hướng và đổi mới','Đặt tiêu chí cho điều nên giữ và điều nên thay. Thử một thay đổi nhỏ trước khi sửa cả hệ thống.'],
['Thiên Cơ','Thái Âm','Suy tính và chiều sâu','Dành thời gian suy nghĩ nhưng đặt một mốc để hành động. Ghi lại giả định giúp bạn không bị cuốn vào những khả năng chưa xảy ra.'],
['Thiên Cơ','Cự Môn','Phân tích và đối thoại','Biến điều nghi ngại thành câu hỏi rõ ràng; tách dữ kiện khỏi cách diễn đạt để cuộc trao đổi đi đến một bước cụ thể.'],
['Thiên Cơ','Thiên Lương','Linh hoạt và nguyên tắc','Xác định nguyên tắc cốt lõi rồi linh hoạt về cách làm. Xin ý kiến người có kinh nghiệm khi hai điều này xung đột.'],
['Thái Dương','Thái Âm','Biểu đạt và lắng nghe','Cân bằng thời gian xuất hiện trước người khác với thời gian hồi phục và suy ngẫm. Hai nhịp này có thể hỗ trợ nhau.'],
['Vũ Khúc','Thiên Phủ','Thực thi và tích lũy','Tổ chức phần việc, ngân sách và nguồn dự phòng thành các mục riêng. Đánh giá tiến độ bằng điều thực hiện được.'],
['Vũ Khúc','Tham Lang','Kỷ luật và cơ hội','Đặt mức thử nghiệm cho ý tưởng mới. Sự hứng thú cần một giới hạn chi phí và một mốc đánh giá.'],
['Vũ Khúc','Thiên Tướng','Hiệu quả và hợp tác','Thống nhất tiêu chuẩn công việc cùng người liên quan. Một kết quả tốt cần cả tiến độ và cách phối hợp dễ duy trì.'],
['Vũ Khúc','Thất Sát','Thực thi và sức ép','Chia mục tiêu khó thành chặng ngắn; kiểm lại nguồn lực và nhịp nghỉ trước khi nhận thêm trách nhiệm.'],
['Vũ Khúc','Phá Quân','Tổ chức và tái cấu trúc','Đo điều đang hoạt động trước khi đổi cách làm. Giữ bản dự phòng và thử thay đổi trong phạm vi có thể quay lại.'],
['Thiên Đồng','Thái Âm','Sự dễ chịu và đời sống bên trong','Tạo không gian hồi phục nhưng nói rõ nhu cầu của mình. Đừng để mong muốn giữ hòa khí thay cho một cuộc trao đổi cần thiết.'],
['Thiên Đồng','Cự Môn','Hòa khí và tiếng nói riêng','Diễn đạt điều chưa hài lòng bằng nhu cầu cụ thể. Một đề nghị nhỏ dễ thực hiện có thể giúp cuộc trò chuyện bớt căng.'],
['Thiên Đồng','Thiên Lương','Chăm sóc và giới hạn','Giúp đỡ trong phần việc bạn có thể duy trì; làm rõ giới hạn để sự nâng đỡ không biến thành quá tải.'],
['Liêm Trinh','Thiên Phủ','Chuẩn mực và nền tảng','Làm rõ điều bạn cam kết giữ, rồi xây một nếp thực hiện đều đặn. Quy tắc hữu ích khi có thể áp dụng trong đời sống.'],
['Liêm Trinh','Tham Lang','Giới hạn và mong muốn','Nhận diện điều hấp dẫn cùng giới hạn của bản thân. Một quyết định rõ ràng giúp mong muốn và cam kết không kéo ngược nhau.'],
['Liêm Trinh','Thiên Tướng','Ranh giới và sự công bằng','Thống nhất cách phân chia trách nhiệm và giải quyết bất đồng. Nói rõ kỳ vọng trước khi nhận lời.'],
['Liêm Trinh','Thất Sát','Nguyên tắc và bước quyết định','Kiểm lại quy tắc và hệ quả trước khi hành động nhanh. Nếu tình huống căng, hãy tìm một người có thể cùng xem xét.'],
['Liêm Trinh','Phá Quân','Cam kết và thay đổi','Khi một cách làm không còn phù hợp, xác định cam kết nào vẫn cần giữ. Thay đổi từng bước giúp bạn đánh giá hệ quả.']
];
function brightness(name,index){if(!Number.isInteger(index)||index<0||index>11)throw Error('Vị trí cung chưa hợp lệ.');const code=table[name]?.[mod(index-2,12)];return code?{code,label:labels[code]}:null}
function inspect(chart,index){const p=chart?.palaces?.find(p=>p.idx===Number(index));if(!p)throw Error('Chưa có cung để đọc.');const group=[0,4,8,6].map((off,i)=>{const q=chart.palaces.find(q=>q.idx===mod(p.idx+off,12));if(!q)throw Error('Lá số thiếu cung liên quan.');return{idx:q.idx,name:q.name,branch:q.branch,relation:['Cung đang đọc','Tam hợp','Tam hợp','Đối diện'][i],stars:q.stars.filter(s=>s.kind==='core').map(s=>({name:s.name,brightness:brightness(s.name,q.idx)}))}}),names=group[0].stars.map(s=>s.name),pair=pairs.find(a=>names.includes(a[0])&&names.includes(a[1]));return{group,pair:pair?{stars:pair.slice(0,2),title:pair[2],text:pair[3]}:null}}
function render(chart,index){const r=inspect(chart,index);return`<section class="tuvi-context" aria-label="Các cung liên quan"><h5>Đọc cùng các cung liên quan</h5><p class="hint">Cung đang xem, hai cung tam hợp và cung đối diện tạo thành tam phương tứ chính. Các sao giữ nguyên vị trí trên lá số.</p><div class="context-grid">${r.group.map(p=>`<article><small>${esc(p.relation)}</small><b>${esc(p.name)} · ${esc(p.branch)}</b><p>${p.stars.length?p.stars.map(s=>`${esc(s.name)} <span class="star-status">${esc(s.brightness?.label||'Chưa có nhãn')}</span>`).join('<br>'):'Không có chính tinh tọa thủ'}</p></article>`).join('')}</div>${r.pair?`<div class="tip"><b>${esc(r.pair.title)}</b><p>${esc(r.pair.stars.join(' và '))} cùng cung. ${esc(r.pair.text)}</p></div>`:''}<p class="hint">Miếu, Vượng, Đắc địa, Lợi, Bình hòa, Bất đắc địa và Hãm là nhãn truyền thống theo bảng đang dùng; không phải thang điểm cuộc đời. Phần đọc phối hợp là gợi mở để chiêm nghiệm.</p></section>`}
window.HHC_TUVI_CONTEXT={brightness,inspect,render};
})();
