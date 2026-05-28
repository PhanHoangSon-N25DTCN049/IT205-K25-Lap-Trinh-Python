# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP:
# - Cấu trúc chương trình: Sử dụng vòng lặp while ở ngoài cùng để tạo Menu điều hướng liên tục.
# - Luồng dữ liệu (Chức năng 1): 
#   + Vòng lặp ngoài duyệt theo số lượng chi nhánh.
#   + Vòng lặp trong duyệt theo số lượng lớp của chi nhánh đó.
# - Xử lý bẫy (Edge cases):
#   + Bẫy 1 (Học viên < 0): Dùng vòng lặp while lồng ở bước nhập số học viên để ép nhập lại đến khi hợp lệ.
#   + Bẫy 2 (Menu không hợp lệ): Dùng lệnh if kiểm tra giá trị nhập vào, nếu ngoài danh sách cho phép thì dùng 'continue' để reset menu.
#   + Bẫy 3 (Không có lớp < 10): Lưu các lớp dưới 10 học viên vào một list. Nếu độ dài list = 0 thì in thông báo "Không có lớp nào dưới 10 học viên".

# (2) SOURCE CODE PYTHON:
def hien_thi_menu():
    print("\n=== HỆ THỐNG QUẢN LÝ THỐNG KÊ HỌC VIÊN ===")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Hiển thị hướng dẫn sử dụng")
    print("3. Thoát chương trình")
    print("==========================================")

while True:
    hien_thi_menu()
    lua_chon = input("Nhập lựa chọn của bạn (1-3): ")

    # Xử lý Bẫy 2: Lựa chọn menu không hợp lệ
    if lua_chon not in ['1', '2', '3']:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại chức năng từ 1 đến 3.")
        continue
        
    if lua_chon == '3':
        print("Thoát chương trình.")
        break
        
    elif lua_chon == '2':
        print("\n--- Hướng dẫn sử dụng ---")
        print("- Chọn chức năng 1 để tiến hành nhập số liệu.")
        print("- Khai báo lần lượt số chi nhánh, số lớp và sĩ số từng lớp.")
        print("- Sĩ số học viên nhập vào phải là số nguyên không âm (>= 0).")
        print("- Báo cáo sẽ được xuất ra tự động ngay trong lúc nhập liệu.")
        
    elif lua_chon == '1':
        # Nhập số chi nhánh
        while True:
            so_chi_nhanh = int(input("\nNhập tổng số chi nhánh: "))
            if so_chi_nhanh > 0:
                break
            print("Số lượng chi nhánh phải lớn hơn 0.")

        # Các biến dùng để thống kê tổng kết
        chi_nhanh_max_hoc_vien = 0
        max_hoc_vien = -1

        # Duyệt qua từng chi nhánh
        for chi_nhanh in range(1, so_chi_nhanh + 1):
            print(f"\n--- Nhập dữ liệu cho Chi nhánh {chi_nhanh} ---")
            
            while True:
                so_lop = int(input(f"Nhập số lượng lớp của Chi nhánh {chi_nhanh}: "))
                if so_lop > 0:
                    break
                print("Số lượng lớp phải lớn hơn 0.")

            tong_hoc_vien_chi_nhanh = 0
            danh_sach_lop_duoi_10 = []

            # Duyệt qua từng lớp của chi nhánh hiện tại
            for lop in range(1, so_lop + 1):
                # Xử lý Bẫy 1: Bắt buộc nhập số học viên >= 0
                while True:
                    so_hoc_vien = int(input(f"Nhập số lượng học viên của lớp {lop}: "))
                    if so_hoc_vien < 0:
                        print("Số học viên không thể là số âm. Vui lòng nhập lại.")
                    else:
                        break
                
                # Tính toán dữ liệu
                tong_hoc_vien_chi_nhanh += so_hoc_vien
                
                if so_hoc_vien < 10:
                    danh_sach_lop_duoi_10.append(lop)

            # So sánh để tìm ra chi nhánh có nhiều học viên nhất
            if tong_hoc_vien_chi_nhanh > max_hoc_vien:
                max_hoc_vien = tong_hoc_vien_chi_nhanh
                chi_nhanh_max_hoc_vien = chi_nhanh

            # Báo cáo ngay sau khi nhập xong 1 chi nhánh
            print(f"\n[Báo cáo Chi nhánh {chi_nhanh}]")
            print(f"- Tổng số học viên: {tong_hoc_vien_chi_nhanh}")
            
            # Xử lý Bẫy 3: Đánh giá lớp có sĩ số thấp
            if len(danh_sach_lop_duoi_10) == 0:
                print("- Đánh giá: Không có lớp nào dưới 10 học viên.")
            else:
                chuoi_lop = ", ".join([str(l) for l in danh_sach_lop_duoi_10])
                print(f"- Các lớp có sĩ số dưới 10 học viên cần hỗ trợ: Lớp {chuoi_lop}")

        # Báo cáo tổng kết sau khi kết thúc toàn bộ chi nhánh
        print("\n[BÁO CÁO TỔNG KẾT]")
        print(f"=> Chi nhánh có quy mô đào tạo lớn nhất là Chi nhánh {chi_nhanh_max_hoc_vien} với {max_hoc_vien} học viên.")