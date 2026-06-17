# Hệ thống quản lý hóa đơn Rikkei Coffee đã được sửa lỗi
class CoffeeOrder:
    # Thuộc tính của lớp (Class Attribute) - Áp dụng chung toàn hệ thống
    _vat_rate = 0.10  # Sử dụng một dấu gạch dưới để biểu thị thuộc tính bảo vệ của lớp

    def __init__(self, table_number):
        self.table_number = table_number
        # Sửa lỗi 1: Sử dụng __ để kích hoạt Name Mangling, bảo vệ thuộc tính
        self.__total_amount = 0  

    # Khởi tạo thuộc tính chỉ đọc (Getter) để xem tổng tiền an toàn từ bên ngoài
    @property
    def total_amount(self):
        return self.__total_amount

    # Phương thức thêm tiền món ăn vào hóa đơn
    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    # Tính tổng tiền khách phải trả (đã cộng VAT)
    def calculate_final_bill(self):
        return self.__total_amount + (self.__total_amount * CoffeeOrder._vat_rate)

    # Sửa lỗi 2: Chuyển đổi thành Class Method để cập nhật Class Attribute đồng bộ
    @classmethod
    def update_vat_rate(cls, new_rate):
        if 0 <= new_rate <= 1:
            cls._vat_rate = new_rate

    # Getter để các đối tượng lấy giá trị VAT hiện tại từ Class
    @property
    def vat_rate(self):
        return CoffeeOrder._vat_rate



order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")


order_table1.add_item(50000) 
order_table2.add_item(30000) 

# 1. Thử nghiệm tấn công: Nhân viên gian lận cố tình gán đè tổng tiền về 0 từ bên ngoài
try:
    order_table1.total_amount = 0
except AttributeError:
    print("[Bảo mật]: Không thể thay đổi trực tiếp tổng tiền từ bên ngoài!")


CoffeeOrder.update_vat_rate(0.08)


print("---------------------------------------------")
print(f"Tổng tiền gốc Bàn 1: {order_table1.total_amount} VNĐ (Không bị sửa về 0)")
print(f"Tổng hóa đơn thanh toán Bàn 1 (sau VAT): {order_table1.calculate_final_bill()} VNĐ")
print(f"Thuế VAT đang áp dụng cho Bàn 1: {order_table1.vat_rate * 100}%")
print(f"Thuế VAT đang áp dụng cho Bàn 2: {order_table2.vat_rate * 100}% (Đã đồng bộ thành công!)")