"""
Quan sát dòng gọi hàm ban đầu, giá trị 15000 đã bị gán nhầm vào tham số discount, còn 0.1 lại được gán vào shipping_fee.
Sự sai lệch vị trí này khiến công thức tính toán bên trong bị đổi thành 100000 - (100000 * 15000) + 0.1, làm tiền gốc bị nhân với 15000 thành 1 tỷ rưỡi,
dẫn đến kết quả trả ra là con số âm khổng lồ -1499999999.9. Tiếp theo, biến order_total lúc này mang giá trị None vì hàm calculate_final_price chỉ dùng lệnh print() mà không có lệnh return.
Trong Python, nếu hàm không có return thì mặc định sẽ trả về None. Khi chương trình chạy đến dòng final_payment = order_total + 5000, hệ thống cố gắng cộng kiểu dữ liệu NoneType với số nguyên (int),
trực tiếp gây ra lỗi TypeError. Sự khác biệt cốt lõi là print chỉ in thông tin ra màn hình,
trong khi return mới thực sự đẩy dữ liệu ra khỏi hàm để lưu trữ và tính toán ở các bước sau.
Cách khắc phục là thay lệnh print thành return và truyền lại đúng thứ tự các tham số khi gọi hàm.
"""

def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total

order_total = calculate_final_price(100000, 0.1, 15000)

final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)