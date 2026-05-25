# hàm input trong python sẽ mặc định lưu dữ liệu dạng string nên khi muốn lưu đữ liệu dạng float thì phải thực hiện ép kiêu dữ liệu
# ở bài này đoạn code chưa được ép kiểu dữ liệu nên khi kiểm ttra sẽ trả về kiểu string

print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân : ")
weight = float(input("Nhập cân nặng bệnh nhân : "));

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : ", name_patient)
print("Cân nặng đã nhập : ", weight)

print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))