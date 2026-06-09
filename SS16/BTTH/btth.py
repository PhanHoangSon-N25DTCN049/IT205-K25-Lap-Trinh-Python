
# 1. Hàm phụ trợ: find_blood_bag(inventory, bag_id)
# - Input: Danh sách túi máu (List) và Mã túi máu cần tìm (String).
# - Thuật toán: Chuẩn hóa mã nhập vào (strip, upper). Duyệt qua danh sách, sử dụng
#   .startswith(bag_id + "-") để tìm chuỗi chứa túi máu, tránh tìm nhầm mã (VD: BL001 và BL0010).
# - Output: Trả về chỉ mục (index) nguyên nếu tìm thấy, ngược lại trả về -1.
#
# 2. Phân tích Chức năng 1 (Xem danh sách & Cộng dồn thể tích):
# - Duyệt mảng, dùng .split("-") để tách chuỗi thành List con.
# - Lấy phần tử ở index 3 (thể tích), ép kiểu sang số nguyên (int) và cộng dồn vào biến tổng.
# - Sử dụng f-string với cú pháp căn lề (VD: {parts[1]:<16}) để tạo bảng đẹp trên terminal.
#
# 3. Phân tích Chức năng 2 (Thêm mới):
# - Cần áp dụng đúng các hàm xử lý chuỗi: .strip().upper() cho Mã túi và Nhóm máu, 
#   .strip().title() cho Tên người hiến.
# - Bẫy lỗi thể tích: Dùng .isdigit() để kiểm tra xem chuỗi có phải là số nguyên hay không, 
#   sau đó ép kiểu sang int để kiểm tra điều kiện > 0.
#
# 4. Phân tích Chức năng 3 (Sửa ngày hết hạn - Xử lý tính bất biến của String):
# - Trong Python, không thể sửa trực tiếp 1 phần của chuỗi ban đầu.
# - Giải pháp: Tìm vị trí túi máu -> Tách chuỗi bằng .split("-") -> Cập nhật ngày hết hạn 
#   ở phần tử cuối cùng (index 4) của list con -> Ghép list con lại thành chuỗi bằng "-".join() 
#   -> Gán đè chuỗi mới này vào đúng index trong danh sách (inventory) ban đầu.
#
# 5. Phân tích Chức năng 4 (Xuất / Hủy túi máu):
# - Dùng hàm tìm index. Nếu index != -1, dùng phương thức inventory.pop(index) để xóa phần tử.



blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]

def find_blood_bag(inventory, bag_id):
    """Hàm phụ trợ tìm vị trí túi máu theo mã"""
    clean_id = bag_id.strip().upper()
    for i, bag in enumerate(inventory):
        if bag.startswith(clean_id + "-"):
            return i
    return -1

def display_inventory(inventory):
    """Chức năng 1: Xem danh sách túi máu trong kho"""
    print("\n--- DANH SÁCH KHO MÁU ---")
    if not inventory:
        print("Kho máu hiện chưa có túi máu nào.")
        return
        
    print(f"{'Mã Túi':<6} | {'Người Hiến':<16} | {'Nhóm Máu':<8} | {'Thể Tích':<8} | {'Ngày Hết Hạn'}")
    print("-" * 62)
    
    total_volume = 0
    for bag in inventory:
        parts = bag.split("-")
        print(f"{parts[0]:<6} | {parts[1]:<16} | {parts[2]:<8} | {parts[3]:<4} ml | {parts[4]}")
        total_volume += int(parts[3])
        
    print("-" * 62)
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")

def add_blood_bag(inventory):
    """Chức năng 2: Nhập túi máu mới"""
    print("\n--- NHẬP TÚI MÁU MỚI ---")
    
    # 1. Nhập mã túi máu
    bag_id = input("Nhập mã túi máu mới: ").strip()
    if not bag_id:
        print("\nLỗi: Mã túi máu không được để trống!")
        return
    bag_id = bag_id.upper()
    
    if find_blood_bag(inventory, bag_id) != -1:
        print(f"\nLỗi: Mã túi máu {bag_id} đã tồn tại! Vui lòng nhập mã khác.")
        return
        
    # 2. Nhập tên người hiến
    donor_name = input("Nhập tên người hiến: ").strip()
    if not donor_name:
        print("\nLỗi: Tên người hiến không được để trống!")
        return
    donor_name = donor_name.title()
    
    # 3. Nhập nhóm máu
    blood_type = input("Nhập nhóm máu: ").strip().upper()
    
    # 4. Nhập thể tích (bẫy lỗi không phải số dương)
    volume = input("Nhập thể tích (ml): ").strip()
    if not volume.isdigit() or int(volume) <= 0:
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return
        
    # 5. Nhập ngày hết hạn
    expiry_date = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()
    
    # Ghép thông tin và thêm vào kho
    new_bag = "-".join([bag_id, donor_name, blood_type, volume, expiry_date])
    inventory.append(new_bag)
    
    print(f"\nThành công: Đã nhập túi máu {bag_id} vào kho!")
    print("\nSau khi chuẩn hóa, dữ liệu được lưu vào list là:")
    print(new_bag)

def update_expiry(inventory):
    """Chức năng 3: Gia hạn / Sửa ngày hết hạn"""
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")
    
    bag_id = input("Nhập mã túi máu cần cập nhật: ").strip()
    if not bag_id:
        print("\nLỗi: Mã túi máu không được để trống!")
        return
    bag_id = bag_id.upper()
    
    idx = find_blood_bag(inventory, bag_id)
    if idx == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {bag_id} trong kho!")
        return
        
    new_expiry = input("Nhập ngày hết hạn mới: ").strip()
    
    # Xử lý cắt - sửa - ghép
    parts = inventory[idx].split("-")
    parts[4] = new_expiry
    inventory[idx] = "-".join(parts)
    
    print(f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {bag_id}!")

def remove_blood_bag(inventory):
    """Chức năng 4: Xuất / Hủy túi máu"""
    print("\n--- XUẤT / HỦY TÚI MÁU ---")
    
    bag_id = input("Nhập mã túi máu cần xuất/hủy: ").strip()
    if not bag_id:
        print("\nLỗi: Mã túi máu không được để trống!")
        return
    bag_id = bag_id.upper()
    
    idx = find_blood_bag(inventory, bag_id)
    if idx == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {bag_id} trong kho!")
        return
        
    inventory.pop(idx)
    print(f"\nThành công: Đã xuất túi máu {bag_id} khỏi kho!")

def main():
    """Hàm main: Hiển thị Menu và điều hướng luồng chương trình"""
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")
        
        choice_input = input("Chọn chức năng (1-5): ").strip()
        
        try:
            choice = int(choice_input)
        except ValueError:
            print("\nLựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
            continue
            
        match choice:
            case 1:
                display_inventory(blood_inventory)
            case 2:
                add_blood_bag(blood_inventory)
            case 3:
                update_expiry(blood_inventory)
            case 4:
                remove_blood_bag(blood_inventory)
            case 5:
                print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
                break
            case _:
                print("\nLựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")

if __name__ == "__main__":
    main()