# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP:
# - Cấu trúc: Vòng lặp ngoài duyệt qua số lượng nhân viên. Vòng lặp trong (nested loop) dùng để in biểu đồ dấu '*'.
# - Xử lý bẫy (Edge cases) & Nghiệp vụ:
#   + Bẫy 1 (Số ngày < 0 hoặc > 22): In thông báo "Dữ liệu không hợp lệ" và dùng lệnh 'continue' bỏ qua nhân viên đó.
#   + Bẫy 2 (Số ngày == 0): In thông báo nhân viên nghỉ toàn bộ tháng.
#   + Đánh giá năng suất: Dùng cấu trúc if/elif/else để phân loại mức độ làm việc (>= 18, < 10, còn lại).

# (2) SOURCE CODE PYTHON:
so_nhan_vien = int(input("Nhập số lượng nhân viên: "))

for i in range(1, so_nhan_vien + 1):
    print(f"\n--- Nhân viên {i} ---")
    ten_nv = input("Nhập tên nhân viên: ")
    so_ngay_lam = int(input("Nhập số ngày làm: "))

    # Xử lý Bẫy 1: Kiểm tra dữ liệu hợp lệ
    if so_ngay_lam < 0 or so_ngay_lam > 22:
        print("Dữ liệu không hợp lệ")
        continue
        
    # Xử lý Bẫy 2: Kiểm tra nhân viên nghỉ toàn bộ
    if so_ngay_lam == 0:
        print(f"Nhân viên {ten_nv} nghỉ toàn bộ tháng")
        continue

    # Hiển thị biểu đồ ngày làm việc bằng nested loop
    print(f"Biểu đồ ngày làm của {ten_nv}: ", end="")
    for j in range(so_ngay_lam):
        print("*", end="")
    print() # Xuống dòng sau khi in xong biểu đồ

    # Thống kê mức độ làm việc
    if so_ngay_lam >= 18:
        print("Đánh giá: Làm việc chăm chỉ")
    elif so_ngay_lam < 10:
        print("Đánh giá: Làm việc ít")
    else:
        print("Đánh giá: Làm việc bình thường")