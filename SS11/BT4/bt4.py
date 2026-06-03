
# * Phân tích Input/Output:
#   - Input:
#     + Lựa chọn tính năng từ menu (match case xử lý).
#     + Nhập mã sản phẩm, số lượng khi mua hoặc nhập kho.
#   - Output:
#     + Danh sách sản phẩm kèm trạng thái tồn kho (Hết hàng/Sắp hết hàng/Còn hàng).
#     + Hóa đơn thanh toán, số tiền khách trả, hoặc báo cáo doanh thu cuối ca.
#
# * Đề xuất giải pháp & Xử lý Edge Cases (Bẫy dữ liệu):
#   - Bẫy 1: Mã SP nhập vào luôn dùng `.strip().upper()` để xóa khoảng trắng và viết hoa.
#   - Bẫy 2: Khi tìm mã SP để Bán/Nhập kho, nếu duyệt hết list dict mà không thấy thì báo "Không tìm thấy sản phẩm cần bán/Nhập kho".
#   - Bẫy 3: Dùng `.isdigit()` check số lượng mua/nhập kho. Nếu không phải số nguyên hoặc số <= 0 thì báo "Số lượng mua/Nhập kho không hợp lệ".
#   - Bẫy 4: Khi bán, so sánh số lượng mua với số lượng tồn kho (`quantity`). Nếu mua > tồn thì báo "Số lượng trong kho không đủ để bán".
#   - Bẫy 5: Nhãn `case _` của match case sẽ bắt toàn bộ các lựa chọn nhập sai ngoài phạm vi 1-5.


# Khởi tạo danh sách sản phẩm ban đầu theo đề bài
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    match choice:
        
        # CHỨC NĂNG 1: HIỂN THỊ DANH SÁCH & CẢNH BÁO TỒN KHO
        case "1":
            if not product_list:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("Danh sách sản phẩm hiện tại:")
                for index, prod in enumerate(product_list, start=1):
                    # Phân loại trạng thái tồn kho theo quy định
                    ton_kho = prod["quantity"]
                    if ton_kho == 0:
                        status = "Hết hàng"
                    elif ton_kho <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                        
                    print(f"{index}. Mã SP: {prod['product_id']} | Tên: {prod['product_name']} | Giá: {prod['price']} | Tồn kho: {ton_kho} | Đã bán: {prod['sold']} | Trạng thái: {status}")

        # CHỨC NĂNG 2: BÁN SẢN PHẨM CHO KHÁCH HÀNG
        case "2":
            raw_id = input("Nhập mã sản phẩm khách muốn mua: ")
            product_id = raw_id.strip().upper()  # Bẫy 1
            
            # Kiểm tra sản phẩm tồn tại
            found_product = None
            for prod in product_list:
                if prod["product_id"] == product_id:
                    found_product = prod
                    break
            
            if found_product is None:
                print("Không tìm thấy sản phẩm cần bán/Nhập kho")  # Bẫy 2
                continue
                
            raw_quantity = input("Nhập số lượng khách mua: ").strip()
            # Bẫy 3: Check số nguyên dương
            if not raw_quantity.isdigit() or int(raw_quantity) <= 0:
                print("Số lượng mua/Nhập kho không hợp lệ")
                continue
                
            buy_quantity = int(raw_quantity)
            
            # Bẫy 4: Kiểm tra xem kho có đủ hàng không
            if buy_quantity > found_product["quantity"]:
                print("Số lượng trong kho không đủ để bán")
                continue
                
            # Xử lý trừ kho và tăng số lượng đã bán
            found_product["quantity"] -= buy_quantity
            found_product["sold"] += buy_quantity
            total_pay = buy_quantity * found_product["price"]
            print(f"Bán hàng thành công! Số tiền khách cần thanh toán: {total_pay}")

        # CHỨC NĂNG 3: NHẬP THÊM HÀNG VÀO KHO
        case "3":
            raw_id = input("Nhập mã sản phẩm cần nhập thêm: ")
            product_id = raw_id.strip().upper()  # Bẫy 1
            
            found_product = None
            for prod in product_list:
                if prod["product_id"] == product_id:
                    found_product = prod
                    break
                    
            if found_product is None:
                print("Không tìm thấy sản phẩm cần bán/Nhập kho")  # Bẫy 2
                continue
                
            raw_quantity = input("Nhập số lượng nhập thêm: ").strip()
            # Bẫy 3: Check số nguyên dương
            if not raw_quantity.isdigit() or int(raw_quantity) <= 0:
                print("Số lượng mua/Nhập kho không hợp lệ")
                continue
                
            import_quantity = int(raw_quantity)
            
            # Cộng thêm vào kho
            found_product["quantity"] += import_quantity
            print(f"Đã nhập thêm {import_quantity} sản phẩm {product_id} vào kho thành công.")

        # CHỨC NĂNG 4: XEM BÁO CÁO DOANH THU
        case "4":
            total_revenue = 0
            has_sales = False
            best_seller_name = ""
            max_sold = -1
            
            # Kiểm tra xem tổng thể đã có món nào bán được chưa
            for prod in product_list:
                if prod["sold"] > 0:
                    has_sales = True
                    break
            
            if not has_sales:
                print("Chưa có doanh thu phát sinh.")
            else:
                print("===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
                for index, prod in enumerate(product_list, start=1):
                    revenue_prod = prod["price"] * prod["sold"]
                    total_revenue += revenue_prod
                    print(f"{index}. {prod['product_name']} | Đã bán: {prod['sold']} | Doanh thu: {revenue_prod}")
                    
                    # Tìm sản phẩm bán chạy nhất dựa trên số lượng sold
                    if prod["sold"] > max_sold:
                        max_sold = prod["sold"]
                        best_seller_name = prod["product_name"]
                        
                print(f"\nTổng doanh thu: {total_revenue}")
                print(f"Sản phẩm bán chạy nhất: {best_seller_name}")

        # CHỨC NĂNG 5: THOÁT CHƯƠNG TRÌNH
        case "5":
            print("Thoát chương trình.")
            break
            
        # BẪY 5: NHẬP SAI MENU
        case _:
            print('"Lựa chọn không hợp lệ", vui lòng nhập lại!')