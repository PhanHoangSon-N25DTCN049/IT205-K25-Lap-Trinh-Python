
# Khởi tạo một tuple chứa thông tin sản phẩm
# Tuple này có tổng cộng 4 phần tử (Mã SP, Tên, Size, Giá)
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# - Phân tích: Phần tử "SP001" thực chất nằm ở index 0 vì Python đếm số thứ tự từ 0.
# - Do đó dòng cũ `product_info[1]` lấy ra tên áo chứ không phải mã.
# -> Sửa lại: Đổi index từ 1 thành 0.
product_code = product_info[0]


# -  Phần tử "Áo polo nam" nằm ở index 1.
# - Dòng cũ dùng `product_info[2]` là nhảy sang phần tử thứ 3 (kích cỡ "Size L") mất rồi.
# -> Đổi index từ 2 thành 1.
product_name = product_info[1]


# -  Dòng cũ dùng `product_info.length()` bị lỗi 'AttributeError' 
#   vì trong Python, kiểu dữ liệu tuple không có phương thức .length().
# - Muốn đếm số lượng phần tử của tuple thì phải dùng hàm build-in len() truyền tuple vào.
# -> Dùng len(product_info) thay vì .length()
product_length = len(product_info)

# - Phân tích: Dòng cũ `product_info[3] = 279000` hoàn toàn không hợp lệ.
#   Đặc tính của Tuple là Immutable (không thể chỉnh sửa, thêm bớt phần tử sau khi tạo).
# - Để giải quyết bài toán cập nhật giá bán từ 299000 thành 279000, 
#   mình sẽ chuyển tuple này sang dạng list (kiểu dữ liệu cho phép sửa),
#   thay đổi giá trị ở vị trí số 3, rồi ép kiểu ngược lại thành tuple mới.
# -> Sửa lại: 
temp_list = list(product_info)  # Chuyển qua list để sửa
temp_list[3] = 279000           # Sửa giá bán ở index 3
product_info = tuple(temp_list) # Ép kiểu ngược lại về tuple


print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)