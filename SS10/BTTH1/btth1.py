# Khởi tạo dữ liệu mẫu ban đầu cho giỏ hàng Shopee
cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    # Hiển thị menu hệ thống
    print("\n===== HỆ THỐNG QUẢN LÝ GIỎ HÀNG SHOPEE =====")
    print("1. Xem chi tiết giỏ hàng và Tổng tiền")
    print("2. Thêm sản phẩm mới hoặc Tăng số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("============================================")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    # Sử dụng cấu trúc match-case để điều hướng menu và xử lý lỗi Validation (Bẫy 3)
    match choice:
        # CHỨC NĂNG 1: XEM CHI TIẾT GIỎ HÀNG VÀ TỔNG TIỀN
        case "1":
            if not cart_items:
                print("Giỏ hàng của bạn đang trống.")
            else:
                print("\n--- CHI TIẾT GIỎ HÀNG ---")
                print(f"{'STT':<5} | {'Mã SP':<8} | {'Tên Sản Phẩm':<25} | {'Số Lượng':<10} | {'Đơn Giá (đ)':<12} | {'Thành Tiền (đ)'}")
                print("-" * 80)
                
                total_quantity = 0
                total_amount = 0
                
                for index, item in enumerate(cart_items, start=1):
                    product_id = item[0]
                    product_name = item[1]
                    quantity = item[2]
                    price = item[3]
                    subtotal = quantity * price
                    
                    total_quantity += quantity
                    total_amount += subtotal
                    
                    print(f"{index:<5} | {product_id:<8} | {product_name:<25} | {quantity:<10} | {price:<12,} | {subtotal:,}")
                    
                print("-" * 80)
                print(f"Tổng số lượng sản phẩm: {total_quantity}")
                print(f"Tổng tiền toàn bộ giỏ hàng: {total_amount:,} đ")
                
        # CHỨC NĂNG 2: THÊM SẢN PHẨM MỚI HOẶC TĂNG SỐ LƯỢNG
        case "2":
            product_id = input("Nhập mã sản phẩm: ").strip().upper()
            product_name = input("Nhập tên sản phẩm: ").strip()
            
            quantity_input = input("Nhập số lượng: ").strip()
            price_input = input("Nhập đơn giá: ").strip()
            
            if not quantity_input.isdigit() or not price_input.isdigit():
                print("Số lượng và đơn giá phải là số nguyên hợp lệ!")
            else:
                quantity = int(quantity_input)
                price = int(price_input)
                
                # BẪY 1: Nhập số lượng hoặc đơn giá âm
                if quantity <= 0 or price < 0:
                    print("Lỗi: Số lượng nhập phải > 0 và Đơn giá phải >= 0!")
                else:
                    found = False
                    for item in cart_items:
                        if item[0] == product_id:
                            item[2] += quantity
                            print(f"Sản phẩm {product_id} đã tồn tại. Đã cộng dồn thêm {quantity} vào giỏ hàng.")
                            found = True
                            break
                    
                    if not found:
                        new_item = [product_id, product_name, quantity, price]
                        cart_items.append(new_item)
                        print(f"Đã thêm mới sản phẩm {product_id} vào giỏ hàng thành công.")
                        
        # CHỨC NĂNG 3: CẬP NHẬT SỐ LƯỢNG SẢN PHẨM
        case "3":
            product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            new_qty_input = input("Nhập số lượng mới: ").strip()
            
            if not new_qty_input.isdigit():
                print("Số lượng phải là số nguyên hợp lệ!")
            else:
                new_quantity = int(new_qty_input)
                
                # BẪY 1: Kiểm tra số lượng mới phải > 0
                if new_quantity <= 0:
                    print("Lỗi: Số lượng cập nhật phải > 0!")
                else:
                    found = False
                    for item in cart_items:
                        if item[0] == product_id:
                            item[2] = new_quantity
                            print(f"Đã cập nhật số lượng mới cho sản phẩm {product_id} thành công.")
                            found = True
                            break
                    
                    # BẪY 2: Mã sản phẩm không tồn tại
                    if not found:
                        print("Mã sản phẩm không tồn tại trong giỏ hàng.")
                        
        # CHỨC NĂNG 4: XÓA SẢN PHẨM KHỎI GIỎ HÀNG
        case "4":
            product_id = input("Nhập mã sản phẩm muốn xóa: ").strip().upper()
            found = False
            
            for item in cart_items:
                if item[0] == product_id:
                    cart_items.remove(item)
                    print(f"Đã xóa hoàn toàn sản phẩm {product_id} khỏi giỏ hàng.")
                    found = True
                    break
                    
            # BẪY 2: Mã sản phẩm không tồn tại
            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
                
        # CHỨC NĂNG 5: THOÁT CHƯƠNG TRÌNH
        case "5":
            print("Đã thoát hệ thống quản lý giỏ hàng Shopee. Tạm biệt!")
            break
            
        # BẪY 3: Khớp với mọi trường hợp nhập sai khác (kể cả chữ cái hoặc số ngoài 1-5)
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!")