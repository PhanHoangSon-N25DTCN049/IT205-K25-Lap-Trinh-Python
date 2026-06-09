# 1. Hàm phụ trợ 1: find_patient_index(patients, er_id)
# - Input: Danh sách patients (List) và Mã ER cần tìm (String).
# - Thuật toán: Chuẩn hóa mã nhập vào (strip, upper). Duyệt qua danh sách, sử dụng
#   phương thức .startswith(er_id + "|") để tìm đúng mã bệnh nhân. Việc gắn thêm "|"
#   là bẫy logic rất quan trọng để tránh tìm "ER01" lại dính nhầm "ER010".
# - Output: Trả về chỉ mục (index) nguyên nếu tìm thấy, ngược lại trả về -1.
#
# 2. Hàm phụ trợ 2: extract_vital_value(vital_string)
# - Input: Chuỗi sinh hiệu nguyên bản, ví dụ "HR:115" hoặc "TEMP:39.5".
# - Thuật toán (Split): Sử dụng .split(":") để cắt chuỗi tại dấu hai chấm, tạo ra mảng 
#   gồm 2 phần tử (ví dụ ["HR", "115"]). Ta lấy phần tử thứ hai ở index 1, ép kiểu 
#   sang số thực (float) để phục vụ cho các phép toán so sánh lớn/nhỏ sau này.
# - Output: Số thực (Float).
#
# 3. Phân tích bẫy lỗi ở tính năng Thêm mới (Admit Patient):
# - Để kiểm tra người dùng có nhập đúng định dạng số (bao gồm số thập phân) hay không 
#   mà không làm crash chương trình, ta dùng hàm .replace(".", "", 1).isdigit(). 
#   Thao tác này loại bỏ 1 dấu chấm thập phân rồi mới kiểm tra xem toàn bộ phần còn 
#   lại có phải là chữ số không.
#
# 4. Phân tích thao tác cập nhật (Update Vitals):
# - Bản chất List chứa String: Cần xác định index của chuỗi trong List -> Lấy chuỗi đó 
#   ra tách bằng .split("|") -> Trở thành List con.
# - Sửa dữ liệu: Truy cập index 2 (với HR) hoặc index 3 (với TEMP) của List con để gán 
#   chuỗi sinh hiệu mới.
# - Lưu trữ: Dùng "|".join() ghép List con lại thành chuỗi, sau đó gán đè chuỗi này
#   vào đúng vị trí index đã tìm được ở mảng lớn patients ban đầu.



# Dữ liệu mock ban đầu
er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]

def find_patient_index(patients, er_id):
    clean_id = er_id.strip().upper()
    for i, p in enumerate(patients):
        if p.startswith(clean_id + "|"):
            return i
    return -1

def extract_vital_value(vital_string):
    parts = vital_string.split(":")
    return float(parts[1])

def display_dashboard(patients):
    print("\n--- BẢNG THEO DÕI CA CẤP CỨU ------------------------------------")
    if not patients:
        print("Khoa cấp cứu hiện đang trống.")
        return
        
    for i, p in enumerate(patients, 1):
        parts = p.split("|")
        # Ép HR sang int để in cho đẹp (loại bỏ .0)
        hr_val = int(extract_vital_value(parts[2]))
        temp_val = extract_vital_value(parts[3])
        print(f"{i}. [{parts[0]}] {parts[1]:<16} | Nhịp tim: {hr_val} bpm | Nhiệt độ: {temp_val} °C")
    print("-" * 65)

def admit_patient(patients):
    print("\n--- TIẾP NHẬN CA CẤP CỨU MỚI ---")
    
    # 1. Nhập mã ER
    er_id = input("Nhập mã ER: ").strip().upper()
    if not er_id:
        print("Mã ER không được để trống!")
        return
    if find_patient_index(patients, er_id) != -1:
        print("Mã ca cấp cứu đã tồn tại!")
        return
        
    # 2. Nhập tên bệnh nhân
    name = input("Nhập tên bệnh nhân: ").strip()
    if not name:
        print("Tên bệnh nhân không được để trống!")
        return
    name = name.title()
    
    # 3. Nhập và bẫy lỗi nhịp tim (HR)
    while True:
        hr_input = input("Nhập nhịp tim HR: ").strip()
        if not hr_input.replace(".", "", 1).isdigit() or float(hr_input) <= 0:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            continue
        hr_str = f"HR:{hr_input}"
        break
        
    # 4. Nhập và bẫy lỗi nhiệt độ (TEMP)
    while True:
        temp_input = input("Nhập nhiệt độ TEMP: ").strip()
        if not temp_input.replace(".", "", 1).isdigit() or float(temp_input) < 36.5:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")
            continue
        temp_str = f"TEMP:{temp_input}"
        break
        
    # Ghép chuỗi và thêm vào danh sách
    new_record = f"{er_id}|{name}|{hr_str}|{temp_str}"
    patients.append(new_record)
    print("\nTiếp nhận ca cấp cứu mới thành công!")
    print("Sau khi chuẩn hóa, dữ liệu được lưu là:")
    print(new_record)

