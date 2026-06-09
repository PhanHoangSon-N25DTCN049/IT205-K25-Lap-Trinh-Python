#  Lỗi chuẩn hóa chuỗi (String)
#  Trong Python, chuỗi (String) là kiểu dữ liệu bất biến (immutable). 
#   Khi gọi raw_diagnosis.strip() và raw_diagnosis.title(), hệ thống tạo ra chuỗi mới 
#   chứ không sửa trực tiếp chuỗi gốc. Do code cũ không gán lại giá trị, chuỗi ban đầu 
#   vẫn giữ nguyên các khoảng trắng và lỗi viết hoa lộn xộn.
# - Cách sửa: Gán kết quả trả về đè lên chính biến đó: 
#   raw_diagnosis = raw_diagnosis.strip().title()
#
# Phương thức extend() nhận vào một đối tượng có thể lặp (iterable). 
#   Khi truyền một chuỗi vào extend(), Python bóc tách từng chữ cái và dấu cách 
#   để ném rời rạc vào cuối danh sách.
# - Cách sửa: Thay bằng phương thức append() để coi toàn bộ chuỗi là một phần tử 
#   duy nhất và chèn nguyên vẹn vào danh sách.


# Danh sách chẩn đoán hiện tại của bệnh nhân
patient_diagnoses = ["Sốt Xuất Huyết"]

# Hàm chuẩn hóa tên bệnh và thêm vào hồ sơ
def add_diagnosis(raw_diagnosis, current_list):
    # Chuẩn hóa chuỗi: cắt khoảng trắng thừa và viết hoa chữ cái đầu mỗi từ
    clean_diagnosis = raw_diagnosis.strip().title()
    
    # Thêm nguyên vẹn chuỗi chẩn đoán vào danh sách
    current_list.append(clean_diagnosis)
    
    return current_list

# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng
new_diagnosis = "  viEm phE QUan  "

# Gọi hàm để xử lý và cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print(f"Hồ sơ bệnh án (Các chẩn đoán): {updated_diagnoses}")