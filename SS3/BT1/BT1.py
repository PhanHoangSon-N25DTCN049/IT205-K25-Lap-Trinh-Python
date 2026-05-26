""" 
Đoạn code của thực tập sinh mắc phải lỗi khởi tạo lại giá trị biến tích lũy bên trong vòng lặp và gán đè thay vì cộng dồn. Luồng thực thi bị sai như sau:
Ở mỗi vòng lặp, câu lệnh total_budget = int(input(...)) được gọi.
Bản chất của toán tử = là toán tử gán (overwrite). Nó xóa sạch giá trị cũ của nhân viên trước đó và ghi đè giá trị của nhân viên mới vào.
Kết quả là khi vòng lặp kết thúc, biến total_budget chỉ giữ duy nhất giá trị của nhân viên cuối cùng (lần nhập thứ 3).
Lỗi kinh điển rút ra
Lỗi 1: Đặt biến tích lũy (total_budget) bên trong vòng lặp khiến nó bị reset liên tục.
Lỗi 2: Dùng toán tử gán = thay vì toán tử cộng dồn +=.
"""

# Khởi tạo biến tổng ngân sách bên ngoài vòng lặp để tích lũy dữ liệu
total_budget = 0
num_of_employees = 3

print("--- NHẬP LƯƠNG NHÂN VIÊN THỜI VỤ ---")

# Sử dụng vòng lặp để thu thập thông tin 3 nhân viên
for i in range(1, num_of_employees + 1):
    salary = int(input(f"Nhập lương nhân viên {i} (VNĐ): "))
    total_budget += salary  # Cộng dồn vào tổng ngân sách (tương đương total_budget = total_budget + salary)

# In kết quả tổng quỹ lương sau khi vòng lặp kết thúc
print(f"Tổng ngân sách cần chuẩn bị: {total_budget:,} VNĐ")