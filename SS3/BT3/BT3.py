""" 
Dữ liệu đầu vào (Input): Lặp lại 3 lần cho 3 nhân sự, mỗi lần nhập:
employee_id (String): Mã nhân viên.
full_name (String): Họ và tên nhân viên
department (String): Phòng ban công tác.
Dữ liệu đầu ra (Output): * Nếu dữ liệu hợp lệ: In ra Phiếu Hồ sơ Điện tử định dạng rõ ràng.
Nếu vi phạm bẫy dữ liệu: In ra cảnh báo lỗi cụ thể và lập tức bỏ qua việc in phiếu của nhân sự đó.

Sử dụng vòng lặp for i in range(1, 4) để kiểm soát đúng 3 lượt nhập liệu.
Để bắt lỗi khoảng trắng hoặc bỏ trống (Edge Cases), ta sử dụng phương thức .strip().
Nếu employee_id.strip() == "" hoặc full_name.strip() == "", hệ thống sẽ kích hoạt lệnh continue để bỏ qua lượt này và chuyển sang người tiếp theo.
"""

print("=== HỆ THỐNG KHIÓK NHẬP LIỆU NHÂN SỰ SỐ ===")

# Vòng lặp cố định đúng 3 lần tương ứng với 3 nhân sự mới
for i in range(1, 4):
    print(f"\n[LƯỢT NHẬP THỨ {i}/3] - Vui lòng điền thông tin:")
    
    employee_id = input("Nhập mã nhân viên: ")
    full_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban công tác: ")
    
    # Xử lý Edge Cases: Bẫy bỏ trống dữ liệu hoặc chỉ nhập khoảng trắng
    if employee_id.strip() == "" or full_name.strip() == "":
        print("LỖI: Mã nhân viên và Họ tên không được để trống hoặc chứa toàn khoảng trắng!")
        print("-> Hệ thống huỷ bỏ lượt khởi tạo này.")
        continue  # Nhảy sang lượt lặp tiếp theo, tuyệt đối không in phiếu
        
    # Xuất Phiếu Hồ sơ Điện tử khi dữ liệu hoàn toàn hợp lệ
    print("        PHIẾU HỒ SƠ NHÂN SỰ ĐIỆN TỬ      ")
    print(f"Mã nhân viên : {employee_id.strip()}")
    print(f"Họ và tên    : {full_name.strip()}")
    print(f"Phòng ban    : {department.strip() if department.strip() != '' else 'Chưa cập nhật'}")
    print("   [Trạng thái: Khởi tạo tài khoản thành công]   ")

print("\n=== TIẾN TRÌNH HOÀN THÀNH: Đã xử lý xong danh sách onboarding hôm nay! ===")