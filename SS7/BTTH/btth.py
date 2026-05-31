# 1. Phân tích bài toán:
#    - Dữ liệu thô: raw_input = "   nGuyen vaN aN  ;  2004   "
#    - Hệ thống hoạt động liên tục bằng vòng lặp while True và hiển thị menu 4 chức năng.
#    - Năm hiện tại được quy định cố định là 2026 để tính tuổi.
#
# 2. Thuật toán xử lý chuỗi:
#    - Chức năng 2: 
#      + Tách họ tên và năm sinh bằng .split(";")
#      + Dùng .strip() xóa khoảng trắng thừa và .title() để chuyển tên về dạng Title Case.
#      + Ép kiểu năm sinh sang số nguyên (int) và lấy 2026 trừ đi để ra tuổi.
#    - Chức năng 3:
#      + Tách nhỏ chuỗi họ tên đã làm sạch bằng khoảng trắng để lấy các phần: Họ, Tên đệm, Tên chính.
#      + Tạo Email: Ghép chữ cái đầu của Họ + Tên đệm + toàn bộ Tên chính -> chuyển .lower() + @company.com
#      + Tạo Mã ID: Lấy Tên chính chuyển .upper() + 2 số cuối năm sinh bằng kỹ thuật cắt chuỗi Slicing [-2:].


# Dữ liệu đầu vào cố định theo yêu cầu đề bài
raw_input = "   nGuyen vaN aN  ;  2004   "

while True:
    # Hiển thị cấu trúc menu điều hướng hệ thống
    print("\n===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    # CHỨC NĂNG 1: Kiểm tra dữ liệu thô ban đầu
    if choice == "1":
        print(f"\nChuỗi dữ liệu gốc: '{raw_input}'")
        
    # CHỨC NĂNG 2: Tách chuỗi, chuẩn hóa tên và tính tuổi (Gốc thời gian: 2026)
    elif choice == "2":
        # Bóc tách dữ liệu dựa trên dấu ";"
        parts = raw_input.split(";")
        
        # Làm sạch khoảng trắng và chuẩn hóa định dạng chữ
        full_name = parts[0].strip().title()
        birth_year = int(parts[1].strip())
        
        # Tính toán số tuổi dựa trên năm giả định 2026
        age = 2026 - birth_year
        
        print("\n--- KẾT QUẢ CHUẨN HÓA ---")
        print(f"Họ và tên: {full_name}")
        print(f"Tuổi: {age} tuổi (Năm sinh: {birth_year})")
        
    # CHỨC NĂNG 3: Phân tích thành phần tên, tạo Email, ID và in thẻ thành viên
    elif choice == "3":
        parts = raw_input.split(";")
        raw_name = parts[0].strip()
        raw_year = parts[1].strip()
        
        # Tách họ tên thành các từ riêng biệt để xử lý cấu trúc
        name_elements = raw_name.split()
        
        # Trích xuất các phần: Họ, Tên đệm và Tên chính
        ho = name_elements[0]
        ten_chinh = name_elements[-1]
        # Ghép các từ ở giữa lại làm tên đệm (phòng trường hợp nhiều tên đệm)
        ten_dem = " ".join(name_elements[1:-1]) 
        
        # Xử lý tạo Email: ký tự đầu của Họ + ký tự đầu của Tên đệm + Tên chính
        # Ví dụ: n + v + an -> nvan@company.com
        email_username = ho[0] + ten_dem[0] + ten_chinh
        email = f"{email_username.lower()}@company.com"
        
        # Xử lý tạo Mã ID: Tên chính viết hoa + 2 số cuối năm sinh (Slicing)
        year_last_two = raw_year[-2:]
        member_id = f"{ten_chinh.upper()}{year_last_two}"
        
        # Chuẩn hóa lại họ tên đầy đủ để in lên thẻ
        full_name_clean = " ".join(name_elements).title()
        
        # In giao diện "Thẻ thành viên" vuông vức bằng kỹ thuật f-string định dạng căn lề
        print("\n" + "*" * 36)
        print(f"*{'THẺ THÀNH VIÊN CÂU LẠC BỘ':^34}*")
        print("*" * 36)
        print(f"* Họ và tên: {full_name_clean:<21}*")
        print(f"* Mã số ID : {member_id:<21}*")
        print(f"* Email    : {email:<21}*")
        print("*" * 36)
        
    # CHỨC NĂNG 4: Thoát chương trình hệ thống
    elif choice == "4":
        print("\nCảm ơn bạn đã sử dụng hệ thống. Chào tạm biệt!")
        break
        
    # XỬ LÝ NGOẠI LỆ: Người dùng nhập sai dải menu quy định
    else:
        print("\nLựa chọn không hợp lệ, vui lòng nhập lại!")