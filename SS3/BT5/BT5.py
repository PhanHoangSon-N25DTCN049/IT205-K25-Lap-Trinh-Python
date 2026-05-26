
# 1. BẢNG THIẾT KẾ DỮ LIỆU (5 TRƯỜNG THÔNG TIN):
# ------------------------------------------------------------------------------
# | Tên biến          | Câu hỏi input                         | Kiểu dữ liệu | Điều kiện validation          |
# |-------------------|---------------------------------------|--------------|-------------------------------|
# | emp_id            | Nhập mã nhân viên (VD: NV001):        | String       | Không trống / không khoảng trắng|
# | emp_name          | Nhập họ và tên (VD: Nguyen Van A):     | String       | Không trống / không khoảng trắng|
# | base_salary       | Nhập mức lương cơ bản (VD: 15000000): | Integer      | Phải là số dương (> 0)        |
# | kpi_score         | Nhập điểm KPI năm (VD: 4.5):          | Float        | Nằm trong khoảng [1.0 - 5.0]  |
# | attendance_rate   | Nhập tỷ lệ chuyên cần (%) (VD: 98):   | Integer      | Nằm trong khoảng [0 - 100]    |


# 2. LUỒNG XỬ LÝ CHƯƠNG TRÌNH (PSEUDOCODE):
# BẮT ĐẦU
#     VÒNG LẶP CHÍNH (Chừng nào người dùng muốn tiếp tục):
#         VÒNG LẶP NHẬP emp_id -> Validation (Nếu trống thì bắt nhập lại)
#         VÒNG LẶP NHẬP emp_name -> Validation (Nếu trống thì bắt nhập lại)
#         VÒNG LẶP NHẬP base_salary -> Validation (Nếu <= 0 thì bắt nhập lại)
#         VÒNG LẶP NHẬP kpi_score -> Validation (Nếu ngoài khoảng 1.0 - 5.0 thì bắt nhập lại)
#         VÒNG LẶP NHẬP attendance_rate -> Validation (Nếu ngoài khoảng 0 - 100 thì bắt nhập lại)
#
#         IN HỒ SƠ NHÂN SỰ ĐIỆN TỬ (Định dạng hiển thị đẹp mắt, rõ ràng)
#         IN LOG HỆ THỐNG (Tên biến + Kiểu dữ liệu thông qua hàm type())
#
#         NHẬP lựa chọn tiếp tục (y/n)
#         NẾU lựa chọn là 'n' hoặc 'no' THÌ:
#             THOÁT VÒNG LẶP CHÍNH
# BÁT ĐẦU

print("==================================================")
print("     KIOSK HR TỰ PHỤC VỤ - TECHCORP SYSTEM        ")
print("==================================================")

# Vòng lặp tổng bao ngoài để quản lý nhập liên tục nhiều nhân viên
while True:
    print("\n--- BẮT ĐẦU CẬP NHẬT HỒ SƠ NHÂN VIÊN MỚI ---")

    # 1. Thu thập và ép lỗi Mã nhân viên (emp_id)
    while True:
        emp_id = input("Nhập mã nhân viên (VD: NV001): ").strip()
        if emp_id != "":
            break
        print("[LỖI ĐẦU VÀO] Mã nhân viên không được để trống!")

    # 2. Thu thập và ép lỗi Họ tên nhân viên (emp_name)
    while True:
        emp_name = input("Nhập họ và tên nhân viên (VD: Nguyen Van A): ").strip()
        if emp_name != "":
            break
        print("[LỖI ĐẦU VÀO] Họ tên nhân viên không được để trống!")

    # 3. Thu thập và ép lỗi Lương cơ bản (base_salary)
    while True:
        base_salary = int(input("Nhập mức lương cơ bản (VD: 15000000): "))
        if base_salary > 0:
            break
        print("[LỖI ĐẦU VÀO] Mức lương cơ bản phải là một số dương lớn hơn 0!")

    # 4. Thu thập và ép lỗi Điểm KPI (kpi_score)
    while True:
        kpi_score = float(input("Nhập điểm KPI năm (Thang 1.0 - 5.0) (VD: 4.5): "))
        if 1.0 <= kpi_score <= 5.0:
            break
        print("[LỖI ĐẦU VÀO] Điểm KPI không hợp lệ! Thang điểm bắt buộc từ 1.0 đến 5.0.")

    # 5. Thu thập và ép lỗi Tỷ lệ chuyên cần (attendance_rate)
    while True:
        attendance_rate = int(input("Nhập tỷ lệ chuyên cần (%) (VD: 98): "))
        if 0 <= attendance_rate <= 100:
            break
        print("[LỖI ĐẦU VÀO] Tỷ lệ chuyên cần không hợp lệ! Vui lòng nhập từ 0 đến 100.")


    # --- KHỐI IN KẾT QUẢ: HỒ SƠ ĐIỆN TỬ ---
    print("\n" + "="*45)
    print("         HỒ SƠ NHÂN SỰ ĐIỆN TỬ PHÁT HÀNH        ")
    print("="*45)
    print(f"Mã nhân viên     : {emp_id}")
    print(f"Họ và tên        : {emp_name}")
    print(f"Lương cơ bản     : {base_salary:,} VNĐ")
    print(f"Điểm hiệu suất   : {kpi_score} / 5.0")
    print(f"Tỷ lệ chuyên cần : {attendance_rate}%")
    print("-" * 45)
    print("Trạng thái hồ sơ : Đã đồng bộ lên Cloud của TechCorp")
    print("="*45)


    # --- KHỐI IN KẾT QUẢ: SYSTEM LOG ---
    print("\n" + "#"*45)
    print("                    SYSTEM LOG                ")
    print("#"*45)
    print(f"Biến 'emp_id'          -> Kiểu dữ liệu: {type(emp_id)}")
    print(f"Biến 'emp_name'        -> Kiểu dữ liệu: {type(emp_name)}")
    print(f"Biến 'base_salary'     -> Kiểu dữ liệu: {type(base_salary)}")
    print(f"Biến 'kpi_score'       -> Kiểu dữ liệu: {type(kpi_score)}")
    print(f"Biến 'attendance_rate' -> Kiểu dữ liệu: {type(attendance_rate)}")
    print("#"*45)


    # Vòng lặp kiểm tra lựa chọn tiếp tục của người dùng
    user_choice = input("\nTiếp tục nhập nhân viên khác? (y/n): ").strip().lower()
    if user_choice in ['n', 'no']:
        print("\n=== ĐÃ ĐÓNG KIOSK. CẢM ƠN BẠN ĐÃ SỬ DỤNG HỆ THỐNG! ===")
        break