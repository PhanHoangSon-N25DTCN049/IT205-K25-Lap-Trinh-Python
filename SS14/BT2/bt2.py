"""
Phân tích lỗi hệ thống tích điểm. Biến total_points được khai báo ở dòng 2 là biến toàn cục (global) do được đặt bên ngoài tất cả các hàm,
có thể được truy cập từ mọi nơi. Về thông báo lỗi UnboundLocalError,
nguyên nhân là do bên trong hàm có chứa phép gán total_points = total_points + points_earned.
Khi phát hiện phép gán này, Python sẽ tự động coi total_points là một biến cục bộ mới hoàn toàn chưa có giá trị.
Việc cố gắng lấy biến cục bộ chưa được khởi tạo này ra để thực hiện phép cộng sẽ gây ra lỗi tham chiếu trước khi gán.
Trường hợp chỉ cần đọc biến total_points bên trong hàm bằng lệnh print mà không thực hiện gán lại thì chương trình sẽ hoạt động bình thường,
vì Python sẽ tự động tìm đến biến toàn cục để lấy giá trị. Nếu muốn sửa lỗi theo hướng giữ nguyên cấu trúc cũ (cách 1),
cần dùng từ khóa global để báo cho Python biết đang muốn thao tác với biến bên ngoài bằng dòng lệnh: global total_points.
Tuy nhiên, theo chuẩn clean code (cách 2),
hàm nên nhận các giá trị đầu vào thông qua tham số và sử dụng lệnh return để trả về kết quả tính toán cuối cùng.
"""

total_points = 100

def add_reward_points(current_points, points_earned):
    new_total = current_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")
    return new_total

total_points = add_reward_points(total_points, 50)

print("Tổng điểm hiện tại của khách hàng:", total_points)