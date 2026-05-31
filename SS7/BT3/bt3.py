
# 1. Vì sao transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu?
# -> Vì chuỗi (string) trong Python là kiểu dữ liệu bất biến (immutable).
# -> Các phương thức như .strip() chỉ trả về một chuỗi mới đã được xử lý chứ không thể
#    sửa đổi trực tiếp giá trị của biến cũ. Muốn lưu thay đổi thì phải gán ngược lại cho biến.

# 2. Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?
# -> Chuỗi giao dịch thực tế được phân tách bằng ký tự dấu gạch đứng '|'.

# 3. Vì sao transaction.split("-") là sai?
# -> Vì dấu gạch ngang '-' chỉ là một phần ký tự nằm trong mã khóa học (PYTHON-01),
#    chứ không phải là ký tự dùng để phân tách giữa các trường dữ liệu với nhau.

# 4. Sau khi tách bằng sai delimiter, dữ liệu trong parts bị lệch như thế nào?
# -> Chuỗi sẽ bị cắt sai cấu trúc và chỉ chia thành 2 phần tại vị trí dấu gạch ngang:
#    Phần 1: từ đầu chuỗi cho đến chữ 'PYTHON'
#    Phần 2: từ số '01' cho đến hết chuỗi. Làm mất hoàn toàn cấu trúc 4 cột ban đầu.

# 5. Vì sao cần .strip() lại từng phần sau khi split()?
# -> Vì phương thức split() chỉ cắt chuỗi tại ký tự '|', các khoảng trắng thừa nằm ở
#    hai đầu của các phân đoạn nhỏ vẫn bị giữ lại (ví dụ: "  15000000  " hoặc " paid  ").

# 6. Vì sao cần chuyển amount từ chuỗi sang số trước khi định dạng tiền?
# -> Vì cú pháp định dạng thêm dấu phẩy hàng nghìn (:,) trong f-string của Python chỉ
#    hỗ trợ và hoạt động trên các kiểu dữ liệu số (int, float) chứ không chạy trên chuỗi.



# Bước 1: Khai báo chuỗi giao dịch đầu vào chứa dữ liệu thô
transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

# Bước 2: Loại bỏ khoảng trắng 2 đầu chuỗi tổng và tách danh sách bằng dấu '|'
parts = transaction.strip().split("|")

# Bước 3: Trích xuất, làm sạch khoảng trắng thừa và chuẩn hóa định dạng từng thuộc tính
name = parts[0].strip().title()      # Viết hoa chữ cái đầu của từng từ
course = parts[1].strip()            # Giữ nguyên mã khóa học sau khi làm sạch
amount = int(parts[2].strip())       # Ép kiểu sang số nguyên để định dạng tiền tệ
status = parts[3].strip().upper()    # Chuyển toàn bộ thành chữ in hoa

# Bước 4: Hiển thị báo cáo giao dịch chuẩn hóa theo đúng yêu cầu nghiệp vụ
print(f"Học viên: {name}")
print(f"Khóa học: {course}")
print(f"Số tiền: {amount:,} VND")   # Sử dụng toán thức :, để tự động thêm dấu phẩy hàng nghìn
print(f"Trạng thái: {status}")