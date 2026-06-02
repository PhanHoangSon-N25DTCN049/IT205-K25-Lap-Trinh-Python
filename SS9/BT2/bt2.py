
# - Sau khi chạy lệnh express_orders.insert(0, "GE100-FAST"), danh sách thay đổi thế nào?
# Trả lời: Phần tử "GE100-FAST" được chèn vào đầu danh sách (index 0). Các phần tử còn lại bị đẩy sang phải, index của chúng tăng lên 1.

# - Vì sao dòng 'express_orders[1] = "GE102-UPDATED"' lại sửa nhầm "GE101" thay vì "GE102-WRONG"?
# Trả lời: Ban đầu "GE101" ở index 0, "GE102-WRONG" ở index 1. Nhưng sau khi chèn "GE100-FAST" vào đầu, "GE101" bị đẩy xuống index 1, còn "GE102-WRONG" bị đẩy xuống index 2. Ghi vào index 1 sẽ ghi đè nhầm lên "GE101".

# - Sau khi chèn "GE100-FAST" vào đầu danh sách, "GE102-WRONG" nằm ở index nào?
# Trả lời: Index 2.

# - Vì sao dòng 'express_orders.pop(3)' không xóa đúng đơn hàng bị hủy?
# Trả lời: Lúc này phần tử "GE103-CANCEL" đang nằm ở index 4 chứ không phải index 3. Gọi pop(3) sẽ xóa nhầm phần tử "GE104".

# - Nếu muốn xóa đúng đơn hàng "GE103-CANCEL", nên dùng remove() như thế nào?
# Trả lời: express_orders.remove("GE103-CANCEL")

# - Phương thức pop() không truyền index sẽ lấy phần tử ở đâu trong danh sách?
# Trả lời: Lấy phần tử ở cuối cùng danh sách.

# - Vì sao dòng 'current_order = express_orders.pop()' lấy sai đơn hàng đang giao?
# Trả lời: Đơn hỏa tốc "GE100-FAST" nằm ở đầu danh sách (index 0). Dùng pop() không truyền tham số sẽ lấy phần tử ở cuối danh sách.

# - Muốn lấy đơn hàng đầu tiên trong danh sách ra để giao, cần viết lệnh như thế nào?
# Trả lời: current_order = express_orders.pop(0)

# - Muốn chương trình cho ra kết quả đúng, cần sửa lại những dòng nào?
# Trả lời: Sửa index khi cập nhật đơn hàng, dùng remove() để xóa đơn hủy, và truyền index 0 vào hàm pop() để lấy đơn đầu tiên.


# 1. Khởi tạo danh sách ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# 2. Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# 3. Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# 4. Sửa đúng vị trí của GE102-WRONG (lúc này đã bị đẩy xuống index 2)
express_orders[2] = "GE102-UPDATED"

# 5. Xóa đơn hàng bị khách hủy bằng phương thức remove
express_orders.remove("GE103-CANCEL")

# 6. Lấy đơn hàng đầu tiên ra để bắt đầu giao bằng pop(0)
current_order = express_orders.pop(0)

# 7. In kết quả kiểm tra đầu ra chuẩn hóa
print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)