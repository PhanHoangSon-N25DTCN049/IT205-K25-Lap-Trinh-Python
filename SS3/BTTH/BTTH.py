
# 1. PHÂN TÍCH INPUT / OUTPUT:
# ------------------------------------------------------------------------------
# * Input:
#   - Số lượng nhân viên (Số nguyên, bắt buộc lớn hơn 0).
#   - Vòng lặp chạy qua từng nhân viên để nhập: Tên nhân viên (Chuỗi), Số ngày đi làm (Số nguyên).
#   - Lựa chọn tiếp tục chương trình (Chuỗi ký tự: 'y' hoặc 'n').
# * Output:
#   - Hiển thị thông tin chi tiết của từng nhân viên ngay sau khi nhập.
#   - Đánh giá chuyên cần: "Cần cải thiện chuyên cần" (< 20 ngày) hoặc "Nhân viên chuyên cần tốt" (>= 20 ngày).
#
# 2. LUỒNG XỬ LÝ CHƯƠNG TRÌNH (PSEUDOCODE):
# ------------------------------------------------------------------------------
# BẮT ĐẦU
#     VÒNG LẶP CHÍNH (Chừng nào người dùng nhập 'y'):
#         NHẬP và ÉP KIỂU số lượng nhân viên (num_employees)
#         
#         VÒNG LẶP Duyệt qua từng nhân viên từ 1 đến num_employees:
#             NHẬP tên nhân viên (emp_name)
#             NHẬP số ngày đi làm (work_days)
#             
#             IN THÔNG TIN vừa nhập để xác nhận
#             
#             NẾU work_days < 20 THÌ:
#                 IN "Đánh giá: Cần cải thiện chuyên cần"
#             CÒN LẠI THÌ:
#                 IN "Đánh giá: Nhân viên chuyên cần tốt"
#                 
#         NHẬP lựa chọn tiếp tục (user_choice)
#         NẾU user_choice bằng 'n' THÌ:
#             THOÁT VÒNG LẶP CHÍNH
# KẾT THÚC
# ==============================================================================

while True:
    print("\n==================================================")
    print("       HỆ THỐNG QUẢN LÝ CHẤM CÔNG NHÂN VIÊN       ")
    print("==================================================")
    
    # 1. Nhập số lượng nhân viên (Có bẫy chặn số âm hoặc bằng 0)
    while True:
        num_employees = int(input("Nhập số lượng nhân viên cần quản lý: "))
        if num_employees > 0:
            break
        print("[LỖI] Số lượng nhân viên phải lớn hơn 0. Vui lòng nhập lại!")

    # 2. Vòng lặp nhập thông tin cho từng nhân viên
    for i in range(1, num_employees + 1):
        print(f"\n--- Nhập thông tin nhân viên thứ {i} ---")
        
        # Bẫy chặn không để trống tên
        while True:
            emp_name = input("Tên nhân viên: ").strip()
            if emp_name != "":
                break
            print("[LỖI] Tên nhân viên không được để trống!")
            
        # Bẫy chặn số ngày đi làm hợp lý trong tháng (0 - 31 ngày)
        while True:
            work_days = int(input("Số ngày đi làm: "))
            if 0 <= work_days <= 31:
                break
            print("[LỖI] Số ngày đi làm không hợp lệ (Phải từ 0 đến 31 ngày)!")

        # 3 & 4. Hiển thị thông tin và Đánh giá chuyên cần luôn cho nhân viên đó
        print("\n>> THÔNG TIN NHÂN VIÊN VỪA NHẬP:")
        print(f"Nhân viên: {emp_name}")
        print(f"Số ngày đi làm: {work_days} ngày")
        
        if work_days < 20:
            print("Đánh giá: Cần cải thiện chuyên cần")
        else:
            print("Đánh giá: Nhân viên chuyên cần tốt")
        print("-" * 35)

    # 5. Hỏi ý kiến người dùng để tiếp tục hoặc kết thúc chương trình
    print("\n==================================================")
    user_choice = input("Bạn có muốn tiếp tục chương trình không? (y/n): ").strip().lower()
    
    if user_choice == 'n':
        print("\n=== CHƯƠNG TRÌNH KẾT THÚC. CẢM ƠN BẠN ĐÃ SỬ DỤNG! ===")
        break