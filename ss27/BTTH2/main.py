from abc import ABC, abstractmethod

# ==========================================
# 1. CARRIER CLASSES (DUCK TYPING DEMO)
# ==========================================

class FedExCarrier:
    """Đối tác vận chuyển FedEx"""
    def ship_package(self, product, quantity: int):
        print(f"[Hệ thống FedEx]: Đang tiếp nhận mã sản phẩm {product.product_code}...")
        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Đơn vị vận chuyển đã tiếp nhận đơn hàng số lượng: {quantity} đơn vị.")


class DHLCarrier:
    """Đối tác vận chuyển DHL"""
    def ship_package(self, product, quantity: int):
        print(f"[Hệ thống DHL]: Đang xử lý phân phối cho mã sản phẩm {product.product_code}...")
        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Đơn vị vận chuyển đã tiếp nhận đơn hàng số lượng: {quantity} đơn vị.")


# ==========================================
# 2. CORE LOGISTICS CLASSES (OOP)
# ==========================================

class BaseProduct(ABC):
    """Lớp trừu tượng định nghĩa bộ khung chuẩn cho mọi loại hàng hóa trong kho"""
    warehouse_name = "Amazon Logistics"
    base_storage_fee = 5000  # Phí lưu kho cơ bản/ngày

    def __init__(self, product_code: str, product_name: str):
        self._product_code = product_code
        self.product_name = product_name
        self.__stock_quantity = 0  # Đóng gói nghiêm ngặt qua Private Attribute

    @property
    def product_code(self) -> str:
        return self._product_code

    @property
    def product_name(self) -> str:
        return self._product_name

    @product_name.setter
    def product_name(self, value: str):
        # Hệ thống tự động chuẩn hóa Tên (In hoa, xóa khoảng trắng thừa)
        self._product_name = " ".join(value.strip().split()).upper()

    @property
    def stock_quantity(self) -> int:
        """Property để đọc số lượng tồn kho hiện tại, không có setter trực tiếp"""
        return self.__stock_quantity

    def _update_stock_quantity(self, quantity: int):
        """Phương thức nội bộ để các lớp con cập nhật lại tồn kho"""
        self.__stock_quantity = quantity

    @abstractmethod
    def import_stock(self, quantity: int) -> bool:
        """Decorator @abstractmethod bắt buộc các lớp con phải ghi đè logic nhập kho"""
        pass

    @abstractmethod
    def export_stock(self, quantity: int) -> bool:
        """Decorator @abstractmethod bắt buộc các lớp con phải ghi đè logic xuất kho"""
        pass

    @staticmethod
    def validate_product_code(product_code: str) -> bool:
        """Decorator @staticmethod: Kiểm tra độc lập mã sản phẩm đầu vào"""
        return len(product_code) == 10 and product_code[0].isalpha()

    @classmethod
    def update_warehouse_name(cls, new_name: str):
        """Decorator @classmethod: Cập nhật tên chuỗi kho trên toàn hệ thống lớp"""
        cls.warehouse_name = new_name

    def __add__(self, other):
        """Nạp chồng toán tử cộng __add__: Cộng dồn số lượng tồn kho"""
        # Bẫy 3: Kiểm tra kiểu dữ liệu khi Overloading để tránh crash hệ thống
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity + other.stock_quantity

    def __lt__(self, other):
        """Nạp chồng toán tử so sánh __lt__: So sánh số lượng tồn kho"""
        # Bẫy 3: Kiểm tra kiểu dữ liệu khi Overloading
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity < other.stock_quantity


class ColdStorageProduct(BaseProduct):
    """Lớp con phục vụ quản lý hàng đông lạnh cần kiểm soát nhiệt độ"""
    def __init__(self, product_code: str, product_name: str, required_temperature: float):
        super().__init__(product_code, product_name)
        self.required_temperature = required_temperature

    def import_stock(self, quantity: int) -> bool:
        if quantity <= 0:
            print("Số lượng nhập kho phải lớn hơn 0.")
            return False
        self._update_stock_quantity(self.stock_quantity + quantity)
        print(f"Nhập kho thành công! Tồn kho hiện tại: {self.stock_quantity} đơn vị.")
        return True

    def export_stock(self, quantity: int) -> bool:
        if quantity <= 0:
            print("Số lượng xuất kho phải lớn hơn 0.")
            return False
        
        # Hàng đông lạnh chịu thêm 5% phí hao hụt bảo quản phụ trội tính trên số lượng xuất
        loss = quantity * 0.05
        total_deduct = quantity + loss
        
        if self.stock_quantity >= total_deduct:
            self._update_stock_quantity(int(self.stock_quantity - total_deduct))
            print("Xuất kho thành công!")
            print(f"Số lượng yêu cầu: {quantity} đơn vị")
            print(f"Số lượng hao hụt bảo quản (5%): {loss} đơn vị")
            print(f"Tổng số lượng khấu trừ trong kho: {total_deduct} đơn vị")
            return True
        else:
            print(f"Giao dịch thất bại! Số lượng tồn kho không đủ để khấu trừ cả hao hụt (Yêu cầu tổng: {total_deduct}).")
            return False

    def apply_cooling_cost(self) -> float:
        """Tính toán chi phí vận hành máy lạnh phát sinh dựa trên số lượng tồn kho"""
        # Giả định chi phi phát sinh bằng số lượng tồn kho nhân với hệ số nhiệt độ âm sâu
        cost = self.stock_quantity * abs(self.required_temperature) * 210
        return cost


