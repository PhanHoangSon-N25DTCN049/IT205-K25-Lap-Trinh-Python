# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP:
# - Input: Số lượng chi nhánh (int), số học viên từng lớp (int). Mỗi chi nhánh cố định 2 lớp.
# - Output: Trạng thái của lớp học in ra ngay sau khi nhập.
# - Cấu trúc lặp:
#   + Vòng lặp ngoài (for): Duyệt qua từng chi nhánh.
#   + Vòng lặp giữa (for): Duyệt qua 2 lớp của mỗi chi nhánh.
#   + Vòng lặp trong cùng (while True): Yêu cầu nhập lại liên tục cho đến khi dữ liệu hợp lệ (>= 0).
# - Xử lý bẫy (Edge cases):
#   + Bẫy 1 (< 0): In cảnh báo và bắt vòng lặp while chạy lại bước nhập.
#   + Bẫy 2 (== 0): In thông báo bỏ qua, dùng 'break' thoát vòng lặp while để sang lớp tiếp theo.
# - Luồng chính (> 0): Kiểm tra điều kiện >= 20 hoặc < 20 để in trạng thái tương ứng, sau đó 'break'.

# (2) SOURCE CODE PYTHON HOÀN CHỈNH:
so_chi_nhanh = int(input("Nhập số lượng chi nhánh: "))
so_lop = 2

# Vòng lặp ngoài: Duyệt từng chi nhánh
for chi_nhanh in range(1, so_chi_nhanh + 1):
    print(f"Chi nhánh {chi_nhanh}:")
    
    for lop in range(1, so_lop + 1):
        
        while True:
            so_hoc_vien = int(input(f"Nhập số học viên đi học của lớp {lop}: "))
            
            if so_hoc_vien < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                continue # Quay lại đầu vòng lặp while
                
            elif so_hoc_vien == 0:
                print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
                break # Thoát vòng lặp while để chuyển sang lớp tiếp theo
                
            else:
                if so_hoc_vien >= 20:
                    print(f"Chi nhánh {chi_nhanh} - Lớp {lop}: Lớp học ổn định")
                else:
                    print(f"Chi nhánh {chi_nhanh} - Lớp {lop}: Lớp cần được nhắc nhở theo dõi")
                
                break # Thoát vòng lặp while sau khi đã đánh giá xong để chuyển sang lớp tiếp theo