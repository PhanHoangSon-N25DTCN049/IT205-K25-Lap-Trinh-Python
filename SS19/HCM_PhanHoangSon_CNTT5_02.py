products = [
    {"id":"SP001",
     "name":"Chuot khong day",
     "price":34000,
     "quantity":22,
     "minimum_quantity":20,
     "total_price": 5555555,
     "status": "Cảnh báo cần nhập hàng"}
];

def display_product (products):
    if not products:
        print("Chưa có sản phẩm nào!");
        return;
    print("--- Danh sách sản phẩm ---");
    header = f"{"Mã SP":<6} | {"Tên sản phẩm":<20} | {'Đơn giá':<10} | {'Số lượng':<10} | {'tối thiểu':<10} | {'giá trị':<15} | {'Trạng thái':<7}";
    print(header)
    print("-"*len(header));
    
    for item in products:
        print(f"{item['id']:<6} | {item['name']:<20} | {item['price']:<10} | {item['quantity']:<10} | {item['minimum_quantity']:<10} | {item['total_price']:<15} | {item['status']:<7}");
    print("-"*len(header));
    
def check_input_str(msg : str):
    while True:
        user_input = input(msg).strip();
        if user_input:    
            return user_input;
        print("Không được bỏ trống!");
        
def check_input_int(msg:str):
    while True:    
        try:
            user_input = int(input(msg));
        except ValueError:
            print("Vui lòng nhập số nguyên!");
        else:
            if user_input < 0:
                print("Số nhập vào phải >= 0");
            return user_input;
    
def check_input_float(msg:str):
    while True:    
        try:
            user_input = float(input(msg));
        except ValueError:
            print("Vui lòng nhập số!");
        else:
            if user_input < 0:
                print("Số nhập vào phải >= 0");
            return user_input;
        
def check_duplication (products,key:str):
    for idx ,item in enumerate(products):
        if item["id"].lower() == key.lower():
            return idx;
    return -1;

#Phân loại trạng thái tự động
def update_status (quantity, min_quantity):
    if quantity == 0:
        return "Hết hàng";
    elif quantity < min_quantity:
        return "Cảnh báo cần nhập hàng";
    elif quantity <= min_quantity*3:
        return "An toàn";
    elif quantity > min_quantity*3:
        return "Quá tải (Thặng dư)";
    

def add_product(products):
    while True:    
        id = check_input_str("Nhập ID sản phẩm: ");
        if check_duplication(products, id) != -1:
            print("Mã sản phẩm đã tồn tại!");
            continue;
        break;
    name = check_input_str("Nhập tên sản phẩm: ");
    price = check_input_float("Nhập đơn giá: ");
    quantity = check_input_int("Nhập số lượng: ");
    minimum_quantity = check_input_int("Nhập định mức tối thiểu: ");
    status = update_status(quantity,minimum_quantity);
    
    new_product = {
        'id':id,
        'name':name,
        'price':price,
        'quantity':quantity,
        'minimum_quantity':minimum_quantity,
        'total_price': price*quantity,
        'status': status
    }
    products.append2
    (new_product);
    print("Thêm sản phẩm thành công");
    
def update_product(products):
    key = check_input_str("Nhập mã sản phẩm cần cập nhật");
    idx_key = check_duplication(products, key);
    if idx_key != -1:
        print(f"--- Cập nhật sản phẩm {products[idx_key]['name']} ---")
        price_new = check_input_float("Nhập đơn giá mới: ");
        quantity_new = check_input_int("Nhập số lượng tồn kho hiện tại: ");
        min_quantity_new = check_input_int("Nhập định mức tối thiểu mới: ");
        status = update_status(quantity_new,min_quantity_new);
        products[idx_key]['price'] = price_new
        products[idx_key]['quantity'] = quantity_new
        products[idx_key]['minimum_quantity'] = min_quantity_new
        products[idx_key]['status'] = status
        products[idx_key]['total_price'] = price_new*quantity_new
        print("Cập nhật thành công!");
    else:
        print(f"Không tìm thấy sản phẩm có mã: {key}");

def del_product(products):
    key = check_input_str("Nhập mã sản phẩm cần xóa");
    idx_key = check_duplication(products, key);
    if idx_key != -1:
        choice_del = check_input_str(f"Bạn có chắc chắn muốn xóa sản phẩm {products[idx_key]['name']} khỏi danh mục không (Y/N):")
        if choice_del == 'Y' or choice_del == "y":
            del products[idx_key];
        print("xóa thành công!");
    else:
        print(f"Không tìm thấy sản phẩm có mã: {key}");

def search_product(products):
    key = check_input_str("Nhập tên hoặc id sản phẩm cần tìm: ");
    idx_key = check_duplication(products, key);
    item = [item for item in products if key.lower() in item["name"].lower()];
    
    if idx_key != -1:
        print(f"{products[idx_key]['id']:<6} | {products[idx_key]['name']:<20} | {products[idx_key]['price']:<10} | {products[idx_key]['quantity']:<10} | {products[idx_key]['minimum_quantity']:<10} | {products[idx_key]['total_price']:<15} | {products[idx_key]['status']:<7}");
    elif item:
        display_product(item);
    else:
        print(f"Không tìm thấy sản phẩm có chứa {key}")


def status_statistics (products):
    if not products:
        print("Chưa có sản phẩm nào!");
        return;
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    for item in products:
        if item["status"] == "Hết hàng":
            count_1 += 1;
        elif item["status"] == "Cảnh báo cần nhập hàng":
            count_2 += 1;
        elif item["status"] == "An toàn":
            count_3 += 1;
        elif item["status"] == "Quá tải (Thặng dư)":
            count_4 += 1;
    print(f"Số lượng hết hàng: {count_1}")
    print(f"Số lượng cần nhập thêm: {count_2}")
    print(f"Số lượng an toàn: {count_3}")
    print(f"Số lượng quá tải: {count_4}");

def main():
    global products;
    while True:
        print("""
--- Hệ thống quản lý sản phẩm ---
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. cập nhật sản phẩm theo id
4. xóa sản phẩm khỏi danh mục
5. tìm kiếm sản phẩm theo id hoặc tên
6. Thống kê trạng thái kho hàng
7. Thoát chương trình 
===================================
              """)
        choice = input("Nhập lựa chọn của bạn(1->8): ");
        match choice:
            case "7":
                print("Kết thúc chương trình! cám ơn bạn vì đã sử dụng");
                break;
            case "1":
                display_product(products);
            case "2":
                add_product(products);
            case "3":
                update_product(products);
            case "4":
                del_product(products);
            case "5":
                search_product(products);
            case "6":
                status_statistics(products);
            case _:
                print("Lỗi lựa chọn vui lòng chọn lại!");
    
if __name__ == "__main__":
    main();