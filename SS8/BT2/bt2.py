# Khởi tạo các biến toàn cục dạng chuỗi để lưu trữ dữ liệu sản phẩm
shop_name = ""
product_name = ""
describe = ""
category = ""
keywords = ""

while True:
    print("\n+======================================================+")
    print("| HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPPEE           |")
    print("+======================================================+")
    print("| 1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê     |")
    print("| 2. Chuẩn hóa tên shop                                |")
    print("| 3. Kiểm tra mã giảm giá hợp lệ                       |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm |")
    print("| 5. Thoát chương trình                                |")
    print("+======================================================+")
    
    choice = input("> Mời bạn chọn chức năng (1 -> 5): ").strip()
    
    match choice:
        case "5":
            print("Thoát chương trình")
            break
            
        case "1":
            # --- CHỨC NĂNG 1: NHẬP DỮ LIỆU VÀ XEM BÁO CÁO THỐNG KÊ ---
            
            # Bẫy 1: Tên Shop không được bỏ trống
            while True:
                shop_name_input = input("Nhập tên shop: ").strip()
                if shop_name_input == "":
                    print("Tên shop không được bỏ trống")
                else:
                    shop_name = shop_name_input
                    break
            
            # Nhập tên sản phẩm
            product_name = input("Nhập tên sản phẩm: ").strip().title()
            
            # Bẫy 2: Nhập mô tả sản phẩm rỗng hoặc chỉ chứa khoảng trắng
            while True:
                describe_input = input("Nhập mô tả sản phẩm: ").strip()
                if describe_input == "":
                    print("Mô tả sản phẩm không được rỗng")
                else:
                    describe = describe_input
                    break
                    
            # Nhập danh mục sản phẩm
            category_input = input("Nhập danh mục sản phẩm: ").strip().lower()
            # Chuẩn hóa khoảng trắng thừa giữa các từ trong danh mục sản phẩm
            category = ""
            has_space = False
            for char in category_input:
                if char != " ":
                    category += char
                    has_space = False
                else:
                    if not has_space:
                        category += " "
                        has_space = True
            category = category.strip()
            
            # Nhập danh sách từ khóa tìm kiếm cách nhau bởi dấu phẩy
            keywords_input = input("Danh sách từ khóa tìm kiếm (cách nhau bởi dấu ,): ").strip()
            
            # Chuẩn hóa chuỗi từ khóa và đếm số lượng từ khóa không dùng list
            keywords = ""
            temp_key = ""
            extended_keywords = keywords_input + ","
            count_keywords = 0
            
            for char in extended_keywords:
                if char != ",":
                    temp_key += char
                else:
                    clean_key = temp_key.strip()
                    if clean_key != "":
                        count_keywords += 1
                        if keywords == "":
                            keywords = clean_key
                        else:
                            keywords += ", " + clean_key
                    temp_key = ""

            # Thống kê số lượng từ hợp lệ trong mô tả sản phẩm (độ dài > 1)
            count_describe_words = 0
            current_word = ""
            extended_describe = describe + " "
            
            for char in extended_describe:
                if char != " ":
                    current_word += char
                else:
                    if len(current_word) > 1:
                        count_describe_words += 1
                    current_word = ""
            
            print("\n--- BÁO CÁO THỐNG KÊ SẢN PHẨM ---")
            print("Tên shop (loại bỏ khoảng trắng):", shop_name)
            print("Tên sản phẩm (chuẩn hóa title):", product_name)
            print("Mô tả sản phẩm:", describe)
            print("Độ dài mô tả sản phẩm:", len(describe))
            print("Số lượng từ hợp lệ trong mô tả:", count_describe_words)
            print("Danh mục sản phẩm (chuẩn hóa):", category)
            print("Danh sách từ khóa:", keywords)
            print("Số lượng từ khóa tìm kiếm:", count_keywords)
            print("Mô tả chữ thường:", describe.lower())
            print("Mô tả chữ hoa:", describe.upper())

        case "2":
            # --- CHỨC NĂNG 2: CHUẨN HÓA TÊN SHOP ---
            if shop_name == "":
                print("Chưa có dữ liệu tên shop. Vui lòng chạy Chức năng 1 trước!")
                continue
                
            # Loại bỏ khoảng trắng đầu cuối và chuyển thành chữ thường
            shop_lower = shop_name.lower()
            
            # Thay thế các khoảng trắng ở giữa các từ bằng dấu gạch ngang '-' (xử lý khoảng trắng thừa)
            shop_normalized = ""
            has_space = False
            for char in shop_lower:
                if char != " ":
                    shop_normalized += char
                    has_space = False
                else:
                    if not has_space:
                        shop_normalized += "-"
                        has_space = True
            
            # Thêm tiền tố 'shop-' ở đầu nếu chưa có
            if not shop_normalized.startswith("shop-"):
                shop_normalized = "shop-" + shop_normalized
                
            print("\n--- CHUẨN HÓA TÊN SHOP ---")
            print("Tên shop ban đầu:", shop_name)
            print("Tên shop sau khi được chuẩn hóa:", shop_normalized)

        case "3":
            # --- CHỨC NĂNG 3: KIỂM TRA MÃ GIẢM GIÁ HỢP LỆ ---
            if shop_name == "":
                print("Chưa khởi tạo thông tin sản phẩm. Vui lòng chạy Chức năng 1 trước!")
                continue
                
            coupon = input("Nhập mã giảm giá: ").strip()
            
            # Kiểm tra các quy tắc hợp lệ
            if coupon == "":
                print("Lỗi: Mã giảm giá không được rỗng")
            elif " " in coupon:
                print("Lỗi: Mã giảm giá không được chứa khoảng trắng")
            elif len(coupon) < 6 or len(coupon) > 12:
                print("Lỗi: Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
            elif not coupon.isupper():
                print("Lỗi: Mã giảm giá phải được viết hoa toàn bộ")
            elif not coupon.startswith("SALE"):
                print("Lỗi: Mã giảm giá phải bắt đầu bằng chuỗi SALE")
            else:
                # Kiểm tra mã chỉ được chứa chữ cái và chữ số
                is_alnum = True
                for char in coupon:
                    if not char.isalnum():
                        is_alnum = False
                        break
                        
                if is_alnum:
                    print("Mã giảm giá hợp lệ")
                else:
                    print("Lỗi: Mã giảm giá chỉ được chứa chữ cái và chữ số")

        case "4":
            # --- CHỨC NĂNG 4: TÌM KIẾM VÀ THAY THẾ TỪ KHÓA ---
            if describe == "":
                print("Chưa có dữ liệu mô tả sản phẩm. Vui lòng chạy Chức năng 1 trước!")
                continue
                
            search_word = input("Từ khóa cần tìm: ")
            replace_word = input("Từ khóa thay thế: ")
            
            if search_word in describe:
                occurrence_count = describe.count(search_word)
                describe = describe.replace(search_word, replace_word)
                
                print("\n--- KẾT QUẢ TÌM KIẾM & THAY THẾ ---")
                print("Số lần xuất hiện của từ khóa:", occurrence_count)
                print("Mô tả sau khi thay thế:", describe)
            else:
                print("Từ khóa cần tìm không tồn tại trong mô tả sản phẩm.")

        case _:
            # Bẫy 3 & Bẫy 4: Xử lý nhập chữ, ký tự đặc biệt hoặc số ngoài khoảng 1-5
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 5.")