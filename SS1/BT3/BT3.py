# Input: * Họ tên bệnh nhân (Kiểu str).
# Mã bệnh án (Kiểu str).
# Khoa/Phòng khám chỉ định (Kiểu str).
# Output: Chuỗi thông tin chuẩn hóa theo định dạng: Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám]

# Sử dụng hàm input() để tiếp nhận dữ liệu chuỗi từ bàn phím.
# Sử dụng toán tử cộng chuỗi + để nối các biến văn bản với các chuỗi định dạng cố định thành một dòng đầu ra duy nhất.


# BƯỚC 1: Nhập dữ liệu ho_ten, ma_ba, khoa_phong thông qua hàm input().
# BƯỚC 2: Sử dụng toán tử + để nối chuỗi theo đúng cấu trúc yêu cầu.
# BƯỚC 3: In kết quả ra màn hình bằng hàm print().

# Tiếp nhận dữ liệu đầu vào từ Lễ tân
ho_ten = input("Nhập họ và tên bệnh nhân: ")
ma_ba = input("Nhập mã bệnh án (ví dụ: BN1024): ")
khoa_phong = input("Nhập Khoa/Phòng khám chỉ định: ")


# Xuất kết quả theo đúng định dạng yêu cầu trong ảnh
print("Bệnh nhân: " + ho_ten + " - Mã BA: " + ma_ba + " - Chuyển tới: " + khoa_phong);