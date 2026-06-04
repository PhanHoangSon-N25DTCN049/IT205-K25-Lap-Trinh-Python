cart_items = [
    {
        "id": "P001", 
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon", 
        "number": 2, 
        "price": 150000
    }
]

while True:
    print("\n--- SHOPEE CART MANAGEMENT SYSTEM ---")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    match choice:
        case '1':
            if len(cart_items) == 0:
                print("Giỏ hàng hiện không có sản phẩm nào.")
            else:
                total_count = 0
                total_price = 0
                
                print(f"{'ID':<10} | {'Tên sản phẩm':<25} | {'Số lượng':<10} | {'Đơn giá':<15}")
                print("-" * 68)
                
                for item in cart_items:
                    print(f"{item['id']:<10} | {item['name']:<25} | {item['number']:<10} | {item['price']:<15}")
                    total_count += item['number']
                    total_price += item['number'] * item['price']
                    
                print("-" * 68)
                print(f"Tổng số lượng tất cả sản phẩm: {total_count}")
                print(f"Tổng tiền toàn bộ giỏ hàng: {total_price}")

        case '2':
            cart_id = input("Nhập mã sản phẩm: ").strip()
            if cart_id == '':
                print("Lỗi: Mã sản phẩm không được để trống.")
                continue
                
            cart_name = input("Nhập tên sản phẩm: ").strip()
            if cart_name == '':
                print("Lỗi: Tên sản phẩm không được để trống.")
                continue
            
            number_str = input("Nhập số lượng: ").strip()
            price_str = input("Nhập đơn giá: ").strip()
            
            # Kiểm tra xem chuỗi có phải là số nguyên (bao gồm cả số âm) hay không
            if not (number_str.lstrip('-').isdigit() and price_str.lstrip('-').isdigit()):
                print("Lỗi: Số lượng và đơn giá phải là số nguyên hợp lệ.")
                continue
            
            cart_number = int(number_str)
            cart_price = int(price_str)

            # Bẫy 1: Xử lý số lượng và đơn giá âm/bằng 0
            if cart_number <= 0 or cart_price < 0:
                print("Lỗi: Số lượng phải lớn hơn 0 và đơn giá không được âm.")
                continue

            for item in cart_items:
                if cart_id == item['id']:
                    item['number'] += cart_number
                    print(f"Mã sản phẩm đã tồn tại. Đã cộng dồn {cart_number} vào số lượng.")
                    break
            else:
                new_cart = {
                    "id": cart_id,
                    "name": cart_name,
                    "number": cart_number,
                    "price": cart_price
                }
                cart_items.append(new_cart)
                print("Đã thêm sản phẩm mới vào giỏ hàng.")

        case '3':
            cart_id = input("Nhập mã sản phẩm cần cập nhật: ").strip()
            number_str = input("Nhập số lượng mới: ").strip()
            
            if not number_str.lstrip('-').isdigit():
                print("Lỗi: Số lượng phải là số nguyên hợp lệ.")
                continue
                
            cart_number = int(number_str)
            
            if cart_number <= 0:
                print("Lỗi: Số lượng phải lớn hơn 0.")
                continue
                
            for item in cart_items:
                if item['id'] == cart_id:
                    item['number'] = cart_number
                    print("Đã cập nhật số lượng thành công.")
                    break
            else:
                # Bẫy 2: Cập nhật sản phẩm không tồn tại
                print("Lỗi: Mã sản phẩm không tồn tại trong giỏ hàng.")

        case '4':
            cart_id = input("Nhập mã sản phẩm muốn xóa: ").strip()
            
            for item in cart_items:
                if item['id'] == cart_id:
                    cart_items.remove(item)
                    print("Đã xóa hoàn toàn sản phẩm khỏi giỏ hàng.")
                    break
            else:
                # Bẫy 2: Xóa sản phẩm không tồn tại
                print("Lỗi: Mã sản phẩm không tồn tại trong giỏ hàng.")

        case '5':
            print("Đã thoát chương trình.")
            break
            
        case _:
            # Bẫy 3: Menu Validation
            print("Lựa chọn không hợp lệ. Vui lòng chỉ nhập số từ 1 đến 5.")