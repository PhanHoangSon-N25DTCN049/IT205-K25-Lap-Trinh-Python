
# * Phân tích Input/Output:
#   - Input:
#     + Lựa chọn từ menu (chạy qua Match Case).
#     + Thông tin nhập thêm khi giao dịch: Mã SP, số lượng mua, số lượng đổi trả, phần trăm giảm giá.
#   - Output:
#     + Danh sách sản phẩm kèm cột trạng thái chuẩn (Hết hàng/Sắp hết hàng/Còn hàng).
#     + In ra tổng tiền khách trả (đã trừ % giảm giá) hoặc số tiền hoàn lại khi đổi trả.
#
# * Đề xuất giải pháp & Xử lý Edge Cases (Bẫy dữ liệu):
#   - Bẫy 1: Mã SP nhập vào luôn dùng `.strip().upper()` để làm sạch khoảng trắng và chữ thường.
#   - Bẫy 2 & Bẫy 4: Khi bán hoặc đổi trả, duyệt tìm mã SP trong danh sách. Nếu không thấy thì thông báo tương ứng "Không tìm thấy sản phẩm cần bán" hoặc "Không tìm thấy sản phẩm cần đổi trả".
#   - Bẫy 3 & Bẫy 5: Check số lượng nhập vào bằng `.isdigit()`. Kiểm tra điều kiện logic: bán không được vượt quá tồn kho (`quantity`), đổi trả không được vượt quá số lượng đã bán (`sold`).
#   - Bẫy 6: Kiểm tra phần trăm giảm giá nhập vào bằng `.isdigit()`, chuyển đổi thành số nguyên và ép khoảng giá trị nằm trong đoạn từ 0 đến 70.
#   - Bẫy 7: Sử dụng `case _` trong cấu trúc match case để bắt các lựa chọn menu sai.


