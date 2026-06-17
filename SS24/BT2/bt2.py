# Hệ thống Thẻ thành viên Rikkei Coffee đã được sửa lỗi hoàn chỉnh
class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        # Khởi tạo thông qua setter để đảm bảo dữ liệu truyền vào lúc đầu cũng được kiểm duyệt
        self.points = points  

    # Sử dụng @property để tạo getter cho phép đọc thuộc tính an toàn từ bên ngoài
    @property
    def points(self):
        return self.__points

    # Sử dụng @points.setter để thiết lập bộ lọc kiểm duyệt dữ liệu
    @points.setter
    def points(self, value):
        # Kiểm tra nếu giá trị không phải số nguyên hoặc nhỏ hơn 0
        if not isinstance(value, int) or value < 0:
            print("Dữ liệu điểm không hợp lệ!")
        else:
            self.__points = value

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.points += amount
        else:
            print("Số điểm cộng thêm phải là số nguyên dương!")

    # Sửa đổi thành Static Method, loại bỏ tham số self
    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


# --- KỊCH BẢN KIỂM CHỨNG HỆ THỐNG ---

# Khởi tạo thẻ thành viên ban đầu hợp lệ
card1 = MemberCard("Le Van C", 100)

print("--- THỬ NGHIỆM GÁN DỮ LIỆU ĐIỂM SAI TRONG THU NGÂN ---")
# 1. Thu ngân gõ nhầm, gán điểm thành số âm (Hệ thống sẽ từ chối và giữ nguyên điểm cũ)
card1.points = -50  

# 2. Thu ngân gõ nhầm sang dạng chuỗi văn bản (Hệ thống từ chối)
card1.points = "một trăm"

print(f"\n=> Kết quả đồng bộ - Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")
print("-----------------------------------------------------")

print("--- KIỂM TRA LOGIC KHUYẾN MÃI QUA STATIC METHOD ---")
# 3. Gọi trực tiếp từ Class MemberCard mà không cần tạo đối tượng "ảo"
bill_test = 250000
result = MemberCard.is_eligible_for_voucher(bill_test)  

print(f"Hóa đơn {bill_test:,} VNĐ có đủ điều kiện nhận Voucher không? -> {result}")