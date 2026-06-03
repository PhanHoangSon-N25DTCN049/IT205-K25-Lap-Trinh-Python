
# * Phân tích Input/Output:
#   - Input: 
#     + Lựa chọn menu từ bàn phím (Sử dụng Match Case để phân tách luồng xử lý).
#     + Thông tin sản phẩm nhập từ bàn phím: product_id (chuỗi), product_name (chuỗi), 
#       price (số nguyên), quantity (số nguyên).
#   - Output:
#     + Danh sách sản phẩm được định dạng theo mẫu yêu cầu.
#     + Các thông báo lỗi tương ứng với từng Edge Case (Bẫy dữ liệu).
#
# * Đề xuất giải pháp & Xử lý Edge Cases:
#   - Dùng vòng lặp `while True` để duy trì menu chạy liên tục.
#   - Chuẩn hóa mã SP bằng `.strip().upper()` để xử lý khoảng trắng và chữ thường (Bẫy 1).
#   - Kiểm tra trùng mã bằng cách duyệt qua list dict, nếu trùng thì báo lỗi (Bẫy 2).
#   - Dùng `isnumeric()` hoặc `isdigit()` kết hợp ép kiểu để bắt lỗi nhập chữ, số âm hoặc bằng 0 (Bẫy 4).
#   - Dùng cấu trúc `match ... case` cấu hình từ trường hợp 1 đến 5. Nhãn mặc định `case _` sẽ xử lý Bẫy 5.


# Danh sách dữ liệu ban đầu hệ thống cấp sẵn
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    # Hiển thị menu hệ thống
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    # Sử dụng cấu trúc Match Case theo đúng yêu cầu mặc định
    match choice:
        
        # CHỨC NĂNG 1: HIỂN THỊ DANH SÁCH
        case "1":
            if not product_list:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("Danh sách sản phẩm hiện tại:")
                for index, prod in enumerate(product_list, start=1):
                    print(f"{index}. Mã SP: {prod['product_id']} | Tên: {prod['product_name']} | Giá: {prod['price']} | Số lượng: {prod['quantity']}")
                    
        # CHỨC NĂNG 2: THÊM SẢN PHẨM MỚI
        case "2":
            raw_id = input("Nhập mã sản phẩm: ")
            # Bẫy 1: Chuẩn hóa khoảng trắng và chữ hoa/thường
            product_id = raw_id.strip().upper()
            
            # Bẫy 2: Kiểm tra trùng mã sản phẩm
            is_duplicate = False
            for prod in product_list:
                if prod["product_id"] == product_id:
                    is_duplicate = True
                    break
            
            if is_duplicate:
                print("Mã sản phẩm bị trùng")
                continue
                
            product_name = input("Nhập tên sản phẩm: ").strip()
            raw_price = input("Nhập giá sản phẩm: ").strip()
            raw_quantity = input("Nhập số lượng sản phẩm: ").strip()
            
            # Bẫy 4: Kiểm tra giá và số lượng phải là số nguyên dương
            if not (raw_price.isdigit() and raw_quantity.isdigit()):
                print("Giá/Số lượng không hợp lệ")
                continue
                
            price = int(raw_price)
            quantity = int(raw_quantity)
            
            if price <= 0 or quantity <= 0:
                print("Giá/Số lượng không hợp lệ")
                continue
                
            # Đạt điều kiện dữ liệu sạch, tiến hành lưu trữ
            new_product = {
                "product_id": product_id,
                "product_name": product_name,
                "price": price,
                "quantity": quantity
            }
            product_list.append(new_product)
            print("Thêm sản phẩm thành công")
            
        # CHỨC NĂNG 3: CẬP NHẬT THÔNG TIN
        case "3":
            raw_id = input("Nhập mã sản phẩm cần cập nhật: ")
            product_id = raw_id.strip().upper()
            
            # Tìm kiếm sản phẩm trong kho
            found_product = None
            for prod in product_list:
                if prod["product_id"] == product_id:
                    found_product = prod
                    break
                    
            # Bẫy 3: Xử lý khi không tìm thấy mã để sửa
            if found_product is None:
                print("Không tìm thấy mã sản phẩm cần cập nhật!")
                continue
                
            new_name = input("Nhập tên sản phẩm mới: ").strip()
            raw_price = input("Nhập giá sản phẩm mới: ").strip()
            raw_quantity = input("Nhập số lượng tồn kho mới: ").strip()
            
            # Check tính hợp lệ của dữ liệu số mới nhập vào
            if not (raw_price.isdigit() and raw_quantity.isdigit()):
                print("Giá/Số lượng không hợp lệ")
                continue
                
            price = int(raw_price)
            quantity = int(raw_quantity)
            
            if price <= 0 or quantity <= 0:
                print("Giá/Số lượng không hợp lệ")
                continue
                
            # Cập nhật trực tiếp vào dict
            found_product["product_name"] = new_name
            found_product["price"] = price
            found_product["quantity"] = quantity
            print("Cập nhật thông tin sản phẩm thành công")
            
        # CHỨC NĂNG 4: XÓA SẢN PHẨM
        case "4":
            raw_id = input("Nhập mã sản phẩm cần xóa: ")
            product_id = raw_id.strip().upper()
            
            found_product = None
            for prod in product_list:
                if prod["product_id"] == product_id:
                    found_product = prod
                    break
                    
            # Bẫy 3: Xử lý khi không tìm thấy mã để xóa
            if found_product is None:
                print("Không tìm thấy mã sản phẩm cần xoá!")
                continue
                
            product_list.remove(found_product)
            print(f"Đã xóa sản phẩm {product_id} thành công.")
            
        # CHỨC NĂNG 5: THOÁT
        case "5":
            print("Thoát chương trình.")
            break
            
        # BẪY 5: NHẬP SAI LỰA CHỌN MENU (Xử lý bằng default case '_')
        case _:
            print('"Lựa chọn không hợp lệ", vui lòng nhập lại!')