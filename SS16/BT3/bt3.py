
# - Vấn đề của if-elif: Khi menu có quá nhiều lựa chọn, việc lặp lại cú pháp 'elif choice == ...' 
#   khiến luồng điều khiển (main flow) trở nên dài dòng và kém tính thẩm mỹ.
# - Giải pháp match-case: Hoạt động tương tự cấu trúc switch-case trong C/C++/Java. Nó đánh giá 
#   trực tiếp giá trị của biến 'choice' và rẽ nhánh vào 'case' tương ứng, giúp code gọn gàng, 
#   dễ đọc và tăng tốc độ xử lý khi số lượng nhánh lớn.
# - Trường hợp mặc định (Default/Else): Sử dụng 'case _' (wildcard) để bắt tất cả các 
#   giá trị không khớp với các case đã định nghĩa ở trên (tương đương với lệnh else).



patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def validate_gender(gender_input):
    clean_gender = gender_input.strip().lower()
    if clean_gender == "nam" or clean_gender == "nu":
        return True
    return False

def find_patient_index(patient_list, patient_id):
    clean_id = patient_id.strip().upper()
    for i in range(len(patient_list)):
        if patient_list[i][0] == clean_id:
            return i
    return -1

def display_patients(patient_list):
    print("\n----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    if not patient_list:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
        
    for idx, patient in enumerate(patient_list, 1):
        print(f"{idx}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")

def add_patient(patient_list):
    print("\n----- TIẾP NHẬN BỆNH NHÂN MỚI -----")
    
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if not patient_id:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return
        
    patient_name = input("Nhập tên bệnh nhân: ").strip().title()
    if not patient_name:
        print("Tên bệnh nhân không được để trống!")
        return
    
    while True:
        gender_input = input("Nhập giới tính Nam/Nu: ")
        if validate_gender(gender_input):
            patient_gender = gender_input.strip().lower().capitalize()
            break
        print("\nGiới tính không hợp lệ, vui lòng nhập lại!")
        
    diagnosis = input("Nhập chẩn đoán bệnh: ").strip().capitalize()
    if not diagnosis:
        print("Chẩn đoán bệnh không được để trống!")
        return
    
    new_patient = [patient_id, patient_name, patient_gender, diagnosis]
    patient_list.append(new_patient)
    print("\nTiếp nhận bệnh nhân thành công!")

def update_diagnosis(patient_list):
    print("\n----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip()
    if not patient_id:
        print("Mã bệnh nhân không được để trống!")
        return
        
    index = find_patient_index(patient_list, patient_id)
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id.upper()}!")
        return
        
    print(f"Tìm thấy bệnh nhân: {patient_list[index][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[index][3]}")
    
    new_diagnosis = input("Nhập chẩn đoán mới: ").strip()
    if not new_diagnosis:
        print("Chẩn đoán bệnh không được để trống!")
        return
        
    patient_list[index][3] = new_diagnosis.capitalize()
    print("Cập nhật chẩn đoán bệnh thành công!")

def search_by_disease(patient_list):
    print("\n----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    keyword = input("Nhập từ khóa tên bệnh: ").strip()
    if not keyword:
        print("Từ khóa tìm kiếm không được để trống!")
        return
        
    results = [p for p in patient_list if keyword.lower() in p[3].lower()]
            
    if results:
        print("Kết quả tìm kiếm:")
        for idx, patient in enumerate(results, 1):
            print(f"{idx}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")
    else:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
        
    print(f"\nCó tổng cộng {len(results)} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("1. Hiển thị danh sách bệnh nhân")
    print("2. Tiếp nhận bệnh nhân mới")
    print("3. Cập nhật chẩn đoán bệnh theo mã BN")
    print("4. Tìm kiếm và thống kê theo tên bệnh")
    print("5. Thoát chương trình")
    print("===========================================")
    
    choice_input = input("Nhập lựa chọn của bạn: ").strip()
    
    try:
        choice = int(choice_input)
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
        continue
        
    # Thay thế if-elif bằng cấu trúc match-case
    match choice:
        case 1:
            display_patients(patients)
        case 2:
            add_patient(patients)
        case 3:
            update_diagnosis(patients)
        case 4:
            search_by_disease(patients)
        case 5:
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        case _:
            # Bắt các trường hợp nhập số âm hoặc số lớn hơn 5
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")