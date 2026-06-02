# 1. Phân tích Input / Output:
#    - Input: 
#        + Lựa chọn chức năng của người dùng (1, 2, 3, 4) nhập từ bàn phím (kiểu chuỗi/số).
#        + Mã đơn hàng mới khi thêm, hoặc mã đơn hàng cần xóa (kiểu chuỗi).
#    - Output:
#        + Giao diện menu và các thông báo phản hồi tương ứng với từng chức năng.
#        + Danh sách đơn hàng được cập nhật trực tiếp sau khi thêm hoặc xóa.

# 2. Đề xuất giải pháp:
#    - Dùng một danh sách `order_list` để lưu trữ mã đơn hàng ban đầu.
#    - Sử dụng vòng lặp `while True` để duy trì menu hệ thống chạy liên tục cho đến khi chọn thoát.
#    - Sử dụng phương thức `.strip()` để xóa khoảng trắng và `.upper()` để viết hoa mã đơn hàng khi xử lý dữ liệu đầu vào.
#    - Dùng cấu trúc `if-elif-else` để phân nhánh các lựa chọn menu và bắt bẫy dữ liệu lỗi (Edge Cases).

# 3. Thiết kế thuật toán (Pseudocode):
#    Khởi tạo order_list = ["GE001", "GE002", "GE003"]
#    Vòng lặp vô hạn:
#        Hiển thị MENU gồm 4 chức năng
#        Nhập lua_chon từ người dùng
#        Nếu lua_chon == "1":
#            Nếu danh sách rỗng -> In "Danh sách đơn hàng hiện đang trống."
#            Ngược lại -> Duyệt qua danh sách và in kèm số thứ tự (dùng enumerate)
#        Nếu lua_chon == "2":
#            Nhập ma_moi
#            Chuẩn hóa: ma_moi = ma_moi.strip().upper()
#            Thêm vào cuối: order_list.append(ma_moi)
#        Nếu lua_chon == "3":
#            Nhập ma_xoa
#            Chuẩn hóa: ma_xoa = ma_xoa.strip().upper()
#            Nếu ma_xoa có trong order_list -> order_list.remove(ma_xoa)
#            Ngược lại -> In "Không tìm thấy mã đơn hàng cần xóa!"
#        Nếu lua_chon == "4":
#            In "Thoát chương trình." -> Dừng vòng lặp (break)
#            Ngược lại -> In "Lựa chọn không hợp lệ, vui lòng nhập lại!"

# Khởi tạo danh sách đơn hàng ban đầu theo bối cảnh hệ thống
order_list = ["GE001", "GE002", "GE003"]

while True:
    # Hiển thị giao diện menu hệ thống
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")
    
    user_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    # Chức năng 1: Hiển thị danh sách đơn hàng
    if user_choice == "1":
        if not order_list:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")
                
    # Chức năng 2: Thêm đơn hàng mới
    elif user_choice == "2":
        new_order = input("Nhập mã đơn hàng mới: ")
        # Bẫy 1: Chuẩn hóa khoảng trắng hai đầu và chuyển thành chữ hoa
        standardized_order = new_order.strip().upper()
        
        if standardized_order == "":
            print("Mã đơn hàng không được để trống!")
        else:
            order_list.append(standardized_order)
            print(f"Đã thêm thành công đơn hàng: {standardized_order}")
            
    # Chức năng 3: Xóa đơn hàng theo mã
    elif user_choice == "3":
        cancel_order = input("Nhập mã đơn hàng cần xóa: ")
        # Chuẩn hóa dữ liệu nhập vào để tìm kiếm chính xác hơn
        standardized_cancel = cancel_order.strip().upper()
        
        # Bẫy 2: Kiểm tra sự tồn tại của đơn hàng trước khi tiến hành xóa
        if standardized_cancel in order_list:
            order_list.remove(standardized_cancel)
            print(f"Đã xóa thành công đơn hàng: {standardized_cancel}")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")
            
    # Chức năng 4: Thoát chương trình
    elif user_choice == "4":
        print("Thoát chương trình.")
        break
        
    # Bẫy 3: Người dùng nhập sai ngoài phạm vi lựa chọn từ 1-4 hoặc nhập chữ cái
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")