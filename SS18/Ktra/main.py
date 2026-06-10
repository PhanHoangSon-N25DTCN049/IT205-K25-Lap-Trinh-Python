inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]

def show_inventory(inventory_list):
    if not inventory_list:
        print("Kho hàng hiện đang trống!");
        return;
    
    print("-- DANH SÁCH HÀNG TỒN KHO --");
    header = f"{'ID':<5} | {'Tên hàng hóa':<15} | {'Số lượng tồn':<5}";
    print(header);
    print("-"*len(header));
    for item in inventory_list:
        print(f"{item["id"]:<5} | {item["name"]:<20} | {item["quantity"]:<5}");
    print("-"*len(header));
    
def check_input_str (msg_input):
    while True:
        user_input = input(f"{msg_input}").strip();
        if user_input:
            return user_input;
        print("Không được bỏ trống");
            
            
def check_input_int (msg):
    while True:
        try:
            user_input = int(input(f"{msg}").strip());
        except ValueError:
            print("Ký tự nhập vào phải là số nguyên và lớn hơn 0");
        else:
            if user_input <= 0:
                print("Ký tự nhập vào phải lớn hơn 0");
                continue;
            break;
            
            
    
def add_item(inventory_list: list):
    print("-- Nhập hàng hóa mới --")
    id = check_input_str("Nhập mã hàng hóa(ID): ");
    name = check_input_str("Nhập tên hàng hóa: ");
    quantity = check_input_int("Nhập số lượng tồn kho: ");
    
    new_product = {
        'id':id,
        'name':name,
        'quantity':quantity
    }
    inventory_list.append(new_product);
    print("Thêm hàng hóa vào kho thành công!");
    
def update_quantity(inventory_list):
    print("-- Cập nhập số lượng tồn kho --");
    key = check_input_str("Nhập mã hàng hóa cần sửa:");
    key_idx = -1
    for idx, item in enumerate(inventory_list):
        if item['id'].lower() == key.lower():
            key_idx = idx;
            break;
    if key_idx != -1:
        print(f"tìm thấy hàng hóa: {inventory_list[key_idx]["name"]} (Số lượng hiện tại: {inventory_list[key_idx]["quantity"]})");
        inventory_list[key_idx]["quantity"] = check_input_int("Nhập số lượng mới");
        print("Cập nhật số lượng thành công");
        return;
    print(f"Không tìm thấy hàng hóa có mã {key}")
        
def main():
    while True:
        print("====================================");
        print("          Quản lý kho hàng")
        print("=====================================");
        print("1. Xem danh sách tồn kho")
        print("2. Nhập thêm hàng hóa mới")
        print("3. Cập nhật số lượng tồn kho theo id")
        print("4. Thoát chương trình")
        print("=====================================");
        choice = input("Mời bạn chọn chức năng(1-4): ");
        match choice:
            case "1":
                show_inventory(inventory);
            case "2":
                add_item(inventory);
            case "3":
                update_quantity(inventory);
            case "4":
                print("Cám ơn bạn đã sử dụng phần mềm!\n[Chương trình kết thúc]");
                break;
            case _:
                print("Lỗi lựa chọn vui lòng chọn lại!");
if __name__ == "__main__":
    main();