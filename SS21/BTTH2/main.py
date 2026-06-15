"""
HỆ THỐNG ĐẶT MÓN & THANH TOÁN HIGHLANDS COFFEE (POS)
"""

import sys
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Thực đơn đồ uống mặc định
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}



def view_menu():
    """Chức năng 1: Xem thực đơn"""
    print("--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, info in DRINK_MENU.items():
        print(f"[{code}] - {info['name']} - {info['price']:,} VNĐ")


def add_to_order(drink_code: str, quantity_str: str, order_list: list) -> bool:
    """Chức năng 2: Thêm món vào giỏ hàng"""
    # Chuẩn hóa chuỗi dữ liệu nhập vào
    clean_code = drink_code.strip().upper()

    # Bẫy 1: Kiểm tra lỗi nhập chữ thay vì nhập số (ValueError)
    try:
        quantity = int(quantity_str)
    except ValueError:
        print("Vui lòng nhập số lượng là một số nguyên!")
        logging.error("ValueError - Invalid quantity input")
        return False

    # Bẫy 2: Kiểm tra xem mã món có tồn tại không
    if clean_code not in DRINK_MENU:
        print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
        logging.warning(f"ItemNotFoundError - Code: {clean_code}")
        return False

    # Bẫy 3: Kiểm tra số lượng phải lớn hơn 0
    if quantity <= 0:
        print("Số lượng phải lớn hơn 0!")
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        return False

    # Nếu hợp lệ thì thêm vào danh sách giỏ hàng
    drink_name = DRINK_MENU[clean_code]["name"]
    order_list.append({
        "code": clean_code,
        "name": drink_name,
        "price": DRINK_MENU[clean_code]["price"],
        "quantity": quantity
    })
    
    logging.info(f"Added {quantity} of {clean_code} to order")
    print(f"Đã thêm {quantity} x {drink_name} vào giỏ hàng.")
    return True


def calculate_total(order_list: list) -> int:
    """Hàm phụ trợ tính tổng số tiền hiện có trong giỏ hàng"""
    total = 0
    for item in order_list:
        total += item["price"] * item["quantity"]
    return total


def view_order(order_list: list):
    """Chức năng 3: Xem giỏ hàng và hiển thị tổng tiền"""
    if not order_list:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("--- GIỎ HÀNG HIỆN TẠI ---")
    print("Mã SP | Tên đồ uống          | Đơn giá  | Số lượng | Thành tiền")
    print("-" * 64)
    
    for item in order_list:
        subtotal = item["price"] * item["quantity"]
        print(f"{item['code']:<5} | {item['name']:<19} | {item['price']:,:<8} | {item['quantity']:<8} | {subtotal:,} VNĐ")
        
    print("-" * 64)
    total_amount = calculate_total(order_list)
    print(f"Tổng tiền cần thanh toán: {total_amount:,} VNĐ")


def checkout(order_list: list) -> list:
    """Chức năng 4: Xác nhận thanh toán đơn hàng"""
    if not order_list:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return order_list

    total_amount = calculate_total(order_list)
    print("--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total_amount:,} VNĐ")
    
    confirm = input(f"Xác nhận thanh toán {total_amount:,} VNĐ? (y/n): ").strip().lower()
    
    if confirm == 'y':
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        print("Giỏ hàng đã được làm trống.")
        return []
    elif confirm == 'n':
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
        return order_list
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")
        return order_list


def test_calculate_total():
    """Hàm kiểm tra xem logic tính tiền của hệ thống có chuẩn không"""
    print("\n[TEST] Đang kiểm tra hàm tính tổng tiền (calculate_total)...")
    # Giả lập một giỏ hàng mẫu: 2 Phin Sữa Đá (70k) + 1 Freeze (55k) = 125k
    mock_order = [
        {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
        {"code": "F1", "name": "Freeze Trà Xanh", "price": 55000, "quantity": 1}
    ]
    
    ket_qua = calculate_total(mock_order)
    
    if ket_qua == 125000:
        print("=> test_calculate_total: PASSED")
        return True
    else:
        print(f"=> test_calculate_total: FAILED (Tính sai tổng tiền: {ket_qua} != 125000)")
        return False


def test_invalid_quantity():
    """Hàm kiểm tra xem hệ thống có chặn được số lượng âm hay không"""
    print("\n[TEST] Đang kiểm tra bộ lọc số lượng không hợp lệ (add_to_order)...")
    mock_order = []
    
    # Chạy thử hàm với số lượng là "-5", hàm phải trả về False (không cho thêm)
    ket_qua = add_to_order("P1", "-5", mock_order)
    
    if ket_qua is False and len(mock_order) == 0:
        print("=> test_invalid_quantity: PASSED")
        return True
    else:
        print("=> test_invalid_quantity: FAILED (Hệ thống không chặn được số lượng âm)")
        return False


def run_pos_menu():
    """Giao diện tương tác Menu chính của POS"""
    current_order = []

    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            view_menu()
        elif choice == "2":
            print("--- THÊM MÓN VÀO GIỎ ---")
            drink_code = input("Nhập mã đồ uống: ")
            quantity_str = input("Nhập số lượng: ")
            add_to_order(drink_code, quantity_str, current_order)
        elif choice == "3":
            view_order(current_order)
        elif choice == "4":
            current_order = checkout(current_order)
        elif choice == "5":
            logging.info("Cashier logged out. System shutdown.")
            print("Đã thoát ca làm việc. Hẹn gặp lại!")
            sys.exit(0)
        else:
            print("Chức năng không hợp lệ! Vui lòng chọn lại từ 1 đến 5.")


if __name__ == "__main__":
    print("=== KHỞI ĐỘNG HỆ THỐNG VÀ KIỂM TRA CHẤT LƯỢNG CODE ===")
    
    # Gọi các hàm test thủ công để chạy nghiệm thu trước
    test1 = test_calculate_total()
    test2 = test_invalid_quantity()
    
    print("\n=======================================================")
    if test1 and test2:
        print("TẤT CẢ CÁC BÀI TEST ĐÃ VƯỢT QUA! MỞ MENU HỆ THỐNG...")
        print("=======================================================")
        # Nếu tất cả hàm test trả về True thì mới chính thức mở Menu POS lên cho người dùng
        run_pos_menu()
    else:
        print("CẢNH BÁO: Code của bạn đang bị lỗi logic nghiệp vụ. Hệ thống dừng khởi động!")
        print("=======================================================")
        sys.exit(1)