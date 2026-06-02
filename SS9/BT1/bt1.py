
# - Sau khi chạy lệnh delivery_orders.insert(0, "GE000"), danh sách thay đổi thế nào?
# Trả lời: Phần tử "GE000" được chèn vào đầu tiên (index 0). Các phần tử cũ bị đẩy sang phải, index tăng lên 1.

# - Vì sao dòng 'delivery_orders[1] = "GE002-UPDATED"' lại sửa sai đơn hàng?
# Trả lời: Vì sau khi chèn "GE000" vào đầu, "GE002" đã bị đẩy xuống index 2 rồi. Ghi đè vào index 1 sẽ làm mất mã "GE001".

# - Sau khi chèn "GE000" vào đầu danh sách, "GE002" nằm ở index nào?
# Trả lời: Index 2.

# - Vì sao dòng 'delivery_orders.remove(3)' gây lỗi?
# Trả lời: Vì hàm remove() tìm theo giá trị để xóa chứ không tìm theo vị trí. Trong list không có chuỗi hay số nào là 3 cả.

# - Phương thức remove() xóa phần tử theo giá trị hay theo vị trí?
# Trả lời: Theo giá trị.

# - Muốn xóa đơn hàng "GE003-CANCEL", cần viết lệnh như thế nào?
# Trả lời: delivery_orders.remove("GE003-CANCEL")

# - Phương thức pop() có tác dụng gì?
# Trả lời: Xóa phần tử cuối cùng ra khỏi list và trả về giá trị của phần tử đó.

# - Vì sao chương trình báo lỗi khi in biến transferred_order?
# Trả lời: Vì lúc dùng pop() mình không gán nó vào biến, nên máy không hiểu transferred_order là gì.

# - Muốn lưu lại đơn hàng vừa lấy ra bằng pop(), cần viết lệnh như thế nào?
# Trả lời: transferred_order = delivery_orders.pop()


# 1. Khởi tạo danh sách ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# 2. Thêm GE004 vào cuối
delivery_orders.append("GE004")

# 3. Chèn GE000 vào đầu
delivery_orders.insert(0, "GE000")

# 4. Sửa đúng vị trí của GE002
delivery_orders[2] = "GE002-UPDATED"

# 5. Xóa theo đúng giá trị chuỗi
delivery_orders.remove("GE003-CANCEL")

# 6. Lấy phần tử cuối ra và gán vào biến để lưu lại
transferred_order = delivery_orders.pop()

# 7. In kết quả kiểm tra
print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)