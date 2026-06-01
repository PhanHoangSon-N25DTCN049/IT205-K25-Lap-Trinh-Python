# Khởi tạo các biến toàn cục dạng chuỗi để lưu trữ dữ liệu video
user_name = ""
title = ""
describe = ""
hashtag = "" 

while True:
    print("\n+================================================+")
    print("| 1. Nhập và phân tích thông tin video           |")
    print("| 2. Chuẩn hóa tên tài khoản                     |")
    print("| 3. Kiểm tra tính hợp lệ của hashtag            |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong mô tả    |")
    print("| 5. Thoát chương trình                          |")
    print("+================================================+")
    
    choice = input("> Mời bạn chọn chức năng (1 -> 5): ").strip()
    
    match choice:
        case "5":
            print("Thoát chương trình")
            break
            
        case "1":
            # --- CHỨC NĂNG 1: NHẬP VÀ PHÂN TÍCH THÔNG TIN VIDEO ---
            
            # Bẫy 1: Tên tài khoản không được rỗng
            while True:
                user_name_input = input("Tên tài khoản người đăng video: ").strip()
                if user_name_input == "":
                    print("Tên tài khoản không được rỗng")
                else:
                    user_name = user_name_input
                    break
                    
            # Nhập và chuẩn hóa tiêu đề (viết hoa chữ cái đầu mỗi từ)
            while True:
                title_input = input("Tiêu đề video: ").strip()
                if title_input == "":
                    print("Tiêu đề không được bỏ trống. Vui lòng nhập lại!")
                else:
                    title = title_input.title()
                    break
                    
            # Bẫy 2: Nhập mô tả video không được rỗng
            while True:
                describe_input = input("Mô tả video: ").strip()
                if describe_input == "":
                    print("Mô tả video không được rỗng")
                else:
                    describe = describe_input
                    break
                    
            # Nhập danh sách hashtag thô
            hashtag_input = input("Danh sách hashtag cách nhau bằng dấu ,: ").strip()
            
            # Chuẩn hóa chuỗi hashtag không dùng list (loại bỏ khoảng trắng thừa quanh dấu phẩy)
            hashtag = ""
            temp_tag = ""
            extended_hashtag = hashtag_input + ","
            
            for char in extended_hashtag:
                if char != ",":
                    temp_tag += char
                else:
                    clean_tag = temp_tag.strip()
                    if clean_tag != "":
                        if hashtag == "":
                            hashtag = clean_tag
                        else:
                            hashtag += ", " + clean_tag
                    temp_tag = ""

            # Logic đếm từ nâng cao: Một ký tự đơn lẻ đứng độc lập không tính là 1 từ
            count_describe = 0
            current_word = ""
            extended_describe = describe + " "  # Thêm khoảng trắng ở cuối để xử lý từ cuối cùng
            
            for char in extended_describe:
                if char != " ":
                    current_word += char
                else:
                    if len(current_word) > 1:
                        count_describe += 1
                    current_word = ""

            # Logic đếm số lượng hashtag từ chuỗi đã chuẩn hóa
            count_hashtag = 0
            if hashtag != "":
                count_hashtag = 1
                for char in hashtag:
                    if char == ",":
                        count_hashtag += 1
                
            print("\n--- BÁO CÁO THỐNG KÊ VIDEO ---")
            print("Tên tài khoản: ", user_name)
            print("Tiêu đề: ", title)
            print("Mô tả: ", describe)
            print("Độ dài mô tả: ", len(describe))
            print("Số lượng từ trong mô tả: ", count_describe)
            print("Danh sách hashtag: ", hashtag)
            print("Số lượng hashtag: ", count_hashtag)
            print("Mô tả vid chữ thường: ", describe.lower())
            print("Mô tả vid chữ hoa: ", describe.upper())

        case "2":
            # --- CHỨC NĂNG 2: CHUẨN HÓA TÊN TÀI KHOẢN ---
            if user_name == "":
                print("Chưa có dữ liệu tài khoản. Vui lòng chạy Chức năng 1 trước!")
                continue
                
            username_normalized = "@" + user_name.lower()
            print("\n--- CHUẨN HÓA TÊN TÀI KHOẢN ---")
            print("Tên tài khoản ban đầu: ", user_name)
            print("Tên tài khoản sau khi được chuẩn hoá: ", username_normalized)

        case "3":
            # --- CHỨC NĂNG 3: KIỂM TRA HASHTAG HỢP LỆ ---
            if user_name == "":
                print("Chưa khởi tạo thông tin video. Vui lòng chạy Chức năng 1 trước!")
                continue
                
            single_hashtag = input("Nhập một hashtag cần kiểm tra: ").strip()
            
            if single_hashtag == "":
                print("Lỗi: Hashtag không được rỗng")
            elif not single_hashtag.startswith("#"):
                print("Lỗi: Hashtag phải bắt đầu bằng ký tự #")
            elif " " in single_hashtag:
                print("Lỗi: Hashtag không được chứa khoảng trắng")
            elif len(single_hashtag) < 2:
                print("Lỗi: Hashtag phải có ít nhất 2 ký tự, bao gồm cả ký tự #")
            else:
                # Kiểm tra các ký tự sau dấu # (chỉ chấp nhận chữ cái, chữ số, hoặc dấu gạch dưới)
                content_after_hash = single_hashtag[1:]
                is_valid = True
                
                for char in content_after_hash:
                    if not (char.isalnum() or char == "_"):
                        is_valid = False
                        break
                        
                if is_valid:
                    print("Hashtag hợp lệ")
                    # Cập nhật hashtag mới vào chuỗi hashtag tổng quản lý
                    if hashtag == "":
                        hashtag = single_hashtag
                    else:
                        hashtag += ", " + single_hashtag
                    print("Danh sách hashtag hiện tại: ", hashtag)
                else:
                    print("Lỗi: Hashtag chỉ nên sử dụng chữ cái, chữ số hoặc dấu gạch dưới sau ký tự #")

        case "4":
            # --- CHỨC NĂNG 4: TÌM KIẾM VÀ THAY THẾ TỪ KHÓA ---
            if describe == "":
                print("Chưa có dữ liệu mô tả video. Vui lòng chạy Chức năng 1 trước!")
                continue
                
            search_word = input("Nhập từ khóa cần tìm: ")
            replace_word = input("Nhập từ khóa thay thế: ")
            
            if search_word in describe:
                occurrence_count = describe.count(search_word)
                describe = describe.replace(search_word, replace_word)
                
                print("\n--- KẾT QUẢ TÌM KIẾM & THAY THẾ ---")
                print(f"Số lần từ khóa '{search_word}' xuất hiện trong mô tả: {occurrence_count}")
                print("Mô tả video sau khi thay thế: ", describe)
            else:
                print(f"Từ khóa '{search_word}' không tồn tại trong mô tả video.")

        case _:
            # Bẫy 3 & Bẫy 4: Xử lý toàn bộ các trường hợp nhập chuỗi (abc, @), số thực (2.5) hoặc ngoài khoảng 1-5
            print("Lựa chọn không hợp lệ! Vui lòng nhập lại số nguyên từ 1 đến 5.")