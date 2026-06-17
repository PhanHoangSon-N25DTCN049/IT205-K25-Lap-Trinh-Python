import re

class BistroTable:
    # Class Attribute - Thuế suất VAT áp dụng chung toàn hệ thống
    _vat_rate = 0.08

    def __init__(self, table_id, capacity):
        self.__table_id = table_id
        self.capacity = capacity
        self.__current_bill = 0

    # Getter cho mã bàn
    @property
    def table_id(self):
        return self.__table_id

    # Getter cho tiền tạm tính
    @property
    def current_bill(self):
        return self.__current_bill

    # Getter tính toán trạng thái động dựa trên số tiền tạm tính
    @property
    def status(self):
        return "Đang trống" if self.__current_bill == 0 else "Có khách"

    # Getter tính tổng tiền gồm thuế VAT khi thanh toán
    @property
    def final_bill(self):
        return self.__current_bill * (1 + BistroTable._vat_rate)

    # Instance Method: Gọi món mới (Tăng tiền hóa đơn)
    def order_dish(self, amount):
        if amount <= 0:
            print("Lỗi: Vui lòng nhập số tiền là một số nguyên dương!")
            return False
        
        self.__current_bill += amount
        print(f">> Thành công: Đã ghi nhận món ăn {amount:,}đ vào Bàn '{self.__table_id}'.")
        print(f">> Số tiền tạm tính hiện tại của bàn: {self.__current_bill:,}đ.")
        return True

    # Instance Method: Hủy món / Giảm trừ hóa đơn (Bẫy 2 & Bẫy 5)
    def cancel_dish(self, amount):
        if amount <= 0:
            print("Lỗi: Vui lòng nhập số tiền là một số nguyên dương!")
            return False
            
        if amount > self.__current_bill:
            print("Lỗi: Số tiền giảm trừ vượt quá giá trị hóa đơn hiện tại!")
            return False

        self.__current_bill -= amount
        print(f">> Thành công: Đã giảm trừ {amount:,}đ khỏi Bàn '{self.__table_id}' do sự cố bếp.")
        print(f">> Số tiền tạm tính còn lại: {self.__current_bill:,}đ.")
        
        if self.__current_bill == 0:
            print(f">> Bàn '{self.__table_id}' hiện đã chuyển về trạng thái Đang trống.")
        return True

    # Instance Method: Thanh toán hóa đơn (Bẫy 3)
    def checkout(self):
        if self.__current_bill == 0:
            print("Lỗi: Bàn này hiện đang trống, không có hóa đơn để thanh toán!")
            return False

        print(f"\n--- HÓA ĐƠN THANH TOÁN BÀN {self.__table_id} ---")
        print(f"Số tiền món ăn: {self.__current_bill:,}đ")
        print(f"Thuế suất VAT áp dụng: {BistroTable._vat_rate * 100:.0f}%")
        print(f"Tổng tiền cần thanh toán (gồm thuế): {self.final_bill:,}đ")
        print("-----------------------------------")
        
        # Reset hóa đơn về 0 và chuyển trạng thái về Đang trống
        self.__current_bill = 0
        print(f">> Thanh toán thành công! Bàn '{self.__table_id}' đã được dọn sạch và chuyển sang trạng thái Đang trống.")
        return True

    # Class Method: Cập nhật thuế suất VAT toàn nhà hàng (Bẫy 4)
    @classmethod
    def update_vat_rate(cls, new_rate):
        if 0.0 <= new_rate <= 0.2:
            cls._vat_rate = new_rate
            print(f"\n>> Thông báo: Rikkei Bistro cập nhật thuế suất VAT mới ở mức {cls._vat_rate * 100:.0f}% thành công!")
            return True
        else:
            print("Lỗi: Tỷ lệ thuế không hợp lệ!")
            return False

    # Getter để bên ngoài lấy thông tin mức thuế hiện hành
    @classmethod
    def get_vat_rate(cls):
        return cls._vat_rate

    # Static Method: Kiểm tra định dạng mã bàn (Bẫy 1)
    @staticmethod
    def is_valid_table_id(table_code):
        # Định dạng chuẩn: Bắt đầu bằng 'TB' và theo sau có ít nhất 1 chữ số (tổng độ dài >= 3)
        return bool(re.match(r"^TB\d+$", table_code)) and len(table_code) >= 3


