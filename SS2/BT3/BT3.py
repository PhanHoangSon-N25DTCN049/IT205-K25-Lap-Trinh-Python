
""" 
Input:
Họ và tên bệnh nhân (patient_name): Kiểu chuỗi (str). Không được để trống hoặc chỉ chứa toàn khoảng trắng.
Tuổi bệnh nhân (patient_age): Kiểu số nguyên (int). Phải nằm trong phạm vi từ 0 đến 150.
Output:
Nếu dữ liệu hợp lệ: In Phiếu khám bệnh điện tử (Họ tên, Tuổi, Kết quả phân luồng).
Nếu dữ liệu không hợp lệ: Chỉ in duy nhất thông báo lỗi và lập tức dừng chương trình (không phân luồng, không in phiếu).
Cấu trúc điều kiện (if-elif-else) rẽ nhánh: Sử dụng để phân loại mức độ ưu tiên của bệnh nhân dựa trên các khoảng tuổi quy định:Dưới 6 tuổi: Phân luồng vào phòng khám Nhi.
Từ 80 tuổi trở lên: Phân luồng vào phòng khám Lão khoa 
Các độ tuổi còn lại: Khám thường.Kiểm tra điều kiện biên và chặn lỗi (Edge Cases): * Sử dụng một cấu trúc if-else lớn ở cuối để bao bọc hành động xuất kết quả.
Hệ thống chỉ in phiếu khi đồng thời thỏa mãn: Tên không được bỏ trống (patient_name != '') và Tuổi phải nằm trong phạm vi sinh học hợp lý từ 0 đến 150 
(0 <= patient_age <= 150). Nếu vi phạm, chương trình lập tức chuyển sang nhánh else để báo lỗi.
"""

patient_name = input('Họ tên bệnh nhân: ');
patient_age = int(input('Tuổi bệnh nhân: '));

result = '';
if patient_age < 6 and patient_age >= 0:
    result = 'ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi.';
elif patient_age >= 80 and patient_age <= 150:
    result = 'ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa';
else:
    result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.";

if patient_name != '' and patient_age >= 0 and patient_age <= 150:
    print('-- Phiếu khám điện tử --');
    print(f'Họ tên: {patient_name}');
    print(f'Tuổi: {patient_age}');
    print(result);
else:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!");