# Dữ liệu đầu vào (Input):
# Mã bệnh nhân: Kiểu chuỗi (str).
# Nhiệt độ cơ thể: Kiểu chuỗi (str) - do nhận từ hàm input().
# Nhịp tim: Kiểu chuỗi (str) - do nhận từ hàm input().

# Kiểu dữ liệu mong muốn đầu ra (Output):
# Mã bệnh nhân: Kiểu chuỗi (str).
# Nhiệt độ cơ thể: Số thực (float).
# Nhịp tim: Số nguyên (int)

# Giải pháp 1 (Ép kiểu gián tiếp): Nhập dữ liệu thô vào các biến tạm thời dưới dạng chuỗi, sau đó mới thực hiện ép kiểu và gán sang biến chính thức.
# Giải pháp 2 (Ép kiểu trực tiếp): Bọc các hàm ép kiểu float() và int() ngay bên ngoài hàm input() tại thời điểm nhập liệu.


# Số lượng biến (Bộ nhớ): Giải pháp 2 tối ưu hơn vì không cần tạo các biến chuỗi tạm thời như Giải pháp 1.
# Độ ngắn gọn của code: Giải pháp 2 ngắn gọn hơn, giảm một nửa số dòng lệnh xử lý nhập liệu.
# Khả năng dễ debug (Dò lỗi): Giải pháp 1 dễ tách biệt lỗi nhập liệu với lỗi ép kiểu hơn. Tuy nhiên, Giải pháp 2 vẫn dễ dàng bắt lỗi nếu kết hợp với các khối lệnh xử lý ngoại lệ sau này.
# Chốt lựa chọn: Giải pháp 2 (Ép kiểu trực tiếp) là phù hợp nhất trong môi trường cấp cứu bệnh viện.
# Lý do: Mã nguồn ngắn gọn giúp hệ thống vận hành nhanh, giảm thiểu độ trễ tối đa và tiết kiệm tài nguyên bộ nhớ cho các thiết bị Monitor chuyên dụng vốn cần xử lý luồng dữ liệu sinh hiệu liên tục.


print("--- HỆ THỐNG TIẾP NHẬN VÀ CHUẨN HÓA SINH HIỆU ---")
# Tiếp nhận và ép kiểu dữ liệu trực tiếp từ bàn phím
ma_benh_nhan = input("Nhập mã bệnh nhân (Ví dụ: BN999): ")
nhiet_do = float(input("Nhập nhiệt độ cơ thể (°C): "))
nhip_tim = int(input("Nhập nhịp tim (nhịp/phút): "))

print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print(f"Mã bệnh nhân: {ma_benh_nhan}")
print(f"Nhiệt độ cơ thể: {nhiet_do} | Kiểu dữ liệu: {type(nhiet_do)}")
print(f"Nhịp tim: {nhip_tim} | Kiểu dữ liệu: {type(nhip_tim)}")