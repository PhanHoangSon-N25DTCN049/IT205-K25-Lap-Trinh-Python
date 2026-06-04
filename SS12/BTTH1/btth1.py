def menu():
    print("==================================================");
    print("      HỆ THỐNG QUẢN LÝ GIỎ HÀNG - AMAZON CLI      ");
    print("==================================================");
    print("  1. Xem chi tiết giỏ hàng và Tổng tiền");
    print("  2. Thêm sản phẩm mới hoặc Tăng số lượng");
    print("  3. Cập nhật số lượng sản phẩm");
    print("  4. Xóa sản phẩm khỏi giỏ hàng");
    print("  5. Thoát chương trình");
    print("==================================================");

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
];

while True:
    menu();
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip();
    
    match choice:
        case "5":
            print("Đã thoát chương trình");
            break;
            
        case "1":
            if not cart_items:
                print("[Thông báo: Giỏ hàng hiện đang trống!]");
                continue;
                
            header = f"{'ID':<10} | {'Tên sản phẩm':<25} | {'Số lượng':<10} | {'Đơn giá':<15}";
            print(header);
            print("-" * len(header));
            
            total_count = 0;
            total_price = 0;
            
            for item in cart_items:
                print(f"{item['id']:<10} | {item['name']:<25} | {item['number']:<10} | {item['price']:<15}");
                total_count += item['number'];
                total_price += item['number'] * item['price'];
                
            print("-" * len(header));
            print(f"Tổng số lượng tất cả sản phẩm: {total_count}");
            print(f"Tổng tiền toàn bộ giỏ hàng: {total_price} VND");
            
        case "2":
            while True:
                cart_id = input("Nhập mã sản phẩm: ").strip();
                if not cart_id:
                    print("Mã sản phẩm không được bỏ trống!");
                else: 
                    break;
            
            while True:
                cart_name = input("Nhập tên sản phẩm: ").strip();
                if not cart_name:
                    print("Tên sản phẩm không được bỏ trống!");
                else: 
                    break;
            
            while True:
                cart_number = input("Nhập số lượng: ").strip();
                if not cart_number:
                    print("Số lượng không được bỏ trống!");
                elif not cart_number.lstrip('-').isdigit(): 
                    print("Dữ liệu nhập vào phải là số!");
                elif int(cart_number) <= 0:
                    print("Số lượng phải lớn hơn 0!");
                else: 
                    break;
            
            while True:
                cart_price = input("Nhập đơn giá: ").strip();
                if not cart_price:
                    print("Đơn giá không được bỏ trống!");
                elif not cart_price.lstrip('-').isdigit(): 
                    print("Dữ liệu nhập vào phải là số!");
                elif int(cart_price) < 0:
                    print("Đơn giá không được âm!");
                else: 
                    break;
            
            check_exist = False;
            for item in cart_items:
                if cart_id == item["id"]:
                    item["number"] += int(cart_number);
                    print(f"Mã sản phẩm đã tồn tại. Đã cộng dồn {cart_number} vào số lượng.");
                    check_exist = True;
                    break;
            
            if not check_exist:
                new_item = {
                    "id": cart_id,
                    "name": cart_name,
                    "number": int(cart_number),
                    "price": int(cart_price)
                };
                cart_items.append(new_item);
                print("Đã thêm sản phẩm mới vào giỏ hàng thành công.");
                
        case "3":
            while True:
                cart_id = input("Nhập mã sản phẩm cần cập nhật: ").strip();
                if cart_id: 
                    break;
                print("Mã sản phẩm không được bỏ trống!");
                
            temp_idx = -1;
            for idx, item in enumerate(cart_items):
                if cart_id == item["id"]:
                    temp_idx = idx;
                    break;
            
            if temp_idx == -1:
                print(f"[Lỗi: Không tìm thấy mã sản phẩm {cart_id} trong giỏ hàng!]");
                continue;
                
            while True:
                new_number = input(f"Nhập số lượng mới cho {cart_id}: ").strip();
                if not new_number:
                    print("Số lượng không được bỏ trống!");
                elif not new_number.lstrip('-').isdigit():
                    print("Dữ liệu nhập vào phải là số!");
                elif int(new_number) <= 0:
                    print("Số lượng phải lớn hơn 0!");
                else: 
                    break;
                    
            cart_items[temp_idx]["number"] = int(new_number);
            print(f"[Thành công]: Đã cập nhật số lượng của {cart_id} thành {new_number}.");

        case "4":
            while True:
                cart_id = input("Nhập mã sản phẩm cần xóa: ").strip();
                if cart_id: 
                    break;
                print("Mã sản phẩm không được bỏ trống!");
                
            temp_idx = -1;
            for idx, item in enumerate(cart_items):
                if cart_id == item["id"]:
                    temp_idx = idx;
                    break;
            
            if temp_idx == -1:
                print(f"[Lỗi: Không tìm thấy mã sản phẩm {cart_id} trong giỏ hàng!]");
                continue;
                
            print(f"[Thành công]: Đã xóa sản phẩm {cart_items[temp_idx]['name']} khỏi giỏ hàng.");
            del cart_items[temp_idx];
            
        case _:
            print("Lỗi lựa chọn! Vui lòng nhập lại số từ 1 đến 5.");