# Lỗi tham chiếu bộ nhớ (Aliasing) của List
# Trong Python, khi gán biến list mới bằng list cũ (new_list = old_list), hệ thống 
# không tạo ra danh sách mới mà chỉ tạo một tham chiếu trỏ về cùng vùng nhớ. 
# Việc thay đổi list mới sẽ làm thay đổi cả list gốc, khiến thuốc bị chèn sai vào lịch sử.
# - Cách sửa: Sử dụng phương thức .copy() để tạo ra một bản sao độc lập:
#   new_prescription = old_prescription.copy()
#
# Lỗi cập nhật phần tử chuỗi trong List (String Immutable)
# Hàm replace() của String sinh ra một chuỗi mới chứ không sửa trực tiếp chuỗi gốc. 
# Do code cũ không gán lại giá trị, tên thuốc "Panadol" vẫn không được cập nhật.
# - Cách sửa: Gán chuỗi mới đè lại vào đúng vị trí (index) tương ứng trong List:
#   new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")


# Danh sách thuốc ngày hôm qua (Lịch sử bệnh án cần giữ nguyên)
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Hàm tạo và cập nhật đơn thuốc cho ngày mới
def update_prescription(old_prescription):
    # Tạo một bản sao độc lập của đơn thuốc để không ảnh hưởng đến lịch sử
    new_prescription = old_prescription.copy()
    
    # Cập nhật tên thuốc ở vị trí đầu tiên (index 0)
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    
    # Thêm thuốc mới cho ngày hôm nay
    new_prescription.append("Oresol")
    
    return new_prescription
    
# Hệ thống chạy cấp thuốc cho ngày hôm nay
today_prescription = update_prescription(yesterday_prescription)

# In kết quả
print(f"Đơn thuốc hôm qua: {yesterday_prescription}")
print(f"Đơn thuốc hôm nay: {today_prescription}")