# 1. Phân tích Input / Output:
#    - Input:
#        + Ba danh sách song song lưu thông tin chi nhánh: branch_names (str), daily_revenues (int), target_achieved (bool).
#        + Lựa chọn từ menu của người dùng (1-4): Nhập dạng chuỗi (str) để chống crash khi người dùng nhập chữ cái.
#    - Output:
#        + Chức năng 1: Bảng báo cáo doanh thu, chuyển True/False thành Đạt/Không Đạt, in tổng doanh thu.
#        + Chức năng 2: Tên và doanh thu của chi nhánh cao nhất và thấp nhất.
#        + Chức năng 3: Danh sách failed_branches chứa các chi nhánh không đạt chỉ tiêu.
#        + Chức năng 4: Lời chào và thoát chương trình.

# 2. Đề xuất giải pháp và xử lý Edge Cases (Bẫy dữ liệu):
#    - Duy trì menu chạy liên tục bằng vòng lặp while True.
#    - Chức năng 1: Duyệt bằng range(len(...)) để lấy dữ liệu đồng bộ từ cả 3 danh sách song song theo cùng một index.
#    - Chức năng 2: Dùng max() và min() trên list daily_revenues, sau đó dùng phương thức .index() để truy ngược lại vị trí tương ứng trong list tên.
#    - Chức năng 3: Khởi tạo list rỗng failed_branches = [], duyệt và .append() nếu trạng thái là False.
#    - Bẫy dữ liệu (Menu Validation): Dùng cấu trúc if-elif-else để lọc. Nếu lựa chọn không nằm trong từ "1" đến "4", hệ thống sẽ thông báo lỗi bằng tiếng Việt và tự động lặp lại menu mà không bị dừng chương trình đột ngột.

# 3. Thiết kế thuật toán (Pseudocode):
#    Khởi tạo 3 danh sách dữ liệu thô ban đầu
#    Vòng lặp vô hạn (while True):
#        Hiển thị MENU gồm 4 lựa chọn chức năng
#        Nhập lua_chon từ bàn phím và loại bỏ khoảng trắng bằng .strip()
#        Nếu lua_chon == "1":
#            Duyệt qua danh sách bằng biến i chạy từ 0 đến len(branch_names) - 1:
#                Nếu target_achieved[i] == True -> trang_thai = "Đạt"
#                Ngược lại -> trang_thai = "Không Đạt"
#                In ra dòng dữ liệu căn lề
#            Tính tong_doanh_thu = sum(daily_revenues) và in ra cuối bảng
#        Nếu lua_chon == "2":
#            Tim doanh_thu_cao = max(daily_revenues) -> index_cao = daily_revenues.index(doanh_thu_cao)
#            Tim doanh_thu_thap = min(daily_revenues) -> index_thap = daily_revenues.index(doanh_thu_thap)
#            In ra tên chi nhánh tương ứng tại index_cao và index_thap
#        Nếu lua_chon == "3":
#            Khởi tạo failed_branches = []
#            Duyệt qua danh sách, nếu target_achieved[i] == False:
#                failed_branches.append(branch_names[i])
#            In ra danh sách failed_branches
#        Nếu lua_chon == "4":
#            In lời chào tạm biệt -> break để thoát vòng lặp
#        Ngược lại (Bẫy lỗi nhập sai menu):
#            In "[Loi] Lua chon khong hop le, vui long nhap lai so tu 1 den 4!"



# Khởi tạo dữ liệu thô ban đầu của hệ thống
branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False]

while True:
    # Hiển thị giao diện menu điều hướng
    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
    print("4. Thoát chương trình")
    print("================================================")
    
    user_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    # CHỨC NĂNG 1: HIỂN THỊ BÁO CÁO DOANH THU TỔNG HỢP
    if user_choice == "1":
        print("\n--- BÁO CÁO DOANH THU CHI TIẾT ---")
        # Sử dụng kỹ thuật định dạng chuỗi để tạo bảng căn lề ngay ngắn
        print(f"{'STT':<5} | {'Tên Chi Nhánh':<25} | {'Doanh Thu (VNĐ)':<15} | {'Trạng Thái'}")
        print("-" * 60)
        
        # Duyệt qua các danh sách song song bằng index
        for i in range(len(branch_names)):
            # Chuyển đổi định dạng hiển thị trạng thái đạt chỉ tiêu
            if target_achieved[i] == True:
                status_text = "Đạt"
            else:
                status_text = "Không Đạt"
            
            # In thông tin từng chi nhánh đã căn lề và định dạng số doanh thu cho dễ nhìn
            print(f"{i + 1:<5} | {branch_names[i]:<25} | {daily_revenues[i]:<15,} | {status_text}")
            
        print("-" * 60)
        # Tính toán và in ra tổng doanh thu toàn bộ các cơ sở
        total_revenue = sum(daily_revenues)
        print(f"Tổng doanh thu hệ thống: {total_revenue:,} VNĐ")
        
    # CHỨC NĂNG 2: THỐNG KÊ CHI NHÁNH CAO NHẤT / THẤP NHẤT
    elif user_choice == "2":
        print("\n--- THỐNG KÊ DOANH THU ĐỈNH ĐIỂM ---")
        
        # Tìm doanh thu lớn nhất và truy vết index ngược lại danh sách tên
        max_revenue = max(daily_revenues)
        max_index = daily_revenues.index(max_revenue)
        
        # Tìm doanh thu nhỏ nhất và truy vết index ngược lại danh sách tên
        min_revenue = min(daily_revenues)
        min_index = daily_revenues.index(min_revenue)
        
        # Hiển thị thông tin kết quả tiếng Việt có dấu
        print(f"Chi nhánh có doanh thu CAO NHẤT: {branch_names[max_index]} ({max_revenue:,} VNĐ)")
        print(f"Chi nhánh có doanh thu THẤP NHẤT: {branch_names[min_index]} ({min_revenue:,} VNĐ)")
        
    # CHỨC NĂNG 3: LỌC DANH SÁCH CƠ SỞ KÉM (KHÔNG ĐẠT CHỈ TIÊU)
    elif user_choice == "3":
        print("\n--- DANH SÁCH CƠ SỞ CHƯA ĐẠT CHỈ TIÊU ---")
        # Tạo danh sách rỗng mới để lưu trữ các cơ sở yếu kém
        failed_branches = []
        
        # Quét danh sách dữ liệu để tìm các vị trí có trạng thái False
        for i in range(len(target_achieved)):
            if target_achieved[i] == False:
                # Dùng phương thức .append() thêm tên chi nhánh vào danh sách mới
                failed_branches.append(branch_names[i])
                
        # In cấu trúc danh sách failed_branches ra màn hình để báo cáo nhân sự
        print("failed_branches =", failed_branches)
        print(f"-> Phát hiện có {len(failed_branches)} cơ sở chưa đạt chỉ tiêu ngày.")
        
    # CHỨC NĂNG 4: THOÁT CHƯƠNG TRÌNH
    elif user_choice == "4":
        print("\nHệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
        # Bẻ gãy vòng lặp while True để dừng chương trình một cách an toàn
        break
        
    # XỬ LÝ NGOẠI LỆ (BẪY DỮ LIỆU MENU VALIDATION)
    else:
        print("\n[Loi] Lua chon khong hop le, vui long nhap lai so tu 1 den 4!")