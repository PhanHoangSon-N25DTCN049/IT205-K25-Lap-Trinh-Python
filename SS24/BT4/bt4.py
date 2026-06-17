import re

class MenuItem:
    # Class Attribute - Phụ phí dịch vụ dùng chung toàn hệ thống
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name
        # Bảo mật dữ liệu bằng Name Mangling nhằm tránh can thiệp trực tiếp bên ngoài
        self.__base_price = base_price
        self.__is_available = True

    # Getter cho giá gốc
    @property
    def base_price(self):
        return self.__base_price

    # Setter cho giá gốc (Bẫy 2: Kiểm tra dữ liệu hợp lệ)
    @base_price.setter
    def base_price(self, new_price):
        if new_price > 0:
            self.__base_price = new_price
            print("Cập nhật giá gốc thành công!")
        else:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")

    # Getter cho trạng thái bán (Chỉ đọc)
    @property
    def is_available(self):
        return self.__is_available

    # Instance Method: Đảo ngược trạng thái phục vụ của món ăn
    def toggle_availability(self):
        self.__is_available = not self.__is_available
        status_str = "ĐANG BÁN" if self.__is_available else "HẾT HÀNG"
        print(f">> Đã cập nhật {self.item_name} thành {status_str}!")

    # Instance Method: Tính toán giá bán niêm yết cuối cùng cho khách
    def calculate_selling_price(self):
        return self.__base_price + (self.__base_price * MenuItem.service_charge)

    # Class Method: Cập nhật phụ phí dịch vụ toàn hệ thống
    @classmethod
    def update_service_charge(cls, new_rate):
        if 0 <= new_rate <= 1:
            cls.service_charge = new_rate
            print("Cập nhật phụ phí dịch vụ thành công!")
        else:
            print("Mức phụ phí dịch vụ không hợp lệ (phải từ 0.0 đến 1.0)!")

    # Static Method: Kiểm tra tính hợp lệ của mã món trước khi tạo thực thể
    @staticmethod
    def is_valid_item_id(item_code):
        # Quy tắc: 2 chữ cái in hoa đầu, theo sau là đúng 2 chữ số
        return bool(re.match(r"^[A-Z]{2}\d{2}$", item_code))


# --- CHƯƠNG TRÌNH ĐIỀU KHIỂN CHÍNH (MAIN FLOW) ---
def main():
    # Khởi tạo Mock data ban đầu theo yêu cầu
    menu_db = [
        MenuItem("CF01", "Cà Phê Đen", 30000),
        MenuItem("CF02", "Bạc Xỉu", 45000),
        MenuItem("TE01", "Trà Đào Cam Sả", 50000)
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
        print("1. Xem thực đơn & Giá niêm yết")
        print("2. Thêm món mới vào menu")
        print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
        print("4. Điều chỉnh giá gốc của món")
        print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
        print("6. Thoát chương trình")
        print("======================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")
                if not menu_db:
                    print("Thực đơn đang trống.")
                    continue
                for idx, item in enumerate(menu_db, 1):
                    status = "Đang bán" if item.is_available else "Hết hàng"
                    selling_price = item.calculate_selling_price()
                    print(f"{idx}. Mã: {item.item_id} | Tên: {item.item_name:<15} | Trạng thái: {status:<9} | Giá niêm yết: {selling_price:,.0f} VNĐ")
            
            case "2":
                print("\n--- THÊM MÓN MỚI VÀO MENU ---")
                item_id = input("Nhập mã món: ").strip()
                
                # Kiểm tra định dạng mã món qua Static Method
                if not MenuItem.is_valid_item_id(item_id):
                    print("\nMã món không hợp lệ!")
                    print("Mã món phải gồm 2 chữ cái in hoa và 2 chữ số. Ví dụ: CF01.")
                    continue
                
                # Bẫy 3: Kiểm tra trùng lặp mã món
                if any(item.item_id == item_id for item in menu_db):
                    print("\nMã món đã tồn tại trong thực đơn! Không thể thêm mới.")
                    continue
                
                item_name = input("Nhập tên món: ").strip()
                try:
                    base_price = float(input("Nhập giá gốc: "))
                    if base_price <= 0:
                        print("Giá gốc ban đầu phải lớn hơn 0!")
                        continue
                    
                    # Khởi tạo đối tượng mới an toàn và đẩy vào db
                    new_item = MenuItem(item_id, item_name, base_price)
                    menu_db.append(new_item)
                    print("\nThêm món mới thành công!")
                except ValueError:
                    print("Vui lòng nhập giá tiền hợp lệ!")
            
            case "3":
                print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")
                item_id = input("Nhập mã món cần cập nhật: ").strip()
                
                # Tìm kiếm đối tượng bằng mã món công khai
                item = next((i for i in menu_db if i.item_id == item_id), None)
                if item:
                    item.toggle_availability()
                else:
                    print("Không tìm thấy mã món này trong hệ thống!")
            
            case "4":
                print("\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")
                item_id = input("Nhập mã món cần đổi giá: ").strip()
                
                item = next((i for i in menu_db if i.item_id == item_id), None)
                if item:
                    try:
                        new_price = float(input("Nhập giá tiền mới: "))
                        # Thay đổi giá trị gián tiếp qua setter để kích hoạt bộ lọc kiểm duyệt
                        item.base_price = new_price
                    except ValueError:
                        print("Vui lòng nhập số tiền hợp lệ!")
                else:
                    print("Không tìm thấy mã món này trong hệ thống!")
            
            case "5":
                print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")
                print(f"Phụ phí hiện tại: {MenuItem.service_charge * 100:.0f}%")
                try:
                    new_rate = float(input("Nhập phụ phí mới. Ví dụ 0.1 tương ứng 10%: "))
                    # Gọi trực tiếp thông qua Class Method để đồng bộ toàn hệ thống
                    MenuItem.update_service_charge(new_rate)
                except ValueError:
                    print("Vui lòng nhập số thập phân hợp lệ!")
            
            case "6":
                print("\nCảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
                break
                
            case _:
                print("\nChức năng không hợp lệ! Vui lòng chọn lại từ 1 đến 6.")

if __name__ == "__main__":
    main()