# Khởi tạo hai biến toàn cục lưu trữ trạng thái tiền tệ
atm_vault_balance = 50000000
user_account_balance = 10000000

def display_balances():
    """
    Chức năng 1: Hiển thị số dư tài khoản của người dùng và số tiền mặt có trong ATM.
    Hàm chỉ đọc dữ liệu từ các biến toàn cục để hiển thị.
    """
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Chức năng 2: Xử lý nạp tiền vào tài khoản và cập nhật tiền mặt trong ATM.
    
    Args:
        amount (int): Số tiền người dùng muốn nạp.
        
    Returns:
        bool: True nếu giao dịch nạp tiền thành công.
    """
    global user_account_balance, atm_vault_balance
    
    user_account_balance += amount
    atm_vault_balance += amount
    return True


def check_withdrawal_rules(amount):
    """
    Kiểm tra các điều kiện (luật) hợp lệ trước khi thực hiện rút tiền.
    
    Args:
        amount (int): Số tiền khách hàng muốn rút.
        
    Returns:
        str: Mã trạng thái lỗi hoặc "OK" nếu thỏa mãn mọi điều kiện.
    """
    # Bẫy 2: Nhập số âm hoặc bằng 0
    if amount <= 0:
        return "INVALID_AMOUNT"
        
    # Bẫy 1: Số tiền không phải là bội số của 50,000
    if amount % 50000 != 0:
        return "NOT_MULTIPLE"
        
    # Biến cục bộ (local variable) tính toán phí
    fee = 1100
    total_deduction = amount + fee
    
    # Kiểm tra số dư người dùng
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
        
    # Kiểm tra lượng tiền mặt vật lý trong trụ ATM
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
        
    return "OK"


def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Chức năng 3 (Thực thi): Tiến hành trừ tiền từ tài khoản và tiền mặt trong ATM.
    
    Args:
        total_deduction (int): Tổng số tiền bị trừ khỏi tài khoản (gốc + phí).
        amount_to_dispense (int): Số tiền mặt máy ATM thực tế nhả ra cho khách.
    """
    global user_account_balance, atm_vault_balance
    
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    
    fee = total_deduction - amount_to_dispense
    
    print("Giao dịch đang xử lý...")
    print(f"Phí giao dịch: {fee:,} VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")


def main():
    """
    Hàm chính điều khiển giao diện dòng lệnh và luồng hoạt động của hệ thống.
    """
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")
        
        choice = input("Vui lòng chọn giao dịch (1-4): ")
        
        match choice:
            case '1':
                display_balances()
                
            case '2':
                print("--- NẠP TIỀN ---")
                try:
                    amount = int(input("Nhập số tiền muốn nạp: "))
                    # Bẫy 2: Xử lý số tiền âm hoặc bằng 0 ngay tại đầu vào
                    if amount <= 0:
                        print("Số tiền không hợp lệ")
                    else:
                        if deposit_money(amount):
                            print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND.")
                except ValueError:
                    print("Số tiền không hợp lệ")
                    
            case '3':
                print("--- RÚT TIỀN ---")
                try:
                    amount = int(input("Nhập số tiền cần rút: "))
                    status = check_withdrawal_rules(amount)
                    
                    # Điều hướng dựa trên giá trị return của hàm kiểm tra
                    if status == "INVALID_AMOUNT":
                        print("Số tiền không hợp lệ")
                    elif status == "NOT_MULTIPLE":
                        print("Số tiền rút phải là bội số của 50,000")
                    elif status == "INSUFFICIENT_FUNDS":
                        print("Giao dịch thất bại: Số dư tài khoản không đủ.")
                    elif status == "ATM_OUT_OF_CASH":
                        print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                    elif status == "OK":
                        fee = 1100
                        total_deduction = amount + fee
                        execute_withdrawal(total_deduction, amount)
                except ValueError:
                    print("Số tiền không hợp lệ")
                    
            case '4':
                print("Cảm ơn quý khách đã sử dụng dịch vụ!")
                break
                
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()