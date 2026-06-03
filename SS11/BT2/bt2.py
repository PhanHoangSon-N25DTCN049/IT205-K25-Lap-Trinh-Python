# ==============================================================================
# BÀI TẬP: LỖI XỬ LÝ THÔNG TIN NHÂN VIÊN (YODY)
# Sinh viên thực hiện phần phân tích và fix lỗi trực tiếp trong file code
# ==============================================================================

# --- PHẦN 1: KHỞI TẠO DATA BAN ĐẦU ---
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}


# --- PHẦN 2: PHÂN TÍCH LỖI VÀ FIX CODE ---

#  Dictionary employee gồm những key nào?
#   -> Trả lời: Gồm các key: "employee_id", "full_name", "department", "status".

#  Vì sao dòng sau gây lỗi? `employee_id = employee[0]`
#   -> Trả lời: Vì dict lưu theo dạng key-value chứ không dùng index giống list. 
#      Viết employee[0] thì Python sẽ đi tìm cái key tên là số 0, không thấy nên quăng lỗi KeyError.
#  Dictionary có truy cập phần tử bằng index giống list không?
#   -> Trả lời: Không.
#  Muốn lấy mã nhân viên "NV001", cần viết lệnh như thế nào?
#   -> Trả lời: Gọi đúng tên key: employee["employee_id"]
employee_id = employee["employee_id"]


#  Vì sao dòng sau gây lỗi? `full_name = employee["name"]`
#   -> Trả lời: Do trong dict ban đầu làm gì có key nào tên là "name".
#  Key đúng để lấy họ tên nhân viên là gì?
#   -> Trả lời: Phải là "full_name".
full_name = employee["full_name"]


#  Vì sao dòng sau chưa cập nhật đúng trạng thái nhân viên? `employee["employee_status"] = "official"`
#   -> Trả lời: Vì key gốc của nó là "status". Viết như trên là đang tự tạo thêm một key mới tinh 
#      tên là "employee_status" chứ không sửa được data của key cũ.
#  Muốn cập nhật trạng thái nhân viên, cần dùng key nào?
#   -> Trả lời: Dùng key "status".
employee["status"] = "official"


#  Vì sao dòng sau gây lỗi? `employee.append("base_salary", 15000000)`
#   -> Trả lời: Hàm .append() là của List, thằng Dict không có phương thức này.
#  Dictionary có phương thức append() không?
#   -> Trả lời: Không.
#  Muốn thêm lương cơ bản base_salary bằng 15000000, cần viết lệnh như thế nào?
#   -> Trả lời: Gán thẳng tên key mới vào: dict[key_moi] = gia_tri
employee["base_salary"] = 15000000


#  Vì sao dòng sau gây lỗi? `del employee["team"]`
#   -> Trả lời: Báo lỗi vì tìm không thấy key nào tên là "team" trong dict để xóa.
#  Muốn xóa thông tin phòng ban, cần dùng key nào?
#   -> Trả lời: Phải dùng key "department".
del employee["department"]


# --- PHẦN 3: IN KẾT QUẢ KIỂM TRA ĐẦU RA ---
print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)