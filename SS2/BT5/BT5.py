""" 
patient_name (String): "Nhập họ và tên bệnh nhân (VD: Nguyen Van A): "

patient_age (Integer): "Nhập tuổi bệnh nhân (VD: 25): "

spo2_level (Integer): "Nhập nồng độ oxy trong máu SpO2 (%) (VD: 96): "

heart_rate (Integer): "Nhập nhịp tim (nhịp/phút) (VD: 80): "

has_insurance (String): "Bệnh nhân có thẻ BHYT không? (yes/no): "

Nhập liệu: Thu thập 5 thông tin trên từ bàn phím.
Phân luồng y khoa: * spo2_level < 90 hoặc heart_rate > 120 -> Báo động ĐỎ.
90 <= spo2_level <= 95 hoặc 100 <= heart_rate <= 120 -> Báo động VÀNG.
Còn lại -> XANH.
Tính tạm ứng: patient_age < 6 hoặc patient_age >= 80 -> 0 VNĐ.
has_insurance == "yes" -> 250,000 VNĐ.
Còn lại -> 500,000 VNĐ.
Xuất kết quả: In Phiếu khám bệnh và Log hệ thống (type()).
"""

# --- KHỐI 1: NHẬP DỮ LIỆU ---
print("=== KIOSK PHÂN LUỒNG TỰ PHỤC VỤ ===")
patient_name = input("Nhập họ và tên bệnh nhân (VD: Nguyen Van A): ")
patient_age = int(input("Nhập tuổi bệnh nhân (VD: 25): "))
spo2_level = int(input("Nhập nồng độ oxy trong máu SpO2 (%) (VD: 96): "))
heart_rate = int(input("Nhập nhịp tim (nhịp/phút) (VD: 80): "))
has_insurance = input("Bệnh nhân có thẻ BHYT không? (yes/no): ").strip().lower()

# --- KHỐI 2: PHÂN LUỒNG Y KHOA ---
if spo2_level < 90 or heart_rate > 120:
    triage_status = "ĐỎ (Cấp cứu khẩn)"
elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
    triage_status = "VÀNG (Theo dõi sát)"
else:
    triage_status = "XANH (Khám thường)"

# --- KHỐI 3: TÍNH TẠM ỨNG VIỆN PHÍ ---
if patient_age < 6 or patient_age >= 80:
    advance_payment = 0
elif has_insurance == "yes":
    advance_payment = 250000
else:
    advance_payment = 500000

# --- KHỐI 4: IN PHIẾU KHÁM BỆNH ---
print("\n" + "="*40)
print("       PHIẾU KHÁM BỆNH ĐIỆN TỬ       ")
print("="*40)
print(f"Họ tên bệnh nhân : {patient_name}")
print(f"Tuổi             : {patient_age} tuổi")
print(f"Chỉ số sinh hiệu : SpO2 {spo2_level}% - Nhịp tim {heart_rate} bpm")
print(f"PHÂN LUỒNG Y KHOA: {triage_status}")
print(f"TẠM ỨNG VIỆN PHÍ : {advance_payment:,} VNĐ")
print("="*40)

# --- KHỐI 5: LOG HỆ THỐNG ---
print("\n" + "#"*40)
print("               SYSTEM LOG               ")
print("#"*40)
print(f"patient_name   : {type(patient_name)}")
print(f"patient_age    : {type(patient_age)}")
print(f"spo2_level     : {type(spo2_level)}")
print(f"heart_rate     : {type(heart_rate)}")
print(f"has_insurance  : {type(has_insurance)}")
print(f"triage_status  : {type(triage_status)}")
print(f"advance_payment: {type(advance_payment)}")
print("#"*40)
