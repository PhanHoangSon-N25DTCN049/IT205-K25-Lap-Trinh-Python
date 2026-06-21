from abc import ABC, abstractmethod


class VNPayGateway:
    """Cổng thanh toán VNPay độc lập"""
    def execute_pay(self, account, amount):
        print(f"[Hệ thống VNPay]: Đang kết nối tới tài khoản {account.account_number}...")
        if account.withdraw(amount):
            print("Xác thực thanh toán bằng Duck Typing thành công!")
            print(f"Tài khoản đã thanh toán hóa đơn giá trị: {amount:,} VND.")
            print(f"Số dư mới: {account.balance:,} VND.")
            return True
        return False

class ViettelMoneyGateway:
    """Cổng thanh toán Viettel Money độc lập"""
    def execute_pay(self, account, amount):
        print(f"[Hệ thống Viettel Money]: Đang xử lý giao dịch cho tài khoản {account.account_number}...")
        if account.withdraw(amount):
            print("Xác thực thanh toán bằng Duck Typing thành công!")
            print(f"Tài khoản đã thanh toán hóa đơn giá trị: {amount:,} VND.")
            print(f"Số dư mới: {account.balance:,} VND.")
            return True
        return False



class DigitalPremiumMixin:
    """Mixin cung cấp dịch vụ hoàn tiền cao cấp, không kế thừa BaseAccount"""
    def cashback_reward(self, amount: float) -> float:
        # Hoàn tiền 1% cho các giao dịch lớn hơn 5,000,000 VND
        if amount > 5000000:
            return amount * 0.01
        return 0.0




class BaseAccount(ABC):
    """Lớp trừu tượng định nghĩa bộ khung chuẩn cho mọi tài khoản"""
    bank_name = "Vietcombank"

    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        self._account_number = account_number
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private Attribute đóng gói số dư

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_holder(self):
        return self._account_holder

    @account_holder.setter
    def account_holder(self, value: str):
        # Chuẩn hóa Tên (In hoa, xóa khoảng trắng thừa)
        self._account_holder = " ".join(value.strip().split()).upper()

    @property
    def balance(self) -> float:
        return self.__balance

    def _update_balance(self, amount: float):
        self.__balance = amount

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        pass

    @staticmethod
    def validate_account_number(account_number: str) -> bool:
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_bank_name(cls, new_name: str):
        cls.bank_name = new_name

    def __add__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance + other.balance

    def __lt__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance < other.balance


