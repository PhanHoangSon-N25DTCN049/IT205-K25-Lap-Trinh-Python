class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        # Thuộc tính ẩn danh (Private) áp dụng cơ chế Name Mangling để bảo mật giá bán
        self.__price = price
        self.is_available = True

    # Getter sử dụng decorator @property để lấy giá bán an toàn từ bên ngoài
    @property
    def price(self):
        return self.__price

    # Instance Method: Đảo ngược trạng thái kinh doanh của đồ uống
    def toggle_available(self):
        self.is_available = not self.is_available
        status_str = "Đang bán" if self.is_available else "Ngừng bán"
        print(f"\nĐã cập nhật trạng thái món {self.code}.")
        print(f"Trạng thái hiện tại: {status_str}")


# --- CHƯƠNG TRÌNH ĐIỀU KHIỂN CHÍNH (MAIN FLOW WITH MATCH-CASE) ---
def main():
    # Dữ liệu khởi tạo mẫu chứa các Object Drink
    menu = [
        Drink("CF01", "Cà phê sữa", 35000),
        Drink("TS01", "Trà sữa matcha", 45000),
        Drink("TD01", "Trà đào cam sả", 40000)
    ]

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
        print("1. Xem danh sách đồ uống")
        print("2. Thêm đồ uống mới")
        print("3. Cập nhật trạng thái kinh doanh")
        print("4. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()

        match choice:
            case "1":
                print("\n--- DANH SÁCH ĐỒ UỐNG ---\n")
                print(f"{'Mã món':<7} | {'Tên món':<16} | {'Giá bán':<7} | Trạng thái")
                print("-" * 49)
                for drink in menu:
                    status = "Đang bán" if drink.is_available else "Ngừng bán"
                    # Truy cập giá bán thông qua property 'drink.price' thay vì '__price'
                    print(f"{drink.code:<7} | {drink.name:<16} | {drink.price:<7} | {status}")
            
            case "2":
                print("\n--- THÊM ĐỒ UỐNG MỚI ---")
                code = input("Nhập mã món: ").strip()
                
                # Kiểm tra trùng lặp mã món trong danh sách menu hiện tại
                if any(drink.code.upper() == code.upper() for drink in menu):
                    print("Mã món đã tồn tại trong hệ thống!")
                    continue
                    
                name = input("Nhập tên món: ").strip()
                try:
                    price = float(input("Nhập giá bán: "))
                    # Kiểm tra tính hợp lệ của giá bán
                    if price <= 0:
                        print("Giá bán không hợp lệ!")
                        continue
                    
                    # Khởi tạo Object mới từ Class Drink và append vào danh sách
                    new_drink = Drink(code, name, price)
                    menu.append(new_drink)
                    print(f"\nThành công: Đã thêm món {name} vào thực đơn!")
                except ValueError:
                    print("Giá bán không hợp lệ!")
            
            case "3":
                print("\n--- CẬP NHẬT TRẠNG THÁI KINH DOANH ---")
                code = input("Nhập mã món cần cập nhật: ").strip()
                
                # Tìm kiếm Object đồ uống tương ứng bằng mã món
                drink = next((d for d in menu if d.code.upper() == code.upper()), None)
                if drink:
                    drink.toggle_available()
                else:
                    print("Không tìm thấy món có mã này!")
            
            case "4":
                print("\nCảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
                break
                
            case _:
                print("\nChức năng không hợp lệ! Vui lòng chọn lại từ 1 đến 4.")

if __name__ == "__main__":
    main()