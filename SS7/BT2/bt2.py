# 1. Vì sao transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu?
#    - Vì chuỗi (string) trong Python là kiểu dữ liệu bất biến (immutable). Các phương thức như .strip() 
#      chỉ trả về một chuỗi mới chứ không thể sửa đổi giá trị trực tiếp trên biến cũ. Muốn lưu thay đổi phải gán lại.

# 2. Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?
#    - Chuỗi thực tế được phân tách bằng ký tự dấu gạch đứng '|'.

# 3. Vì sao transaction.split("-") là sai?
#    - Vì dấu gạch ngang '-' chỉ xuất hiện bên trong mã khóa học (PYTHON-01) chứ không phải ký tự phân tách các cột.

# 4. Sau khi tách bằng sai delimiter, dữ liệu trong parts bị lệch như thế nào?
#    - Chuỗi bị cắt sai vị trí và chỉ chia làm 2 phần tại chữ PYTHON và số 01, làm mất cấu trúc 4 cột cần quản lý.

# 5. Vì sao cần .strip() lại từng phần sau khi split()?
#    - Vì sau khi split(), các khoảng trắng thừa nằm ở hai đầu của từng phân đoạn nhỏ vẫn còn tồn tại (ví dụ: " paid ").

# 6. Vì sao cần chuyển amount từ chuỗi sang số trước khi định dạng tiền?
#    - Vì Python chỉ hỗ trợ toán thức định dạng hiển thị dấu phẩy hàng nghìn (:,) trên các kiểu dữ liệu số (int, float).



# Bước 1: Khai báo dữ liệu đầu vào chứa lỗi khoảng trắng và chữ hoa/thường lộn xộn
transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

# Bước 2: Loại bỏ khoảng trắng 2 đầu chuỗi tổng, rồi tách thành danh sách dựa trên dấu phân tách chuẩn '|'
parts = transaction.strip().split("|")

name = parts[0].strip().title()      # Viết hoa chữ cái đầu mỗi từ
course = parts[1].strip()            # Giữ nguyên mã khóa học sau khi làm sạch
amount = int(parts[2].strip())       # Ép kiểu sang số nguyên để chuẩn bị định dạng tiền tệ
status = parts[3].strip().upper()    # Chuyển toàn bộ thành chữ in hoa

print(f"Học viên: {name}")
print(f"Khóa học: {course}")
print(f"Số tiền: {amount:,} VND")
print(f"Trạng thái: {status}")