# Khởi tạo danh sách sản phẩm ban đầu hệ thống cấp sẵn
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả sản phẩm")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-6): ").strip()
    
    match choice:
        
        # CHỨC NĂNG 1: HIỂN THỊ DANH SÁCH SẢN PHẨM
        case "1":
            if not product_list:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("Danh sách sản phẩm hiện tại:")
                for index, prod in enumerate(product_list, start=1):
                    # Tính trạng thái tồn kho theo quy định
                    ton_kho = prod["quantity"]
                    if ton_kho == 0:
                        status = "Hết hàng"
                    elif ton_kho <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                        
                    print(f"{index}. Mã SP: {prod['product_id']} | Tên: {prod['product_name']} | Giá: {prod['price']} | Tồn kho: {ton_kho} | Đã bán: {prod['sold']} | Đổi trả: {prod['returned']} | Giảm giá: {prod['discount']}% | Trạng thái: {status}")

        # CHỨC NĂNG 2: BÁN SẢN PHẨM CHO KHÁCH HÀNG
        case "2":
            raw_id = input("Nhập mã sản phẩm khách muốn mua: ")
            product_id = raw_id.strip().upper()  # Bẫy 1
            
            found_product = None
            for prod in product_list:
                if prod["product_id"] == product_id:
                    found_product = prod
                    break
                    
            if found_product is None:
                print("Không tìm thấy sản phẩm cần bán")  # Bẫy 2
                continue
                
            raw_quantity = input("Nhập số lượng khách mua: ").strip()
            if not raw_quantity.isdigit() or int(raw_quantity) <= 0:
                print("Số lượng mua không hợp lệ")
                continue
                
            buy_quantity = int(raw_quantity)
            
            if buy_quantity > found_product["quantity"]:
                print("Số lượng trong kho không đủ để bán")  # Bẫy 3
                continue
                
            # Tính toán tiền sau khi áp dụng giảm giá
            discount_price = found_product["price"] * (100 - found_product["discount"]) / 100
            total_pay = discount_price * buy_quantity
            
            # Cập nhật số liệu hệ thống
            found_product["quantity"] -= buy_quantity
            found_product["sold"] += buy_quantity
            
            print(f"Bán hàng thành công! Tổng tiền khách cần thanh toán: {int(total_pay)}")

        # CHỨC NĂNG 3: XỬ LÝ ĐỔI TRẢ SẢN PHẨM
        case "3":
            raw_id = input("Nhập mã sản phẩm khách muốn đổi/trả: ")
            product_id = raw_id.strip().upper()  # Bẫy 1
            
            found_product = None
            for prod in product_list:
                if prod["product_id"] == product_id:
                    found_product = prod
                    break
                    
            if found_product is None:
                print("Không tìm thấy sản phẩm cần đổi trả")  # Bẫy 4
                continue
                
            raw_quantity = input("Nhập số lượng đổi/trả: ").strip()
            if not raw_quantity.isdigit() or int(raw_quantity) <= 0:
                print("Số lượng đổi/trả không hợp lệ")
                continue
                
            return_quantity = int(raw_quantity)
            
            if return_quantity > found_product["sold"]:
                print("Số lượng đổi/trả không được vượt quá số lượng đã bán")  # Bẫy 5
                continue
                
            # Tính toán tiền hoàn lại theo giá đã giảm hiện tại
            discount_price = found_product["price"] * (100 - found_product["discount"]) / 100
            total_refund = discount_price * return_quantity
            
            # Cập nhật số liệu hệ thống
            found_product["sold"] -= return_quantity
            found_product["quantity"] += return_quantity
            found_product["returned"] += return_quantity
            
            print(f"Xử lý đổi trả thành công! Số tiền hoàn lại cho khách: {int(total_refund)}")

        # CHỨC NĂNG 4: ÁP DỤNG GIẢM GIÁ CHO SẢN PHẨM
        case "4":
            raw_id = input("Nhập mã sản phẩm cần áp dụng giảm giá: ")
            product_id = raw_id.strip().upper()  # Bẫy 1
            
            found_product = None
            for prod in product_list:
                if prod["product_id"] == product_id:
                    found_product = prod
                    break
                    
            if found_product is None:
                print("Không tìm thấy mã sản phẩm yêu cầu!")
                continue
                
            raw_discount = input("Nhập phần trăm giảm giá (0-70): ").strip()
            # Bẫy 6: Kiểm tra tính hợp lệ của phần trăm giảm giá
            if not raw_discount.isdigit():
                print("Phần trăm giảm giá không hợp lệ")
                continue
                
            discount_val = int(raw_discount)
            if discount_val < 0 or discount_val > 70:
                print("Phần trăm giảm giá không hợp lệ")
                continue
                
            # Cập nhật mức giảm giá mới
            found_product["discount"] = discount_val
            print(f"Đã cập nhật mức giảm giá của sản phẩm {product_id} thành {discount_val}%.")

        # CHỨC NĂNG 5: NHẬP THÊM HÀNG VÀO KHO CỬA HÀNG
        case "5":
            raw_id = input("Nhập mã sản phẩm cần nhập thêm: ")
            product_id = raw_id.strip().upper()  # Bẫy 1
            
            found_product = None
            for prod in product_list:
                if prod["product_id"] == product_id:
                    found_product = prod
                    break
                    
            if found_product is None:
                print("Không tìm thấy mã sản phẩm yêu cầu!")
                continue
                
            raw_quantity = input("Nhập số lượng nhập thêm: ").strip()
            if not raw_quantity.isdigit() or int(raw_quantity) <= 0:
                print("Số lượng nhập kho phải là số nguyên dương!")
                continue
                
            import_quantity = int(raw_quantity)
            found_product["quantity"] += import_quantity
            print(f"Đã nhập thêm {import_quantity} sản phẩm {product_id} vào kho thành công.")

        # CHỨC NĂNG 6: THOÁT CHƯƠNG TRÌNH
        case "6":
            print("Thoát chương trình.")
            break
            
        # BẪY 7: NHẬP SAI LỰA CHỌN MENU
        case _:
            print('"Lựa chọn không hợp lệ", vui lòng nhập lại!')