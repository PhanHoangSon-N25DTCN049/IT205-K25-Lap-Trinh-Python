# 1. Phân tích Input / Output:
#    - Input:
#        + Lựa chọn từ menu (1-5): Kiểu chuỗi (str) để tránh crash chương trình khi nhập chữ.
#        + Mã đơn hàng cần xử lý khi chọn chức năng 2, 3, 4: Kiểu chuỗi (str).
#    - Output:
#        + Trạng thái đơn hàng trong list được cập nhật trực tiếp theo đúng luồng.
#        + Các thông báo lỗi hoặc thông báo thành công tương ứng với từng nghiệp vụ.

# 2. Đề xuất giải pháp và xử lý Edge Cases (Bẫy dữ liệu):
#    - Quản lý danh sách bằng một List `order_list` chứa các chuỗi định dạng "MÃ - TRẠNG_THÁI".
#    - Dùng vòng lặp `while True` để chạy menu liên tục.
#    - Bẫy 1 (Chuẩn hóa): Mã đơn hàng nhập vào luôn được xử lý bằng `.strip().upper()` để loại khoảng trắng và viết hoa.
#    - Bẫy 2 (Không tồn tại): Duyệt qua danh sách để kiểm tra mã đơn nhập vào có khớp với phần mã trong danh sách không. 
#      Nếu duyệt hết list mà không thấy thì báo "Không tìm thấy mã đơn hàng."
#    - Bẫy 3, 4, 5 (Sai trạng thái): Tách chuỗi bằng `.split(" - ")` để kiểm tra trạng thái hiện tại trước khi xử lý. 
#      Chỉ cập nhật nếu trạng thái hiện tại đúng luồng logic yêu cầu.
#    - Bẫy 6 (Sai menu): Sử dụng `else` ở cuối nhánh menu chính để bắt các trường hợp nhập sai lựa chọn 1-5.

# 3. Thiết kế thuật toán (Pseudocode):
#    Khởi tạo order_list = ["GE001 - PENDING", "GE002 - ASSIGNED", "GE003 - DELIVERING"]
#    Vòng lặp vô hạn:
#        Hiển thị MENU điều phối gồm 5 lựa chọn
#        Nhập lua_chon
#        Nếu lua_chon == "1":
#            Nếu order_list trống -> In "Danh sách đơn hàng hiện đang trống."
#            Ngược lại -> Duyệt và in kèm STT bằng `enumerate`
#        Nếu lua_chon == "2" hoặc "3" hoặc "4":
#            Nhập ma_don -> Chuẩn hóa bằng strip().upper()
#            Đặt biến tim_thay = False
#            Duyệt qua từng đơn hàng trong order_list bằng index:
#                Tách đơn hàng thành ma_hien_tai và trang_thai_hien_tai
#                Nếu ma_don == ma_hien_tai:
#                    tim_thay = True
#                    Xử lý logic tương ứng với từng chức năng (Kiểm tra trạng thái cũ -> Cập nhật trạng thái mới)
#                    Dừng duyệt vòng lặp (break)
#            Nếu tim_thay == False -> In "Không tìm thấy mã đơn hàng."
#        Nếu lua_chon == "5":
#            In "Thoát chương trình" -> Dừng vòng lặp (break)
#        Ngược lại -> In "Lựa chọn không hợp lệ, vui lòng nhập lại!"



# Khởi tạo danh sách đơn hàng ban đầu theo bối cảnh hệ thống
order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:
    print("\n===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Gán tài xế cho đơn hàng")
    print("3. Cập nhật trạng thái giao hàng")
    print("4. Hủy đơn hàng")
    print("5. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    # --- CHỨC NĂNG 1: HIỂN THỊ DANH SÁCH ĐƠN HÀNG ---
    if choice == "1":
        if not order_list:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")
                
    # --- CHỨC NĂNG 2: GÁN TÀI XẾ CHO ĐƠN HÀNG ---
    elif choice == "2":
        search_code = input("Nhập mã đơn hàng cần gán tài xế: ").strip().upper() # Bẫy 1
        found = False
        
        for i in range(len(order_list)):
            parts = order_list[i].split(" - ")
            order_code = parts[0].strip()
            status = parts[1].strip()
            
            if order_code == search_code:
                found = True
                # Bẫy 3: Chỉ được gán tài xế cho đơn hàng PENDING
                if status == "PENDING":
                    order_list[i] = f"{order_code} - ASSIGNED"
                    print(f"Cập nhật thành công: {order_list[i]}")
                else:
                    print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")
                break
                
        if not found: # Bẫy 2
            print("Không tìm thấy mã đơn hàng.")
            
    # --- CHỨC NĂNG 3: CẬP NHẬT TRẠNG THÁI GIAO HÀNG ---
    elif choice == "3":
        search_code = input("Nhập mã đơn hàng cần cập nhật trạng thái: ").strip().upper() # Bẫy 1
        found = False
        
        for i in range(len(order_list)):
            parts = order_list[i].split(" - ")
            order_code = parts[0].strip()
            status = parts[1].strip()
            
            if order_code == search_code:
                found = True
                # Bẫy 4: Kiểm tra luồng cập nhật trạng thái
                if status == "ASSIGNED":
                    order_list[i] = f"{order_code} - DELIVERING"
                    print(f"Cập nhật thành công: {order_list[i]}")
                elif status == "DELIVERING":
                    order_list[i] = f"{order_code} - COMPLETED"
                    print(f"Cập nhật thành công: {order_list[i]}")
                elif status == "PENDING":
                    print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")
                elif status == "COMPLETED":
                    print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")
                elif status == "CANCELLED":
                    print("Đơn hàng đã bị hủy, không thể cập nhật.")
                break
                
        if not found: # Bẫy 2
            print("Không tìm thấy mã đơn hàng.")
            

    elif choice == "4":
        search_code = input("Nhập mã đơn hàng cần hủy: ").strip().upper() # Bẫy 1
        found = False
        
        for i in range(len(order_list)):
            parts = order_list[i].split(" - ")
            order_code = parts[0].strip()
            status = parts[1].strip()
            
            if order_code == search_code:
                found = True
                # Bẫy 5: Kiểm tra điều kiện hủy đơn hàng
                if status == "PENDING" or status == "ASSIGNED":
                    order_list[i] = f"{order_code} - CANCELLED"
                    print(f"Cập nhật thành công: {order_list[i]}")
                elif status == "DELIVERING":
                    print("Đơn hàng đang được giao, không thể hủy.")
                elif status == "COMPLETED":
                    print("Đơn hàng đã hoàn tất, không thể hủy.")
                elif status == "CANCELLED":
                    print("Đơn hàng đã được hủy trước đó.")
                break
                
        if not found: # Bẫy 2
            print("Không tìm thấy mã đơn hàng.")
            

    elif choice == "5":
        print("Thoát chương trình")
        break
        

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")