
# 1. Hàm phụ trợ: find_patient_index(records, patient_id)
# - Input: records (List các chuỗi), patient_id (String).
# - Output: Trả về số nguyên (index) nếu tìm thấy, trả về -1 nếu không thấy.
# - Luồng xử lý: Chuẩn hóa patient_id (viết hoa, xóa khoảng trắng). Duyệt qua mảng records,
#   dùng phương thức .startswith(patient_id + "-") để tìm chuỗi khớp phần đầu.
#
# 2. Hàm chức năng 1: display_records(records)
# - Input: records (List).
# - Output: None (chỉ in ra màn hình).
# - Luồng xử lý: Kiểm tra mảng rỗng. Nếu có dữ liệu, dùng vòng lặp duyệt qua, tách từng 
#   chuỗi bằng .split("-") thành list con và in ra theo định dạng (dùng f-string căn lề).
#
# 3. Hàm chức năng 2: add_patient(records)
# - Input: records (List). Output: None (thêm trực tiếp vào tham chiếu mảng).
# - Luồng xử lý: 
#   + Nhập mã BN: Chuẩn hóa, dùng hàm phụ trợ check trùng -> Ném lỗi nếu trùng.
#   + Nhập Tên: Thay thế dấu '-' bằng khoảng trắng (.replace), chuẩn hóa .title().
#   + Nhập Năm sinh: Kiểm tra bằng .isdigit() và điều kiện 1900 <= năm <= năm hiện tại.
#   + Nhập Chẩn đoán: Thay thế dấu '-' bằng khoảng trắng, chuẩn hóa .capitalize().
#   + Ghép 4 chuỗi bằng f-string (với dấu '-') và .append() vào records.
#
# 4. Hàm chức năng 3: update_diagnosis(records)
# - Input: records (List). Output: None.
# - Luồng xử lý: Tìm index bằng hàm phụ trợ. Nếu index != -1, lấy chuỗi tại index đó 
#   tách ra bằng .split("-"). Cho người dùng nhập chẩn đoán mới, chuẩn hóa và gán đè 
#   vào phần tử cuối (index 3) của list vừa tách. Cuối cùng dùng "-".join() ghép lại 
#   và gán đè lên mảng records tại index tìm được.
#
# 5. Hàm chức năng 4: generate_age_report(records)
# - Input: records (List). Output: None.
# - Luồng xử lý: Khởi tạo biến đếm. Duyệt mảng, tách chuỗi lấy phần tử index 2 ép kiểu 
#   sang int. Tính tuổi = Năm hiện tại - Năm sinh. Dùng if-elif phân loại và tăng biến đếm.


from datetime import datetime

# Dữ liệu ban đầu (Mock data)
patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

def find_patient_index(records, patient_id):
    clean_id = patient_id.strip().upper()
    for i, record in enumerate(records):
        # Dùng startswith kèm dấu '-' để đảm bảo khớp chính xác mã, tránh lỗi tìm BN1 ra BN10
        if record.startswith(clean_id + "-"):
            return i
    return -1

def display_records(records):
    print("\n--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")
    if not records:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return
        
    for i, record in enumerate(records, 1):
        parts = record.split("-")
        # f"{parts[1]:<15}" giúp căn lề trái tên bệnh nhân chiếm 15 khoảng trắng
        print(f"{i}. [{parts[0]}] {parts[1]:<15} | Năm sinh: {parts[2]} | Chẩn đoán: {parts[3]}")
    print("-" * 74)

def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")
    
    # Mã BN
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if not patient_id:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return
        
    # Tên BN (xử lý dấu '-' thành khoảng trắng trước khi dùng title)
    raw_name = input("Nhập tên bệnh nhân: ").strip()
    patient_name = raw_name.replace("-", " ").title()
    
    # Năm sinh
    year_str = input("Nhập năm sinh: ").strip()
    current_year = datetime.now().year
    # Bẫy lỗi: Phải là số và nằm trong khoảng hợp lệ
    if not year_str.isdigit() or not (1900 <= int(year_str) <= current_year):
        print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")
        return
        
    # Chẩn đoán (xử lý dấu '-' thành khoảng trắng trước khi dùng capitalize)
    raw_diagnosis = input("Nhập chẩn đoán: ").strip()
    diagnosis = raw_diagnosis.replace("-", " ").capitalize()
    
    # Ghép chuỗi và thêm vào List
    new_record = f"{patient_id}-{patient_name}-{year_str}-{diagnosis}"
    records.append(new_record)
    
    print("\nThêm hồ sơ bệnh nhân thành công!")

def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")
    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip()
    
    index = find_patient_index(records, patient_id)
    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id.upper()}!")
        return
        
    # String immutable -> Tách ra thành mảng để sửa
    parts = records[index].split("-")
    print(f"\nTìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")
    
    raw_new_diagnosis = input("Nhập chẩn đoán mới: ").strip()
    new_diagnosis = raw_new_diagnosis.replace("-", " ").capitalize()
    
    # Cập nhật mảng tạm và ghép lại thành chuỗi mới
    parts[3] = new_diagnosis
    records[index] = "-".join(parts)
    
    print("\nCập nhật chẩn đoán thành công!")

def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    current_year = datetime.now().year
    
    children = 0
    adults = 0
    seniors = 0
    
    for record in records:
        parts = record.split("-")
        age = current_year - int(parts[2])
        
        if age < 16:
            children += 1
        elif 16 <= age <= 60:
            adults += 1
        else:
            seniors += 1
            
    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {seniors} bệnh nhân")
    print("-" * 38)


# Luồng chạy chính của chương trình
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")
    
    choice_input = input("Chọn chức năng (1-5): ").strip()
    
    try:
        choice = int(choice_input)
    except ValueError:
        print("Lựa chọn không hợp lệ!")
        continue
        
    match choice:
        case 1:
            display_records(patient_records)
        case 2:
            add_patient(patient_records)
        case 3:
            update_diagnosis(patient_records)
        case 4:
            generate_age_report(patient_records)
        case 5:
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        case _:
            print("Vui lòng chọn từ 1 đến 5!")