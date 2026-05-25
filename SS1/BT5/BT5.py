# patient_name	Họ và tên bệnh nhân	str
# patient_id	Mã số bệnh nhân	str
# body_temperature	Nhiệt độ cơ thể	float
# heart_rate	Nhịp tim	int
# body_weight	Cân nặng float

# BƯỚC 1: [Khối Khởi tạo] Hiển thị lời chào đón thân thiện của Kiosk.
# BƯỚC 2: [Khối Thu thập] Giao tiếp với người dùng qua các câu hỏi input() chứa hướng dẫn chi tiết và ví dụ.
# BƯỚC 3: [Khối Xử lý] Loại bỏ khoảng trắng thừa và ép kiểu ngầm dữ liệu sinh hiệu sang int/float.
# BƯỚC 4: [Khối Hiển thị] Xuất bản "Phiếu Khám Bệnh Điện Tử" trực quan và in kèm "Log hệ thống" cho IT.


print("=== KIOSK Y TẾ TỰ ĐỘNG ===")

patient_name = input("Nhập họ và tên (Ví dụ: Nguyễn Văn A): ")
patient_id = input("Nhập mã bệnh nhân (Ví dụ: BN2026): ")
body_temperature = float(input("Nhập nhiệt độ cơ thể (°C) (Ví dụ: 36.5): "))
heart_rate = int(input("Nhập nhịp tim (nhịp/phút) (Ví dụ: 80): "))
body_weight = float(input("Nhập cân nặng (kg) (Ví dụ: 65.2): "))

print("\n" + "="*40 + "\n        PHIẾU KHÁM BỆNH ĐIỆN TỬ\n" + "="*40)
print(f"Bệnh nhân: {patient_name} | Mã BA: {patient_id}")
print(f"Sinh hiệu: {body_temperature}°C - {heart_rate} bpm - {body_weight}kg")
print("="*40 + "\nTrạng thái: ĐÃ TIẾP NHẬN THÀNH CÔNG\n" + "="*40)

# 4.2. Log hệ thống dành cho bộ phận IT
print(">>> SYSTEM LOGS FOR IT:")
print(f"patient_name: {patient_name} ({type(patient_name).__name__})")
print(f"patient_id: {patient_id} ({type(patient_id).__name__})")
print(f"body_temperature: {body_temperature} ({type(body_temperature).__name__})")
print(f"heart_rate: {heart_rate} ({type(heart_rate).__name__})")
print(f"body_weight: {body_weight} ({type(body_weight).__name__})")