# Dữ liệu đầu vào (Input):
# Tên bệnh nhân, Giới tính, Số điện thoại, Email, Triệu chứng ban đầu: Kiểu chuỗi (str).
# Năm sinh: Ép sang kiểu số nguyên (int).
# Chi phí khám: Ép sang kiểu số thực (float).
# Dữ liệu tự động sinh: Mã bệnh nhân định dạng BN + Năm sinh + 3 số ngẫu nhiên.
# Dữ liệu đầu ra (Output): Hiển thị dạng "thẻ bệnh nhân" chứa toàn bộ thông tin cùng với kiểu dữ liệu kiểm tra bằng hàm type().

# BƯỚC 1: Import thư viện random để lấy số ngẫu nhiên.
# BƯỚC 2: Nhập và ép kiểu trực tiếp các thông tin bệnh nhân từ bàn phím.
# BƯỚC 3: Sinh ngẫu nhiên một số từ 100 đến 999. Khởi tạo mã BN bằng f-string.
# BƯỚC 4: In ra giao diện "THẺ THÔNG TIN BỆNH NHÂN" kèm kiểm tra type() cho từng trường.

import random
print("=== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ===")
# 1. Nhập thông tin và ép kiểu dữ liệu trực tiếp
ten_bn = input("Nhập tên bệnh nhân: ")
gioi_tinh = input("Nhập giới tính: ")
nam_sinh = int(input("Nhập năm sinh: "))
sdt = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
trieu_chung = input("Nhập triệu chứng ban đầu: ")
chi_phi = float(input("Nhập chi phí khám: "))

# 2. Tạo mã bệnh nhân tự động (Ví dụ: BN1998456)
so_ngau_nhien = random.randint(100, 999)
ma_bn = f"BN{nam_sinh}{so_ngau_nhien}"

# 3. Hiển thị thẻ bệnh nhân và kiểm tra kiểu dữ liệu
print("\n" + "="*50)
print("              THẺ THÔNG TIN BỆNH NHÂN             ")
print(f"Mã bệnh nhân   : {ma_bn} | Kiểu: {type(ma_bn)}")
print(f"Tên bệnh nhân  : {ten_bn} | Kiểu: {type(ten_bn)}")
print(f"Giới tính      : {gioi_tinh} | Kiểu: {type(gioi_tinh)}")
print(f"Năm sinh       : {nam_sinh} | Kiểu: {type(nam_sinh)}")
print(f"Số điện thoại  : {sdt} | Kiểu: {type(sdt)}")
print(f"Email          : {email} | Kiểu: {type(email)}")
print(f"Triệu chứng    : {trieu_chung} | Kiểu: {type(trieu_chung)}")
print(f"Chi phí khám   : {chi_phi:,} VNĐ | Kiểu: {type(chi_phi)}")