class SavingsAccount(BaseAccount):
    """Tài khoản tiết kiệm có sinh lãi và tính phí phạt rút trước hạn"""
    def __init__(self, account_number: str, account_holder: str, interest_rate: float, initial_balance: float = 0.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        if amount <= 0:
            print("Số tiền nạp phải lớn hơn 0.")
            return
        self._update_balance(self.balance + amount)

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
            return False
        
        penalty = amount * 0.02
        total_deduct = amount + penalty
        
        if self.balance >= total_deduct:
            self._update_balance(self.balance - total_deduct)
            print("Rút tiền thành công!")
            print(f"Số tiền rút: {amount:,} VND")
            print(f"Phí phạt rút trước hạn (2%): {penalty:,} VND")
            print(f"Số dư còn lại: {self.balance:,} VND")
            return True
        print("Giao dịch thất bại! Số dư tài khoản không đủ để thanh toán và chịu phí.")
        return False

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Số dư trước tính lãi: {self.balance:,} VND")
        print(f"Lãi suất năm: {self.interest_rate * 100}%")
        print(f"Tiền lãi nhận được: +{interest:,} VND")
        self._update_balance(self.balance + interest)
        print(f"Số dư mới sau khi cộng lãi: {self.balance:,} VND")


class CreditAccount(BaseAccount):
    """Tài khoản tín dụng chi tiêu thấu chi (cho phép số dư âm)"""
    def __init__(self, account_number: str, account_holder: str, credit_limit: float, initial_balance: float = 0.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.credit_limit = credit_limit

    def deposit(self, amount: float):
        if amount <= 0:
            print("Số tiền nạp phải lớn hơn 0.")
            return
        self._update_balance(self.balance + amount)

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
            return False
        
        # Bẫy 2 — Vượt quá hạn mức tín dụng âm
        if self.balance - amount < -self.credit_limit:
            print("Lỗi: Vượt quá hạn mức thấu chi cho phép!")
            return False
        
        self._update_balance(self.balance - amount)
        if self.balance < 0:
            print("Rút tiền thành công! (Sử dụng hạn mức thấu chi)")
        else:
            print("Rút tiền thành công!")
        print(f"Số tiền rút: {amount:,} VND")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        return True


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    """Tài khoản thế hệ mới, đa kế thừa tuân thủ đúng quy tắc MRO"""
    def __init__(self, account_number: str, account_holder: str, interest_rate: float, initial_balance: float = 0.0):
        super().__init__(account_number, account_holder, interest_rate, initial_balance)

    def deposit(self, amount: float):
        if amount <= 0:
            print("Số tiền nạp phải lớn hơn 0.")
            return
        
        cashback = self.cashback_reward(amount)
        total_credit = amount + cashback
        
        self._update_balance(self.balance + total_credit)
        print("Nạp tiền thành công!")
        if cashback > 0:
            print(f"[Ưu đãi Premium]: Bạn được hoàn tiền 1% ({cashback:,} VND) vào tài khoản!")
        print(f"Số dư mới: {self.balance:,} VND")



def process_payment(payment_gateway, account: BaseAccount, amount: float):
    """Hàm toàn cục chứng minh Duck Typing"""
    try:
        # Bẫy 4 — Sai lệch phương thức trong Duck Typing
        if not hasattr(payment_gateway, "execute_pay"):
            raise AttributeError("Cổng thanh toán không hợp lệ hoặc chưa được tích hợp")
        return payment_gateway.execute_pay(account, amount)
    except AttributeError as e:
        print(f"Lỗi hệ thống: {e}")
        return False




def main():
    accounts = []
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====")
        print("1. Mở tài khoản mới (Chọn loại tài khoản)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Giao dịch Nạp / Rút tiền & Tính điểm thưởng (Đa hình)")
        print("4. Tích lũy / Áp dụng lãi suất định kỳ")
        print("5. Kiểm tra tính năng gộp tài khoản & So sánh (Overloading)")
        print("6. Thanh toán hóa đơn qua Cổng trung gian (Duck Typing)")
        print("7. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-7): ").strip()

        match choice:
            case "1":
                print("\n--- CHỌN LOẠI TÀI KHOẢN ---")
                print("1. Savings Account (Tài khoản Tiết kiệm)")
                print("2. Credit Account (Tài khoản Tín dụng)")
                print("3. Hybrid Account (Tài khoản Đa năng)")
                type_choice = input("Chọn loại tài khoản (1-3): ").strip()
                
                if type_choice not in ["1", "2", "3"]:
                    print("Lựa chọn không hợp lệ.")
                    continue

                acc_num = input("Nhập số tài khoản 10 chữ số: ").strip()
                if not BaseAccount.validate_account_number(acc_num):
                    print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
                    continue

                name = input("Nhập tên chủ tài khoản: ")
                initial_deposit = 10000000.0 

                match type_choice:
                    case "1":
                        try:
                            rate = float(input("Nhập lãi suất năm (ví dụ 0.06): ").strip())
                        except ValueError:
                            print("Lãi suất phải là một số thực.")
                            continue
                        new_acc = SavingsAccount(acc_num, name, rate, initial_deposit)
                        print("\nMở tài khoản Tiết kiệm thành công!")
                    case "2":
                        try:
                            limit = float(input("Nhập hạn mức tín dụng (ví dụ 20000000): ").strip())
                        except ValueError:
                            print("Hạn mức phải là một số.")
                            continue
                        new_acc = CreditAccount(acc_num, name, limit, 0.0) 
                        print("\nMở tài khoản Tín dụng thành công!")
                    case "3":
                        try:
                            rate = float(input("Nhập lãi suất năm (ví dụ 0.06): ").strip())
                        except ValueError:
                            print("Lãi suất phải là một số thực.")
                            continue
                        new_acc = HybridAccount(acc_num, name, rate, initial_deposit)
                        print("\nMở tài khoản Đa năng thành công!")

                new_acc.account_holder = name 
                accounts.append(new_acc)
                current_account = new_acc
                print(f"Chủ tài khoản: {current_account.account_holder}")

            case "2":
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
                    continue
                
                print("\n--- THÔNG TIN TÀI KHOẢN HIỆN TẠI ---")
                print(f"Loại tài khoản: {type(current_account).__name__}")
                print(f"Ngân hàng: {current_account.bank_name}")
                print(f"Số tài khoản: {current_account.account_number}")
                print(f"Chủ tài khoản: {current_account.account_holder}")
                print(f"Số dư: {current_account.balance:,} VND")
                if hasattr(current_account, 'interest_rate'):
                    print(f"Lãi suất: {current_account.interest_rate * 100}% / năm")
                if hasattr(current_account, 'credit_limit'):
                    print(f"Hạn mức tín dụng: {current_account.credit_limit:,} VND")
                
                print("\n[Hệ thống kiểm tra MRO]:")
                mro_list = [cls.__name__ for cls in type(current_account).__mro__]
                print(" -> ".join(mro_list))

            case "3":
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
                    continue
                    
                print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
                print("1. Nạp tiền")
                print("2. Rút tiền")
                tx_choice = input("Chọn giao dịch (1-2): ").strip()
                
                try:
                    amount = float(input("Nhập số tiền: ").strip())
                except ValueError:
                    print("Số tiền phải là số hợp lệ.")
                    continue

                match tx_choice:
                    case "1":
                        current_account.deposit(amount)
                    case "2":
                        current_account.withdraw(amount)
                    case _:
                        print("Lựa chọn không đúng.")

            case "4":
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
                    continue
                    
                print("\n--- TÍNH LÃI ĐỊNH KỲ ---")
                if isinstance(current_account, SavingsAccount):
                    current_account.apply_interest()
                else:
                    print("Tính năng không hỗ trợ cho loại tài khoản này.")

            case "5":
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
                    continue
                    
                print("\n--- ĐỒNG BỘ & SO SÁNH TÀI KHOẢN (OPERATOR OVERLOADING) ---")
                if len(accounts) < 2:
                    dummy_acc = SavingsAccount("0987654321", "TRAN THI BINH", 0.05, 15000000.0)
                    accounts.append(dummy_acc)
                    print("[Thông báo]: Hệ thống tự động kích hoạt tài khoản đối ứng đối chứng (B): TRAN THI BINH (Số dư: 15,000,000 VND)")
                
                print(f"Tài khoản hiện tại (A): {current_account.account_holder} (Số dư: {current_account.balance:,} VND)")
                target_acc = accounts[-1] if accounts[-1] != current_account else accounts[0]
                print(f"Tài khoản đối ứng (B): {target_acc.account_holder} (Số dư: {target_acc.balance:,} VND)")
                
                if current_account < target_acc:
                    print("[Kết quả So sánh (__lt__)]: Số dư tài khoản A NHỎ HƠN số dư tài khoản B.")
                else:
                    print("[Kết quả So sánh (__lt__)]: Số dư tài khoản A LỚN HƠN HOẶC BẰNG số dư tài khoản B.")
                    
                total_sum = current_account + target_acc
                print(f"[Kết quả Tổng hợp (__add__)]: Tổng số tiền sở hữu của cả 2 tài khoản là: {total_sum:,} VND.")

            case "6":
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
                    continue
                    
                print("\n--- THANH TOÁN HÓA ĐƠN QUA CỔNG TRUNG GIAN ---")
                print("1. Thanh toán qua VNPay")
                print("2. Thanh toán qua Viettel Money")
                gateway_choice = input("Chọn cổng thanh toán (1-2): ").strip()
                
                try:
                    bill_amount = float(input("Nhập số tiền hóa đơn: ").strip())
                except ValueError:
                    print("Số tiền không hợp lệ.")
                    continue
                    
                match gateway_choice:
                    case "1":
                        gateway = VNPayGateway()
                    case "2":
                        gateway = ViettelMoneyGateway()
                    case _:
                        gateway = object() 
                    
                process_payment(gateway, current_account, bill_amount)

            case "7":
                print("\nCảm ơn đã trải nghiệm hệ thống Vietcombank Digibank Pro Simulator!")
                break
                
            case _:
                print("Chức năng chưa hợp lệ, xin vui lòng chọn từ 1-7.")

if __name__ == "__main__":
    main()