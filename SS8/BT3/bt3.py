# Khởi tạo các biến toàn cục dạng chuỗi để lưu trữ dữ liệu đơn hàng
sender_name = ""
sender_phone = ""
pickup_address = ""
receiver_name = ""
receiver_phone = ""
delivery_address = ""
delivery_note = ""

while True:
    print("\n+======================================================+")
    print("| HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS               |")
    print("+======================================================+")
    print("| 1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê     |")
    print("| 2. Chuẩn hóa mã đơn hàng                             |")
    print("| 3. Ẩn số điện thoại khách hàng (Bảo mật)             |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong ghi chú        |")
    print("| 5. Thoát chương trình                                |")
    print("+======================================================+")
    
    choice = input("> Mời bạn chọn chức năng (1 -> 5): ").strip()
    
    match choice:
        case "5":
            print("Thoát chương trình")
            break
            
        case "1":
            # --- CHỨC NĂNG 1: NHẬP DỮ LIỆU ĐƠN HÀNG VÀ XEM BÁO CÁO ---
            
            # Nhập và chuẩn hóa thông tin người gửi
            while True:
                name_input = input("Nhập tên người gửi: ").strip()
                if name_input == "":
                    print("Tên người gửi không được bỏ trống")
                else:
                    sender_name = name_input.title()
                    break
            
            # Nhập SĐT người gửi kèm kiểm tra tính hợp lệ
            while True:
                phone_input = input("Nhập số điện thoại người gửi: ").strip()
                if phone_input == "":
                    print("Số điện thoại người gửi không được bỏ trống")
                elif not phone_input.isdigit():
                    print("Số điện thoại không hợp lệ")
                elif len(phone_input) != 10:
                    print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                else:
                    sender_phone = phone_input
                    break
                    
            # Nhập địa chỉ lấy hàng và loại bỏ khoảng trắng thừa ở giữa
            while True:
                addr_input = input("Nhập địa chỉ lấy hàng: ").strip()
                if addr_input == "":
                    print("Địa chỉ lấy hàng không được bỏ trống")
                else:
                    pickup_address = ""
                    has_space = False
                    for char in addr_input:
                        if char != " ":
                            pickup_address += char
                            has_space = False
                        else:
                            if not has_space:
                                pickup_address += " "
                                has_space = True
                    break

            # Nhập và chuẩn hóa thông tin người nhận
            while True:
                name_input = input("Nhập tên người nhận: ").strip()
                if name_input == "":
                    print("Tên người nhận không được bỏ trống")
                else:
                    receiver_name = name_input.title()
                    break
            
            # Nhập SĐT người nhận kèm kiểm tra tính hợp lệ (Bẫy 1, 2, 3)
            while True:
                phone_input = input("Nhập số điện thoại người nhận: ").strip()
                if phone_input == "":
                    print("Số điện thoại người nhận không được bỏ trống")
                elif not phone_input.isdigit():
                    print("Số điện thoại không hợp lệ")
                elif len(phone_input) != 10:
                    print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                else:
                    receiver_phone = phone_input
                    break
                    
            # Nhập địa chỉ giao hàng và loại bỏ khoảng trắng thừa ở giữa
            while True:
                addr_input = input("Nhập địa chỉ giao hàng: ").strip()
                if addr_input == "":
                    print("Địa chỉ giao hàng không được bỏ trống")
                else:
                    delivery_address = ""
                    has_space = False
                    for char in addr_input:
                        if char != " ":
                            delivery_address += char
                            has_space = False
                        else:
                            if not has_space:
                                delivery_address += " "
                                has_space = True
                    break
                    
            # Nhập ghi chú giao hàng (Bẫy 1: Không được rỗng)
            while True:
                note_input = input("Nhập ghi chú giao hàng: ").strip()
                if note_input == "":
                    print("Ghi chú giao hàng không được bỏ trống")
                else:
                    delivery_note = note_input
                    break

            # Thuật toán đếm số từ hợp lệ trong ghi chú (độ dài > 1)
            count_note_words = 0
            current_word = ""
            extended_note = delivery_note + " "
            
            for char in extended_note:
                if char != " ":
                    current_word += char
                else:
                    if len(current_word) > 1:
                        count_note_words += 1
                    current_word = ""
            
            print("\n--- BÁO CÁO THỐNG KÊ ĐƠN HÀNG ---")
            print("Tên người gửi (chuẩn hóa):", sender_name)
            print("Tên người nhận (chuẩn hóa):", receiver_name)
            print("Địa chỉ lấy hàng (chuẩn hóa):", pickup_address)
            print("Địa chỉ giao hàng (chuẩn hóa):", delivery_address)
            print("Ghi chú giao hàng:", delivery_note)
            print("Độ dài ghi chú giao hàng:", len(delivery_note))
            print("Số lượng từ trong ghi chú giao hàng:", count_note_words)
            print("Ghi chú giao hàng dạng chữ thường:", delivery_note.lower())
            print("Ghi chú giao hàng dạng chữ hoa:", delivery_note.upper())

        case "2":
            # --- CHỨC NĂNG 2: CHUẨN HÓA MÃ ĐƠN HÀNG ---
            order_id_raw = input("Nhập mã đơn hàng cần chuẩn hóa: ").strip()
            
            if order_id_raw == "":
                print("Lỗi: Mã đơn hàng không được để trống")
                continue
                
            # Chuyển toàn bộ sang chữ hoa
            order_id_upper = order_id_raw.upper()
            
            # Thay thế tất cả khoảng trắng ở giữa bằng dấu gạch ngang '-'
            order_id_clean = ""
            has_space = False
            for char in order_id_upper:
                if char != " ":
                    order_id_clean += char
                    has_space = False
                else:
                    if not has_space:
                        order_id_clean += "-"
                        has_space = True
                        
            # Tự động thêm tiền tố 'GRAB-' nếu chưa có ở đầu mã
            if not order_id_clean.startswith("GRAB-"):
                order_id_normalized = "GRAB-" + order_id_clean
            else:
                order_id_normalized = order_id_clean
                
            print("\n--- CHUẨN HÓA MÃ ĐƠN HÀNG ---")
            print("Mã đơn hàng ban đầu:", order_id_raw)
            print("Mã đơn hàng sau khi được chuẩn hóa:", order_id_normalized)

        case "3":
            # --- CHỨC NĂNG 3: ẨN SỐ ĐIỆN THOẠI KHÁCH HÀNG ---
            if sender_phone == "" or receiver_phone == "":
                print("Chưa có dữ liệu đơn hàng. Vui lòng chạy Chức năng 1 trước!")
                continue
                
            # Áp dụng quy tắc ẩn thông tin bằng slicing thuần túy
            hidden_sender_phone = sender_phone[:3] + "*****" + sender_phone[8:]
            hidden_receiver_phone = receiver_phone[:3] + "*****" + receiver_phone[8:]
            
            print("\n--- THÔNG TIN SỐ ĐIỆN THOẠI BẢO MẬT ---")
            print("SĐT người gửi:", hidden_sender_phone)
            print("SĐT người nhận:", hidden_receiver_phone)

        case "4":
            # --- CHỨC NĂNG 4: TÌM KIẾM VÀ THAY THẾ TRONG GHI CHÚ ---
            # Bẫy 4: Chưa nhập thông tin đơn hàng ở chức năng 1
            if delivery_note == "":
                print("Chưa có ghi chú giao hàng để tìm kiếm")
                continue
                
            search_word = input("Từ khóa cần tìm: ")
            replace_word = input("Từ khóa thay thế: ")
            
            if search_word in delivery_note:
                occurrence_count = delivery_note.count(search_word)
                delivery_note = delivery_note.replace(search_word, replace_word)
                
                print("\n--- KẾT QUẢ TÌM KIẾM & THAY THẾ ---")
                print("Số lần xuất hiện của từ khóa:", occurrence_count)
                print("Ghi chú đơn hàng sau khi thay thế:", delivery_note)
            else:
                print("Từ khóa cần tìm không tồn tại trong ghi chú giao hàng.")

        case _:
            # Bẫy 5 & Bẫy 6: Xử lý nhập chữ, nhập ký tự đặc biệt hoặc số nằm ngoài khoảng 1-5
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 5.")