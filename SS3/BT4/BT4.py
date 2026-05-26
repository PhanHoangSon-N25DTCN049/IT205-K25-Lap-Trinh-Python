""" 
Dữ liệu đầu vào (Input): * Chuỗi ký tự nhập từ bàn phím đại diện cho số lượng nhân sự mới, sau đó được ép kiểu sang số nguyên (int).
Dữ liệu đầu ra (Output):Khi nhập số $\le 0$: In thông báo lỗi "[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0."
và yêu cầu nhập lại.Khi nhập số $> 0$: In thông báo thành công "[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho X nhân sự mới!" và kết thúc chương trình.


Giải pháp 1: Sử dụng vòng lặp while True kết hợp break (Vòng lặp vô hạn có điều kiện dừng)Thiết lập một vòng lặp vô hạn.
Bên trong vòng lặp, yêu cầu người dùng nhập số lượng. 
Kiểm tra nếu số lượng $> 0$ thì dùng lệnh break để thoát khỏi vòng lặp, ngược lại thì báo lỗi để vòng lặp tiếp tục chạy.
Giải pháp 2: Sử dụng vòng lặp kiểm tra điều kiện biến kiểm soát while số_lượng <= 0Khởi tạo biến số lượng bằng một giá trị mặc định không hợp lệ (ví dụ: 0 hoặc -1).
Vòng lặp chạy với điều kiện chừng nào biến này còn $\le 0$. Bên trong vòng lặp sẽ liên tục cập nhật giá trị nhập từ người dùng.


Tiêu chí	                                Giải pháp 1: while True + break	                                            Giải pháp 2: while kiểm tra biến điều kiện
Độ ngắn gọn của code	                    Ngắn gọn hơn, không cần khai báo biến mồi trước vòng lặp.	                Dài hơn một chút do phải khởi tạo giá trị giả lập cho biến trước khi vào vòng lặp.
Mức độ dễ hiểu (Gần ngôn ngữ tự nhiên)	    Rất tự nhiên: "Cứ lặp liên tục cho đến khi (break) nhập đúng số dương".	    Hơi khiên cưỡng ở bước đầu vì phải ép biến nhận giá trị lỗi (0 hoặc -1) để mồi cho vòng lặp chạy.
"""

print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

# Sử dụng vòng lặp vô hạn để ép HR nhập dữ liệu hợp lệ
while True:
    # Thu thập dữ liệu đầu vào và ép kiểu sang số nguyên
    new_employees_count = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    
    # Xử lý các Edge Cases (Bẫy dữ liệu số âm và số 0)
    if new_employees_count <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")
        # Không cần lệnh gì thêm, vòng lặp sẽ tự động quay lại dòng input
    else:
        # Trường hợp số dương hợp lệ -> In thông báo thành công và thoát vòng lặp
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {new_employees_count} nhân sự mới!")
        break

print("————— CHƯƠNG TRÌNH KẾT THÚC —————")