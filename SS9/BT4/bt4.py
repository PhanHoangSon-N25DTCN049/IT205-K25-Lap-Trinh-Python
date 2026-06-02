
# 1. Phân tích Input / Output:
#    - Input:
#        + Lựa chọn từ menu chính (1-4) và menu con (1-4): Kiểu chuỗi (str) để tránh lỗi khi nhập chữ.
#        + Chức năng thêm đơn: Mã đơn hàng (str), Trạng thái đơn hàng (str).
#        + Chức năng sửa/xóa: Vị trí đơn hàng cần tác động (nhập dạng str rồi chuyển sang int).
#    - Output:
#        + Các thông báo trạng thái thành công, thông báo lỗi trực quan trên màn hình console.
#        + Danh sách đơn hàng được cập nhật, định dạng chuẩn hóa dạng "MÃ_ĐƠN_HÀNG - TRẠNG_THÁI".
#        + Bảng thống kê chi tiết số lượng theo từng trạng thái cụ thể.

# 2. Đề xuất giải pháp và xử lý Edge Cases (Bẫy dữ liệu):
#    - Khởi tạo `order_list` chứa một số đơn hàng mẫu để test cấu trúc chuỗi.
#    - Dùng vòng lặp `while True` lồng nhau để quản lý luồng chuyển đổi giữa Menu chính và Menu con.
#    - Bẫy 1 (Chuẩn hóa): Dùng `.strip().upper()` cho cả mã và trạng thái trước khi nối chuỗi bằng toán tử f-string.
#    - Bẫy 2 & 3 (Sai vị trí / Nhập chữ): Dùng `.isdigit()` kiểm tra vị trí nhập vào có phải số nguyên dương không.
#      Sau đó chuyển đổi sang chỉ số index trong Python bằng công thức: index = vị trí - 1.
#      Kiểm tra tính hợp lệ của index bằng điều kiện: 0 <= index < len(order_list).
#    - Bẫy 4 (Sai menu): Sử dụng nhánh `else` cuối cùng trong cấu trúc rẽ nhánh để bắt các lựa chọn ngoài phạm vi.
#    - Bẫy 5 (Thống kê list rỗng): Dùng phương thức `.count()` hoặc duyệt chuỗi để đếm độc lập, đảm bảo list rỗng vẫn in ra mức số lượng bằng 0.

# 3. Thiết kế thuật toán (Pseudocode):
#    Khởi tạo order_list = ["GE001 - PENDING", "GE002 - DELIVERING", "GE003 - CANCELLED"]
#    Vòng lặp Menu Chính (while True):
#        In 4 lựa chọn Menu chính -> Nhập lua_chon_chinh
#        Nếu lua_chon_chinh == "1":
#            Nếu order_list rỗng -> In thông báo trống
#            Ngược lại -> Duyệt enumerate(order_list) và in ra theo định dạng STT. Đơn hàng
#        Nếu lua_chon_chinh == "2":
#            Vòng lặp Menu Con (while True):
#                In 4 lựa chọn Menu cập nhật -> Nhập lua_chon_con
#                Nếu lua_chon_con == "1" (Thêm):
#                    Nhập ma, nhập trang_thai -> Chuẩn hóa -> Ghép chuỗi -> append vào list
#                Nếu lua_chon_con == "2" (Sửa):
#                    Nhập vi_tri -> Nếu không phải số hoặc ngoài khoảng -> Báo lỗi
#                    Hợp lệ -> Nhập ma_moi, trang_thai_moi -> Chuẩn hóa -> Ghép chuỗi -> Gán vào list[index]
#                Nếu lua_chon_con == "3" (Xóa):
#                    Nhập vi_tri -> Nếu không hợp lệ -> Báo lỗi
#                    Hợp lệ -> Xóa phần tử bằng pop(index) -> In ra phần tử vừa xóa
#                Nếu lua_chon_con == "4" (Quay lại):
#                    break khỏi vòng lặp menu con
#                Ngược lại -> Báo lựa chọn không hợp lệ
#        Nếu lua_chon_chinh == "3":
#            Khởi tạo các biến đếm pending, delivering, completed, cancelled = 0
#            Duyệt qua từng item trong order_list:
#                Tách chuỗi tại ký tự " - " lấy phần trạng thái
#                Nếu trạng thái khớp ứng -> Tăng biến đếm tương ứng thêm 1
#            In bảng thống kê số lượng và tổng số đơn hàng
#        Nếu lua_chon_chinh == "4":
#            In "Thoát chương trình" -> break khỏi vòng lặp menu chính
#        Ngược lại -> Báo lựa chọn menu chính không hợp lệ