def update_vitals(patients):
    print("\n--- CẬP NHẬT LẠI SINH HIỆU ---")
    er_id = input("Nhập mã ER cần cập nhật: ").strip()
    
    idx = find_patient_index(patients, er_id)
    if idx == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return
        
    parts = patients[idx].split("|")
    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Sinh hiệu hiện tại: {parts[2]} | {parts[3]}")
    
    print("Bạn muốn cập nhật:")
    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")
    choice = input("Chọn loại sinh hiệu: ").strip()
    
    if choice == "1":
        new_hr = input("Nhập nhịp tim mới: ").strip()
        if not new_hr.replace(".", "", 1).isdigit() or float(new_hr) <= 0:
            print("\nSinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            return
        parts[2] = f"HR:{new_hr}"
        print("\nCập nhật nhịp tim thành công!")
        
    elif choice == "2":
        new_temp = input("Nhập nhiệt độ mới: ").strip()
        if not new_temp.replace(".", "", 1).isdigit() or float(new_temp) < 36.5:
            print("\nSinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")
            return
        parts[3] = f"TEMP:{new_temp}"
        print("\nCập nhật nhiệt độ thành công!")
        
    else:
        print("\nLựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")
        return
        
    # Cập nhật lại vào mảng gốc
    patients[idx] = "|".join(parts)

def trigger_red_alert(patients):
    print("\n--- KIỂM TRA BÁO ĐỘNG ĐỎ ---")
    if not patients:
        print("Khoa cấp cứu hiện đang trống.")
        return
        
    critical_cases = []
    
    for p in patients:
        parts = p.split("|")
        hr_val = extract_vital_value(parts[2])
        temp_val = extract_vital_value(parts[3])
        
        # Điều kiện báo động: HR > 100 HOẶC TEMP >= 39.0
        if hr_val > 100 or temp_val >= 39.0:
            critical_cases.append(parts)
            
    if not critical_cases:
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
    else:
        print("\n!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")
        for i, parts in enumerate(critical_cases, 1):
            hr_val = int(extract_vital_value(parts[2]))
            temp_val = extract_vital_value(parts[3])
            print(f"{i}. [{parts[0]}] {parts[1]:<15} | HR: {hr_val} bpm | TEMP: {temp_val} °C | CẦN XỬ LÝ KHẨN CẤP")
        print("-" * 53)
        print(f"Tổng số ca nguy kịch: {len(critical_cases)}")

def discharge_patient(patients):
    print("\n--- XUẤT VIỆN / CHUYỂN KHOA ---")
    er_id = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip()
    if not er_id:
        print("Mã ER không được để trống!")
        return
        
    idx = find_patient_index(patients, er_id)
    if idx == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return
        
    # Lưu lại tên để in thông báo trước khi pop
    patient_name = patients[idx].split("|")[1]
    patients.pop(idx)
    print(f"Đã chuyển khoa thành công cho bệnh nhân {patient_name}!")


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
    print("1. Bảng theo dõi bệnh nhân")
    print("2. Tiếp nhận ca cấp cứu mới")
    print("3. Cập nhật lại sinh hiệu")
    print("4. BÁO ĐỘNG ĐỎ Lọc bệnh nhân nguy kịch")
    print("5. Xuất viện / Chuyển khoa")
    print("6. Thoát chương trình")
    print("=================================================")
    
    choice_input = input("Chọn chức năng (1-6): ").strip()
    
    try:
        choice = int(choice_input)
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng chọn số từ 1-6!")
        continue
        
    # Áp dụng match-case cho luồng điểu khiển chính
    match choice:
        case 1:
            display_dashboard(er_patients)
        case 2:
            admit_patient(er_patients)
        case 3:
            update_vitals(er_patients)
        case 4:
            trigger_red_alert(er_patients)
        case 5:
            discharge_patient(er_patients)
        case 6:
            print("Kết thúc ca trực. Thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng chọn số từ 1-6!")