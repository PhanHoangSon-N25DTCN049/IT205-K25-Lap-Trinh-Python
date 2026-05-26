
patient_name = input('Họ tên bệnh nhân: ').split();
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