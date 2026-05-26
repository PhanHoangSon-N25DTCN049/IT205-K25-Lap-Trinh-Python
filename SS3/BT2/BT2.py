""" 
Khi nhập số ngày công = 0 cho nhân viên, luồng thực thi của chương trình cũ diễn ra như sau:
Hệ thống khớp điều kiện if (hoặc elif tùy cách viết cũ) dành cho trường hợp bằng 0 và in ra dòng cảnh báo lên màn hình HR.
Tuy nhiên, do các câu lệnh tính thưởng và gửi email tiếp theo được đặt ngay phía dưới (cùng cấp hoặc nằm ngoài khối điều khiển rẽ nhánh) mà không có bất kỳ lệnh điều hướng hay chặn lại nào.
Chương trình tiếp tục chạy tuần tự từ trên xuống dưới, lấy giá trị ngày công bằng 0 để tính toán (ra 0 VNĐ) và thực hiện hàm gửi email "Chúc mừng...".

Vấn đề nằm ở chỗ khối lệnh tính thưởng và gửi email lẽ ra chỉ được chạy khi ngày công hợp lệ (> 0).
Để sửa lỗi, ta cần dùng từ khóa continue ngay trong nhánh cảnh báo lỗi (ngày công == 0) để lập tức bỏ qua toàn bộ các câu lệnh phía sau
và nhảy sang lượt lặp tiếp theo của nhân viên mới.
"""

# Giả định danh sách số ngày công của các nhân viên cần xét duyệt
work_days_list = [22, 0, 25]  

print("--- HỆ THỐNG XÉT DUYỆT THƯỞNG TẾT ---")

for i, work_days in enumerate(work_days_list, start=1):
    print(f"\n[Nhân viên {i}] Số ngày công: {work_days}")
    
    # Bước 1: Kiểm tra bẫy dữ liệu nghỉ không lương cả tháng (0 ngày công)
    if work_days == 0:
        print("CẢNH BÁO (HR): Nhân viên nghỉ không lương cả tháng. Không tính thưởng!")
        continue  # Bỏ qua các bước dưới, lập tức chuyển sang nhân viên tiếp theo
        
    # Bước 2: Kiểm tra dữ liệu không hợp lệ (nếu có)
    if work_days < 0:
        print("LỖI: Số ngày công không được âm!")
        continue

    # Bước 3: Tính thưởng và gửi email (Chỉ chạy khi ngày công > 0 nhờ lệnh continue ở trên)
    bonus = work_days * 150000  # Ví dụ mức thưởng 150.000 VNĐ / ngày công
    print(f"-> Hệ thống: Đã tính thưởng ({bonus:,} VNĐ).")
    print(f"-> Email gửi đi: 'Chúc mừng bạn nhận được {bonus:,} VNĐ tiền thưởng!'")