class HazardousProduct(BaseProduct):
    """Lớp con quản lý hàng hóa nguy hiểm / Đảm bảo hạn mức lưu trữ an toàn"""
    def __init__(self, product_code: str, product_name: str, max_safety_limit: int = 500):
        super().__init__(product_code, product_name)
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity: int) -> bool:
        if quantity <= 0:
            print("Số lượng nhập kho phải lớn hơn 0.")
            return False
        
        # Bẫy 2: Ngăn chặn vượt quá giới hạn lưu kho an toàn
        if self.stock_quantity + quantity > self.max_safety_limit:
            print(f"Giao dịch thất bại! Số lượng nhập vào khiến tồn kho vượt quá hạn mức an toàn cho phép (Tối đa: {self.max_safety_limit}).")
            return False
            
        self._update_stock_quantity(self.stock_quantity + quantity)
        print(f"Nhập kho thành công! Tồn kho hiện tại: {self.stock_quantity} đơn vị.")
        return True

    def export_stock(self, quantity: int) -> bool:
        if quantity <= 0:
            print("Số lượng xuất kho phải lớn hơn 0.")
            return False
        if self.stock_quantity >= quantity:
            self._update_stock_quantity(self.stock_quantity - quantity)
            print(f"Xuất kho thành công! Tồn kho hiện tại: {self.stock_quantity} đơn vị.")
            return True
        print("Giao dịch thất bại! Số lượng tồn kho không đủ.")
        return False


class HybridPremiumProduct(ColdStorageProduct, HazardousProduct):
    """Dòng sản phẩm lai cao cấp kế thừa các đặc tính từ cả ColdStorage và Hazardous theo MRO"""
    def __init__(self, product_code: str, product_name: str, required_temperature: float, max_safety_limit: int):
        # Gọi __init__ theo thứ tự danh sách thiết lập MRO
        super().__init__(product_code, product_name, required_temperature)
        HazardousProduct.__init__(self, product_code, product_name, max_safety_limit)

    def import_stock(self, quantity: int) -> bool:
        """Tích hợp kiểm tra giới hạn an toàn của hàng nguy hiểm trước khi nhập của hàng đông lạnh"""
        if self.stock_quantity + quantity > self.max_safety_limit:
            print(f"Giao dịch thất bại! Số lượng nhập vào khiến tồn kho vượt quá hạn mức an toàn cho phép (Tối đa: {self.max_safety_limit}).")
            return False
        return super().import_stock(quantity)

    def export_stock(self, quantity: int) -> bool:
        """Kế thừa hành vi xuất kho có tính hao hụt đặc thù của hàng đông lạnh"""
        return super().export_stock(quantity)


# ==========================================
# 3. GLOBAL DUCK TYPING METHOD
# ==========================================

def dispatch_to_carrier(carrier_agent, product: BaseProduct, quantity: int):
    """Hàm toàn cục thực thi điều phối vận chuyển áp dụng cơ chế Duck Typing"""
    try:
        # Bẫy 4: Sai lệch phương thức trong Duck Typing (Kiểm tra sự tồn tại của hàm ship_package)
        if not hasattr(carrier_agent, "ship_package"):
            raise AttributeError("Đơn vị vận chuyển không hợp lệ hoặc chưa ký kết hợp đồng kỹ thuật.")
        
        # Thực hiện xuất kho thử nghiệm trước khi giao cho đơn vị vận chuyển
        if product.export_stock(quantity):
            carrier_agent.ship_package(product, quantity)
            print(f"Số lượng tồn kho cập nhật: {product.stock_quantity} đơn vị.")
            return True
        return False
    except AttributeError as e:
        print(f"Lỗi hệ thống: {e}")
        return False


# ==========================================
# 4. CLI MENU SYSTEM WITH MATCH-CASE
# ==========================================