# --- CHƯƠNG TRÌNH ĐIỀU KHIỂN CHÍNH (MAIN FLOW) ---
def main():
    # Khởi tạo danh sách các bàn ăn theo dữ liệu mẫu của đề bài
    table_records = [
        BistroTable("TB01", 4),
        BistroTable("TB02", 2),
        BistroTable("TB03", 8)
    ]

    while True:
        print("\n===== HỆ THỐNG ĐIỀU PHỐI BÀN ĂN - RIKKEI BISTRO =====")
        print("1. Hiển thị sơ đồ & Trạng thái bàn ăn")
        print("2. Gọi món mới (Tăng tiền hóa đơn)")
        print("3. Hủy món / Giảm trừ hóa đơn (Sự cố nhà bếp)")
        print("4. Cập nhật thuế suất VAT toàn nhà hàng")
        print("5. Thanh toán hóa đơn & Trả bàn trống")
        print("6. Thoát chương trình")
        print("=====================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                print("\n--- SƠ ĐỒ BÀN ĂN RIKKEI BISTRO ---")
                for idx, table in enumerate(table_records, 1):
                    print(f"{idx}. Mã bàn: {table.table_id} | Sức chứa: {table.capacity} người | Tạm tính: {table.current_bill:,}đ | Trạng thái: {table.status}")
                print("----------------------------------")

            case "2":
                print("\n--- GỌI MÓN MỚI ---")
                table_id = input("Nhập mã bàn gọi món: ").strip().upper()  # Bẫy 1: Chuẩn hóa chữ thường thành hoa
                
                if not BistroTable.is_valid_table_id(table_id):
                    print("Lỗi: Mã bàn không hợp lệ!")
                    continue
                    
                table = next((t for t in table_records if t.table_id == table_id), None)
                if not table:
                    print("Lỗi: Không tìm thấy mã bàn này trong hệ thống!")
                    continue
                    
                try:
                    amount = int(input("Nhập giá tiền món ăn mới: "))
                    table.order_dish(amount)
                except ValueError:
                    print("Lỗi: Vui lòng nhập số tiền là một số nguyên dương!")

            case "3":
                print("\n--- HỦY MÓN / GIẢM TRỪ HÓA ĐƠN ---")
                table_id = input("Nhập mã bàn cần hủy món: ").strip().upper()
                
                if not BistroTable.is_valid_table_id(table_id):
                    print("Lỗi: Mã bàn không hợp lệ!")
                    continue
                    
                table = next((t for t in table_records if t.table_id == table_id), None)
                if not table:
                    print("Lỗi: Không tìm thấy mã bàn này trong hệ thống!")
                    continue
                    
                try:
                    amount = int(input("Nhập giá trị món muốn giảm trừ: "))
                    table.cancel_dish(amount)
                except ValueError:
                    print("Lỗi: Vui lòng nhập số tiền là một số nguyên dương!")

            case "4":
                print("\n--- CẬP NHẬT THUẾ SUẤT VAT TOÀN NHÀ HÀNG ---")
                current_vat = BistroTable.get_vat_rate()
                print(f"[HỆ THỐNG] Thuế suất VAT hiện tại là: {current_vat * 100:.0f}% ({current_vat})")
                
                try:
                    new_rate = float(input("Nhập thuế suất VAT mới (ví dụ: 0.1 cho 10%): "))
                    BistroTable.update_vat_rate(new_rate)
                except ValueError:
                    print("Lỗi: Tỷ lệ thuế không hợp lệ!")

            case "5":
                print("\n--- THANH TOÁN HÓA ĐƠN ---")
                table_id = input("Nhập mã bàn thanh toán: ").strip().upper()
                
                if not BistroTable.is_valid_table_id(table_id):
                    print("Lỗi: Mã bàn không hợp lệ!")
                    continue
                    
                table = next((t for t in table_records if t.table_id == table_id), None)
                if not table:
                    print("Lỗi: Không tìm thấy mã bàn này trong hệ thống!")
                    continue
                    
                table.checkout()

            case "6":
                print("\nCảm ơn bạn đã sử dụng hệ thống điều phối bàn ăn Rikkei Bistro!")
                break

            case _:
                print("\nChức năng không hợp lệ! Vui lòng chọn từ 1 đến 6.")

if __name__ == "__main__":
    main()