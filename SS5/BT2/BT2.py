# (1) PHÂN TÍCH LỖI:
# - Chi nhánh 1 hiển thị đúng (83): Vì lúc này biến tổng mới được khởi tạo bằng 0.
# - Chi nhánh 2 hiển thị sai (143): Do biến tổng không được reset, hệ thống tiếp tục lấy 83 (của CN1) + 60 (của CN2).
# - Chi nhánh 3 hiển thị sai (240): Tiếp tục cộng dồn lỗi, lấy 143 (của CN1+CN2) + 97 (của CN3).
# -> Nguyên nhân gốc rễ: Biến lưu tổng số học viên đặt ở bên ngoài vòng lặp chi nhánh, 
#    dẫn đến việc dữ liệu bị cộng dồn liên tục qua các vòng lặp thay vì tính riêng cho từng chi nhánh.

# (2) SOURCE CODE ĐÃ SỬA LỖI:
so_chi_nhanh = 3
so_lop = 3

# Vòng lặp ngoài: Duyệt từng chi nhánh
for chi_nhanh in range(1, so_chi_nhanh + 1):
    print(f"--- Nhập dữ liệu Chi nhánh {chi_nhanh} ---")
    
    # SỬA LỖI TẠI ĐÂY: Reset tổng số học viên về 0 mỗi khi bắt đầu tính cho một chi nhánh mới
    tong_hoc_vien_chi_nhanh = 0 
    
    # Vòng lặp trong: Duyệt từng lớp của chi nhánh đó
    for lop in range(1, so_lop + 1):
        so_hoc_vien = int(input(f"Nhập số lượng học viên lớp {lop}: "))
        tong_hoc_vien_chi_nhanh += so_hoc_vien
        
    # Hiển thị kết quả độc lập cho từng chi nhánh
    print(f"-> Kết quả: Chi nhánh {chi_nhanh} có {tong_hoc_vien_chi_nhanh} học viên\n")