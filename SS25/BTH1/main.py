class BankAccount:
    # Class attributes
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number: str, account_name: str):
        self.__account_number = account_number
        self.__balance = 0
        # Sử dụng setter để chuẩn hóa tên ngay khi khởi tạo
        self.account_name = account_name

    # Đóng gói dữ liệu: Chỉ cho phép đọc số dư, không có setter
    @property
    def balance(self):
        return self.__balance

    # Getter cho tên chủ tài khoản
    @property
    def account_name(self):
        return self.__account_name

    # Setter cho tên chủ tài khoản kèm kiểm tra bẫy dữ liệu và chuẩn hóa
    @account_name.setter
    def account_name(self, new_name: str):
        self.__account_name = new_name.upper()

    # Getter cho số tài khoản (phục vụ hiển thị thông tin)
    @property
    def account_number(self):
        return self.__account_number

    # Static method kiểm tra số tài khoản độc lập
    @staticmethod
    def validate_account_number(account_number: str) -> bool:
        return account_number.isdigit() and len(account_number) == 10

    @staticmethod
    def validate_account_name(account_name: str) -> bool:
        return   True if not account_name else False;
    
    # Class method cập nhật thuộc tính chung của toàn bộ lớp
    @classmethod
    def update_transaction_fee(cls, new_fee: int):
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            print(f"Phí giao dịch hiện tại vẫn là {cls.transaction_fee:,} VND")
            return
        cls.transaction_fee = new_fee
        print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {new_fee:,} VND")

    # Phương thức nạp tiền
    def deposit(self, amount: int):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")
        print(f"Số dư mới: {self.balance:,} VND")

    # Phương thức rút tiền
    def withdraw(self, amount: int):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        
        total_deduction = amount + BankAccount.transaction_fee
        if self.__balance < total_deduction:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            print(f"Số dư mới: {self.balance:,} VND")
            return
        
        self.__balance -= total_deduction
        print(f"Rút tiền thành công: -{amount:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
        print(f"Số dư mới: {self.balance:,} VND")

    # Phương thức hiển thị thông tin tài khoản
    def display_info(self):
        print("--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


# Chương trình điều khiển Menu CLI chính
def main():
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Giao dịch Nạp / Rút tiền")
        print("4. Cập nhật Tên chủ tài khoản")
        print("5. Đổi phí giao dịch hệ thống")
        print("6. Thoát chương trình")
        print("==========================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                print("\n--- MỞ TÀI KHOẢN MỚI ---")
                while True:
                    acc_num = input("Nhập số tài khoản 10 chữ số: ").strip()
                    if BankAccount.validate_account_number(acc_num):
                        break
                    print("Số tài khoản không hợp lệ!")
                    print("Số tài khoản phải gồm đúng 10 chữ số.")
                
                while True:
                    acc_name = input("Nhập tên chủ tài khoản: ").strip();
                    if BankAccount.validate_account_name(acc_name):
                        print("Tên tài khoản không được để trống")
                        continue;
                    break;
                
                current_account = BankAccount(acc_num, acc_name)
                print("Mở tài khoản thành công!")
                print(f"Số tài khoản: {current_account.account_number}")
                print(f"Tên chủ tài khoản: {current_account.account_name}")

            case "2":
                if current_account is None:
                    print("\nHệ thống chưa có thông tin tài khoản")
                    print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                else:
                    print()
                    current_account.display_info()

            case "3":
                if current_account is None:
                    print("\nHệ thống chưa có thông tin tài khoản")
                    print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                else:
                    print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
                    print("1. Nạp tiền")
                    print("2. Rút tiền")
                    sub_choice = input("Chọn loại giao dịch (1-2): ").strip()
                    
                    try:
                        amount = int(input("Nhập số tiền giao dịch: ").strip())
                    except ValueError:
                        print("Số tiền nhập vào phải là số nguyên hợp lệ.")
                        continue

                    match sub_choice:
                        case "1":
                            current_account.deposit(amount)
                        case "2":
                            current_account.withdraw(amount)
                        case _:
                            print("Lựa chọn loại giao dịch không hợp lệ.")

            case "4":
                if current_account is None:
                    print("\nHệ thống chưa có thông tin tài khoản")
                    print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                else:
                    print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
                    while True:
                        new_name = input("Nhập tên mới: ")
                        if BankAccount.validate_account_name(new_name):
                            print("Tên tài khoản không được để trống");
                            continue;
                        break;
                    current_account.account_name = new_name
                    print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")

            case "5":
                print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
                print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")
                try:
                    new_fee = int(input("Nhập phí giao dịch mới: ").strip())
                    BankAccount.update_transaction_fee(new_fee)
                except ValueError:
                    print("Phí giao dịch phải là số nguyên hợp lệ.")

            case "6":
                print("\nCảm ơn bạn đã sử dụng Vietcombank Digibank!")
                break

            case _:
                print("\nChức năng không hợp lệ. Vui lòng chọn lại từ 1 đến 6.")

if __name__ == "__main__":
    main()