# Khởi tạo danh sách dữ liệu mẫu theo bối cảnh hệ thống
order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")
    
    chuyen_muc = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    if chuyen_muc == "1":
        if not order_list:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")
                
    elif chuyen_muc == "2":
        while True:
            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")
            
            sub_choice = input("Nhập lựa chọn cập nhật (1-4): ").strip()
            
            # 2.1. Thêm đơn hàng mới
            if sub_choice == "1":
                ma_don = input("Nhập mã đơn hàng: ").strip().upper()
                trang_thai = input("Nhập trạng thái đơn hàng (PENDING/DELIVERING/COMPLETED/CANCELLED): ").strip().upper()
                
                if ma_don == "" or trang_thai == "":
                    print("Không được để trống mã đơn hàng hoặc trạng thái!")
                else:
                    new_item = f"{ma_don} - {trang_thai}"
                    order_list.append(new_item)
                    print(f"Đã thêm thành công: {new_item}")
            
            # 2.2. Sửa đơn hàng theo vị trí
            elif sub_choice == "2":
                pos_input = input("Nhập vị trí cần sửa: ").strip()
                
                # Bẫy số 3: Kiểm tra đầu vào phải là ký tự số nguyên dương
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ!")
                else:
                    target_index = int(pos_input) - 1
                    # Bẫy số 2: Kiểm tra vị trí nằm trong phạm vi của List
                    if 0 <= target_index < len(order_list):
                        ma_moi = input("Nhập mã đơn hàng mới: ").strip().upper()
                        tt_moi = input("Nhập trạng thái mới: ").strip().upper()
                        
                        if ma_moi == "" or tt_moi == "":
                            print("Dữ liệu sửa đổi không được để trống!")
                        else:
                            order_list[target_index] = f"{ma_moi} - {tt_moi}"
                            print("Cập nhật đơn hàng thành công!")
                    else:
                        print("Không tồn tại đơn hàng ở vị trí này!")
            
            # 2.3. Xóa đơn hàng theo vị trí
            elif sub_choice == "3":
                pos_input = input("Nhập vị trí đơn hàng cần xóa: ").strip()
                
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ!")
                else:
                    target_index = int(pos_input) - 1
                    if 0 <= target_index < len(order_list):
                        # Thực hiện xóa và lưu vết phần tử bị xóa bỏ khỏi list
                        removed_order = order_list.pop(target_index)
                        print(f"Đã xóa thành công đơn hàng: {removed_order}")
                    else:
                        print("Không tồn tại đơn hàng ở vị trí này!")
                        
            # 2.4. Quay lại menu chính
            elif sub_choice == "4":
                break
                
            # Bẫy số 4: Sai lựa chọn menu con
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                
    elif chuyen_muc == "3":
        # Khởi tạo bộ đếm mặc định cho tất cả trạng thái (Bẫy số 5)
        count_pending = 0
        count_delivering = 0
        count_completed = 0
        count_cancelled = 0
        
        # Duyệt mảng và phân tách chuỗi con để trích xuất trạng thái thống kê
        for item in order_list:
            if " - " in item:
                # Tách chuỗi tại vị trí ký tự nối " - ", lấy phần tử thứ 2 (chỉ số 1) làm trạng thái
                parts = item.split(" - ")
                status = parts[1].strip()
                
                if status == "PENDING":
                    count_pending += 1
                elif status == "DELIVERING":
                    count_delivering += 1
                elif status == "COMPLETED":
                    count_completed += 1
                elif status == "CANCELLED":
                    count_cancelled += 1
                    
        print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
        print(f"PENDING: {count_pending}")
        print(f"DELIVERING: {count_delivering}")
        print(f"COMPLETED: {count_completed}")
        print(f"CANCELLED: {count_cancelled}")
        print(f"Tổng số đơn hàng: {len(order_list)}")
        
    elif chuyen_muc == "4":
        print("Thoát chương trình")
        break
        
    # Bẫy số 4: Sai lựa chọn menu chính
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")