def main():
    products = []
    current_product = None

    while True:
        print("\n===== AMAZON INVENTORY SIMULATOR PRO =====")
        print("1. Đăng ký mã hàng hóa mới (Chọn loại sản phẩm)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Giao dịch Nhập / Xuất kho (Đa hình)")
        print("4. Kiểm tra điều kiện bảo quản / Tính chi phí phụ trội")
        print("5. Kiểm tra tính năng gộp lô hàng & So sánh tồn kho (Overloading)")
        print("6. Điều phối vận chuyển qua Đối tác thứ ba (Duck Typing)")
        print("7. Thoát chương trình")
        print("==========================================")
        
        choice = input("Chọn chức năng (1-7): ").strip()

        match choice:
            case "1":
                print("\n--- CHỌN LOẠI SẢN PHẨM KHỞI TẠO ---")
                print("1. Cold Storage Product (Hàng Đông Lạnh)")
                print("2. Hazardous Product (Hàng Nguy Hiểm)")
                print("3. Hybrid Premium Product (Hàng Lai Cao Cấp)")
                type_choice = input("Chọn loại sản phẩm (1-3): ").strip()

                if type_choice not in ["1", "2", "3"]:
                    print("Lựa chọn loại hàng hóa không hợp lệ.")
                    continue

                prod_code = input("Nhập mã sản phẩm 10 ký tự: ").strip()
                # Kiểm tra tính hợp lệ của mã qua phương thức staticmethod
                if not BaseProduct.validate_product_code(prod_code):
                    print("Mã sản phẩm không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng chữ.")
                    continue

                name = input("Nhập tên sản phẩm: ")
                new_prod = None

                match type_choice:
                    case "1":
                        try:
                            temp = float(input("Nhập nhiệt độ bảo quản yêu cầu (độ C): ").strip())
                        except ValueError:
                            print("Nhiệt độ phải là số thực.")
                            continue
                        new_prod = ColdStorageProduct(prod_code, name, temp)
                        print(f"Đăng ký sản phẩm Đông Lạnh thành công!")
                    case "2":
                        try:
                            limit = int(input("Nhập hạn mức an toàn tối đa (ví dụ 500): ").strip())
                        except ValueError:
                            print("Hạn mức phải là số nguyên.")
                            continue
                        new_prod = HazardousProduct(prod_code, name, limit)
                        print(f"Đăng ký sản phẩm Nguy Hiểm thành công!")
                    case "3":
                        try:
                            temp = float(input("Nhập nhiệt độ bảo quản yêu cầu (độ C): ").strip())
                            limit = int(input("Nhập hạn mức an toàn tối đa: ").strip())
                        except ValueError:
                            print("Dữ liệu đầu vào sai kiểu định dạng số.")
                            continue
                        new_prod = HybridPremiumProduct(prod_code, name, temp, limit)
                        print(f"Đăng ký sản phẩm Lai Cao Cấp thành công!")

                # Chuẩn hóa tên tự động được thực hiện qua setter property khi gán giá trị
                new_prod.product_name = name
                products.append(new_prod)
                current_product = new_prod
                print(f"Tên sản phẩm: {current_product.product_name}")

            case "2":
                if current_product is None:
                    print("Hệ thống chưa ghi nhận sản phẩm hiện tại nào. Vui lòng tạo ở Chức năng 1.")
                    continue

                print("\n--- THÔNG TIN SẢN PHẨM HIỆN TẠI ---")
                print(f"Loại sản phẩm: {type(current_product).__name__}")
                print(f"Chuỗi kho: {current_product.warehouse_name}")
                print(f"Mã sản phẩm: {current_product.product_code}")
                print(f"Tên sản phẩm: {current_product.product_name}")
                print(f"Số lượng tồn kho: {current_product.stock_quantity} đơn vị")
                
                if hasattr(current_product, 'required_temperature'):
                    print(f"Nhiệt độ yêu cầu: {current_product.required_temperature} độ C")
                if hasattr(current_product, 'max_safety_limit'):
                    print(f"Hạn mức an toàn tối đa: {current_product.max_safety_limit} đơn vị")

                print("\n[Hệ thống kiểm tra MRO]:")
                mro_list = [cls.__name__ for cls in type(current_product).__mro__]
                print(" -> ".join(mro_list))

            case "3":
                if current_product is None:
                    print("Hệ thống chưa có sản phẩm hoạt động. Vui lòng tạo ở Chức năng 1.")
                    continue

                print("\n--- GIAO DỊCH NHẬP / XUẤT KHO ---")
                print("1. Nhập kho")
                print("2. Xuất kho")
                tx_choice = input("Chọn giao dịch (1-2): ").strip()

                try:
                    qty = int(input("Nhập số lượng hàng hóa: ").strip())
                except ValueError:
                    print("Số lượng bắt buộc phải là số nguyên.")
                    continue

                # Tính đa hình (Polymorphism) tự động kích hoạt logic chuẩn xác tùy theo thực thể lớp con
                match tx_choice:
                    case "1":
                        current_product.import_stock(qty)
                    case "2":
                        current_product.export_stock(qty)
                    case _:
                        print("Lựa chọn nghiệp vụ không chính xác.")

            case "4":
                if current_product is None:
                    print("Hệ thống chưa có sản phẩm hoạt động.")
                    continue

                print("\n--- TÍNH PHÍ BẢO QUẢN ĐÔNG LẠNH ---")
                # Kiểm tra xem sản phẩm hiện tại có thuộc nhánh đông lạnh để tính phí phát sinh không
                if isinstance(current_product, ColdStorageProduct):
                    cost = current_product.apply_cooling_cost()
                    print(f"Số lượng tồn kho hiện tại: {current_product.stock_quantity} đơn vị")
                    print(f"Nhiệt độ yêu cầu: {current_product.required_temperature} độ C")
                    print(f"Chi phí làm lạnh phát sinh trong ngày: +{cost:,} VND")
                else:
                    print("Tính năng không hỗ trợ! Sản phẩm hiện tại không thuộc nhóm yêu cầu kiểm soát nhiệt độ.")

            case "5":
                if current_product is None:
                    print("Hệ thống chưa có sản phẩm hoạt động.")
                    continue

                print("\n--- ĐỒNG BỘ & SO SÁNH TỒN KHO (OPERATOR OVERLOADING) ---")
                if len(products) < 2:
                    # Tự động tạo nhanh một lô sản phẩm đối ứng để demo Overloading nếu danh sách chỉ có 1
                    dummy_prod = ColdStorageProduct("AMZ9999999", "BEEF STEAK", -18.0)
                    dummy_prod.import_stock(350)
                    products.append(dummy_prod)
                    print("[Thông báo]: Hệ thống tự động thiết lập sản phẩm đối ứng (B): BEEF STEAK (Tồn kho: 350 đơn vị)")

                print(f"Sản phẩm hiện tại (A): {current_product.product_name} (Tồn kho: {current_product.stock_quantity} đơn vị)")
                target_prod = products[-1] if products[-1] != current_product else products[0]
                print(f"Chọn sản phẩm đối ứng (B) từ danh sách: {target_prod.product_code} ({target_prod.product_name} - Tồn kho: {target_prod.stock_quantity} đơn vị)")

                # Thử nghiệm tính toán so sánh qua __lt__ overloading
                if current_product < target_prod:
                    print("[Kết quả So sánh (__lt__)]: Tồn kho sản phẩm A ÍT HƠN tồn kho sản phẩm B.")
                else:
                    print("[Kết quả So sánh (__lt__)]: Tồn kho sản phẩm A LỚN HƠN HOẶC BẰNG tồn kho sản phẩm B.")

                # Thử nghiệm tính tổng qua __add__ overloading
                total_sum = current_product + target_prod
                print(f"[Kết quả Tổng hợp (__add__)]: Tổng số lượng tồn kho của cả 2 mã sản phẩm là: {total_sum} đơn vị.")

            case "6":
                if current_product is None:
                    print("Hệ thống chưa có sản phẩm hoạt động.")
                    continue

                print("\n--- ĐIỀU PHỐI ĐƠN VỊ VẬN CHUYỂN NGOÀI ---")
                print("1. Vận chuyển qua đối tác FedEx")
                print("2. Vận chuyển qua đối tác DHL")
                carrier_choice = input("Chọn đối tác vận chuyển (1-2): ").strip()

                try:
                    qty = int(input("Nhập số lượng hàng hóa bàn giao: ").strip())
                except ValueError:
                    print("Số lượng hàng hóa phải là số nguyên.")
                    continue

                match carrier_choice:
                    case "1":
                        carrier = FedExCarrier()
                    case "2":
                        carrier = DHLCarrier()
                    case _:
                        # Gán một đối tượng trống không có hàm ship_package để kích hoạt thử nghiệm Bẫy số 4
                        carrier = object()

                dispatch_to_carrier(carrier, current_product, qty)

            case "7":
                print("\nCảm ơn đã sử dụng hệ thống Amazon Inventory Simulator Pro!")
                break

            case _:
                print("Chức năng không hợp lệ, vui lòng chọn lại từ 1-7.")

if __name__ == "__main__":
    # Minh họa Bẫy 1: Ngăn chặn tạo đối tượng từ lớp trừu tượng directly
    try:
        # Dòng code này cố tình kích hoạt thử nghiệm nhằm chứng minh cơ chế an toàn bảo vệ của ABC
        # abstract_item = BaseProduct("AMZTEST123", "TEST PRODUCT")
        pass
    except TypeError as error:
        print(f"[CẢNH BÁO KIẾN TRÚC]: {error}")

    main()